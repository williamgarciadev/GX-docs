---
title: "HowTo: Use SendMessage method from Interop external object"
source_id: 15528
source_url: https://wiki.genexus.com/commwiki/wiki?15528
genexus_version: "18"
---

# HowTo: Use SendMessage method from Interop external object

The SendMessage method offered by the [Interop external object](https://wiki.genexus.com/commwiki/wiki?23734) allows sending general messages using applications installed on the end user's device.

`[imagen omitida: wiki id 54694]`

Two parameters can be set:

* **Message:**The content of the message.
* **To:**The recipient of the general message (e.g. by phone number, email, Facebook account, Twitter username, etc.).

The method will display every application installed on the end user's device for sending the message without considering the semantics of the *To* parameter (phone, email, etc.). The end user should select which app should resolve the request; otherwise, the *To* parameter will be ignored. For instance, if the *To* parameter is set under the [Phone domain](https://wiki.genexus.com/commwiki/wiki?14639), and the end user tries to send the message by email, only the Message parameter will be used.

To use the method, follow the steps below:

### [Step 1](#Step+1)

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)s:

```
Customer
{
  CustomerId*
  CustomerName
  CustomerPhoto
  CustomerPhone
  CustomerEmail
  CustomerAddress
  CompanyId
  CompanyName
}
```

```
Company
{
  CompanyId*
  CompanyName
}
```

### [Step 2](#Step+2)

Apply the [Work With pattern](https://wiki.genexus.com/commwiki/wiki?15975) to the Customer Transaction.

### Step 3

Go to the Section (General) node located under the Detail node. From the Layout tab, right-click on the Application Bar and insert a button as follows:  
  
`[imagen omitida: wiki id 54705]`

### [Step 4](#Step+4)

Add the following behavior to the Message event:

```
Event 'Message'
    Interop.SendMessage("",CustomerPhone)
EndEvent
```

This action will try to send an empty message to a specific customer (in this case, using the phone number). If the end user selects the SMS messaging app, it will directly be opened to send the message to the target user. However, if the end user selects the Email app, it will only open the email application because the message is empty and the phone number is discarded. If you only want to send SMS, use the [SendSMS method](https://wiki.genexus.com/commwiki/wiki?17310).

At runtime, it will behave as follows:  
  
`[imagen omitida: wiki id 37803]`


|  |
| --- |
| **Backlinks** |
| [Calling objects from Menu Events](https://wiki.genexus.com/commwiki/wiki?17392) | [Composite examples](https://wiki.genexus.com/commwiki/wiki?15551) | [Interop external object](https://wiki.genexus.com/commwiki/wiki?23734) |
| [Interop external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55183) |

---
