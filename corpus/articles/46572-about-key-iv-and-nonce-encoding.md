---
title: "About key, IV, and nonce encoding"
source_id: 46572
source_url: https://wiki.genexus.com/commwiki/wiki?46572
genexus_version: "18"
---

# About key, IV, and nonce encoding

The GeneXusSecurityAPI's modules use different symmetric keys, IVs, and nonces.

The majority of them specify a hexadecimal string as input. It means a literal hex representation of bits that is different from a UTF (or other character encodings) representation of bits.

Verify if your key is hexa or another encoding before using it and if it is compliant with the algorithm specification. If it is not or is on a wrong encoding, the execution could fail or it could return the wrong result.

The easiest way to discover the encoding is by counting the characters to find out if it reaches the expected length for the algorithm or a given length if a specific encoding is used.

To change the encoding, you can use the [HexaEncoder](https://wiki.genexus.com/commwiki/wiki?42675) object on this module.

## [Hexadecimal representation](#Hexadecimal+representation+)

Hexadecimal representation, also known as Hex or Hexa is a base 16 numerical system made up of 16 symbols.

0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F

It does not distinguish capital letters from small letters, A is the same as a.

On computer systems, it is translated to the binary numerical system using 4 bits by symbol as shown on the following table:

| Hexa | Binary |
| --- | --- |
| 0 | 0000 |
| 1 | 0001 |
| 2 | 0010 |
| 3 | 0011 |
| 4 | 0100 |
| 5 | 0101 |
| 6 | 0110 |
| 7 | 0111 |
| 8 | 1000 |
| 9 | 1001 |
| A | 1010 |
| B | 1011 |
| C | 1100 |
| D | 1101 |
| E | 1110 |
| F | 1111 |

Then, the binary interpretation of a sample key will be as follows:

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hexa key | 1E | D1 | D4 | C8 | 70 | 7B | 53 | 99 |
| Binary key | 00011110 | 11010001 | 11010100 | 11001000 | 01110000 | 01111011 | 01010011 | 10011001 |

In conclusion, a hexadecimal key made up of 16 characters will translate to a 64-bit key.

## [UTF representation](#UTF+representation)

UTF encoding or Unicode Translation Format is a coding system for character sets.

It defines 3 types of encodings:

* **UTF-8** − It comes in 8-bit units (bytes); a character in UTF8 can have between 1 to 4 bytes, making UTF8 variable length.
* **UTF-16** − It comes in 16-bit units (shorts); it can be 1 or 2 shorts long, making UTF16 variable length.
* **UTF-32** − It comes in 32-bit units (longs). It is a fixed-width format and is always 1 "long" in length.

### [About UTF-8](#About+UTF-8)

It is the most commonly used in computer systems and allows representing common language symbols and control characters.

The most common alphabetical symbols are represented by 8 bits (1 Byte) as shown in [this table](https://www.utf8-chartable.de/unicode-utf8-table.pl?utf8=bin).

So, it is really different from the hexa representation and distinguishes capital letters from small letters: A(01000001) is not the same as a(01100001).

Translating the hexa example key from UTF-8 to binary:

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UTF-8 key | 1E | D1 | D4 | C8 | 70 | 7B | 53 | 99 |
| Hexa key | 3145 | 4431 | 4434 | 4338 | 3730 | 3742 | 3533 | 3939 |
| Binary key | 0011000101000101 | 0100010000110001 | 0100010000110100 | 0100001100111000 | 0011011100110000 | 0011011101000010 | 0011010100110011 | 0011100100111001 |

In conclusion, the same string key interpreted as UTF-8 is a 128-bit key and it will change if capital letters are replaced with small letters, as shown in the next example.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UTF-8 key | 1e | d1 | d4 | c8 | 70 | 7b | 53 | 99 |
| Hexa key | 3165 | 6431 | 6434 | 6338 | 3730 | 3762 | 3533 | 3939 |
| Binary key | 0011000101100101 | 0110010000110001 | 0110010000110100 | 0110001100111000 | 0011011100110000 | 0011011101100010 | 0011010100110011 | 0011100100111001 |

## 

## [Troubleshooting](#Troubleshooting)

Related errors classified by the module's object:

* SymmetricBlockCipher
  + Error codes between SB022 and SB030
* SymmetricStreamCipher
  + Error codes between SS007 and SS012
* CMAC
  + Error codes CM003 and CM004
* HMAC
  + Error codes HS 002 and HS003
* JWTOptions and JWTCreator
  + Error code OP001


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
