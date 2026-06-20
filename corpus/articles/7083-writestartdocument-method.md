---
title: "WriteStartDocument method"
source_id: 7083
source_url: https://wiki.genexus.com/commwiki/wiki?7083
genexus_version: "18"
---

# WriteStartDocument method

Writes the XML declaration using version 1.0 and ISO-8859-1 coding.

### [Syntax](#Syntax)

**&***DataType***.WriteStartDocument(** **[***Encoding***[,** *StandAlone* ]] **)**  
  
**Where:**  
*Encoding*  
   Corresponds to the encoding to be used in the XML file. Must be a text. Its optional.

*StandAlone*  
   Must be 0 or 1; its optional.

### [Scope](#Scope)

**Extended Data Types:** [XmlWriter](https://wiki.genexus.com/commwiki/wiki?6938)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

* Optionally, you can indicate a text value to set the encoding of the XML file. The default value for the encoding is "ISO-8859-1".
* You also have the option to indicate an integer (0/1) as a Boolean value to be used in the standalone declaration.
* This method must be called at the start of the document’s generation (after the open() and before any other method).

### [See Also](#See+Also)

[Xmlwriter Data Type](https://wiki.genexus.com/commwiki/wiki?6938)


|  |
| --- |
| **Backlinks** |
| [Encodings in GeneXus](https://wiki.genexus.com/commwiki/wiki?19316) | [XMLWriter Data Type](https://wiki.genexus.com/commwiki/wiki?6938) |

---
