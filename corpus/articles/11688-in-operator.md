---
title: "IN Operator"
source_id: 11688
source_url: https://wiki.genexus.com/commwiki/wiki?11688
genexus_version: "18"
---

# IN Operator

It is a logical operator that returns True if the left operand value is equal to some of the values in the right operand.

### [Syntax](#Syntax)

Att | Var | VarBasedOnSDT.Property **IN** [(<comma-separated-constant-list>) | *Collection* | *Array* ]

Att **IN** [Data Selector object](https://wiki.genexus.com/commwiki/wiki?5271)

**Where:**  
*Att*Is an [Attribute](https://wiki.genexus.com/commwiki/wiki?7240) defined in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836).

*Var*Is a scalar [Variable](https://wiki.genexus.com/commwiki/wiki?7375) defined in the [GeneXus object](https://wiki.genexus.com/commwiki/wiki?1866) where you are using the IN Operator.

*VarBasedOnSDT.Property*  
Is a property of a [Variable](https://wiki.genexus.com/commwiki/wiki?7375) based on a [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021). Take into account that it must be a property of one element (if your definition is a collection).

*Collection*  
    Refers to attributes or variables based on [Collection Domains](https://wiki.genexus.com/commwiki/wiki?6393) or [variables defined as collection](https://wiki.genexus.com/commwiki/wiki?6352) with the same data type of the left operand.

**Note**: The first operand can't be an [expression](https://wiki.genexus.com/commwiki/wiki?51320,,) (i.e "&numValue.ToString() IN &CharCollection" is not supported).

### [Description](#Description)

When the right operand is a list of constants delimited by a comma, the IN operand is equivalent to the expression: LeftOperand = FirstConstant OR LeftOperand = SecondConstant ...

When the right operand is a Collection or Array, the semantic is the same but the list varies depending on the elements the Collection or Array has in that specific execution.

In the case of *In DataSelectors,*see [Data Selectors in For Each command](https://wiki.genexus.com/commwiki/wiki?5312).

#### [Associated specification messages and controls:](#Associated+specification+messages+and+controls%3A)

* spc0075: Operand %1 does not match the data type of %2 in the IN comparison.
* spc0076: %1 must be a collection to be used as the right operand in an IN comparison.
* spc0077: %1's data type (%2) is not supported in an IN comparison.

### [**Samples**](#Samples)

```
If &element in &Collection
    //do something
EndIf
```

```
For Each
    where Attribute in &Collection
    //do something
EndFor
```

```
For Each
    where Attribute in DataSelector
    //do something
EndFor
```

```
if &Message.Id in &ErrorCodesCollection  //&Message is based on Messages.Message
    //do something 
Endif 
```

### [**See also**](#See+also)

* [For in command](https://wiki.genexus.com/commwiki/wiki?6359)
* [Implementing SDT collections](https://wiki.genexus.com/commwiki/wiki?6296)
* [Collection variables](https://wiki.genexus.com/commwiki/wiki?6352)
* [Data Selectors in For Each command](https://wiki.genexus.com/commwiki/wiki?5312)


|  |
| --- |
| **Backlinks** |
| [Category:Operators](https://wiki.genexus.com/commwiki/wiki?6882) |

---
