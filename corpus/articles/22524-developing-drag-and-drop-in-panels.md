---
title: "Developing Drag and Drop in Panels"
source_id: 22524
source_url: https://wiki.genexus.com/commwiki/wiki?22524
genexus_version: "18"
---

# Developing Drag and Drop in Panels

This feature enables the end-user to drag & drop elements in controls (Attribute, Image, Textblock, GridRow (grid's inside table), Table, Button, or any User Control). For example, users can drag a product from a grid to a shopping cart image in order to add it to the cart.

To implement the drag & drop feature in a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829), the following events are used:

* [Drag Event](https://wiki.genexus.com/commwiki/wiki?22532)
* [Drop Event](https://wiki.genexus.com/commwiki/wiki?22533)
* [DropAccepted Event](https://wiki.genexus.com/commwiki/wiki?22542)
* [DragCanceled Event](https://wiki.genexus.com/commwiki/wiki?25084) - available as from [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?20247,,)

The Drag event is applied to the element that is going to be dragged, and the Drop event is applied to the possible targets. When dragging an element, the possible targets are all those that have an associated Drop event with the input parameter based on the same data type as the Drag output parameter.

#### [Note](#Note)

When an element is dragged, it is no longer displayed in its original position. To have it displayed again, the Visible property must be set to True when dropping (in the DropAccepted event).

### [Feedback during the Drag & Drop operation](#Feedback+during+the+Drag+%26+Drop+operation)

When a drag & drop operation is made, the controls involved can change their appearance to give feedback to the user. For this purpose, you can set the properties available within the Drag & Drop group of the Attribute, Image, Textblock, Grid, GridRow, Group, and Table classes.

These properties are as follows:

* **Start Dragging**  
  Configures the class to be applied to the element when starting to Drag it.
* **Accept Drag**  
  Configures the class to eventually suggest the user drop this element when the element is dragged and the drag operation is accepted.
* **NoAccept Drag**  
  Configures the class to be used when an element accepts the Drag operation but the element being dragged is not of the expected type.
* **DragOver**  
  Configures the class to provide feedback when an element accepts the Drag operation and the mouse is moving over this element.

### [Feature in action](#Feature+in+action)

### [Availability](#Availability)

This feature is available as of [GeneXus X Evolution 2 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?22626,,).  
In Android only for version 4.0 or higher.

### [Sample](#Sample)

* [LightCRM](https://wiki.genexus.com/commwiki/wiki?22592,,)
* [LightCRM (X Evolution 2)](https://wiki.genexus.com/commwiki/wiki?21779,,)


|  |
| --- |
| **Backlinks** |
| [Attribute theme-class](https://wiki.genexus.com/commwiki/wiki?37646) | [Category:Drag and Drop](https://wiki.genexus.com/commwiki/wiki?5730) |
| [Drag event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?22532) | [DragCanceled event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?25084) | [Drop event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?22533) | [DropAccepted event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?22542) |
|
| [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |

---
