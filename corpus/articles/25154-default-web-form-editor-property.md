---
title: "Default Web Form Editor property"
source_id: 25154
source_url: https://wiki.genexus.com/commwiki/wiki?25154
genexus_version: "18"
---

# Default Web Form Editor property

The Default Web Form Editor property operates at the version level.  
It determines the web editor that will be used by default in designing web forms.

### [Values](#Values)

|  |  |
| --- | --- |
| **HTML** | The editor to be used is [HTML Editor](https://wiki.genexus.com/commwiki/wiki?7673). This is the default value. |
| **Abstract Layout** | The editor to be used is [Web Abstract Editor](https://wiki.genexus.com/commwiki/wiki?24795). As a result, the design will be [responsive](http://en.wikipedia.org/wiki/Responsive_web_design). |

### [Description](#Description)

The Default Web Form Editor property determines the editor that will be used in designing the web form for any new object.  
Consider this to be the editor for the [Root form](https://wiki.genexus.com/commwiki/wiki?24972), because the form may be designed using either editor, interchangeably, building up a tree structure, with the possibility, for different parts of the form, to use a different editors. For more details on this go to [Nesting abstract and HTML form layouts](https://wiki.genexus.com/commwiki/wiki?24786,,).

### [Requirements](#Requirements)

In order to make a [RWD](https://wiki.genexus.com/commwiki/wiki?25157,,) the [HTML Document Type property](https://wiki.genexus.com/commwiki/wiki?13517) needs to be set to HTML 5 because Bootstrap makes use of certain HTML elements and CSS properties that require the use of the HTML5 doctype.

### [Scope](#Scope)

**Objects:**[Transactions](https://wiki.genexus.com/commwiki/wiki?1908), Web Panels.  
**Controls:**Forms  
**Languages:** .NET, Java  
**Interfaces:**Web

### [See Also](#See+Also)

[Web Form Defaults property](https://wiki.genexus.com/commwiki/wiki?25135)


|  |
| --- |
| **Backlinks** |
| [Considerations to develop a Responsive Web Application](https://wiki.genexus.com/commwiki/wiki?29133) | [How to convert my application to make it responsive](https://wiki.genexus.com/commwiki/wiki?25214) | [Web Form Defaults property](https://wiki.genexus.com/commwiki/wiki?25135) |

---
