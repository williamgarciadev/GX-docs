---
title: "AddItem method"
source_id: 8668
source_url: https://wiki.genexus.com/commwiki/wiki?8668
genexus_version: "18"
---

# AddItem method

Adds a new item at the end of a control.

### [Syntax](#Syntax)

*control***.additem(***code***,** *description* [ **,** *index* ] **)**

**Where:**

*control*  
    Is the name of a control inserted in the form. The control name coincides with the attribute/variable name.

*index*  
    It is optional, and represents the position where the item is inserted. Its value must be greater than 0. If no Index is specified, then the item is added at the end. It is not supported by Form.Meta or Form.MetaEquiv.

### [Scope](#Scope)

**Controls:** Combo Box, [Dynamic Combo Box](https://wiki.genexus.com/commwiki/wiki?7598), [Dynamic List Box](https://wiki.genexus.com/commwiki/wiki?7599), List Box, Radio Button, Grid.  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[Java](https://wiki.genexus.com/commwiki/wiki?12258),
Ruby (up to GeneXus X Evolution 3),
Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

This method is used to add a new item at the end (or at a certain position) of the data set shown by a control inserted in the form.

The [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) of the attribute or variable control must be Combo Box, Dynamic Combo Box, Dynamic List Box or List Box.

It can be also a variable that is a collection. So, when it is inserted into the form it is shown as a Grid control.

### [Samples](#Samples)

The following code can be included inside an event, to load a variable whose [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) = Combo Box with all countries of the American continent. The first item will be 'All'.

```
&Var.clear()
&Var.additem(0, 'All')
For each Country                    //The base table navigated is Country
    where ContinentCode = 'AME'
         &Var.additem(CountryCode, CountryName)
EndFor
```

In this example, a MetaTag to the Web Panel is added:

```
Form.Meta.additem(‘Content’, ‘GeneXus’)
```

**Notes:**

* *Form.Meta* and *Form.MetaEquiv* only applies to Web Interface.
* *Form.Meta* and *Form.MetaEquiv* are Objects' properties.

### [See Also](#See+Also)

[RemoveItem method](https://wiki.genexus.com/commwiki/wiki?8672)  
[Count property](https://wiki.genexus.com/commwiki/wiki?7023)  
[Clear method](https://wiki.genexus.com/commwiki/wiki?8665)


|  |
| --- |
| **Backlinks** |
| [DesignOps - Conventions](https://wiki.genexus.com/commwiki/wiki?46872) | [RemoveItem method](https://wiki.genexus.com/commwiki/wiki?8672) | [Value method](https://wiki.genexus.com/commwiki/wiki?8847) |

---
