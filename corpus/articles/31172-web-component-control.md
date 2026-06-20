---
title: "Web Component control"
source_id: 31172
source_url: https://wiki.genexus.com/commwiki/wiki?31172
genexus_version: "18"
---

# Web Component control

It is a control that can be inserted in a web object form to show the content of a [Web Component object](https://wiki.genexus.com/commwiki/wiki?1864) inside it.

To insert a Web Component control, drag the icon that represents it (`[imagen omitida: wiki id 6057]`) from the toolbox to a Web Form.

The following image shows a [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) form that contains three Web Component controls.

`[imagen omitida: wiki id 35527]`

To make the development task easier, the [Control Name property](https://wiki.genexus.com/commwiki/wiki?8754) of the Web Component controls have been modified to be more descriptive: Header, Login, and Footer.

A grid has also been added in a table to show a list of the airlines. The Login Web Component control is included in the same table on the left.

Header, Login, and Footer were inserted to show one [Web Component object](https://wiki.genexus.com/commwiki/wiki?1864) each.

So, the next step is to define for each Web Component control which Web Component object must be shown inside it at runtime. To achieve it, you must fill the Web Component control [Object property](https://wiki.genexus.com/commwiki/wiki?7011) with the desired web component object name.

`[imagen omitida: wiki id 35528]`

Suppose that other web objects in the same [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) have in their forms web component controls too, to show inside them the same header and footer (or in some cases the login also).

### [Notes](#Notes)

* Web Component controls can even be inserted in [Free Style](https://wiki.genexus.com/commwiki/wiki?6058) grids.
* The Web Component object code is generated inside the same HTML that is generated for the Web object that contains it. This means that the server includes the Web Component at runtime and sends the HTML code containing the Web Component back to the browser.
* Web Components can be created at runtime. This allows you to create highly dynamic applications, which means that the application's layout or behavior can be changed by creating different Web Components, depending on certain application parameters. Read more about this here: [Dynamic Component Creation](https://wiki.genexus.com/commwiki/wiki?5404).

### [See also](#See+also)

[Web Component Control Properties](https://wiki.genexus.com/commwiki/wiki?10044)


|  |
| --- |
| **Backlinks** |
| [Category:Common Controls](https://wiki.genexus.com/commwiki/wiki?5928) | [Component control](https://wiki.genexus.com/commwiki/wiki?29811) | [ControlName property](https://wiki.genexus.com/commwiki/wiki?8754) |
| [Developing Drag and Drop in Web Panels](https://wiki.genexus.com/commwiki/wiki?5579) | [Drag event in Web](https://wiki.genexus.com/commwiki/wiki?9642) | [Drop event in Web](https://wiki.genexus.com/commwiki/wiki?9643) | [Category:Free Style Grid control](https://wiki.genexus.com/commwiki/wiki?6058) |
| [GetString method](https://wiki.genexus.com/commwiki/wiki?8831) | [Insert Web Component](https://wiki.genexus.com/commwiki/wiki?9912) | [Link function](https://wiki.genexus.com/commwiki/wiki?8444) | [Link function (GeneXus 18 Upgrade 12 or prior)](https://wiki.genexus.com/commwiki/wiki?60052) |
| [Object property](https://wiki.genexus.com/commwiki/wiki?7011) | [TabbedView Web Component](https://wiki.genexus.com/commwiki/wiki?4796) | [Web Component Control Properties](https://wiki.genexus.com/commwiki/wiki?10044) | [Category:Web Component object](https://wiki.genexus.com/commwiki/wiki?1864) |

---
