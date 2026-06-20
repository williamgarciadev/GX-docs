---
title: "CryptoSign data type"
source_id: 33458
source_url: https://wiki.genexus.com/commwiki/wiki?33458
genexus_version: "18"
---

# CryptoSign data type

**Warning**: This data type will be discontinued in GeneXus 18 Upgrade 5. [GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) is on the way to replace this data type. It is recommended to migrate your code and use this API before GeneXus 18 Upgrade 5.

CryptoSign belongs to the [Cryptography data types](https://wiki.genexus.com/commwiki/wiki?22980).

It enables us to handle digital signatures with a public key-private key, as per standard  [PKCS#7/CMS](http://es.wikipedia.org/wiki/PKCS) or PKCS1, using X509 certificates.

### [CryptoSign Methods](#CryptoSign+Methods)

|  |  |
| --- | --- |
| **Name** | **Description** |
| **Sign(**text:String[,detached:Boolean]**)**:String | Returns the text that results from applying the signature algorithm, using the certificate specified by the text entered. The detached parameter indicates if only the signature is returned or if the signature is returned together with the content. The detached parameter is valid only when the PKCS7 format is used. |
| **Verify(**signature:String,text:String[,detached:Boolean]**)**:Boolean | With a given text and a signature, verifies if the signature corresponds to the text using the information of the configured certificate. The detached parameter is valid only when the PKCS7 format is used |

### [Properties](#Properties)

|  |  |
| --- | --- |
| **Certificate**:CryptoCertificate | Allows us to specify the certificate that will be used in signing the text. |
| **Algorithm**:CryptoAlgorithmSign | Allows us to specify the signature algorithm. SHA1withRSA is the default signature algorithm. |
| **ValidateCertificate**:Boolean | Specifies whether the fact that the certificate is valid or not must be validated in the Verify method. |
| **Standard**:{PKCS7,PKCS1} | Allows us to specify the standard that will be used. The default value is PKCS1. The detached parameter is valid only when the PKCS7 format is used, in which case the standard must be specified as PKCS7. |

### [Example](#Example)

#### [A. How to sign a text](#A.+How+to+sign+a+text)

In the example below, upon a given certificate in .pfx format, a text is signed using the Hash SignSHA1withRSA algorithm.  
The first thing is to load the disk certificate. If the loading is error-free, we must request the private key to sign the text. If a key exists, a Hash algorithm is selected for the signature, and the Sign method is used to sign the text.

```
&errorCode = &CryptoCert.Load("my_keystore.pfx", &pwd) //&CryptoCert is of CryptoCertificate type.
if &errorCode = 0
    if (&CryptoCert.HasPrivateKey())
     &CryptoSign.Algorithm = CryptoSignAlgorithm.SHA1withRSA //&CryptoSign is of CryptoSign type. 
     //CryptoSignAlgorithm is an enumerated domain containing the signature algorithms supported. 
     &CryptoSign.Certificate = &CryptoCert
     &signedText = &CryptoSign.Sign(&textToSign, false)
     if &CryptoSign.ErrCode <> 0
       //Process Errors
     endif
   else
     //Process Errors
  endif
else
  //Process Errors
endif
```

#### [B. How to validate a text’s signature](#B.+How+to+validate+a+text%E2%80%99s+signature)

In the case of a certificate with a public key, the text signature is verified as shown in the following example:

```
&errorCode = &CryptoCert.Load("MyPublicKey.cer")
if &errorCode = 0
    &CryptoSign.Certificate = &CryptoCert //&CryptoSign is of CryptoSign type.
    &CryptoSign.ValidateCertificate = True //True means that the certificate is validated in the signature validation process.
    &CryptoSign.Algorithm = CryptoSignAlgorithm.SHA1withRSA
    &isOK = &CryptoSign.Verify(&SignedText,&TextToSign,false)
    if not &isOK
       //Process Errors
    else
      //OK
    endif
else
 //Process Errors
endif
```

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators:** | .NET, Java |

### [Note](#Note)

The SHA256withRSA is used by default since GeneXus Evolution v15 U10. The previous versions use SHA1withRSA.


|  |
| --- |
| **Backlinks** |
| [.NET Platform restrictions](https://wiki.genexus.com/commwiki/wiki?39853) | [Toc:Cryptography data types](https://wiki.genexus.com/commwiki/wiki?22980) |

---
