---
title: "For in command"
source_id: 6359
source_url: https://wiki.genexus.com/commwiki/wiki?6359
genexus_version: "18"
---

# For in command

Traverses an array or a collection.

### [Syntax](#Syntax)

**For** *&Var* **in** *expression*  
   code  
**Endfor**

**Where**:

&*Var*  
   Specifies a variable that must have the same data type as the items of the *expression*

*expression*  
   Any expression whose value is a collection, array or matrix.

*code*  
   GeneXus code to be run in each iteration.

### [Samples](#Samples)

Suppose the *expression* is an array variable:

```
for &var in &varArray()
   … // code
endfor
```

The previous code stores each value of the array &varArray in the &var variable. For vectors of one dimension, the code is expanded to:

```
&x = 1
Do while &x <= rows(&varArray())
   &var = &varArray(&x)
   ... // code
   &x += 1
EndDo
```

*Expression* can also be an array of two dimension (matrix) variables:

```
for &var in &varMatrix()
   ... // code
endfor
```

The expanded code would be as follows:

```
&x = 1
Do while &x <= rows(&varMatrix())
   &y = 1
    Do while &y <= cols(&varMatrix())
       &var = &varMatrix( &x, &y)
       ... // code
       &y += 1
    EndDo
  &x += 1
EndDo
```

It may even be a [collection variable](https://wiki.genexus.com/commwiki/wiki?6352) of any type (including a variable with Collection Property set as 'False' but of an 'SDT collection' data type). For more details, see the two ways of [Implementing SDT collections](https://wiki.genexus.com/commwiki/wiki?6296):

```
for &var in &collection
    ...
endfor
```

An expression can not only be a variable, but also, for example, the result of a [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270) or a [Procedure](https://wiki.genexus.com/commwiki/wiki?6293):

```
for &var in DataProvider(parms)
    ...
endfor
```

```
for &var in Procedure(parms)
    ...
endfor
```

Remember not to write any method, '[Udp method](https://wiki.genexus.com/commwiki/wiki?3964)' is assumed.

In sum, any *expression* whose evaluation results in a collection, array or matrix, is a valid one to run through.

**Notes**:

* The array/matrix/collection values cannot be changed during the scanning. This means that changes in the &Var value, in the command scope, do not affect the corresponding array/matrix/collection or vice versa.
* The vector/matrix/collection position cannot be obtained during the scanning. For this, a variable must be defined as counter.
* These structures can be nested to scan several arrays, matrixes or collections. This takes into account when a Subroutine that also has a For In is called within the structure.
* Like in a [For Each command](https://wiki.genexus.com/commwiki/wiki?20195,,) or Do While, commands can be included that "break" the scanning, such as Exit or Return.
* Available for User Events in
  [Android](https://wiki.genexus.com/commwiki/wiki?14453) and
  [Apple](https://wiki.genexus.com/commwiki/wiki?14917) since [GeneXus 16 upgrade 3](https://wiki.genexus.com/commwiki/wiki?42129,,). In this case, Procedures and Data Providers cannot be used as part of the expression within the For in command. That is to say, when you are using the For in command in User Events on these platforms, you cannot use the output of a Procedure or a Data Provider as an expression.

### [See Also](#See+Also)

[Collection variables](https://wiki.genexus.com/commwiki/wiki?6352)  
[Collection Domains](https://wiki.genexus.com/commwiki/wiki?6393)


|  |
| --- |
| **Backlinks** |
| [Collection Domains](https://wiki.genexus.com/commwiki/wiki?6393) | [Collection variables](https://wiki.genexus.com/commwiki/wiki?6352) | [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) |
| [IN Operator](https://wiki.genexus.com/commwiki/wiki?11688) | [Input clause](https://wiki.genexus.com/commwiki/wiki?25406) | [Using Data Providers in Other GX Objects](https://wiki.genexus.com/commwiki/wiki?5310) |

---
