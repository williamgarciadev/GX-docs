---
title: "Asymmetric Key Management"
source_id: 43918
source_url: https://wiki.genexus.com/commwiki/wiki?43918
genexus_version: "18"
---

# Asymmetric Key Management

To manage asymmetric keys the module provides 3 data types:

* [PrivateKey](https://wiki.genexus.com/commwiki/wiki?43919)
* [Certificate](https://wiki.genexus.com/commwiki/wiki?43920)
* [PublicKey](https://wiki.genexus.com/commwiki/wiki?54578) Available since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238)

**Valid Key** **formats**

* Encoded Base64 key PKCS8 formatted (.pem extension). It can contain a public key, private key, certificate or both.
  + Encrypted .pem files or encrypted PKCS8 private keys are not admitted.
  + Files with .key extensions are not supported.
* DER certificate (.crt or .cer extension). It contains only public keys.
* PKCS12 certificate or keystore (.p12 or .pfx or .jks extension). It contains only private keys or both.
  + JKS format (JavaKeyStore) is available only for Java implementation.
  + For PKCS12 certificates the file password is needed for both Java and .Net implementations.
  + .Net implementation does not use the PKCS12 alias; it takes the public key from the first certificate on the certificate chain and the first default private key listed on the file.
  + Files with .pkcs12 extensions are not supported.
* Every certificate must implement the X509 standard.
* Public keys outside certificates are admitted in PKCS8 format. Supported since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238)

### [Key pair generation](#Key+pair+generation)

The key pair can be generated locally with some tools, the most popular of which is [OpenSSL](https://www.openssl.org/).

Anyone can create, sign and distribute a certificate but most people will not trust it and, by default, software will not trust it either. This type of certificate is known as self-signed and is commonly used for testing.

When the key pair is generated, the encryption and signing algorithms are established along with the hash algorithm that will be used to generate and verify signatures. The signature will always be verified using the algorithms preestablished on the certificate.

For more information, read the article [Cryptography Asymmetric information](https://wiki.genexus.com/commwiki/wiki?42685)

### [Useful tools:](#Useful+tools%3A)

* [OpenSSL](https://www.openssl.org/)
* [CertUtil](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/certutil)
* [KeyStore Explorer](https://keystore-explorer.org/)
* [Java KeyTool](https://docs.oracle.com/javase/8/docs/technotes/tools/unix/keytool.html)


|  |
| --- |
| **Backlinks** |
| [Connection Options FTPS](https://wiki.genexus.com/commwiki/wiki?45278) | [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
