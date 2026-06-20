---
title: "WebWrapper data type"
source_id: 6624
source_url: https://wiki.genexus.com/commwiki/wiki?6624
genexus_version: "18"
---

# WebWrapper data type

**Deprecated**: Since [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?28265,,).

Although this Data Type has been deprecated in GeneXus 15, it is still included in newer versions of GeneXus for the only reason of compatibility of code written in previous GeneXus versions, where it may work for very specific and simple Web Panels for very specific email clients. The privacy and security concerns and anti-spam policies of email clients make necessary the use of very specific HTML in emails. So, to send emails with HTML Text you may need to use specific services for that. More information at [SAC 48351](https://www.genexus.com/es/developers/websac?data=48351;;)


WebWrapper is a GeneXus data type that allows to encapsulate Web objects execution (the generated HTML code), and process it as desired. In particular, you can send a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) via e-mail using this feature.

One way of sending a Web Panel via e-mail from a GeneXus object is by defining a WebWrapper type variable.

The main idea is to capture the contents of the Web Panel (its HTML code) and send it via e-mail. Thus, it must be noted that the mail client receiving the e-mail must have the capacity to interpret the HTML language.

### [Properties](#Properties)

|  |
| --- |
| [BaseUrl property](https://wiki.genexus.com/commwiki/wiki?7008) |
| [Object property](https://wiki.genexus.com/commwiki/wiki?7011) |

### [Methods](#Methods)

|  |
| --- |
| [GetResponse method](https://wiki.genexus.com/commwiki/wiki?7097) |

Any event produced in the Web Panel making a post to the server (e.g.: clicking on a button, releasing a procedure, etc.) will cause the Web Panel to be opened in the browser, in the address specified in the  [BaseUrl property](https://wiki.genexus.com/commwiki/wiki?7008).

### [Images in Web Panel sent via e-mail](#Images+in+Web+Panel+sent+via+e-mail)

There are two ways of including images in the web wrapper:

* Including the images in the Web Panel as an absolute URL. The disadvantage of this option is that the user must be online the moment he is reading the mail. By adding the image as external, you can specify an absolute reference to it. See   
  [Image object](https://wiki.genexus.com/commwiki/wiki?23387)  
  .
* Including relative images in the Web Panel and sending them as an attachment to the e-mail.  
  In this case, the image route must not include directories (i.e. /imagines/logo.jpg); it only has to make a direct reference to it  (i.e. logo.jpg).

### [Example](#Example)

```
Event SendMail
    &DirTo.Address = 'jhon@yahoo.com'    
    &DirTo.Name = 'Jhon Smith'
    &mailmsg.To.Clear()
    &mailmsg.To.Add(&dirto)
    &mailmsg.Subject = 'GeneXus News'
    &SMTPSession.Host = &host
    &Sender.Address = 'GeneXus'
    &Sender.Name = 'GeneXus'
    &SMTPSession.Sender = &Sender
    &RetCode = &SMTPSession.Login()
    &Wrap.Object = Create(SearchStudents)
    &infoContent = &Wrap.GetResponse()
    &MailMsg.HTMLText = &infoContent
    &SMTPSession.Send(&MailMsg)
    &smtpsession.Logout() 
EndEvent  // SendMail
```

---

|  |
| --- |
| **Backlinks** |
| [BaseUrl property](https://wiki.genexus.com/commwiki/wiki?7008) | [Data types list](https://wiki.genexus.com/commwiki/wiki?6779) |
| [GetResponse method](https://wiki.genexus.com/commwiki/wiki?7097) |

---
