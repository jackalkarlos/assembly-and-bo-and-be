# Burda anlatım olmayacak, sadece notlar.. OnlyNotes gibi düşünebilirsiniz..

## Base 10:

```We mortal humans use the decimal (base 10) system.
Base 10 includes 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.
Here is 243 in base 10:
243 = (102 * 2) + (101 * 4) + (100 * 3) = 200 + 40 + 3.
```

If decimal is denoted, it will usually be with the suffix of "d" such as 12d.

## Base 7:
```We can apply this to any base. For example, 243 in base 7:
243(in base 7) = (72 * 2) + (71 * 4) + (70 * 3) = 98 + 28 + 3 = 129(in decimal).

Base 7 includes 0, 1, 2, 3, 4, 5, 6.
9 isn't in base 7, so how do we represent it in base 7?
9(in decimal) = (71 * 1) + (70 * 2) = 7 + 2. Our answer is going to be 12(base7) = 9(base10).
```

## Base 2:
```
What about base 2? Base 2 includes 0 and 1. It works the same as the others. Here are some good values to know:
210 = 1024, 29 = 512, 28 = 256, 27 = 128, etc.
```
![image](https://github.com/jackalkarlos/assembly-and-bo-and-be/assets/88983987/ed0e28f7-cc15-4187-b2d7-ef2e2a241b54)

## Hexadecimal:
```
Hexa = 6, Dec = 10. Hexadecimal is base 16. Hexadecimal is very similar but can be a little confusing for some people. You see, we only have ten different individual numbers (0, 1, 2, 3, 4, 5, 6, 7, 8, 9). Hexadecimal needs 16 different numbers. You could use 0, 1... 11, 12, 13... but that would be extremely confusing. For example, what is 1432? Is that 1,4,3,2 or 14,3,2? When we need to represent anything above 9 we can instead use letters such as A, B, C, D, E, and F in the case of hexadecimal.

A = 10, B = 11, ..., F = 15

Hexadecimal numbers are usually given a "0x" prefix or the suffix "h" such as 0xFF or FFh.

0x4A = (161 * 4d) + (160 * 10d) = 64d + 10d = 74d.
```
Learn more hexadecimal here:

https://www.khanacademy.org/math/algebra-home/alg-intro-to-algebra/algebra-alternate-number-bases/v/hexadecimal-number-system

Prefixes and Suffixes:
To distinguish between different number systems, we use prefixes or suffixes. There are many things used to distinguish between the number systems, I will only show the most common.

Decimal is represented with the suffix "d" or with nothing. Examples: 12d or 12.
Hexadecimal is represented with the prefix "0x" or suffix "h". Examples: 0x12 or 12h. Another way hexadecimal is represented is with the prefix of "\x". However, this is typically used per byte. Two hexadecimal digits make one byte. Examples: \x12 or \x12\x45\x21. If bits and bytes seem a little weird we'll get into them soon so don't worry.
Binary is represented with a suffix "b" or with padding of zeros at the start. Examples: 100101b or 00100101. The padding at the start is often used because a decimal number can't start with a zero.



# Data Type And Size

Bits and Bytes
Data type sizes vary based on architecture. These are the most common sizes and are what you will come across when working with desktop Windows and Linux.

Bit is one binary digit. Can be 0 or 1.
Nibble is 4 bits.
Byte is 8 bits.
Word is 2 bytes.
Double Word (DWORD) is 4 bytes. Twice the size of a word.
Quad Word (QWORD) is 8 bytes. Four times the size of a word.
Before we get into other data types, let's talk about signed vs unsigned. Signed numbers can be positive or negative. Unsigned numbers can only be positive. The names come from how they work. Signed numbers need a sign bit to distinguish whether or not they're negative, similar to how we use the + and - signs.

Data Type Sizes
Char - 1 byte (8 bits).
Int - There are 16-bit, 32-bit, and 64-bit integers. When talking about integers, it's usually 32-bit. For signed integers, one bit is used to specify whether the integer is positive or negative.
Signed Int
16 bit is -32,768 to 32,767.
32 bit is -2,147,483,648 to 2,147,483,647.
64-bit is -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807.
Unsigned Int - Minimum is zero, maximum is twice that of a signed int (of the same size). For example: unsigned 32-bit int goes from 0 to 4,294,967,295. That is twice the signed int maximum of 2,147,483,647, however, its minimum value is 0. This is due to signed integers using the sign bit, making it unavailable to represent a value.
Bool - 1 byte. Interestingly, a bool only needs 1 bit because it's either 1 or 0 but it still takes up a full byte. This is because computers don't tend to work with individual bits due to alignment (talked about later). So instead, they work in chunks such as 1 byte, 2 bytes, 4 bytes, 8 bytes, and so on.
For more data types go here: https://www.tutorialspoint.com/cprogramming/c_data_types.htm

Offsets
Data positions are referenced by how far away they are from the address of the first byte of data, known as the base address (or just the address), of the variable. The distance a piece of data is from its base address is considered the offset. For example, let's say we have some data, 12345678. Just to push the point, let's also say each number is 2 bytes. With this information, 1 is at offset 0x0, 2 is at offset 0x2, 3 is at offset 0x4, 4 is at offset 0x6, and so on. You could reference these values with the format BaseAddress+0x##. BaseAddress+0x0 or just BaseAddress would contain the 1, BaseAddress+0x2 would be the 2, and so on.



