---
title: "WSSecurity Data Type"
source_id: 44552
source_url: https://wiki.genexus.com/commwiki/wiki?44552
genexus_version: "18"
---

# WSSecurity Data Type

Consumes WS-Security services. Not applicable for providing SOAP Web Services. It is only used to consume WS.  
The [Use Native Soap property](https://wiki.genexus.com/commwiki/wiki?13446) must be set to Yes.

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)  
**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

WS-Security services allow for secure interoperability with web services. For this, the messages transmitted are protected to:

- Validate that the message was not modified during transmission (integrity).  
- Not allow the message to be seen by a third party (confidentiality).

The mechanism is based on modifying SOAP messages; specific SOAP headers are included and the SOAP body is modified with information that is used to ensure integrity and confidentiality.

These modifications involve adding the following:

- A security token that specifies the credentials of the originator of the message.  
- A description of how the message is signed (key used, algorithm, which part of the message is signed) and its signature.  
- A description of how the message is encrypted (encryption key, algorithm, which part of the message is encrypted).

### [WSSecurity Properties](#WSSecurity+Properties+)

|  |  |  |
| --- | --- | --- |
| Signature | WSSignature | It specifies the information for signing the SOAP message. |
| Encryption | WSEncryption | It specifies the information for encrypting the SOAP message. |
| ExpirationTimeout | Numeric | It allows the creation of Expiration information in the Soap Header. It is specified in seconds. |

### [WSSignature Properties](#WSSignature+Properties+)

|  |  |
| --- | --- |
| Keystore | WSSecurityKeyStore |
| Alias | Character |
| keyIdentifierType | Numeric |
| CanonicalizationAlgorithm | Character |
| SignatureAlgorithm | Character |
| Digest | Character |

### [WSEncryption Properties](#WSEncryption+Properties+)

|  |  |
| --- | --- |
| Keystore | WSSecurityKeyStore |
| Alias | Character |
| keyIdentifierType | Numeric |

### [WSSecurityKeyStore Properties](#WSSecurityKeyStore+Properties+)

|  |  |
| --- | --- |
| Type | Character |
| Password | Character |
| Source | Character |

Constants for the property keyIdentifierType from WSSignature Data Type and WSEncryption Data Type:

|  |
| --- |
| BINARY\_SECURITY\_TOKEN |
| ISSUER\_SERIAL |
| X509\_KEY\_IDENTIFIER |
| SKI\_KEY\_IDENTIFIER |
| THUMBPRINT\_IDENTIFIER |
| KEY\_VALUE |

Constants for the property Type from WSSecurityKeyStore Data Type:

|  |
| --- |
| JKS |
| JCEKS |
| PKCS11 |

### [Sample](#Sample)

```
//Encryption
&WsSecurityKeyStore.Password = "prueba123"
&WsSecurityKeyStore.Type = WSSecurityKeyStore.JKS
&WsSecurityKeyStore.Source = "C:\temp\keystoreprueba.jks"

&wsEncryption.Alias = "epagos"
&wsEncryption.keyIdentifierType = WsSecurity.BINARY_SECURITY_TOKEN
&wsEncryption.Keystore = &WsSecurityKeyStore

&wssecurity.Encryption = &wsEncryption

&wssecurity.ExpirationTimeout = 5

//Signature
&wssecurity.Signature.Alias = "alias1"
&wssecurity.Signature.keyIdentifierType = WsSecurity.BINARY_SECURITY_TOKEN
&wssecurity.Signature.Keystore.Password = "PasswordAlias1"
&wssecurity.Signature.Keystore.Type = WSSecurityKeyStore.JKS
&wssecurity.Signature.Keystore.Source = "C:\temp\prueba2.jks"

&wssecurity.Signature.CanonicalizationAlgorithm = "CanonicalizationMethod.EXCLUSIVE"
&wssecurity.Signature.SignatureAlgorithm = "http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"
&wssecurity.Signature.Digest = "DigestMethod.SHA256"

&location.WSSecurity = &wssecurity
```

### [See Also](#See+Also)

[Locations](https://wiki.genexus.com/commwiki/wiki?6981)
