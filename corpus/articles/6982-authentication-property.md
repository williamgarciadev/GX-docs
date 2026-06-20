---
title: "Authentication Property"
source_id: 6982
source_url: https://wiki.genexus.com/commwiki/wiki?6982
genexus_version: "18"
---

# Authentication Property

Indicates whether the authentication with the server will be attempted or not.

### [Syntax](#Syntax)

**&***DataType***.Authentication**  
  
**Type Returned:**   
Numeric

### [Values](#Values)

|  |  |
| --- | --- |
| **0** | Indicates that the server does not require authentication. This is the default value. |
| **1** | Indicates that the server requires authentication. |

### [Description](#Description)

**SMTPSession:** The only authentication mechanism supported is C*lear Text*. If the *UserName* and *Password* properties are specified and the server does not support authentication by C*lear Text*,error 23 will occur.

### [Scope](#Scope)

**Extended Data Types:** [Location](https://wiki.genexus.com/commwiki/wiki?6981), [SMTPSession](https://wiki.genexus.com/commwiki/wiki?6937)  
**Languages:** .NET, Java, Ruby (up to Genexus X Evolution 3), Visual FoxPro (up to GeneXus X eEvolution 3)

### [See Also](#See+Also)

[Login Method](https://wiki.genexus.com/commwiki/wiki?6963)  
[Password Property](https://wiki.genexus.com/commwiki/wiki?6994)  
[UserName Property](https://wiki.genexus.com/commwiki/wiki?7001)  
[Send Method](https://wiki.genexus.com/commwiki/wiki?6965)  
[SMTPSession Data Type](https://wiki.genexus.com/commwiki/wiki?6937)  
[Location Data Type](https://wiki.genexus.com/commwiki/wiki?6981)  
[Locations](https://wiki.genexus.com/commwiki/wiki?6981)  
[AuthenticationMethod](https://wiki.genexus.com/commwiki/wiki?6990)  
[AuthenticationRealm](https://wiki.genexus.com/commwiki/wiki?6980)  
[AuthenticationUser](https://wiki.genexus.com/commwiki/wiki?7018)  
[AuthenticationPassword](https://wiki.genexus.com/commwiki/wiki?7019)


|  |
| --- |
| **Backlinks** |
| [AuthenticationMethod Property](https://wiki.genexus.com/commwiki/wiki?6990) | [AuthenticationMethod property (for mails data types)](https://wiki.genexus.com/commwiki/wiki?50349) | [AuthenticationPassword Property](https://wiki.genexus.com/commwiki/wiki?7019) |
| [AuthenticationRealm Property](https://wiki.genexus.com/commwiki/wiki?6980) | [AuthenticationUser Property](https://wiki.genexus.com/commwiki/wiki?7018) | [Location data type](https://wiki.genexus.com/commwiki/wiki?6981) | [Login method](https://wiki.genexus.com/commwiki/wiki?6963) |
| [Password property](https://wiki.genexus.com/commwiki/wiki?6994) | [SMTPSession Data Type](https://wiki.genexus.com/commwiki/wiki?6937) | [UserName Property](https://wiki.genexus.com/commwiki/wiki?7001) |

---
