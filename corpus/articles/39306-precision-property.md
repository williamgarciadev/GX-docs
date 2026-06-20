---
title: "Precision property"
source_id: 39306
source_url: https://wiki.genexus.com/commwiki/wiki?39306
genexus_version: "18"
---

# Precision property

Determines the precision of a DateTime field. Specifically, whether the DateTime field supports handling Milliseconds.

### [Values](#Values)

|  |  |
| --- | --- |
| **Milliseconds** | Handles milliseconds precision (0 to 999). |
| **Seconds** | Maximum precision is seconds; it does not handle milliseconds (default value). |

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Java](https://wiki.genexus.com/commwiki/wiki?12258), .NET, [.NET Core](https://wiki.genexus.com/commwiki/wiki?38604)  
**Level:** [Attribute](https://wiki.genexus.com/commwiki/wiki?7240), [Domain](https://wiki.genexus.com/commwiki/wiki?7221)

### [Description](#Description)

When Precision is set to Milliseconds, then the [DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370) field supports storing and displaying the DateTime with higher precision than just 1 second; it then supports fractions of seconds like 3.5 seconds (three and a half seconds), 10.250 seconds (ten seconds with 250 milliseconds) or 5.005 seconds (5 seconds with 5 milliseconds). Such a field is often also called a Timestamp.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build All](https://wiki.genexus.com/commwiki/wiki?5691).

### [Availability](#Availability)

This property is available since [GeneXus 15 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?38845,,).

### [See Also](#See+Also)

[Hour format property](https://wiki.genexus.com/commwiki/wiki?39440)


|  |
| --- |
| **Backlinks** |
| [AddMilliseconds method](https://wiki.genexus.com/commwiki/wiki?39524) | [Attribute Empty Value for each DBMS and Data Type](https://wiki.genexus.com/commwiki/wiki?19150) | [DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370) |
| [Difference method](https://wiki.genexus.com/commwiki/wiki?12677) | [Hour format property](https://wiki.genexus.com/commwiki/wiki?39440) | [Map User Control Properties](https://wiki.genexus.com/commwiki/wiki?54170) |
| [MilliSecond method](https://wiki.genexus.com/commwiki/wiki?39523) | [Now function](https://wiki.genexus.com/commwiki/wiki?8335) | [TAdd function](https://wiki.genexus.com/commwiki/wiki?8512) | [TDiff function](https://wiki.genexus.com/commwiki/wiki?8513) |
| [TtoC function](https://wiki.genexus.com/commwiki/wiki?8361) |

---
