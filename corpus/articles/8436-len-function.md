---
title: "Len function"
source_id: 8436
source_url: https://wiki.genexus.com/commwiki/wiki?8436
genexus_version: "18"
---

# Len function

Returns the number of characters in a character expression.

### [Syntax](#Syntax)

**Len(***Character-Expression***)**  
  
**Where:**  
*Character-Expression*   
    Must be a Character Expression.

**Type Returned:**  
Numeric

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Work Panel](https://wiki.genexus.com/commwiki/wiki?7387,,)  
**Generators:** 

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), RPG, Cobol, Visual FoxPro (up to GeneXus X Evolution 3), Ruby (up to GeneXus X Evolution 3)

### [Description](#Description)

The Len function returns the number of characters in a character expression. Trailing blanks are ignored.

### [Samples](#Samples)

```
Event 'Len function test'
     &CharExp = 'HELLO'
     &Length = Len(&CharExp)
     msg(Str(&Length,1))        //The shown result is: 5     
Endevent
```

```
- &CharExp: Character(20)
- &Length: Numeric(1)
```

### [See Also](#See+Also)

[Length method](https://wiki.genexus.com/commwiki/wiki?12704)


|  |
| --- |
| **Backlinks** |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) |
| [Length method](https://wiki.genexus.com/commwiki/wiki?12704) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [Query object expressions](https://wiki.genexus.com/commwiki/wiki?11782) |

---
