---
title: "HowTo: Use the Cancel Method from Actions in Native Mobile applications"
source_id: 18363
source_url: https://wiki.genexus.com/commwiki/wiki?18363
genexus_version: "18"
---

# HowTo: Use the Cancel Method from Actions in Native Mobile applications

When inserting records, many times you need to check some restrictions before saving it. For example, calling a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829), a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293), return to the [Work With List Node](https://wiki.genexus.com/commwiki/wiki?15984), etc. So, using the cancel action allows you to add more behavior to your application, when complex constraints determine whether a record should be saved or not.

The Cancel method can also be used on any Native Mobile application. The behavior outside the insertion of a record on a [Work With](https://wiki.genexus.com/commwiki/wiki?15974) should be: Cancel the execution of the Composite block, and return to the caller screen.

In this article, you will see one simple example of the previously mentioned. You are going to be able to create your own simple Cancel button.

Use the following Transaction with the [Work With pattern applied](https://wiki.genexus.com/commwiki/wiki?15975) as used on [Save method](https://wiki.genexus.com/commwiki/wiki?16015):

```
Customer
{
  CustomerId*
  CustomerName
  CustomerLastName
  CustomerBirthDate
  CustomerMessage
}
```

As seen on the Actions external object, the Cancel method doesn’t expect any parameter:

`[imagen omitida: wiki id 55620]`

The behavior you want this example to have is to cancel a Transaction insertion when the button you created is pressed.

First, add the new Cancel button to the [Application Bar](https://wiki.genexus.com/commwiki/wiki?19486) on the Edit mode in Section General of the Work With pattern in the Customer Transaction object. Then, set the Priority property = High.

`[imagen omitida: wiki id 55621]`

By double-clicking over the new Action (button MyCancel) it will take you to the event associated:

`[imagen omitida: wiki id 55622]`

```
Event 'MyCancel'
    Actions.Cancel()
EndEvent
```

### [Sample](#Sample)

#### [Android](#Android)

`[imagen omitida: wiki id 18391]`


|  |
| --- |
| **Backlinks** |
| [Actions external object](https://wiki.genexus.com/commwiki/wiki?31350) |

---
