---
title: "CryptoSignXML data type"
source_id: 33459
source_url: https://wiki.genexus.com/commwiki/wiki?33459
genexus_version: "18"
---

# CryptoSignXML data type

**Warning**: This data type will be discontinued in GeneXus 18 Upgrade 5. [GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) is on the way to replace this data type. It is recommended to migrate your code and use this API before GeneXus 18 Upgrade 5.

CryptoSignXML belongs to the [Cryptography data types](https://wiki.genexus.com/commwiki/wiki?22980). It enables us to handle digital signatures for XML documents with a public-private key according to the [XMLDSIG](http://www.w3.org/TR/xmldsig-core/) standard, using X509 certificates.

### [CryptoSignXML Methods](#CryptoSignXML+Methods)

|  |  |
| --- | --- |
| **Name** | **Description** |
| **Sign(**text:String**)**:String | Returns the XML signature resulting from the application of the signature algorithm using the specified certificate on the XML text entered. This is called XML Signature. |
| **SignElements(**text:String,Xpath:String**)**:String | Returns the XML signature resulting from the application of the signature algorithm using the specified certificate on the XML text entered. The signature is applied to each element verified by the xPath , which is used as an element selector. |
| **Verify(**signatre:String**)** | In the case of a signed XML, it verifies the match of the signature and the text, using the data from the certificate configured. When the certificate is not indicated, it is inferred from the signature Tag of the signature. |
| **AddReference(**xmlNode:String**)** | The signature is calculated from the string specified by the parameter. The parameter should be an XML node. |

### [Properties](#Properties)

|  |  |
| --- | --- |
| **KeyInfoClauses**:StringCollection | Allows us to add information to the signature. By default, the signature contains X509IssuerSerial, X509SubjectName, X509Certificate. Another supported value for KeyInfoClauses is RSAKeyValue. Eg: &CryptoSignXML.KeyInfoClauses.Add('RSAKeyValue') |
| **Certificate**:CryptoCertificate | Allows us to specify the certificate to be used in signing the text. |
| **ValidateCertificate**:Boolean | Specifies if the validity of the certificate specified in the Create method must be validated or not. |

### [Notes](#Notes)

* ### [The signature done today on XML documents is [Enveloped](http://es.wikipedia.org/wiki/Firma_XML).](#The+signature+done+today+on+XML+documents+is+http%3A%2F%2Fes.wikipedia.org%2Fwiki%2FFirma_XML+Enveloped.)

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators:** | .NET, Java |


|  |
| --- |
| **Backlinks** |
| [Toc:Cryptography data types](https://wiki.genexus.com/commwiki/wiki?22980) |

---
