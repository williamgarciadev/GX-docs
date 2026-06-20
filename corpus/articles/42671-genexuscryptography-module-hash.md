---
title: "GeneXusCryptography Module Hash"
source_id: 42671
source_url: https://wiki.genexus.com/commwiki/wiki?42671
genexus_version: "18"
---

# GeneXusCryptography Module Hash

**Note**: These hashing functions are part of [GeneXus Cryptography Module](https://wiki.genexus.com/commwiki/wiki?43917).

## [Hashing functions](#Hashing+functions)

NIST definition:

*"A hash function is used to produce a condensed representation of its input, taking an input* *of arbitrary length and outputting a value with a predetermined length. Hash functions are used in the generation and verification of digital signatures, for key derivation, for random number generation, in the computation of message authentication codes and for hash-only applications."* [Source](https://www.nist.gov/publications/transitioning-use-cryptographic-algorithms-and-key-lengths)

A hash function is a mathematical function. The main goal of this type of function is to be irreversible, which means that generating the input from the output is impossible. As a consequence, the attacks for this type of function involve brute-forcing, dictionary attacks, or rainbow tables; that is, generating an input somehow and comparing it to the result.

The output of these functions is called digest.

Another important property of this type of function is that they can dramatically change the output with any minor change on the input. That amplifies the unpredictability of the output.

A good hash function is expected to offer a very low probability of collisions, which is usually calculated for each algorithm. In this context, a collision means that different inputs could result in the same output.

The computation costs of hash functions are low and are widely used for integrity checking, password generation, password storage (using [salting](https://en.wikipedia.org/wiki/Salt_(cryptography)) in this case is recommended) or combined with encryption algorithms to generate signatures.

New cracking tools are frequently developed and newly developed mathematical proofs are published for hash functions, so checking the OWASP recommendations before selecting hash functions is recommended.

### [NIST Recommendations (\*)](#NIST+Recommendations+%28*%29)

| Hash Function | Use | Status |
| --- | --- | --- |
| SHA-1 | Digital signature generation | Disallowed, except where specifically allowed by NIST protocol-specific guidance. |
| Digital signature verification | Legacy use |
| Non-digital-signature applications | Acceptable (\*\*) |
| SHA - 2 famility (SHA-224, SHA-256, SHA-384, SHA-512, SHA-512/224 and SHA 512/256) | Acceptable for all hash function applications | |
| SHA-3 family (SHA3-224, SHA3-256, SHA3-384 and SHA3-512) | Acceptable for all hash function applications | |

(\*) Created: March 21, 2019. Updated: June 13, 2019. Last checked: July 14, 2025.  
(\*\*) GeneXus standard classes use SHA1 only for integrity checks tasks and not for any cryptographic purposes.

### [Useful readings](#Useful+readings)

* [Testing for weak encryption (OWASP)](https://www.owasp.org/index.php/Testing_for_Weak_Encryption_(OTG-CRYPST-004))
* [OWASP's Cryptographic Storage Cheat Sheet](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Cryptographic_Storage_Cheat_Sheet.md)
* [NIST Transitioning the Use of Cryptographic Algorithms and Key Lengths](https://www.nist.gov/publications/transitioning-use-cryptographic-algorithms-and-key-lengths)


|  |
| --- |
| **Backlinks** |
| [GeneXus Cryptography Module](https://wiki.genexus.com/commwiki/wiki?43917) | [Table of contents:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
