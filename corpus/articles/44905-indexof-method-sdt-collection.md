---
title: "IndexOf method - SDT Collection"
source_id: 44905
source_url: https://wiki.genexus.com/commwiki/wiki?44905
genexus_version: "18"
---

# IndexOf method - SDT Collection

Returns the index associated to an SDT item in an SDT collection.

### [Syntax](#Syntax)

***&**VarBasedOnSDTCollection.***IndexOf(*****&**VarBasedOnSDT**Item***)**  
  
**Where:**

*&VarBasedOnSDTCollection*  
     It must be a variable based on an SDT collection (or a variable based on a simple SDT and defined as a collection).

*&VarBasedOnSDT**Item*  
     Variable based on an SDT item.

### [Scope](#Scope)

**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3)

### [Description](#Description)

It returns the index (a numeric value) associated with the *Item* parameter element of an SDT collection.

### [Samples](#Samples)

In general, the IndexOf method of an SDT Collection is used in conjunction with the [Remove method](https://wiki.genexus.com/commwiki/wiki?8664). Once you have the desired index (position in the SDT), you can use the associated Remove method.

```
&index = &sdtCollection.IndexOf(&sdtCollection.CurrentItem)
&sdtCollection.Remove(&index)
```

### [Considerations](#Considerations)

This method works with the elements' references and not with their contents. This implies that if a variable with a list of SDT is received as a parameter and a temporary variable is loaded with an item content, IndexOf will return 0 (empty) since this reference is not within the list. It can be useful only in the moment the list is loaded.

### [See Also](#See+Also)

[Structured Data Type methods](https://wiki.genexus.com/commwiki/wiki?24589)


|  |
| --- |
| **Backlinks** |
| [IndexOf method](https://wiki.genexus.com/commwiki/wiki?12696) | [Structured Data Type methods](https://wiki.genexus.com/commwiki/wiki?24589) |

---
