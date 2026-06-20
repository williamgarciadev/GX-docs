---
title: "SetNull method"
source_id: 12730
source_url: https://wiki.genexus.com/commwiki/wiki?12730
genexus_version: "18"
---

# SetNull method

This method allows loading a null value in an attribute, and enables independence from the [Generate null for nullvalue() property](https://wiki.genexus.com/commwiki/wiki?8986) used in assigning a null value attribute.

### [Syntax](#Syntax)

*attribute***.SetNull(****)**

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)  
**Generators:** 

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), RPG, Visual FoxPro (up to GeneXus X Evolution 3), Cobol

### [Description](#Description)

If the attribute allows nulls in the table, using this method can force the attribute to take the null value.

The SetNull method is applied as follows:

* Attributes: The attribute must accept nulls (Nullable property = Yes)
* Variables based on BC: The associated attribute must accept nulls (Nullable property = Yes)
* Variables based on SDT, for example, to stop recursion.

### [Samples](#Samples)

#### [Case to Recursive SDTs:](#Case+to+Recursive+SDTs%3A)

If you define an 'Employee' SDT with a 'Manager' member of the type 'Employee', to stop recursion you have to program &Person.Manager.SetNull().

Before referring to the manager, ask if &Employee.Manager.Isnull(). If you do not program this line, the Manager is automatically initiated.

`[imagen omitida: wiki id 6285]`

```
&Employee.Id = 99
&Employee.Name = 'Mary Shelley'
&Employee.Manager.Id  = 69
&Employee.Manager.Name  = 'Er'
&Employee.Manager.Manager.SetNull()
&Employee.ToXML()
```

Programming is the same as in previous versions, plus IsNull() and SetNull() handling.

The result is the following:

```
<Employee>
</Employee>
```

#### [Other examples:](#Other+examples%3A)

```
OwnerCel.SetNull() if OwnerName.IsEmpty();
```

```
If Y.IsNull()
   X.SetNull()
Else
   X = Y
EndIf
```

### [See Also](#See+Also)

[Null function](https://wiki.genexus.com/commwiki/wiki?8421)  
[IsNull function](https://wiki.genexus.com/commwiki/wiki?2357)


|  |
| --- |
| **Backlinks** |
| [Cosmos DB nulls handling](https://wiki.genexus.com/commwiki/wiki?53633) | [Generate null for nullvalue() property](https://wiki.genexus.com/commwiki/wiki?8986) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) |
| [Nullvalue function](https://wiki.genexus.com/commwiki/wiki?8226) |

---
