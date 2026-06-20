---
title: "Disconnect method"
source_id: 7101
source_url: https://wiki.genexus.com/commwiki/wiki?7101
genexus_version: "18"
---

# Disconnect method

Disconnects the associated data store.

### [Syntax](#Syntax)

**&***DataType***.Disconnect()**  
  
**Type Returned:**   
Numeric

### [Scope](#Scope)

**Extended Data Types:** [DBConnection](https://wiki.genexus.com/commwiki/wiki?6923)  
**Objects:**

[Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)  
**Generators:** 

[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

When you have a DBConnection variable, this method disconnects from the data store associated to the variable. It returns zero if the connection was successful. If there was an error, it returns its code.   
This method does not give an error when used in a program generated with the "Connect at first request" property, if the connection has not been made yet.

### [See Also](#See+Also)

[DBConnection](https://wiki.genexus.com/commwiki/wiki?6923)  
[Error Codes and Messages for DBConnection](https://wiki.genexus.com/commwiki/wiki?6945)


|  |
| --- |
| **Backlinks** |
| [DBConnection Data Type](https://wiki.genexus.com/commwiki/wiki?6923) | [LDAPClient Data Type](https://wiki.genexus.com/commwiki/wiki?6886) |

---
