---
title: "WriteDocType method"
source_id: 7095
source_url: https://wiki.genexus.com/commwiki/wiki?7095
genexus_version: "18"
---

# WriteDocType method

Writes the DocType declaration of the XML document.

### [Syntax](#Syntax)

**&***DataType***.WriteDocType(***DocName,* [*SubSet* ] **)**

**Where:**  
*DocName*  
   Name of the DocType

*SubSet*  
    Indicates the subset to be included in the declaration

### [Scope](#Scope)

**Extended data types:** [XMLWriter Data Type](https://wiki.genexus.com/commwiki/wiki?6938)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

Writes the DocType declaration of the XML document. If a Subset is included, it is entered between brackets at the end of the declaration.

### [Samples](#Samples)

```
WriteDocType(‘book’,‘!ENTITY ge “entity”’)
```

Generates the following:

```
<!DOCTYPE book [ !ENTITY ge “entity” ] >
```

### [See Also](#See+Also)

[XMLWriter Data Type](https://wiki.genexus.com/commwiki/wiki?6938)  
[WriteDocTypePublic method](https://wiki.genexus.com/commwiki/wiki?7094)  
[WriteDocTypeSystem method](https://wiki.genexus.com/commwiki/wiki?7096)


|  |
| --- |
| **Backlinks** |
| [WriteDocTypePublic method](https://wiki.genexus.com/commwiki/wiki?7094) | [WriteDocTypeSystem method](https://wiki.genexus.com/commwiki/wiki?7096) | [XMLWriter Data Type](https://wiki.genexus.com/commwiki/wiki?6938) |

---
