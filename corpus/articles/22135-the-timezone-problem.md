---
title: "The TimeZone problem"
source_id: 22135
source_url: https://wiki.genexus.com/commwiki/wiki?22135
genexus_version: "18"
---

# The TimeZone problem

Users of Web or Smart Device applications are frequently located in different time zones, both among themselves and in relation to the application server. In this context, data of [DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370) can be entered and viewed in different time zones. Failure to take this into account may lead to confusion when interpreting DateTime field values.

In GeneXus, time zone support is aimed at normalizing how DateTime field values are used and stored in order to solve the problems mentioned above.

### [Background](#Background)

The Earth is divided into time zones which are offset from Coordinated Universal Time ([UTC](https://wiki.genexus.com/commwiki/wiki?21994,,)).  This offset is expressed as the number of hours and minutes to be added to UTC time to obtain the local time in a certain [TimeZone](https://wiki.genexus.com/commwiki/wiki?21997,,) ([TZ](https://wiki.genexus.com/commwiki/wiki?21998,,)). For example, since Montevideo’s TZ has a [TimeZone Offset](https://wiki.genexus.com/commwiki/wiki?22007,,) of -3:00 (minus three hours and zero minutes), when the time is 6:31 p.m. in Montevideo, UTC time is 9:31 p.m.

In some parts of the world (in general they are countries, but these zones can be represented by cities when the countries are big), the time is usually changed during summer in order to save energy. This is known as Daylight Saving Time ([DST](https://wiki.genexus.com/commwiki/wiki?22003,,)). For example, in Uruguay the Time Zone Offset is -2:00 instead of -3:00 during summer.

What should be taken into account about DST is that for the same TZ, the offset value can change depending on the time of year.

It must be noted that the TZ problem doesn’t apply to Date or DateTime type fields that don’t include the Date part (see [DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370) and [Time domain](https://wiki.genexus.com/commwiki/wiki?15050)). Both the date and time are necessary to correctly determine the offset to apply.

### [Problem details](#Problem+details)

Suppose that a DateTime attribute stored in the database has the value November 19, 2010 22:48. The application server is located in New York and two users, one in Tokyo and the other in Buenos Aires, see the attribute value in a Web or [SD](https://wiki.genexus.com/commwiki/wiki?20766) application. What value should be displayed to each user?

1. Exactly the same value (November 19, 2010 22:48)
2. The value converted to their corresponding TZs (Tokyo and Buenos Aires)
3. The same value converted to New York’s TZ (where the server resides)

To answer this question we need to analyze the value of the [DateTime storage timezone property](https://wiki.genexus.com/commwiki/wiki?17218).

* If the property has Undefined value, only the first answer is possible.

Since GeneXus doesn’t know the TZ over which the attribute value is expressed, it can't convert it.

* If the property doesn't have Undefined value, the second answer is correct.

In this case, GeneXus knows the TZ corresponding to the attribute value (UTC or Application Server) and automatically makes the conversion to each user’s TZ.

In a similar situation, let’s say that both users (one in Tokyo and the other in Buenos Aires) record a transaction at the same second. The user in Tokyo will record it on July 28, 2012 0:28:17 and the user in Buenos Aires on July 27, 2012, 12:28:17. What value should be stored in the database as registration time/date for each transaction?

Once again, to answer this question we need to analyze the value of the DateTime storage timezone property.

* If the property has Undefined value, transactions will be recorded with different values.

Note that even though the application may know the TZ of each transaction, this value is lost as soon as it is stored in the database. DateTime type attributes don’t keep TZ specifications at the level of each value.

* If the property doesn’t have Undefined value, both transactions will be recorded as if they were made simultaneously.

GeneXus converts the date of the transaction made by the user in Tokyo and that of the user in Buenos Aires from their corresponding TZs to the one indicated by the property value.

**Sample Table**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Datetime Value** | **Application Client Location** | **DateTime Storage Timezone Property Value / DB Stored Value** | | |
| **Undefined** | **UTC** | **Application Server**   New York (UTC -5) |
| July 28, 2012  00:28:17 | Tokio (UTC +9) | July 28, 2012  00:28:17 | July 27, 2012  15:28:17 | July 27, 2012  10:28:17 |
| July 27, 2012  12:28:17 | Buenos Aires (UTC -3) | July 27, 2012, 12:28:17 | July 27, 2012  15:28:17 | July 27, 2012  10:28:17 |

### 

### [More here](#More+here)

* Read [Enabling TimeZone Support](https://wiki.genexus.com/commwiki/wiki?22147) to learn how to enable/disable time zone support.
* To automatically determine the TZ in which to show data, read [Current TimeZone](https://wiki.genexus.com/commwiki/wiki?22146).


|  |
| --- |
| **Backlinks** |
| [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Toc:TimeZone Support](https://wiki.genexus.com/commwiki/wiki?21988) |
| [ToUniversalTime method](https://wiki.genexus.com/commwiki/wiki?16416) |

---
