---
title: "Offline Database Object events"
source_id: 23566
source_url: https://wiki.genexus.com/commwiki/wiki?23566
genexus_version: "18"
---

# Offline Database Object events

The Offline Database Object only allows the **Start event**. It is intended for variables initialization and other processing that could be needed before table synchronization happens.  That is why it is executed before the conditions apply in the synchronization.

### [Syntax](#Syntax)

**Event Start**  
*Event\_code*  
**EndEvent**  
  
**Where:**  
  
*Event\_code*  
   Code associated with the event.

### [Sample](#Sample)

```
Event Start
    &DeviceID = ClientInformation.Id
    For Each
    where DeviceID = &DeviceID
        &SalesAreaID = SalesAreaID
    EndFor
EndEvent
```

And then this variables can be used in the Conditions tabs like shown in the following code stub:

```
SalesAreaID = &SalesAreaID;
CustomerStatus = CustomerStatus.Active;
```

### [Availability](#Availability)

This feature is available since [GeneXus Tilo Beta 2](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?23074,,).

### [See Also](#See+Also)

[Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509)  
[Offline Database Object conditions](https://wiki.genexus.com/commwiki/wiki?23570)


|  |
| --- |
| **Backlinks** |
| [Category:Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509) | [Offline Database Object conditions](https://wiki.genexus.com/commwiki/wiki?23570) | [Offline Database Object Navigation Report](https://wiki.genexus.com/commwiki/wiki?23568) |
| [Table of contents:Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22228) | [KB:Sales](https://wiki.genexus.com/commwiki/wiki?23672) |

---
