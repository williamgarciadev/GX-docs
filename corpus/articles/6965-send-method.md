---
title: "Send method"
source_id: 6965
source_url: https://wiki.genexus.com/commwiki/wiki?6965
genexus_version: "18"
---

# Send method

Sends a message.

### [Syntax](#Syntax)

**&***VarBasedOnExtendedDataType***.Send(***Message***)**  
  
**Type Returned:**   
Numeric  
  
**Where:**  
*Message*  
    Is a *MailMessage* type parameter.

### [Scope](#Scope)

**Extended Data Types:** [MAPISession](https://wiki.genexus.com/commwiki/wiki?6935), [OutlookSession](https://wiki.genexus.com/commwiki/wiki?6936), [SMTPSession](https://wiki.genexus.com/commwiki/wiki?6937)  
**Generators:** 

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

**MAPISession:** If the address of a recipient cannot be solved, a Names window will be shown allowing the user to choose the right recipient among all the possible recipients for the address specified.   
After performing a Send, the immediate sending of emails is done compulsorily. As a result, if a telephone connection to the Internet is being used, dialing will begin when the Send method is called.    
  
**OutlookSession:** If a destination address cannot be solved, the editing window will be shown, as if the value of the *EditWindow* property were 1.

**Note**: This method returns an error code, so it is possible to call it as a (**&**Err **= &**DataType**.Send(…..)**) function.

### [See Also](#See+Also)

[EditWindow Property](https://wiki.genexus.com/commwiki/wiki?7030)  
[Receive Method](https://wiki.genexus.com/commwiki/wiki?6964)  
[MailMessage Data Type](https://wiki.genexus.com/commwiki/wiki?6925)  
[MAPISession Data Type](https://wiki.genexus.com/commwiki/wiki?6935)  
[OutlookSession Data Type](https://wiki.genexus.com/commwiki/wiki?6936)  
[SMTPSession Data Type](https://wiki.genexus.com/commwiki/wiki?6937)


|  |
| --- |
| **Backlinks** |
| [AttachDir Property](https://wiki.genexus.com/commwiki/wiki?6953) | [Authentication Property](https://wiki.genexus.com/commwiki/wiki?6982) | [ChangeFolder method](https://wiki.genexus.com/commwiki/wiki?6962) |
| [Count property](https://wiki.genexus.com/commwiki/wiki?7023) | [Delete method](https://wiki.genexus.com/commwiki/wiki?6014) | [EditWindow Property](https://wiki.genexus.com/commwiki/wiki?7030) | [Host Property](https://wiki.genexus.com/commwiki/wiki?6999) |
| [Login method](https://wiki.genexus.com/commwiki/wiki?6963) | [Logout method](https://wiki.genexus.com/commwiki/wiki?7080) | [MAPISession Data Type](https://wiki.genexus.com/commwiki/wiki?6935) | [MarksAsRead method](https://wiki.genexus.com/commwiki/wiki?7092) |
| [NewMessages Property](https://wiki.genexus.com/commwiki/wiki?6961) | [OutlookSession Data Type](https://wiki.genexus.com/commwiki/wiki?6936) | [Password property](https://wiki.genexus.com/commwiki/wiki?6994) | [Port Property](https://wiki.genexus.com/commwiki/wiki?5019) |
| [Profile Property](https://wiki.genexus.com/commwiki/wiki?7025) | [Receive method](https://wiki.genexus.com/commwiki/wiki?6964) | [Sender Property](https://wiki.genexus.com/commwiki/wiki?7015) | [SMTPSession Data Type](https://wiki.genexus.com/commwiki/wiki?6937) |
| [Timeout property](https://wiki.genexus.com/commwiki/wiki?7042) | [UserName Property](https://wiki.genexus.com/commwiki/wiki?7001) |

---
