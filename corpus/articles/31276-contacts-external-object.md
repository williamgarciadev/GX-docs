---
title: "Contacts External Object"
source_id: 31276
source_url: https://wiki.genexus.com/commwiki/wiki?31276
genexus_version: "18"
---

# Contacts External Object

The Contacts [External Object](https://wiki.genexus.com/commwiki/wiki?5669) enables you to programmatically manage the contacts on the device.

`[imagen omitida: wiki id 58847]`

You can find the Contacts External Object in the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210) within the SD module, which in turn is located within the GeneXus module. That is to say, it is part of the [Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288).

## [Properties](#Properties)

It does not have any.

## [Methods](#Methods)

### [AddContact method](#AddContact+method)

Adds a contact. Returns True if the operation was successful or the contact was already added. Returns False if any failure occurs and/or the user cancels the execution. If the returned value is not used, the event execution is canceled.

See [HowTo: Use AddContact method from Contacts external object](https://wiki.genexus.com/commwiki/wiki?15792).

|  |  |
| --- | --- |
| **Return value** | Boolean |
| **Parameters** | FirstName:[Character(40)](https://wiki.genexus.com/commwiki/wiki?6777), LastName:[Character(40)](https://wiki.genexus.com/commwiki/wiki?6777) [, Email:[Email](https://wiki.genexus.com/commwiki/wiki?14650) ] [, Phone:[Phone](https://wiki.genexus.com/commwiki/wiki?14639) ]  [, CompanyName: [Character(40)](https://wiki.genexus.com/commwiki/wiki?6777) ] [, Photo:[URL](https://wiki.genexus.com/commwiki/wiki?15668) ] [, Message:[Character(80)](https://wiki.genexus.com/commwiki/wiki?6777)] |

### [RemoveContact method](#RemoveContact+method)

Removes a contact. Returns True if the contact was removed successfully. Returns False if any failure such as the following occurs: the contact to be removed is not present in the catalog and/or the user cancels the execution. If the returned value is not used, the event execution is canceled.

See [HowTo: Use RemoveContact method from Contacts external object](https://wiki.genexus.com/commwiki/wiki?15895).

|  |  |
| --- | --- |
| **Return value** | Boolean |
| **Parameters** | FirstName:Character(40), LastName:Character(40) [, Email:Email] [, Phone:Phone]  [, Message:Character(80)] |

### [ViewContact method](#ViewContact+method)

Views the contact information stored in the device.

See [HowTo: Use ViewContact method from Contacts external object](https://wiki.genexus.com/commwiki/wiki?15856).

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | FirstName:Character(40), LastName:Character(40) [, Email:Email] [, Phone:Phone] |

### [GetAllContacts method](#GetAllContacts+method)

Retrieves all the contacts' information from the device with their details.

|  |  |
| --- | --- |
| **Return value** | Collection( ContactInfo ) |
| **Parameters** | None |

### [PickContact method](#PickContact+method)

Opens the native platform's contact selection screen, allowing the end user to select a contact from the list available on the device. Execution is synchronous, pausing the program until the user selects a contact and closes the interface, allowing the execution to continue.

|  |  |
| --- | --- |
| **Return value** | ContactInfo |
| **Parameters** | None |

### [PickContacts method](#PickContacts+method)

Opens the native platform's contact selection screen, allowing the end user to select multiple contacts from the list available on the device. Execution is synchronous, pausing the program until the user selects a contact and closes the interface, allowing the execution to continue. On Android, because the native API only allows selecting one, this method will return at most a single contact.

|  |  |
| --- | --- |
| **Return value** | Collection(ContactInfo) |
| **Parameters** | None |

## [Events](#Events)

It does not have any.

## [Structured Data Types](#Structured+Data+Types)

### [ContactInfo](#ContactInfo)

Encapsulates single contact information stored in the device.

* DisplayName:Character(80)  
  Contains the name displayed on the device.
* FirstName:Character(40)  
  The contact's first name.
* LastName:Character(40)  
  The contact's last name.
* Email:Email  
  The contact's email.
* Phone:Phone  
  The contact's phone number.
* CompanyName:Character(40)  
  The contact's company name.
* Photo:[Image](https://wiki.genexus.com/commwiki/wiki?15204)  
  The contact's photo.
* Notes:Character(200)  
  Notes associated with the contact.

## [Samples](#Samples)

```
Event 'AddToContacts'
    &IsOK = Contacts.AddContact(PersonName,PersonLastName,PersonEmail,PersonPhone,CompanyName,PersonPhoto,PersonMessage)
Endevent
```

```
Event 'RemoveContact'
    &IsOK = Contacts.RemoveContact(PersonName,PersonLastName,PersonEmail,PersonPhone,PersonMessage)
Endevent
```

```
Event 'ViewContact'
    Contacts.ViewContact(PersonName,PersonLastName,PersonEmail,PersonPhone)
Endevent
```

```
Event 'ViewContactsList'
    &AddressBookContacts = Contacts.GetAllContacts()
Endevent
```

## [Scope](#Scope)

**Generators**: [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

## [Notes](#Notes)

* As of [GeneXus 16 upgrade 8](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?44913,,), the "Message" parameter will be ignored for devices with iOS 13.
* Since [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?45901,,), to access the notes stored in contacts on devices with iOS 13 or later, you need to configure the [Access Contacts Notes property](https://wiki.genexus.com/commwiki/wiki?46110).
* RemoveContact and ViewContact methods are available for Android as of [GeneXus 17](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46066,,).
* **PickContact** and **PickContacts** methods are available since [GeneXus 17 upgrade 1](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46852,,).


|  |
| --- |
| **Backlinks** |
| [Access Contacts Notes property](https://wiki.genexus.com/commwiki/wiki?46110) | [GeneXus Core module](https://wiki.genexus.com/commwiki/wiki?31268) | [GeneXus Core module (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54413) |
| [HowTo: Use AddContact method from Contacts external object](https://wiki.genexus.com/commwiki/wiki?15792) | [HowTo: Use RemoveContact method from Contacts external object](https://wiki.genexus.com/commwiki/wiki?15895) | [HowTo: Use ViewContact method from Contacts external object](https://wiki.genexus.com/commwiki/wiki?15856) | [Purpose Strings properties group](https://wiki.genexus.com/commwiki/wiki?32755) |
| [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) | [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) |

---
