---
title: "Concat function"
source_id: 8352
source_url: https://wiki.genexus.com/commwiki/wiki?8352
genexus_version: "18"
---

# Concat function

Concatenates two strings, including a separator if desired.

### [Syntax](#Syntax)

**Concat(***character-expression1***,** *character-expression2***,** [ ,*character-expression3* ] **)**

*character-expression1 **+*** *character-expression2*   
  
**Where:**  
  
*character-expression3*  
    Is the separator between *character-expression1 and character-expression2*

**+** *(plus sign)*

**Type Returned:**  
Character

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453),
[Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

Returns a String that results from the concatenation of *character-expression1 and character-expression2> and separator character-expression3.* Trailing blanks of string character-expression1 are truncated. If character-expression3 is not specified, no separator is inserted.

**Note**: In the iSeries, if the strings character-expression1, character-expression2 or character-expression3 are substituted with functions (substr(), str(), etc), then the returned value is null, because the returned values of these functions are 256-character-long variables.

### [Samples](#Samples)

```
LastName  = 'SMITH '
FirstName = 'JOHN '
&FullName  = Concat(FirstName,LastName,' ')
```

Result: &FullName = 'JOHN SMITH '

In case you want to maintain the trailing blanks in the first parameter, you may change the order of the parameters. For example:

```
LastName  = 'SMITH'
FirstName = 'JOHN '
&FullName = Concat(,LastName,FirstName)
```

With the plus sign, the concatenation is very simple:

```
&FullName  = &Firstname + ' ' + &Lastname
```

Result: &FullName = 'JOHN SMITH'

### [See Also](#See+Also)

[Str function](https://wiki.genexus.com/commwiki/wiki?7474)  
[Substr function](https://wiki.genexus.com/commwiki/wiki?8527)


|  |
| --- |
| **Backlinks** |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) |
| [Category:Operators](https://wiki.genexus.com/commwiki/wiki?6882) | [Str function](https://wiki.genexus.com/commwiki/wiki?7474) | [Substr function](https://wiki.genexus.com/commwiki/wiki?8527) | [Substring method](https://wiki.genexus.com/commwiki/wiki?12713) |

---
