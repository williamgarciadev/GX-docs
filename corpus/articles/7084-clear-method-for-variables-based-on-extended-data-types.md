---
title: "Clear method for variables based on Extended data types"
source_id: 7084
source_url: https://wiki.genexus.com/commwiki/wiki?7084
genexus_version: "18"
---

# Clear method for variables based on Extended data types

Clears or empties the variable based on an Extended data type, to which you apply the method.

### [Syntax](#Syntax)

**&***VarBasedOnExtendedDataType***.Clear()**

**Where:**

**&***VarBasedOnExtendedDataType*Is the [Variable](https://wiki.genexus.com/commwiki/wiki?7375) name to which the method is applied.

**Type returned:**   
Numeric

### [Scope](#Scope)

**Data Types:** [Cache](https://wiki.genexus.com/commwiki/wiki?32105), [ExcelDocument](https://wiki.genexus.com/commwiki/wiki?2476), [MailMessage](https://wiki.genexus.com/commwiki/wiki?6925), [Properties](https://wiki.genexus.com/commwiki/wiki?31606), 
WApiApplicationData, WApiFilter, [WebSession](https://wiki.genexus.com/commwiki/wiki?6321), [MailRecipientCollection](https://wiki.genexus.com/commwiki/wiki?6996), [StringCollection](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?6954,,), [WebSession](https://wiki.genexus.com/commwiki/wiki?6321)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

This method clears or empties the variable based on an Extended data type, to which you apply the method.

In the case of:

* ExcelDocument: It deletes the contents of all cells in the active worksheet.
* MailRecipientCollection/StringCollection: It empties the collection. All collection elements are deleted.
* WebSession: It clears the web session variables.

**Note**:This method returns an error code, so it is possible to call it as a function (**&**Err **= &**DataType**.Clear()**).

### [See Also](#See+Also)

[ExcelDocument data type](https://wiki.genexus.com/commwiki/wiki?2476)  
[MailRecipient Data Type](https://wiki.genexus.com/commwiki/wiki?6926)  
[MailRecipientCollection Data Type](https://wiki.genexus.com/commwiki/wiki?6996)  
[StringCollection Data Type](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?6954,,)


|  |
| --- |
| **Backlinks** |
| [ExcelDocument data type](https://wiki.genexus.com/commwiki/wiki?2476) | [MailRecipientCollection Data Type](https://wiki.genexus.com/commwiki/wiki?6996) | [Properties data type](https://wiki.genexus.com/commwiki/wiki?31606) |
| [WebSession data type](https://wiki.genexus.com/commwiki/wiki?6321) |

---
