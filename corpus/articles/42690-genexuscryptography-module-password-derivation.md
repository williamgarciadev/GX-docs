---
title: "GeneXusCryptography Module Password Derivation"
source_id: 42690
source_url: https://wiki.genexus.com/commwiki/wiki?42690
genexus_version: "18"
---

# GeneXusCryptography Module Password Derivation

This is part of [GeneXus Cryptography Module](https://wiki.genexus.com/commwiki/wiki?43917)

For more information about Password derivation and storage, read the [OWASP Password Storage Cheat Sheet](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Password_Storage_Cheat_Sheet.md).

## [PasswordDerivationAlgorithm Domain](#PasswordDerivationAlgorithm+Domain)

Values:

```
SCrypt, Bcrypt, Argon2
```

## [Argon2Version Domain](#Argon2Version+Domain)

Values:

```
ARGON2_VERSION_10, ARGON2_VERSION_13
```

## [Argon2HashType Domain](#Argon2HashType+Domain)

Values:

```
ARGON2_d, ARGON2_i, ARGON2_id
```

## [PasswordDerivation](#PasswordDerivation)

Implements Password-specific hashing (derivation) functions. It uses Bouncy Castle implementation for the algorithms and therefore has the same limitations and restrictions.

### [DoGenerateSCrypt](#DoGenerateSCrypt)

Warning! The Scrypt password derivation function is safe to use for key derivation, not for hashing (storing) passwords. It is vulnerable to GPU (or ASIC) brute force attacks since it is widely used in cryptocurrencies. 

```
PasswordDerivation.DoGenerateSCrypt(password, salt, CPUCost, blockSize, parallelization, keyLenght)
```

* Input password: Character(100)
* Input salt: Character(100)
* Input CPUCost: Numeric(9.0)
* Input blockSize: Numeric(9.0)
* Input parallelization: Numeric(9.0)
* Input keyLenght: Numeric(9.0)
* Returns: VarChar(256) Base64 encoded

SCrypt parameter restrictions:

```
CPUCost (N) - CPU/Memory cost parameter. Must be larger than 1, a power of 2 and less than 2^(128 * r / 8).
blockSize (r) - the block size, must be >= 1.
parallelization (p) - Parallelization parameter. Must be a positive integer less than or equal to Integer.MAX_VALUE / (128 * r * 8).
```

Source: <https://www.bouncycastle.org/docs/docs1.5on/org/bouncycastle/crypto/generators/SCrypt.html>

```
Example:
&PasswordDerivation.DoGenerateSCrypt("password", "123456", 16384, 8, 1, 256)
```

### [DoGenerateDefaultSCrypt](#DoGenerateDefaultSCrypt)

Warning! This algorithm should not be used with fixed parameters. The adequate parameters should be calculated to fit the hardware and the system's functional requirements.

```
PasswordDerivation.DoGenerateDefaultSCrypt(password, salt)
```

* Input password: Character(100)
* Input salt: Character(100)
* Returns: VarChar(256) Base64 encoded

It calculates Scrypt algorithm with fixed arbitrary parameters.

```
CPUCost (N) - 16384
blockSize (r) - 8
parallelization (p) - 1
keyLenght - 256

​​
Example:
&PasswordDerivation.DoGenerateDefaultSCrypt("password", "123456")
```

### [DoGenerateBcrypt](#DoGenerateBcrypt)

```
PasswordDerivation.DoGenerateBcrypt(password, salt, cost)
```

* Input password: Character(100)
* Input salt: Character(100) hexadecimal
* Input cost: Numeric(9.0)
* Returns: VarChar(256) Base64 encoded

Bcrypt parameter restrictions:

```
password - the password bytes (up to 72 bytes) to use for this invocation.
salt - the 128 bit salt to use for this invocation.
cost - the bcrypt cost parameter. The cost of the bcrypt function grows as 2^cost. Legal values are 4..31 inclusive.
output - a 192 bit (24 byte) hash.
```

Source: <http://javadox.com/org.bouncycastle/bcprov-jdk15on/1.53/org/bouncycastle/crypto/generators/BCrypt.html>

```
Example:
&salt = &Hexa.fromHexa("0c6a8a8235bb90219d004aa4056ec884")
&PasswordDerivation.DoGenerateBcrypt("password", &salt , 6)
```

### [DoGenerateDefaultBcrypt](#DoGenerateDefaultBcrypt)

Warning! This algorithm should not be used with fixed parameters. The adequate parameters should be calculated to fit the hardware and the system's functional requirements.

```
PasswordDerivation.DoGenerateDefaultBcrypt(password, salt, cost)
```

* Input password: Character(100)
* Input salt: Character(100) hexadecimal
* Returns: VarChar(256) Base64 encoded

It calculates Bcrypt algorithm with fixed arbitrary parameters.

```
cost - 6
```

```
Example: 
&salt = &Hexa.fromHexa("0c6a8a8235bb90219d004aa4056ec884")
&PasswordDerivation.DoGenerateDefaultBcrypt("pasword", &salt)
```

### [DoGenerateArgon2](#DoGenerateArgon2)

(Available since [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/wiki?45624,,), just for Java)

Warning! The adequate parameters should be calculated to fit the hardware and the system's functional requirements.

```
PasswordDerivation.DoGenerateArgon2(argon2Version, argon2HashType, iterations, memory, parallelism, password, salt, hashLength)
```

* Input argon2Version: Argon2Version Domain
* Input argon2HashType: Argon2HashType Domain
* Input iterations: Numeric(9)
* Input memory: Numeric(9)
* Input parallelism: Numeric(9)
* Input password: Character(100)
* Input salt: Character(100) hexadecimal
* Input hashLength: Numeric(9) bytes

Argon2 parameter restrictions

```
parallelism - must be between 1 and 16777216
iterations - must be greater than 1
hashLength - must be greater than 4
```

```
Example:
&PasswordDerivation.DoGenerateArgon2(Argon2Version.ARGON2_VERSION_10, Argon2HashType.ARGON2_d, 1, 4, 1, "password", "14ae8da01afea8700c2358dcef7c5358d9021282bd88663a4562f59fb74d22ee", 32)
```


|  |
| --- |
| **Backlinks** |
| [GeneXus Cryptography Module](https://wiki.genexus.com/commwiki/wiki?43917) | [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
