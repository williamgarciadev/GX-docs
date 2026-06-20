---
title: "TimeZone Support - General Considerations"
source_id: 22019
source_url: https://wiki.genexus.com/commwiki/wiki?22019
genexus_version: "18"
---

# TimeZone Support - General Considerations

There are some considerations you need to take into account when [TimeZone Support](https://wiki.genexus.com/commwiki/wiki?21988) is enabled.

* Date or Time only values

The corresponding [TZ](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?21998,,) offset is applied when the date and time are available. If any of them is missing, such as in a [Time variable](https://wiki.genexus.com/commwiki/wiki?8102), or [Time domain](https://wiki.genexus.com/commwiki/wiki?15050), [Date data type](https://wiki.genexus.com/commwiki/wiki?7373) or [DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370) attributes with only the Time part enabled (**0**:X), the offset cannot be made.

* Application server and database server share the same timezone

The application and database servers are assumed to be in the same TZ: that of the application server. If the DB server has a different TZ, issues could happen when using [ServerNow function](https://wiki.genexus.com/commwiki/wiki?8491) and/or [ServerDate function](https://wiki.genexus.com/commwiki/wiki?8490).

* Access to data from other applications

All DateTime fields of a DB are assumed to be in the TZ indicated by the [DateTime storage timezone property](https://wiki.genexus.com/commwiki/wiki?17218). This should be taken into account if the data is queried or updated by other applications.

All DateTime fields of [External Objects with Type property 'Native Object'](https://wiki.genexus.com/commwiki/wiki?6148) are assumed to be in CTZ format. This should be taken into account when integrating native classes.

* Object's navigation considerations

When [TimeZone Support](https://wiki.genexus.com/commwiki/wiki?21988) is enabled, the following set of functions is not evaluated in the Database Server (optimized) due to DST.

* [Hour function](https://wiki.genexus.com/commwiki/wiki?8415), [Hour method](https://wiki.genexus.com/commwiki/wiki?12652),
* [Day function](https://wiki.genexus.com/commwiki/wiki?8376), [Day method](https://wiki.genexus.com/commwiki/wiki?12646),
* [Month function](https://wiki.genexus.com/commwiki/wiki?8379), [Month method](https://wiki.genexus.com/commwiki/wiki?12647),
* [Year function](https://wiki.genexus.com/commwiki/wiki?8380), [Year method](https://wiki.genexus.com/commwiki/wiki?12648),
* [DoW function](https://wiki.genexus.com/commwiki/wiki?8344), [DayOfWeek method](https://wiki.genexus.com/commwiki/wiki?12657),
* [EoM function](https://wiki.genexus.com/commwiki/wiki?8392), [EndOfMonth method](https://wiki.genexus.com/commwiki/wiki?12656),
* [Minute function](https://wiki.genexus.com/commwiki/wiki?8416), [Minute method](https://wiki.genexus.com/commwiki/wiki?12650),
* [YMDHMStoT function](https://wiki.genexus.com/commwiki/wiki?7626)

* The DateTime values exchanged via [REST Web Services](https://wiki.genexus.com/commwiki/wiki?14573) are in [UTC](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?21994,,).

* [DST](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?22003,,) adjustment for DateTime values prior to 1970 may not be correct!
* In the Date Time storage timezone property you must set a valid Timezone included in the [Olson table](https://en.wikipedia.org/wiki/Tz_database) (**IANA time zone database**), if you set a "custom" Time Zone (not included in the Olson table) the "Name 'Standard time Montevideo' not found in zoneinfo directory" (see [SAC #38552](https://www.genexus.com/es/developers/websac?data=38552))

### [See Also](#See+Also)

[TimeZone Support - DateTime handling](https://wiki.genexus.com/commwiki/wiki?21990)


|  |
| --- |
| **Backlinks** |
| [Changing the value of DateTime Storage property](https://wiki.genexus.com/commwiki/wiki?22022) | [DateTime storage timezone property](https://wiki.genexus.com/commwiki/wiki?17218) | [Day function](https://wiki.genexus.com/commwiki/wiki?8376) |
| [Day method](https://wiki.genexus.com/commwiki/wiki?12646) | [DayOfWeek method](https://wiki.genexus.com/commwiki/wiki?12657) | [DoW function](https://wiki.genexus.com/commwiki/wiki?8344) | [EndOfMonth method](https://wiki.genexus.com/commwiki/wiki?12656) |
| [EoM function](https://wiki.genexus.com/commwiki/wiki?8392) | [Hour function](https://wiki.genexus.com/commwiki/wiki?8415) | [Hour method](https://wiki.genexus.com/commwiki/wiki?12652) | [Minute function](https://wiki.genexus.com/commwiki/wiki?8416) |
| [Minute method](https://wiki.genexus.com/commwiki/wiki?12650) | [Month function](https://wiki.genexus.com/commwiki/wiki?8379) | [Month method](https://wiki.genexus.com/commwiki/wiki?12647) | [Server Side Functions/Methods](https://wiki.genexus.com/commwiki/wiki?11572) |
| [ServerDate function](https://wiki.genexus.com/commwiki/wiki?8490) | [ServerNow function](https://wiki.genexus.com/commwiki/wiki?8491) | [Table of contents:TimeZone Support](https://wiki.genexus.com/commwiki/wiki?21988) | [Year function](https://wiki.genexus.com/commwiki/wiki?8380) |
| [Year method](https://wiki.genexus.com/commwiki/wiki?12648) | [YMDHMStoT function](https://wiki.genexus.com/commwiki/wiki?7626) |

---
