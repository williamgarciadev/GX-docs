---
title: "MAPISession Data Type"
source_id: 6935
source_url: https://wiki.genexus.com/commwiki/wiki?6935
genexus_version: "18"
---

# MAPISession Data Type

Unifies the interaction functions with the sending and reception of messages for the different languages generated.

An important advantage of this implementation as compared to the previous ones is that this one allows you to use more than one connection event to the mail server.

### [Description](#Description)

It allows you to send/receive messages via Microsoft's MAPI (Mail Application Program Interface).

Using the latter modality is not recommended unless you want to use the Microsoft Exchange Server's services and Microsoft Outlook is not available.

The requirements for using this feature are:

* Microsoft Outlook 97 or later version or Microsoft's Exchange Client
* Collaboration Data Objects (CDO) 1.2 or later version

The CDOs 1.2 include the following products:

* MS Outlook 98 and MS Outlook 2000 (1.21 Version)
* MS Exchange 5.5 Server (Version 1.2 or Version 1.21 in SP1 or higher)

### [Properties](#Properties)

|  |  |
| --- | --- |
| [AttachDir](https://wiki.genexus.com/commwiki/wiki?6953) | [ErrDescription](https://wiki.genexus.com/commwiki/wiki?6931) |
| [Count](https://wiki.genexus.com/commwiki/wiki?7023) | [ErrDisplay](https://wiki.genexus.com/commwiki/wiki?6929) |
| [EditWindow](https://wiki.genexus.com/commwiki/wiki?7030) | [NewMessages](https://wiki.genexus.com/commwiki/wiki?6961) |
| [ErrCode](https://wiki.genexus.com/commwiki/wiki?6930) | [Profile](https://wiki.genexus.com/commwiki/wiki?7025) |

### [Methods](#Methods)

|  |  |
| --- | --- |
| [ChangeFolder](https://wiki.genexus.com/commwiki/wiki?6962) | [MarkAsRead](https://wiki.genexus.com/commwiki/wiki?7092) |
| [Delete](https://wiki.genexus.com/commwiki/wiki?6014) | [Receive](https://wiki.genexus.com/commwiki/wiki?6964) |
| [Login](https://wiki.genexus.com/commwiki/wiki?6963) | [Send](https://wiki.genexus.com/commwiki/wiki?6965) |
| [Logout](https://wiki.genexus.com/commwiki/wiki?7080) |  |

### [Scope](#Scope)

**Languages:** .NET, Java, Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [See Also](#See+Also)

[OutlookSession Data Type](https://wiki.genexus.com/commwiki/wiki?6936)  
[POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966)  
[SMTPSession Data Type](https://wiki.genexus.com/commwiki/wiki?6937)


|  |
| --- |
| **Backlinks** |
| [AttachDir Property](https://wiki.genexus.com/commwiki/wiki?6953) | [ChangeFolder method](https://wiki.genexus.com/commwiki/wiki?6962) | [Count property](https://wiki.genexus.com/commwiki/wiki?7023) |
| [Data types list](https://wiki.genexus.com/commwiki/wiki?6779) | [Delete method](https://wiki.genexus.com/commwiki/wiki?6014) | [EditWindow Property](https://wiki.genexus.com/commwiki/wiki?7030) | [ErrCode Property](https://wiki.genexus.com/commwiki/wiki?6930) |
| [ErrDescription Property](https://wiki.genexus.com/commwiki/wiki?6931) | [ErrDisplay Property](https://wiki.genexus.com/commwiki/wiki?6929) | [Error Codes and Messages for MAPISession](https://wiki.genexus.com/commwiki/wiki?6940) | [Login method](https://wiki.genexus.com/commwiki/wiki?6963) |
| [Logout method](https://wiki.genexus.com/commwiki/wiki?7080) | [MailMessage data type](https://wiki.genexus.com/commwiki/wiki?6925) | [MarksAsRead method](https://wiki.genexus.com/commwiki/wiki?7092) | [NewMessages Property](https://wiki.genexus.com/commwiki/wiki?6961) |
| [OutlookSession Data Type](https://wiki.genexus.com/commwiki/wiki?6936) | [POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966) | [Profile Property](https://wiki.genexus.com/commwiki/wiki?7025) | [Receive method](https://wiki.genexus.com/commwiki/wiki?6964) |
| [Send method](https://wiki.genexus.com/commwiki/wiki?6965) | [SMTPSession Data Type](https://wiki.genexus.com/commwiki/wiki?6937) |

---
