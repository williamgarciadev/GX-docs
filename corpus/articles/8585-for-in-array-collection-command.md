---
title: "For In Array/Collection command"
source_id: 8585
source_url: https://wiki.genexus.com/commwiki/wiki?8585
genexus_version: "18"
---

# For In Array/Collection command

Scans a unidimensional or multidimensional array or a structured data type collection.

### [Syntax](#Syntax)

**For** ***&**Var* **in** ***&**Variable()*  
    *code*  
**Endfor**

**Where:**  
  
**&***Var*  
     Specifies a variable that must have the same data type of the *Array()*.  
  
**&***Variable()*  
     Details a variable based on an array of one or more dimensions, or a structured data type collection.

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), RPG, Cobol, Ruby (up to GeneXus X Evolution 3)

### [Description](#Description)

This command allows you to process or scan any array or structured data type collection variable.  
  
**Notes:**

* It is not possible to modify the array values in the scanning. This means that changes in the *&Var* value, in the structure scope, do not affect the corresponding Variable value or vice versa.
* It is not possible to obtain the vector position during the scanning. This is possible if a variable as a counter is defined.
* It is possible to nest these structures to scan several Variables (arrays or collections). This takes into account when a Subroutine, that also has a For In &Variable, is called within the structure.
* Like in [For Each command](https://wiki.genexus.com/commwiki/wiki?24744) or [Do While](https://wiki.genexus.com/commwiki/wiki?8582), it is possible to include commands that "break" the scanning, such as [Exit command](https://wiki.genexus.com/commwiki/wiki?8590) or [Return command](https://wiki.genexus.com/commwiki/wiki?31353).

### [Samples](#Samples)

The following code belongs to a unidimensional array. It stores each value of the array in the *&Var* variable

```
for &var in &arr()
   … // code
endfor
```

In case of one-dimensional vectors, the code is expanded to:

```
&x = 1
Do while &x <= rows(&arr())
   &var = &array(&x)
    ... // code
   &x += 1
Enddo 
```

In case of two-dimensional arrays, the command is analog:

```
for &var in &arr2()
   … // code
endfor
```

With &arr2, the expanded code would be:

```
&x = 1
Do while &x <= rows(&arr2())
   &y = 1
    Do while &y <= cols(&arr2())
       &var = &arr2( &x, &y)
        ... // code
       &y += 1
    Enddo
    &x += 1
Enddo
```

In case of an SDT collection:

|  |  |  |
| --- | --- | --- |
| Name | Collection | ItemName |
| SDT01 | True | SDT01Item |
| Itm1 |
| Itm2 |
| … |

The code would be:

```
for &item in &collection
  … 
endfor
```

With &collection is a variable based on “SDT01” Structure Data type collection, and &item is based on “SDT01.SDT01Item” type.

The expanded code would be:

```
&x = 1
Do while &x <= &collection.count
   &item.Itm1 = &collection.item(&x).Itm1
   &item.Itm2 = &collection.item(&x).Itm2
   ... // code
   &x += 1
Enddo
```

### [See Also](#See+Also)

[Do While Command](https://wiki.genexus.com/commwiki/wiki?8582)


|  |
| --- |
| **Backlinks** |
| [Code Snippets](https://wiki.genexus.com/commwiki/wiki?10662) | [Do While command](https://wiki.genexus.com/commwiki/wiki?8582) | [HowTo: Create a Code Snippet](https://wiki.genexus.com/commwiki/wiki?10725) |

---
