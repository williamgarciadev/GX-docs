---
title: "Symmetric Key Generation Utils"
source_id: 42683
source_url: https://wiki.genexus.com/commwiki/wiki?42683
genexus_version: "18"
---

# Symmetric Key Generation Utils

This is part of [GeneXus Cryptography Module](https://wiki.genexus.com/commwiki/wiki?43917). and allows to create differents kind of key, for symmetric Encryption.

## [SymmetricKeyType Domain](#SymmetricKeyType+Domain)

Values:

```
GENERICRANDOM
```

## [SymmetricKeyGenerator](#SymmetricKeyGenerator)

### [DoGenerateHashBasedKey](#DoGenerateHashBasedKey)

```
SymmetricKeyGenerator.DoGenerateHashBasedKey(hashAlgorithm , plainText)
```

* Input hashAlgorithm: HashAlgorithm Domain value
* Input plainText: LongVarChar(2M) plaint text
* Returns: VarChar(256) hexadecimal

Generates a fixed-length key based on the plain text digest.

It uses UTF-8 by default unless [CryptographyEncodingUtil](https://wiki.genexus.com/commwiki/wiki?43502) is used.

### [DoGenerateKey](#DoGenerateKey)

```
SymmetricKeyGenerator.DoGenerateKey(symmetricKeyType, length)
```

* Input symmetricKeyType: SymmetricKeyType Domain value
* Input length: Numeric(9.0) bits
* Returns: VarChar(256) hexadecimal

Generates a fixed-length key with the given type of generator indicated on symmetricKeyType.

### [DoGenerateIV](#DoGenerateIV)

```
SymmetricKeyGenerator.DoGenerateIV(symmetricKeyType, length)
```

* Input symmetricKeyType: SymmetricKeyType Domain value
* Input length: Numeric(9.0) bits
* Returns: VarChar(256) hexadecimal

Generates a fixed-length IV with a Secure Random Algorithm for the given length expressed in bits.

### [DoGenerateNonce](#DoGenerateNonce)

```
SymmetricKeyGenerator.DoGenerateNonce(symmetricKeyType, length)
```

* Input symmetricKeyType: SymmetricKeyType Domain value
* Input length: Numeric(9.0) bits
* Returns: VarChar(256) hexadecimal

Generates a fixed-length nonce with a Secure Random Algorithm for the given length expressed in bits.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
