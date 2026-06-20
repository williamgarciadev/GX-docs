---
title: "GetAttributeName, GetAttributePrefix, GetAttributeLocalName,GetAttributeURI Methods"
source_id: 2712
source_url: https://wiki.genexus.com/commwiki/wiki?2712
genexus_version: "18"
---

# GetAttributeName, GetAttributePrefix, GetAttributeLocalName,GetAttributeURI Methods

Returns the different name components of an attribute that has name spaces, indicated by an index.

### Syntax

&DataType**.GetAttributeName**(*Index*)  
&DataType.**GetAttributePrefix**(*Index*)  
&DataType.**GetAttributeLocalName**(*Index*)  
&DataType.**GetAttributeURI**(*Index*)

Where:  
*Index* is the index of the attribute element.

Type Returned:  
Character

|  |  |
| --- | --- |
| **GetAttributeName** | Returns the full name, including the namespace if it exists. |
| **GetAttributePrefix** | Returns only the namespace if it exists. |
| **GetAttributeLocalName** | Returns the name of the attribute, excluding the namespace if it exists. |
| **GetAttributeURI** | Returns the URI of the namespace if it exists. |

### Notes

They are valid only for Element type nodes.  
The positions are numbered from 1 and up.

### Scope

**Extended Data Types:** [XMLReader Data Type](https://wiki.genexus.com/commwiki/wiki?6928)

### See Also

[XMLReader Data Type](https://wiki.genexus.com/commwiki/wiki?6928)


|  |
| --- |
| **Backlinks** |
| [XMLReader Data Type](https://wiki.genexus.com/commwiki/wiki?6928) |

---
