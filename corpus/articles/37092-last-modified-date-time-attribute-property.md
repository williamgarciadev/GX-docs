---
title: "Last Modified Date Time Attribute property"
source_id: 37092
source_url: https://wiki.genexus.com/commwiki/wiki?37092
genexus_version: "18"
---

# Last Modified Date Time Attribute property

Indicates the DateTime-based attribute that contains information about when the record was last modified.

### [Scope](#Scope)

**Objects:** Transaction  
**Platforms:** Smart Devices(Android, IOS)

### [Description](#Description)

This attribute will be used as a reference for the timestamp algorithm to determine which rows must be synchronized from the server to the device. In other words, the device will synchronize those rows whose last modified date time is later than the last synchronization timestamp.

In the next synchronization, the server uses the timestamp sent by the device to compare with the value in the Last Modified Date Time Attribute. All rows modified or added after the last synchronization are considered.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [Samples](#Samples)

Suppose we have a Chat transaction object defined as follows:

`[imagen omitida: wiki id 37099]`

As you can see, we have set the following properties (both are required for using synchronization by timestamp).

* [Logically Deleted Attribute property](https://wiki.genexus.com/commwiki/wiki?37091) = ChatIsDeleted
* [Last Modified Date Time Attribute property](https://wiki.genexus.com/commwiki/wiki?37092) = ChatTimestamp

Also, suppose there are two friends communicating through our chat system and they already have the following rows synchronized on their devices.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *friend1* | *friend2* | *10/12/17 12:00:01 AM* | False | Happy birthday! |
| *friend2* | *friend1* | *10/12/17 12:00:02 AM* | False | Thks =) See you tomorrow at the dance club? |
| *friend1* | *friend2* | *10/13/17 12:05:47 AM* | False | Mom ¬¬ I'm fine. Write u later. Bye |

Minutes later, *friend1* realizes he/she has made a mistake sending a message to *friend2* instead of *Mom*. Luckily, our chat system allows the end user to change the content of sent messages, and *friend1* decides to change the text to "*Hey dude! I'm at the dance club. Where r u?*"

Typically, the developer implements this functionality by using the [New command](https://wiki.genexus.com/commwiki/wiki?6714) (not recommended) or combining [Business Component Load method](https://wiki.genexus.com/commwiki/wiki?23211) with [Commit command](https://wiki.genexus.com/commwiki/wiki?7964) in a Procedure as follows.

```
parm(in:&From, in:&To, &DateTime, in:&Text);

&Chat.Load(&From,&To,&DateTime)
&Chat.ChatMessage = &Text // instantiated with 'Hey dude! I'm at the dance club. Where r u?"'
&Chat.Save()
commit
```

The developer expects that this new row on the Chat table will reflect the change automatically on the target device after the insertion. However, when synchronization by timestamp is used, since the last message is already synchronized on the friend2 device, the updated row will never be sent (there is no hash comparison). Therefore, the appropriate mechanism for updating (or inserting) data **must be implemented by the developer**. In this case, the Procedure shown above should be changed for the following code.

```
&Chat.Load(&From,&To,&DateTime) 
&Chat.ChatMessage = &Text   // instantiated with 'Hey dude! I'm at the dance club. Where r u?"'
&Chat.ChatTimestamp = now() // Last update modified (value 10/13/17 12:06:17 AM)
&Chat.Save() 
commit
```

Once the row has been updated by the developer, both devices will have the following records on its offline database (convenient for *friend1*).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *friend1* | *friend2* | *10/12/17 12:00:01 AM* | False | Happy birthday! |
| *friend2* | *friend1* | *10/12/17 12:00:02 AM* | False | Thks =) See you tomorrow at the dance club? |
| *friend1* | *friend2* | ***10/13/17 12:06:17 AM*** | False | **Hey dude! I'm at the dance club. Where r u?** |

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a Rebuild All.

### [Availability](#Availability)

This property is available since [GeneXus 15 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?36778,,).

### [See Also](#See+Also)

* [Logically Deleted Attribute property](https://wiki.genexus.com/commwiki/wiki?37091)
* [Data Receive Granularity property](https://wiki.genexus.com/commwiki/wiki?23541)


|  |
| --- |
| **Backlinks** |
| [Data Receive Granularity property](https://wiki.genexus.com/commwiki/wiki?23541) | [Last Modified Date Time Attribute property](https://wiki.genexus.com/commwiki/wiki?37092) | [Logically Deleted Attribute property](https://wiki.genexus.com/commwiki/wiki?37091) |
| [Offline Native Mobile synchronization granularity alternatives](https://wiki.genexus.com/commwiki/wiki?37109) | [KB:Sales](https://wiki.genexus.com/commwiki/wiki?23672) | [Specification Codes from spc0150 onwards](https://wiki.genexus.com/commwiki/wiki?6774) |

---
