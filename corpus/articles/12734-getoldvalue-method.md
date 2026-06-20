---
title: "GetOldValue method"
source_id: 12734
source_url: https://wiki.genexus.com/commwiki/wiki?12734
genexus_version: "18"
---

# GetOldValue method

Returns the last stored value of a given attribute.

### [Syntax](#Syntax)

*Attribute***.GetOldValue(****)**  
  
**Type Returned:**  
Same as the *Attribute*'s type

### [Scope](#Scope)

**Objects:** [Transaction](https://wiki.genexus.com/commwiki/wiki?1908)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258), RPG, Cobol, Visual FoxPro (up to GeneXus X Evolution 3), Ruby (up to GeneXus X Evolution 3)

### [Description](#Description)

Returns the last stored value, although not already committed 1, of a certain attribute.

The type definition that is returned is equal to the Attribute's type definition.

If *A***t*tribute* is a non-redundant formula, the returned value is the result of evaluating the formula using the last stored values of the attributes involved in the formula.

1 That means, if the GetOldValue is executed with the [AfterValidate Triggering event](https://wiki.genexus.com/commwiki/wiki?8282), it will retrieve the new value.

**Note**: The GetOldValue method used within a rule doesn't return values to the user.

### [Samples](#Samples)

```
msg('Current name: ' + CustomerName + NewLine() + 'Previous name: ' + GetOldValue(CustomerName)) on AfterUpdate;
```

Supposing the current CustomerName value is 'John Doe' and the previous CustomerName value was 'Peter Parker' it will message:

'Current name: John Doe'  
'Previous name: '

So, use the GetOldValue method as follows:

```
&CustomerName = GetOldValue(CustomerName) on AfterUpdate;
msg('Current name: ' + CustomerName + NewLine() + 'Previous name: ' + &CustomerName) on AfterUpdate;
```


|  |
| --- |
| **Backlinks** |
| [GeneXus deprecated functions, methods, and rules](https://wiki.genexus.com/commwiki/wiki?6620) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) |

---
