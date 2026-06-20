---
title: "Dynamic Component Creation"
source_id: 5404
source_url: https://wiki.genexus.com/commwiki/wiki?5404
genexus_version: "18"
---

# Dynamic Component Creation

Using [Web Components](https://wiki.genexus.com/commwiki/wiki?1864) or [Components](https://wiki.genexus.com/commwiki/wiki?29811) is one of the options available for building a high degree of component re-usability by centralizing behavior in a single object.

The possibility of instantiating specific Components at runtime enables you to have highly dynamic applications. This means you can change the application layout or behavior by instantiating different Components depending on certain application parameters.

### [Description](#Description)

When using Components you can achieve a high degree of parameterization by using the [Create](https://wiki.genexus.com/commwiki/wiki?8359) and [CreateFromURL](https://wiki.genexus.com/commwiki/wiki?20509) functions to dynamically change the object to be displayed in a certain section of a layout.

To use it, all you have to do is insert a Component Control in any Object and assign the result of the execution of the *Create* or *CreateFromURL* function to the control [Object property](https://wiki.genexus.com/commwiki/wiki?7011).

The Create function is used to create an instance of a Component. It has two options: static and dynamic.

### [Create Syntax](#Create+Syntax)

*Control*.Object = **Create(** xxx, [parameters]**)**

Where:

*Control  
   It is the name of the Component control added to the object.*

*xxx*  
   It is a Component or an attribute/variable containing the Component (\*).

*parameters*  
   Is the list of xxx parameters separated by a semicolon.

With the *static* option, you cannot change the web component reference at runtime, while the dynamic option allows you to change the name of the Web Component at run-time, but the parameters and data types are fixed.

(\*) Note that in Smart Devices, it is not the name of the panel; refer to [Call Variable](https://wiki.genexus.com/commwiki/wiki?17489) to know how to name it.

### [Samples](#Samples)

```
// Static creation
Control.Object = View.Create(&parm1, &parm2)

// Dynamic Creation using the Create function ( Variable Object with fixed parameters )
&Object = "View" // or something like "sd:WorkWithPerson.Person.Detail" in Panels
Control.Object = Create(&Object, &parm1, &parm2)

// Dynamic Creation using the CreateFromURL function
&Object = "View"
&link = link( &Object , &parm1, &parm2 )
Control.Object = CreateFromURL(&link)
```

Web: Check the GeneXus Work With Pattern which uses this feature to create the [TabbedView Web Component](https://wiki.genexus.com/commwiki/wiki?4796).

### [See also](#See+also)

[CreateFromURL function](https://wiki.genexus.com/commwiki/wiki?20509)  
[Create function](https://wiki.genexus.com/commwiki/wiki?8359)


|  |
| --- |
| **Backlinks** |
| [Component control](https://wiki.genexus.com/commwiki/wiki?29811) | [Create function](https://wiki.genexus.com/commwiki/wiki?8359) | [CreateFromURL function](https://wiki.genexus.com/commwiki/wiki?20509) |
| [TabbedView Web Component](https://wiki.genexus.com/commwiki/wiki?4796) | [Web Component control](https://wiki.genexus.com/commwiki/wiki?31172) |

---
