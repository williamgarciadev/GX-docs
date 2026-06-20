---
title: "WriteDocTypePublic method"
source_id: 7094
source_url: https://wiki.genexus.com/commwiki/wiki?7094
genexus_version: "18"
---

# WriteDocTypePublic method

#### [Writes the DocType declaration of the XML document with a Public Type declaration.](#Writes+the+DocType+declaration+of+the+XML+document+with+a+Public+Type+declaration.)

### [Syntax](#Syntax)

&DataType.**WriteDocTypePublic(***DocName, PubId, uri [ ,SubSet ]* **)**

**Where:**  
*DocName*  
     Name of DocType

*PubId*  
   Public Type declaration identification.

*uri*  
   Public Type declaration uri.

*SubSet*  
   Indicates the subset to be included in the declaration.

### [Description](#Description)

Writes the DocType declaration of the XML document with a Public Type declaration. If a Subset is included, it is entered between brackets at the end of the declaration.

### [Samples](#Samples)

```
WriteDocTypePublic(‘book,‘Id’, ‘http://www.ser.com/dtd’)
```

Generates the following: !DOCTYPE book PUBLIC “Id” “http://www.ser.com/dtd”. 

### [See Also](#See+Also)

[Xmlwriter Data Type](https://wiki.genexus.com/commwiki/wiki?6938)  
[WriteDocType](https://wiki.genexus.com/commwiki/wiki?7095)  
[WriteDocTypeSystem](https://wiki.genexus.com/commwiki/wiki?7096)


|  |
| --- |
| **Backlinks** |
| [WriteDocType method](https://wiki.genexus.com/commwiki/wiki?7095) | [WriteDocTypeSystem method](https://wiki.genexus.com/commwiki/wiki?7096) | [XMLWriter Data Type](https://wiki.genexus.com/commwiki/wiki?6938) |

---
