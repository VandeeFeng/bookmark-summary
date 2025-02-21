Title: A mental model for Linux file, hard and soft links

URL Source: https://bhoot.dev/2024/on-linux-file-and-links/

Markdown Content:
I always felt bothered about my superficial understanding of inode, hard and soft links in Linux. Here I attempt to structure my learnings into a simplified mental model. Corrections are welcome.

What makes a file in Linux?
---------------------------

At the storage level, a file is a block of data. There is more to it than just that, but I won't delve deep into it.

At the filesystem level, this block of data is represented as a an abstraction called **_inode_**. Think of inode as a data structure that stores metadata about the underlying data block.

A **_pathname_** makes this pair of (inode, data block) accessible and usable for humans.

Think of the whole this way - the data block of a file lies in a lower level of abstraction than the pathname (which lives at the filesystem level). inode acts as a bridge - a representative to the data block at the filesystem level.

![Image 1](https://bhoot.dev/static/images/on-linux-file-and-links/file-structure.svg)

Components of a file. From bottom up, data block, inode, and pathname

Roughly, **file = pathname + inode + data block**.

So, when you talk about a file, you may be referring to any or all of these components.

Hard links
----------

Now, **if we think of pathnames as labels slapped on an (inode, data block) pair, then we can refer to the same inode with different labels.**

![Image 2](https://bhoot.dev/static/images/on-linux-file-and-links/hard-links.svg)

Two pathnames `/tmp/filename1` and `/home/bhoot/filename2` point to the same inode, thus representing two hard links.

In the above figure, `/tmp/filename1` and `/home/bhoot/filename2` point to the same inode. These two are _hard links_. **A hard link connects a pathname to an inode.**

The above figure can be interpreted in several ways:

1.  The pathnames point to the inode, not the other way round. Thus, a pathname is aware of the inode, but the inode is not aware of the pathname.
    
2.  At this level of abstraction, is it possible to tell which one of the two pathnames originally created the file? I think not. Hard links are supposed to be equal in status to each other.
    
3.  As a corollary to the above point, **there is always at least one hard link attached to a file**. When you create a file, say, with `touch /a/pathname`, you create a hard link between `/a/pathname` and the file's inode.
    

### Deleting a hard link

Refer to the figure above. If you do `rm /tmp/filename1`, what should happen from a sane perspective?

Should the command remove the entire _/tmp/filename1 + inode + data block_ combo? Then what happens to the other pathname `/home/bhoot/filename2` that points to the same inode?

The right way would be to preserve the integrity of the other pathname `/home/bhoot/filename2` while deleting only the targeted pathname `/tmp/filename1`.

That's what happens when you delete a file - the (hard) link between the _specified_ pathname and the inode is removed.

Similarly, `mv f1 f2` creates a new hard link `f2` & deletes the old hard link `f1`.

![Image 3](https://bhoot.dev/static/images/on-linux-file-and-links/hard-link-rm.svg)

Representation of one of the two hard links, linked to the same inode, being removed. Only the affected pathname is removed. The inode and underlying data block stay in tact.

What happens when all the hard links to a file are deleted? Now, there are no pathnames in the filesystem that refer to that data block anymore. Thus, the inode is marked for deletion, and the associated data block is orphaned.

![Image 4](https://bhoot.dev/static/images/on-linux-file-and-links/hard-link-rm-all.svg)

When all the hard links to an inode are removed, the entire file, along with its content, is removed from the filesystem.

Soft links
----------

Take a look at the following figure.

![Image 5](https://bhoot.dev/static/images/on-linux-file-and-links/soft-links.svg)

A regular file identified by the pathname `/home/bhoot/filename2` on the left-hand side. A soft link file identified by the pathname `filename3` on the right-hand side. The link file points to the regular file. Both the regular and link files have their own inode and their own data block.

The above figure shows a soft link in blue colour (its blue, right?) pointing from the link file `filename3` to the target file `/home/bhoot/filename2`. **A soft link or a symbolic link points a soft link file to a target file.**.

**Thus, a soft link links a link file to a target file. This is in contrast to a hard link, which links a pathname to an inode.**

### A soft link is a file

As we saw in the [What is a file in Linux?](https://bhoot.dev/2024/on-linux-file-and-links/#what-is-a-file-in-linux) section, a pathname is always linked to an _inode + data block_. This is true in case of a soft link, too. In the above figure, the soft link file `filename3`, which points to `/home/bhoot/filename2`, also has its own inode & a data block.

You can check the inode number associated with a pathname with `ls -i` command. **Two hard link files pointing to the same inode will print the same inode number, while a soft link file and its target file will print different inode numbers.**

```
# create a regular file
$ echo "HELLO WORLD HOW ARE YOU?" > file.txt

# create a hard link
$ ln file.txt hardlink.txt

# both hard links refer to the same inode
$ ls -i file.txt hardlink.txt 
17751620 file.txt  17751620 hardlink.txt

# create a soft link
$ ln -s file.txt softlink.txt

# inode of soft link file is different from the target file
$ ls -i file.txt softlink.txt 
17751620 file.txt  17751663 softlink.txt
```

### Contents of a soft link file

How is a soft link relationship stored? In the _data block of the soft link file_. **The content of a soft link is the pathname of the target file it points to**.

There are 2 ways to verify this:

1.  `readlink filename3` prints the content of the soft link `filename3`, which is the name of the target pathname.
    
    ```
    $ readlink filename3
    ```
    
2.  `stat --format="%s" filename3` prints the size of `filename3`, which is equal to the number of characters in the name of `/home/bhoot/filename2`.
    
    ```
    $ stat --format="%s" filename3
    ```
    

### I/O operations on a soft link file

#### Copying a soft link file

What happens when you copy a soft link file? ~Same thing as when a regular file is copied.~ Or so I thought.

```
# create a regular file
$ echo "HELLO WORLD HOW ARE YOU?" > file.txt

# check the content size of target file
$ stat --format="%s" file.txt
25

# create a soft link
$ ln -s file.txt softlink.txt

# check the size of the soft link file
$ stat --format="%s" softlink.txt
8

# copy the soft link file
$ cp softlink.txt softlink2.txt

# check the size of the new soft link file, which should be equal to the soft link file
$ stat --format="%s" softlink2.txt
25 # WAT?
```

What happened there? The `cp` command simply copied the target file instead of the link file.

~**My guess is that when those I/O operations, which involve acting on the _data block_ of a file, are ran on a soft link file, they are actually executed on the target file that the soft link file is pointed to.**~

~Thus, `cp softlink.txt softlink2.txt` would actually copy the target file. Similarly, `cat softlink.txt` would print the content of the target file. But, `mv`, which does not need to act on the underlying data block of a file, would just operate on the soft link file itself.~

**NOTE:** When I wrote the couple of struck-out paragraphs above, the purpose was only to have a _convenient logic_ of memorising how I/O operations work on soft links by default. Memorising techniques need not be technically accurate. However, I have struck it out because the logic is also blatantly inaccurate and has been rightly [called out by others](https://news.ycombinator.com/item?id=42099928). By default, `cp` sure works as described above, but `cp -P` copies the soft link itself, i.e., the soft link's inode and data block.

#### Moving a soft link file

What happens when you move a soft link file? This is more predictable. Thankfully, the same as what happens when a regular file is moved - the new pathname entry is created, while the old pathname entry is removed. Because the new pathname still points to the same old inode + data block, it also points to the same target file.

![Image 6](https://bhoot.dev/static/images/on-linux-file-and-links/soft-link-mv.svg)

Moving a soft link file replaces the old soft link's pathname with a new one. The new pathname keeps pointing to the same target file.

### Moving the target file

A more interesting question worth pondering: what happens when the _target_ file is moved or deleted? Let's go with a case of severe deletion.

![Image 7](https://bhoot.dev/static/images/on-linux-file-and-links/soft-link-rm-pointee.svg)

Moving or deleting a _target_ file is a more disruptive operation

A soft link file depends on its content to determine which file it points to. Even when the target file is deleted, the content of soft link file doesn't change, i.e., it still keeps pointing to the now deleted target file. With its purpose existing no more, the soft link thus becomes a dangling, dead link.

In closing
----------

In my mind, the terms hard link and soft link are a bit confusing in that they sound like different tools used for a similar purpose. But, **a hard link exists as a directory entry that links a pathname to an inode, while a soft link exists as a file that links its own pathname to another pathname.**

So, from the perspective of structural existence, hard links actually look softer than soft links.

Also, I'm cursing my 8-hours old self for thinking that I could wrap up this post and get it out in 3 to 4 hours.

Further reading
---------------

*   An [excellent post by Pádraig Brady](https://www.pixelbeat.org/docs/unix_links.html) also adds _reflinks_ to this perspective. In this post, I talked about stuff as if a data block is represented by exactly one inode at the filesystem level. But reflinks enable many-to-one mapping between inodes and a data block.
*   `man 7 inode`
*   `man 7 symlink`
*   `man 7 path_resolution`
