---
title: "GetVariable method"
source_id: 7056
source_url: https://wiki.genexus.com/commwiki/wiki?7056
genexus_version: "18"
---

# GetVariable method

Returns the value with which the variable is loaded in the POST in a String.

### [Syntax](#Syntax)

**&***VarBasedOnHttpRequest***.GetVariable (***Character-expression**)***  
  
**Where:**  
*Character-expression*  
     Is an expression that refers to the variable name that contains the value to be obtained.  
  
**Type Returned:**  
Character

### [Scope](#Scope)

**Extended Data Types:** [HttpRequest](https://wiki.genexus.com/commwiki/wiki?6933)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3)

### Samples

**Sample #1:** Getting a control value from a GeneXus generated web page.

```
&value = &httprequest.GetVariable(CustomerId.InternalName)  //The value of the screen attribute CustomerId is stored in the &value variable.
```

```
&value = &httprequest.GetVariable(&Email.InternalName)      //The value of the screen variable &Email is stored in the &value variable.
```

**Sample #2:** Getting a control value from a screen control with name= "txtEmail".

```
&value = &httprequest.GetVariable("txtEmail")   //The value of the screen control with name “txtEmail” is stored in the &value variable.
```

### See Also

[HttpRequest Data Type](https://wiki.genexus.com/commwiki/wiki?6933)


|  |
| --- |
| **Backlinks** |
| [HttpRequest data type](https://wiki.genexus.com/commwiki/wiki?6933) |

---
