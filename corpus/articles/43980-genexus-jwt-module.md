---
title: "GeneXus JWT Module"
source_id: 43980
source_url: https://wiki.genexus.com/commwiki/wiki?43980
genexus_version: "18"
---

# GeneXus JWT Module

GeneXus JWT Module is an independent module that implements the JSON Web Token standard defined in [RFC7519](https://tools.ietf.org/html/rfc7519)

The module is based on Microsoft's [System.IdentityModel.Tokens.Jwt](https://www.nuget.org/packages/System.IdentityModel.Tokens.Jwt/) library for .Net implementation and [Auth0](https://mvnrepository.com/artifact/com.auth0/java-jwt/3.8.1) for Java implementation.

JWT is commonly used to validate information integrity and authenticity, or as a means for authentication. In some cases, it is also used as a guarantee for data confidentiality when the information is also encrypted.

At present, this module doesn't implement data encryption. It implements a signed JWT that is not nested.

This module begins to support nested private claims since [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?45901,,).

It does not implement arrays on claims, nested signatures nor specific JSON data types yet.

## [Detail](#Detail)

The module is organized in folders using standard defined categories.

* JWT - JWT engines for signature and verification, and specific optionals.
* Utils - Specific utilities to work with the module.

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
* Microsoft.IdentityModel.JsonWebTokens
  + [Microsoft.IdentityModel.JsonWebTokens\_5.3.0](https://www.nuget.org/packages/Microsoft.IdentityModel.JsonWebTokens/)
  + [Microsoft.IdentityModel.JsonWebTokens\_6.5.1](https://www.nuget.org/packages/Microsoft.IdentityModel.JsonWebTokens/) for .Net Framework since [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?45624,,)
  + [Microsoft.IdentityModel.JsonWebTokens\_6.5.0](https://www.nuget.org/packages/Microsoft.IdentityModel.JsonWebTokens/) for .Net Core since [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?45624,,)
  + [Microsoft.IdentityModel.JsonWebTokens\_6.34.0](https://www.nuget.org/packages/Microsoft.IdentityModel.JsonWebTokens/) for .Net and .Net Framework since [GeneXus 18 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?54242)
* Microsoft.IdentityModel.Logging
  + [Microsoft.IdentityModel.Logging\_5.5.0](https://www.nuget.org/packages/Microsoft.IdentityModel.Logging/)
  + [Microsoft.IdentityModel.Logging\_6.5.1](https://www.nuget.org/packages/Microsoft.IdentityModel.Logging/) for .Net Framework since [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?45624,,)
  + [Microsoft.IdentityModel.Logging\_6.5.0](https://www.nuget.org/packages/Microsoft.IdentityModel.Logging/) for .Net Core since [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?45624,,)
* Microsoft.IdentityModel.Tokens
  + [Microsoft.IdentityModel.Tokens\_5.3.0](https://www.nuget.org/packages/Microsoft.IdentityModel.Tokens/)
  + [Microsoft.IdentityModel.Tokens\_6.5.1](https://www.nuget.org/packages/Microsoft.IdentityModel.Tokens/) for .Net Framework since [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?45624,,)
  + [Microsoft.IdentityModel.Tokens\_6.5.0](https://www.nuget.org/packages/Microsoft.IdentityModel.Tokens/) for .Net Core since [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?45624,,)
  + [Microsoft.IdentityModel.Tokens\_6.34.0](https://www.nuget.org/packages/Microsoft.IdentityModel.Tokens/) for .Net and .Net Framework since [GeneXus 18 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?54242)
* System.IdentityModels.Tokens.Jwt
  + [System.IdentityModels.Tokens.Jwt\_5.3.0](https://www.nuget.org/packages/System.IdentityModel.Tokens.Jwt/)
  + [System.IdentityModels.Tokens.Jwt\_6.5.1](https://www.nuget.org/packages/System.IdentityModel.Tokens.Jwt/) for .Net Framework since [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?45624,,)
  + [System.IdentityModels.Tokens.Jwt\_6.5.0](https://www.nuget.org/packages/System.IdentityModel.Tokens.Jwt/) for .Net Core since [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?45624,,)
  + [System.IdentityModels.Tokens.Jwt\_6.34.0](https://www.nuget.org/packages/System.IdentityModel.Tokens.Jwt/) for .Net and .Net Framework since [GeneXus 18 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?54242)

Java

* BouncyCastle
  + [bcprov-jdk15on-1.60.jar](https://mvnrepository.com/artifact/org.bouncycastle/bcprov-jdk15on/1.60) & [bcpkix-jdk15on-1.60.jar](https://mvnrepository.com/artifact/org.bouncycastle/bcpkix-jdk15on/1.60)
  + [bcprov-jdk15on-1.64.jar](https://mvnrepository.com/artifact/org.bouncycastle/bcprov-jdk15on/1.64) & [bcpkix-jdk15on-1.64.jar](https://mvnrepository.com/artifact/org.bouncycastle/bcpkix-jdk15on/1.64) since [GeneXus 16 upgrade 9](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?45275,,)
  + [bcprov-jdk15on-1.69.jar](https://mvnrepository.com/artifact/org.bouncycastle/bcprov-jdk15on/1.69) & [bcpkix-jdk15on-1.69.jar](https://mvnrepository.com/artifact/org.bouncycastle/bcpkix-jdk15on/1.69) since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?48684,,)
  + [bcprov-jdk18on-1.75.jar](https://mvnrepository.com/artifact/org.bouncycastle/bcprov-jdk18on/1.75) & [bcpkix-jdk18on-1.75.jar](https://mvnrepository.com/artifact/org.bouncycastle/bcpkix-jdk18on/1.75) since [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239)
  + [bcprov-jdk18on-1.78.1.jar](https://mvnrepository.com/artifact/org.bouncycastle/bcprov-jdk18on/1.78.1) & [bcpkix-jdk18on-1.78.1.jar](https://mvnrepository.com/artifact/org.bouncycastle/bcpkix-jdk18on/1.75) since [GeneXus 18 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?54244)
* AuthO
  + [java-jwt-3.9.0.jar](https://mvnrepository.com/artifact/com.auth0/java-jwt/3.9.0)
  + [java-jwt-3.10.3.jar](https://mvnrepository.com/artifact/com.auth0/java-jwt/3.10.3) since [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?45901,,)
  + [java-jwt-4.4.0.jar](https://mvnrepository.com/artifact/com.auth0/java-jwt/4.4.0) since [GeneXus 18 upgrade 11](https://wiki.genexus.com/commwiki/wiki?54245)
* Jackson
  + [jackson-databind-2.9.10.1.jar](https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-databind/2.9.10.1)
    - [jackson-databind-2.9.10.3.jar](https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-databind/2.9.10.3) since [GeneXus 16 Upgrade 9](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?45275,,)
    - [jackson-databind-2.9.10.4.jar](https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-databind/2.9.10.4) since [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?45624,,)
    - [jackson-databind-2.11.0.jar](https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-databind/2.11.0) since [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?45901,,)
    - [jackson-databind-2.12.2.jar](https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-databind/2.12.2) since [GeneXus 17 upgrade 7](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?49301,,)
    - [jackson-databind-2.13.2.1.jar](https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-databind/2.13.2.1) since [GeneXus 17 Upgrade 10](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?49971,,)
    - [jackson-databind-2.14.1.jar](https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-databind/2.14.1) since [GeneXus 18 Upgrade 2](https://wiki.genexus.com/commwiki/wiki?53396)
  + [jackson-core-2.9.9.jar](https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-core/2.9.9)
    - [jackson-core-2.11.0.jar](https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-core/2.11.0) since [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?45901,,)
    - [jackson-core-2.12.2.jar](https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-core/2.12.2) since [GeneXus 17 upgrade 7](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?49301,,)
    - [jackson-core-2.13.2.jar](https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-core/2.13.2) since [GeneXus 17 Upgrade 10](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?49971,,)
    - [jackson-core-2.14.1.jar](https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-core/2.14.1) since [GeneXus 18 Upgrade 2](https://wiki.genexus.com/commwiki/wiki?53396)
  + [jackson-annotations-2.9.9.jar](https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-annotations/2.9.9)
    - [jackson-annotations-2.11.0.jar](https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-annotations/2.11.0) since [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?45901,,)
    - [jackson-annotations-2.12.2.jar](https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-annotations/2.12.2) since [GeneXus 17 upgrade 7](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?49301,,)
    - [jackson-annotations-2.14.1.jar](https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-annotations/2.14.1) since [GeneXus 18 Upgrade 2](https://wiki.genexus.com/commwiki/wiki?53396)
  + Apache Commons Codec
    - [commons-codec-1.11.jar](https://mvnrepository.com/artifact/commons-codec/commons-codec/1.11)
    - [commons-codec-1.15.jar](https://mvnrepository.com/artifact/commons-codec/commons-codec/1.15) since [GeneXus 18 upgrade 11](https://wiki.genexus.com/commwiki/wiki?54245)

## [Install](#Install)

You have to install **SecurityAPICommons and GeneXusJWT modules** using the [Manage Module References](https://wiki.genexus.com/commwiki/wiki?40172) dialog from the Knowledge Manager option (located in the GeneXus IDE toolbar).

## [Availability](#Availability)

[GeneXus 16 Upgrade 8](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?44913,,)

For Net Core it's available since [GeneXus 16 Upgrade 9](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?45275,,)

## [Scope](#Scope)

Java, Net Framework and Net Core Web (server-side module)


|  |
| --- |
| **Backlinks** |
| [Table of contents:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) | [Integrated Security by Domain](https://wiki.genexus.com/commwiki/wiki?50682) | [JWT Creator](https://wiki.genexus.com/commwiki/wiki?43989) |
| [JWT Domains](https://wiki.genexus.com/commwiki/wiki?43982) | [JWT Optional Data](https://wiki.genexus.com/commwiki/wiki?43983) | [JWT Utils](https://wiki.genexus.com/commwiki/wiki?43986) |

---
