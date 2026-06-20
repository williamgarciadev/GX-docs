---
title: "PadRight method"
source_id: 12706
source_url: https://wiki.genexus.com/commwiki/wiki?12706
genexus_version: "18"
---

# PadRight method

Builds a character expression from another one, by adding a specified character N times, or blanks to its right side.

### [Syntax](#Syntax)

*Str***.PadRight(***Len* [,*FillChar*]**)**

**Where:**  
  
*Str*  
   Is the character expression from which you want to add right blanks or with the FillChar if indicated.

*Len*  
   Is the numeric expression that indicates the length of the returned string.

*FillChar*  
   Is the character that is added to the right side of ‘Str’. It is an optional parameter, if it is not specified then blanks will be added.

**Type Returned:**  
Character

### [Scope](#Scope)

**Data Types:** [Character](https://wiki.genexus.com/commwiki/wiki?6777), [VarChar](https://wiki.genexus.com/commwiki/wiki?6778), [LongVarChar](https://wiki.genexus.com/commwiki/wiki?7371)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),

[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

Returns a character string, which is the result of adding the ‘FillChar’ to the right side of ‘Str’ as many times until the string is left as long as 'len'.

### [Samples](#Samples)

```
&MyText = “My string”
&Result=&MyText.PadRight(10, ‘*’) // &Result value is “My string*”
```

```
&MyText = “My string”
&Result=&MyText.PadRight(11, ‘*’) // &Result value is “My string**”
```

```
&MyText = “My string”
&Result=&MyText.PadRight(12, ‘*’) // &Result value is “My string***”
```

```
&MyText = “My string”
&Result=&MyText.PadRight(12)       // &Result value is “My string   ”
```

**Note**: All trailing spaces from the original string will be removed before applying the function.

### [See Also](#See+Also)

[PadR function](https://wiki.genexus.com/commwiki/wiki?8476)  
[PadL function](https://wiki.genexus.com/commwiki/wiki?8475)  
[PadLeft method](https://wiki.genexus.com/commwiki/wiki?12705)  
[Trim function](https://wiki.genexus.com/commwiki/wiki?8424)  
[LTrim function](https://wiki.genexus.com/commwiki/wiki?8423)  
[RTrim function](https://wiki.genexus.com/commwiki/wiki?8425)


|  |
| --- |
| **Backlinks** |
| [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [PadR function](https://wiki.genexus.com/commwiki/wiki?8476) |

---
