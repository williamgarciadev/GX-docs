---
title: "Hashing"
source_id: 42719
source_url: https://wiki.genexus.com/commwiki/wiki?42719
genexus_version: "18"
---

# Hashing

Warning! Not all available hash algorithms are safe. Most of them are included for legacy integration compatibility. If you are planning to select an algorithm for a brand new application, choose wisely. Read the OWASP or NIST bibliography and recommendations if you are not certain about what to choose for your application.

## [HashAlgorithm Domain](#HashAlgorithm+Domain)

Values:

```
MD5, SHA1, SHA224, SHA256, SHA384, SHA512, BLAKE2B_224, BLAKE2B_256, BLAKE2B_384, BLAKE2B_512, BLAKE2S_128, BLAKE2S_160, BLAKE2S_224, BLAKE2S_256, GOST3411_2012_256, GOST3411_2012_512, GOST3411, KECCAK_224, KECCAK_256, KECCAK_288, KECCAK_384, KECCAK_512, MD2, MD4, RIPEMD128, RIPEMD160, RIPEMD256, RIPEMD320, SHA3_224, SHA3_256, SHA3_384, SHA3_512, SHAKE_128, SHAKE_256, SM3, TIGER, WHIRLPOOL
```

## [Hashing](#Hashing)

Implements hashing functions using Bouncy Castle implementation.

```
Hashing.DoHash(hashAlgorithm, txtToHash)
```

* Input hashAlgorithm: HashAlgorithm Domain Value
* Input txtToHash: VarChar(1M) UTF-8 encoded
* Returns: VarChar(256) hexadecimal

Calculates the hash digest with the given algorithm.

```
Example1:  &digest = &Hashing.DoHash(HashAlgorithm.MD5, "plain text UTF-8")
Example2:: &digest = &Hashing.DoHash(HashAlgorithm.SHA1, "plain text UTF-8")
Example3:: &digest = &Hashing.DoHash(HashAlgorithm.SHA256, "plain text UTF-8")
```


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
