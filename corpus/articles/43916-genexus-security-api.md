---
title: "GeneXus Security API"
source_id: 43916
source_url: https://wiki.genexus.com/commwiki/wiki?43916
genexus_version: "18"
---

# GeneXus Security API

The Security API is a collection of specific modules that implement cryptographic functions, digital signature standards, input type controls and integrity checks, and more.

## [Modules list](#Modules+list)

* SecurityAPICommons
  + Common objects and utilities
* GeneXusCryptography
  + Cryptographic functions
* GeneXusXmlSignature
  + Digital XML signature standards implementation
* GeneXusJWT
  + JSON Web Token implementation
* GeneXusSftp
  + Restricted SFTP Client implementation.
* GeneXusFtps (Available since GeneXus v16 Upgrade 9)
  + Restricted FTPS Client implementation.

## [Install](#Install)

You have to install **SecurityAPI modules** using the [Manage Module References](https://wiki.genexus.com/commwiki/wiki?40172) dialog in the Knowledge Manager option (GeneXus IDE toolbar). All modules on this API require the SecurityAPICommons module.

### [Availability](#Availability)

This property is available since [GeneXus 16 upgrade 8](https://wiki.genexus.com/commwiki/wiki?44913,,).

## [Scope](#Scope)

**Generators:**[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), .[.NET](https://wiki.genexus.com/commwiki/wiki?38604) (server-side module), [Java](https://wiki.genexus.com/commwiki/wiki?12258)


* Modules
  + [SecurityAPICommons Module](https://wiki.genexus.com/commwiki/wiki?47252)
    - [Encoders](https://wiki.genexus.com/commwiki/wiki?42668)
      * [Hexadecimal Encoder](https://wiki.genexus.com/commwiki/wiki?42675)
      * [Base64 Encoder](https://wiki.genexus.com/commwiki/wiki?42676)
      * [Base64UrlEncoder](https://wiki.genexus.com/commwiki/wiki?55420)
    - [Symmetric Key Generation Utils](https://wiki.genexus.com/commwiki/wiki?42683)
    - [Asymmetric Key Management](https://wiki.genexus.com/commwiki/wiki?43918)
      * [PrivateKey](https://wiki.genexus.com/commwiki/wiki?43919)
      * [Certificate](https://wiki.genexus.com/commwiki/wiki?43920)
      * [PublicKey](https://wiki.genexus.com/commwiki/wiki?54578)
    - [File Extensions Whitelisting](https://wiki.genexus.com/commwiki/wiki?45554)
  + [GeneXus Cryptography Module](https://wiki.genexus.com/commwiki/wiki?43917)
    - [Encoding Management](https://wiki.genexus.com/commwiki/wiki?43502)
    - [Hash](https://wiki.genexus.com/commwiki/wiki?42671)
      * [Hashing](https://wiki.genexus.com/commwiki/wiki?42719)
    - [Password Derivation Functions](https://wiki.genexus.com/commwiki/wiki?46946)
      * [Password Derivation Object](https://wiki.genexus.com/commwiki/wiki?42690)
    - [MAC calculations](https://wiki.genexus.com/commwiki/wiki?44267,,)
      * [HMAC](https://wiki.genexus.com/commwiki/wiki?44268)
      * [CMAC](https://wiki.genexus.com/commwiki/wiki?44270)
    - [Symmetric](https://wiki.genexus.com/commwiki/wiki?42673)
      * [Symmetric Block Encryption](https://wiki.genexus.com/commwiki/wiki?42681)
      * [Symmetric Stream Encryption](https://wiki.genexus.com/commwiki/wiki?42682)
    - [Asymmetric](https://wiki.genexus.com/commwiki/wiki?42685)
      * [Asymmetric Block Encryption](https://wiki.genexus.com/commwiki/wiki?42686)
      * [Asymmetric Signer](https://wiki.genexus.com/commwiki/wiki?42687)
      * [Standard Signatures](https://wiki.genexus.com/commwiki/wiki?57502)
    - [Checksum calculations](https://wiki.genexus.com/commwiki/wiki?47424)
      * [ChecksumCreator](https://wiki.genexus.com/commwiki/wiki?47425)
      * [Checksum Domains](https://wiki.genexus.com/commwiki/wiki?47428)
  + [GeneXus XmlSignature Module](https://wiki.genexus.com/commwiki/wiki?43921)
    - [Xml Digital Signature Standard (DSig)](https://wiki.genexus.com/commwiki/wiki?43564)
      * [XmlDSig Domains](https://wiki.genexus.com/commwiki/wiki?43565)
      * [Optional data](https://wiki.genexus.com/commwiki/wiki?43578)
      * [XML DSig Signer](https://wiki.genexus.com/commwiki/wiki?43579)
        + [.Net specific information](https://wiki.genexus.com/commwiki/wiki?43603)
        + [Java specific information](https://wiki.genexus.com/commwiki/wiki?43604)
      * [How to sign an XML](https://wiki.genexus.com/commwiki/wiki?45987)
  + [GeneXus JWT Module](https://wiki.genexus.com/commwiki/wiki?43980)
    - [JSON Web Token Standard (JWT)](https://wiki.genexus.com/commwiki/wiki?43981)
      * [JWT Domains](https://wiki.genexus.com/commwiki/wiki?43982)
      * [Optional Data](https://wiki.genexus.com/commwiki/wiki?43983)
      * [Utils](https://wiki.genexus.com/commwiki/wiki?43986)
      * [JWT Creator](https://wiki.genexus.com/commwiki/wiki?43989)
        + [About JWT with ECDSA](https://wiki.genexus.com/commwiki/wiki?47251,,)
      * [How to create a simple JWT](https://wiki.genexus.com/commwiki/wiki?46132)
  + [GeneXus SFTP Module](https://wiki.genexus.com/commwiki/wiki?44965)
    - [SFTP Client](https://wiki.genexus.com/commwiki/wiki?44966)
    - [Connection Options SFTP](https://wiki.genexus.com/commwiki/wiki?44967)
  + [GeneXus FTPS Module](https://wiki.genexus.com/commwiki/wiki?45274)
    - [FTPS Domains](https://wiki.genexus.com/commwiki/wiki?45276)
    - [FTPS Client](https://wiki.genexus.com/commwiki/wiki?45277)
    - [Connection Options FTPS](https://wiki.genexus.com/commwiki/wiki?45278)
* [Error Handling](https://wiki.genexus.com/commwiki/wiki?43582,,)
* [About key, IV, and nonce encoding](https://wiki.genexus.com/commwiki/wiki?46572)
* [Conversion from Cryptography Data type](https://wiki.genexus.com/commwiki/wiki?45222)

---
