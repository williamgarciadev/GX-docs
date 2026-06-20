---
title: "GetNextUID method"
source_id: 7045
source_url: https://wiki.genexus.com/commwiki/wiki?7045
genexus_version: "18"
---

# GetNextUID method

Returns the UID of the following message.

### [Syntax](#Syntax)

**&***DataType***.GetNextUID(***UID***)**  
  
**Type Returned:**   
Numeric  
  
**Where:**  
*UID*  
    This parameter is Character, the UID of the following message in the present section.

### [Scope](#Scope)

**Extended Data Types:** [POP3Session](https://wiki.genexus.com/commwiki/wiki?6966)  
**Generators:** 

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

The UID is a chain that identifies each message in a unique manner. It is useful when messages received are kept in a database and are not deleted from the POP3 server.

In these cases, the UID of each message can be obtained before receiving the message, and this UID will be kept with the corresponding message. If there is already a message with the UID obtained, it is possible to skip it with the Skip method, instead of receiving it again. This mechanism is particularly useful when using a POP3 server that does not support the [NewMessages Property](https://wiki.genexus.com/commwiki/wiki?6961).   
  
Some servers cannot support this method. In these cases, error 30 is received.

**Note**: This method returns an error code, so it is possible to call it as a (I.E.: **&**Err **= &**POP3Session**.GetNextUID()**) function.

### [See Also](#See+Also)

[POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966)


|  |
| --- |
| **Backlinks** |
| [POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966) |

---
