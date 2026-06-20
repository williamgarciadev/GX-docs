---
title: "DateTime picker for Native Mobile Applications"
source_id: 34167
source_url: https://wiki.genexus.com/commwiki/wiki?34167
genexus_version: "18"
---

# DateTime picker for Native Mobile Applications

When you include an editable attribute or variable based on [DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370) (or its variants [Date data type](https://wiki.genexus.com/commwiki/wiki?7373) and [Time domain](https://wiki.genexus.com/commwiki/wiki?15050)), GeneXus automatically incorporates a picker in the application form where the end user is able to select the value associated with that field.

### [Android platform](#Android+platform)

The picker follows the [Material Design](https://material.io/guidelines/material-design/introduction.html) guidelines and displays it as a pop-up tiny window on the current form.  
More information in [HowTo: Adding Material Design to Android applications](https://wiki.genexus.com/commwiki/wiki?31004).

|  |  |
| --- | --- |
| **Type** | **Runtime effect and behavior** |
| [Date](https://wiki.genexus.com/commwiki/wiki?7373) | It displays a prompt with a calendar where it is possible to select the date value. |
| [Time](https://wiki.genexus.com/commwiki/wiki?15050) | It displays a prompt with a clock to select the desirable time. |
| [DateTime](https://wiki.genexus.com/commwiki/wiki?7370) | It includes two independent fields for edit, the Date and the Time. |

### [Apple platform](#Apple+platform)

The picker follows the [Apple's Human Interface](https://developer.apple.com/ios/human-interface-guidelines/ui-controls/pickers/) guidelines and displays it as a wheel control on the current form.

|  |  |
| --- | --- |
| **Type** | **Runtime effect and behavior** |
| [Date](https://wiki.genexus.com/commwiki/wiki?7373) | By default, It displays a wheel in the bottom of the Panel where it's possible to set the date value.    Also, if the [Auto Grow property](https://wiki.genexus.com/commwiki/wiki?20204) is enabled on the editable field, the wheel will be displayed in-line. |
| [Time](https://wiki.genexus.com/commwiki/wiki?15050) | By default, it displays a wheel to select the hour, minutes and AM/PM in the bottom of the Panel.    Analogously to the previous scenario, It can be displayed in-line. |
| [DateTime](https://wiki.genexus.com/commwiki/wiki?7370) | By default, It puts a prompt where it's possible to edit the Date and the Time independently by selecting one of them.    Analogously to the previous scenario, It can be displayed by both wheels in-line.  In this case, the date is fully selected (not by month, day and year). |

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Objects:** | [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With pattern and Work With object](https://wiki.genexus.com/commwiki/wiki?15974) |
| **Data type:** | Character, VarChar |
| **Generators:** | [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258) |


|  |
| --- |
| **Backlinks** |
| [Time Invite Message property.](https://wiki.genexus.com/commwiki/wiki?37100) |

---
