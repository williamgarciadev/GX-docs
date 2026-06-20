---
title: "WriteNSStartElement method"
source_id: 7060
source_url: https://wiki.genexus.com/commwiki/wiki?7060
genexus_version: "18"
---

# WriteNSStartElement method

Starts a compound element, but using namespaces.

### [Syntax](#Syntax)

**&***VarBasedOnXmlWriter*.**WriteNSStartElement(***LocalName* [ **,** *Prefix***,** *NameSpaceURI* ] **)**  
  
**Where:**  
*LocalName*  
   LocalName of the element to be created  
  
*Prefix*  
   Prefix of the element to be created  
  
*NameSpaceURI*  
   Uri of namespace

### [Scope](#Scope)

**Extended Data Types:** [XmlWriter](https://wiki.genexus.com/commwiki/wiki?6938)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[Java](https://wiki.genexus.com/commwiki/wiki?12258),
Ruby (up to GeneXus X Evolution 3),
Visual Basic (up to GeneXus X Evolution 3),
Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

#### [This method is equal to the [WriteStartElement method](https://wiki.genexus.com/commwiki/wiki?7069), but using namespaces.](#This+method+is+equal+to+the+wiki%3F7069%2CWriteStartElement%2Bmethod+WriteStartElement+method%2C+but+using+namespaces.)

If you indicate a NameSpaceURI that is not in the element’s definition environment, or if it has a prefix different from the Prefrix parameter, then the attribute xmlns:prefix=URI is created automatically.

### [See Also](#See+Also)

[Xmlwriter Data Type](https://wiki.genexus.com/commwiki/wiki?6938)  
[WriteNSElement](https://wiki.genexus.com/commwiki/wiki?7059)


|  |
| --- |
| **Backlinks** |
| [WriteNSElement method](https://wiki.genexus.com/commwiki/wiki?7059) | [XMLWriter Data Type](https://wiki.genexus.com/commwiki/wiki?6938) |

---
