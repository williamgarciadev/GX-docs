---
title: "GeneXus Cryptography Module"
source_id: 43917
source_url: https://wiki.genexus.com/commwiki/wiki?43917
genexus_version: "18"
---

# GeneXus Cryptography Module

GeneXusCryptography Module is an independent module that implements diverse cryptographic functions.

The module is based on  [Bouncy Castle](https://www.bouncycastle.org/) on both implementations; Java and .Net (C# & NetCore).

## [Detail](#Detail)

The module is organized in folders using cryptography categories.

* [Hash](https://wiki.genexus.com/commwiki/wiki?42671): Contains Hashing class with hash algorithm implementations.
* [PasswordDerivation](https://wiki.genexus.com/commwiki/wiki?42690): Contains algorithm implementations for Scrypt and Bcrypt password derivation/verification/storage algorithms.
* [Symmetric](https://wiki.genexus.com/commwiki/wiki?42673): Contains SymmetricBlockCipher and SymmetricStreamCipher classes, each one implementing block/stream encryption and decryption algorithms.
* [Asymmetric](https://wiki.genexus.com/commwiki/wiki?42685): Contains AsymmetricBlockCipher and AsymmetricSigner classes. They implement block encryption and decryption methods for RSA, and digital signature and verification for RSA and ECDSA key types, respectively.
* [Encoders](https://wiki.genexus.com/commwiki/wiki?42668): Contains Hexa and Base64 encoding classes to encode and decode text.

## [Dependencies](#Dependencies)

GeneXus

* SecurityAPICommons Module

.Net

Requires .Net Framework 4.7 since [GeneXus 17 upgrade 1](https://wiki.genexus.com/commwiki/wiki?46852,,)

Requires dotnet SDK>=3.1 and 5.0 since [GeneXus 17 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?48247,,)

Requieres dotnet SDK>= 6.0 since [GeneXus 17 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?49616,,)

* BouncyCastle
  + [BouncyCastle\_1.8.6.1](https://www.nuget.org/packages/BouncyCastle/) since [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/wiki?45624,,)
  + Not in use since [GeneXus 17 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?49956,,)
  + [BouncyCastle.Cryptography 2.2.1](https://www.nuget.org/packages/BouncyCastle.Cryptography/2.2.1) since [GeneXus 18 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?54242)
* Portable.BouncyCastle
  + [Portable.BouncyCastle\_1.8.5](https://www.nuget.org/packages/Portable.BouncyCastle/)
  + [Portable.BouncyCastle\_1.8.6.7](https://www.nuget.org/packages/Portable.BouncyCastle/) since [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/wiki?45624,,)
  + [Portable.BouncyCastle 1.9.0](https://www.nuget.org/packages/Portable.BouncyCastle/)  since [GeneXus 17 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?49956,,)
  + Not in use since [GeneXus 18 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?54242)

Java

* BouncyCastle
  + [bcprov-jdk15on-1.60.jar](https://mvnrepository.com/artifact/org.bouncycastle/bcprov-jdk15on/1.60) & [bcpkix-jdk15on-1.60.jar](https://mvnrepository.com/artifact/org.bouncycastle/bcpkix-jdk15on/1.60)
  + [bcprov-jdk15on-1.64.jar](https://mvnrepository.com/artifact/org.bouncycastle/bcprov-jdk15on/1.64) & [bcpkix-jdk15on-1.64.jar](https://mvnrepository.com/artifact/org.bouncycastle/bcpkix-jdk15on/1.64) since [GeneXus 16 upgrade 9](https://wiki.genexus.com/commwiki/wiki?45275,,)
  + [bcprov-jdk15on-1.69.jar](https://mvnrepository.com/artifact/org.bouncycastle/bcprov-jdk15on/1.69) & [bcpkix-jdk15on-1.69.jar](https://mvnrepository.com/artifact/org.bouncycastle/bcpkix-jdk15on/1.69) since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?48684,,)
  + [bcprov-jdk18on-1.75.jar](https://mvnrepository.com/artifact/org.bouncycastle/bcprov-jdk18on/1.75) & [bcpkix-jdk18on-1.75.jar](https://mvnrepository.com/artifact/org.bouncycastle/bcpkix-jdk18on/1.75) since [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239)

## [Install](#Install)

You have to install **SecurityAPICommons and GeneXusCryptography modules** from the [Manage Module References](https://wiki.genexus.com/commwiki/wiki?40172) dialog in the Knowledge Manager option (located in the GeneXus IDE toolbar).

## [Availability](#Availability)

[GeneXus 16 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?44913,,)

For Net Core is available since [GeneXus 16 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?45275,,)

## [Scope](#Scope)

Java, Net Framework and Net Core Web (server-side module)

## [Cryptography](#Cryptography)

### [What is it?](#What+is+it%3F)

*"In computer science, cryptography refers to secure information and communication techniques derived from mathematical concepts and a set of rule-based calculations called algorithms to transform messages in ways that are hard to decipher. These deterministic algorithms are used for cryptographic key generation and digital signing and verification to protect data privacy, web browsing on the internet and confidential communications such as credit card transactions and email."* [Source](https://searchsecurity.techtarget.com/definition/cryptography)

The main goals of cryptography are known as **CIA**:

* **C**onfidentiality
* **I**ntegrity
* **A**uthenticity

In this context, non-repudiation is another aspect of security.

There are 3 types of cryptographic functions:

* Hash. It does not use keys.
* Secret Key cryptography. It uses one type of key.
* Public Key cryptography. It uses a pair of mathematically bound keys.

The 3 types are usually used for different purposes.

Once an algorithm is established as a standard, the race begins to break it by finding its vulnerabilities.

```
Cryptography vs Cryptoanalysis
Cryptographers create encryption codes.
Cryptoanalysts try to break them.
```

There aren't any unbreakable algorithms, as every one of them is going to be broken eventually. So, the goal is to replace an algorithm for a better one before it is fully broken. That is why the standards change over time.

### [Why do cryptographic algorithms have to be public?](#Why+do+cryptographic+algorithms+have+to+be+public%3F)

Because an attacker has infinite time and resources to reverse engineering any algorithm and it needs to be distributed to be used. Keeping a cryptographic algorithm secret is virtually impossible or useless except for those used in military environments only.

Publishing the algorithm also makes it possible for cryptoanalysts to analyze it and find vulnerabilities before some black-hat hacker does.

Conclusion:

**Always use public, standardized and up-to-date cryptographic algorithms.**

### [Useful readings](#Useful+readings)

* [Testing for weak encryption (OWASP)](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/09-Testing_for_Weak_Cryptography/04-Testing_for_Weak_Encryption)
* [OWASP's Cryptographic Storage Cheat Sheet](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Cryptographic_Storage_Cheat_Sheet.md)
* [OWASP Guide to Cryptography](https://wiki.owasp.org/index.php/Guide_to_Cryptography)
* [NIST - Transitioning the Use of Cryptographic Algorithms and Key Lengths](https://www.nist.gov/publications/transitioning-use-cryptographic-algorithms-and-key-lengths)


|  |
| --- |
| **Backlinks** |
| [Asymmetric Encryption Block Cipher](https://wiki.genexus.com/commwiki/wiki?42686) | [Asymmetric Signing](https://wiki.genexus.com/commwiki/wiki?42687) | [Certificate](https://wiki.genexus.com/commwiki/wiki?43920) |
| [CMAC](https://wiki.genexus.com/commwiki/wiki?44270) | [Encoding Management](https://wiki.genexus.com/commwiki/wiki?43502) | [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) | [GeneXusCryptography Module Asymmetric](https://wiki.genexus.com/commwiki/wiki?42685) |
| [GeneXusCryptography Module Hash](https://wiki.genexus.com/commwiki/wiki?42671) | [GeneXusCryptography Module Symmetric](https://wiki.genexus.com/commwiki/wiki?42673) | [HMAC](https://wiki.genexus.com/commwiki/wiki?44268) | [Integrated Security by Domain](https://wiki.genexus.com/commwiki/wiki?50682) |
| [Optional data](https://wiki.genexus.com/commwiki/wiki?43578) | [PrivateKey](https://wiki.genexus.com/commwiki/wiki?43919) | [PublicKey](https://wiki.genexus.com/commwiki/wiki?54578) | [Symmetric Block Encryption](https://wiki.genexus.com/commwiki/wiki?42681) |
| [Symmetric Key Generation Utils](https://wiki.genexus.com/commwiki/wiki?42683) | [Symmetric Stream Encryption](https://wiki.genexus.com/commwiki/wiki?42682) | [XML DSig Signer](https://wiki.genexus.com/commwiki/wiki?43579) | [XmlDSig Domains](https://wiki.genexus.com/commwiki/wiki?43565) |

---
