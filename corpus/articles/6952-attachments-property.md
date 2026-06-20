---
title: "Attachments Property"
source_id: 6952
source_url: https://wiki.genexus.com/commwiki/wiki?6952
genexus_version: "18"
---

# Attachments Property

Returns the paths to the files attached in a mail message and contains methods to add or remove attachments.

### [Syntax](#Syntax)

**&***MailMessageVariableName***.Attachments**  
  
**Type Returned:**   
StringCollection

**Where:**  
*MailMessageVariableName*  
    Is a variable based on the [MailMessage data type](https://wiki.genexus.com/commwiki/wiki?6925).

### [Scope](#Scope)

**Extended Data Types:** [MailMessage](https://wiki.genexus.com/commwiki/wiki?6925)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

When you receive a mail, the **Attachment** property contains the paths to the files attached to it.

If you need to add attachments to a mail message that you want to send, you can use the Add method as shown:

**&***MailMessageVariableName***.Attachments**.Add(*'path'*)

where:

*'path'*  
    Is the path where the file to be attached is located (including the file name and extension).

**Notes:**

* If a complete route is not specified when sending a message, the attached files will be searched for in the directory specified by the *AttachDir* property*.*
* To provide compatibility between the UNIX and Windows environments, you can use either the slash (/) or the backslash (\) as directory delimiters in the route of the attached files.

### [Sample](#Sample)

```
&MailMessage.Attachments.Add("C:\fullgx\kbaux\image001.jpg")
&MailMessage.Attachments.Add("C:\fullgx\kbaux\promptX.gif")
&MailMessage.Attachments.Add("C:\fullgx\kbaux\TempFile_1.txt")
```

### [See Also](#See+Also)

[AttachDir Property](https://wiki.genexus.com/commwiki/wiki?6953)  
[MailMessage data type](https://wiki.genexus.com/commwiki/wiki?6925)  
[StringCollection Data Type](https://wiki.genexus.com/commwiki/wiki?6954,,)


|  |
| --- |
| **Backlinks** |
| [AttachDir Property](https://wiki.genexus.com/commwiki/wiki?6953) | [MailMessage data type](https://wiki.genexus.com/commwiki/wiki?6925) |

---
