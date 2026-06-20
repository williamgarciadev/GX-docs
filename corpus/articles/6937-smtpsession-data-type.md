---
title: "SMTPSession Data Type"
source_id: 6937
source_url: https://wiki.genexus.com/commwiki/wiki?6937
genexus_version: "18"
---

# SMTPSession Data Type

Unifies interaction functions with the sending and reception of messages for the different languages generated.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

It allows you to use a mail session to send messages through a server using the SMTP protocol (Simple Mail Transfer Protocol).

To use this feature, the requirement is to have TCP/IP protocol installed. It does not require Microsoft Office.

An important advantage of this implementation is that it enables the use of more than one connection event to the mail server.

### [Properties](#Properties)

|  |
| --- |
| [AttachDir](https://wiki.genexus.com/commwiki/wiki?6953) |
| [Authentication](https://wiki.genexus.com/commwiki/wiki?6982) |
| [ErrCode](https://wiki.genexus.com/commwiki/wiki?6930) |
| [ErrDescription](https://wiki.genexus.com/commwiki/wiki?6931) |
| [ErrDisplay](https://wiki.genexus.com/commwiki/wiki?6929) |
| [Host](https://wiki.genexus.com/commwiki/wiki?6999) |
| [AuthenticationMethod](https://wiki.genexus.com/commwiki/wiki?50349) |
| [Password](https://wiki.genexus.com/commwiki/wiki?6994) |
| [Port](https://wiki.genexus.com/commwiki/wiki?5019) |
| [Sender](https://wiki.genexus.com/commwiki/wiki?7015) |
| [Timeout](https://wiki.genexus.com/commwiki/wiki?7042) |
| [UserName](https://wiki.genexus.com/commwiki/wiki?7001) |
| [Secure](https://wiki.genexus.com/commwiki/wiki?21181) |

**Note**: The [AuthenticationMethod property](https://wiki.genexus.com/commwiki/wiki?50349) can be used since [GeneXus 17 Upgrade 9](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?49956,,) because it is related to a new implementation of the data type. This implementation is not active by default. To activate it, you have to create a file named "config.gx" under the Knowledge Base root directory containing the following line: "SMTPSession=MailKit".

### [Methods](#Methods)

|  |
| --- |
| [Login](https://wiki.genexus.com/commwiki/wiki?6963) |
| [Logout](https://wiki.genexus.com/commwiki/wiki?7080) |
| [Send](https://wiki.genexus.com/commwiki/wiki?6965) |

### [Sample](#Sample)

The following sample is for Gmail and shows the configuration of some properties for a variable based on the SMTPSession data type:

```
    &SMTPSession.Host = 'smtp.gmail.com'
    &SMTPSession.Port = 465
    &SMTPSession.Timeout = 20
    &SMTPSession.Secure = 1
    &SMTPSession.Authentication = 1
    &SMTPSession.UserName = 'Info@gmail.com'
    &SMTPSession.Password = '**********************'
    &SMTPSession.Sender.Address  = 'Info@gmail.com'
    &SMTPSession.Sender.Name  = 'Info@gmail.com'
    
    &ret = &SMTPSession.Login() 
    if &SMTPSession.ErrCode <> 0 
       &MailMsg = &ret.ToString() + ':Error al loguease'
       Do 'ManageError'                     //subroutine that manages errors  
    else
       &MailMsg = "login OK"               //&MailMsg is based on the varchar data type
       &MailMessage.Clear()                //&MailMessage is based on the [[MailMessage Data Type]]
       &MailMessage.To.Clear() 
       &MailMessage.BCC.Clear()
       &MailMessage.CC.Clear() 
       &MailMessage.Subject="Email Subject XXX"
       &MailMessage.Text="Message body" 
       &MailMessage.Attachments.Clear()

       &MailRecipient.Address = "xxx@gmail.com"   //&MailRecipient is based on the [[MailRecipient Data Type]]
       &MailRecipient.Name = "xxx"    
       &MailMessage.To.Add(&MailRecipient)
       &MailMessage.CC.Add(&MailRecipient)
       &MailMessage.BCC.Add(&MailRecipient)
   
       &sendmsg = &SMTPSession.Send(&MailMessage)    
       &ret = &SMTPSession.Logout()
   endif
```

### [See Also](#See+Also)

[MAPISession Data Type](https://wiki.genexus.com/commwiki/wiki?6935)  
[OutlookSession Data Type](https://wiki.genexus.com/commwiki/wiki?6936)  
[POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966)  
[Special considerations for SMTPSession or Pop3Session with Google Accounts](https://wiki.genexus.com/commwiki/wiki?50227)


|  |
| --- |
| **Backlinks** |
| [A03:2021 - Injection](https://wiki.genexus.com/commwiki/wiki?50183) | [AttachDir Property](https://wiki.genexus.com/commwiki/wiki?6953) |
| [Authentication Property](https://wiki.genexus.com/commwiki/wiki?6982) | [AuthenticationMethod property (for mails data types)](https://wiki.genexus.com/commwiki/wiki?50349) | [Data types list](https://wiki.genexus.com/commwiki/wiki?6779) | [ErrCode Property](https://wiki.genexus.com/commwiki/wiki?6930) |
| [ErrDescription Property](https://wiki.genexus.com/commwiki/wiki?6931) | [ErrDisplay Property](https://wiki.genexus.com/commwiki/wiki?6929) | [Error Codes and Messages for SMTPSession](https://wiki.genexus.com/commwiki/wiki?6943) |
| [Host Property](https://wiki.genexus.com/commwiki/wiki?6999) | [Login method](https://wiki.genexus.com/commwiki/wiki?6963) | [Logout method](https://wiki.genexus.com/commwiki/wiki?7080) |
| [Mail Secure Property](https://wiki.genexus.com/commwiki/wiki?21181) | [MailMessage data type](https://wiki.genexus.com/commwiki/wiki?6925) | [MAPISession Data Type](https://wiki.genexus.com/commwiki/wiki?6935) | [OutlookSession Data Type](https://wiki.genexus.com/commwiki/wiki?6936) |
| [Password property](https://wiki.genexus.com/commwiki/wiki?6994) | [POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966) | [Port Property](https://wiki.genexus.com/commwiki/wiki?5019) | [Send method](https://wiki.genexus.com/commwiki/wiki?6965) |
| [Sender Property](https://wiki.genexus.com/commwiki/wiki?7015) | [Special considerations for SMTPSession or Pop3Session with Google Accounts](https://wiki.genexus.com/commwiki/wiki?50227) | [Timeout property](https://wiki.genexus.com/commwiki/wiki?7042) |
| [UserName Property](https://wiki.genexus.com/commwiki/wiki?7001) |

---
