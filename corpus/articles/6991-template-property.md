---
title: "Template property"
source_id: 6991
source_url: https://wiki.genexus.com/commwiki/wiki?6991
genexus_version: "18"
---

# Template property

Indicates the name of the template that will be used for new documents.

### [Syntax](#Syntax)

**control.** Template   

**&***DataType***.Template =** *Template*  
  
**Type Returned:**  
Character  
  
**Where:**  
*DataType*  
Is the name of the ExcelDocument or WordDocument type variable.  
  
*Template*  
Indicates the path and the name of the file that will be used as Template in subsequent calls to the *Open* method with a nonexistent file name.  
The default value is the empty string. In this case, the default template will be used.

### [Scope](#Scope)

**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258), .NET  
**Level:** [Variable](https://wiki.genexus.com/commwiki/wiki?7375)

### [Description](#Description)

This property applies to variables based on the [ExcelDocument](https://wiki.genexus.com/commwiki/wiki?2476), [WordDocument](https://wiki.genexus.com/commwiki/wiki?2478,,) Data Types.

`[imagen omitida: wiki id 48400]`

If a template is defined and then deleted because it is no longer needed, to use the default template again, you have to call this property by sending an empty string as the parameter (“”).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at run-time.

### [See Also](#See+Also)

[Open method](https://wiki.genexus.com/commwiki/wiki?6992)  
[ExcelDocument data type](https://wiki.genexus.com/commwiki/wiki?2476)


|  |
| --- |
| **Backlinks** |
| [ExcelDocument data type](https://wiki.genexus.com/commwiki/wiki?2476) | [Open method](https://wiki.genexus.com/commwiki/wiki?6992) |

---
