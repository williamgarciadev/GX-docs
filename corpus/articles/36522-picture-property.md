---
title: "Picture property"
source_id: 36522
source_url: https://wiki.genexus.com/commwiki/wiki?36522
genexus_version: "18"
---

# Picture property

Sets the desired format to accept and display the value for an attribute or variable.

### [Scope](#Scope)

**Level:** [Attribute](https://wiki.genexus.com/commwiki/wiki?7240), [Variable](https://wiki.genexus.com/commwiki/wiki?7375)

### [Description](#Description)

This property is offered for [Attributes and Variables](https://wiki.genexus.com/commwiki/wiki?6911) to set their edit format (mask). The following table shows the possible values that can be entered for the property:

|  |  |
| --- | --- |
| **9** | Indicates that a digit between 0 and 9 must be entered or shown. |
| **Z** | Indicates that you want to show blank when there is a left zero. The Z must be in uppercase. |
| . **(period)** | [IDE](https://wiki.genexus.com/commwiki/wiki?5587,,) decimal separator representation. |
| **, (comma)** | [IDE](https://wiki.genexus.com/commwiki/wiki?5587,,) thousand separator representation. |
| **X** | Represents any character. |
| ! | Represents a single character in uppercase. |
| **+** | Indicates that all values (positives and negatives) will be displayed preceded by the sign. |
| **@!** | Indicates that you want the full field to be entered and shown in uppercase. |
| **( )** | Indicates that negative values are displayed in parentheses and positive values remain the same. For example, for picture (99.9) value 12 will be displayed as 12 and value -12 as (12). |
| **DB** | Indicates that negative values will not include the sign and will be followed by the string "DB" (debit), while positive values will be followed by the string "CR" (credit). |

Note that the decimal separator (period character) and thousand separator (comma character) will be generated according to the [Decimal separator property](https://wiki.genexus.com/commwiki/wiki?7670).

If the picture changes at runtime to decrease precision (for example, from 999.99 to 999), the decimal value is lost; if after that it returns to the original value, the decimal will be 00 until the variable value is set again.

If Z is placed to the right of the decimal part of a number, it behaves the same as 9.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies both at run-time and at design-time.

### [Samples](#Samples)

* For Numeric fields —for example, a Numeric(4) attribute— by default its Picture property value will be ZZZ9. This means that non-significant zeros will not be shown. If you want the zeros on the left of the number to be displayed, you must set the value 9999.
* For Date data type fields:
  + If the field [Date format property (for Language Objects)](https://wiki.genexus.com/commwiki/wiki?8904) is set with "Year with two digits" value, the Picture property will automatically be set with 99/99/99.
  + If the field [Date format property (for Language Objects)](https://wiki.genexus.com/commwiki/wiki?8904) is set with "Year with four digits" value, the Picture property will automatically be set with 99/99/9999.

### [See Also](#See+Also)

[Picture Properties Group](https://wiki.genexus.com/commwiki/wiki?6800)


|  |
| --- |
| **Backlinks** |
| [Invite Message property](https://wiki.genexus.com/commwiki/wiki?19697) | [InviteMessage property (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?53870) | [Picture Properties Group](https://wiki.genexus.com/commwiki/wiki?6800) |
| [ToFormattedString method](https://wiki.genexus.com/commwiki/wiki?12722) |

---
