Title: Relocation generation in assemblers

URL Source: https://maskray.me/blog/2025-03-16-relocation-generation-in-assemblers

Published Time: 2025-03-16T07:00:00.000Z

Markdown Content:
MaskRay
Home
Archives
Feeds
TIL
Presentations

2025-03-16
Relocation generation in assemblers

This post explores how GNU Assembler and LLVM integrated assembler generate relocations, an important step to generate a relocatable file. Relocations identify parts of instructions or data that cannot be fully determined during assembly because they depend on the final memory layout, which is only established at link time or load time. These are essentially placeholders that will be filled in (typically with absolute addresses or PC-relative offsets) during the linking process.

Relocation generation: the basics

Symbol references are the primary candidates for relocations. For instance, in the x86-64 instruction movl sym(%rip), %eax (GNU syntax), the assembler calculates the displacement between the program counter (PC) and sym. This distance affects the instruction's encoding and typically triggers a R_X86_64_PC32 relocation, unless sym is a local symbol defined within the current section.

Both the GNU assembler and LLVM integrated assembler utilize multiple passes during assembly, with several key phases relevant to relocation generation:

Parsing phase

During parsing, the assembler builds section fragments that contain instructions and other directives. It parses each instruction into its opcode (e.g., movl) and operands (e.g., sym(%rip), %eax). It identifies registers, immediate values (like 3 in movl $3, %eax), and expressions.

Expressions can be constants, symbol refereces (like sym), or unary and binary operators (-sym, sym0-sym1). Those unresolvable at parse time-potential relocation candidates-turn into "fixups". These often skip immediate operand range checks, as shown here:

1
2
3
4
5
6
7

	
% echo 'addi a0, a0, 2048' | llvm-mc -triple=riscv64
<stdin>:1:14: error: operand must be a symbol with %lo/%pcrel_lo/%tprel_lo modifier or an integer in the range [-2048, 2047]
addi a0, a0, 2048
             ^
% echo 'addi a0, a0, %lo(x)' | llvm-mc -triple riscv64 -show-encoding
        addi    a0, a0, %lo(x)                  # encoding: [0x13,0x05,0bAAAA0101,A]
                                        #   fixup A - offset: 0, value: %lo(x), kind: fixup_riscv_lo12_i


A fixup ties to a specific location (an offset within a fragment), with its value being the expression (which must eventually evaluate to a relocatable expression).

Meanwhile, the assembler tracks defined and referenced symbols, and for ELF, it tracks symbol bindings (STB_LOCAL, STB_GLOBAL, STB_WEAK) from directives like .globl, .weak, or the rarely used .local.

Section layout phase

After parsing, the assembler arranges each section by assigning precise offsets to its fragments-instructions, data, or other directives (e.g., .line, .uleb128). It calculates sizes and adjusts for alignment. This phase finalizes symbol offsets (e.g., start: at offset 0x10) while leaving external ones for the linker.

This phase, which employs a fixed-point iteration, is quite complex. I won't go into details, but you might find Clang's -O0 output: branch displacement and size increase interesting.

Relocation decision phase

Then the assembler evaluates each fixup to determine if it can be resolved directly or requires a relocation entry. This process starts by attempting to convert fixups into relocatable expressions.

Evaluating relocatable expressions

In their most general form, relocatable expressions follow the pattern relocatin_specifier(sym_a - sym_b + offset), where

relocation_specifier: This may or may not be absent. I will explain this concept later.
sym_a is a symbol reference (the "addend")
sym_b is an optional symbol reference (the "subtrahend")
offset is a constant value

Most common cases involve only sym_a or offset (e.g., movl sym(%rip), %eax or movl $3, %eax). Only a few target architectures support the subtrahend term (sym_b). Notable exceptions include AVR and RISC-V, as explored in The dark side of RISC-V linker relaxation.

Attempting to use unsupported expression forms will result in assembly errors:

1
2
3
4
5
6
7

	
% echo -e 'movl a+b, %eax\nmovl a-b, %eax' | clang -c -xassembler -
<stdin>:1:1: error: expected relocatable expression
movl a+b, %eax
^
<stdin>:2:1: error: symbol 'b' can not be undefined in a subtraction expression
movl a-b, %eax
^

PC-relative fixups

PC-relative fixups compute their values as sym_a + offset - current_location. (I’ve skipped - sym_b, since no target I know permits a subtrahend here.)

When sym_a is a local symbol defined within the current section, these PC-relative fixups evaluate to constants. But if sym_a is a global or weak symbol in the same section, a relocation entry is generated. This ensures ELF symbol interposition stays in play.

Resolution Outcomes

The assembler's evaluation of fixups leads to one of three outcomes:

Error: When the expression isn't supported.
Resolved fixups: When the fixup evaluates to a constant, the assembler updates the relevant bits in the instruction directly. No relocation entry is needed.
Unresolved fixups: When the fixup evaluates to a relocatable expression but not a constant, the assembler
Generates an appropriate relocation (offset, type, symbol, addend).
Usually zeros out the bits in the instruction field that will be modified by the linker.

If you are interested in relocation representations in different object file formats, please check out my post Exploring object file formats.

Examples in action

Branches

1
2
3
4
5
6
7
8
9
10
11
12

	
% echo -e 'call fun\njmp fun' | clang -c -xassembler - -o - | fob -dr -
...
       0: e8 00 00 00 00                callq   0x5 <.text+0x5>
                0000000000000001:  R_X86_64_PLT32       fun-0x4
       5: e9 00 00 00 00                jmp     0xa <.text+0xa>
                0000000000000006:  R_X86_64_PLT32       fun-0x4
% echo -e 'bl fun\nb fun' | clang --target=aarch64 -c -xassembler - -o - | fob -dr -
...
       0: 94000000      bl      0x0 <.text>
                0000000000000000:  R_AARCH64_CALL26     fun
       4: 14000000      b       0x4 <.text+0x4>
                0000000000000004:  R_AARCH64_JUMP26     fun


Absolute and PC-relative symbol references

1
2
3
4
5
6

	
% echo -e 'movl a, %eax\nmovl a(%rip), %eax' | clang -c -xassembler - -o - | llvm-objdump -dr -
...
       0: 8b 04 25 00 00 00 00          movl    0x0, %eax
                0000000000000003:  R_X86_64_32S a
       7: 8b 05 00 00 00 00             movl    (%rip), %eax            # 0xd <.text+0xd>
                0000000000000009:  R_X86_64_PC32        a-0x4


(a-.)(%rip) would probably be more semantically correct but is not adopted by GNU Assembler.

Relocation specifiers

Relocation specifiers guide the assembler on how to resolve and encode expressions into instructions. They specify details like:

Whether to reference the symbol itself, its Procedure Linkage Table (PLT) entry, or its Global Offset Table (GOT) entry.
Which part of a symbol's address to use (e.g., lower or upper bits).
Whether to use an absolute address or a PC-relative one.

This concept appears across various architectures but with inconsistent terminology. The Arm architecture refers to elements like :lo12: and :lower16: as "relocation specifiers". IBM's AIX documentation also uses this term. Many GNU Binutils target documents simply call these "modifiers", while AVR documentation uses "relocatable expression modifiers".

Picking the right term was tricky. "Relocatable expression modifier" nails the idea of tweaking relocatable expressions but feels overly verbose. "Relocation modifier", though concise, suggests adjustments happen during the linker's relocation step rather than the assembler's expression evaluation. I landed on "relocation specifier" as the winner. It's clear, aligns with Arm and IBM’s usage, and fits the assembler's role seamlessly.

For example, RISC-V addi can be used with either an absolute address or a PC-relative address. Relocation specifiers %lo and %pcrel_lo could differentiate the two uses. Similarly, %hi, %pcrel_hi, and %got_pcrel_hi could differentiate the uses of lui and auipc.

1
2
3
4
5
6
7
8
9
10
11

	
# Position-dependent code (PDC) - absolute addressing
lui     a0, %hi(var)                    # Load upper immediate with high bits of symbol address
addi    a0, a0, %lo(var)                # Add lower 12 bits of symbol address

# Position-independent code (PIC) - PC-relative addressing
auipc   a0, %pcrel_hi(var)              # Add upper PC-relative offset to PC
addi    a0, a0, %pcrel_lo(.Lpcrel_hi1)  # Add lower 12 bits of PC-relative offset

# Position-independent code via Global Offset Table (GOT)
auipc   a0, %got_pcrel_hi(var)          # Calculate address of GOT entry relative to PC
ld      a0, %pcrel_lo(.Lpcrel_hi1)(a0)  # Load var's address from GOT


Why use %hi with lui if it's always paired? It's about clarify and explicitness. %hi ensures consistency with %lo and cleanly distinguishes it from from %pcrel_hi. Since both lui and auipc share the U-type instruction format, tying relocation specifiers to formats rather than specific instructions is a smart, flexible design choice.

Relocation specifier flavors

Assemblers use various syntaxes for relocation specifiers, reflecting architectural quirks and historical conventions. Below, we explore the main flavors, their usage across architectures, and some of their peculiarities.

expr@specifier

This is likely the most widespread syntax, adopted by many binutils targets, including ARC, C-SKY, Power, M68K, SuperH, SystemZ, and x86, among others. It's also used in Mach-O object files, e.g., adrp x8, _bar@GOTPAGE.

This suffix style puts the specifier after an @. It's intuitive—think sym@got. In PowerPC, operators can get elaborate, such as sym@toc@l(9). Here, @toc@l is a single, indivisible operator-not two separate @ pieces-indicating a TOC-relative reference with a low 16-bit extraction.

Parsing is loose: while both expr@specifier+expr and expr+expr@specifier are accepted (by many targets), conceptually it's just specifier(expr+expr). For example, x86 accepts sym@got+4 or sym+4@got, but don't misread—@got applies to sym+4, not just sym.

%specifier(expr)

MIPS, SPARC, and RISC-V favor this prefix style, wrapping the expression in parentheses for clarity. In MIPS, parentheses are optional, and operators can nest, like

1
2
3
4
5

	
# MIPS
addiu   $2, $2, %lo(0x12345)
addiu   $2, $2, %lo 0x12345
lui     $1, %hi(%neg(%gp_rel(main)))
ld      $1, %got_page($.str)($gp)


Like expr@specifier, the specifier applies to the whole expression. Don't misinterpret %lo(3)+sym-it resolves as sym+3 with an R_MIPS_LO16 relocation.

1
2
3

	
# MIPS
addiu   $2, $2, %lo(3)+sym  # R_MIPS_LO16  sym+0x3
addiu   $2, $2, %lo 3+sym   # R_MIPS_LO16  sym+0x3


expr(specifier)

A simpler suffix style, this is used by AArch32 for data directives. It's less common but straightforward, placing the operator in parentheses after the expression.

1
2

	
.word sym(gotoff)
.long f(FUNCDESC)


:specifier:expr

AArch32 and AArch64 adopt this colon-framed prefix notation, avoiding the confusion that parentheses might introduce.

1
2
3
4
5
6
7
8

	
// AArch32
movw    r0, :lower16:x

// AArch64
add     x8, x8, :lo12:sym

adrp    x0, :got:var
ldr     x0, [x0, :got_lo12:var]


Applying this syntax to data directives, however, could create parsing ambiguity. In both GNU Assembler and LLVM, .word :plt:fun would be interpreted as .word: plt: fun, treating .word and plt as labels, rather than achieving the intended meaning.

Recommendation

For new architectures, I'd suggest adopting %specifier expr, and never use @specifier. The % symbol works seamlessly with data directives, and during operand parsing, the parser can simply peek at the first token to check for a relocation specifier.

( %specifier(...) resembles % expansion in GNU Assembler's altmacro mode.

1
2
3

	
.altmacro
.macro m arg; .long \arg; .endm
.data; m %(1+2)

)

Anti-patterns

RISC-V favors %specifier(expr) but clings to call sym@plt for legacy reasons.

AArch64 uses :specifier:expr, yet R_AARCH64_PLT32 (.word foo@plt - .) and PAuth ABI (.quad (g + 7)@AUTH(ia,0)) cannot use : after data directives due to parsing ambiguity.

TLS symbols

When a symbol is defined in a section with the SHF_TLS flag (Thread-Local Storage), GNU assembler assigns it the type STT_TLS in the symbol table. For undefined TLS symbols, the process differs: GCC and Clang don’t emit explicit labels. Instead, assemblers identify these symbols through TLS-specific relocation specifiers in the code, deduce their thread-local nature, and set their type to STT_TLS accordingly.

1
2
3
4
5

	
// AArch64
add     x8, x8, :tprel_hi12:tls

// x86
movl    %fs:tls@TPOFF, %eax

Composed relocations

Most instructions trigger zero or one relocation, but some generate two. Often, one acts as a marker, paired with a standard relocation. For example:

PPC64 bl __tls_get_addr(x@tlsgd) pairs a marker R_PPC64_TLSGD with R_PPC64_REL24
RISC-V linker relaxation uses R_RISCV_RELAX alongside another relocation.

These marker cases tie into "composed relocations", as outlined in the Generic ABI:

If multiple consecutive relocation records are applied to the same relocation location (r_offset), they are composed instead of being applied independently, as described above. By consecutive, we mean that the relocation records are contiguous within a single relocation section. By composed, we mean that the standard application described above is modified as follows:

In all but the last relocation operation of a composed sequence, the result of the relocation expression is retained, rather than having part extracted and placed in the relocated field. The result is retained at full pointer precision of the applicable ABI processor supplement.

In all but the first relocation operation of a composed sequence, the addend used is the retained result of the previous relocation operation, rather than that implied by the relocation type.

Note that a consequence of the above rules is that the location specified by a relocation type is relevant for the first element of a composed sequence (and then only for relocation records that do not contain an explicit addend field) and for the last element, where the location determines where the relocated value will be placed. For all other relocation operands in a composed sequence, the location specified is ignored.

An ABI processor supplement may specify individual relocation types that always stop a composition sequence, or always start a new one.

GNU Assembler internals

GNU Assembler utilizes struct fixup to represent both the fixup and the relocatable expression.

1
2
3
4
5
6
7
8
9
10
11

	
struct fix {
  ...
  /* NULL or Symbol whose value we add in.  */
  symbolS *fx_addsy;

  /* NULL or Symbol whose value we subtract.  */
  symbolS *fx_subsy;

  /* Absolute number we add in.  */
  valueT fx_offset;
};


The relocation specifier is part of the instruction instead of part of struct fix. Targets have different internal representations of instructions.

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27

	
// gas/config/tc-aarch64.c
struct reloc
{
  bfd_reloc_code_real_type type;
  expressionS exp;
  int pc_rel;
  enum aarch64_opnd opnd;
  uint32_t flags;
  unsigned need_libopcodes_p : 1;
};

struct aarch64_instruction
{
  aarch64_inst base;
  aarch64_operand_error parsing_error;
  int cond;
  struct reloc reloc;
  unsigned gen_lit_pool : 1;
};

// gas/config/tc-ppc.c
struct ppc_fixup
 {
   expressionS exp;
   int opindex;
   bfd_reloc_code_real_type reloc;
 };

LLVM internals

LLVM integrated assembler encodes fixups and relocatable expressions separately.

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16

	
class MCFixup {
  /// The value to put into the fixup location. The exact interpretation of the
  /// expression is target dependent, usually it will be one of the operands to
  /// an instruction or an assembler directive.
  const MCExpr *Value = nullptr;

  /// The byte index of start of the relocation inside the MCFragment.
  uint32_t Offset = 0;

  /// The target dependent kind of fixup item this is. The kind is used to
  /// determine how the operand value should be encoded into the instruction.
  MCFixupKind Kind = FK_NONE;

  /// The source location which gave rise to the fixup, if any.
  SMLoc Loc;
};


It encodes relocatable expressions as MCValue, with:

RefKind as an optional relocation specifier.
SymA as an optional symbol reference (addend)
SymB as an optional symbol reference (subtrahend)
Cst as a constant value

This mirrors the relocatable expression concept, but RefKind—added in 2014 for AArch64—remains rare among targets. (I've migrated PowerPC's @l @ha folding to use RefKind.)

AArch64 implements a clean approach to select the relocation type. It dispatches on the fixup kind (an operand within a specific instruction format), then refines it with the relocation specifier.

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16

	
// AArch64ELFObjectWriter::getRelocType
unsigned Kind = Fixup.getTargetKind();
switch (Kind) {
// Handle generic MCFixupKind.
case FK_Data_1:
case FK_Data_2:
  ...

// Handle target-specific MCFixupKind.
case AArch64::fixup_aarch64_add_imm12:
  if (RefKind == AArch64MCExpr::VK_DTPREL_HI12)
    return R_CLS(TLSLD_ADD_DTPREL_HI12);
  if (RefKind == AArch64MCExpr::VK_TPREL_HI12)
    return R_CLS(TLSLE_ADD_TPREL_HI12);
  ...
}

MCSymbolRefExpr issues

The expression structure follows a traditional object-oriented hierarchy:

1
2
3
4
5
6
7

	
MCExpr
  MCConstantExpr: Value
  MCSymbolRefExpr: VariantKind, Symbol
  MCUnaryExpr: Op, Expr
  MCBinaryExpr: Op, LHS, RHS
  MCTargetExpr
    AArch64MCExpr: VariantKind, Expr


MCSymbolRefExpr::VariantKind enums the relocation specifier, but it's a poor fit:

Other expressions, like MCConstantExpr (e.g., PPC 4@l) and MCBinaryExpr (e.g., PPC (a+1)@l), also need it.
Semantics blur when folding expressions with @, which is unavoidable when @ can occur at any position within the full expression.
The generic MCSymbolRefExpr lacks target-specific hooks, cluttering the interface with any target-specific logic.

Consider what happens with addition or subtraction:

1
2
3

	
MCBinaryExpr
  LHS(MCSymbolRefExpr): VariantKind, SymA
  RHS(MCSymbolRefExpr): SymB


Here, the specifier attaches only to the LHS, leaving the full result uncovered. This awkward design demands workarounds.

Parsing a+4@got exposes clumsiness. After AsmParser::parseExpression processes a+4, it detects @got and retrofits it onto MCSymbolRefExpr(a), which feels hacked together.
Many targets (e.g., X86) use MCValue::getAccessVariant to grab LHS's specifier, though MCValue::RefKind would be cleaner.

Worse, leaky abstractions that MCSymbolRefExpr is accessed widely in backend code introduces another problem: while MCBinaryExpr with a constant RHS mimics MCSymbolRefExpr semantically, code often handles only the latter.

MCTargetExpr encoding relocation specifiers

MCTargetExpr subclasses, as used by AArch64 and RISC-V, offer a cleaner approach to encode relocations. We should limit MCTargetExpr to top-level use to encode one single relocation and avoid its inclusion as a subexpression.

1
2
3

	
AArch64MCExpr
  RefKind
  Expr(MCBinaryExpr): Op, LHS, RHS


MCSymbolRefExpr::VariantKind as the legacy way to encode relocations should be completely removed (probably in a distant future as many cleanups are required).

Our long-term goal is to migrate MCValue to use MCSymbol pointers instead of MCSymbolRefExpr pointers.

1
2
3
4
5
6
7
8
9
10
11
12
13

	
// Current
class MCValue {
  const MCSymbolRefExpr *SymA = nullptr, *SymB = nullptr;
  int64_t Cst = 0;
  uint32_t RefKind = 0;
};

// Future
class MCValue {
  const MCSymbol *SymA = nullptr, *SymB = nullptr;
  int64_t Cst = 0;
  uint32_t RefKind = 0;
};

AsmParser: expr@specifier

In LLVM's assembly parser library (LLVMMCParser), the parsing of expr@specifier was supported for all targets until I updated it to be an opt-in feature in March 2025.

Share
binutils
llvm
OLDER
Compiling C++ with the Clang API
POPULAR
All about thread-loca... (40253)
.init, .ctors, and .i... (22416)
When can glibc be bui... (17989)
All about Global Offs... (16424)
Stack unwinding (13335)
All about Procedure L... (12228)
ELF interposition and... (10444)
-fno-semantic-interpo... (10025)
All about symbol vers... (9667)
C++ exception handlin... (9525)
Relative relocations ... (9482)
Evolution of the ELF ... (8424)
ELF hash function may... (8334)
Weak symbol (7927)
Linker notes on AArch64 (7747)
支持Android、iOS 9内置IPSe... (7712)
All about LeakSanitizer (7697)
All about UndefinedBe... (7687)
LLD and GNU linker in... (7566)
GNU indirect function (7519)
Relocatable linking (7132)
2019年总结——工具链的一年 (7122)
The dark side of RISC... (7060)
Control-flow integrity (7055)
glibc and DT_GNU_HASH (5903)
Why isn't ld.lld faster? (5820)
Linker garbage collec... (5540)
指定dynamic linker以使用高版... (5139)
ODR violation detection (5053)
C++ language server c... (5000)
Explain GNU style lin... (4925)
All about sanitizer i... (4850)
Assemblers (4761)
gcov与LLVM中的实现 (4742)
2022年总结 (4517)
约瑟夫问题的两个O(log n)解法 (4469)
Compressed debug sect... (4410)
DEFCON 26 CTF参赛记 (4375)
RISC-V linker relaxat... (4164)
Integrated assembler ... (4144)
zstd compressed debug... (3992)
Skipping boring funct... (3917)
Relocation overflow a... (3896)
Copy relocations, can... (3888)
Symbol processing (3853)
-march=, -mcpu=, and ... (3852)
C standard library he... (3793)
Build glibc with LLD 13 (3613)
Android微信数据导出 (3557)
Precompiled headers (3522)
Force-directed算法(1)——... (3426)
Exploring GNU extensi... (3366)
Compiler driver and c... (3281)
Command line processi... (3199)
Unwinding through a s... (3176)
Everything I know abo... (2976)
COMDAT and section group (2914)
近况 (2869)
完美迷宫生成算法 (2822)
All about COMMON symbols (2814)
Layering check with C... (2797)
Removing global state... (2780)
Clang's -O0 output: b... (2720)
2021年总结 (2618)
从-fpatchable-function... (2566)
_FORTIFY_SOURCE (2335)
《Debug Hacks》和调试技巧 (2261)
Segment tree (2112)
皈依Emacs (2102)
lld 15 ELF changes (2090)
WeeChat操作各种聊天软件 (2087)
Exploring object file... (2065)
DEFCON 24 CTF参赛记 (2002)
一次服务器BMC固件逆向经历 (1989)
Dependency related li... (1953)
Archives and --start-lib (1870)
DEFCON 25 CTF参赛记 (1821)
Light ELF: exploring ... (1759)
Everything I know abo... (1758)
使用Suricata进行IDS/IPS (1729)
Distribution of debug... (1726)
我是这样使用微信的——wechatircd... (1721)
2020年总结 (1716)
Metadata sections, CO... (1637)
Analysis and introspe... (1629)
SECTIONS and OVERWRIT... (1609)
Competitive programmi... (1602)
2014年总结——竞赛的一年 (1580)
调试技巧2 (1562)
从ASC'14到ISC'15——我的超算竞... (1553)
lld 14 ELF changes (1509)
Mapping symbols: reth... (1496)
C++ standard library ... (1478)
A compact relocation ... (1462)
LeetCode solutions (1449)
ccls 0.20181225 release (1441)
Toolchain testing (1434)
Modified condition/de... (1367)
PI_STATIC_AND_HIDDEN/... (1348)
Nginx根据Accept-Languag... (1345)
FreeBSD src browsing ... (1256)
Port LLVM XRay to App... (1251)
Understanding orphan ... (1227)
模块内函数调用和libc符号重命名 (1219)
C++ exit-time destruc... (1209)
wechatircd——用IRC客户端控制... (1162)
Linker notes on Power... (1147)
Function multi-versio... (1122)
Clang -Wunused-comman... (1107)
OverTheWire - Natas W... (1086)
脱离chroot的枷锁 (1017)
建立清华大学Node Packaged M... (1007)
Tinkering with Neovim (998)
DWARF in reproducible... (975)
Exploring the section... (971)
2024年总结 (961)
RedTigers Hackit Warg... (927)
Dominator tree (925)
Linker notes on x86 (901)
Linker compatibility ... (891)
Evil--在Emacs中模拟Vim (888)
Compiler output files (878)
8门编程语言的设计思考 (859)
lld linked musl on Po... (855)
自动获取SSH密码并登录 (829)
kth element in a suba... (814)
A deep dive into Clan... (797)
我的xmonad配置 (791)
DEFCON 23 CTF参赛记 (787)
无需每日扫码的IRC版微信和QQ：wech... (779)
终端模拟器下使用双倍宽度多色Emoji字体 (770)
用udev自动挂载usb设备 (756)
ELF Hacks (753)
Cyber Grand Challenge... (746)
J语言初探 (746)
lld 16 ELF changes (726)
DEFCON 21——我的奋斗 (702)
C minifier with Clang (691)
DEFCON 21 CTF参赛记 (686)
江苏信安竞赛初赛工作组记事 (634)
My involvement with L... (628)
使用Burkhard-Keller tre... (622)
ccls and LSP Semantic... (619)
Real World CTF 2018 r... (617)
Understanding and imp... (616)
Gmail的OfflineIMAP XOA... (596)
偃师——finite automaton生成工具 (587)
D-Link路由器后门注记 (582)
DEFCON 22 CTF参赛记 (578)
Python is ugly (578)
80分钟8语言 (576)
MMU-less systems and ... (569)
gcc中sqrt实现 (565)
LeetCode Best Time to... (559)
算法、FP、前端、安全、系统管理——201... (557)
BCTF工作组记事 (556)
2018-09-09 ccls最近更新 (532)
异于Make的另一种构建系统 (528)
AddressSanitizer: glo... (510)
NOIP 2004 数字游戏（虫食算） (490)
二叉树遍历算法总结 (477)
telegramircd——用IRC客户端... (474)
并行N-body模拟 (468)
基于 mutt+offlineimap+n... (460)
Real World CTF 2018 c... (449)
在Makefile中自动生成依赖 (443)
Simplifying disassemb... (434)
Haskell学习笔记 (419)
Compressed arbitrary ... (412)
$ccls/navigate和index.... (411)
第二届青少年开发者大会 (398)
HDU OJ一些题目 (397)
自然语言处理之词语抽取 (392)
webqqircd——用IRC客户端控制W... (389)
When QOI meets XZ (386)
Buffalo WZR-600DHP Op... (384)
ML编译器Caml Featherweig... (374)
jq实现原理——字节码 (370)
称球问题扩展——根据当前已知信息选择最优称量方案 (365)
Makefile介绍 (361)
.emacs (358)
用Makefile搭建博客 (345)
2023年总结 (345)
Extract an archive me... (339)
整系数Discrete Fourier t... (338)
Toolchain notes on MIPS (335)
三柱汉诺塔相关扩展问题 (318)
用Perl的正则表达式分析csv文件 (313)
Ko-Aluru suffix array... (311)
常数空间Invert Binary Tre... (308)
LeetCode Expression A... (306)
lld 19 ELF changes (304)
ML编译器Caml Featherweig... (303)
Toolchain notes on z/... (292)
用Makefile搭建博客-2 (288)
终端模拟器下宽字符退格 (287)
My involvement with L... (282)
GTK+ tic-tac-toe（井字棋） (279)
Trend Micro Codinsani... (267)
ISC'14 Student Cluste... (259)
PyGTK迷宫生成器mazer (259)
RuCTFE 2012参赛记 (257)
Haskell实现的Splay树 (256)
Linker notes on PE/COFF (254)
BCTF 2016 hsab及BetaFo... (248)
BCTF 2015 CamlMaze命题报... (247)
八数码 (244)
使用Double-array trie优化... (243)
智能体大赛与平台开发 (240)
“1001夜”学生节线上解谜活动1001/... (239)
GTK+黑白棋reversi (237)
计算所有后缀的排名 (234)
用Google Analytics API... (233)
Reflections on LLVM's... (231)
TUNA技术沙龙及A Pretty Pri... (229)
域名迁移至maskray.me (226)
Linker notes on AArch32 (225)
Keeping pace with LLV... (225)
cquery最近改动与libclang.s... (223)
用Pike's VM实现的非回溯正则表达式引擎 (214)
SVT13117ECS上Gentoo安装记... (209)
A compact section hea... (206)
根据计划求解Rush (203)
用DocPad构建静态网站 (200)
Tiling window manager... (195)
USACO JAN10 Gold (194)
Dancing Links+Algorit... (194)
genkernel (190)
用rss2email阅读feeds (190)
给xbindkeys添加key seque... (180)
用Expect连接无线网络 (179)
ZJU 1638. Greedy Island (178)
Raw symbol names in i... (178)
Ouroborus Program - q... (164)
lld 18 ELF changes (161)
cquery USR优化和分层diff (157)
RISC-V TLSDESC works! (155)
网络学堂feeds2mail (154)
String index structur... (151)
使用cquery：C++ language... (145)
clang-format and sing... (141)
DSO undef and non-exp... (129)
SECUINSIDE CTF Quals ... (126)
Js_of_ocaml和Emscripten (123)
My involvement with L... (123)
Awesome 3 debian menu (105)
r2con 2017 r2cLEMENCy (100)
XV Olimpiada Informat... (100)
checker (95)
reviews.llvm.org beca... (92)
ccls: a fork of the C... (79)
lld 17 ELF changes (47)
Exporting Tweets (23)
Emacs helm-kythe与Hask... (16)
TAG CLOUD
adc ai9 algorithm arm asc assebmly assembler assembly automaton awesome bctf binary binutils bmc build system c c++ ccls cgc chroot clang clang-format codinsanity coffee script compiler compression computer security contest cpp csv ctf data structure debug defcon desktop docker elf emacs email emoji emscripten event expect ext4 fdpic feeds firmware floating point forensics fp freebsd game gcc gdb gentoo github glibc graph graph drawing gtk hacker culture hackerrank hanoi haskell hpc image inotify ipsec irc isc j javascript josephus problem jq kernel kythe ld leetcode libunwind linker linux lld lldb llvm lsp m68k makefile math maze mirror ml musl mutt n-body neovim network nginx nim nlp node.js noip notmuch npm ocaml offlineimap oi oj openwrt parallel parser generator perl powerpc presentation puzzle python qq radare2 regex regular expression reverse engineering review riscv router rtld ruby ructfe s390x sanitizer scheme search security shell ssh stringology student festival puzzle suffix array suffix automaton summary suricata telegram telegramircd terminal tls traversal tree trendmicro udev unicode unix usb vim vpn vte wargame web analytics webqqircd website wechat wechatircd window manager windows x86 xbindkeys xmonad xz yanshi
BLOGROLL
BYVoid
fqj1994
ppwwyyxx
© 2025 MaskRay
Powered by Hexo
Home Archives Feeds TIL Presentations
