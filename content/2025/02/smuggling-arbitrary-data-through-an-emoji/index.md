---
title: Smuggling arbitrary data through an emoji
date: 2025-02-13
extra:
  source: https://paulbutler.org/2025/smuggling-arbitrary-data-through-an-emoji/
  original_title: Smuggling arbitrary data through an emoji
---
## Summary
**摘要**:
本文主要介绍了如何利用 Unicode 编码中的变体选择器(Variation Selectors)在文本中隐藏数据的方法。Unicode 使用码位(Codepoints)来表示字符,变体选择器用于修改前一个字符的显示方式,本身不显示任何内容。作者发现可以将多个变体选择器连接起来,每个变体选择器代表一个字节的数据,从而在任何 Unicode 字符后隐藏任意字节串。文章详细解释了如何将字节转换为变体选择器,并提供了 Rust 代码示例来演示如何编码和解码数据。例如,可以将 "hello" 编码到 emoji 😊 之后,使其看起来像一个普通的 emoji,但实际包含了隐藏的数据。作者也提到了这种技术的潜在滥用风险,例如绕过内容审查和文本水印。最后,作者还探讨了大型语言模型(LLM)对此类隐藏数据的处理能力,发现虽然 tokenizer 可以保留变体选择器作为 token,但模型本身通常不愿意解码它们。

**要点总结**:
1.  Unicode 码位和变体选择器:Unicode 使用码位表示字符,变体选择器(VS-1 到 VS-256)用于修改前一个字符的显示方式,本身不显示任何内容。变体选择器分为两个范围:U+FE00..U+FE0F 和 U+E0100..U+E01EF。
2.  数据隐藏原理:通过将多个变体选择器连接在一起,每个变体选择器代表一个字节的数据,从而在任何 Unicode 字符后隐藏任意字节串。由于变体选择器在渲染时通常被忽略,因此隐藏的数据对人眼是不可见的。
3.  编码和解码方法:文章提供了 Rust 代码示例,展示了如何将字节转换为变体选择器,并将多个变体选择器连接到基本字符后进行编码。同时,也展示了如何从包含变体选择器的字符串中解码出原始字节数据。编码过程包括将每个字节转换为对应的变体选择器,解码过程则相反,将变体选择器转换回字节。
4.  潜在滥用风险:这种技术可能被用于绕过内容审查,因为隐藏的数据对人眼不可见,人类审核员可能无法检测到。此外,还可以用于文本水印,通过在文本中嵌入隐藏的标识信息,追踪泄露信息的来源。
5.  LLM 的处理能力:大型语言模型(LLM)的 tokenizer 通常会保留变体选择器作为 token,这意味着模型在理论上可以访问这些隐藏的数据。然而,大多数模型本身并不愿意尝试解码这些数据,但结合代码解释器后,某些模型能够成功解码。

## Full Content
Title: Smuggling arbitrary data through an emoji

URL Source: https://paulbutler.org/2025/smuggling-arbitrary-data-through-an-emoji/

Markdown Content:
This Hacker News [comment by GuB-42](https://news.ycombinator.com/item?id=42823876) intrigued me:

> With ZWJ (Zero Width Joiner) sequences you could in theory encode an unlimited amount of data in a single emoji.

Is it really possible to encode arbitrary data in a single emoji?

**tl;dr:** yes, although I found an approach without ZWJ. In fact, you can encode data in _any_ unicode character. This sentence has a hidden message󠅟󠅘󠄐󠅝󠅩󠄜󠄐󠅩󠅟󠅥󠄐󠅖󠅟󠅥󠅞󠅔󠄐󠅤󠅘󠅕󠄐󠅘󠅙󠅔󠅔󠅕󠅞󠄐󠅝󠅕󠅣󠅣󠅑󠅗󠅕󠄐󠅙󠅞󠄐󠅤󠅘󠅕󠄐󠅤󠅕󠅨󠅤󠄑. (Try pasting it into [this decoder](https://emoji.paulbutler.org/?mode=decode))

 Your browser does not support the video tag.

Some background
---------------

Unicode represents text as a sequence of _codepoints_, each of which is basically just a number that the Unicode Consortium has assigned meaning to. Usually, a specific codepoint is written as `U+XXXX`, where `XXXX` is a number represented as uppercase hexadecimal.

For simple latin-alphabet text, there is a one-to-one mapping between Unicode codepoints and characters that appear on-screen. For example, `U+0067` represents the character `g`.

For other writing systems, some on-screen characters may be represented by multiple codepoints. The character की (in [Devanagari script](https://en.wikipedia.org/wiki/Devanagari)) is represented by a consecutive pairing of the codepoints `U+0915` and `U+0940`.

Variation selectors
-------------------

Unicode designates 256 codepoints as “variation selectors”, named VS-1 to VS-256. These have no on-screen representation of their own, but are used to modify the presentation of the preceeding character.

Most unicode characters do not have variations associated with them. Since unicode is an evolving standard and aims to be future-compatible, variation selectors are supposed to be preserved during transformations, even if their meaning is not known by the code handling them. So the codepoint `U+0067` (“g”) followed by `U+FE01` (VS-2) renders as a lowercase “g”, exactly the same as `U+0067` alone. But if you copy and paste it, the variation selector will tag along with it.

Since 256 is exactly enough variations to represent a single byte, this gives us a way to “hide” one byte of data in any other unicode codepoint.

As it turns out, the [Unicode spec](https://www.unicode.org/versions/Unicode16.0.0/) does not specifically say anything about sequences of multiple variation selectors, except to imply that they should be ignored during rendering.

_See where I’m going with this?_

We can concatenate a sequence of variation selectors together to represent any arbitrary byte string.

For example, let’s say we want to encode the data `[0x68, 0x65, 0x6c, 0x6c, 0x6f]`, which represents the text “hello”. We can do this by converting each byte into a corresponding variation selector, and then concatenating them together.

The variation selectors are broken into two ranges of codepoints: the original set of 16 at [`U+FE00 .. U+FE0F`](https://unicode.org/charts/nameslist/n_FE00.html), and remaining 240 at [`U+E0100 .. U+E01EF`](https://unicode.org/charts/nameslist/n_E0100.html) (ranges inclusive).

To convert from a byte to a variation selector, we can do something like this Rust code:

```
fn byte_to_variation_selector(byte: u8) -> char {
    if byte < 16 {
        char::from_u32(0xFE00 + byte as u32).unwrap()
    } else {
        char::from_u32(0xE0100 + (byte - 16) as u32).unwrap()
    }
}
```

To encode a series of bytes, we can concatenate a number of these variation selectors after a base character.

```
fn encode(base: char, bytes: &[u8]) -> String {
    let mut result = String::new();
    result.push(base);
    for byte in bytes {
        result.push(byte_to_variation_selector(*byte));
    }
    result
}
```

Then to encode the bytes `[0x68, 0x65, 0x6c, 0x6c, 0x6f]`, we can run:

```
fn main() {
    println!("{}", encode('😊', &[0x68, 0x65, 0x6c, 0x6c, 0x6f]));
}
```

Which outputs

```
😊󠅘󠅕󠅜󠅜󠅟
```

It just looks like a regular emoji, but try pasting it into [the decoder](https://emoji.paulbutler.org/?mode=decode).

If we instead use the debug formatter, we see what’s going on:

```
fn main() {
    println!("{:?}", encode('😊', &[0x68, 0x65, 0x6c, 0x6c, 0x6f]));
}
```

This prints:

```
"😊\u{e0158}\u{e0155}\u{e015c}\u{e015c}\u{e015f}"
```

This reveals the characters that were “hidden” in the original output.

Decoding
--------

Decoding is similarly straightforward.

```
fn variation_selector_to_byte(variation_selector: char) -> Option<u8> {
    let variation_selector = variation_selector as u32;
    if (0xFE00..=0xFE0F).contains(&variation_selector) {
        Some((variation_selector - 0xFE00) as u8)
    } else if (0xE0100..=0xE01EF).contains(&variation_selector) {
        Some((variation_selector - 0xE0100 + 16) as u8)
    } else {
        None
    }
}

fn decode(variation_selectors: &str) -> Vec<u8> {
    let mut result = Vec::new();
    
    for variation_selector in variation_selectors.chars() {
        if let Some(byte) = variation_selector_to_byte(variation_selector) {
            result.push(byte);
        } else if !result.is_empty() {
            return result;
        }
        // note: we ignore non-variation selectors until we have
        // encountered the first one, as a way of skipping the "base
        // character".
    }

    result
}
```

To use it:

```
use std::str::from_utf8;

fn main() {
    let result = encode('😊', &[0x68, 0x65, 0x6c, 0x6c, 0x6f]);
    println!("{:?}", from_utf8(&decode(&result)).unwrap()); // "hello"
}
```

Note that the base character does not need to be an emoji – the treatment of variation selectors is the same with regular characters. It’s just more fun with emoji.

Can this be abused?
-------------------

To be clear, this is an abuse of unicode and you shouldn’t do it. If your mind is wandering to practical use cases for this, shut it down.

That said, I can think of a couple of nefarious ways this could be (ab)used:

### 1\. Sneaking data past human content filters

Since data encoded this way are invisible once rendered, a human moderator or reviewer will not know they are there.

### 2\. Watermarking text

There are techniques for using subtle variations in text to “watermark” a message, so that if it is sent to a number of people and then leaked, it’s possible to trace it to the original recipient. Variation selector sequences are a way to do this that survives most copy/pastes and allows arbitrary data density. You could go so far as to watermark _every single character_ if you wanted to.

Addendum: can an LLM decode it?
-------------------------------

Since this made it on [Hacker News](https://news.ycombinator.com/item?id=43023508), some people have asked about how LLMs deal with this hidden data.

Generally, tokenizers _do_ seem to preserve the variation selectors as tokens, so in theory the model has access to them. [OpenAI’s tokenizer](https://platform.openai.com/tokenizer) is a good sanity check of this:

![Image 3: OpenAI tokenizer](https://paulbutler.org/2025/smuggling-arbitrary-data-through-an-emoji/tokenizer.png)

Overall though, models don’t even seem willing to try decoding them internally. However, when paired with a code interpreter, some models are actually able to solve them!

Here’s an example of Gemini 2 Flash solving one in a remarkable seven seconds, using [Codename Goose](https://block.github.io/goose/) and [foreverVM](https://forevervm.com/) (disclaimer: I work on foreverVM).

Your browser does not support the video tag.

Here’s a [longer video](https://x.com/paulgb/status/1889834975853523323) of Claude solving one.

