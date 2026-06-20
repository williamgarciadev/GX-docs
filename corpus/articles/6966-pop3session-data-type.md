---
title: "POP3Session Data Type"
source_id: 6966
source_url: https://wiki.genexus.com/commwiki/wiki?6966
genexus_version: "18"
---

# POP3Session Data Type

Unifies interaction functions with the sending and reception of messages for the different languages generated.

An important advantage of this implementation is that it enables the use of more than one connection event to the mail server.

### [Description](#Description)

It allows you to use a mail session to receive messages from a server using the POP3 protocol (Post Office Protocol Version 3).

To use this feature, the requirement is to have installed TCP/IP protocol. It does not require Microsoft Office.

### [Properties](#Properties)

|  |  |
| --- | --- |
| [AttachDir](https://wiki.genexus.com/commwiki/wiki?6953) | [NewMessages](https://wiki.genexus.com/commwiki/wiki?6961) |
| [Count](https://wiki.genexus.com/commwiki/wiki?7023) | [Password](https://wiki.genexus.com/commwiki/wiki?6994) |
| [ErrCode](https://wiki.genexus.com/commwiki/wiki?6930) | [Port](https://wiki.genexus.com/commwiki/wiki?5019) |
| [ErrDescription](https://wiki.genexus.com/commwiki/wiki?6931) | [Timeout](https://wiki.genexus.com/commwiki/wiki?7042) |
| [ErrDisplay](https://wiki.genexus.com/commwiki/wiki?6929) | [UserName](https://wiki.genexus.com/commwiki/wiki?7001) |
| [Host](https://wiki.genexus.com/commwiki/wiki?6999) | [Secure](https://wiki.genexus.com/commwiki/wiki?21181) |
| [AuthenticationMethod](https://wiki.genexus.com/commwiki/wiki?50349) |  |

**Note**: The [AuthenticationMethod property](https://wiki.genexus.com/commwiki/wiki?50349) can be used since [GeneXus 17 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?49956,,) because it is related to a new implementation of the data type. Momentarily, this implementation is not active by default. To activate it, you have to create a file named "*config.gx*" under the Knowledge Base root directory containing the following line: "OpenPOP=MailKit".

### [Methods](#Methods)

|  |  |
| --- | --- |
| [Delete](https://wiki.genexus.com/commwiki/wiki?6014) | [Logout](https://wiki.genexus.com/commwiki/wiki?7080) |
| [GetNextUID](https://wiki.genexus.com/commwiki/wiki?7045) | [Receive](https://wiki.genexus.com/commwiki/wiki?6964) |
| [Login](https://wiki.genexus.com/commwiki/wiki?6963) | [Skip](https://wiki.genexus.com/commwiki/wiki?7085) |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [See Also](#See+Also)

[MAPISession Data Type](https://wiki.genexus.com/commwiki/wiki?6935)  
[OutlookSession Data Type](https://wiki.genexus.com/commwiki/wiki?6936)  
[SMTPSession Data Type](https://wiki.genexus.com/commwiki/wiki?6937)

[Error Codes and Messages for POP3Session](https://wiki.genexus.com/commwiki/wiki?6942)  
[Special considerations for SMTPSession or Pop3Session with Google Accounts](https://wiki.genexus.com/commwiki/wiki?50227)


|  |
| --- |
| **Backlinks** |
| [AttachDir Property](https://wiki.genexus.com/commwiki/wiki?6953) | [AuthenticationMethod property (for mails data types)](https://wiki.genexus.com/commwiki/wiki?50349) | [Count property](https://wiki.genexus.com/commwiki/wiki?7023) |
| [Data types list](https://wiki.genexus.com/commwiki/wiki?6779) | [Delete method](https://wiki.genexus.com/commwiki/wiki?6014) | [ErrCode Property](https://wiki.genexus.com/commwiki/wiki?6930) | [ErrDescription Property](https://wiki.genexus.com/commwiki/wiki?6931) |
| [ErrDisplay Property](https://wiki.genexus.com/commwiki/wiki?6929) | [Error Codes and Messages for POP3Session](https://wiki.genexus.com/commwiki/wiki?6942) |
| [GetNextUID method](https://wiki.genexus.com/commwiki/wiki?7045) | [Host Property](https://wiki.genexus.com/commwiki/wiki?6999) | [Login method](https://wiki.genexus.com/commwiki/wiki?6963) | [Logout method](https://wiki.genexus.com/commwiki/wiki?7080) |
| [Mail Secure Property](https://wiki.genexus.com/commwiki/wiki?21181) | [MailMessage data type](https://wiki.genexus.com/commwiki/wiki?6925) | [MAPISession Data Type](https://wiki.genexus.com/commwiki/wiki?6935) | [NewMessages Property](https://wiki.genexus.com/commwiki/wiki?6961) |
| [OutlookSession Data Type](https://wiki.genexus.com/commwiki/wiki?6936) | [Password property](https://wiki.genexus.com/commwiki/wiki?6994) | [Port Property](https://wiki.genexus.com/commwiki/wiki?5019) | [Receive method](https://wiki.genexus.com/commwiki/wiki?6964) |
| [Skip method](https://wiki.genexus.com/commwiki/wiki?7085) | [SMTPSession Data Type](https://wiki.genexus.com/commwiki/wiki?6937) | [Special considerations for SMTPSession or Pop3Session with Google Accounts](https://wiki.genexus.com/commwiki/wiki?50227) | [Timeout property](https://wiki.genexus.com/commwiki/wiki?7042) |
| [UserName Property](https://wiki.genexus.com/commwiki/wiki?7001) |

---
