---
title: "ToNumeric method"
source_id: 12717
source_url: https://wiki.genexus.com/commwiki/wiki?12717
genexus_version: "18"
---

# ToNumeric method

Converts a number in character format to numeric format.

### [Syntax](#Syntax)

*String*.ToNumeric([DecimalSeparator: Character])

**Where:**  
  
*String* Is an attribute or variable based on the Character/VarChar/LongVarChar data type.

*DecimalSeparator* (optional)  
   Character used as the decimal separator during conversion.

**Type Returned:**  
Numeric N(18.2)

### [Scope](#Scope)

**Data Types:** [Character](https://wiki.genexus.com/commwiki/wiki?6777), [VarChar](https://wiki.genexus.com/commwiki/wiki?6778), [LongVarChar](https://wiki.genexus.com/commwiki/wiki?7371)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),

[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

This method converts the numbers of a character expression to a numeric type. It processes the numbers in the character expression from left to right until a non-numeric character is encountered. If the first character of the character expression is not a number, the result of ToNumeric method will be 0.

### [Samples](#Samples)

```
&AcceptTxt = '-123.35'
&Nbr = &AcceptTxt.ToNumeric() //&Nbr = -123

&AcceptTxt = 'ABC'(*)
&Nbr = &AcceptTxt.ToNumeric() //&Nbr = 0

&AcceptTxt = '12A' (*)
&Nbr = &AcceptTxt.ToNumeric() //&Nbr = 12
```

**Note**: Converting alphanumerics to numerics (\*) is not supported when the method is evaluated in the DBMS (see [Server-Side Functions and Methods](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?11572,,) or [SAC #42709](https://www.genexus.com/en/developers/websac?data=42709;;)).

### [See Also](#See+Also)

[Val function](https://wiki.genexus.com/commwiki/wiki?8528)  
[Str function](https://wiki.genexus.com/commwiki/wiki?7474)  
[ToString method](https://wiki.genexus.com/commwiki/wiki?7090)


|  |
| --- |
| **Backlinks** |
| [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [Val function](https://wiki.genexus.com/commwiki/wiki?8528) |

---
