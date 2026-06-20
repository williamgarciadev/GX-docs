---
title: "DateTime storage timezone property"
source_id: 17218
source_url: https://wiki.genexus.com/commwiki/wiki?17218
genexus_version: "18"
---

# DateTime storage timezone property

Controls whether DateTime data type attributes are all stored using the same TimeZone in the Database or not. It is also used to enable/disable TimeZone Support.

### [Scope](#Scope)

**Level:** [Environment](https://wiki.genexus.com/commwiki/wiki?7115)

### [Description](#Description)

Sets the [TimeZone](https://wiki.genexus.com/commwiki/wiki?21997,,) in which the DateTime fields are stored in the Database. Depending on the value set, it enables TimeZone Support.

**Values**

* **Undefined**

The [TimeZone](https://wiki.genexus.com/commwiki/wiki?21997,,) of DateTime attributes is Unknown. No conversion from or to the [Current TimeZone](https://wiki.genexus.com/commwiki/wiki?22146) is made.

This is the ***default value for Knowledge Bases converted from previous versions*** in order to preserve compatibility.

* **GMT/UTC**

All DateTime data type attributes are stored in [UTC](https://wiki.genexus.com/commwiki/wiki?21994,,). Conversion from and to the Current TimeZone is automatic.

This is the ***default value for new Knowledge Bases***.

* **Application Server**

All DateTime data type attributes are stored in the application server's [TZ](https://wiki.genexus.com/commwiki/wiki?21998,,). Conversion from and to the Current TimeZone is automatic.

Use this value if you are converting your application from previous GeneXus versions and you *positively know* that the actual data in the database is stored in the application server's timezone. You get TimeZone support without having to convert all DateTime values in your Database.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a Rebuild All.

### [See Also](#See+Also)

* [Changing the value of DateTime Storage property](https://wiki.genexus.com/commwiki/wiki?22022)
* [TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019)
* [View DateTime values in a selected time zone - TimeZone Scenario](https://wiki.genexus.com/commwiki/wiki?22140)
* [Last Updated - TimeZone Scenario](https://wiki.genexus.com/commwiki/wiki?22139,,)


|  |
| --- |
| **Backlinks** |
| [Changing the value of DateTime Storage property](https://wiki.genexus.com/commwiki/wiki?22022) | [Changing the value of DateTime Storage property at application installation/upgrade time](https://wiki.genexus.com/commwiki/wiki?22045) | [CosmosDB date and datetime handling](https://wiki.genexus.com/commwiki/wiki?54281) |
| [CurrentOffset method](https://wiki.genexus.com/commwiki/wiki?21917) | [Enabling TimeZone Support](https://wiki.genexus.com/commwiki/wiki?22147) | [FromTimeZone method](https://wiki.genexus.com/commwiki/wiki?21916) |
| [GetTimeZone method](https://wiki.genexus.com/commwiki/wiki?21915) | [SetTimeZone method](https://wiki.genexus.com/commwiki/wiki?21893) | [The TimeZone problem](https://wiki.genexus.com/commwiki/wiki?22135) |
| [Toc:TimeZone Support](https://wiki.genexus.com/commwiki/wiki?21988) | [TimeZone Support - DateTime handling](https://wiki.genexus.com/commwiki/wiki?21990) | [TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019) |
| [ToUniversalTime method](https://wiki.genexus.com/commwiki/wiki?16416) |

---
