---
title: "UserName Property"
source_id: 7001
source_url: https://wiki.genexus.com/commwiki/wiki?7001
genexus_version: "18"
---

# UserName Property

This property sets the user name that must be entered to obtain authentication in the server.

### [Syntax](#Syntax)

**&***DataType***.UserName**  
  
**Type Returned:**   
Character

### [Description](#Description)

**SMTPSession:** This property will be ignored if the value of the *Authentication* property is set to 0.   
  
**DBConnection:** Associates a user to the connection. The property must always contain the same value as the one returned by the userid('server') function.  This is true immediately after the connection is made and until the developer changes, if ever, its value. In this case the value may be different until the Connect() method is executed.

### [Scope](#Scope)

**Extended Data Types:** [DBConnection](https://wiki.genexus.com/commwiki/wiki?6923), [POP3Session](https://wiki.genexus.com/commwiki/wiki?6966), [SMTPSession](https://wiki.genexus.com/commwiki/wiki?6937)  
**Languages:** .NET, Java, Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [See Also](#See+Also)

[Authentication Property](https://wiki.genexus.com/commwiki/wiki?6982)  
[Receive Method](https://wiki.genexus.com/commwiki/wiki?6964)  
[Send Method](https://wiki.genexus.com/commwiki/wiki?6965)  
[POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966)  
[SMTPSession Data Type](https://wiki.genexus.com/commwiki/wiki?6937)  
[DBConnection DataType](https://wiki.genexus.com/commwiki/wiki?6923)


|  |
| --- |
| **Backlinks** |
| [Authentication Property](https://wiki.genexus.com/commwiki/wiki?6982) | [DBConnection Data Type](https://wiki.genexus.com/commwiki/wiki?6923) | [Login method](https://wiki.genexus.com/commwiki/wiki?6963) |
| [POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966) | [SMTPSession Data Type](https://wiki.genexus.com/commwiki/wiki?6937) | [Special considerations for SMTPSession or Pop3Session with Google Accounts](https://wiki.genexus.com/commwiki/wiki?50227) |
|

---
