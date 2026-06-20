---
title: "CryptoAsymmetricEncrypt data type"
source_id: 33462
source_url: https://wiki.genexus.com/commwiki/wiki?33462
genexus_version: "18"
---

# CryptoAsymmetricEncrypt data type

**Warning**: This data type will be discontinued in GeneXus 18 Upgrade 5. [GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) is on the way to replace this data type. It is recommended to migrate your code and use this API before GeneXus 18 Upgrade 5.

It enables us to encrypt a text using an asymmetrical algorithm.

### [CryptoAsymmetricEncrypt Methods](#CryptoAsymmetricEncrypt+Methods)

|  |  |
| --- | --- |
| **Name** | **Description** |
| **Encrypt(**text:String**)** | For a given text, it returns it encrypted using asymmetrical cryptography according to the algorithm and the public key of the certificate specified. |
| **Decrypt(**text :String**)** | Returns the given text de-encrypted according to the algorithm and the private key of the certificate specified. A requirement is that the certificate must contain the private key. |

### [Properties](#Properties)

|  |  |
| --- | --- |
| **Algorithm**:String | Enables the specification of the hash algorithms that will be used. SHA256 is used by default |
| **Certificate**:CryptoCertificate | Allows us to specify the certificate that will be used for encrypting or de-encrypting. |

### [Example](#Example)

#### [A. Encrypt a text using an asymmetrical encryption algorithm.](#A.+Encrypt+a+text+using+an+asymmetrical+encryption+algorithm.)

The example below shows the encrypting of a text using a public key certificate.

```
&ErrorCode = &cryptoCert.Load("MyPublicKey.cer")
if &ErrorCode = 0
      &CryptoEncrypt.Certificate = &cryptoCert //&CryptoEncrypt is of CryptoAsymmetricEncrypt type
      &result = &CryptoEncrypt.Encrypt(&Text)
      if &CryptoEncrypt.ErrCode <> 0
           //Process Errors
      endif
endif
```

#### [B. De-encrypting an encrypted text with an asymmetrical algorithm.](#B.+De-encrypting+an+encrypted+text+with+an+asymmetrical+algorithm.)

This example shows how to de-encrypt an encrypted text using an asymmetrical algorithm.

```
&ErrorCode = &cryptoCert.Load("MyPFX.pfx",&pwd) //&CryptoCert is of CryptoCertificate type.
 if &ErrorCode= 0
    if &cryptoCert.HasPrivateKey() 
        &CryptoEncrypt.Certificate = &cryptoCert //&CryptoEncrypt is of the CryptoAsymmetricEncrypt type
        &Text= &CryptoEncrypt.Decrypt(&EncryptedText)
    else
       //Process Errors
  endif
else
  //Process Errors
endif
```

### [Notes](#Notes)

* iOS only support*SHA256* (default) in Algorithm property. Other algorithms are ignored.
* Android uses *RSA/ECB/OAEPWithSHA-256AndMGF1Padding* in Algorithm property when the developer indicates an unsupported algorithm.

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators:** | .NET, Java, Android, Apple |

### [Availability](#Availability)

This data type is available as of [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?28265,,).  
For iOS is available as of [Genexus 15 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?38023,,).  
For Android is available as of [GeneXus 15 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?38845,,).


|  |
| --- |
| **Backlinks** |
| [Toc:Cryptography data types](https://wiki.genexus.com/commwiki/wiki?22980) |

---
