---
title: "WriteElement method"
source_id: 7070
source_url: https://wiki.genexus.com/commwiki/wiki?7070
genexus_version: "18"
---

# WriteElement method

Writes an element with the indicated value.

### [Syntax](#Syntax)

**&**DataType**.WriteElement(***ValueName***,** *ElementValue***)**  
  
**Where:**  
*ValueName*  
   Name of the element  
  
*ElementValue*  
   Value to be written inside the element

### [Scope](#Scope)

**Extended Data Types:** [XmlWriter](https://wiki.genexus.com/commwiki/wiki?6938)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

  
**N****otes:**

* When ElementValue is of the Character type, special characters are substituted by character sequences (the '<' is substituted by '<', the '>' by '>', and so on).
* Unlike WriteStartElement, the element created does not contain sub-elements.

### [See Also](#See+Also)

[Xmlwriter Data Type](https://wiki.genexus.com/commwiki/wiki?6938)  
[WriteStartElement](https://wiki.genexus.com/commwiki/wiki?7069)


|  |
| --- |
| **Backlinks** |
| [WriteAttribute method](https://wiki.genexus.com/commwiki/wiki?7068) | [WriteNSElement method](https://wiki.genexus.com/commwiki/wiki?7059) | [WriteStartElement method](https://wiki.genexus.com/commwiki/wiki?7069) |
| [XMLWriter Data Type](https://wiki.genexus.com/commwiki/wiki?6938) |

---
