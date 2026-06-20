---
title: "Replace method"
source_id: 12710
source_url: https://wiki.genexus.com/commwiki/wiki?12710
genexus_version: "18"
---

# Replace method

Replaces the occurrences of a string by the ones of another string.

### [Syntax](#Syntax)

*str1***.****Replace(***str2*, *str3***)**

**Where:**  
*str1*  
    Is the attribute or variable on which the replacements will be made. It must be based on the Character, VarChar or LongVarChar data type.

*str2*  
    Is the string to be searched for and replaced. It must be an attribute, variable or fixed value based on the Character or VarChar data type.

*str3*  
    Is the string replacing the searched one. It must be an attribute, variable or fixed value based on the Character or VarChar data type.

**Type Returned:**  
Character

### [Scope](#Scope)

**Data Types:** [Character](https://wiki.genexus.com/commwiki/wiki?6777), [VarChar](https://wiki.genexus.com/commwiki/wiki?6778), [LongVarChar](https://wiki.genexus.com/commwiki/wiki?7371)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

The Replace method returns a string resulting from replacing all the occurrences of string *Str2*, found in *Str1*, by the string *Str3*.

#### [**Notes:**](#Notes%3A)

* The replacement is simultaneously made. i.e.: when a replacing text is inserted, the inserted text does not take part in the following pattern searches.
* This method differentiates between capital letters and small letters; “a” is different from “A”.

### [Samples](#Samples)

```
&Source = “Test#of#the#Replace#method”
&Ret = &Source.Replace(“#”, " ")        //&Ret = “Test of the Replace method”
```

In this case, the &Ret variable would have the following text (it would be the result of replacing all the occurrences of the  ‘#’ character in  &Source by blank spaces).

### [See Also](#See+Also)

[StrReplace function](https://wiki.genexus.com/commwiki/wiki?8505)  
[StrSearch function](https://wiki.genexus.com/commwiki/wiki?8529)


|  |
| --- |
| **Backlinks** |
| [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [StrReplace function](https://wiki.genexus.com/commwiki/wiki?8505) |

---
