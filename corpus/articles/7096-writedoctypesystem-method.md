---
title: "WriteDocTypeSystem method"
source_id: 7096
source_url: https://wiki.genexus.com/commwiki/wiki?7096
genexus_version: "18"
---

# WriteDocTypeSystem method

Writes the DocType declaration of the XML document with a System Type declaration.

### [Syntax](#Syntax)

*DataType***.WriteDocTypeSystem(***DocName***,** *Uri* [ ,*SubSet* ] **)**

**Where:**  
*DocName*  
   Name of DocType

*Uri*  
   System type declaration uri

*SubSet*  
   Indicates the subset to be included in the declaration; must be string <>

### [Scope](#Scope)

**Extended Data Types:** [XmlWriter](https://wiki.genexus.com/commwiki/wiki?6938)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

Writes the DocType declaration of the XML document with a System Type declaration. If a Subset is included, it is entered between brackets at the end of the declaration.

### [Samples](#Samples)

```
WriteDocTypeSystem(‘book’,‘file.dtd’)
```

Generates the following: !DOCTYPE book SYSTEM “file.dtd”.

### [See Also](#See+Also)

[Xmlwriter Data Type](https://wiki.genexus.com/commwiki/wiki?6938)  
[WriteDocType](https://wiki.genexus.com/commwiki/wiki?7095)  
[WriteDocTypePublic](https://wiki.genexus.com/commwiki/wiki?7094)


|  |
| --- |
| **Backlinks** |
| [WriteDocType method](https://wiki.genexus.com/commwiki/wiki?7095) | [WriteDocTypePublic method](https://wiki.genexus.com/commwiki/wiki?7094) | [XMLWriter Data Type](https://wiki.genexus.com/commwiki/wiki?6938) |

---
