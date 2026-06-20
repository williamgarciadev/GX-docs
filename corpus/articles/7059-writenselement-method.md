---
title: "WriteNSElement method"
source_id: 7059
source_url: https://wiki.genexus.com/commwiki/wiki?7059
genexus_version: "18"
---

# WriteNSElement method

Writes an element with the indicated value, using namespaces.

### [Syntax](#Syntax)

**&**DataType**.WriteNSElement(***LocalName* [ **,***NameSpaceURI* [ **,***Value* ] ] )  
  
**Where:**  
*LocalName*  
   Local Name of the element to be written  
  
*NameSpaceURI*   
   URI of namespace  
  
*Value*  
   Value of the element to be written

### [Scope](#Scope)

**Extended data types:** [XMLWriter Data Type](https://wiki.genexus.com/commwiki/wiki?6938)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

This method is equal to the [WriteElement method](https://wiki.genexus.com/commwiki/wiki?7070), but using namespaces.

The prefix is automatically determined, based on the defined prefixes in the element’s environment. If no prefix is associated to the specified URI, a name space is defined by default along with the element.

### [Samples](#Samples)

```
WriteNSElement(‘Price’, ’20.5’,‘http://www.genexus.com’)
```

Generates the following:

```
prefix:Price  20.5   /prefix:Price or
Price xmlns=” [http://www.genexus.com/|http://www.genexus.com]”   20.5   /Price
```

### [See Also](#See+Also)

[XMLWriter Data Type](https://wiki.genexus.com/commwiki/wiki?6938)  
[WriteNSStartElement method](https://wiki.genexus.com/commwiki/wiki?7060)


|  |
| --- |
| **Backlinks** |
| [WriteNSStartElement method](https://wiki.genexus.com/commwiki/wiki?7060) | [XMLWriter Data Type](https://wiki.genexus.com/commwiki/wiki?6938) |

---
