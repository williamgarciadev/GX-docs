---
title: "GeneXusCryptography Module Symmetric"
source_id: 42673
source_url: https://wiki.genexus.com/commwiki/wiki?42673
genexus_version: "18"
---

# GeneXusCryptography Module Symmetric

**Note**: This is part of [GeneXus Cryptography Module](https://wiki.genexus.com/commwiki/wiki?43917).

## [Symmetric Cryptography](#Symmetric+Cryptography)

It is also known as Secret Key Cryptography.

The main characteristic of symmetric cryptography is that it uses the same shared key to encrypt and decrypt messages.

The key must be shared over another secure channel.

It is used for:

* Transmission of a message over an insecure channel
* Secure storage on insecure media
* Authentication
* Integrity checks.

The symmetric encryption algorithms are classified as block ciphers or stream ciphers based on its input type.

### [Block ciphers](#Block+ciphers)

*"A **block cipher** is a [deterministic algorithm](https://en.wikipedia.org/wiki/Deterministic_algorithm) operating on fixed-length groups of [bits](https://en.wikipedia.org/wiki/Bit), called a block, with an unvarying transformation that is specified by a [symmetric key](https://en.wikipedia.org/wiki/Symmetric_key). (...) are a means of effectively improving security by combining simple operations such as [substitutions](https://en.wikipedia.org/wiki/Substitution_cipher) and [permutations](https://en.wikipedia.org/wiki/Transposition_cipher). Iterated product ciphers carry out encryption in multiple rounds, each of which uses a different subkey derived from the original key."* ([Source](https://en.wikipedia.org/wiki/Block_cipher))

Block ciphers need an IV - Initialization Vector to combine and initialize the first block. It should be used combined with a secure mode of operation and padding.

The block cipher's algorithm actually describes how to process a block, and the mode of operation describes how to apply the block cipher to a sequence of blocks to encrypt an uncertain amount of input data. There are various modes of operation, each one with its own advantages and disadvantages. Some of them are no longer secure.

The padding scheme defines some data to add somewhere in the message to mask the predictability that could be contained in the original message, therefore, adding complexity to the encryption. More complex paddings are usually more secure.

### [Stream ciphers](#Stream+ciphers)

*A **stream cipher** is a [symmetric key](https://en.wikipedia.org/wiki/Symmetric_key_algorithm) [cipher](https://en.wikipedia.org/wiki/Cipher) where plaintext digits are combined with a [pseudorandom](https://en.wikipedia.org/wiki/Pseudorandom) cipher digit stream ([keystream](https://en.wikipedia.org/wiki/Keystream)). In a stream cipher, each [plaintext](https://en.wikipedia.org/wiki/Plaintext) [digit](https://en.wikipedia.org/wiki/Numerical_digit) is encrypted one at a time with the corresponding digit of the keystream, to give a digit of the ciphertext stream. Since encryption of each digit is dependent on the current state of the cipher, it is also known as **state cipher**. In practice, a digit is typically a**[bit](https://en.wikipedia.org/wiki/Bit)**and* *the combining* *operation* *an [exclusive-or](https://en.wikipedia.org/wiki/Exclusive-or) (XOR).* ([Source](https://en.wikipedia.org/wiki/Stream_cipher))

Stream ciphers are computationally cheaper and faster ciphers but are usually not as secure as block ciphers.

### [NIST Recommendations (March 21, 2019)](#NIST+Recommendations+%28March+21%2C+2019%29)

| Algorithm | Status |
| --- | --- |
| Two-key TDEA Encryption | Disallowed |
| Two-key TDEA Decryption | Legacy use |
| Three-key TDEA Encryption | Deprecated through 2023  Disallowed after 2023 |
| Three-key TDEA Decryption | Legacy use |
| SKIPJACK Encryption | Disallowed |
| SKIPJACK Decryption | Legacy use |
| AES-128 Encryption and Decryption | Acceptable |
| AES-192 Encryption and Decryption | Acceptable |
| AES-256 Encryption and Decryption | Acceptable |

#### [Definition of status approval terms](#Definition+of+status+approval+terms)

* Acceptable: is used to mean that the algorithm and key length in a FIPS or SP are safe to use; no security risk is currently known when used in accordance with any associated guidance.
* Deprecated: means that the algorithm and key length may be used, but the user must accept some security risk.
* Disallowed: means that the algorithm or key length is no longer allowed for applying cryptographic protection.

### [Useful readings](#Useful+readings)

* [Testing for weak encryption (OWASP)](https://www.owasp.org/index.php/Testing_for_Weak_Encryption_(OTG-CRYPST-004))
* [OWASP's Cryptographic Storage Cheat Sheet](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Cryptographic_Storage_Cheat_Sheet.md)
* [NIST Transitioning the Use of Cryptographic Algorithms and Key Lengths](https://www.nist.gov/publications/transitioning-use-cryptographic-algorithms-and-key-lengths)


|  |
| --- |
| **Backlinks** |
| [GeneXus Cryptography Module](https://wiki.genexus.com/commwiki/wiki?43917) | [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
