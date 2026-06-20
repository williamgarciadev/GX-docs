---
title: "Link property"
source_id: 8811
source_url: https://wiki.genexus.com/commwiki/wiki?8811
genexus_version: "18"
---

# Link property

Assigns links to controls in web panel forms. It can be used in combination with the Link function.

### [Syntax](#Syntax)

**control.** Link   

*Contro*l.**link =** *Exp*  
  
**Where:**  
*Contro*l  
    Is the name of a control inserted in the form.    
  
*Exp*  
    Is any valid URL (another web panel, an executable file, a static page, etc.). Parameters can be attributes, variables or constants and they are optional.

### [Scope](#Scope)

**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258), .NET, [.NET Core](https://wiki.genexus.com/commwiki/wiki?38604)  
**Controls:** Attribute/Variable, [Image](https://wiki.genexus.com/commwiki/wiki?5939), [Text Block](https://wiki.genexus.com/commwiki/wiki?5948)

### [Description](#Description)

### [[Examples](https://wiki.genexus.com/commwiki/wiki?8811)](#https%3A%2F%2Fwiki.genexus.com%2Fcommwiki%2Fservlet%2Fwiki%3F8811%2CLink%2BProperty%23Examples+Examples)

Suppose you have a text control in a web panel form and you want to assign a link to it so that when the user clicks on the text control another web panel is called. You should include the following line within event Start code:

```
ViewDescpTxt.Link = link(‘ViewDsc.exe’, &code)
```

in this example you are calling web panel “ViewDsc” and this will receive the code as parameter, therefore web panel ViewDsc must have the rule: parm(Code). Note that parameters are only input values.  
  
Other examples of links:

```
ViewPage.Link = link(‘http://www.artech.com.uy/index.html’)

ViewProduct.Link = link(‘hViewPrd.exe’)
```

### [See Also](#See+Also)

[LinkTarget property](https://wiki.genexus.com/commwiki/wiki?8812)

[Link Function](https://wiki.genexus.com/commwiki/wiki?8444)


|  |
| --- |
| **Backlinks** |
| [How to use responsive images in a web application](https://wiki.genexus.com/commwiki/wiki?31566) | [LinkTarget property](https://wiki.genexus.com/commwiki/wiki?8812) |

---
