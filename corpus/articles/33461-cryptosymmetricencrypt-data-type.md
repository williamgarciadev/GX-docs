---
title: "CryptoSymmetricEncrypt data type"
source_id: 33461
source_url: https://wiki.genexus.com/commwiki/wiki?33461
genexus_version: "18"
---

# CryptoSymmetricEncrypt data type

**Warning**: This data type will be discontinued in GeneXus 18 Upgrade 5. [GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) is on the way to replace this data type. It is recommended to migrate your code and use this API before GeneXus 18 Upgrade 5.

Enables the encryption and decryption of text using a symmetrical algorithm (DES, Rijndael, TripleDES), using CBC mode (Cipher Block Chaining).

The Create method allows us to specify the algorithm used in encrypting the text. This allows us to choose the encryption algorithm without the need to add a new data type.

### [CryptoSymmetricEncrypt Methods](#CryptoSymmetricEncrypt+Methods)

|  |  |
| --- | --- |
| **Name** | **Description** |
| **Encrypt(**text:String**)** | Encrypts the given text using symmetric cryptography according to the chosen algorithm, the key and the initialization vector (IV). |
| **Decrypt(**text:String**)** | Decrypts the given encrypted string using the specified algorithm, the key and the initialization vector (IV). |

### [Properties](#Properties)

|  |  |
| --- | --- |
| **Algorithm:**CryptoAlgorithmEncrypt | Specifies the encryption algorithm to be used. |
| **Key**:String | Encryption key must be base-64 encoded. If no key is provided, it is generated automatically upon creating the instance (required when decrypting). |
| **IV**:String | Encryption initialization vector must be base-64 encoded. If no initialization vector is provided, it is generated automatically upon creating the instance (required when decrypting). |
| **KeySize**:Numeric |  |
| **BlockSize**:Numeric |  |

**Note**: The *Key* and *IV* (Initialization Vector) properties must be encoded using the Base64 format.  
The reason for this requirement is that, internally, the encryption algorithm uses an array of bytes, which cannot always be represented as a String (it can have non-printable characters)..

### [Example](#Example+)

#### [A. How to encrypt a text using a symmetrical algorithm.](#A.+How+to+encrypt+a+text+using+a+symmetrical+algorithm.)

In the example below, the text contained in variable &text is encrypted using the TripleDES algorithm.

```
// Make sure to use a String coded as Base64
&CryptoEncrypt.Key ="alNZVUNUc2hxeDBrT3VEczU4TnNoYjFPa1pqN21oMVM=" //CryptoEncrypt is of CryptoSymmetricEncrypt type
&CryptoEncrypt.Algorithm = CryptoEncryptAlgorithm.TripleDES
&result = &CryptoEncrypt.Encrypt(&Text) //The text is encrypted and the result obtained.
```

#### [B. How to de-encrypt an encrypted text with a symmetrical algorithm.](#B.+How+to+de-encrypt+an+encrypted+text+with+a+symmetrical+algorithm.)

```
&Text = &CryptoEncrypt.Decrypt(&EncryptedText) //CryptoEncrypt is of CryptoSymmetricEncrypt type
//Process Errors
msg(format("Error %1 %2", &Cryptoencrypt.ErrCode.ToString(), &Cryptoencrypt.ErrDescription))
```

#### [C. How to encrypt a text using a symmetrical algorithm without specifying a KEY and IV.](#C.+How+to+encrypt+a+text+using+a+symmetrical+algorithm+without+specifying+a+KEY+and+IV.)

In the example below, the text contained in variable &text is encrypted using the Rijndael algorithm.

```
&CryptoEncrypt= New()
&CryptoEncrypt.BlockSize = 128
&CryptoEncrypt.KeySize = 256
&CryptoEncrypt.Algorithm = CryptoEncryptAlgorithm.Rijndael
&D_text2 = &CryptoEncrypt.Encrypt(&text)
&D_Key = &CryptoEncrypt.Key.ToString()
&IV = &CryptoEncrypt.IV.ToString()
```

It is important to notice that after the Encrypt method, you must save the values of the automatically generated Key and IV to be able to decrypt the text in the future.

### [Notes](#Notes)

* Native Mobile supported algorithms:  
  - AES/CBC/NoPadding (128)  
  - AES/CBC/PKCS5Padding (128)  
  - AES/ECB/NoPadding (128)  
  - AES/ECB/PKCS5Padding (128)  
  - DES/CBC/NoPadding (56)  
  - DES/CBC/PKCS5Padding (56)  
  - DES/ECB/NoPadding (56)  
  - DES/ECB/PKCS5Padding (56)  
  - DESede/CBC/NoPadding (168)  
  - DESede/CBC/PKCS5Padding (168)  
  - DESede/ECB/NoPadding (168)  
  - DESede/ECB/PKCS5Padding (168)  
  - RSA/ECB/PKCS1Padding (1024, 2048)  
  - RSA/ECB/OAEPWithSHA-1AndMGF1Padding (1024, 2048)  
  - RSA/ECB/OAEPWithSHA-256AndMGF1Padding (1024, 2048)

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators:** | .NET, Java, Apple, Android |

### [Availability](#Availability)

This data type is available as of [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?28265,,).  
For Native Mobile environments, it is available as of [Genexus 15 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?38023,,) for Apple and [GeneXus 15 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?38845,,) for Android.


|  |
| --- |
| **Backlinks** |
| [Toc:Cryptography data types](https://wiki.genexus.com/commwiki/wiki?22980) |

---
