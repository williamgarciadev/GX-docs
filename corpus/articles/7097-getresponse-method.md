---
title: "GetResponse method"
source_id: 7097
source_url: https://wiki.genexus.com/commwiki/wiki?7097
genexus_version: "18"
---

# GetResponse method

**Deprecated**: Since [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?28265,,).

Returns the HTML code that is returned by the Web object specified in the [Object property](https://wiki.genexus.com/commwiki/wiki?7011) of the variable based on the WebWrapper data type.

### [Syntax](#Syntax)

**&***VarBasedOnWebWrapper***.GetResponse()**

### [Scope](#Scope)

**Extended Data Types:**[WebWrapper](https://wiki.genexus.com/commwiki/wiki?6624)      
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3)

### [Description](#Description)

The GetResponse method must always be assigned to the HTMLText property of a variable based on the MailMessage data type as shown in the following code:

```
&Wrap.BaseURL = “http://myserver/mysystem/”                //&Wrap: WebWrapper data type
&Wrap.Object = Create(Hnotify, &CustomerId)
&MailMsg.To.New(&CustomerName, &CustomerMail)              //&MailMsg: MailMessage data type
&MailMsg.HTMLText = &Wrap.GetResponse()
&Oulook.Send(&MailMsg)                                     //&Outlook: OutlookSession data type
```

### [See Also](#See+Also)

[WebWrapper](https://wiki.genexus.com/commwiki/wiki?6624)  
[HTMLText](https://wiki.genexus.com/commwiki/wiki?7043)


|  |
| --- |
| **Backlinks** |
| [GeneXus deprecated functions, methods, and rules](https://wiki.genexus.com/commwiki/wiki?6620) | [WebWrapper data type](https://wiki.genexus.com/commwiki/wiki?6624) |

---
