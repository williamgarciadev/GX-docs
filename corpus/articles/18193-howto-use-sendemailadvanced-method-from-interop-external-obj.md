---
title: "HowTo: Use SendEmailAdvanced method from Interop external object in Native Mobile apps"
source_id: 18193
source_url: https://wiki.genexus.com/commwiki/wiki?18193
genexus_version: "18"
---

# HowTo: Use SendEmailAdvanced method from Interop external object in Native Mobile apps

The [Interop external object](https://wiki.genexus.com/commwiki/wiki?23734) provides several methods to interact with the device in which the app is being executed.

The SendEmailAdvanced method enables you to open an Email native application and fill the message fields with values taken from the parameters.

`[imagen omitida: wiki id 54665]`

There are two SendEmailAdvanced methods with the same name. The difference between them is the number of parameters needed. Another method to achieve the same objective but with fewer parameters is the [SendEmail method](https://wiki.genexus.com/commwiki/wiki?17321).

The following steps guide you on how to use the SendEmailAdvanced method.

### [Step 1](#Step+1)

Create a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) with the following variables:

`[imagen omitida: wiki id 18194]`

**Note**: In the SendEmailAdvanced method, as well as in the SendEmail method, the size of the [VarChar data type](https://wiki.genexus.com/commwiki/wiki?6778) parameters passed to it doesn't matter. Even though it asks for a VarChar(200), it could receive a message of any size, including bigger than 200.

### [Step 2](#Step+2)

Add the variables to the Layout:

`[imagen omitida: wiki id 18196]`

### [Step 3](#Step+3)

Right-click on the Application Bar and add a button...

`[imagen omitida: wiki id 18197]`

...with the 'Send Email' event associated with it:

```
Event 'Send EMail'
    Interop.SendEmailAdvanced(&to,&Cc,&Bcc,&Subject,&Message)
EndEvent
```

### [Step 4](#Step+4)

Now all that's left is to press F5. By scanning the QR code or using an emulator, you will see the results:

`[imagen omitida: wiki id 18201]`

`[imagen omitida: wiki id 18202]`

**Note**: Since [GeneXus 17 upgrade 4](https://wiki.genexus.com/commwiki/wiki?47936,,), it is possible to attach files to an email in
[Android](https://wiki.genexus.com/commwiki/wiki?14453) and
[Apple](https://wiki.genexus.com/commwiki/wiki?14917) generators.


|  |
| --- |
| **Backlinks** |
| [Interop external object](https://wiki.genexus.com/commwiki/wiki?23734) | [Interop external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55183) | [Key Color](https://wiki.genexus.com/commwiki/wiki?23130) |

---
