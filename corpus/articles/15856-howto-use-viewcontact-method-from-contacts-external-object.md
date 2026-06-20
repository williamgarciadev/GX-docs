---
title: "HowTo: Use ViewContact method from Contacts external object"
source_id: 15856
source_url: https://wiki.genexus.com/commwiki/wiki?15856
genexus_version: "18"
---

# HowTo: Use ViewContact method from Contacts external object

The purpose of this article is to explain through an example how to use the ViewContact method offered by the  [Contacts external object](https://wiki.genexus.com/commwiki/wiki?31276).

### [Step 1](#Step+1)

Create a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) with the following attributes:

```
Customer
{
  CustomerId*
  CustomerName
  CustomerLastName
}
```

### [Step 2](#Step+2)

Apply the [Work With pattern](https://wiki.genexus.com/commwiki/wiki?15975) to it.

### [Step 3](#Step+3)

Using the ViewContact method you will be able to see in the app the contacts' information stored in the device.

The ViewContact method accepts the following parameters:

`[imagen omitida: wiki id 15859]`

FirstName and LastName are mandatory. Email and Phone are optional.

Go to the Work With tab and click on the Section (General) node located under the Detail node:

`[imagen omitida: wiki id 15899]`

Select the Events tab and define the following event:

```
Event 'ViewInfo'
    AddressBook.ViewContact(CustomerName, CustomerLastName, '', '')
Endevent
```

**Note**: The parameters that are not used must be included in the call of the method anyway.

Finally, go to the Layout tab and insert in the Application Bar a button associated with the 'ViewInfo' event:

`[imagen omitida: wiki id 54692]`


|  |
| --- |
| **Backlinks** |
| [Contacts external object](https://wiki.genexus.com/commwiki/wiki?31276) |

---
