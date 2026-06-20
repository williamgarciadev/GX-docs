---
title: "Password Derivation"
source_id: 46946
source_url: https://wiki.genexus.com/commwiki/wiki?46946
genexus_version: "18"
---

# Password Derivation

## [**Introduction**](#Introduction)

It is important to store passwords in a way that prevents them from being obtained by an attacker, even if the application or database is compromised, and that is the mission of the password derivation algorithms.

A key derivation function is a cryptographic hash function that derives one or more secret keys from a secret value such as the main key, a password, or a passphrase using a pseudorandom function ([Source](https://en.wikipedia.org/wiki/Key_derivation_function)). So, these functions are designed to survive password guessing (brute force) attacks by using a set of customized amounts of resources and rounds to reach the result and delay the response from the system. Also, storing the keys using a one-way function (the hash) and salt avoids the retrieving of the plain text key from the stored one if the database is compromised.

## [**Password Hashing Algorithms**](#Password+Hashing+Algorithms+)

### [**Argon2**](#Argon2)

Argon2 is the winner of the 2015 [Password Hashing Competition](https://password-hashing.net/). It has better password cracking resistance (when configured correctly) than Bcrypt and Scrypt (for similar configuration parameters for CPU and RAM usage). There are three different versions of the algorithm, and the Argon2id variant should be used where available, as it provides a balanced approach to resisting both side-channel and GPU-based attacks.

Argon2 has three different parameters that can be configured, meaning that it's more complicated to correctly tune for the environment. If you're not in a position to properly tune it, then a simpler algorithm such as [Bcrypt](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Password_Storage_Cheat_Sheet.md#bcrypt) may be a better choice. For more information about Argon2, see [guidance on choosing appropriate parameters](https://password-hashing.net/argon2-specs.pdf).

### [**Bcrypt**](#Bcrypt)

Bcrypt is the most widely supported of the algorithms and should be the default choice unless there are specific requirements for PBKDF2, Scrypt, or appropriate knowledge to tune Argon2. Bcrypt is older than Scrypt and is less resistantto ASIC and GPU attacks. It provides a configurable iterations count but uses constant memory, so it is easier to build hardware-accelerated password crackers.

For more information about Bcrypt, see [A Future-Adaptable Password Scheme](https://www.openbsd.org/papers/bcrypt-paper.pdf), [Bcrypt Algorithm](https://en.wikipedia.org/wiki/Bcrypt).

### [**Scrypt**](#Scrypt)

The Scrypt function is designed to hinder such attempts by raising the resource demands of the algorithm. Specifically, the algorithm is designed to use a large amount of memory compared to other password-based KDFs, making the size and the cost of a hardware implementation much more expensive, and therefore limiting the amount of parallelism an attacker can use, for a given amount of financial resources. When configured properly, Scrypt is considered a highly secure KDF function, so you can use it as a general-purpose password to key derivation algorithm; e.g. when encrypting wallets, files, or app passwords.

Warning! The Scrypt password derivation function is safe to use for key derivation, not for hashing (storing) passwords. It is vulnerable to GPU (or ASIC) brute force attacks since it is widely used in cryptocurrencies.

For more information about Scrypt, see [RFC7914](https://tools.ietf.org/html/rfc7914).

In all cases, the use of a non-automatization method, such as Captcha, is recommended to provide more security.

### [**More info:**](#More+info%3A)

[OWASP Password Storage Cheat Sheet](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Password_Storage_Cheat_Sheet.md)

[NIST Recommendation for Password-Based Key Derivation](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-132.pdf)

[GeneXusCryptography Module Password Derivation](https://wiki.genexus.com/commwiki/wiki?42690)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
