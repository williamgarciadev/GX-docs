---
title: "SecurityAPICommons Module"
source_id: 47252
source_url: https://wiki.genexus.com/commwiki/wiki?47252
genexus_version: "18"
---

# SecurityAPICommons Module

SecurityAPICommons Module is an independent module that implements Key Management and some encoding utilities to be used in conjunction with the other SecurityAPI Modules.

## [Detail](#Detail)

This module is organized in folders using categories.

* Asymmetric - Asymmetric key management
* Encoders - Encoding utils
* Symmetric - Symmetric key management
* Utils - Some useful utils like a whitelist by extensions.

## [Dependencies](#Dependencies)

.Net

Requires .Net Framework 4.7 since [GeneXus 17 upgrade 1](https://wiki.genexus.com/commwiki/wiki?46852,,)

Requires dotnet SDK>=3.1 and 5.0 since [GeneXus 17 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?48247,,)

Requieres dotnet SDK>= 6.0 since [GeneXus 17 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?49616,,)

* BouncyCastle
  + [BouncyCastle\_1.8.6.1](https://www.nuget.org/packages/BouncyCastle/) since [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/wiki?45624,,)
  + [Portable.BouncyCastle 1.9.0](https://www.nuget.org/packages/Portable.BouncyCastle/)  since [GeneXus 17 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?49956,,)
  + [BouncyCastle.Cryptography 2.2.1](https://www.nuget.org/packages/BouncyCastle.Cryptography/2.2.1) since [GeneXus 18 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?54242)
* System.Security.Cryptography.Algorithms
  + [System.Security.Cryptography.Algorithms\_4.3.0](https://www.nuget.org/packages/System.Security.Cryptography.Algorithms/4.3.0)  since [GeneXus 17 upgrade 1](https://wiki.genexus.com/commwiki/wiki?46852,,)
* System.Security.Cryptography.Cng
  + [System.Security.Cryptography.Cng\_4.7.0](https://www.nuget.org/packages/System.Security.Cryptography.Cng/4.7.0) since [GeneXus 17 upgrade 1](https://wiki.genexus.com/commwiki/wiki?46852,,)
* System.Security.Cryptography.Primitives
  + [System.Security.Cryptography.Primitives\_4.3.0](https://www.nuget.org/packages/System.Security.Cryptography.Primitives/4.3.0) since [GeneXus 17 upgrade 1](https://wiki.genexus.com/commwiki/wiki?46852,,)

Java

* BouncyCastle
  + [bcprov-jdk15on-1.60.jar](https://mvnrepository.com/artifact/org.bouncycastle/bcprov-jdk15on/1.60) & [bcpkix-jdk15on-1.60.jar](https://mvnrepository.com/artifact/org.bouncycastle/bcpkix-jdk15on/1.60)
  + [bcprov-jdk15on-1.64.jar](https://mvnrepository.com/artifact/org.bouncycastle/bcprov-jdk15on/1.64) & [bcpkix-jdk15on-1.64.jar](https://mvnrepository.com/artifact/org.bouncycastle/bcpkix-jdk15on/1.64) since [GeneXus 16 upgrade 9](https://wiki.genexus.com/commwiki/wiki?45275,,)
  + [bcprov-jdk15on-1.69.jar](https://mvnrepository.com/artifact/org.bouncycastle/bcprov-jdk15on/1.69) & [bcpkix-jdk15on-1.69.jar](https://mvnrepository.com/artifact/org.bouncycastle/bcpkix-jdk15on/1.69) since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?48684,,)
  + [bcprov-jdk18on-1.75.jar](https://mvnrepository.com/artifact/org.bouncycastle/bcprov-jdk18on/1.75) & [bcpkix-jdk18on-1.75.jar](https://mvnrepository.com/artifact/org.bouncycastle/bcpkix-jdk18on/1.75) since [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239)

## [Install](#Install)

You have to install **SecurityAPICommons module** using the [Manage Module References](https://wiki.genexus.com/commwiki/wiki?40172) dialog from the Knowledge Manager option (located in the GeneXus IDE toolbar).

## [Availability](#Availability)

[GeneXus 16 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?44913,,)

For Net Core it's available since [GeneXus 16 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?45275,,)

## [Scope](#Scope)

Java, Net Framework and Net Core Web (server-side module)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) | [Integrated Security by Domain](https://wiki.genexus.com/commwiki/wiki?50682) |

---
