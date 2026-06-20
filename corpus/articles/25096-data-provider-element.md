---
title: "Data Provider Element"
source_id: 25096
source_url: https://wiki.genexus.com/commwiki/wiki?25096
genexus_version: "18"
---

# Data Provider Element

It is one of the three main components of the [Data Provider output-based declarative language](https://wiki.genexus.com/commwiki/wiki?5309).

An Element is an atomic value in the Output. 'Code' and 'Name' are Elements in the following example:

```
Customers    // this is a Group
{
   Customer  // this is a Group
   {
      Code = CustomerId    // this is an Element assignment
      Name = CustomerName  // this is an Element assignment
   }
}
```

Each Element must be **assigned** by means of a [Data Provider Element statement](https://wiki.genexus.com/commwiki/wiki?25103). Its syntax is that of [Inline Formulas](https://wiki.genexus.com/commwiki/wiki?6441).

### [Samples](#Samples)

```
SampleOfElements
{ 
   Constant = 'ABC' 
   Complex = 1 if CustomerBalance > 1000; 0 otherwise; 
}
```

**Note:** [IIf clause](https://wiki.genexus.com/commwiki/wiki?2419,,) can be used too, as well as aggregation formulas.

If an Element is assigned with some attributes, GeneXus will infer how to obtain them from the Database in the same way it does in the [For Each command](https://wiki.genexus.com/commwiki/wiki?24744).

Elements and Attributes usually have the same name, as follows:

```
Customers 
{
   Customer 
   {
      CustomerId = CustomerId
      CustomerName = CustomerName
   }
}
```

But beware: the elements on the left are not attributes (but "elements"), unlike those on the right. In order to allow more compact writing, this code is the same as the following:

```
Customers    
{
   Customer
   {
      CustomerId
      CustomerName
   }
}
```

And you can still make it more compact. If you omit the Item name, GeneXus will infer it.

`[imagen omitida: wiki id 9166]`

The Item name is necessary if any element of the collection will have different inputs.

```
Samples
{
   //Fixed Data
   SampleItem
   {
      SampleId = 0
      SampleDsc = 'Fix sample'
   }
   // Data retrieved from the data base 
   SampleItem 
   { 
      SampleId = SampleIdInTable 
      SampleDsc = SampleIdInTable
   }
}
```


|  |
| --- |
| **Backlinks** |
| [Data Provider Element statement](https://wiki.genexus.com/commwiki/wiki?25103) | [Toc:Data Provider language](https://wiki.genexus.com/commwiki/wiki?5309) | [Data Provider: Input](https://wiki.genexus.com/commwiki/wiki?6292) |
| [Inline Formulas within a contextual table](https://wiki.genexus.com/commwiki/wiki?6426) |

---
