---
title: "Login method"
source_id: 6963
source_url: https://wiki.genexus.com/commwiki/wiki?6963
genexus_version: "18"
---

# Login method

Starts a session.

### [Syntax](#Syntax)

**&***DataType***.Login**  
  
**Type Returned:**   
Numeric

### [Scope](#Scope)

**Extended Data Types:** [MAPISession](https://wiki.genexus.com/commwiki/wiki?6935), [POP3Session](https://wiki.genexus.com/commwiki/wiki?6966), [SMTPSession](https://wiki.genexus.com/commwiki/wiki?6937)  
**Generators:** 

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

**MAPISession:** The MAPI session will be started with the profile indicated in the *Profile* property. If this property has not been assigned, a window will be opened, prompting you for the profile to be used.   
After starting a session with the indicated profile, the “Inbox” folder (or an equivalent one) is opened.  
   
**SMTPSession/POP3Session:** The SMTP/POP3 session will be started with the server indicated in the *Host* property and in the port indicated in the *Port* property. The values of the *UserName* and *Password* properties will be used for the server authentication.

**Note**: This method returns an error code, so it is possible to call it as a (I.E.:  &Err = &DataType.Login) function.

### [See Also](#See+Also)

[Authentication Property](https://wiki.genexus.com/commwiki/wiki?6982)  
[Host Property](https://wiki.genexus.com/commwiki/wiki?6999)  
[Password Property](https://wiki.genexus.com/commwiki/wiki?6994)  
[Port Property](https://wiki.genexus.com/commwiki/wiki?5019)  
[Profile Property](https://wiki.genexus.com/commwiki/wiki?7025)  
[UserName Property](https://wiki.genexus.com/commwiki/wiki?7001)  
[Receive Method](https://wiki.genexus.com/commwiki/wiki?6964)  
[Send Method](https://wiki.genexus.com/commwiki/wiki?6965)  
[MAPISession Data Type](https://wiki.genexus.com/commwiki/wiki?6935)  
[POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966)  
[SMTPSession Data Type](https://wiki.genexus.com/commwiki/wiki?6937)


|  |
| --- |
| **Backlinks** |
| [Authentication Property](https://wiki.genexus.com/commwiki/wiki?6982) | [Err variable](https://wiki.genexus.com/commwiki/wiki?51028) | [Host Property](https://wiki.genexus.com/commwiki/wiki?6999) |
| [MAPISession Data Type](https://wiki.genexus.com/commwiki/wiki?6935) | [NewMessages Property](https://wiki.genexus.com/commwiki/wiki?6961) | [POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966) | [Profile Property](https://wiki.genexus.com/commwiki/wiki?7025) |
| [Sender Property](https://wiki.genexus.com/commwiki/wiki?7015) | [SMTPSession Data Type](https://wiki.genexus.com/commwiki/wiki?6937) | [Timeout property](https://wiki.genexus.com/commwiki/wiki?7042) |

---
