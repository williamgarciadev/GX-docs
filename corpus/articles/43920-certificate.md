---
title: "Certificate"
source_id: 43920
source_url: https://wiki.genexus.com/commwiki/wiki?43920
genexus_version: "18"
---

# Certificate

This is part of [GeneXus Cryptography Module](https://wiki.genexus.com/commwiki/wiki?43917). and allows to manage certificates, for asymmetric Encryption.

## [Certificate](#Certificate)

**Valid Public Key formats**

* Encoded Base64 key PKCS8 formatted (.pem extension). It can contain a public key, private key, certificate or both.
  + Encrypted .pem files are not supported
  + Files with .key extensions are supported since [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?45901,,)
* DER certificate (.crt or .cer extension). It contains only public keys.
* PKCS12 certificate or keystore (.p12 or .pfx or .jks extension). It contains only private keys or both.
  + JKS format (JavaKeyStore) is available only for Java implementation.
  + For PKCS12 certificates the file password is needed for both Java and .Net implementations.
  + .Net implementation does not use the PKCS12 alias; it takes the public key from the first certificate on the certificate chain and the first default private key listed on the file.
  + Files with .pkcs12 extensions are supported since [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?45901,,)
* Every certificate must implement the X509 standard.
* Public keys outside certificates are admitted in PKCS8 format. Supported since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238)

### [Properties](#Properties)

* String issuer
* String subject
* String serialNumber
* String thumbprint
* Date notAfter
* Date notBefore
* int version

### [Load](#Load)

```
Certificate.Load(path)
```

* Input path: VarChar(256) path to the X509 certificate
* Returns: Boolean true if it is correctly loaded

### [LoadPKCS12](#LoadPKCS12)

```
Certificate.LoadPKCS12(path, alias, password)
```

* Input path: VarChar(256) path of the X509 certificate
* Input alias: Character(100) certificate's alias
* Input password: Character(100) file password
* Returns Boolean true if it is correctly loaded

Loads a public key from a PKCS#12 formatted certificate.

### [FromBase64](#FromBase64)

```
Certificate.FromBase64(base64Data)
```

* Input base64Data: VarChar(256) base64 encoded X509 certificate
* Returns Boolean true if it is correctly loaded

Loads an X509 certificate from its base64 encoded representation.

### [ToBase64](#ToBase64)

```
Certificate.ToBase64()
```

* Returns VarChar(256) base64 encoded certificate

Retrieves the loaded certificate on base64 encoding.


|  |
| --- |
| **Backlinks** |
| [Asymmetric Key Management](https://wiki.genexus.com/commwiki/wiki?43918) | [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
