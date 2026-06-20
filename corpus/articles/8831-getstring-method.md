---
title: "GetString method"
source_id: 8831
source_url: https://wiki.genexus.com/commwiki/wiki?8831
genexus_version: "18"
---

# GetString method

Allows a Web Panel that contains Web Components to query the values of controls within Web Components.

### [Syntax](#Syntax)

*WebComponentControl***.GetString(**"ControlName"**)**

**Where:**

*WebComponentControl*  
    Is the name of the [Web Component control](https://wiki.genexus.com/commwiki/wiki?31172) included in the [Web Panel Web Layout](https://wiki.genexus.com/commwiki/wiki?8132).

*ControlName*  
    Is the name of the control to be queried. It must be enclosed between quotes. If it is a variable, it must be prefixed by an ampersand.

### [Scope](#Scope)

**Controls:** [Web Component control](https://wiki.genexus.com/commwiki/wiki?31172)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3)

### [Description](#Description)

This method can be applied to Web Components controls included in [Web Panels](https://wiki.genexus.com/commwiki/wiki?6916) to get the value of a Web Component control within a parent Web Panel.   
The name of the control to be queried is the only parameter and must be enclosed between quotes (if it is a variable, it must be prefixed by an ampersand).

### [Samples](#Samples)

Suppose you have in a Web Component object the &Var1 variable displayed on the screen.

If you include this Web Component in a Web Panel (the Web Component control is named Component1), from a Web Panel event you will be able to define the following:

```
&Var2 = Component1.GetString("&Var1")
```

**Notes:**

* This method is only supported on Web Panels with [Web User Experience property](https://wiki.genexus.com/commwiki/wiki?22449) = Previous versions compatible.
* For Web Panels with [Web User Experience property](https://wiki.genexus.com/commwiki/wiki?22449) = Smooth, please use [Global Events](https://wiki.genexus.com/commwiki/wiki?31164) or [WebSession data type](https://wiki.genexus.com/commwiki/wiki?6321).
* To use this method you have to set the [Standard Functions property at Knowledge Base level](https://wiki.genexus.com/commwiki/wiki?7403) to "Allows non-standard functions when specifying".

####
