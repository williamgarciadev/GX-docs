---
title: "HowTo: Use Calendar external object in Native Mobile applications"
source_id: 31287
source_url: https://wiki.genexus.com/commwiki/wiki?31287
genexus_version: "18"
---

# HowTo: Use Calendar external object in Native Mobile applications

You can incorporate behavior into your Native Mobile Applications by adding Actions that offer different ways to interact with the devices.

This document explains how to schedule a date in the Calendar from your application.

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators:** | [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917) |

### [Steps](#Steps)

1. Consider the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)s:

```
Customer
{
    CustomerId*
    CustomerFirstName
    CustomerLastName
    CustomerBirthDate
    CustomerPhone
    CustomerEmail
    CustomerAddress

}

Date
{
    DateId*
    DateDescription
    DateStartDate
    DateEndDate
    DateStartTime
    DateEndTime
    DatePlace
    CustomerId
    CustomerFirstName
    CustomerLastName
}
```

2. Open the [Calendar external object](https://wiki.genexus.com/commwiki/wiki?39346) and pay attention to the Schedule method:

`[imagen omitida: wiki id 57489]`

It has six configurable parameters.

3. Apply the [Work With pattern](https://wiki.genexus.com/commwiki/wiki?15974) to the Customer Transaction:

`[imagen omitida: wiki id 57256]`

4. Select the Section(General) node. The next step consists of adding, **in the Edit Layout**, a new button to the Application Bar (enter "Calendar" for the Event Name).

`[imagen omitida: wiki id 57503]`

5. Double-click on the new action to go to the event that will be triggered when the action is executed. The event must contain a call to the [Calendar external object](https://wiki.genexus.com/commwiki/wiki?39346) and the Schedule method with the parameters needed.

```
Event 'Calendar'
      Calendar.Schedule(DateDescription,DateStartDate,DateEndDate,DateStartTime,DateEndTime,DatePlace)
Endevent
```

**Note:** Even though all the parameters may not be used, they must be included in the method call. If some are not used, you can include the empty string ("") instead.

Now your action has been configured.

## [Final result](#Final+result)

|  |  |
| --- | --- |
| **Android** | **iOS** |
|  |  |

**Note:** In Android, the scheduled meeting is open and already saved. Tap on Cancel if you want to delete it. If you tap on the Back button, the event is saved anyway. That's because of the Android API design.

### [See Also](#See+Also)

[Calendar external object](https://wiki.genexus.com/commwiki/wiki?39346)


|  |
| --- |
| **Backlinks** |
| [Calendar external object](https://wiki.genexus.com/commwiki/wiki?39346) |

---
