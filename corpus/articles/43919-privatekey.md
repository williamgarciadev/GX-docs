---
title: "PrivateKey"
source_id: 43919
source_url: https://wiki.genexus.com/commwiki/wiki?43919
genexus_version: "18"
---

# PrivateKey

This is part of [GeneXus Cryptography Module](https://wiki.genexus.com/commwiki/wiki?43917). and allows to manage a Privatekey, for asymmetric Encryption.

## [PrivateKey](#PrivateKey)

**Valid key formats**

* Encoded Base64 key PKCS8 formatted (.pem extension). It can contain a public key, private key, certificate or both.
  + Encrypted .pem files are not admitted.
  + Encrypted PKCS8 private keys are admitted since GeneXus 17 Upgrade 2
  + Files with .key extensions are supported since [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?45901,,)
* PKCS12 certificate or keystore (.p12 or .pfx or .jks extension). It contains only private keys or both.
  + JKS format (JavaKeyStore) is available only for Java implementation.
  + For PKCS12 certificates the file password is needed for both Java and .Net implementations.
  + .Net implementation does not use the PKCS12 alias; it takes the public key from the first certificate on the certificate chain and the first default private key listed on the file.
  + Files with .pkcs12 extensions are supported since [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?45901,,)
* Every certificate must implement the X509 standard.
* Public keys outside certificates are admitted in PKCS8 format. Supported since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238)

### [Load](#Load)

```
PrivateKey.Load(path)
```

* Input path: VarChar(256) path of the private key file
* Returns: Boolean true if it is correctly loaded

Loads a private key.

### [LoadEncrypted](#LoadEncrypted)

(This method is available since GeneXus v17 Upgrade 2)

```
PrivateKey.LoadEncrypted(path, encryptionPassword)
```

* Input path: VarChar(256) path of the private key file
* Input encryptionPassword: Character(100) PKCS8 encryption key
* Returns: Boolean true if it is correctly loaded

Loads a PKCS8 encrypted private key.

### [LoadPKCS12](#LoadPKCS12)

```
PrivateKey.LoadPKCS12(path, alias, password)
```

* Input path: VarChar(256) path of the private key file
* Input alias: Character(100) certificate alias
* Input password: Character(100) file password
* Returns: Boolean true if it is correctly loaded

Loads a private key from a PKCS#12 formatted certificate.

### [ToBase64](#ToBase64)

This method is available since [GeneXus 17](https://wiki.genexus.com/commwiki/wiki?46066,,)

```
PrivateKey.ToBase64()
```

* Returns: Varchar(256) base64 en BER/DER encoded private key

Returns the BER/DER encoded base64 preloaded private key.

### [FromBase64](#FromBase64)

This method is available since [GeneXus 17](https://wiki.genexus.com/commwiki/wiki?46066,,)

```
PrivateKey.FromBase64(base64)
```

* Input base64: VarChar(256) base64 BER/DER encoded private key
* Returns: Boolean true if it is correctly loaded

Loads a BER/DER encoded base64 private key


|  |
| --- |
| **Backlinks** |
| [Asymmetric Key Management](https://wiki.genexus.com/commwiki/wiki?43918) | [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
