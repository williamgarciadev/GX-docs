---
title: "Object property"
source_id: 7011
source_url: https://wiki.genexus.com/commwiki/wiki?7011
genexus_version: "18"
---

# Object property

Assigns the Object that is to be encapsulated in a [Web Component control](https://wiki.genexus.com/commwiki/wiki?31172), [Component control](https://wiki.genexus.com/commwiki/wiki?29811),  [QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075) or [DashboardViewer control](https://wiki.genexus.com/commwiki/wiki?36770).

### [Syntax](#Syntax)

*ControlName***.Object**

**Where:**  
*ControlName*Must be the name of a [Web Component control](https://wiki.genexus.com/commwiki/wiki?31172), [Component control](https://wiki.genexus.com/commwiki/wiki?29811), [QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075) or [DashboardViewer control](https://wiki.genexus.com/commwiki/wiki?36770).

### [Description](#Description)

When used for Web Components and Components, this property must be used in conjunction with the [Create function](https://wiki.genexus.com/commwiki/wiki?8359) or [CreateFromURL function](https://wiki.genexus.com/commwiki/wiki?20509). For example:

```
ControlName.Object = Create(ObjectName, [par1, par2, ..., parN])
```

On the other hand, when used for QueryViewers and DashboardViewers, the syntax is:

```
ControlName.Object = ObjectName([par1, par2, ..., parN])
 
```

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Controls:** | [Web Component](https://wiki.genexus.com/commwiki/wiki?31172), [Component](https://wiki.genexus.com/commwiki/wiki?29811), [QueryViewer](https://wiki.genexus.com/commwiki/wiki?9075), [DashboardViewer](https://wiki.genexus.com/commwiki/wiki?36770) |
| **Generators:** | [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453) |
|  |  |

### [See also](#See+also)

* [QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075)
* [Create function](https://wiki.genexus.com/commwiki/wiki?8359)
* [CreateFromURL function](https://wiki.genexus.com/commwiki/wiki?20509)


|  |
| --- |
| **Backlinks** |
| [Component control](https://wiki.genexus.com/commwiki/wiki?29811) | [Create function](https://wiki.genexus.com/commwiki/wiki?8359) | [Dynamic Component Creation](https://wiki.genexus.com/commwiki/wiki?5404) |
| [GetResponse method](https://wiki.genexus.com/commwiki/wiki?7097) | [Refresh command in web](https://wiki.genexus.com/commwiki/wiki?25286) | [Web Component control](https://wiki.genexus.com/commwiki/wiki?31172) | [Web Component Control Properties](https://wiki.genexus.com/commwiki/wiki?10044) |
| [WebWrapper data type](https://wiki.genexus.com/commwiki/wiki?6624) |

---
