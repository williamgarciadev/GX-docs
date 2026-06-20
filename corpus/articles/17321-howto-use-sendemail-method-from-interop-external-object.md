---
title: "HowTo: Use SendEmail method from Interop external object"
source_id: 17321
source_url: https://wiki.genexus.com/commwiki/wiki?17321
genexus_version: "18"
---

# HowTo: Use SendEmail method from Interop external object

The SendEmail method offered by the [Interop external object](https://wiki.genexus.com/commwiki/wiki?23734) provides a way to send an email from your application.

When this method is executed, it opens the native email application of the device with a new email ready to be sent.

`[imagen omitida: wiki id 54734]`

The method accepts three parameters:

* **To:**Recipient of the email. Based on the [Email domain](https://wiki.genexus.com/commwiki/wiki?14650).
* **Subject:** Subject of the email.
* **Message:** Content of the email to send.

The following steps guide you on how to use the PlaceCall method.

### [Step 1](#Step+1+)

Create a new [Panel object](https://wiki.genexus.com/commwiki/wiki?24829):

### [Step 2](#Step+2)

Define:

* A variable based on the [Email domain](https://wiki.genexus.com/commwiki/wiki?14650) to enter the recipient of the email (For example, &To).
* Variables based on VarChar(200): one for the subject and another one for the message (For example, &Subject and &Message).

### [Step 3](#Step+3)

Insert the variables in the Panel Layout.

### [Step 4](#Step+4)

Insert a button in the Panel Layout. Double-click on the button and define the following code associated with the event:

```
Event 'Email'
    Interop.SendEmail(&To,&Subject,&Message)
EndEvent
```

Done! The entry Panel will accept an email address and a message. When the button is tapped, the native email application of the device will open with the new email ready to be sent.

`[imagen omitida: wiki id 17326]`

`[imagen omitida: wiki id 17327]`


|  |
| --- |
| **Backlinks** |
| [HowTo: Use SendEmailAdvanced method from Interop external object in Native Mobile apps](https://wiki.genexus.com/commwiki/wiki?18193) | [Interop external object](https://wiki.genexus.com/commwiki/wiki?23734) | [Interop external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55183) |

---
