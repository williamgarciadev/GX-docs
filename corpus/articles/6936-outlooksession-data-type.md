---
title: "OutlookSession Data Type"
source_id: 6936
source_url: https://wiki.genexus.com/commwiki/wiki?6936
genexus_version: "18"
---

# OutlookSession Data Type

Unifies the interaction functions with the sending and reception of messages for the different generated languages.

An important advantage of this implementation regarding the previous ones is that this one allows using more than one connection event to the mail server.

**Deprecated**: Since GeneXus X.

Note: Although this Data Type has been deprecated in GeneXus X, it is still included in newer versions of GeneXus for the only reason of compatibility of code written in previous GeneXus versions. Due to incompatibilities with newer versions of Microsoft Office, instead of using this Data type, [SMTPSession Data Type](https://wiki.genexus.com/commwiki/wiki?6937) or [POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966) should be used to send or receive emails. More information at [SAC 29664](https://www.genexus.com/developers/websac?es,,,29664)

### [Description](#Description)

It allows using a mail session to send and receive messages via Microsoft Outlook.

In order to use this feature the requirement is to have installed Microsoft Outlook 97.

### [Properties](#Properties)

|  |  |
| --- | --- |
| [AttachDir](https://wiki.genexus.com/commwiki/wiki?6953) | [ErrDescription](https://wiki.genexus.com/commwiki/wiki?6931) |
| [Count](https://wiki.genexus.com/commwiki/wiki?7023) | [ErrDisplay](https://wiki.genexus.com/commwiki/wiki?6929) |
| [EditWindow](https://wiki.genexus.com/commwiki/wiki?7030) | [NewMessages](https://wiki.genexus.com/commwiki/wiki?6961) |
| [ErrCode](https://wiki.genexus.com/commwiki/wiki?6930) |  |

### [Methods](#Methods)

|  |  |
| --- | --- |
| [ChangeFolder](https://wiki.genexus.com/commwiki/wiki?6962) | [Receive](https://wiki.genexus.com/commwiki/wiki?6964) |
| [Delete](https://wiki.genexus.com/commwiki/wiki?6014) | [Send](https://wiki.genexus.com/commwiki/wiki?6965) |
| [MarkAsRead](https://wiki.genexus.com/commwiki/wiki?7092) |  |

### [Considerations](#Considerations)

Since Microsoft Outlook 2010 there is no support for [Collaboration Data Objects (CDO)](https://support.microsoft.com/en-us/kb/2028411); it is recommended to use SMTP and POP3 protocols instead.

To use this with .NET generator read [SAC 29664](http://www2.gxtechnical.com/portal/hgxpp001.aspx?15,4,61,O,S,0,,29664).

### [Scope](#Scope)

**Languages:** .NET, Java, Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [See Also](#See+Also)

[MAPISession Data Type](https://wiki.genexus.com/commwiki/wiki?6935)  
[POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966)  
[SMTPSession Data Type](https://wiki.genexus.com/commwiki/wiki?6937)


|  |
| --- |
| **Backlinks** |
| [AttachDir Property](https://wiki.genexus.com/commwiki/wiki?6953) | [ChangeFolder method](https://wiki.genexus.com/commwiki/wiki?6962) | [Count property](https://wiki.genexus.com/commwiki/wiki?7023) |
| [Data types list](https://wiki.genexus.com/commwiki/wiki?6779) | [Delete method](https://wiki.genexus.com/commwiki/wiki?6014) | [EditWindow Property](https://wiki.genexus.com/commwiki/wiki?7030) | [ErrCode Property](https://wiki.genexus.com/commwiki/wiki?6930) |
| [ErrDescription Property](https://wiki.genexus.com/commwiki/wiki?6931) | [ErrDisplay Property](https://wiki.genexus.com/commwiki/wiki?6929) | [Error Codes and Messages for OutlookSession](https://wiki.genexus.com/commwiki/wiki?6941) | [MailMessage data type](https://wiki.genexus.com/commwiki/wiki?6925) |
| [MAPISession Data Type](https://wiki.genexus.com/commwiki/wiki?6935) | [MarksAsRead method](https://wiki.genexus.com/commwiki/wiki?7092) | [NewMessages Property](https://wiki.genexus.com/commwiki/wiki?6961) | [POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966) |
| [Receive method](https://wiki.genexus.com/commwiki/wiki?6964) | [Send method](https://wiki.genexus.com/commwiki/wiki?6965) | [SMTPSession Data Type](https://wiki.genexus.com/commwiki/wiki?6937) |

---
