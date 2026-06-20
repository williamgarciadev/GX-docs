---
title: "NodeType Property"
source_id: 6997
source_url: https://wiki.genexus.com/commwiki/wiki?6997
genexus_version: "18"
---

# NodeType Property

Returns the current node type obtained through the method Read or ReadType.

### [Syntax](#Syntax)

**&***DataType***.NodeType**  
  
**Type Returned:**   
Integer

### [Values](#Values)

**1:**         Element  
**2:**         EndTag  
**4:**         Text  
**8:**         Comment  
**16:**       WhiteSpace  
**32:**       Cdata  
**64:**       ProcessingInstruction  
**128:**     DocumentType  
  
**Note:**

The following properties contain constant values which can be used to compare the NodeType property result to the ReadType method.

* CDataType
* CommentType
* DoctypeType
* ElementType
* EndTagType
* ProcessingInstructionType
* TextType
* WhiteSpaceType

### [Scope](#Scope)

**Extended Data Types:** [XmlReader](https://wiki.genexus.com/commwiki/wiki?6928)  
**Languages:** .NET, Java, Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [See Also](#See+Also)

[XmlReader Data Type](https://wiki.genexus.com/commwiki/wiki?6928)


|  |
| --- |
| **Backlinks** |
| [XMLReader Data Type](https://wiki.genexus.com/commwiki/wiki?6928) |

---
