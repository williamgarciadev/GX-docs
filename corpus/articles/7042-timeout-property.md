---
title: "Timeout property"
source_id: 7042
source_url: https://wiki.genexus.com/commwiki/wiki?7042
genexus_version: "18"
---

# Timeout property

Sets the maximum time (in seconds) that the system will wait for an answer to be sent from the server after each request.

### [Syntax](#Syntax)

**&***ExtendedDataType***.Timeout** = <numeric-expression>

**Where:**

**&***ExtendedDataType*  
  Is a variable based on the [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932) or [Location data type](https://wiki.genexus.com/commwiki/wiki?6981) or [POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966) or [SMTPSession Data Type](https://wiki.genexus.com/commwiki/wiki?6937).

numeric-expression  
   Is a Numeric [expression](https://wiki.genexus.com/commwiki/wiki?51320,,) that indicates the maximum time (in seconds) that the system will wait for an answer to be sent from the server after each request.

**Type Returned:**  
None

### [Description](#Description)

This value must be adapted to the communication network speed and to the server load. Low values should be used for local networks, and higher values for the Internet, particularly if there is a connection to remote servers.

* POP3Session, SMTPSession: The default value is 30.
* Location: The default value is 0, which means that the waiting time is undefined.

### [Scope](#Scope)

**Extended Data Types:** [HttpClient](https://wiki.genexus.com/commwiki/wiki?6932), [Location](https://wiki.genexus.com/commwiki/wiki?6981), [POP3Session](https://wiki.genexus.com/commwiki/wiki?6966), [SMTPSession](https://wiki.genexus.com/commwiki/wiki?6937)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Runtime / Design time](#Runtime+%2F+Design+time)

This property applies only at runtime.

### [See Also](#See+Also)

[Login Method](https://wiki.genexus.com/commwiki/wiki?6963)  
[Receive Method](https://wiki.genexus.com/commwiki/wiki?6964)  
[Send Method](https://wiki.genexus.com/commwiki/wiki?6965)  
[POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966)  
[SMTPSession Data Type](https://wiki.genexus.com/commwiki/wiki?6937)  
[Location Data Type](https://wiki.genexus.com/commwiki/wiki?6981)  
[Locations](https://wiki.genexus.com/commwiki/wiki?6981)  
[HttpClient Data Type](https://wiki.genexus.com/commwiki/wiki?6932)


|  |
| --- |
| **Backlinks** |
| [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932) | [HttpClient data type (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?55613) | [Location data type](https://wiki.genexus.com/commwiki/wiki?6981) |
| [POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966) | [SMTPSession Data Type](https://wiki.genexus.com/commwiki/wiki?6937) |

---
