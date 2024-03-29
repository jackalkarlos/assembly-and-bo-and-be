# Burda anlatım olmayacak, sadece notlar.. OnlyNotes gibi düşünebilirsiniz..

## Base 10:


Biz ölümlü insanlar olarak Base10 sistemini kullanıyoruz. Aşağıda 243 sayısının base10'a dönüştürme işlemi bulunmakta.

```
Base 10 şu sayıları içerir -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.
243 sayısının Base10'a dönüştürülme işlemi:
243 = (102 * 2) + (101 * 4) + (100 * 3) = 200 + 40 + 3.
```

Eğer ondalık ifade belirtiliyorsa genellikle "d" eki ile gösterilir, örneğin 12d.

## Base 7:

Bu base dönüştürme sapıklığını herhangi bir sayıya uygulayabiliriz. Aşağıda base 7 işlemi bulunuyor.
```
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

Ondalık sayılar "d" ekiyle veya eki olmadan temsil edilir. Örnekler: 12d veya 12.

Hexadecimal is represented with the prefix "0x" or suffix "h". Examples: 0x12 or 12h. 

Another way hexadecimal is represented is with the prefix of "\x". However, this is typically used per byte. Two hexadecimal digits make one byte. Examples: \x12 or \x12\x45\x21. 

If bits and bytes seem a little weird we'll get into them soon so don't worry.

Binary is represented with a suffix "b" or with padding of zeros at the start. Examples: 100101b or 00100101. The padding at the start is often used because a decimal number can't start with a zero.


# Data Type And Size
## Bits and Bytes

"Data type sizes vary based on architecture. These are the most common sizes and are what you will come across when working with desktop Windows and Linux."

`Bit is one binary digit. Can be 0 or 1.`

`Nibble is 4 bits.`

`Byte is 8 bits.`

`Word is 2 bytes.`

`Double Word (DWORD) is 4 bytes. Twice the size of a word.`

`Quad Word (QWORD) is 8 bytes. Four times the size of a word.`


Before we get into other data types, let's talk about signed vs unsigned. Signed numbers can be POSITIVE OR NEGATIVE. Unsigned numbers CAN ONLY BE POSITIVE. The names come from how they work. Signed numbers need a sign bit to distinguish whether or not they're negative, similar to how we use the + and - signs.

## Data Type Sizes
`Char - 1 byte (8 bits).`

`Int - There are 16-bit, 32-bit, and 64-bit integers. When talking about integers, it's usually 32-bit. For signed integers, one bit is used to specify whether the integer is positive or negative.`

Signed Int

`16 bit is -32,768 to 32,767.`

`32 bit is -2,147,483,648 to 2,147,483,647.`

`64-bit is -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807.`


Unsigned Int - 

Minimum is zero, maximum is twice that of a signed int (of the same size). For example: unsigned 32-bit int goes from 0 to 4,294,967,295. That is twice the signed int maximum of 2,147,483,647, however, its minimum value is 0. This is due to signed integers using the sign bit, making it unavailable to represent a value.

Bool - 1 byte. 

Interestingly, a bool only needs 1 bit because it's either 1 or 0 but it still takes up a full byte. This is because computers don't tend to work with individual bits due to alignment (talked about later). So instead, they work in chunks such as 1 byte, 2 bytes, 4 bytes, 8 bytes, and so on.
For more data types go here: https://www.tutorialspoint.com/cprogramming/c_data_types.htm

Offsets
Data positions are referenced by how far away they are from the address of the first byte of data, known as the base address (or just the address), of the variable. The distance a piece of data is from its base address is considered the offset. For example, let's say we have some data, 12345678. Just to push the point, let's also say each number is 2 bytes. With this information, 1 is at offset 0x0, 2 is at offset 0x2, 3 is at offset 0x4, 4 is at offset 0x6, and so on. You could reference these values with the format BaseAddress+0x##. BaseAddress+0x0 or just BaseAddress would contain the 1, BaseAddress+0x2 would be the 2, and so on.


# Binary Operations

NOT (Shown as "!")
The NOT operation will simply flip the bit.

```
NOT 1 = 0
NOT 0 = 1
```

![image](https://github.com/jackalkarlos/assembly-and-bo-and-be/assets/88983987/817817fd-0e60-49b9-b732-14385e90075c)

AND (Shown as "&")

AND will check if both bits are 1 and if they are the result will be 1, otherwise, the result is 0.

```
1 AND 1 = 1
1 AND 0 = 0
0 AND 0 = 0
```

![image](https://github.com/jackalkarlos/assembly-and-bo-and-be/assets/88983987/a87dc529-557c-438a-94ed-0a481616bb34)

OR (Shown as "|")

OR will check if one of the bits is one and if so, then the result is 1, otherwise, the result is 0.

```
1 OR 1 = 1
1 OR 0 = 1
0 OR 0 = 0
```

![image](https://github.com/jackalkarlos/assembly-and-bo-and-be/assets/88983987/75e55ca6-c6d3-4c9b-baff-1099bb804295)

XOR (Shown as "^")

The result is 1 if either of the bits is one, but not both, otherwise, the result is 0. Another way to think of XOR is it's checking if the bits are different.

```
1 XOR 1 = 0
1 XOR 0 = 1
0 XOR 0 = 0
```

![image](https://github.com/jackalkarlos/assembly-and-bo-and-be/assets/88983987/d9f1fe63-0763-4843-a3c2-ce08fece1392)


# Same code in C and ASM

![image](https://github.com/jackalkarlos/assembly-and-bo-and-be/assets/88983987/04e9909e-6ef2-4820-a66e-b2c0e5e855d6)

How it works in C:

`if x equal 4 call func1, else return nothing`

How it works in ASM:
```
1. Move x to rax (accumulator register)
2. Compare to rax with 4
3. If not equal jump to line 5
4. call func1
5. finish
```

# 64 Bit Registers

RAX - Mantık biriminin (ALU) sonuçlarını tutar. Aritmetik ve mantıksal olarak hesaplanması gereken işlemler hesaplandıktan sonra bu değişkene kaydedilir. Karşılaştırma, çıkarma, toplama gibi işlemler için kullanılabilir. Bir fonksiyonun dönüş değerini belirlemek için de kullanılabilir. Dönüş değerleri RAX içinde tutulabilir.

RBX - RBX kaydedici, bellek adreslerini tutmak için kullanılan bir kaydedicidir. Ancak RBX, tüm bellek adreslerini tutmaz, yalnızca pointerların (işaretçilerin) bellek adreslerini tutar. Base Pointer ile karıştırılmamalıdır. Ancak bazı zamanlar Base Pointer olarak kullanılabilir.

RDX - Genelde veri işleme operasyonlarında kullanılan basit bir data registeridir.

RCX - Sayaç görevi yapar. Döngü sayacı olarak kullanılır.

RSI - String manipülasyonu işlemlerinde stringin hafıza adresinin başlangıç değerini tutar.

RDI - String manipülasyonu işlemlerinde stringin hafıza adresinin bitiş değerini tutar.

RSP - Yığın işaretçisidir. Bir yığının en üstündeki adresi tutar.

RBP - Yığın işaretçisidir. Bir yığının en altındaki adresi tutar.

RIP - Bir sonraki çalıştırılacak fonksiyonun ya da instruction'un adresini tutar. En çok manipüleye açık değişkenlerden biridir.

![image](https://github.com/jackalkarlos/assembly-and-bo-and-be/assets/88983987/681af818-2503-4f6a-8899-23635b6f9f43)

If `0x0123456789ABCDEF` was loaded into a 64-bit register such as RAX, then RAX refers to `0x0123456789ABCDEF`, EAX refers to `0x89ABCDEF`, AX refers to `0xCDEF`, AH refers to `0xCD`, AL refers to `0xEF`.

What is the difference between the "E" and "R" (like EIP for 32 bit and RIP for 64 bit) prefixes? Besides one being a 64-bit register and the other 32 bits, the "E" stands for extended. The "R" stands for register. The "R" registers were newly introduced in x64, and no, you won't see them on 32-bit systems.

To see how all registers are broken apart go here:
https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/x64-architecture


# Different Data Types

### Floating Point Values - Floats and Doubles.

### Integer Values - Integers, Booleans, Chars, Pointers, etc.
Different data types can't be put in just any register. Floating-point values are represented differently than integers. Because of this, floating-point values have special registers. These registers include YMM0 to YMM15 (64-bit) and XMM0 to XMM15 (32-bit). The XMM registers are the lower half of the YMM registers, similar to how EAX is the lower 32 bits of RAX. Something unique about these registers is that they can be treated as arrays. In other words, they can hold multiple values. For example, YMM# registers are 256-bit wide each and can hold 4 64-bit values or 8 32-bit values. Similarly, the XMM# registers are 128-bits wide and can hold 2 64-bit values or 4 32-bit values. Special instructions are needed to utilize these registers as vectors.

A nice table of these registers, and more information about them, can be found here: https://en.wikipedia.org/wiki/Advanced_Vector_Extensions

### Extra Registers
There are additional registers that should be mentioned. These registers don't have any special uses. There are registers r8 to r15 which are designed to be used by integer type values (not floats or doubles). The lower 4 bytes (32 bits), 2 bytes (16 bits), and 8 bits (1 byte) can all be accessed. These can be accessed by appending the letter "d", "w", or "b".
Examples:

R8 - Full 64-bit (8 bytes) register.

R8D - Lower double word (4 bytes).

R8W - Lower word (2 bytes)

R8B - Lower byte.
