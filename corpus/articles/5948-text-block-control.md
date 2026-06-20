---
title: "Text Block control"
source_id: 5948
source_url: https://wiki.genexus.com/commwiki/wiki?5948
genexus_version: "18"
---

# Text Block control

The Text Block control allows you to insert text in forms with multiple functions. For example, to show short texts next to other controls, or to show messages, warnings, etc.

* This control can be seen as text directly inserted into the form.
* You can change its appearance (its back color, content, etc.) dynamically (at runtime) by setting properties.

For example, the following code changes the text and the back color of the Text Block named TextBlock1:

```
Event Start
  TextBlock1.Caption='Hello world!'
  TextBlock1.BackColor=RGB(255,000,000)
EndEvent
```

### [How to add a Text Block into a form](#How+to+add+a+Text+Block+into+a+form)

* Drag the Text Block icon from the [GeneXus Toolbox](https://wiki.genexus.com/commwiki/wiki?10000).
* Drop it into the desired part of the form.

### [Login Sample](#Login+Sample)

In the following example, you can see a user login screen. If the user name and password entered are correct, a success message will be displayed in the Tb\_Msg Text Block present in the form. Otherwise, the following message will be displayed: "Password incorrect. Please retry." in the same Text Block.

`[imagen omitida: wiki id 5951]`

In the event associated with the button, the following code has been defined:

```
Event 'Ok'
  &PassIsValid=PassIsValid()
  Do case
     case &PassIsValid = True
          MsgTB.Caption = 'Welcome to the system!'
     otherwise
          MsgTB.Caption = 'Invalid password. Please retry...'
  EndCase
EndEvent
```

### [Associating Links to Text Blocks](#Associating+Links+to+Text+Blocks)

You can associate a link to a Text Block control, like the following code shows:

```
Event Start
    CustomersTB.Link = Link(WWCustomer)
    ProductsTB.Link = Link(WWProduct)
    ProductTypesTB.Link = Link(WWProductType)
    SuppliersTB.Link = Link(WWSupplier)
Endevent
```

In particular, in the previous example, there are four Text block controls (named CustomersTB, ProductsTB, ProductTypesTB, and SuppliersTB) that were included inside an [Action Group Control](https://wiki.genexus.com/commwiki/wiki?25631) to show them in the Form inside a Toolbar, as the following image shows:

`[imagen omitida: wiki id 44204]`

When the user clicks on each Text Block, the corresponding Work With for Web object will be opened at runtime.

### [See Also](#See+Also)

[Text Block properties](https://wiki.genexus.com/commwiki/wiki?9908)  
[Action Group Control for the Web](https://wiki.genexus.com/commwiki/wiki?25631)  
[Action Group Control for Panels](https://wiki.genexus.com/commwiki/wiki?25106)


|  |
| --- |
| **Backlinks** |
| [Alignment property](https://wiki.genexus.com/commwiki/wiki?28993) | [Caption property](https://wiki.genexus.com/commwiki/wiki?4633) | [Col Span property](https://wiki.genexus.com/commwiki/wiki?8752) |
| [Category:Common Controls](https://wiki.genexus.com/commwiki/wiki?5928) | [Comparison between Theme and Design System objects](https://wiki.genexus.com/commwiki/wiki?48985) | [ControlName property](https://wiki.genexus.com/commwiki/wiki?8754) | [Dashboard object Parameters](https://wiki.genexus.com/commwiki/wiki?42662) |
| [Dashboard widgets](https://wiki.genexus.com/commwiki/wiki?36779) | [Default HTML Format (TextBlocks only) property](https://wiki.genexus.com/commwiki/wiki?9083) | [Design System Object - Classes that can be combined](https://wiki.genexus.com/commwiki/wiki?48690) | [Design System Object - Classes to separate what is particular from what is shared](https://wiki.genexus.com/commwiki/wiki?48686) |
| [Design System Object - How to provide style data to your controls](https://wiki.genexus.com/commwiki/wiki?48685) | [Design System Object - Untyped classes](https://wiki.genexus.com/commwiki/wiki?48689) | [Design System Object - What controls do you need to implement the Header?](https://wiki.genexus.com/commwiki/wiki?48683) | [DesignOps - Conventions](https://wiki.genexus.com/commwiki/wiki?46872) |
| [DesignOps - Guide for designers](https://wiki.genexus.com/commwiki/wiki?46871) | [Drag event in Web](https://wiki.genexus.com/commwiki/wiki?9642) | [Drop event in Web](https://wiki.genexus.com/commwiki/wiki?9643) | [Format property](https://wiki.genexus.com/commwiki/wiki?46309) |
| [Format property (for Web)](https://wiki.genexus.com/commwiki/wiki?31666) | [Category:Free Style Grid control](https://wiki.genexus.com/commwiki/wiki?6058) | [Table of contents:GeneXus Application Localization](https://wiki.genexus.com/commwiki/wiki?6330) | [GeneXus Markup Language (GXML)](https://wiki.genexus.com/commwiki/wiki?46876) |
| [gx-elevation property](https://wiki.genexus.com/commwiki/wiki?28180) | [gx-focused-class property](https://wiki.genexus.com/commwiki/wiki?51849) | [HowTo: Format plain text programmatically](https://wiki.genexus.com/commwiki/wiki?31657) | [HowTo: Use Textblock in Panels](https://wiki.genexus.com/commwiki/wiki?18491) |
| [Insert Text Block](https://wiki.genexus.com/commwiki/wiki?9907) | [Link property](https://wiki.genexus.com/commwiki/wiki?8811) | [LinkTarget property](https://wiki.genexus.com/commwiki/wiki?8812) | [On Click Event property](https://wiki.genexus.com/commwiki/wiki?8746) |
| [Return On Click property](https://wiki.genexus.com/commwiki/wiki?8745) | [Row Span property](https://wiki.genexus.com/commwiki/wiki?8828) | [SD Horizontal Position property](https://wiki.genexus.com/commwiki/wiki?45182) | [Web Panel Web Layout](https://wiki.genexus.com/commwiki/wiki?8132) |

---
