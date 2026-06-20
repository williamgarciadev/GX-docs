---
title: "Sender Property"
source_id: 7015
source_url: https://wiki.genexus.com/commwiki/wiki?7015
genexus_version: "18"
---

# Sender Property

This property sets the sender data that is to be included in the messages sent.

### [Syntax](#Syntax)

**&***SMTPSession***.Sender**  
  
**Type Returned:**   
MailRecipient

### [Description](#Description)

When a *SMTPSession* type variable is created, the Senderproperty has a MailRecipient object with empty Name and Addressproperties. Thus, the sender data can be directly assigned in the *Name* and *Address* properties of the already created object. Another option is to assign another MailRecipienttype object from which these properties can be copied.   
   
It is necessary to have valid data in the Sender property so that the Login method can work.

### [Scope](#Scope)

**Extended Data Types:** [SMTPSession](https://wiki.genexus.com/commwiki/wiki?6937)  
**Languages:** .NET, Java, Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [See Also](#See+Also)

[Login Method](https://wiki.genexus.com/commwiki/wiki?6963)  
[MailRecipient Data Type](https://wiki.genexus.com/commwiki/wiki?6926)  
[Send Method](https://wiki.genexus.com/commwiki/wiki?6965)  
[SMTPSession Data Type](https://wiki.genexus.com/commwiki/wiki?6937)


|  |
| --- |
| **Backlinks** |
| [SMTPSession Data Type](https://wiki.genexus.com/commwiki/wiki?6937) |

---
