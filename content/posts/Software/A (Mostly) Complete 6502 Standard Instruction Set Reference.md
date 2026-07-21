---
title: A (Mostly) Complete 6502 Standard Instruction Set Reference
date: 2026-07-20
lastmod: 2026-07-20
draft: false
tags:
  - Software
  - C64U
  - VintageComputing
---
I have been working on this for a couple days, in preparation for writing machine code on the C64 and Apple-1 and other 6502 based machines. I wanted something that I could edit and reference in other documents as I start to acrue some practical knowledge, so I took to adapting the already excellent reference document found at https://masswerk.at/6502/6502_instruction_set.html. This is a great reference, and should suit anybody pretty well. I only adapted it to markdown so that I had a copy that I can update as I learn. So, I give you the 10,454 word document that almost drove me insane!
<br>

# Table of Contents
***
1. [Foreword](#foreword)
2. [Registers and Common Properties](#registers-and-common-properties)
	1. [Registers](#registers)
	2. [Common Properties](#common-properties)
3. [Addressing Modes in Detail](#addressing-modes-in-detail)
	1. [Implied Addressing](#implied-addressing)
	2. [Immediate Addressing](#immediate-addressing)
	3. [Absolute Addressing](#absolute-addressing)
	4. [Zero-Page Addressing](#zero-page-addressing)
	5. [Indexed Addressing - Absolute,X and Absolute,Y](#indexed-addressing---absolutex-and-absolutey)
	6. [Indexed Addressing - Zero-Page,X and Zero-Page,Y](#indexed-addressing---zero-pagex-and-zero-pagey)
	7. [Indirect Addressing](#indirect-addressing)
	8. [Pre-Indexed Indirect, "(Zero-Page,X)"](#pre-indexed-indirect-zero-pagex)
	9. [Post-Indexed Indirect, "(Zero-Page),Y"](#post-indexed-indirect-zero-pagey)
	10. [Relative Addressing (Conditional Branching)](#relative-addressing-conditional-branching)
4. [Arithmetic Primer](#arithmetic-primer)
	1. [Signed Values](#signed-values)
	2. [Flags with ADC and SBC](#flags-with-adc-and-sbc)
	3. [Decimal Mode (BCD)](#decimal-mode-bcd)
5. [Transfer Instructions](#transfer-instructions)
	1. [`LDA` - Load Accumulator with Memory](#lda---load-accumulator-with-memory)
	2. [`LDX` - Load Index X with Memory](#ldx---load-index-x-with-memory)
	3. [`LDY` - Load Index Y with Memory](#ldy---load-index-y-with-memory)
	4. [`STA` - Store Accumulator in Memory](#sta---store-accumulator-in-memory)
	5. [`STX` - Store Index X in Memory](#stx---store-index-x-in-memory)
	6. [`STY` - Store Index Y in Memory](#sty---store-index-y-in-memory)
	7. [`TAX` - Transfer Accumulator to Index X](#tax---transfer-accumulator-to-index-x)
	8. [`TAY` - Transfer Accumulator to Index Y](#tay---transfer-accumulator-to-index-y)
	9. [`TSX` - Transfer Stack Pointer to Index X](#tsx---transfer-stack-pointer-to-index-x)
	10. [`TXA` - Transfer Index X to Accumulator](#txa---transfer-index-x-to-accumulator)
	11. [`TXS` - Transfer Index X to Stack Register](#txs---transfer-index-x-to-stack-register)
	12. [`TYA` - Transfer Index Y to Accumulator](#tya---transfer-index-y-to-accumulator)
6. [Stack Instructions](#stack-instructions)
	1. [`PHA` - Push Accumulator on Stack](#pha---push-accumulator-on-stack)
	2. [`PHP` - Push Processor Status on Stack](#php---push-processor-status-on-stack)
	3. [`PLA` - Pull Accumulator from Stack](#pla---pull-accumulator-from-stack)
	4. [`PLP` - Pull Processor Status from Stack](#plp---pull-processor-status-from-stack)
7. [Decrement and Increment Instructions](#decrement-and-increment-instructions)
	1. [`DEC` - Decrement Memory by One](#dec---decrement-memory-by-one)
	2. [`DEX` - Decrement Index X by One](#dex---decrement-index-x-by-one)
	3. [`DEY` - Decrement Index Y by One](#dey---decrement-index-y-by-one)
	4. [`INC` - Increment Memory by One](#inc---increment-memory-by-one)
	5. [`INX` - Increment Index X by One](#inx---increment-index-x-by-one)
	6. [`INY` - Increment Index Y by One](#iny---increment-index-y-by-one)
8. [Arithmetic Instructions](#arithmetic-instructions)
	1. [`ADC` - Add Memory to Accumulator with Carry](#adc---add-memory-to-accumulator-with-carry)
	2. [`SBC` - Subtract Memory from Accumulator with Borrow](#sbc---subtract-memory-from-accumulator-with-borrow)
9. [Logical Operations](#logical-operations)
	1. [`AND` - AND Memory with Accumulator](#and---and-memory-with-accumulator)
	2. [`EOR` - Exclusive-OR Memory with Accumulator](#eor---exclusive-or-memory-with-accumulator)
	3. [`ORA` - OR Memory with Accumulator](#ora---or-memory-with-accumulator)
10. [Shift & Rotate Instructions](#shift--rotate-instructions)
	1. [`ASL` - Shift Left One Bit](#asl---shift-left-one-bit)
	2. [`LSR` - Shift Right One Bit](#lsr---shift-right-one-bit)
	3. [`ROL` - Rotate One Bit Left](#rol---rotate-one-bit-left)
	4. [`ROR` - Rotate One Bit Right](#ror---rotate-one-bit-right)
11. [Flag Instructions](#flag-instructions)
	1. [`CLC` - Clear Carry Flag](#clc---clear-carry-flag)
	2. [`CLD` - Clear Decimal Mode](#cld---clear-decimal-mode)
	3. [`CLI` - Clear Interrupt Disable Bit](#cli---clear-interrupt-disable-bit)
	4. [`CLV` - Clear Overflow Flag](#clv---clear-overflow-flag)
	5. [`SEC` - Set Carry Flag](#sec---set-carry-flag)
	6. [`SED` - Set Decimal Flag](#sed---set-decimal-flag)
	7. [`SEI` - Set Interrupt Disable Status](#sei---set-interrupt-disable-status)
12. [Comparison Instructions](#comparison-instructions)
	1. [`CMP` - Compare Memory with Accumulator](#cmp---compare-memory-with-accumulator)
	2. [`CPX` - Compare Memory and Index X](#cpx---compare-memory-and-index-x)
	3. [`CPY` - Compare Memory and Index Y](#cpy---compare-memory-and-index-y)
13. [Bit Instruction](#bit-instruction)
	1. [`BIT` - Test Bits in Memory with Accumulator](#bit---test-bits-in-memory-with-accumulator)
14. [Conditional Branch Instructions](#conditional-branch-instructions)
	1. [`BCC` - Branch on Carry Clear](#bcc---branch-on-carry-clear)
	2. [`BCS` - Branch on Carry Set](#bcs---branch-on-carry-set)
	3. [`BEQ` - Branch on Result Zero](#beq---branch-on-result-zero)
	4. [`BMI` - Branch on Result Minus](#bmi---branch-on-result-minus)
	5. [`BNE` - Branch on Result not Zero](#bne---branch-on-result-not-zero)
	6. [`BPL` - Branch on Result Plus](#bpl---branch-on-result-plus)
	7. [`BVC` - Branch on Overflow Clear](#bvc---branch-on-overflow-clear)
	8. [`BVS` - Branch on Overflow Set](#bvs---branch-on-overflow-set)
15. [Jump and Subroutine Instructions](#jump-and-subroutine-instructions)
	1. [`JMP` - Jump to New Location](#jmp---jump-to-new-location)
	2. [`JSR` - Jump to New Location Saving Return Address](#jsr---jump-to-new-location-saving-return-address)
	3. [`RTS` - Return from Subroutine](#rts---return-from-subroutine)
16. [Interrupt Instructions](#interrupt-instructions)
	1. [`BRK` - Force Break](#brk---force-break)
	2. [`RTI` - Return from Interrupt](#rti---return-from-interrupt)
		1. [Curious Interrupt Behavior](#curious-interrupt-behavior)
		2. [The Break Flag and the Stack](#the-break-flag-and-the-stack)
17. [Other Instructions](#other-instructions)
	1. [`NOP` - No Operation](#nop---no-operation)

<br>
<br>
<br>

# Foreword
***
- The main source for this document is https://masswerk.at/6502/6502_instruction_set.html
   - You may ask, "Why copy and paste all this into a markdown file?" I have my reasons:
      - I wanted a reference that covers only the standard instruction set, so I could get familiar with it in a way that transfers across many machines.
      - I wanted it in markdown so I can link back to this file from machine-specific appendices (memory maps, character maps, etc.).
      - I wanted it to be a fairly complete reference, so in addition to the great info already on the site, I've written examples for each operator.
        - If an operator only has one address mode, there is no example. 
   - This document covers only the standard instruction set shared by all 6502 machine code.
      - Some computers implement additional opcodes; those will be noted in separate appendix-style documents as I encounter them.
   - Operators are grouped by similarity.
      - For example, the `ADC` and `SBC` operators are grouped into an Arithmetic section.
      - Sections may include additional information about how those operators work.
- Flags Legend:
   - `+` .... modified
   - `-` .... not modified
   - `1` .... set
   - `0` .... cleared
   - `M6` .... memory bit 6
   - `M7` .... memory bit 7
- Footnotes:
   - `*` — Add 1 cycle if page boundary is crossed.
   - `**` — Add 1 cycle if branch occurs on the same page; add 2 cycles if branch occurs to a different page.
   - `***` — On the original NMOS CPU, the lookup of the effective address's high byte is always performed on the same memory page as the low byte (e.g., `JMP ($11FF)` resolves to a lookup at $11FF for the low byte and at $1100 for the high byte). On the CMOS version, add 1 cycle if the address is at a page boundary.

<br>
<br>
<br>

# Registers and Common Properties 
***
### Registers

| Register | Register Name   | Size   |
| -------- | --------------- | ------ |
| PC       | Program Counter | 16 bit |
| AC       | Accumulator     | 8 bit  |
| X        | X register      | 8 bit  |
| Y        | Y register      | 8 bit  |
| SR       | Status register | 8 bit  |
| SP       | Stack pointer   | 8 bit  |
- The accumulator is the main register of the 6502.
	- Typically used for the first operand of the Arithmetic Logic Unit (ALU); results are deposited back in the accumulator.
- X and Y are general-purpose auxiliary registers.
	- Commonly referred to as index registers. Their contents are added to a base memory location before values are stored to or retrieved from the resulting address, known as the effective address. Commonly used for loops and table lookups at a given index.
- The program counter keeps track of the memory location holding the current instruction code.
	- Automatically incremented to progress the program.
- The stack pointer points to the top of the stack.
- The status register holds the status of the processor, consisting of flags reflecting the results of previous operations.
	- All arithmetic operations update the Z, N, C, and V flags.
	- Status Register flags (bit 7 to bit 0):
		- `N` - Negative
			- Indicates whether a result was positive or negative.
		- `V` - Overflow
			- Indicates if an overflow occurred.
			- Since this is an 8-bit CPU, if an operation results in a signed value outside the range -128 to +127, the overflow flag is set.
		- `-` - ignored
		- `B` - Break
			- Not a real flag.
			- Only appears when the status register is pushed onto the stack: set to 1 if pushed by software (BRK or PHP), and 0 if pushed by hardware (an interrupt).
			- This lets an interrupt handler distinguish a software break from a hardware interrupt by checking this value.
		- `D` - Decimal
			- Sets the ALU to binary-coded decimal mode for addition and subtraction.
		- `I` - Interrupt
			- Blocks any maskable interrupt requests (IRQ).
		- `Z` - Zero
			- Indicates that a result was all zeros.
		- `C` - Carry
			- Used as a buffer in arithmetic operations.

<br>

### Common Properties
- Processor Stack
	- A LIFO, top-down stack occupying memory addresses $0100–$01FF.
- Bytes, Words, Addressing
	- Bytes are 8 bits.
	- Words are 16 bits, in low-byte/high-byte order (little-endian).
	- The address range is 16 bits; operands follow instruction codes.
- Signed Values
	- Signed values are two's complement, with the sign in bit 7 (most significant bit).
		- %11111111 = $FF = -1
		- %10000000 = $80 = -128
		- %01111111 = $7F = +127
	- Both signed binary and Binary Coded Decimal (BCD) arithmetic modes are available; BCD values are unsigned (positive or zero only).
- System Vectors
	- $FFFA, $FFFB ... NMI (Non-Maskable Interrupt) vector, 16-bit (LB, HB)
	- $FFFC, $FFFD ... RES (Reset) vector, 16-bit (LB, HB)
	- $FFFE, $FFFF ... IRQ (Interrupt Request) vector, 16-bit (LB, HB)
- Start/Reset Operations
	- An active-low reset line holds the processor in a known, disabled state while the system initializes. 
		- When the reset line goes high, the processor performs a start sequence of 7 cycles, at the end of which the program counter (PC) is read from the address provided in the 16-bit reset vector at $FFFC (LB-HB). 
		- On the eighth cycle, the processor transfers control by jumping to that address. 
			- Any further initialization is left to the program. (Instructions exist to initialize and load every register except the program counter, which is set by the reset vector.)

<br>
<br>
<br>

# Addressing Modes in Detail
***
### Implied Addressing
These instructions act directly on one or more registers or flags internal to the CPU. Therefore, these instructions are principally single-byte instructions, lacking an explicit operand. The operand is implied, as it is already provided by the instruction itself.

Instructions targeting exclusively the contents of the accumulator may or may not be denoted by using an explicit "A" as the operand, depending on the flavor of syntax. (This may be regarded as a special address mode of its own, but it is really a special case of an implied instruction. It is still a single-byte instruction and no operand is provided in machine language.)

#### Mnemonic Examples
```asm6502
CLC    ;clear the carry flag
ROL A  ;rotate contents of accumulator left by one position
ROL    ;same as above, implicit notation (A implied)
TXA    ;transfer contents of X-register to the accumulator
PHA    ;push the contents of the accumulator to the stack
RTS    ;return from subroutine (by pulling PC from stack)
```
*Mind that some of these instructions, while simple in appearance, may be quite complex operations, like "PHA", which involves the accumulator, the stack pointer, and memory access.*

<br>

### Immediate Addressing
Here, a literal operand is given immediately after the instruction. The operand is always an 8-bit value and the total instruction length is always 2 bytes. In memory, the operand is a single byte following immediately after the instruction code. In assembler, the mode is usually indicated by a "#" prefix adjacent to the operand.
```asm6502
Mnemonic   Instruction  
 LDA #7       A9 07  
                  |  
                  V  
              A: 07
```

#### Mnemonic Examples
```asm6502
LDA #$07  ;load the literal hexadecimal value "$07" into the accumulator  
ADC #$A0   ;add the literal hexadecimal value "A0" to the accumulator  
CPX #$32  ;compare the X-register to the literal hexadecimal value "$32"
```

<br>

### Absolute Addressing
Absolute addressing mode provides the 16-bit address of a memory location, the contents of which are used as the operand to the instruction. In machine language, the address is provided in two bytes immediately after the instruction (making these 3-byte instructions) in low-byte, high-byte order (LLHH), i.e. little-endian. In assembler, conventional numbers (HHLL order, i.e. big-endian) are used to provide the address.

Absolute addresses are also used by the jump instructions JMP and JSR to provide the address of the next instruction to continue with in the control flow.
```asm6502
Mnemonic   Instruction      Data  
LDA $3010    AD 10 30    $3010: 34  
                                 |  
                                 V  
                             A: 34
```

#### Mnemonic Examples
```asm6502
LDA $3010  ;load the contents of address "$3010" into the accumulator  
ROL $08A0  ;rotate the contents of address "$08A0" left by one position  
JMP $4000  ;jump to (continue with) location "$4000"
```

<br>

### Zero-Page Addressing
The 16-bit address space available to the 6502 is thought of as consisting of 256 "pages" of 256 memory locations each ($00…$FF). In this model, the high-byte of an address gives the page number and the low-byte a location inside that page. The very first of these pages, where the high-byte is zero (addresses $0000…$00FF), is somewhat special.

Zero-page addressing is similar to absolute addressing, but these instructions use only a single byte for the operand — the low-byte — while the high-byte is assumed to be zero by definition. Therefore, these instructions are a total of two bytes long (one less than absolute mode) and take one CPU cycle less to execute, since there is one byte less to fetch.
```asm6502
Mnemonic   Instruction    Data  
LDA $80      A5 80      $0080: 34  
                                |  
                                V  
                            A: 34
```

#### Mnemonic Examples
```asm6502
LDA $80  ;load the contents of address "$0080" into the accumulator  
BIT $A2  ;perform bit-test with the contents of address "$00A2"  
ASL $9A  ;arithmetic shift left of the contents of location "$009A"
```
(One way to think of the zero-page is as a page of 256 additional registers — somewhat slower than the internal registers, but with zero-page instructions executing faster than "normal" instructions. The zero-page has a few more tricks up its sleeve, making these addresses perform more like real registers; see below.)

<br>

### Indexed Addressing - Absolute,X and Absolute,Y
Indexed addressing adds the contents of either the X-register or the Y-register to the provided address to give the _effective address_, which provides the operand.

These instructions are useful for, e.g., loading values from tables or writing to a continuous segment of memory in a loop. The most basic forms are "absolute,X" and "absolute,Y", where either the X- or the Y-register, respectively, is added to a given base address. Since the base address is a 16-bit value, these are generally 3-byte instructions. Since there is an additional operation required to determine the effective address, these instructions are one cycle slower than those using absolute addressing mode. If adding the contents of the index register changes the high-byte of the base address — so that the effective address falls on the next memory page — the additional operation to increment the high-byte takes another CPU cycle. This is also known as crossing a page boundary.
```asm6502
  Mnemonic    Instruction     Data  
LDA $3120,X    BD 20 31  
                       \
                        + = $3132: 78  
                       /            |   
                  X: 12             |  
                                    V  
                                A: 78
```

#### Mnemonic Examples
```asm6502
LDA $3120,X  ;load the contents of address "$3120 + X" into A  
LDX $8240,Y  ;load the contents of address "$8240 + Y" into X  
INC $1400,X  ;increment the contents of address "$1400 + X"
```

<br>

### Indexed Addressing - Zero-Page,X and Zero-Page,Y
As with absolute addressing, there is also a zero-page mode for indexed addressing. However, this is generally only available with the X-register. (The one exception is LDX, which has an indexed zero-page mode using the Y-register.) As with normal zero-page mode, these instructions are one byte shorter in total length (two bytes) and take one CPU cycle less than instructions in absolute indexed mode.

Unlike absolute indexed instructions with 16-bit base addresses, zero-page indexed instructions never affect the high-byte of the effective address — it simply wraps around within the zero-page — so there is no penalty for crossing page boundaries.
```asm6502
 Mnemonic    Instruction     Data  
LDA $80,X       B5 80  
                     \
                      + = $0082: 64  
                     /            |  
                X: 02             |  
                                  V  
                              A: 64
```

#### Mnemonic Examples
```asm6502
LDA $80,X  ;load the contents of address "$0080 + X" into A  
LSR $82,X  ;shift the contents of address "$0082 + X" left  
LDX $60,Y  ;load the contents of address "$0060 + Y" into X
```

<br>

### Indirect Addressing
This mode looks up a given address and uses the contents of that address and the next one (in LLHH little-endian order) as the effective address. In its basic form, this mode is available only for the JMP instruction. (Its typical use is for jump vectors and jump tables.)
Like the absolute JMP instruction, it uses a 16-bit address (3 bytes total), but takes two additional CPU cycles to execute, since there are two additional bytes to fetch for the lookup of the effective jump target.
Indirect addressing is generally denoted by putting the lookup address in parentheses.

```asm6502
Mnemonic     Instruction      Lookup
JMP ($FF82)    6C 82 FF -> $FF82: C4 80
                                     |
                                     V
                               PC: $80C4 (Effective Target)
```

**Mnemonic Example:**
```asm6502
JMP ($FF82)  ;jump to the address given in locations "$FF82" and "$FF83"
```

Note: On the original NMOS 6502, the high-byte of the lookup address is not incremented across page boundaries. That is, if the low-byte of the lookup address is $FF, the high-byte will be fetched from $00 on the same page. (E.g., "JMP ($11FF)" will effectively resolve to a lookup at $11FF for the low-byte and $1100 for the high-byte, where we might expect $1200 to be used for the latter.)
This is corrected on the CMOS version of the CPU, which behaves as expected but takes an extra cycle to do so.

<br>

### Pre-Indexed Indirect, "(Zero-Page,X)"
Indexed indirect address modes are generally available only for instructions supplying an operand to the accumulator (LDA, STA, ADC, SBC, AND, ORA, EOR, etc.). The placement of the index register inside or outside the parentheses indicating the address lookup gives a clue as to what these instructions are doing.

Pre-indexed indirect addressing is only available in combination with the X-register. It works much like "zero-page,X" mode, but after the X-register has been added to the base address, instead of directly accessing that location, an additional lookup is performed, reading the contents of the resulting address and the next one (in LLHH little-endian order) to determine the effective address.

As with "zero-page,X" mode, the total instruction length is 2 bytes, but there are two additional CPU cycles required to fetch the effective 16-bit address. Also as with "zero-page,X" mode, the lookup address will never overflow into the next page, but simply wraps around within the zero-page.

These instructions are useful whenever we want to loop over a table of pointers to scattered addresses, or apply the same operation to various addresses stored as a table in the zero-page.
```asm6502
  Mnemonic    Instruction     Lookup            Data  
LDA ($70,X)      A1 70  
                      \
                       + = $0075: 23 20 ---> $3023: A5  
                      /                              |  
                 X: 05                               |  
                                                     V  
                                                 A: A5
```

#### Mnemonic Examples
```asm6502
LDA ($70,X) ;load the contents of the location given in addresses 
            ;  "$0070+X" and "$0071+X" into A  
STA ($A2,X) ;store the contents of A in the location given in addresses 
            ;  "$00A2+X" and "$00A3+X"  
EOR ($BA,X) ;perform an exclusive OR of the contents of A and the contents
            ;  of the location given in addresses "$00BA+X" and "$00BB+X"
```

<br>

### Post-Indexed Indirect, "(Zero-Page),Y"
Post-indexed indirect addressing is only available in combination with the Y-register. As indicated by the indexing term ",Y" appended outside the parentheses indicating the indirect lookup, a pointer is first read from the given zero-page address and resolved, and only then is the contents of the Y-register added to it to give the effective address.

The total instruction length is 2 bytes, but it takes an additional CPU cycle to resolve and index the 16-bit pointer. As with "absolute,X" mode, the effective address may overflow into the next page, in which case execution takes an extra CPU cycle.

These instructions are useful whenever we want to perform lookups on varying base addresses, or loop over tables whose base address is stored in the zero-page.
```asm6502
  Mnemonic   Instruction     Lookup         Data  
LDA ($70),Y     B1 70      $0070: 20 35  
                                       \
                                        + = $3530: 23  
                                       /            |  
                                  Y: 10             |  
                                                    V  
                                                A: 23
```

#### Mnemonic Examples
```asm6502
LDA ($70),Y  ;add the contents of the Y-register to the pointer provided in 
             ;  "$0070" and "$0071" and load the contents of this address into A
STA ($A2),Y  ;store the contents of A in the location given by the pointer in 
             ;  "$00A2" and "$00A3" plus the contents of the Y-register  
EOR ($BA),Y  ;perform an exclusive OR of the contents of A and the address given
             ;  by the addition of Y to the pointer in "$00BA" and "$00BB"
```

<br>

### Relative Addressing (Conditional Branching)
This final address mode is exclusive to conditional branch instructions, which branch in the execution path depending on the state of a given CPU flag. Here, the instruction provides only a relative offset, which is added to the contents of the program counter (PC) as it points to the next instruction. The relative offset is a signed single-byte value in two's complement encoding (giving a range of −128…+127), allowing branches up to half a page forward or backward. This makes these instructions compact, fast, and relocatable — but it also means the branch target can never be farther away than half a memory page.

Generally, an assembler will handle this calculation, so we only need to provide the target address without worrying about the relative offset ourselves.

These instructions are always 2 bytes long and take 2 CPU cycles if the branch is not taken (the condition resolves to 'false'), and 3 cycles if the branch is taken (the condition is true). If the branch is taken and the target is on a different page, this adds another CPU cycle (4 in total).
```asm6502
PC       Mnemonic        Instruction     Target  
$1000    BEQ $1005          F0 03  
                                 \ Offset  
    PC points to next instruction \
$1002 ---------------------------> + = PC: $1005
```

#### Mnemonic Examples
*(Examples are provided in usual assembler format. Notice how these look much like instructions in absolute address mode.)*
```asm6502
BEQ $1005  ;branch to location "$1005", if the zero flag is set.
		   ;If the current address is $1000, this gives an offset of $03.  
BCS $08C4  ;branch to location "$08C4", if the carry flag is set. 
           ;If the current address is $08D4, this gives an offset of $EE (−$12). 
BCC $084A  ;branch to location "$084A", if the carry flag is clear.
```

<br>
<br>
<br>

# Arithmetic Primer
***
*Small Editor's Note: I originally placed this in the Arithmetic Instructions section, like how some of the other sections have info at the start. But as you can see, it's a very big section. I figured it would be cleaner to place it before the instructions section, so that's why it's here.*

The 6502 processor features two basic arithmetic instructions: `ADC`, _ADd with Carry_, and `SBC`, _SuBtract with Carry_. As the names suggest, these provide addition and subtraction for single-byte operands and results. However, operations are not limited to a single-byte range, which is where the carry flag comes in, providing the means for a single-bit carry (or borrow) to combine operations over several bytes.

To accomplish this, the carry is included in each of these operations: for additions, it is added (much like another operand); for subtractions — which are just an addition using the inverse of the operand (the complement value of the operand) — the role of the carry is inverted as well. Therefore, it is crucial to set up the carry appropriately: for additions, the carry must initially be cleared (using `CLC`), while for subtractions, it must initially be set (using `SEC` — more on `SBC` below).

```asm6502
         ;ADC: A = A + M + C
CLC      ;clear carry in preparation
LDA #2   ;load 2 into the accumulator
ADC #3   ;add 3 -> now 5 in accumulator

         ;SBC: A = A - M - C̅   ("C̅": "not carry")
SEC      ;set carry in preparation
LDA #15  ;load 15 into the accumulator
SBC #8   ;subtract 8 -> now 7 in accumulator
```

_Note:_ Here, we used immediate mode, indicated by the "#" prefix before the operand, to directly load a literal value. If there is no such "#" prefix, we generally mean to use the value stored at the address given by the operand, as we will see in the next example.

To combine this for 16-bit values (2 bytes each), we simply chain the instructions for the next bytes to operate on, but this time without setting or clearing the carry again.

Supposing the following locations for storing 16-bit values:
```asm6502
                    low-byte high-byte 
first argument ....  $1000     $1001 
second argument ...  $1002     $1003 
result ............  $1004     $1005  
```

we perform a 16-bit addition by:
```asm6502
CLC         ;prepare carry for addition
LDA $1000   ;load value at address $1000 into A (low byte of first argument)
ADC $1002   ;add low byte of second argument at $1002
STA $1004   ;store low byte of result at $1004
LDA $1001   ;load high byte of first argument
ADC $1003   ;add high byte of second argument
STA $1005   ;store high byte of result (result in $1004 and $1005)
```

and, conversely, for a 16-bit subtraction:
```asm6502
SEC         ;prepare carry for subtraction
LDA $1000   ;load value at address $1000 into A (low byte of first argument)
SBC $1002   ;subtract low byte of second argument at $1002
STA $1004   ;store low byte of result at $1004
LDA $1001   ;load high byte of first argument
SBC $1003   ;subtract high byte of second argument
STA $1005   ;store high byte of result (result in $1004 and $1005)
```
_Note:_ Another important preparatory step is to put the processor into binary mode using the `CLD` _(CLear Decimal flag)_ instruction. (See the section on decimal mode below.) This only needs to be done once.

<br>

### Signed Values

Operations for unsigned and signed values are principally the same; the only difference is in how we interpret the values. Generally, the 6502 uses what is known as _two's complement_ to represent negative values.

(Earlier computers used something known as _ones' complement_, where all bits are simply flipped to represent a negative value. While simple, this came with a few drawbacks — like an additional value of negative zero — which are overcome by two's complement.)

In two's complement representation, we simply flip all the bits in a byte to their opposite (the same as an XOR with `$FF`) and then add 1 to the result.

E.g., to represent -4:
(We use "$" to indicate a hexadecimal number and "%" for binary notation. A dot separates the high- and low-nibble, i.e. groups of 4 bits.)
```asm6502
    %0000.0100  ; 4 
XOR %1111.1111  ; 255 
-------------- 
    %1111.1011  ; complement (all bits flipped) 
 +           1 
-------------- 
    %1111.1100  ; -4, two's complement
```

Thus, in a single byte, we can represent values ranging from -128 (%1000.0000 or $80) to +127 (%0111.1111 or $7F).

A notable feature is that the highest-value bit (the leftmost bit) is always 1 for a negative value and always 0 for a positive one — for which it is also known as the _sign bit_. Whenever we interpret a value as a signed number, a set sign bit indicates a negative value.

This works just the same for larger values, e.g., for a signed 16-bit value:
```asm6502
-512 = %1111.1110.0000.0000 = $FE $00 
-516 = %1111.1101.1111.1100 = $FD $FC (mind how the +1 step carries over)
```

Notably, the underlying binary operations are still the same as with unsigned values, and provide the expected results:
```asm6502
  dec     binary     hex 

   00   %0110.0100   $64 
+ -24   %1110.1000   $E8 
------------------------ 
   76   %0100.1100   $4C   (+ carry)
```

_Note:_ We can now see how `SBC` actually works: by adding the _ones' complement_ of the operand to the accumulator. If we add 1 from the carry to the result, this effectively produces a subtraction in _two's complement_ (the inverse of the operand + 1). If the carry happens to be zero, the result falls short by 1 in terms of two's complement — equivalent to adding 1 to the operand before the subtraction. Thus, the carry either provides the correction required for a valid two's complement representation, or, if missing, results in a subtraction that includes a binary borrow.

<br>

### Flags with ADC and SBC

Besides the carry flag (C), which allows us to chain multi-byte operations, the CPU sets the following flags based on the result of an arithmetic operation:
```asm6502
zero flag (Z) ........ set if the result is zero, else unset  
negative flag (N) .... always reflects the sign bit of the result  
overflow flag (V) .... indicates overflow in signed operations
```

The overflow flag may need some explanation: how is signed overflow different from the carry flag? The overflow flag addresses a certain ambiguity of the sign bit and the negative flag in a signed context: if both operands share the same sign, a case may arise where the sign bit flips (as indicated by a change in the negative flag) even though the true result should still be of that same sign. This condition is indicated by the overflow flag. Notably, such an overflow can never occur when the operands are of opposite signs.

E.g., adding positive $40 to positive $40:
```asm6502
         acc.     acc.     flags
         hex     binary   NVDIZC

LDA #$40 $40  %0100.0000  000000
ADC #$40 $80  %1000.0000  110000
```

Here, the change of the sign bit doesn't reflect the true mathematical result — it's merely a consequence of carry propagation from bit 6 into bit 7, the sign bit. Since both operands are positive, the true result must be positive as well, so the overflow flag is set to signal that the sign bit is unreliable. The overflow flag (V) is meaningful only in a signed context, and has no meaning in an unsigned context.

<br>

### Decimal Mode (BCD)

Besides binary arithmetic, the 6502 processor supports a second mode: binary coded decimal (BCD), where each byte, rather than representing a range of 0…255, represents two decimal digits packed into a single byte. For this, a byte is divided into two sections of 4 bits — the high- and low-nibble. Only values from 0…9 are used for each nibble, so a byte can represent only a 2-digit decimal value, i.e. 0…99. E.g.,
```asm6502
dec    binary     hex

14   %0001.0100   $14
98   %1001.1000   $98
```

Notice how this translates intuitively to hexadecimal notation, where the
figures A…F are never used.

Whether the processor is in decimal mode is determined by the decimal flag
(D). If it is set (using `SED`), the processor will use BCD arithmetic. If it
is cleared (using `CLD`), the processor is in binary mode.
Decimal mode only affects the `ADC` and `SBC` instructions (not `INC` or `DEC`).

**Examples:**
```asm6502
SED
CLC
LDA #$12
ADC #$44 ;accumulator now holds $56

SED
CLC
LDA #$28
ADC #$14 ;accumulator now holds $42
```

Mind that BCD mode is always unsigned:
```asm6502
       acc.  NVDIZC 
SED 
SEC 
LDA #0 $00   001011 
SBC #1 $99   101000
```

The carry flag and zero flag work in decimal mode as expected. The negative flag is set similarly to binary mode (and is of questionable value there). The overflow flag has no meaning in decimal mode.

Multi-byte operations work the same way in decimal mode: we first prepare the carry, then chain operations on the individual bytes in increasing value order, starting with the lowest-value pair.

(It's worth noting that the Western Design Center (WDC) version of the processor, the 65C02, always clears the decimal flag when it enters an interrupt, while the original NMOS version of the 6502 does not.)

<br>
<br>
<br>

# Transfer Instructions
***
### `LDA` - Load Accumulator with Memory

| addressing   | assembler    | opc | bytes | cycles                                                                                                                   |
| ------------ | ------------ | --- | ----- | ------------------------------------------------------------------------------------------------------------------------ |
| immediate    | LDA \#oper   | A9  | 2     | 2                                                                                                                        |
| zeropage     | LDA oper     | A5  | 2     | 3                                                                                                                        |
| zeropage,X   | LDA oper,X   | B5  | 2     | 4                                                                                                                        |
| absolute     | LDA oper     | AD  | 3     | 4                                                                                                                        |
| absolute,X   | LDA oper,X   | BD  | 3     | 4* |
| absolute,Y   | LDA oper,Y   | B9  | 3     | 4* |
| (indirect,X) | LDA (oper,X) | A1  | 2     | 6                                                                                                                        |
| (indirect),Y | LDA (oper),Y | B1  | 2     | 5* |
- **Flags:** N Z C I D V -> `+ + - - - -`
- **Examples:**
    ```asm6502
    LDA #$07    ;load the literal value $07 into the accumulator
    LDA $3010   ;load the contents of address $3010 into the accumulator
    LDA $80,X   ;load the contents of address ($0080 + X) into the accumulator
    LDA ($70,X) ;load the contents of the address pointed to by ($0070 + X) into A
    LDA ($70),Y ;load the contents of the address (pointer at $0070) + Y into A
    ```

<br>

### `LDX` - Load Index X with Memory

| addressing | assembler  | opc | bytes | cycles                                                                                                                   |
| ---------- | ---------- | --- | ----- | ------------------------------------------------------------------------------------------------------------------------ |
| immediate  | LDX \#oper | A2  | 2     | 2                                                                                                                        |
| zeropage   | LDX oper   | A6  | 2     | 3                                                                                                                        |
| zeropage,Y | LDX oper,Y | B6  | 2     | 4                                                                                                                        |
| absolute   | LDX oper   | AE  | 3     | 4                                                                                                                        |
| absolute,Y | LDX oper,Y | BE  | 3     | 4* |
- **Flags:** N Z C I D V -> `+ + - - - -`
- **Examples:**
    ```asm6502
    LDX #$0A    ;load the literal value $0A into the X register
    LDX $60     ;load the contents of address $0060 into X
    LDX $60,Y   ;load the contents of address ($0060 + Y) into X
    LDX $8240,Y ;load the contents of address ($8240 + Y) into X
    ```

<br>

### `LDY` - Load Index Y with Memory

| addressing | assembler  | opc | bytes | cycles                                                                                                                   |
| ---------- | ---------- | --- | ----- | ------------------------------------------------------------------------------------------------------------------------ |
| immediate  | LDY \#oper | A0  | 2     | 2                                                                                                                        |
| zeropage   | LDY oper   | A4  | 2     | 3                                                                                                                        |
| zeropage,X | LDY oper,X | B4  | 2     | 4                                                                                                                        |
| absolute   | LDY oper   | AC  | 3     | 4                                                                                                                        |
| absolute,X | LDY oper,X | BC  | 3     | 4* |
- **Flags:** N Z C I D V -> `+ + - - - -`
- **Examples:**
    ```asm6502
    LDY #$0A    ;load the literal value $0A into the Y register
    LDY $A2     ;load the contents of address $00A2 into Y
    LDY $80,X   ;load the contents of address ($0080 + X) into Y
    LDY $3120,X ;load the contents of address ($3120 + X) into Y
    ```

<br>

### `STA` - Store Accumulator in Memory

|addressing|assembler|opc|bytes|cycles|
|---|---|---|---|---|
|zeropage|STA oper|85|2|3|
|zeropage,X|STA oper,X|95|2|4|
|absolute|STA oper|8D|3|4|
|absolute,X|STA oper,X|9D|3|5|
|absolute,Y|STA oper,Y|99|3|5|
|(indirect,X)|STA (oper,X)|81|2|6|
|(indirect),Y|STA (oper),Y|91|2|6|
- **Flags:** N Z C I D V -> `- - - - - -`
- **Examples:**
    ```asm6502
    STA $80      ;store the contents of the accumulator at address $0080
    STA $3010    ;store the contents of the accumulator at address $3010
    STA $A2,X    ;store the contents of A at address ($00A2 + X)
    STA ($A2,X)  ;store A at the address pointed to by ($00A2 + X)
    STA ($A2),Y  ;store A at the address (pointer at $00A2) + Y
    ```

<br>

### `STX` - Store Index X in Memory

| addressing | assembler  | opc | bytes | cycles |
| ---------- | ---------- | --- | ----- | ------ |
| zeropage   | STX oper   | 86  | 2     | 3      |
| zeropage,X | STX oper,X | 96  | 2     | 4      |
| absolute   | STX oper   | 8E  | 3     | 4      |
- **Flags:** N Z C I D V -> `- - - - - -`
- **Examples:**
    ```asm6502
    STX $60     ;store the contents of X at address $0060
    STX $60,Y   ;store the contents of X at address ($0060 + Y)
    STX $8240   ;store the contents of X at address $8240
    ```

<br>

### `STY` - Store Index Y in Memory

|addressing|assembler|opc|bytes|cycles|
|---|---|---|---|---|
|zeropage|STY oper|84|2|3|
|zeropage,X|STY oper,X|94|2|4|
|absolute|STY oper|8C|3|4|
- **Flags:** N Z C I D V -> `- - - - - -`
- **Examples:**
    ```asm6502
    STY $A2     ;store the contents of Y at address $00A2
    STY $A2,X   ;store the contents of Y at address ($00A2 + X)
    STY $3120   ;store the contents of Y at address $3120
    ```

<br>

### `TAX` - Transfer Accumulator to Index X

|addressing|assembler|opc|bytes|cycles|
|---|---|---|---|---|
|implied|TAX|AA|1|2|
- **Flags:** N Z C I D V -> `+ + - - - -`

<br>

### `TAY` - Transfer Accumulator to Index Y

|addressing|assembler|opc|bytes|cycles|
|---|---|---|---|---|
|implied|TAY|A8|1|2|
- **Flags:** N Z C I D V -> `+ + - - - -`

<br>

### `TSX` - Transfer Stack Pointer to Index X

| addressing | assembler | opc | bytes | cycles |
| ---------- | --------- | --- | ----- | ------ |
| implied    | TSX       | BA  | 1     | 2      |
- **Flags:** N Z C I D V -> `+ + - - - -`

<br>

### `TXA` - Transfer Index X to Accumulator

| addressing | assembler | opc | bytes | cycles |
| ---------- | --------- | --- | ----- | ------ |
| implied    | TXA       | 8A  | 1     | 2      |
- **Flags:** N Z C I D V -> `+ + - - - -`

<br>

### `TXS` - Transfer Index X to Stack Register

| addressing | assembler | opc | bytes | cycles |
| ---------- | --------- | --- | ----- | ------ |
| implied    | TXS       | 9A  | 1     | 2      |
- **Flags:** N Z C I D V -> `- - - - - -`

<br>

### `TYA` - Transfer Index Y to Accumulator

| addressing | assembler | opc | bytes | cycles |
| ---------- | --------- | --- | ----- | ------ |
| implied    | TYA       | 98  | 1     | 2      |
- **Flags:** N Z C I D V -> `+ + - - - -`

<br>
<br>
<br>

# Stack Instructions
***
These instructions transfer the accumulator or status register (flags) to and from the stack. The processor stack is a last-in-first-out (LIFO) stack of 256 bytes, implemented at addresses $0100–$01FF. The stack grows downward as new values are pushed onto it, with the current insertion point maintained in the stack pointer register.
(When a byte is pushed onto the stack, it is stored at the address indicated by the current value of the stack pointer, which is then decremented by 1. Conversely, when a value is pulled from the stack, the stack pointer is incremented first. The stack pointer is accessible via the TSX and TXS instructions.)

<br>

### `PHA` - Push Accumulator on Stack

| addressing | assembler | opc | bytes | cycles |
| ---------- | --------- | --- | ----- | ------ |
| implied    | PHA       | 48  | 1     | 3      |
- **Flags:** N Z C I D V -> `- - - - - -`

<br>

### `PHP` - Push Processor Status on Stack

| addressing | assembler | opc | bytes | cycles |
| ---------- | --------- | --- | ----- | ------ |
| implied    | PHP       | 08  | 1     | 3      |
- **Flags:** N Z C I D V -> `- - - - - -`

<br>

### `PLA` - Pull Accumulator from Stack

| addressing | assembler | opc | bytes | cycles |
| ---------- | --------- | --- | ----- | ------ |
| implied    | PLA       | 68  | 1     | 4      |
- **Flags:** N Z C I D V -> `+ + - - - -`

<br>

### `PLP` - Pull Processor Status from Stack

| addressing | assembler | opc | bytes | cycles |
| ---------- | --------- | --- | ----- | ------ |
| implied    | PLP       | 28  | 1     | 4      |
- **Flags:** N Z C I D V -> `+ + - - - -`

<br>
<br>
<br>

# Decrement and Increment Instructions
***
### `DEC` - Decrement Memory by One

|addressing|assembler|opc|bytes|cycles|
|---|---|---|---|---|
|zeropage|DEC oper|C6|2|5|
|zeropage,X|DEC oper,X|D6|2|6|
|absolute|DEC oper|CE|3|6|
|absolute,X|DEC oper,X|DE|3|7|
- **Flags:** N Z C I D V -> `+ + - - - -`
- **Examples:**
    ```asm6502
    DEC $80     ;decrement the contents of address $0080 by one
    DEC $80,X   ;decrement the contents of address ($0080 + X) by one
    DEC $3010   ;decrement the contents of address $3010 by one
    DEC $3010,X ;decrement the contents of address ($3010 + X) by one
    ```

<br>

### `DEX` - Decrement Index X by One

| addressing | assembler | opc | bytes | cycles |
| ---------- | --------- | --- | ----- | ------ |
| implied    | DEX       | CA  | 1     | 2      |
- **Flags:** N Z C I D V -> `+ + - - - -`

<br>

### `DEY` - Decrement Index Y by One

| addressing | assembler | opc | bytes | cycles |
| ---------- | --------- | --- | ----- | ------ |
| implied    | DEY       | 88  | 1     | 2      |
- **Flags:** N Z C I D V -> `+ + - - - -`

<br>

### `INC` - Increment Memory by One

| addressing | assembler  | opc | bytes | cycles |
| ---------- | ---------- | --- | ----- | ------ |
| zeropage   | INC oper   | E6  | 2     | 5      |
| zeropage,X | INC oper,X | F6  | 2     | 6      |
| absolute   | INC oper   | EE  | 3     | 6      |
| absolute,X | INC oper,X | FE  | 3     | 7      |
- **Flags:** N Z C I D V -> `+ + - - - -`
- **Examples:**
    ```asm6502
    INC $80     ;increment the contents of address $0080 by one
    INC $80,X   ;increment the contents of address ($0080 + X) by one
    INC $3010   ;increment the contents of address $3010 by one
    INC $3010,X ;increment the contents of address ($3010 + X) by one
    ```

<br>

### `INX` - Increment Index X by One

| addressing | assembler | opc | bytes | cycles |
| ---------- | --------- | --- | ----- | ------ |
| implied    | INX       | E8  | 1     | 2      |
- **Flags:** N Z C I D V -> `+ + - - - -`

<br>

### `INY` - Increment Index Y by One

| addressing | assembler | opc | bytes | cycles |
| ---------- | --------- | --- | ----- | ------ |
| implied    | INY       | C8  | 1     | 2      |
- **Flags:** N Z C I D V -> `+ + - - - -`

<br>
<br>
<br>

# Arithmetic Instructions
***
### `ADC` - Add Memory to Accumulator with Carry

| addressing   | assembler    | opc | bytes | cycles                                                                                                                   |
| ------------ | ------------ | --- | ----- | ------------------------------------------------------------------------------------------------------------------------ |
| immediate    | ADC \#oper   | 69  | 2     | 2                                                                                                                        |
| zeropage     | ADC oper     | 65  | 2     | 3                                                                                                                        |
| zeropage,X   | ADC oper,X   | 75  | 2     | 4                                                                                                                        |
| absolute     | ADC oper     | 6D  | 3     | 4                                                                                                                        |
| absolute,X   | ADC oper,X   | 7D  | 3     | 4* |
| absolute,Y   | ADC oper,Y   | 79  | 3     | 4* |
| (indirect,X) | ADC (oper,X) | 61  | 2     | 6                                                                                                                        |
| (indirect),Y | ADC (oper),Y | 71  | 2     | 5* |
- **Flags:** N Z C I D V -> `+ + + - - +`
- **Examples:**
    ```asm6502
    CLC         ;clear carry before adding
    ADC #$10    ;add the literal value $10 to the accumulator
    ADC $80     ;add the contents of address $0080 to the accumulator
    ADC $80,X   ;add the contents of address ($0080 + X) to the accumulator
    ADC $3010   ;add the contents of address $3010 to the accumulator
    ADC $3010,X ;add the contents of address ($3010 + X) to the accumulator
    ADC $3010,Y ;add the contents of address ($3010 + Y) to the accumulator
    ADC ($70,X) ;add the contents of the address pointed to by ($0070 + X) to A
    ADC ($70),Y ;add the contents of the address (pointer at $0070) + Y to A
    ```

<br>

### `SBC` - Subtract Memory from Accumulator with Borrow

| addressing   | assembler    | opc | bytes | cycles                                                                                                                   |
| ------------ | ------------ | --- | ----- | ------------------------------------------------------------------------------------------------------------------------ |
| immediate    | SBC \#oper   | E9  | 2     | 2                                                                                                                        |
| zeropage     | SBC oper     | E5  | 2     | 3                                                                                                                        |
| zeropage,X   | SBC oper,X   | F5  | 2     | 4                                                                                                                        |
| absolute     | SBC oper     | ED  | 3     | 4                                                                                                                        |
| absolute,X   | SBC oper,X   | FD  | 3     | 4* |
| absolute,Y   | SBC oper,Y   | F9  | 3     | 4* |
| (indirect,X) | SBC (oper,X) | E1  | 2     | 6                                                                                                                        |
| (indirect),Y | SBC (oper),Y | F1  | 2     | 5* |
- **Flags:** N Z C I D V -> `+ + + - - +`
- **Examples:**
    ```asm6502
    SEC         ;set carry before subtracting
    SBC #$10    ;subtract the literal value $10 from the accumulator
    SBC $80     ;subtract the contents of address $0080 from the accumulator
    SBC $80,X   ;subtract the contents of address ($0080 + X) from the accumulator
    SBC $3010   ;subtract the contents of address $3010 from the accumulator
    SBC $3010,X ;subtract the contents of address ($3010 + X) from the accumulator
    SBC $3010,Y ;subtract the contents of address ($3010 + Y) from the accumulator
    SBC ($70,X) ;subtract the contents of the address pointed to by ($0070 + X) from A
    SBC ($70),Y ;subtract the contents of the address (pointer at $0070) + Y from A
    ```
    
<br>
<br>
<br>

# Logical Operations
***
### `AND` - AND Memory with Accumulator

| addressing   | assembler    | opc | bytes | cycles                                                                                                                   |
| ------------ | ------------ | --- | ----- | ------------------------------------------------------------------------------------------------------------------------ |
| immediate    | AND \#oper   | 29  | 2     | 2                                                                                                                        |
| zeropage     | AND oper     | 25  | 2     | 3                                                                                                                        |
| zeropage,X   | AND oper,X   | 35  | 2     | 4                                                                                                                        |
| absolute     | AND oper     | 2D  | 3     | 4                                                                                                                        |
| absolute,X   | AND oper,X   | 3D  | 3     | 4* |
| absolute,Y   | AND oper,Y   | 39  | 3     | 4* |
| (indirect,X) | AND (oper,X) | 21  | 2     | 6                                                                                                                        |
| (indirect),Y | AND (oper),Y | 31  | 2     | 5* |
- **Flags:** N Z C I D V -> `+ + - - - -`
- **Examples:**
    ```asm6502
    AND #$0F    ;mask the accumulator, keeping only the low nibble
    AND $80     ;AND the accumulator with the contents of address $0080
    AND $80,X   ;AND the accumulator with the contents of address ($0080 + X)
    AND $3010   ;AND the accumulator with the contents of address $3010
    AND $3010,X ;AND the accumulator with the contents of address ($3010 + X)
    AND $3010,Y ;AND the accumulator with the contents of address ($3010 + Y)
    AND ($70,X) ;AND the accumulator with the contents of the address pointed to by ($0070 + X)
    AND ($70),Y ;AND the accumulator with the contents of the address (pointer at $0070) + Y
    ```

<br>

### `EOR` - Exclusive-OR Memory with Accumulator

| addressing   | assembler    | opc | bytes | cycles |
| ------------ | ------------ | --- | ----- | ------ |
| immediate    | EOR \#oper   | 49  | 2     | 2      |
| zeropage     | EOR oper     | 45  | 2     | 3      |
| zeropage,X   | EOR oper,X   | 55  | 2     | 4      |
| absolute     | EOR oper     | 4D  | 3     | 4      |
| absolute,X   | EOR oper,X   | 5D  | 3     | 4*     |
| absolute,Y   | EOR oper,Y   | 59  | 3     | 4*     |
| (indirect,X) | EOR (oper,X) | 41  | 2     | 6      |
| (indirect),Y | EOR (oper),Y | 51  | 2     | 5*     |
- **Flags:** N Z C I D V -> `+ + - - - -`
- **Examples:**
    ```asm6502
    EOR #$FF    ;flip every bit in the accumulator
    EOR $80     ;EOR the accumulator with the contents of address $0080
    EOR $80,X   ;EOR the accumulator with the contents of address ($0080 + X)
    EOR $3010   ;EOR the accumulator with the contents of address $3010
    EOR $3010,X ;EOR the accumulator with the contents of address ($3010 + X)
    EOR $3010,Y ;EOR the accumulator with the contents of address ($3010 + Y)
    EOR ($70,X) ;EOR the accumulator with the contents of the address pointed to by ($0070 + X)
    EOR ($70),Y ;EOR the accumulator with the contents of the address (pointer at $0070) + Y
    ```

<br>

### `ORA` - OR Memory with Accumulator

| addressing   | assembler    | opc | bytes | cycles |
| ------------ | ------------ | --- | ----- | ------ |
| immediate    | ORA \#oper   | 09  | 2     | 2      |
| zeropage     | ORA oper     | 05  | 2     | 3      |
| zeropage,X   | ORA oper,X   | 15  | 2     | 4      |
| absolute     | ORA oper     | 0D  | 3     | 4      |
| absolute,X   | ORA oper,X   | 1D  | 3     | 4*     |
| absolute,Y   | ORA oper,Y   | 19  | 3     | 4*     |
| (indirect,X) | ORA (oper,X) | 01  | 2     | 6      |
| (indirect),Y | ORA (oper),Y | 11  | 2     | 5*     |
- **Flags:** N Z C I D V -> `+ + - - - -`
- **Examples:**
    ```asm6502
    ORA #$80    ;set the high bit of the accumulator
    ORA $80     ;OR the accumulator with the contents of address $0080
    ORA $80,X   ;OR the accumulator with the contents of address ($0080 + X)
    ORA $3010   ;OR the accumulator with the contents of address $3010
    ORA $3010,X ;OR the accumulator with the contents of address ($3010 + X)
    ORA $3010,Y ;OR the accumulator with the contents of address ($3010 + Y)
    ORA ($70,X) ;OR the accumulator with the contents of the address pointed to by ($0070 + X)
    ORA ($70),Y ;OR the accumulator with the contents of the address (pointer at $0070) + Y
    ```

<br>
<br>
<br>

# Shift & Rotate Instructions
***
All shift and rotate instructions preserve the bit shifted out in the carry flag.

<br>

### `ASL` - Shift Left One Bit

| addressing  | assembler  | opc | bytes | cycles |
| ----------- | ---------- | --- | ----- | ------ |
| accumulator | ASL A      | 0A  | 1     | 2      |
| zeropage    | ASL oper   | 06  | 2     | 5      |
| zeropage,X  | ASL oper,X | 16  | 2     | 6      |
| absolute    | ASL oper   | 0E  | 3     | 6      |
| absolute,X  | ASL oper,X | 1E  | 3     | 7      |
- **Flags:** N Z C I D V -> `+ + + - - -`
- **Examples:**
    ```asm6502
    ASL A       ;shift the accumulator left by one bit; bit 7 goes into carry
    ASL $80     ;shift the contents of address $0080 left by one bit
    ASL $80,X   ;shift the contents of address ($0080 + X) left by one bit
    ASL $3010   ;shift the contents of address $3010 left by one bit
    ASL $3010,X ;shift the contents of address ($3010 + X) left by one bit
    ```

<br>

### `LSR` - Shift Right One Bit

| addressing  | assembler  | opc | bytes | cycles |
| ----------- | ---------- | --- | ----- | ------ |
| accumulator | LSR A      | 4A  | 1     | 2      |
| zeropage    | LSR oper   | 46  | 2     | 5      |
| zeropage,X  | LSR oper,X | 56  | 2     | 6      |
| absolute    | LSR oper   | 4E  | 3     | 6      |
| absolute,X  | LSR oper,X | 5E  | 3     | 7      |
- **Flags:** N Z C I D V -> `0 + + - - -`
- **Examples:**
    ```asm6502
    LSR A       ;shift the accumulator right by one bit; bit 0 goes into carry
    LSR $80     ;shift the contents of address $0080 right by one bit
    LSR $80,X   ;shift the contents of address ($0080 + X) right by one bit
    LSR $3010   ;shift the contents of address $3010 right by one bit
    LSR $3010,X ;shift the contents of address ($3010 + X) right by one bit
    ```

<br>

### `ROL` - Rotate One Bit Left

| addressing  | assembler  | opc | bytes | cycles |
| ----------- | ---------- | --- | ----- | ------ |
| accumulator | ROL A      | 2A  | 1     | 2      |
| zeropage    | ROL oper   | 26  | 2     | 5      |
| zeropage,X  | ROL oper,X | 36  | 2     | 6      |
| absolute    | ROL oper   | 2E  | 3     | 6      |
| absolute,X  | ROL oper,X | 3E  | 3     | 7      |
- **Flags:** N Z C I D V -> `+ + + - - -`
- **Examples:**
    ```asm6502
    ROL A       ;rotate the accumulator left by one bit, carry in from bit 0, bit 7 into carry
    ROL $80     ;rotate the contents of address $0080 left by one bit
    ROL $80,X   ;rotate the contents of address ($0080 + X) left by one bit
    ROL $3010   ;rotate the contents of address $3010 left by one bit
    ROL $3010,X ;rotate the contents of address ($3010 + X) left by one bit
    ```

<br>

### `ROR` - Rotate One Bit Right

| addressing  | assembler  | opc | bytes | cycles |
| ----------- | ---------- | --- | ----- | ------ |
| accumulator | ROR A      | 6A  | 1     | 2      |
| zeropage    | ROR oper   | 66  | 2     | 5      |
| zeropage,X  | ROR oper,X | 76  | 2     | 6      |
| absolute    | ROR oper   | 6E  | 3     | 6      |
| absolute,X  | ROR oper,X | 7E  | 3     | 7      |
- **Flags:** N Z C I D V -> `+ + + - - -`
- **Examples:**
    ```asm6502
    ROR A       ;rotate the accumulator right by one bit, carry in from bit 7, bit 0 into carry
    ROR $80     ;rotate the contents of address $0080 right by one bit
    ROR $80,X   ;rotate the contents of address ($0080 + X) right by one bit
    ROR $3010   ;rotate the contents of address $3010 right by one bit
    ROR $3010,X ;rotate the contents of address ($3010 + X) right by one bit
    ```

<br>
<br>
<br>

# Flag Instructions
***
### `CLC` - Clear Carry Flag

| addressing | assembler | opc | bytes | cycles |
| ---------- | --------- | --- | ----- | ------ |
| implied    | CLC       | 18  | 1     | 2      |
- **Flags:** N Z C I D V -> `- - 0 - - -`

<br>

### `CLD` - Clear Decimal Mode

| addressing | assembler | opc | bytes | cycles |
| ---------- | --------- | --- | ----- | ------ |
| implied    | CLD       | D8  | 1     | 2      |
- **Flags:** N Z C I D V -> `- - - - 0 -`

<br>

### `CLI` - Clear Interrupt Disable Bit

| addressing | assembler | opc | bytes | cycles |
| ---------- | --------- | --- | ----- | ------ |
| implied    | CLI       | 58  | 1     | 2      |
- **Flags:** N Z C I D V -> `- - - 0 - -`

<br>

### `CLV` - Clear Overflow Flag

| addressing | assembler | opc | bytes | cycles |
| ---------- | --------- | --- | ----- | ------ |
| implied    | CLV       | B8  | 1     | 2      |
- **Flags:** N Z C I D V -> `- - - - - 0`

<br>

### `SEC` - Set Carry Flag

| addressing | assembler | opc | bytes | cycles |
| ---------- | --------- | --- | ----- | ------ |
| implied    | SEC       | 38  | 1     | 2      |
- **Flags:** N Z C I D V -> `- - 1 - - -`

<br>

### `SED` - Set Decimal Flag

| addressing | assembler | opc | bytes | cycles |
| ---------- | --------- | --- | ----- | ------ |
| implied    | SED       | F8  | 1     | 2      |
- **Flags:** N Z C I D V -> `- - - - 1 -`

<br>

### `SEI` - Set Interrupt Disable Status

| addressing | assembler | opc | bytes | cycles |
| ---------- | --------- | --- | ----- | ------ |
| implied    | SEI       | 78  | 1     | 2      |
- **Flags:** N Z C I D V -> `- - - 1 - -`

<br>
<br>
<br>

# Comparison Instructions
***
The 6502 MPU features three basic compare instructions in various address modes:

| Instruction | Comparison              |
| ----------- | ----------------------- |
| CMP         | Accumulator and operand |
| CPX         | X register and operand  |
| CPY         | Y register and operand  |

The compare instructions subtract the operand from the respective register (as if the carry were set) without storing the result — the register's contents remain unchanged — and adjust the N, Z, and C flags as with any ordinary subtraction.

Flags are set as follows:

|Relation|Z|C|N|
|---|---|---|---|
|register < operand|0|0|_sign-bit of result_|
|register = operand|1|1|0|
|register > operand|0|1|_sign-bit of result_|

This means we can determine the derivative relation _"greater than or equal"_ (gte) by checking just the carry flag (using the `BCS` instruction):

|Relation|Z|C|N|
|---|---|---|---|
|register ≥ operand|_x_|1|_sign-bit of result_|

(For why the carry flag behaves this way, see the notes on subtraction, above.) 
Note that the negative flag is not significant here, and all conditions can be evaluated by checking the carry and/or zero flag(s) alone.

<br>

### `CMP` - Compare Memory with Accumulator

| addressing   | assembler    | opc | bytes | cycles |
| ------------ | ------------ | --- | ----- | ------ |
| immediate    | CMP \#oper   | C9  | 2     | 2      |
| zeropage     | CMP oper     | C5  | 2     | 3      |
| zeropage,X   | CMP oper,X   | D5  | 2     | 4      |
| absolute     | CMP oper     | CD  | 3     | 4      |
| absolute,X   | CMP oper,X   | DD  | 3     | 4*     |
| absolute,Y   | CMP oper,Y   | D9  | 3     | 4*     |
| (indirect,X) | CMP (oper,X) | C1  | 2     | 6      |
| (indirect),Y | CMP (oper),Y | D1  | 2     | 5*     |
- **Flags:** N Z C I D V -> `+ + + - - -`
- **Examples:**
    ```asm6502
    CMP #$40    ;compare the accumulator to the literal value $40
    CMP $80     ;compare the accumulator to the contents of address $0080
    CMP $80,X   ;compare the accumulator to the contents of address ($0080 + X)
    CMP $3010   ;compare the accumulator to the contents of address $3010
    CMP $3010,X ;compare the accumulator to the contents of address ($3010 + X)
    CMP $3010,Y ;compare the accumulator to the contents of address ($3010 + Y)
    CMP ($70,X) ;compare the accumulator to the contents of the address pointed to by ($0070 + X)
    CMP ($70),Y ;compare the accumulator to the contents of the address (pointer at $0070) + Y
    ```

<br>

### `CPX` - Compare Memory and Index X

| addressing | assembler  | opc | bytes | cycles |
| ---------- | ---------- | --- | ----- | ------ |
| immediate  | CPX \#oper | E0  | 2     | 2      |
| zeropage   | CPX oper   | E4  | 2     | 3      |
| absolute   | CPX oper   | EC  | 3     | 4      |
- **Flags:** N Z C I D V -> `+ + + - - -`
- **Examples:**
    ```asm6502
    CPX #$05  ;compare the X register to the literal value $05
    CPX $80   ;compare the X register to the contents of address $0080
    CPX $3010 ;compare the X register to the contents of address $3010
    ```

<br>

### `CPY` - Compare Memory and Index Y

| addressing | assembler  | opc | bytes | cycles |
| ---------- | ---------- | --- | ----- | ------ |
| immediate  | CPY \#oper | C0  | 2     | 2      |
| zeropage   | CPY oper   | C4  | 2     | 3      |
| absolute   | CPY oper   | CC  | 3     | 4      |
- **Flags:** N Z C I D V -> `+ + + - - -`
- **Examples:**
    ```asm6502
    CPY #$05  ;compare the Y register to the literal value $05
    CPY $80   ;compare the Y register to the contents of address $0080
    CPY $3010 ;compare the Y register to the contents of address $3010
    ```

<br>
<br>
<br>

# Bit Instruction
***
The `BIT` instruction is somewhat similar to `CMP`, but performs a bit-wise comparison between the contents of the accumulator and a memory location given as the operand. 

`BIT` performs a logical AND between the two values and sets the zero flag according to the result. Additionally, bit #7 (the sign bit) and bit #6 of the operand are transferred to the corresponding bits of the status register — the negative flag and the o**V**erflow flag, respectively. (Thus, these two bits can easily be used to store and set flags for conditional branches; see below.) The contents of the accumulator remain unaffected.

`BIT` may be the most obscure instruction on the 6502: while other instructions serve a very clear purpose, like transferring values or performing basic arithmetic or logical operations, this one serves a rather specialized purpose — but does so in a very general way. That purpose is bit testing. 

Generally, testing a particular bit is achieved by masking (isolating) that bit (or multiple bits) with an AND operation, then checking the zero flag (Z) with a `BNE` or `BEQ` instruction. This, however, destroys the contents of the accumulator. 

This is where `BIT` comes in: much like the comparison instructions perform a subtraction without storing the result, `BIT` performs a logical AND without storing the result, but still reflects that result in the state of the zero flag (Z). This allows the same kind of check using `BNE` or `BEQ`, without affecting the contents of the accumulator. 

Since the sign bit is often used as a flag, testing it is also covered by `BIT`: in addition to setting the zero flag, it transfers bits 7 and 6 of the operand into the corresponding bits of the status register — which happen to be the negative (N) and overflow (V) flags. This means bits 7 and 6 of the operand can be tested independently using the `BMI`/`BPL` and `BVS`/`BVC` instructions.

```asm6502
accumulator        operand
[76543210]   AND   [76543210] == 0 ? 
                    ↓↓         ↓ 
                    NV         Z
```

An interesting use of the `BIT` instruction can be seen in MS/Commodore BASIC:
```asm6502
        ;a condition has been previously evaluated 
        ;by setting the carry, now set a flag… 
        
        BCS SETFLAG   ;set a flag in location "FLAG" 
        (...) 

SETFLAG ROR FLAG      ;rotate carry into sign position 
                      ;previous sign-bit now in bit 6 
        BIT FLAG      ;bit 6 (prev. sign) into overflow flag (V) 
        BVS ABORT     ;was the flag set already? 
        (...)         ;no: adjust to condition… 
        JMP CONTINUE  ;done, continue with task… 
ABORT   (...)         ;flag set twice, abort the operation…
```

This is easily modified to check the state of `FLAG` first instead:
```asm6502
        BCS SETFLAG   ;set a flag… 
        (...) 
SETFLAG BIT FLAG      ;sign-bit into negative flag (N) 
        BMI ABORT     ;is the flag set already? 
        ROR FLAG      ;no: rotate carry into sign position 
                      ;(carry is left untouched by BIT) 
        (...)         ;adjust to condition… 
        JMP CONTINUE  ;done 
ABORT   (...)         ;flag already set, abort…
```

In both cases, we don't care about the AND operation itself or its effect on the zero flag (Z) — only about the bit transfer into the V or N flag, respectively.

<br>

### `BIT` - Test Bits in Memory with Accumulator

| addressing | assembler | opc | bytes | cycles |
| ---------- | --------- | --- | ----- | ------ |
| zeropage   | BIT oper  | 24  | 2     | 3      |
| absolute   | BIT oper  | 2C  | 3     | 4      |
- **Flags:** N Z C I D V -> `M7 + - - - M6`
- **Examples:**
    ```asm6502
    BIT $80   ;AND accumulator with contents of $0080
            ;   set Z, N (from bit 7), V (from bit 6)
    BIT $3010 ;AND accumulator with contents of $3010
            ;   set Z, N (from bit 7), V (from bit 6)
    ```

<br>
<br>
<br>

# Conditional Branch Instructions
***
Branch targets are relative, signed 8-bit address offsets. An offset of zero corresponds to the immediately following address. While it is perfectly feasible to calculate offsets by hand, more often these are computed by an assembler program from absolute addresses or labels. In the latter case, branch instructions may look more like absolute address mode instructions, while actually taking just a relative offset as a single-byte operand.

<br>

### `BCC` - Branch on Carry Clear

| addressing | assembler | opc | bytes | cycles                                                                                                                                                                            |
| ---------- | --------- | --- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| relative   | BCC oper  | 90  | 2     | 2** |
- **Flags:** N Z C I D V -> `- - - - - -`

<br>

### `BCS` - Branch on Carry Set

| addressing | assembler | opc | bytes | cycles                                                                                                                                                                            |
| ---------- | --------- | --- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| relative   | BCS oper  | B0  | 2     | 2** |
- **Flags:** N Z C I D V -> `- - - - - -`

<br>

### `BEQ` - Branch on Result Zero

| addressing | assembler | opc | bytes | cycles                                                                                                                                                                            |
| ---------- | --------- | --- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| relative   | BEQ oper  | F0  | 2     | 2** |
- **Flags:** N Z C I D V -> `- - - - - -`

<br>

### `BMI` - Branch on Result Minus

| addressing | assembler | opc | bytes | cycles                                                                                                                                                                            |
| ---------- | --------- | --- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| relative   | BMI oper  | 30  | 2     | 2** |
- **Flags:** N Z C I D V -> `- - - - - -`

<br>

### `BNE` - Branch on Result not Zero

| addressing | assembler | opc | bytes | cycles                                                                                                                                                                            |
| ---------- | --------- | --- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| relative   | BNE oper  | D0  | 2     | 2** |
- **Flags:** N Z C I D V -> `- - - - - -`

<br>

### `BPL` - Branch on Result Plus

| addressing | assembler | opc | bytes | cycles                                                                                                                                                                            |
| ---------- | --------- | --- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| relative   | BPL oper  | 10  | 2     | 2** |
- **Flags:** N Z C I D V -> `- - - - - -`

<br>

### `BVC` - Branch on Overflow Clear

| addressing | assembler | opc | bytes | cycles                                                                                                                                                                            |
| ---------- | --------- | --- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| relative   | BVC oper  | 50  | 2     | 2** |
- **Flags:** N Z C I D V -> `- - - - - -`

<br>

### `BVS` - Branch on Overflow Set

| addressing | assembler | opc | bytes | cycles                                                                                                                                                                            |
| ---------- | --------- | --- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| relative   | BVS oper  | 70  | 2     | 2** |
- **Flags:** N Z C I D V -> `- - - - - -`

<br>
<br>
<br>

# Jump and Subroutine Instructions
***
`JSR` and `RTS` affect the stack, as the return address is pushed onto or pulled from the stack, respectively. (`JSR` first pushes the high byte of the return address [PC+2] onto the stack, then the low byte. The stack will then contain, seen from the bottom — i.e. from the most recently added byte — [PC+2]-L, [PC+2]-H.)

The 256-byte processor stack of the 6502 is located at $0100…$01FF in memory, growing downward from top to bottom. 

There are three 2-byte address locations at the very top of the 64K address space, serving as jump vectors for reset/startup and interrupt operations:
```asm6502
$FFFA, $FFFB ... NMI (Non-Maskable Interrupt) vector  
$FFFC, $FFFD ... RES (Reset) vector  
$FFFE, $FFFF ... IRQ (Interrupt Request) vector
```

When an interrupt occurs, any instruction currently being processed completes first. Only then is the value of the program counter (PC) pushed onto the stack in high-low order, followed by the value currently in the status register, and control is transferred to the address found in the respective interrupt vector. The registers stored on the stack are restored at the end of the interrupt routine, as control is transferred back to the interrupted code by the `RTI` instruction. 

Similarly, when a `JSR` instruction is encountered, the PC is pushed onto the stack and later restored by the `RTS` instruction. (Here, the value actually stored is the address of the instruction *before* the location the program will eventually return to. Thus, the effective return address is PC+1.)

<br>

### `JMP` - Jump to New Location
| addressing | assembler  | opc | bytes | cycles  |
| ---------- | ---------- | --- | ----- | ------- |
| absolute   | JMP oper   | 4C  | 3     | 3       |
| indirect   | JMP (oper) | 6C  | 3     | 5\*\*\* |
- **Flags:** N Z C I D V -> `- - - - - -`
- **Notes:**
	- operand 1st byte -> PCL (Low Byte)
	- operand 2nd byte -> PCH (High Byte)
- **Examples:**
    ```asm6502
    JMP $4000   ;jump directly to address $4000
    JMP ($FF82) ;jump to the address stored in the word at $FF82/$FF83
    JMP ($10FF) ;NMOS 6502: high byte incorrectly fetched from $1000, not $1100
    ```

<br>

### `JSR` - Jump to New Location Saving Return Address
|addressing|assembler|opc|bytes|cycles|
|---|---|---|---|---|
|absolute|JSR oper|20|3|6|
- **Flags:** N Z C I D V -> `- - - - - -`
- Notes:
	- will `push (PC+2)` (Save current address to return to)
	- operand 1st byte -> PCL (Low Byte)
	- operand 2nd byte -> PCH (High Byte)

<br>

### `RTS` - Return from Subroutine
| addressing | assembler | opc | bytes | cycles |
| ---------- | --------- | --- | ----- | ------ |
| implied    | RTS       | 60  | 1     | 6      |
- **Flags:** N Z C I D V -> `- - - - - -`
- Notes:
	- will `pull PC, PC+1 -> PC` (Going back to address after `JSR` call)

<br>
<br>
<br>

# Interrupt Instructions
***
### `BRK` - Force Break
|addressing|assembler|opc|bytes|cycles|
|---|---|---|---|---|
|implied|BRK|00|1|7|
- **Flags:** N Z C I D V -> `- - - 1 - -`
- Notes:
	- Does the following when called:
		- interrupt
		- push PC+2 (save execution location)
		- push SR (save the processor status at the time of the break)

<br>

### `RTI` - Return from Interrupt
| addressing | assembler | opc | bytes | cycles |
| ---------- | --------- | --- | ----- | ------ |
| implied    | RTI       | 40  | 1     | 6      |
- **Flags:** set from stack
- Notes:
	- Will pull Status Register (SR) and Program Counter (PC) from stack when run.

<br>

#### Curious Interrupt Behavior
- If the instruction being executed was a taken branch with a 3-cycle execution time (i.e. no page boundary crossed), the interrupt will only trigger after one extra CPU cycle. 
- On the NMOS 6502, an NMI hardware interrupt occurring at the start of a `BRK` instruction will hijack it: the `BRK` instruction still executes as normal, but the NMI vector is used instead of the IRQ vector. 
- The 65C02 clears the decimal flag on any interrupt (including `BRK`).

<br>

#### The Break Flag and the Stack
Interrupts and stack operations involving the status register (the P register) are the only instances where the break flag appears — and even then, only on the stack. It has no representation in the CPU itself and cannot be accessed by any instruction. 

- The break flag is set to 1 whenever the transfer was caused by software (`BRK` or `PHP`). 
- The break flag is set to 0 whenever the transfer was caused by a hardware interrupt. 
- The break flag is masked and cleared (0) whenever transferred from the stack back to the status register, either by `PLP` or during a return from interrupt (`RTI`). 

This makes it somewhat difficult to inspect the break flag in order to distinguish a software interrupt (`BRK`) from a hardware interrupt (NMI or IRQ), so the mechanism is rarely used in practice. Accessing the break mark placed in the extra byte following a `BRK` instruction is even more cumbersome, and probably requires indexed zeropage operations. 

Bit 5 (unused) of the status register is set to 1 whenever the register is pushed to the stack. Bits 5 and 4 are always ignored when transferred back to the status register. 

E.g.,
```asm6502
1)
         SR: N V - B D I Z C
             0 0 - - 0 0 1 1

    PHP  ->  0 0 **1** **1** 0 0 1 1  =  $33
    PLP  <-  0 0 - - 0 0 1 1  =  $03
  but:
    PLA  <-  0 0 **1** **1** 0 0 1 1  =  $33

2)
    LDA #$32 ;00110010
    PHA  ->  0 0 **1** **1** 0 0 1 0  =  $32
    PLP  <-  0 0 - - 0 0 1 0  =  $02

3)
    LDA #$C0
    PHA  ->  1 1 0 0 0 0 0 0  =  $C0
    LDA #$08
    PHA  ->  0 0 0 0 1 0 0 0  =  $08
    LDA #$12
    PHA  ->  0 0 **0** **1** 0 0 1 0  =  $12

    RTI
         SR: 0 0 - - 0 0 1 0  =  $02
         PC: $C008
```

Note that most emulators display the status register (SR or P) as it would appear once pushed to the stack, with bits 4 and 5 turned on — adding a bias of $30 to the register value. Here, we chose to omit this virtual presence of those bits, since there isn't really a slot for them in the hardware.

<br>
<br>
<br>

# Other Instructions
***
### `NOP` - No Operation
| addressing | assembler | opc | bytes | cycles |
| ---------- | --------- | --- | ----- | ------ |
| implied    | NOP       | EA  | 1     | 2      |
- **Flags:** N Z C I D V -> `- - - - - -`
- **Example:**
    ```asm6502
    ; wastes 10 cycles
    NOP
    NOP
    NOP
    NOP
    NOP
    ```