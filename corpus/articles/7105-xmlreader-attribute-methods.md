---
title: "XMLReader Attribute Methods"
source_id: 7105
source_url: https://wiki.genexus.com/commwiki/wiki?7105
genexus_version: "18"
---

# XMLReader Attribute Methods

Possibility of accessing the notation and entity referenced by an attribute of the ENTITY type.

### [Syntax](#Syntax)

**GetAttEntityValueByIndex(***Index***)**  
  
**GetAttEntityValueByName(***Name***)**  
  
**GetAttEntityNotationByIndex(***Index***)**  
  
**GetAttEntityNotationByName(***Name***)**  
  
**Where:**  
*Index*   
   Index of the attribute  
  
*Name*  
   Name of the attribute  
  
**Type Returned:**  
   Character

### [Description](#Description)

The following methods enable accessing the notation and entity referenced by an attribute of the ENTITY type. The attribute may be specified with its position in the text or its name, and it is not verified when it is of the ENTITY type. If no statement was made in the document’s DTD for the attribute value, an empty string is returned.  
  
**Notes:**

* Valid for nodes of the Element type only.
* Positions are numbered starting at 1.

### [Scope](#Scope)

**Extended Data Types:** [XmlReader](https://wiki.genexus.com/commwiki/wiki?6928)  
**Languages:** .NET, Java, Ruby (up to GeneXus X Evolution 3), Visual FoxPro  (up to GeneXus X Evolution 3)

### [See Also](#See+Also)

[XmlReader Data Type](https://wiki.genexus.com/commwiki/wiki?6928)


|  |
| --- |
| **Backlinks** |
| [XMLReader Data Type](https://wiki.genexus.com/commwiki/wiki?6928) |

---
