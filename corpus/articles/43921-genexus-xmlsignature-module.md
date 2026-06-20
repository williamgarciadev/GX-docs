---
title: "GeneXus XmlSignature Module"
source_id: 43921
source_url: https://wiki.genexus.com/commwiki/wiki?43921
genexus_version: "18"
---

# GeneXus XmlSignature Module

GeneXusXmlSignature Module implements XML Signature standards.

The module is based on [XML Security Library (xmlsec)](https://www.aleksey.com/xmlsec/) for Java implementation, and [System.Security.Cryptography.Xml](https://docs.microsoft.com/en-us/dotnet/api/system.security.cryptography.xml?view=netframework-4.8) for .Net implementation.

## [Details](#Details)

The module is organized in folders using standard defined categories.

* XmlDSig - This folder contains the definition of the signature engines and optional data types needed.
* JavaSpecificConfig - This folder contains an object to define configurations, and only applies to Java generation. [More information.](https://wiki.genexus.com/commwiki/wiki?43604)

## [Dependencies](#Dependencies)

GeneXus

* SecurityAPICommons Module

.Net

Requires .Net Framework 4.7 since [GeneXus 17 upgrade 1](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46852,,)

Requires dotnet SDK>=3.1 and 5.0 since [GeneXus 17 Upgrade 5](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?48247,,)

Requieres dotnet SDK>= 6.0 since [GeneXus 17 Upgrade 8](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?49616,,)

* BouncyCastle
  + [BouncyCastle\_1.8.6.1](https://www.nuget.org/packages/BouncyCastle/) since [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?45624,,)
  + Not in use since [GeneXus 17 Upgrade 9](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?49956,,)
  + [BouncyCastle.Cryptography 2.2.1](https://www.nuget.org/packages/BouncyCastle.Cryptography/2.2.1) since [GeneXus 18 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?54242)
  + [BouncyCastle.Cryptography 2.3.1](https://www.nuget.org/packages/BouncyCastle.Cryptography/2.3.1) since [GeneXus 18 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?54244)
* Portable.BouncyCastle
  + [Portable.BouncyCastle\_1.8.5](https://www.nuget.org/packages/Portable.BouncyCastle/)
  + [Portable.BouncyCastle\_1.8.6.7](https://www.nuget.org/packages/Portable.BouncyCastle/) since [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?45624,,)
  + [Portable.BouncyCastle 1.9.0](https://www.nuget.org/packages/Portable.BouncyCastle/)  since [GeneXus 17 Upgrade 9](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?49956,,)
  + Not in use since [GeneXus 18 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?54242)

Java

* BouncyCastle
  + [bcprov-jdk15on-1.60.jar](https://mvnrepository.com/artifact/org.bouncycastle/bcprov-jdk15on/1.60) & [bcpkix-jdk15on-1.60.jar](https://mvnrepository.com/artifact/org.bouncycastle/bcpkix-jdk15on/1.60)
  + [bcprov-jdk15on-1.64.jar](https://mvnrepository.com/artifact/org.bouncycastle/bcprov-jdk15on/1.64) & [bcpkix-jdk15on-1.64.jar](https://mvnrepository.com/artifact/org.bouncycastle/bcpkix-jdk15on/1.64) since [GeneXus 16 upgrade 9](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?45275,,)
  + [bcprov-jdk15on-1.69.jar](https://mvnrepository.com/artifact/org.bouncycastle/bcprov-jdk15on/1.69) & [bcpkix-jdk15on-1.69.jar](https://mvnrepository.com/artifact/org.bouncycastle/bcpkix-jdk15on/1.69) since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?48684,,)
  + [bcprov-jdk18on-1.75.jar](https://mvnrepository.com/artifact/org.bouncycastle/bcprov-jdk18on/1.75) & [bcpkix-jdk18on-1.75.jar](https://mvnrepository.com/artifact/org.bouncycastle/bcpkix-jdk18on/1.75) since [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239)
  + [bcprov-jdk18on-1.78.1.jar](https://mvnrepository.com/artifact/org.bouncycastle/bcprov-jdk18on/1.78.1) & [bcpkix-jdk18on-1.78.1.jar](https://mvnrepository.com/artifact/org.bouncycastle/bcpkix-jdk18on/1.75) since [GeneXus 18 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?54244)

* xmlsec library
  + [xml sec 2.1.4](https://mvnrepository.com/artifact/org.apache.santuario/xmlsec/2.1.4)
  + [xml sec 2.2.4](https://mvnrepository.com/artifact/org.apache.santuario/xmlsec/2.1.4) since [GeneXus 17 upgrade 7](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?49301,,)
  + [xml sec 3.0.3](https://mvnrepository.com/artifact/org.apache.santuario/xmlsec/3.0.3) since [GeneXus 18 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?54241)
* Simple log for Java
  + [slf4j-nop-1.7.7.jar](https://mvnrepository.com/artifact/org.slf4j/slf4j-nop/1.7.7)
* Woodstox
  + [woodstox-core-5.0.3.jar](https://mvnrepository.com/artifact/com.fasterxml.woodstox/woodstox-core/5.0.3)
  + [stax2-api-3.1.4.jar](https://mvnrepository.com/artifact/org.codehaus.woodstox/stax2-api/3.1.4)
* Apache Commons Codec
  + [commons-codec-1.11.jar](https://mvnrepository.com/artifact/commons-codec/commons-codec/1.11)
  + [commons-codec-1.15.jar](https://mvnrepository.com/artifact/commons-codec/commons-codec/1.15) since [GeneXus 18 upgrade 11](https://wiki.genexus.com/commwiki/wiki?54245)

## [Install](#Install)

Install **SecurityAPICommons and GeneXusXmlSignature modules** using the [Manage Module References](https://wiki.genexus.com/commwiki/wiki?40172) dialog from the Knowledge Manager option (located in the GeneXus IDE toolbar).

## [Availability](#Availability)

[GeneXus 16 Upgrade 8](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?44913,,)

For Net Core is available since [GeneXus 16 Upgrade 9](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?45275,,)

## [Scope](#Scope)

Java, .Net Framework Web and Net Core Web (server-side module)


|  |
| --- |
| **Backlinks** |
| [Table of contents:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) | [XmlDSig .Net specific information](https://wiki.genexus.com/commwiki/wiki?43603) | [XmlDSig Java specific information](https://wiki.genexus.com/commwiki/wiki?43604) |

---
