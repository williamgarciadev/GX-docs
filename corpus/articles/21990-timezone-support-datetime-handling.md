---
title: "TimeZone Support - DateTime handling"
source_id: 21990
source_url: https://wiki.genexus.com/commwiki/wiki?21990
genexus_version: "18"
---

# TimeZone Support - DateTime handling

If [TimeZone Support](https://wiki.genexus.com/commwiki/wiki?21988) is enabled, DateTime fields entered by the user, DateTime constants and all operations performed on DateTime fields are made in the [CTZ](https://wiki.genexus.com/commwiki/wiki?22005). A conversion to the value indicated in the [DateTime storage timezone property](https://wiki.genexus.com/commwiki/wiki?17218) (and to read inversely from that value) is performed only to save it in the database.

### [Example](#Example)

An event application such as [EventDay (X Evolution 2)](https://wiki.genexus.com/commwiki/wiki?21617,,) is considered. This application, which is accessed from all over the world, is installed on a server located in the Eastern United States (its Regional Options are configured for this region). [DateTime storage timezone property](https://wiki.genexus.com/commwiki/wiki?17218) is set to [UTC](https://wiki.genexus.com/commwiki/wiki?21994,,); therefore, DateTime fields store all values in UTC.

When a user accesses this application from Montevideo, he/she sees that a certain event starts on 6/6/2013 at 8 a.m. Knowing that the user is located in this region, the application converted DateTime values from UTC to UYT.

If another user accesses it from a different region –for instance, Eastern United States (EST)- the time shown will be that of the region from where the user is connecting; in particular, the [TZ](https://wiki.genexus.com/commwiki/wiki?21998,,) indicated by the browser or the native Smart Device application being run. Both the browser and the native application obtain these data from the Regional Settings of the device / PC, etc.

It should be pointed out that any operation performed on the application, such as a conversion to Character using [TtoC function](https://wiki.genexus.com/commwiki/wiki?8361), is made in the CTZ. Therefore, if msg((TTOC(EventDateTime))) was programmed, the result would also be displayed in the CTZ.

`[imagen omitida: wiki id 17450]`

### [See also](#See+also)

[Current TimeZone](https://wiki.genexus.com/commwiki/wiki?22146)


|  |
| --- |
| **Backlinks** |
| [Toc:TimeZone Support](https://wiki.genexus.com/commwiki/wiki?21988) | [TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019) |

---
