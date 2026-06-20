---
title: "StrReplace function"
source_id: 8505
source_url: https://wiki.genexus.com/commwiki/wiki?8505
genexus_version: "18"
---

# StrReplace function

Replaces the occurrences of a string by the ones of another string.

### [Syntax](#Syntax)

**StrReplace(***str1*, *str2*, *str3***)**

**Where:**  
  
*str1*  
    Is the string on which the replacements will be made, the strong string. This variable may be Character, VarChar or LongVarChar type.

*str2*  
    Is the string to be searched for and replaced. This variable may be Character or VarChar type.

*str3*  
    Is the string replacing the searched one. This variable may be Character or VarChar type.

**Type Returned:**  
Character

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

The StrReplace function returns a string resulting from replacing all the occurrences of string *&Str2*, found in *&Str1*, by the string *&Str3*.

**Notes:**

* The replacement is simultaneously made. i.e.: when a replacing text is inserted, the inserted text does not take part in the following pattern searches.
* This function differentiates between capital letters and small letters; “a” is different from “A”.

### [Samples](#Samples)

```
&Source = “Test#of#the#StrReplace#function”
&Ret = StrReplace(&Source, “#”, “ “)
// Result: &Ret = “Test of the StrReplace function”
```

In this case, the &Ret variable will have the text above (it will be the result of replacing all the occurrences of the  ‘#’ character in  &Source by blank spaces).

### [See Also](#See+Also)

[Replace method](https://wiki.genexus.com/commwiki/wiki?12710)  
[StrSearch function](https://wiki.genexus.com/commwiki/wiki?8529)


|  |
| --- |
| **Backlinks** |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) |
| [IndexOf method](https://wiki.genexus.com/commwiki/wiki?12696) | [LastIndexOf method](https://wiki.genexus.com/commwiki/wiki?12697) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [Query object expressions](https://wiki.genexus.com/commwiki/wiki?11782) |
| [Replace method](https://wiki.genexus.com/commwiki/wiki?12710) | [StrSearch function](https://wiki.genexus.com/commwiki/wiki?8529) | [StrSearchRev function](https://wiki.genexus.com/commwiki/wiki?8507) |

---
