---
title: "Add method"
source_id: 8657
source_url: https://wiki.genexus.com/commwiki/wiki?8657
genexus_version: "18"
---

# Add method

Adds an item to a collection.

### [Syntax](#Syntax)

***&**VarBasedOnSDTCollection.***Add(****&***VarBasedOnSDT**Item* [ **,** *Position* ] **)**|     **&***VarBasedOnSimpleDataTypeDefinedAsCollection*.**Add(**Item [ **,** *Position* ]**)**  
  
**Where:**   
  
*&VarBasedOnSDTCollection*  
   Variable based on an SDT collection (or a variable based on a simple SDT and defined as a collection). Learn more about these options at [Implementing SDT collections](https://wiki.genexus.com/commwiki/wiki?6296).

*&VarBasedOnSDT**Item*  
    Variable based on the SDT item to be added to the collection.

&*VarBasedOnSimpleDataTypeDefinedAsCollection* Variable based on a simple data type and defined/marked as a collection.

*Item* Fixed value or variable/attribute that stores the value to be added to the collection.

*Position*  
    Relative position.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3).

### [Description](#Description)

This method adds an Item to the collection in a relative position: *Position*. If *Position* is omitted, or if “0” is specified, the Item is added at the end of the collection. *Position* starts at 1.  
  
Before adding each element to a collection, it is necessary to create a memory space using the new operator.

### [Samples](#Samples)

Consider the following [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021):

`[imagen omitida: wiki id 57622]`

Suppose you define two variables in a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) (it could be another object), as shown below:

* &Attractions: Based on the Attractions SDT (so, it is a collection of items with attractions data).
* &OneAttraction: Based on Attractions.AttractionsItem (so, its data type corresponds to an item of the collection).

The &Attractions collection is already loaded with some items and you need to add a new item.

The following Event loads an item and adds it to the collection:

```
Event 'add attraction to the collection'
   &OneAttraction = new()
   &OneAttraction.Id = &Id       //a variable with value is assigned but it could be a fixed value or an attribute (if it is instantiated) 
   &OneAttraction.Name = &Name   //a variable with value is assigned but it could be a fixed value or an attribute (if it is instantiated)
   &Attractions.Add(&OneAttraction)
Endevent
```

**Note**: The same method can also be used to add a new item to a list of Java Scripts (in [Transactions](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,) and [Web Panels](https://wiki.genexus.com/commwiki/wiki?6916)), as shown: *Control**.*****Add(***Item***)**.For more details, see: [Access to a Web Object's Header](https://wiki.genexus.com/commwiki/wiki?7064)

### [See Also](#See+Also)

[Structured Data Type methods](https://wiki.genexus.com/commwiki/wiki?24589)  
[Implementing SDT collections](https://wiki.genexus.com/commwiki/wiki?6296)


|  |
| --- |
| **Backlinks** |
| [Clone method - SDT](https://wiki.genexus.com/commwiki/wiki?8748) | [MailRecipientCollection Data Type](https://wiki.genexus.com/commwiki/wiki?6996) | [New operator (SDT)](https://wiki.genexus.com/commwiki/wiki?8615) |
| [Structured Data Type methods](https://wiki.genexus.com/commwiki/wiki?24589) |

---
