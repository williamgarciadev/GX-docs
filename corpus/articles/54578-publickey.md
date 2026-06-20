---
title: "PublicKey"
source_id: 54578
source_url: https://wiki.genexus.com/commwiki/wiki?54578
genexus_version: "18"
---

# PublicKey

This is part of [GeneXus Cryptography Module](https://wiki.genexus.com/commwiki/wiki?43917). and allows to manage a PublicKey, for asymmetric Encryption.

## [PublicKey](#PublicKey)

This data type is available since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238)

**Valid key formats**

* Encoded Base64 key PKCS8 formatted (.pem extension). It can contain a public key, private key, certificate or both.
  + Encrypted .pem files are not admitted.
  + Encrypted PKCS8 private keys are admitted since GeneXus 17 Upgrade 2
  + Files with .key extensions are supported since [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?45901,,)
* PKCS12 certificate or keystore (.p12 or .pfx or .jks extension). It contains only private keys or both.
  + JKS format (JavaKeyStore) is available only for Java implementation.
  + For PKCS12 certificates the file password is needed for both Java and .Net implementations.
  + .Net implementation does not use the PKCS12 alias; it takes the public key from the first certificate on the certificate chain and the first default private key listed on the file.
  + Files with .pkcs12 extensions are supported since [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?45901,,)
* Every certificate must implement the X509 standard.
* Public keys outside certificates are admitted in PKCS8 format. Supported since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238)

### [Load](#Load)

```
PublicKey.Load(path)
```

* Input path: VarChar(9999) path of the public key file
* Returns: Boolean true if it is correctly loaded

Loads a public key.

### [ToBase64](#ToBase64)

```
PublicKey.ToBase64()
```

* Returns: Varchar(9999) base64 en BER/DER encoded public key

Returns the BER/DER encoded base64 preloaded public key.

### [FromBase64](#FromBase64)

```
PublicKey.FromBase64(base64)
```

* Input base64: VarChar(9999) base64 BER/DER encoded public key
* Returns: Boolean true if it is correctly loaded

Loads a BER/DER encoded base64 public key.

### [FromJwks](#FromJwks)

(This method is available since  [GeneXus 18 Upgrade 14](https://wiki.genexus.com/commwiki/wiki?59631) )

```
PublicKey.FromJwks(jwks,  kid)
```

* Input jwks: LongVarChar(2M) JWKS (JSON Web Key Set) string
* Input kid: VarChar(9999) key identifier (usually obtained from the JWT header)
* Returns: Boolean true if it is correctly loaded

Loads the public key identified with the kid from a JWKS JSON string.


|  |
| --- |
| **Backlinks** |
| [Asymmetric Key Management](https://wiki.genexus.com/commwiki/wiki?43918) | [GeneXus 18 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?54245) | [Table of contents:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |
| [Standard Signatures](https://wiki.genexus.com/commwiki/wiki?57502) |

---
