---
title: "Set method"
source_id: 6810
source_url: https://wiki.genexus.com/commwiki/wiki?6810
genexus_version: "18"
---

# Set method

When applied to a variable based on the *WebSession* data type, it adds information to the current active session.  
When applied to a variable based on the *Expression* data type, it sets a value for the variable.  
When applied to a variable/attribute based on the *Date*/ *DateTime* data type, it assigns a year-month-date (time-minutes-seconds), as [YMDtoD](https://wiki.genexus.com/commwiki/wiki?7627) and [YMDHMStoT](https://wiki.genexus.com/commwiki/wiki?7626) functions do.

### [Syntax](#Syntax)

**&**v*arBasedOnWebSession***.Set(***Key***,** *Value***)**  
**&**v*arBasedOnExpressionDataType*.**Set(***Key*, *Value***)**  
*DateAttOrVar***.Set(**yy*,mm,dd***)**  
*DateTime**AttOrVar***.Set(**yy*,mm, dd,* [HH[:MM][:SS]]**)**

**Where:**  
  
*Key*  
   Is the Session or Expression key, and it has to be a String.

*Value*  
   Value that must be based on the Character / Var Char data type.

*yy*  
   Is a numeric [expression](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?51320,,) that represents the year. This value **does** adjust according to the property ‘[First year of 20th century property](https://wiki.genexus.com/commwiki/wiki?7631)’.  
  
*mm*  
   Is a numeric expression that represents the month.  
  
*dd*  
   Is a numeric expression that represents the day.  
  
*HH*  
   Is a numeric expression that represents the hour. The time value **must** be specified in 24-hour format.  
  
*MM*  
   Is a numeric expression that represents the minutes.  
  
*SS*  
   Is a numeric expression that represents the seconds.

### [Scope](#Scope)

**Extended Data Types:** [WebSession](https://wiki.genexus.com/commwiki/wiki?6321), [Expression](https://wiki.genexus.com/commwiki/wiki?6631)  
**Standard Data Types:** [Date](https://wiki.genexus.com/commwiki/wiki?7373), [DateTime](https://wiki.genexus.com/commwiki/wiki?7370)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), [Angular](https://wiki.genexus.com/commwiki/wiki?42550) (Angular generator does not support the WebSession data type)

### [See Also](#See+Also)

[TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019)  
[YMDtoD function](https://wiki.genexus.com/commwiki/wiki?7627)  
[WebSession](https://wiki.genexus.com/commwiki/wiki?6321)  
[Expression](https://wiki.genexus.com/commwiki/wiki?6631)  
[YMDtoD function](https://wiki.genexus.com/commwiki/wiki?7627)  
[YMDHMStoT function](https://wiki.genexus.com/commwiki/wiki?7626)


|  |
| --- |
| **Backlinks** |
| [Expression data type](https://wiki.genexus.com/commwiki/wiki?6631) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [Properties Data Type](https://wiki.genexus.com/commwiki/wiki?31606) |
| [WebSession data type](https://wiki.genexus.com/commwiki/wiki?6321) | [YMDtoD function](https://wiki.genexus.com/commwiki/wiki?7627) |

---
