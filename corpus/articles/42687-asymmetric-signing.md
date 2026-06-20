---
title: "Asymmetric Signing"
source_id: 42687
source_url: https://wiki.genexus.com/commwiki/wiki?42687
genexus_version: "18"
---

# Asymmetric Signing

**Note**: This is part of [GeneXus Cryptography Module](https://wiki.genexus.com/commwiki/wiki?43917).

Implements PKCS#1 signatures.

## [AsymmetricSigningAlgorithm Domain](#AsymmetricSigningAlgorithm+Domain)

Values:

```
RSA, ECDSA
```

## [AsymmetricSigner](#AsymmetricSigner)

Signs a text with a private key and verifies the signature with a public key.

As for paddings, it follows [RFC-4051](https://www.ietf.org/rfc/rfc4051.txt).

Considerations

* The hashing algorithm is identified from the certificate in public-key cases.
* HashAlgorithm NONE value is not a valid value for the signing algorithms.
* When using ECDSA key type, the default HashAlgorithm value used is SHA1.

**Valid Key** **formats**

* Encoded Base64 key PKCS8 formatted (.pem extension). It can contain a public key, private key, certificate or both.
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

### [DoSign](#DoSign)

```
AsymmetricSigner.DoSign(privateKey, hashAlgorithm, plainText)
```

* Input privateKey: PrivateKey type, preloaded private key
* Input hashAlgorithm: HashAlgorithm Domain value
* Input plainText: Varchar(9999) It uses UTF-8 by default unless [CryptographyEncodingUtil](https://wiki.genexus.com/commwiki/wiki?43502) is used.
* Returns: Varchar(9999) Base64 encoded

Signs a text with the specified certificate key and the given hash algorithm.

```
Example:

&key.Load("C:\\certificates\\key.pem")
&hash = HashAlgorithm.SHA256
&plainText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In aliquet ultrices dolor a consectetur."

&signature = &AsymmetricSigner.DoSign(&key, &hash, &plainText)
```

### [DoVerify](#DoVerify)

```
AsymmetricSigner.DoVerify(certificate, plainText, signature)
```

* Input certificate: Certificate type, preloaded certificate
* Input plainText: Varchar(9999) It uses UTF-8 by default unless [CryptographyEncodingUtil](https://wiki.genexus.com/commwiki/wiki?43502) is used.
* Input signature: Varchar(9999) Base64 encoded
* Returns: Boolean, true if the signature is valid for the plainText with the certificate data.

```
Example:

&certificate.Load("C:\\certificates\\certificate.cer")
&plainText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In aliquet ultrices dolor a consectetur."
&signature = "Il3rfo20i3kqdTcrg/O0nhYAtb6y+l7fKKEzP1gvKNhnCNKwZajCEiBarg21E7nVXjvXeB4E7QSXCLD8kEUNlsfkuAkvnbf52+zcRb5HxaN+jWargDlVw2v1zzxYxQ8VdjVNdBioI6oHWzurcfRfn9D8Kfuy9mUWwGlZkHgpAj6RGdr95B67Fn5XnAjN1iEW9LPuRHi4rN2VqJ8GQT3mQ9y76kuv4mKfabzq/8ar+zxqXKa2B+0znVjTK7gbWtUZCL6hRnXfttdVYhnblvGKIix2WsfZEDXtjVcyOc5MCe83cGLEVFgd4R0vZEqq7E4M4jgZyTaQlqBXCgscxUGwVQ=="

&verify = &AsymmetricSigner.DoVerify(&certificate, &plainText, &signature)
```

### [DoVerifyWithPublicKey](#DoVerifyWithPublicKey)

This method is available since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238)

```
AsymmetricSigner.DoVerifyWithPublicKey(publicKey, plainText, signature, hashAlgorithm)
```

* Input publicKey: PublicKeytype, preloaded public key
* Input plainText: Varchar(9999) It uses UTF-8 by default unless [CryptographyEncodingUtil](https://wiki.genexus.com/commwiki/wiki?43502) is used.
* Input signature: Varchar(9999) Base64 encoded
* HashAlgoritm: HashAlgorithm domain value
* Returns: Boolean, true if the signature is valid for the plainText with the public key data and hash algorithm.

```
Example:

&publicKey.Load("C:\\certificates\\pubkey.pem")
&plainText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In aliquet ultrices dolor a consectetur."
&hash = HashAlgorithm.SHA256
&signature = "Il3rfo20i3kqdTcrg/O0nhYAtb6y+l7fKKEzP1gvKNhnCNKwZajCEiBarg21E7nVXjvXeB4E7QSXCLD8kEUNlsfkuAkvnbf52+zcRb5HxaN+jWargDlVw2v1zzxYxQ8VdjVNdBioI6oHWzurcfRfn9D8Kfuy9mUWwGlZkHgpAj6RGdr95B67Fn5XnAjN1iEW9LPuRHi4rN2VqJ8GQT3mQ9y76kuv4mKfabzq/8ar+zxqXKa2B+0znVjTK7gbWtUZCL6hRnXfttdVYhnblvGKIix2WsfZEDXtjVcyOc5MCe83cGLEVFgd4R0vZEqq7E4M4jgZyTaQlqBXCgscxUGwVQ=="

&verify = &AsymmetricSigner.DoVerifyWithPublicKey(&publicKey, &plainText, &signature, &hash)
```

### [DoSignFile](#DoSignFile)

This method is available since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?48684,,)

AsymmetricSigner.DoSignFile(privateKey, hashAlgorithm, path)

* Input privateKey: PrivateKey type, preloaded private key
* Input hashAlgorithm: HashAlgorithm Domain value
* Input path: Varchar(9999) File's path to sign
* Returns: Varchar(9999) Base64 encoded

Signs a file with the specified certificate key and the given hash algorithm.

```
Example:
&key.Load("C:\\certificates\\key.pem")
&hash = HashAlgorithm.SHA256
&path= "C:\\Temp\\file.txt"
&signature = &AsymmetricSigner.DoSign(&key, &hash, &path)
```

### [DoVerifyFile](#DoVerifyFile)

This method is available since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?48684,,)

```
AsymmetricSigner.DoVerifyFile(certificate, path, signature)
```

* Input certificate: Certificate type, preloaded public key
* Input path: Varchar(9999) File's path to be verified
* Input signature: Varchar(9999) Base64 encoded
* Returns: Boolean, true if the signature is valid for the file with the certificate data.

```
Example:

&certificate.Load("C:\\certificates\\certificate.cer")
&path= "C:\\Temp\\file.txt"
&signature = "Il3rfo20i3kqdTcrg/O0nhYAtb6y+l7fKKEzP1gvKNhnCNKwZajCEiBarg21E7nVXjvXeB4E7QSXCLD8kEUNlsfkuAkvnbf52+zcRb5HxaN+jWargDlVw2v1zzxYxQ8VdjVNdBioI6oHWzurcfRfn9D8Kfuy9mUWwGlZkHgpAj6RGdr95B67Fn5XnAjN1iEW9LPuRHi4rN2VqJ8GQT3mQ9y76kuv4mKfabzq/8ar+zxqXKa2B+0znVjTK7gbWtUZCL6hRnXfttdVYhnblvGKIix2WsfZEDXtjVcyOc5MCe83cGLEVFgd4R0vZEqq7E4M4jgZyTaQlqBXCgscxUGwVQ=="

&verify = &AsymmetricSigner.DoVerifyFile(&certificate, &path, &signature)
```

### [DoVerifyFileWithPublicKey](#DoVerifyFileWithPublicKey)

This method is available since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238)

```
AsymmetricSigner.DoVerifyFileWithPublicKey(publicKey, path, signature, hashAlgorithm)
```

* Input certificate: Certificate type, preloaded public key
* Input path: Varchar(9999) File's path to be verified
* Input signature: Varchar(9999) Base64 encoded
* HashAlgorithm: HashAlgorithm domain value
* Returns: Boolean, true if the signature is valid for the file with the public key data and hash algorithm.

```
Example:

&publicKey.Load("C:\\certificates\\pubkey.pem")
&path= "C:\\Temp\\file.txt"
&hash = HashAlgorithm.SHA256
&signature = "Il3rfo20i3kqdTcrg/O0nhYAtb6y+l7fKKEzP1gvKNhnCNKwZajCEiBarg21E7nVXjvXeB4E7QSXCLD8kEUNlsfkuAkvnbf52+zcRb5HxaN+jWargDlVw2v1zzxYxQ8VdjVNdBioI6oHWzurcfRfn9D8Kfuy9mUWwGlZkHgpAj6RGdr95B67Fn5XnAjN1iEW9LPuRHi4rN2VqJ8GQT3mQ9y76kuv4mKfabzq/8ar+zxqXKa2B+0znVjTK7gbWtUZCL6hRnXfttdVYhnblvGKIix2WsfZEDXtjVcyOc5MCe83cGLEVFgd4R0vZEqq7E4M4jgZyTaQlqBXCgscxUGwVQ=="

&verify = &AsymmetricSigner.DoVerifyFileWithPublicKey(&publicKey, &path, &signature, &hash)
```

## [Security tips](#Security+tips)

When assigning file paths, do not use user input concatenations or sanitize user entries to avoid path traversal or path manipulation vulnerability risks.


|  |
| --- |
| **Backlinks** |
| [.NET Platform restrictions](https://wiki.genexus.com/commwiki/wiki?39853) | [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
