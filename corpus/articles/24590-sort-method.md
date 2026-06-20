---
title: "Sort method"
source_id: 24590
source_url: https://wiki.genexus.com/commwiki/wiki?24590
genexus_version: "18"
---

# Sort method

Sorts the elements of a [SDT](https://wiki.genexus.com/commwiki/wiki?10021) collection variable. It also sorts a variable based on a simple data type that is a collection.

### [Syntax](#Syntax)

**&***VarBasedOnSDTCollection*.**Sort(**"[ColumnListString]"**)**|     **&***VarThatIsCollection*.**Sort()**

**Where:**   
  
*ColumnListString*  
    List of SDT elements to sort in a string separated by a comma. Ascending order is set by default. Use [] or () to set a descending order.

### [Scope](#Scope)

**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892),
[Java](https://wiki.genexus.com/commwiki/wiki?12258)

### Samples

**1)** Consider the following SDT collection:

```
SDT_Collection
  SDT_Item
    Id
    Number
```

And the &VarSDT variable based on the SDT\_Collection SDT.

To order ascending by Id:

```
&VarSDT.Sort("Id")
```

To order descending by Id:

```
&VarSDT.Sort("[Id]")
```

To order ascending by Id and descending by Number:

```
&SDT_Sort.Sort("Id,[Number]")
```

To order descending by Id and ascending by Number:

```
&SDT_Sort.Sort("(Id),Number")
```

**2)** Consider the &CustomerNameCollection variable based on the Character data type.

To order ascending the collection of customer names:

```
&CustomerNameCollection.Sort()
```

### Considerations

The C# generators use the method ArrayList.Sort from [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892). It compares two String objects by evaluating the numeric values of the individual Unicode characters of the strings using the [CompareOrdinal](<br />
https://docs.microsoft.com/en-us/dotnet/api/system.string.compareordinal?redirectedfrom=MSDN&view=netcore-3.1#overloads) method.

[Java](https://wiki.genexus.com/commwiki/wiki?12258) uses the standard:  [String API](http://docs.oracle.com/javase/7/docs/api/java/lang/String.html#compareTo%28java.lang.String%29) to compare elements; it compares them lexicographically. The comparison is based on the Unicode value of each character in the strings.

All implement the Quicksort algorithm; equal elements do not preserve order.

### [See Also](#See+Also)

[Structured Data Type methods](https://wiki.genexus.com/commwiki/wiki?24589)  
[Implementing SDT collections](https://wiki.genexus.com/commwiki/wiki?6296)


|  |
| --- |
| **Backlinks** |
| [Structured Data Type methods](https://wiki.genexus.com/commwiki/wiki?24589) |

---
