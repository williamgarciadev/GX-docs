---
title: "Format function"
source_id: 8406
source_url: https://wiki.genexus.com/commwiki/wiki?8406
genexus_version: "18"
---

# Format function

Creates a character text from a given text that may contain parameter markers and the values indicated for the parameters.

### [Syntax](#Syntax)

**Format(**S*tr* [, <*character-expression1>*,..., <*character-expressionN>*]**)**

**Where:**  
  
*Str*  
  Is a character data type that contains zero or more parameter markers (from 1 to 9) like %1, %2, etc.  
  It may be a character [expression](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?51320,,).  
  This content may be [translated](https://wiki.genexus.com/commwiki/wiki?6330).  
  
*character-expression1,...,character-expressionN*  
  List of character [expressions](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?51320,,)separated by commas*.* They indicate the values to be placed where the parameter markers are sited in *Str.*

**Type Returned:**  
Character

### [Scope](#Scope)

**Objects:**[Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453),
[Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

The Format function allows you to create a character text from a given text that may contain parameter markers and the values indicated for the parameters.

If a '%' sign needs to be included in the text, it must be preceded by the '\' (backslash) sign to indicate that it is not a parameter. For example: "This is not a parameter marker: \%1".

### [Samples](#Samples)

**1)** In the following example, parameter markers are %1 and %2. They state where, in the resulting string, the values of "Alex" and "26" must be embedded.

```
Msg(Format("%1 is %2 years old.", "Alex", "26"))
```

The [Msg rule](https://wiki.genexus.com/commwiki/wiki?6854) will show the text: *"Alex is 26 years old"*.

**2)**In the following example, the markers are replaced with attributes, and the result is assigned to a variable:

```
&Variable=Format("Customer %1 was born in %2", CustomerName, CountryName);
```


|  |
| --- |
| **Backlinks** |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) |
| [Table of contents:GeneXus Application Localization](https://wiki.genexus.com/commwiki/wiki?6330) | [Msg command](https://wiki.genexus.com/commwiki/wiki?31635) | [Refmsg rule](https://wiki.genexus.com/commwiki/wiki?6865) |

---
