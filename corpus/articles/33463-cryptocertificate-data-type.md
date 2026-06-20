---
title: "CryptoCertificate data type"
source_id: 33463
source_url: https://wiki.genexus.com/commwiki/wiki?33463
genexus_version: "18"
---

# CryptoCertificate data type

**Warning**: This data type will be discontinued in GeneXus 18 Upgrade 5. [GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) is on the way to replace this data type. It is recommended to migrate your code and use this API before GeneXus 18 Upgrade 5.

This is an API that enables you to handle certificates.

### [CryptoCertificate Methods](#CryptoCertificate+Methods)

|  |  |
| --- | --- |
| **Name** | **Description** |
| **Load(**certPath:String,[password]**)**:Int(ErrCode) | Allows initialization of a certificate from route and password if necessary. |
| **FromBase64(**data:String**)** | Initializes certificate from its representation in base64. |
| **ToBase64()**:String | Obtains a representation of the certificate in base64. |
| **KeyInfo()**:StringCollection | Allows us to specify the information from the certificate that must be added to the signature when an XML signature is generated. |
| **HasPrivateKey()**: Boolean | Returns true if the certificate has an associated private key. The private key is necessary to de-encrypt texts. |
| **Verify()**:Boolean | Indicates if the certificate is reliable. |

### [Properties](#Properties)

|  |  |
| --- | --- |
| **Issuer**:Character |  |
| **Subject**:Character |  |
| **SerialNumber**:Character |  |
| **Thumbprint**:Character |  |
| **NotAfter**:DateTime |  |
| **NotBefore:**DateTime |  |
| **Version**:Character |  |
| **ErrCode**:Numeric | Returns error of the last transaction. |
| **ErrDescription**:String | Returns a description of error of the last transaction. |

### [Example](#Example)

For instance, the execution of the following code allows reading of the certificate’s properties.

```
&subject = &cryptoCert.subject
```

The result will be similar to this:

CN = TESTING COMPANY   
SERIALNUMBER = RUC219999820013  
C = UY  
S = Montevideo  
O = TEST COMPANY  
OU = TEST AREA  
OU = TEST DIVISION  
E = prueba@correo.com.uy

### [Supported Certificates](#Supported+Certificates)

**NET** (requires an associated private key for digital signature)

* DER Encoded Binary X.509 (.cer)
* Base64 Encoded X.509 (.cer)
* PKCS#7 / Cryptographic Message Syntax Standard (.p7b)
* PKCS#12 / Personal Information Exchange (.pfx or .p12)

**JAVA**

* DER Encoded Binary X.509 (.cer)
* Base64 Encoded X.509 (.cer)
* PKCS#7 / Cryptographic Message Syntax Standard (.p7b)
* PKCS#12 / Personal Information Exchange (.pfx or .p12)
* Java Key Store (.jks)

**iOS (Swift)**

* DER Encoded Binary X.509 (.cer)
* PKCS#12 / Personal Information Exchange (.pfx or .p12)

### [Notes](#Notes)

* This data type is not supported for Windows applications. There are no plans to support it.
* Native Mobile apps only support Load and HasPrivateKeys methods.

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators:** | .NET, Java, Apple |

### [Availability](#Availability)

This data type is available as of [GeneXus 15](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?28265,,).  
For Native Mobile environments, it is available as of [Genexus 15 Upgrade 10](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?38023,,).


|  |
| --- |
| **Backlinks** |
| [Table of contents:Cryptography data types](https://wiki.genexus.com/commwiki/wiki?22980) |

---
