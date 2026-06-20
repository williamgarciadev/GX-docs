---
title: "HowTo: Use RemoveContact method from Contacts external object"
source_id: 15895
source_url: https://wiki.genexus.com/commwiki/wiki?15895
genexus_version: "18"
---

# HowTo: Use RemoveContact method from Contacts external object

The purpose of this article is to explain how to use the RemoveContact method offered by the [Contacts external object](https://wiki.genexus.com/commwiki/wiki?31276) to delete a contact from a device through an app.

`[imagen omitida: wiki id 54698]`

The following steps guide you on how to use the method.

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

Go to the Section (General) node located under the Detail node:

`[imagen omitida: wiki id 15899]`

In the Events section define the following event:

```
Event 'RemoveContact'
    AddressBook.RemoveContact(CustomerName, CustomerLastName, '', '', '')
Endevent
```

**Note**: Even though some parameters are not used, they have to be included. That's why some parameters are passed as empty values.

### [Step 4](#Step+4)

Finally, go to the Layout tab and insert in the Application Bar a button associated with the 'RemoveContact' event.

`[imagen omitida: wiki id 54692]`


|  |
| --- |
| **Backlinks** |
| [Contacts external object](https://wiki.genexus.com/commwiki/wiki?31276) |

---
