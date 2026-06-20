---
title: "Button control"
source_id: 6011
source_url: https://wiki.genexus.com/commwiki/wiki?6011
genexus_version: "18"
---

# Button control

A Button is a control that by pressing it, the end-user can execute actions like insert, update, delete, print, go to another object, etc.).

To insert a Button control into a form, drag the Button icon from the [GeneXus Toolbox](https://wiki.genexus.com/commwiki/wiki?10000) to the desired part.

Every button must be associated with an event.

`[imagen omitida: wiki id 6012]`

The event may already exist in the object (it could be a System Event or a [User defined event](https://wiki.genexus.com/commwiki/wiki?8044) that was already defined in the object), or you can define a new [User defined event](https://wiki.genexus.com/commwiki/wiki?8044) for the button you are creating.

For this, each button has the [On Click Event property](https://wiki.genexus.com/commwiki/wiki?8746) to assign the name of the event that will be executed at the moment of clicking on the control.

`[imagen omitida: wiki id 6013]`

In the shown example, the pointed button has the 'List Attractions By Country' event assigned to its [On Click Event property](https://wiki.genexus.com/commwiki/wiki?8746).

The 'List Attractions By Country' is a [User defined event](https://wiki.genexus.com/commwiki/wiki?8044) that was previously defined in the Events section of the object. Inside its code, the only action defined is a call to the AttractionsList object (sending to it the &CountryId variable value).

Moreover, every button has the [Control Name property](https://wiki.genexus.com/commwiki/wiki?8754) to define the control name that identifies it inside the object.

#### [Look & Feel of Buttons](#Look+%26+Feel+of+Buttons)

The size of a button is determined by the length of its label ([Caption property](https://wiki.genexus.com/commwiki/wiki?4633) value). If you want all the buttons in the form to have the same size, or you want to have one of them with a specific size, you can associate a [Theme Class](https://wiki.genexus.com/commwiki/wiki?6246) to the button that has the characteristics (Height and Width) you want.

You can have standard or rounded buttons too, and you can design them using [Theme](https://wiki.genexus.com/commwiki/wiki?4375).

#### [Grouping buttons](#Grouping+buttons)

You can create in a form an [Action Group Control for the Web](https://wiki.genexus.com/commwiki/wiki?25631) or an [Action Group Control for Panels](https://wiki.genexus.com/commwiki/wiki?25106) and insert inside it a group of buttons in order to define Toolbars or Menus.

### [See also](#See+also)

[Caption property](https://wiki.genexus.com/commwiki/wiki?4633)  
[BadgeText property](https://wiki.genexus.com/commwiki/wiki?42041)  
[Action Group Control for the Web](https://wiki.genexus.com/commwiki/wiki?25631)  
[Action Group Control for Panels](https://wiki.genexus.com/commwiki/wiki?25106)


|  |
| --- |
| **Backlinks** |
| [Accessible Name Control property](https://wiki.genexus.com/commwiki/wiki?55456) | [Accessible Name Custom property](https://wiki.genexus.com/commwiki/wiki?55469) | [Accessible Name property](https://wiki.genexus.com/commwiki/wiki?55454) |
| [Application Bar control in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?19486) | [AudioRecorder external object](https://wiki.genexus.com/commwiki/wiki?34096) | [Button properties](https://wiki.genexus.com/commwiki/wiki?9916) | [Caption property](https://wiki.genexus.com/commwiki/wiki?4633) |
| [Col Span property](https://wiki.genexus.com/commwiki/wiki?8752) | [Category:Common Controls](https://wiki.genexus.com/commwiki/wiki?5928) | [ControlName property](https://wiki.genexus.com/commwiki/wiki?8754) | [Developing Drag and Drop in Web Panels](https://wiki.genexus.com/commwiki/wiki?5579) |
| [Drag event in Web](https://wiki.genexus.com/commwiki/wiki?9642) | [Drop event in Web](https://wiki.genexus.com/commwiki/wiki?9643) | [Format property (for Web)](https://wiki.genexus.com/commwiki/wiki?31666) | [Category:Free Style Grid control](https://wiki.genexus.com/commwiki/wiki?6058) |
| [GeneXus Markup Language (GXML)](https://wiki.genexus.com/commwiki/wiki?46876) | [gx-elevation property](https://wiki.genexus.com/commwiki/wiki?28180) | [gx-focused-class property](https://wiki.genexus.com/commwiki/wiki?51849) | [HowTo: Format plain text programmatically](https://wiki.genexus.com/commwiki/wiki?31657) |
| [Insert Button](https://wiki.genexus.com/commwiki/wiki?9914) | [JSEvent method](https://wiki.genexus.com/commwiki/wiki?8809) | [On Click Event property](https://wiki.genexus.com/commwiki/wiki?8746) | [Row Span property](https://wiki.genexus.com/commwiki/wiki?8828) |
| [SetFocus method](https://wiki.genexus.com/commwiki/wiki?8836) | [Web Panel Web Layout](https://wiki.genexus.com/commwiki/wiki?8132) |

---
