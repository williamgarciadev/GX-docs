---
title: "Optional data"
source_id: 43578
source_url: https://wiki.genexus.com/commwiki/wiki?43578
genexus_version: "18"
---

# Optional data

**Note**: These options are part of [GeneXus Cryptography Module](https://wiki.genexus.com/commwiki/wiki?43917).

## [SDT DSigOptions](#SDT+DSigOptions)

### [Properties:](#Properties%3A)

* **DSigSignatureType**: DSigSignatureType Domain - Default value: ENVELOPED
* **Canonicalization**: Canonicalization Domain - Default value: C14n\_OMIT\_COMMENTS
* **KeyInfoType**: KeyInfoType Domain - Default value: X509Certificate
* **XmlSchemaPath**: Path of the XML Schema to verify. - Default value: empty
* **IdentifierAttribute**: Just for signing XML based on ID attribute.- Default value: empty

#### [Implementation details](#Implementation+details)

* DSigSignatureType, Canonicalization, and KeyInfoType are set by default on the most commonly used XML DSig configuration.
* XmlSchemaPath is empty by default. It receives a path to the XML schema; only .dtd, .xml and .xsd extensions are allowed. When this property is configured with anything but empty and it is passed to a signature method, it will try to verify the schema. To verify schemas on signed XMLs the schema must contain the definition for the signature or it will fail.
* IdentifierAttribute. In XML, a special Identification parameter with  [type ID](https://www.w3.org/TR/SVGMobile12/types.html#DataTypeID)  can be defined which is unique to the document. This property is used to find the name of the identifier on the XML document without using the schema definition because in most cases the attribute used as an identifier is not well defined or is not defined as an identifier at all. This property is required only to sign/verify an element finding it by its ID.

## [Security tips](#Security+tips)

* When assigning file paths, do not use user input concatenations or sanitize user entries to avoid path traversal or path manipulation vulnerability risks.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) | [XML DSig Signer](https://wiki.genexus.com/commwiki/wiki?43579) |

---
