---
title: "ValidationType property"
source_id: 6969
source_url: https://wiki.genexus.com/commwiki/wiki?6969
genexus_version: "18"
---

# ValidationType property

Determines how to validate the XML file.

### [Syntax](#Syntax)

**&***DataType***.ValidationType**

### [Values](#Values)

|  |  |
| --- | --- |
| **0** | Validation is not carried out |
| **1** | Automatic validation |
| **2** | Validation by means of DTD |
| **3** | Validation by means of a “Schema” |
| **4** | Validation by means of XDR |

### [Description](#Description)

When the automatic validation is selected, the behavior is the following (extracted from .NET documentation):

If there is no DTD or schema, it will parse the XML without validation.

If there is a DTD defined in a !DOCTYPE ... declaration, it will load the DTD and process the DTD declarations so that default attributes and general entities will be made available. General entities are only loaded and parsed if they are used (expanded).

If there is no !DOCTYPE ... declaration but there is an XSD "schemaLocation" attribute, it will load and process those XSD schemas and it will return any default attributes defined in those schemas.

If there is no !DOCTYPE ... declaration and no XSD or XDR schema information then the parser is a non-validating parser (i.e. ValidationType=ValidationType.None)

If there is no !DOCTYPE ... declaration and no XSD "schemaLocation" attribute but there are some namespaces using the MSXML "x-schema:" URN prefix, it will load and process those schemas and it will return any default attributes defined in those schemas.

If there is no !DOCTYPE ... declaration but there is a schema declaration (schema), it will validate using the in-line schema.

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Extended data types** | [XMLReader Data Type](https://wiki.genexus.com/commwiki/wiki?6928) |
| **Languages** | .NET, Java, Ruby (up to GeneXus X Evolution 3) |
|  |  |

### [See also](#See+also)

[XMLReader Data Type](https://wiki.genexus.com/commwiki/wiki?6928)


|  |
| --- |
| **Backlinks** |
| [A03:2021 - Injection](https://wiki.genexus.com/commwiki/wiki?50183) | [A08:2021 - Software and data integrity failures](https://wiki.genexus.com/commwiki/wiki?50188) |
| [AddSchema method](https://wiki.genexus.com/commwiki/wiki?7073) | [XMLReader Data Type](https://wiki.genexus.com/commwiki/wiki?6928) |

---
