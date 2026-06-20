---
title: "Asymmetric Encryption Block Cipher"
source_id: 42686
source_url: https://wiki.genexus.com/commwiki/wiki?42686
genexus_version: "18"
---

# Asymmetric Encryption Block Cipher

**Note**: This is part of [GeneXus Cryptography Module](https://wiki.genexus.com/commwiki/wiki?43917).

## [AsymmetricEncryptionAlgorithm Domain](#AsymmetricEncryptionAlgorithm+Domain)

Values:

```
RSA
```

* RSA is only able to encrypt data to a maximum of your key size (2048 bits = 256 bytes) minus padding.
* If the input text is too long, it will throw a runtime exception type DataLengthException: attempt to process message too long for the cipher
* If you want to encrypt more data, you can use something like the following:

```
Generate a 256-bit random keystring K
Encrypt your data with AES-CBC with K
Encrypt K with RSA
Send both to the other side
```

[Source](https://tls.mbed.org/kb/cryptography/rsa-encryption-maximum-data-size)

## [AsymmetricEncryptionPadding Domain](#AsymmetricEncryptionPadding+Domain)

Values:

```
NOPADDING, OAEPPADDING, PCKS1PADDING, ISO97961PADDING
```

## [AsymmetricCipher](#AsymmetricCipher)

Encrypts and decrypts texts using an asymmetric block algorithm.

It may be used in both ways, with private key encryption and public key decryption, or public key encryption and private key decryption.

**Valid Key** **formats**

* Encoded Base64 key PKCS8 formatted (.pem extension). It can contain a public key, private key, certificate or both.
  + Encrypted .pem files are not admitted.
  + Encrypted PKCS8 private keys are admitted since GeneXus 17 Upgrade 2
  + Files with .key extensions are supported since [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?45901,,)
* DER certificate (.crt or .cer extension). It contains only public keys.
* PKCS12 certificate or keystore (.p12 or .pfx or .jks extension). It contains only private keys or both.
  + JKS format (JavaKeyStore) is available only for Java implementation.
  + For PKCS12 certificates the file password is needed for both Java and .Net implementations.
  + .Net implementation does not use the PKCS12 alias; it takes the public key from the first certificate on the certificate chain and the first default private key listed on the file.
  + Files with .pkcs12 extensions are supported since [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?45901,,)
* Every certificate must implement the X509 standard.
* Public keys outside certificates are admitted in PKCS8 format. Supported since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238)

### [DoEncrypt\_WithPrivateKey](#DoEncrypt_WithPrivateKey)

```
AsymmetricCipher.DoEncrypt_WithPrivateKey(hashAlgorithm, asymmetricEncryptionPadding, key, plainText)
```

* Input hashAlgorithm: HashAlgorithm Domain value
* Input asymmetricEncryptionPadding: AsymmetricEncryptionPadding Domain value
* Input privateKey: PrivateKey type, preloaded private key
* Input plainText: VarChar(9999) It uses UTF-8 by default unless [CryptographyEncodingUtil](https://wiki.genexus.com/commwiki/wiki?43502) is used.
* Return: VarChar(9999) Base64 encoded

Encrypts the plain text with the given parameters.

```
Example:

&key.Load("C:\\certificates\\key.pem")
&hash = HashAlgorithm.SHA256
&padding = AsymmetricEncryptionPadding.PCKS1PADDING
&plainText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In aliquet ultrices dolor a consectetur."

&encrypted = &AsymmetricCipher.DoEncrypt_WithPrivateKey(&hash, &padding, &key, &plainText)
```

### [DoEncrypt\_WithCertificate](#DoEncrypt_WithCertificate)

This method is available since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238)

```
AsymmetricCipher.DoEncrypt_WithPublicKey(hashAlgorithm, asymmetricEncryptionPadding, certificate, plainText)
```

* Input hashAlgorithm: HashAlgorithm Domain value
* Input asymmetricEncryptionPadding: AsymmetricEncryptionPadding Domain value
* Input certificate: Certificate type, preloaded public key
* Input plainText: VarChar(9999) It uses UTF-8 by default unless [CryptographyEncodingUtil](https://wiki.genexus.com/commwiki/wiki?43502) is used.
* Return: VarChar(9999) Base64 encoded

Encrypts the plain text with the given parameters.

```
Example:

&certificate.Load("C:\\certificates\\certificate.pem")
&hash = HashAlgorithm.SHA256
&padding = AsymmetricEncryptionPadding.PCKS1PADDING
&plainText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In aliquet ultrices dolor a consectetur."

&encrypted = &AsymmetricCipher.DoEncrypt_WithPublicKey(&hash, &padding, &certificate, &plainText)
```

### [DoEncrypt\_WithPublicKey](#DoEncrypt_WithPublicKey)

```
AsymmetricCipher.DoEncrypt_WithPublicKey(hashAlgorithm, asymmetricEncryptionPadding, publicKey, plainText)
```

* Input hashAlgorithm: HashAlgorithm Domain value
* Input asymmetricEncryptionPadding: AsymmetricEncryptionPadding Domain value
* Input publicKey: PublicKey type, preloaded public key
* Input plainText: VarChar(9999) It uses UTF-8 by default unless [CryptographyEncodingUtil](https://wiki.genexus.com/commwiki/wiki?43502) is used.
* Return: VarChar(9999) Base64 encoded

Encrypts the plain text with the given parameters.

```
Example:

&publicKey.Load("C:\\certificates\\pubkey.pem")
&hash = HashAlgorithm.SHA256
&padding = AsymmetricEncryptionPadding.PCKS1PADDING
&plainText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In aliquet ultrices dolor a consectetur."

&encrypted = &AsymmetricCipher.DoEncrypt_WithPublicKey(&hash, &padding, &publicKey, &plainText)
```

**Breaking change**. This method used to receive a certificate instead of a public key.  This change is made since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238)

### [DoDecrypt\_WithPrivateKey](#DoDecrypt_WithPrivateKey)

```
AsymmetricCipher.DoDecrypt_WithPrivateKey(hashAlgorithm, asymmetricEncryptionPadding, privateKey, encryptedInput)
```

* Input hashAlgorithm: HashAlgorithm Domain value
* Input asymmetricEncryptionPadding: AsymmetricEncryptionPadding Domain value
* Input privateKey: PrivateKey type, preloaded private key
* Input encryptedInput: VarChar(9999) Base64 encoded
* Returns: VarChar(9999) It uses UTF-8 by default unless [CryptographyEncodingUtil](https://wiki.genexus.com/commwiki/wiki?43502) is used.

Decrypts the encrypted input with the given parameters.

```
Example:

&key.Load("C:\\certificates\\key.pem")
&hash = HashAlgorithm.SHA256 
&padding = AsymmetricEncryptionPadding.PCKS1PADDING
&encrypted = "fu+S9ztam76KfzYMlZBEv6ABZp46bLtl05DwRQxL0FF2fXKs0uoclJqOdzqOWwRB5oKkSRJmAAjSOhqWA1k5Yp6dg+8gNLKPCRdQ1/xraNvUt82fnBlKJ37D+R20QxgkCVwKZ0I0ZkK5sb/T7rTJieVBHt3ncf3JpAGukginDwMJ0yti6Y9kpXwXZHsTVs5MDRD+lgtuWZhT+zXN3Ep5b1prV3LDM7PsenSxQorGzUQR3ccu+YJch+Kcp1va/RqeUAzaRufC66deu6EEBtJ7MrbOliVHZgQGwuwlP74G0LjwWQlh2LHyRkpjjWi4uv9rJ2Z8ClpNCsqVQyI3rvZB3g=="

&decrypted = &AsymmetricCipher.DoDecrypt_WithPrivateKey(&hash, &padding, &key, &encrypted)
```

### [DoDecrypt\_WithPublicKey](#DoDecrypt_WithPublicKey)

```
AsymmetricCipher.DoDecrypt_WithPrivateKey(hashAlgorithm, asymmetricEncryptionPadding, publicKey, encryptedInput)
```

* Input hashAlgorithm: HashAlgorithm Domain value
* Input asymmetricEncryptionPadding: AsymmetricEncryptionPadding Domain value
* Input publicKey: PublicKey type, preloaded public key
* Input encryptedInput: VarChar(9999) Base64 encoded
* Returns: VarChar(9999) It uses UTF-8 by default unless [CryptographyEncodingUtil](https://wiki.genexus.com/commwiki/wiki?43502) is used.

Decrypts the encrypted input with the given parameters.

```
Example:

&publicKey.Load("C:\\certificates\\pubkey.pem")
&hash = HashAlgorithm.SHA256 
&padding = AsymmetricEncryptionPadding.PCKS1PADDING
&encrypted = "fu+S9ztam76KfzYMlZBEv6ABZp46bLtl05DwRQxL0FF2fXKs0uoclJqOdzqOWwRB5oKkSRJmAAjSOhqWA1k5Yp6dg+8gNLKPCRdQ1/xraNvUt82fnBlKJ37D+R20QxgkCVwKZ0I0ZkK5sb/T7rTJieVBHt3ncf3JpAGukginDwMJ0yti6Y9kpXwXZHsTVs5MDRD+lgtuWZhT+zXN3Ep5b1prV3LDM7PsenSxQorGzUQR3ccu+YJch+Kcp1va/RqeUAzaRufC66deu6EEBtJ7MrbOliVHZgQGwuwlP74G0LjwWQlh2LHyRkpjjWi4uv9rJ2Z8ClpNCsqVQyI3rvZB3g=="

&decrypted = &AsymmetricCipher.DoDecrypt_WithPublicKey(&hash, &padding, &publicKey, &encrypted)
```

**Breaking change**. This method used to receive a certificate instead of a public key.  This change is made since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238)

### [DoDecrypt\_WithCertificate](#DoDecrypt_WithCertificate)

This method is available since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238)  
  
AsymmetricCipher.DoDecrypt\_WithPrivateKey(hashAlgorithm, asymmetricEncryptionPadding, certificate, encryptedInput)

* Input hashAlgorithm: HashAlgorithm Domain value
* Input asymmetricEncryptionPadding: AsymmetricEncryptionPadding Domain value
* Input certificate: Certificate type, preloaded public key
* Input encryptedInput: VarChar(9999) Base64 encoded
* Returns: VarChar(9999) It uses UTF-8 by default unless [CryptographyEncodingUtil](https://wiki.genexus.com/commwiki/wiki?43502) is used.

Decrypts the encrypted input with the given parameters.

```
Example:

&certificate.Load("C:\\certificates\\certificate.pem")
&hash = HashAlgorithm.SHA256 
&padding = AsymmetricEncryptionPadding.PCKS1PADDING
&encrypted = "fu+S9ztam76KfzYMlZBEv6ABZp46bLtl05DwRQxL0FF2fXKs0uoclJqOdzqOWwRB5oKkSRJmAAjSOhqWA1k5Yp6dg+8gNLKPCRdQ1/xraNvUt82fnBlKJ37D+R20QxgkCVwKZ0I0ZkK5sb/T7rTJieVBHt3ncf3JpAGukginDwMJ0yti6Y9kpXwXZHsTVs5MDRD+lgtuWZhT+zXN3Ep5b1prV3LDM7PsenSxQorGzUQR3ccu+YJch+Kcp1va/RqeUAzaRufC66deu6EEBtJ7MrbOliVHZgQGwuwlP74G0LjwWQlh2LHyRkpjjWi4uv9rJ2Z8ClpNCsqVQyI3rvZB3g=="

&decrypted = &AsymmetricCipher.DoDecrypt_WithPublicKey(&hash, &padding, &certificate, &encrypted)
```

## [Security tips](#Security+tips)

When assigning file paths, do not use user input concatenations or sanitize user entries to avoid path traversal or path manipulation vulnerability risks.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
