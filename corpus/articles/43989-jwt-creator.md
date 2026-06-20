---
title: "JWT Creator"
source_id: 43989
source_url: https://wiki.genexus.com/commwiki/wiki?43989
genexus_version: "18"
---

# JWT Creator

**Note**: This is part of the [GeneXus JWT Module](https://wiki.genexus.com/commwiki/wiki?43980) and provides functions to create, verify, and retrieve useful information from a token.

**Valid Key****Formats**

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

**Available signature algorithms:**

* Asymmetric
  + RSA with
    - SHA1
    - SHA256
    - SHA512
    - .Net implementation-specific: it does not support RSA key lengths shorter than 1024 bits.
  + ECDSA with
    - SHA256
    - SHA384
    - SHA512
    - ECDSA is supported since [GeneXus 17 upgrade 1](https://wiki.genexus.com/commwiki/wiki?46852,,).
* Symmetric
  + HMACWithSha256
  + HMACWithSha512

## [DoCreate](#DoCreate)

Creates JWT tokens.

* If a symmetric algorithm is provided, it will use the secret indicated in the options.
* If an asymmetric algorithm is provided, it will use the PrivateKey and Certificate preloaded in the options.
* It adds all the Registered and Public Claims declared in the options.

```
DoCreate(algorithm, privateClaims, options)
```

* Input algorithm: JWTAlgorithm domain data
* Input pivateClaims: PrivateClaims type data
* Input options: JWTOptions type data
* Returns signed JWT with the algorithm indicated using keys from the options.

Example:

```
&token=&JWT.DoCreate(JWTAlgorithm.HS256, &PrivateClaims, &JWTOptions)
```

## [DoCreateFromJSON](#DoCreateFromJSON)

This method is available since [GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066)

Creates JWT tokens using a JSON payload.

* If a symmetric algorithm is provided, it will use the secret indicated in the options.
* If an asymmetric algorithm is provided, it will use the PrivateKey and Certificate preloaded in the options.
* It adds all the Registered and Public Claims declared in the options.

```
DoCreateFromJSON(algorithm, payload, options)
```

* Input algorithm: JWTAlgorithm domain data
* Input payload: VarChar(9999) String JSON
* Input options: JWTOptions type data
* Returns signed JWT with the algorithm indicated using keys from the options.

Example:

```
&payload = '{"sub":"subject1","aud":"audience1","nbf":1594116920,"hola1":"hola1","iss":"GXSA","hola2":"hola2","exp":1909649720,"iat":1596449720,"jti":"0696bb20-6223-4a1c-9ebf-e15c74387b9c, 0696bb20-6223-4a1c-9ebf-e15c74387b9c"}'
&secret = &keyGen.DoGenerateKey(SymmetricKeyType.GENERICRANDOM, 256)
&JWTOptions.SetSecret(&secret)

&token=&JWT.DoCreateFromJSON(JWTAlgorithm.HS256, &payload, &JWTOptions)
```

## [DoVerify](#DoVerify)

Verifies JWT tokens.

* Automatically verifies the revocation list if it exists in the options.
* If a symmetric algorithm is provided, it will use the secret indicated in the options.
* If an asymmetric algorithm is provided, it will use the Certificate preloaded in the options.
* It validates all the Registered and Public Claims declared in the options.
* It validates the header parameters since [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?45901,,)

```
DoVerify(token, algorithm, privateClaims, options)
```

* Input token: VarChar(256)
* Input algorithm: JWTAlgorithm domain data (mandatory parameter auditioned since [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/wiki?45624,,) as security measure)
* Input pivateClaims: PrivateClaims type data. If the object is empty, it will not try to validate them and will return true if the other token information is valid.
* Input options: JWTOptions type data
* Returns: Boolean true if the token verifies the signature and other parameters indicated in the options.

Example:

```
&verifies=&JWT.DoVerify(&token, JWTAlgorithm.RS256, &PrivateClaims, &JWTOptions)
```

## [DoVerifySignature](#DoVerifySignature)

This method is available since [GeneXus 17](https://wiki.genexus.com/commwiki/wiki?46066,,)

Verifies JWT tokens.

* Automatically verifies the revocation list if it exists in the options.
* If a symmetric algorithm is provided, it will use the secret indicated in the options.
* If an asymmetric algorithm is provided, it will use the Certificate preloaded in the options.
* It does not verify Private claims or header parameters. It is up to you which ones to verify using your own verification method.
* It does verify the token´s Registered Claims against the configured on the given JWTOptions.

```
DoVerifySignature (token, algorithm, options)
```

* Input token: VarChar(256)
* Input algorithm: JWTAlgorithm domain data as a security measure.
* Input options: JWTOptions type data
* Returns: Boolean true if the token verifies the signature and Registered claims indicated in the options.

Example:

```
&verifies=&JWT.DoVerifySignature(&token, JWTAlgorithm.RS256, &JWTOptions)
```

## [DoVerifyJustSignature](#DoVerifyJustSignature)

This method is available since [GeneXus 17](https://wiki.genexus.com/commwiki/wiki?46066,,)

Verifies JWT tokens.

* Automatically verifies the revocation list if it exists in the options.
* If a symmetric algorithm is provided, it will use the secret indicated in the options.
* If an asymmetric algorithm is provided, it will use the Certificate preloaded in the options.
* It does not verify any claims or header parameters. It is up to you which ones to verify using your own verification method.
* As for Java implementation, the library forces the time validating claims against the machine´s current time. On .Net and Net Core implementation, none of the claims are validated.

```
DoVerifyJustSignature (token, algorithm, options)
```

* Input token: VarChar(256)
* Input algorithm: JWTAlgorithm domain data as a security measure.
* Input options: JWTOptions type data
* Returns: Boolean true if the token verifies the signature.

Example:

```
&verifies=&JWT.DoVerifyJustSignature(&token, JWTAlgorithm.RS256, &JWTOptions)
```

## [GetPayload](#GetPayload)

Returns the payload content in a JSON formatted string.

```
GetPayload(token)
```

* Input token: VarChar(256)
* Returns VarChar(256) string JSON

Example:

```
&payload=&JWT.GetPayload(&token)
```

## [GetHeader](#GetHeader)

Returns the header content in a JSON formatted string.

```
GetHeader(token)
```

* Input token: VarChar(256)
* Returns VarChar(256) string JSON

Example:

```
&header=&JWT.GetHeader(&token)
```

## [GetTokenID](#GetTokenID)

Returns the GUID alphanumeric token identification from the jti registered claim.

```
GetTokenID(token)
```

* Input token: Character(100)
* Returns VarChar(256) alphanumeric GUID

Example:

```
&id=&JET.GetTokenID(&token)
```

## [Security tips](#Security+tips)

* When assigning file paths, do not use user input concatenations or sanitize user entries to avoid path traversal or path manipulation vulnerability risks.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
