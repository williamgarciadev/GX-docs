---
title: "Text method"
source_id: 8841
source_url: https://wiki.genexus.com/commwiki/wiki?8841
genexus_version: "18"
---

# Text method

Obtains the description of a certain item from one of the supported controls.

### [Syntax](#Syntax)

*ControlName***.Text(***n***)**  
  
**Where:**  
*n*   
    Is the position of the item in the list (1 refers to the first item from the list)

### [Scope](#Scope)

**Controls:** Combo Boxes, [Dynamic Combo Box](https://wiki.genexus.com/commwiki/wiki?7598), [Dynamic List Box](https://wiki.genexus.com/commwiki/wiki?7599), Forms.Meta, Forms.MetaEquiv, List Boxes  
**Generators:** 

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

The returned value is the item in the position passed.  
Forms.Meta and Forms.MetaEquiv only applies to Web Interface.

### [Samples](#Samples)

```
&CountryName = CountryList.Text(4)
```

In this example, the variable &CountryName is loaded with the description of the attribute CountryList which was defined as a [Dynamic List Box](https://wiki.genexus.com/commwiki/wiki?7599) and shows a list of countries loaded from a table. In this case, the fourth item from the list is obtained.

### [See Also](#See+Also)

[Text Property](https://wiki.genexus.com/commwiki/wiki?10197)
