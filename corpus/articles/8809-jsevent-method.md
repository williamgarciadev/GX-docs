---
title: "JSEvent method"
source_id: 8809
source_url: https://wiki.genexus.com/commwiki/wiki?8809
genexus_version: "18"
---

# JSEvent method

Uses the controls “Click” and “OnChange” events to trigger JavaScript code.

### [Syntax](#Syntax)

*Control***.JSEvent(**'*Event\_JavaScript'***,** "Y*our\_JavaScript\_code")*  
  
**Where:**  
***‘****Event\_JavaScript’*  
    Is the name of the JavaScript event to be dealt.  
  
*"Your\_JavaScript\_code"*  
code to be dealt.

### [Scope](#Scope)

**Objects:** [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)  
**Controls:** Bitmap Type Variable, [Button](https://wiki.genexus.com/commwiki/wiki?6011), Combo, Dynamic Combo, Dynamic List Box, List Box, Picture, Text Block  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3)

### [Description](#Description)

The valid values are: "onclick" (Edit, Button, Pictures, Bitmap type variables and Text Blocks type controls) and "onchange" (for Combo, Dynamic Combo, Listbox and Dynamic Listbox type controls).  
  
It must be possible to include the JavaScript code written in the second parameter in an IF; i.e.: it must return TRUE or FALSE.  
If the result is TRUE, the control associated event will be triggered.

### [Samples](#Samples)

```
ButtonName.JSEvent( 'onclick', "confirm( 'Are you sure?')")
```

When the user presses the button, the confirmation will appear and, only if the answer is Yes, the GeneXus event associated to the button will be executed (if any).

### [Compatibility](#Compatibility)

**Warning**: Since [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?28265,,) it is recommended to use whenever possible [External Objects for Javascript](https://wiki.genexus.com/commwiki/wiki?31064) instead of the JSEvent event. The JSevent use cases are still valid to trigger a function based on user confirmation (such as the javascript confirm function).

Since [GeneXus 16 upgrade 5](https://wiki.genexus.com/commwiki/wiki?43446,,), it is neccesary to modify Javascript code for complex conditionals. If you have conditional similar to:

```
ButtonControlName.JSEvent("onclick", !"if (/*conditions*/) {confirm('Something');} else {true;}")
```

you need to change it in the following way adding an anonymous wrapper function and make sure to always return a *True* or *False* value:

```
ButtonControlName.JSEvent("onclick", !"function() {if (/*conditions*/) { return confirm('Something');} else { return true;} }()")
```

otherwise the following error will appear on the javascript console

```
SyntaxError: Unexpected token 'if'
    at new Function (<anonymous>)
```

### [See Also](#See+Also)

[Selecting Events](https://wiki.genexus.com/commwiki/wiki?8209)


|  |
| --- |
| **Backlinks** |
| [Security Scanner built-in tool](https://wiki.genexus.com/commwiki/wiki?46412) | [Security Scanner built-in tool (GeneXus 18 or prior)](https://wiki.genexus.com/commwiki/wiki?52570) |

---
