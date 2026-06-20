---
title: "Logically Deleted Attribute property"
source_id: 37091
source_url: https://wiki.genexus.com/commwiki/wiki?37091
genexus_version: "18"
---

# Logically Deleted Attribute property

Indicates the boolean attribute that contains the information about the deletion of the record.
If the value of this attribute is True, the record is considered as deleted.

### [Description](#Description)

Deletion of rows from a database table usually is differentiated into two alternatives:

* **Physical delete**  
  A row is permanently deleted from the database (a.k.a. *Hard delete*). In GeneXus, this is made by combining [For Each command](https://wiki.genexus.com/commwiki/wiki?24744) and [Delete command](https://wiki.genexus.com/commwiki/wiki?6828), or by using [Business Component Delete method](https://wiki.genexus.com/commwiki/wiki?23238).
* **Logical delete**  
  In contrast to physical delete, the row will never be dropped from the database (a.k.a. *Soft delete*). Instead, the developer includes a special boolean attribute on the concerned table (e.g. IsDeleted) and marks a row as deleted (true) or not (false) -- it can be seen as an update.

When using synchronization by timestamp for interchanging data between server and device, a physical deletion on the server-side is counterproductive because such deleted rows will never be dropped from the device's offline database in subsequent synchronizations. For clarifying this concept, refer to Sample section.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [Samples](#Samples)

Suppose we have a Chat transaction object defined as follows.

`[imagen omitida: wiki id 37099]`

As you have noticed, we have set the following properties (both are required for using synchronization by timestamp).

* [Logically Deleted Attribute property](https://wiki.genexus.com/commwiki/wiki?37091) = ChatIsDeleted
* [Last Modified Date Time Attribute property](https://wiki.genexus.com/commwiki/wiki?37092) = ChatTimestamp

Suppose there are two friends communicating with our chat system and they already have the following rows synchronized on their devices.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *friend1* | *friend2* | *10/12/17 12:00:01 AM* | False | Happy birthday! |
| *friend2* | *friend1* | *10/12/17 12:00:02 AM* | False | Thks =) See you tomorrow? |
| *friend1* | *friend2* | *10/13/17 03:57:03 AM* | False | Hey dude! U still in the dance club? Can't find u. Call me. |

Some minutes later, *friend1* finally founds *friend2* and decides to delete the last message sent. Typically the developer would create a Procedure object with the following code.

```
parm(in:&From,in:&To,in:&DateTime);
```

```
For each Chat
Where ChatUsernameFrom = &From      // instanciated with 'friend1'
      and ChatUsernameTo = &To      // instanciated with 'friend2'
      and ChatTimestamp = &DateTime // instanciated with 10/13/17 03:57:03 AM
   delete
EndFor
```

Note that the deletion is made physically. Then, due synchronization by timestamp mechanism, the *friend2* device in a subsequent synchronization will remain the original set of rows (without deleting the third one), but the server and *friend1* remain only the first two. The reason behind this behavior is that the server does not know which data has every device, it only sends data by considering [Last Modified attribute](https://wiki.genexus.com/commwiki/wiki?37092). This problem is the **full responsibility of the developer** who should fix it by the developer by replacing the deletion code in the Procedure as follows:

```
For each Chat
Where ChatUsernameFrom = &From      // instanciated with 'friend1
      and ChatUsernameTo = &To      // instanciated with 'friend2'
      and ChatTimestamp = &DateTime // instanciated with 10/13/17 03:57:03 AM
  ChatIsDeleted = True   // Logical delete
  ChatTimestamp = Now()  // Table update due deletion (value 10/13/17 04:15:17 AM)
EndFor
```

In such case, there is no physical deletion in the server-side, i.e. the database state will be:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *friend1* | *friend2* | *10/12/17 12:00:01 AM* | False | Happy birthday! |
| *friend2* | *friend1* | *10/12/17 12:00:02 AM* | False | Thks =) See you tomorrow? |
| *friend1* | *friend2* | ***10/13/17 04:15:17 AM*** | **True** | Hey dude! U still in the dance club? I can't find u. Call me. |

Consequently, due to timestamp algorithm, both offline databases (for *friend1* and *friend2*) won't have the deleted message after a new synchronization.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *friend1* | *friend2* | *10/12/17 12:00:01 AM* | False | Happy birthday! |
| *friend2* | *friend1* | *10/12/17 12:00:02 AM* | False | Thks =) See you tomorrow? |

### [Availability](#Availability)

This property is available since [GeneXus 15 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?36778,,).

### [Scope](#Scope)

**Objects:** Transaction  
**Platforms:** Smart Devices(Android, IOS)


|  |
| --- |
| **Backlinks** |
| [Data Receive Granularity property](https://wiki.genexus.com/commwiki/wiki?23541) | [Last Modified Date Time Attribute property](https://wiki.genexus.com/commwiki/wiki?37092) | [Logically Deleted Attribute property](https://wiki.genexus.com/commwiki/wiki?37091) |
| [Offline Native Mobile synchronization granularity alternatives](https://wiki.genexus.com/commwiki/wiki?37109) | [KB:Sales](https://wiki.genexus.com/commwiki/wiki?23672) | [Specification Codes from spc0150 onwards](https://wiki.genexus.com/commwiki/wiki?6774) |

---
