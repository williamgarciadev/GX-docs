---
title: "SetTimeZone method"
source_id: 21893
source_url: https://wiki.genexus.com/commwiki/wiki?21893
genexus_version: "18"
---

# SetTimeZone method

Replaces the [Current TimeZone](https://wiki.genexus.com/commwiki/wiki?22146) (CTZ) with the one indicated in the parameter.

### [Syntax](#Syntax)

&boolean = DateTime.**SetTimeZone(***<TimeZone>***)**

**Where:**  
*TimeZone*  
           Is a parameter that must be of [Timezones Domains](https://wiki.genexus.com/commwiki/wiki?21989) type.

**Note**: This domain doesn’t list all possible Time Zone values. Therefore, if you need to use one that is not included in the domain, using TimeZones.Convert(<string>) is suggested; being <string> the Time Zone's name.

**Data Type:**  
[DateTime](https://wiki.genexus.com/commwiki/wiki?7370)

**Type returned:**  
[Boolean](https://wiki.genexus.com/commwiki/wiki?4374)

* True if the function was successfully executed.
* False if the parameter value is not valid.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3)

### [Description](#Description)

By using this method, an application could offer a feature that shows data in a different TZ than the one automatically selected. For example, an SD application for managing meetings usually shows the time of a meeting in the TZ corresponding to the physical location in which it will take place. However, an end-user may need to have this time shown in a different TZ, in order to be able to participate in the meeting.

* This method has no effect on the way data is stored in and/or retrieved from the database (read [DateTime storage timezone property](https://wiki.genexus.com/commwiki/wiki?17218)).
* Changing the [CTZ](https://wiki.genexus.com/commwiki/wiki?22005) with this method affects the entire session, until it is executed again.

### [Samples](#Samples)

```
Event 'SetTZ'
   &bool= DateTime.SetTimeZone(Timezones.Azores)
Endevent
```

Suppose that this application is run from a device in Uruguay. The TimeZone considered for all operations with DateTimes will be America/Montevideo. If, for example, a query is made by the TimeZone (with [GetTimeZone method](https://wiki.genexus.com/commwiki/wiki?21915)), ‘America/Montevideo’ will be obtained.

However, after running the ‘SetTZ’ event shown in the example, the TimeZone for the entire application is changed to 'Atlantic/Azores' for all operations with DateTimes as from executing this event and until another SetTimeZone is executed.

### [See Also](#See+Also)

[Enabling TimeZone Support](https://wiki.genexus.com/commwiki/wiki?22147)  
[DateTime storage timezone property](https://wiki.genexus.com/commwiki/wiki?17218)  
[GetTimeZone method](https://wiki.genexus.com/commwiki/wiki?21915)  
[FromTimeZone method](https://wiki.genexus.com/commwiki/wiki?21916)  
[CurrentOffset method](https://wiki.genexus.com/commwiki/wiki?21917)


|  |
| --- |
| **Backlinks** |
| [Current TimeZone](https://wiki.genexus.com/commwiki/wiki?22146) | [CurrentOffset method](https://wiki.genexus.com/commwiki/wiki?21917) | [FromTimeZone method](https://wiki.genexus.com/commwiki/wiki?21916) |
| [GetTimeZone method](https://wiki.genexus.com/commwiki/wiki?21915) | [Toc:TimeZone Support](https://wiki.genexus.com/commwiki/wiki?21988) | [View DateTime values in a selected time zone - TimeZone Scenario](https://wiki.genexus.com/commwiki/wiki?22140) |

---
