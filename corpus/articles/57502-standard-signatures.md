---
title: "Standard Signatures"
source_id: 57502
source_url: https://wiki.genexus.com/commwiki/wiki?57502
genexus_version: "18"
---

# Standard Signatures

Standard signatures are digital signatures that adhere to standards designed to ensure interoperability and security in the exchange of electronic data and documents.

In this article, you can learn about their characteristics and how to implement them.

## [Domain SignatureStandard](#Domain+SignatureStandard)

They are digital signature standards that are applied in a specific field or domain.

**Values:** CMS

### [CMS value](#CMS+value)

Implements CMS (Cryptographic Message Syntax) standard described on [RFC 5652](https://datatracker.ietf.org/doc/html/rfc5652).

The CMS is derived from PKCS #7 version 1.5, documented in [RFC 2315](https://datatracker.ietf.org/doc/html/rfc2315).  PKCS #7 version 1.5 was developed outside of the IETF; it was originally published as an RSA Laboratories Technical Note in November 1993. For this reason, sometimes people refer to CMS as PKCS#7.

## [SignatureStandardOptions](#SignatureStandardOptions)

Here you can find Signature Standard options that add optional values to sign a String using a standard.

### [SetSignatureStandard](#SetSignatureStandard)

Sets the standard to use to sign a String.

**Default value:** CMS

```
SetSignatureStandard(signatureStandard)
```

* Input signatureStandard: SignatureStandard domain value
* Returns: Boolean, true if it was successfully configured

Sample

```
&iscorrect = &SignatureStandardOptions.SetSignatureStandard(SignatureStandard.CMS)
```

### [SetCertificate](#SetCertificate)

Adds an X509Certificate to be used on the signature verification. It must be preloaded using [SecurityAPI - Certificate Object](https://wiki.genexus.com/commwiki/wiki?43920).

```
SetCertificate(certificate)
```

* Input certificate: Certificate type value
* Returns: void

Sample

```
&SignatureStandardOptions.SetCertificate(&certificate)
```

### [SetEncapsulated](#SetEncapsulated)

Sets whether the text will be encapsulated on the signed output.

**Default value:** false

```
SetEncapsulated(isEncapsulated)
```

* Input isEncapsulated: Boolean true if is encapsulated.
* Returns: void

Sample

```
&SignatureStandardOptions.SetEncapsulated(true)
```

### [SetPrivateKey](#SetPrivateKey)

Adds a private key to be used to sign the text. It must be preloaded using [SecurityAPI - PublicKey Object](https://wiki.genexus.com/commwiki/wiki?54578).

```
SetPrivateKey(privateKey)
```

* Input privateKey: PrivateKey type value
* Returns: void

Sample

```
&SignatureStandardOptions.SetPrivateKey(&privateKey)
```

## [StandardSigner](#StandardSigner)

Facilitates the creation of digital signatures that comply with a particular standard.

Considerations

* The algorithm to be used is identified from the private key or certificate.
* The current implementation only accepts RSA key pairs.

**Valid Key** **formats**

* Encoded Base64 key PKCS8 formatted (.pem extension). It can contain a public key, private key, certificate, or both.
  + Encrypted .pem files are not admitted.
  + Encrypted PKCS8 private keys have been admitted since [GeneXus 17 upgrade 2](https://wiki.genexus.com/commwiki/wiki?47418,,).
  + Files with .key extensions have been supported since [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?45901,,).
* DER certificate (.crt or .cer extension). It contains only public keys.
* PKCS12 certificate or keystore (.p12 or .pfx or .jks extension). It contains only private keys or both.
  + JKS format (JavaKeyStore) is available only for Java implementation.
  + For PKCS12 certificates the file password is needed for both Java and .Net implementations.
  + .NET implementation does not use the PKCS12 alias; it takes the public key from the first certificate on the certificate chain and the first default private key listed on the file.
  + Files with .pkcs12 extensions have been supported since [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?45901,,).
* Every certificate must implement the X509 standard.
* Public keys outside certificates are not implemented since they are not defined by the CMS (current implementation) standard.

### [Sign](#Sign)

Signs a plain text using a standard defined on SignatureStandardOptions.

```
Sign(plainText, options)
```

* Input plainText: Varchar(9999) It uses UTF-8 by default unless [CryptographyEncodingUtil](https://wiki.genexus.com/commwiki/wiki?43502) is used.
* Input options: SignatureStandardOptions object
* Returns: VarChar(9999) Base64 encoded signed text

Sample

```
&privateKey.Load("C:/keys/key.pem")
&SignatureStandardOptions.SetPrivateKey(&privateKey)
&SignatureStandardOptions.SetEncapsulated(false)
&SignatureStandardOptions.SetStandard(SignatureStandard.CSM)
&result = &StandardSigner.Sign("Lorem ipsum", &SignatureStandardOptions)
```

### [Verify](#Verify)

Verifies a Base64 encoded signed text using SignatureStandardOptions configuration.

```
StandardSigner.Verify(signedData, plainText, options)
```

* Input signedData: VarChar(9999) Base64 encoded signed text to verify.
* Input plainText: VarChar(9999) It uses UTF-8 by default unless [CryptographyEncodingUtil](https://wiki.genexus.com/commwiki/wiki?43502) is used. If the text is encapsulated on the signedData (indicated as SignatureStandardOptions.SetEncaptulated(true)) this parameter can be left as an empty string (example: "")
* Input options: SignatureStandardOptions object
* Returns: Boolean true if verified, false otherwise

Sample encapsulated signature:

```
&certificate.Load("C:/keys/cert.cer")
&SignatureStandardOptions.SetCertificate(&certificate)
&SignatureStandardOptions.SetEncapsulated(true)
&SignatureStandardOptions.SetStandard(SignatureStandard.CMS)
&result = &StandardSigner.Verify(signedData, "", &SignatureStandardOptions)
```

Sample not encapsulated signature:

```
&certificate.Load("C:/keys/cert.cer")
&SignatureStandardOptions.SetCertificate(&certificate)
&SignatureStandardOptions.SetEncapsulated(false)
&SignatureStandardOptions.SetStandard(SignatureStandard.CMS)
&result = &StandardSigner.Verify(signedData, "Lorem ipsum", &SignatureStandardOptions)
```

## [Security tips](#Security+tips)

When assigning file paths, do not use user input concatenations or sanitize user entries to avoid path traversal or path manipulation vulnerability risks.

### [Availability](#Availability)

These objects have been available since [GeneXus 18 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?54243).


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
