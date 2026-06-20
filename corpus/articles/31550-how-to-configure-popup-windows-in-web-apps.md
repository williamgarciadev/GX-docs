---
title: "How to configure Popup windows in Web apps"
source_id: 31550
source_url: https://wiki.genexus.com/commwiki/wiki?31550
genexus_version: "18"
---

# How to configure Popup windows in Web apps

The Popup style is configured through the Theme. Specific classes are available to configure the header, content, and other parts of the Popup window.

There are two ways of configuring the popup style:

1. Configure the *Popup class property* of the Form Class in the Theme (this should be the Form class used in your web forms). In this case, all the web components of the form, including the Master page, have to be associated with the same Form Class.

2. Set the Popup Class of the window.

The [Class property](https://wiki.genexus.com/commwiki/wiki?8741) can be assigned to the Window Data type in order to determine the look & feel of the window. Look at the following sample code:

```
Event 'Boton1'
 &Window.Object = WebPanel1.Create() //&window is Window data type
 &Window.Class = ThemeClass:PopupClass   //PopupClass is a class defined in the Theme, descendant of the predefined PopUp class
 &Window.Open()
EndEvent
```

Through the *Popup Class* (assigned to the *Popup class property* of the Form) or dynamically to the window, you can configure the Header, Content, Resize, and Close button style of the Popups.

## [Popup Class Property](#Popup+Class+Property+)

The Popup Class is a "Form class" property (available for all the Form classes and its descendants), as shown in the figure below:

`[imagen omitida: wiki id 31551]`

## [Popup Class](#Popup+Class)

`[imagen omitida: wiki id 31552]`

The Popup class has the following properties:

### [Header Class property](#Header+Class+property)

It's a Section class that allows configuring the Popup header settings.

### [Content Class Property](#Content+Class+Property)

It's a Section class that allows configuring the Popup content settings.

### [Resize Handle Class Property](#Resize+Handle+Class+Property)

It's an image class that allows configuring the resize handle image settings (in the bottom right corner of the window).

### [Close Button Class Property](#Close+Button+Class+Property)

It's an image class that allows configuring the close button image settings (in the top right corner of the window).

## [See Also](#See+Also)

[How to configure control effects in WEB apps](https://wiki.genexus.com/commwiki/wiki?29662)  
[How to configure link colors and hovering effects for links](https://wiki.genexus.com/commwiki/wiki?29647)
