---
title: "HowTo: Use AddContact method from Contacts external object"
source_id: 15792
source_url: https://wiki.genexus.com/commwiki/wiki?15792
genexus_version: "18"
---

# HowTo: Use AddContact method from Contacts external object

The purpose of this article is to explain how to use the AddContact method offered by the [Contacts external object](https://wiki.genexus.com/commwiki/wiki?31276) for adding a contact through a Native Mobile app.

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

Using the AddContact method you will be able to add a contact through the app to be stored in the device.

The method expects the following parameters:

`[imagen omitida: wiki id 54664]`

**Note**: FirstName and LastName are mandatory. Email and Phone are optional.

In the Work With tab, go to the Section (General) node located under the Detail node:

`[imagen omitida: wiki id 15899]`

Define the following event in the Events tab:

```
Event 'AddToContacts'
     AddressBook.AddContact(PersonName, PersonLastName, PersonEmail, PersonPhone, CompanyName, '' , PersonMessage)
Endevent
```

**Note**: The parameters that are not used must be included in the call of the method anyway.

### [Step 4](#Step+4)

Finally, go to the Layout tab and insert in the Application Bar a button associated with the 'AddToContact' event.

`[imagen omitida: wiki id 54692]`


|  |
| --- |
| **Backlinks** |
| [Contacts external object](https://wiki.genexus.com/commwiki/wiki?31276) |

---
