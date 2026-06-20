---
title: "View DateTime values in a selected time zone - TimeZone Scenario"
source_id: 22140
source_url: https://wiki.genexus.com/commwiki/wiki?22140
genexus_version: "18"
---

# View DateTime values in a selected time zone - TimeZone Scenario

The article [Last Updated - TimeZone Scenario](https://wiki.genexus.com/commwiki/wiki?22139,,) describes the need to show/accept fields of [DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370) in the [TimeZone](https://wiki.genexus.com/commwiki/wiki?21997,,) corresponding to each user ([Current TimeZone](https://wiki.genexus.com/commwiki/wiki?22146)) regardless of the time zone where these fields were originally generated.

Now, let’s suppose that a user in Tokyo needs to see fields of DateTime type in a time zone different than his current [TZ](https://wiki.genexus.com/commwiki/wiki?21998,,). For instance, this could be the schedule of a conference that takes place in another country. The user sees the conference times in his time zone but he may also need to see them in the time zone of the country where they take place.

### [Solution](#Solution)

To solve this scenario, the application must have [TimeZone Support](https://wiki.genexus.com/commwiki/wiki?21988) enabled and allow the user to select the time zone of the country where the conference takes place from the user’s interface.

Suppose that the conference takes place in New York. Its time zone is [TimeZones](https://wiki.genexus.com/commwiki/wiki?21989).New\_York. The application must have an event, similar to the one below, that changes alternatively from the user’s time zone to New York’s time zone, and whose code invokes the [SetTimeZone method](https://wiki.genexus.com/commwiki/wiki?21893).

```
Event "Change time zone"
    if DateTime.GetTimeZone() <> TimeZones.New_York
      // &PreviousTimeZone is a variable based on the TimeZones Domain that is used to hold the value of the default user time zone.
      &PreviousTimeZone = DateTime.GetTimeZone()
      DateTime.SetTimeZone(TimeZones.New_York)
   else
      DateTime.SetTimeZone(&PreviousTimeZone)
   endif
   Refresh
EndEvent
```

### [Other scenarios](#Other+scenarios)

[Last Updated - TimeZone Scenario](https://wiki.genexus.com/commwiki/wiki?22139,,)

### [See also](#See+also)

[Current TimeZone](https://wiki.genexus.com/commwiki/wiki?22146)  
[SetTimeZone method](https://wiki.genexus.com/commwiki/wiki?21893)  
[Timezones Domain](https://wiki.genexus.com/commwiki/wiki?21989)


|  |
| --- |
| **Backlinks** |
| [DateTime storage timezone property](https://wiki.genexus.com/commwiki/wiki?17218) | [Enabling TimeZone Support](https://wiki.genexus.com/commwiki/wiki?22147) | [Toc:TimeZone Support](https://wiki.genexus.com/commwiki/wiki?21988) |

---
