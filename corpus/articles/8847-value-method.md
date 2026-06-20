---
title: "Value method"
source_id: 8847
source_url: https://wiki.genexus.com/commwiki/wiki?8847
genexus_version: "18"
---

# Value method

Obtains the value of a certain item from an object.

### [Syntax](#Syntax)

*ControlName***.Value(***n***)**

**Where:**  
*n*   
    Is the item’s position in the list (1 refers to the first item from the list)

### [Scope](#Scope)

**Controls:** Combo Boxes, Dynamic Combo Boxes, Dynamic List Boxes, List Boxes, RadioButton, Form.Meta, Form.MetaEquiv  
**Generators:** 

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

When a list box, dynamic list box, combo box, radio button, dynamic combo box, Form.Meta or Form.MetaEquiv is defined, each item has a value and a text (or description). This method is used to obtain the value of a certain item from a [Transaction](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,) or a [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916). Form.Meta and Form.Equiv only apply to a Web Interface.

### [Samples](#Samples)

```
&CountryCode = CountryList.Value(4)
```

In this example, the &Countrycode variable is loaded with the value of the CountryList attribute, which was defined as a Dynamic List Box and contains a list of countries loaded from a table. In this case, the fourth item from the list is used.

### [See Also](#See+Also)

[AddItem method](https://wiki.genexus.com/commwiki/wiki?8668)  
[RemoveItem method](https://wiki.genexus.com/commwiki/wiki?8672)  
[Clear method](https://wiki.genexus.com/commwiki/wiki?8665)
