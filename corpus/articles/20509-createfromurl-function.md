---
title: "CreateFromURL function"
source_id: 20509
source_url: https://wiki.genexus.com/commwiki/wiki?20509
genexus_version: "18"
---

# CreateFromURL function

Changes an object to be displayed in a certain section of a layout dynamically, with a high degree of parametrization when using a Dynamic Component Creation

All you have to do is to insert a Component Control in any Object and assign the result of the execution of the CreateFromURL function to the control object property.

### [Syntax](#Syntax)

*Control***.Object** = **CreateFromURL(**URL**)**

**Where:**

*URL*It is a string variable (as [VarChar data type](https://wiki.genexus.com/commwiki/wiki?6778)) containing the object and parameters.

Web: Check the GeneXus Work With Pattern which uses this feature to create the [TabbedView Web Component](https://wiki.genexus.com/commwiki/wiki?4796).

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Sample for Web](#Sample+for+Web)

In this example there is a Web Form containing a Web Component called Component, whose purpose is to load the links recently accessed by the user. They are dynamically loaded, meaning, for example, that they are loaded every time that the [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) is Refreshed.

```
Event Refresh
    For &Index = &FirstTab To &LastTab
        Do 'LoadItem'
    EndFor
EndEvent

Sub 'LoadItem'
    &WebComponentUrl = &Tab.WebComponent
     Component.Object = CreateFromURL(&WebComponentUrl)
EndSub
```

The variable &WebComponentURL is Character(1000).

The &Tab variable is based on  the TabOptions [SDT](https://wiki.genexus.com/commwiki/wiki?2427)  whose structure is as follows:

`[imagen omitida: wiki id 21256]`

### [Sample for Smart Devices](#Sample+for+Smart+Devices)

```
Event Start
   &Url = MyPanel.Link(&parm1)
   Component1.Object = CreateFromURL(&Url)
EndEvent
```

### [Availability](#Availability)

CreateFromURL function is available also in Smart Devices since [GeneXus 15 upgrade 12](https://wiki.genexus.com/commwiki/wiki?39737,,).

### [See Also](#See+Also)

* [Create function](https://wiki.genexus.com/commwiki/wiki?8359)
* [Dynamic Component Creation](https://wiki.genexus.com/commwiki/wiki?5404)


|  |
| --- |
| **Backlinks** |
| [Create function](https://wiki.genexus.com/commwiki/wiki?8359) | [Dynamic Component Creation](https://wiki.genexus.com/commwiki/wiki?5404) | [Link Function](https://wiki.genexus.com/commwiki/wiki?8444) |
| [Object property](https://wiki.genexus.com/commwiki/wiki?7011) |

---
