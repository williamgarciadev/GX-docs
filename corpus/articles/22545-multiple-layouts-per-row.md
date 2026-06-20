---
title: "Multiple Layouts per Row"
source_id: 22545
source_url: https://wiki.genexus.com/commwiki/wiki?22545
genexus_version: "18"
---

# Multiple Layouts per Row

Mobile device applications that show repetitive data vary the way in which they show the data of an item in the collection. This is very common in news applications; for instance, when you want to highlight a news article to catch the user's attention or in other scenarios to achieve a non-uniform user interface.

This feature called **Multiple Layouts per Row** significantly simplifies the implementation of this type of interfaces.

### [Purpose](#Purpose)

To create various alternatives for the way in which elements are arranged in a Grid for Smart Devices.

### [How it works](#How+it+works)

For example, let’s consider the [EventDay](https://wiki.genexus.com/commwiki/wiki?22550,,) application, in which there is a grid that loads all the sessions of an event that will be offered on a certain date. In addition, these sessions can be classified as Keynotes and ordinary sessions. Suppose that you want to change the layout of Keynote sessions to make them look more attractive than those sessions that are not Keynotes.

To do so, you have to create a new Layout over the SD Grid of the sessions:

* Click on the upper right corner of the SD Grid.
* On the menu that is displayed, click on “Add New Item Layout”.

`[imagen omitida: wiki id 22546]`

* Enter a name for the new Layout (i.e.: "Keynote").
* Arrange the Layout as desired (Add/move/remove elements).

`[imagen omitida: wiki id 22547]`

* To assign a specific layout to a Grid row, the following code must be written in the Load event of the grid. In this example, the condition is that the session must be a Keynote:

```
Event Grid.Load
    If  SessionIsKeynote
        Grid1.ItemLayout = "Keynote"
    EndIf
EndEvent
```

* Lastly, Run it by pressing F5 and watch the results:

|  |  |  |
| --- | --- | --- |
| **Sesión Keynote** |  | **Sesión normal** |
|  |  |  |

### [Feature in action](#Feature+in+action)

### [Considerations](#Considerations)

* The attributes that determine the grid navigation is the set of attributes of all the Grid’s layouts.
* If a non-existent Layout is specified at runtime, the Default Layout is displayed for that item.

### [See Also](#See+Also)

* [EventDay](https://wiki.genexus.com/commwiki/wiki?22550,,) Sample KB
* [Default Selected Item Layout property](https://wiki.genexus.com/commwiki/wiki?22556)


|  |
| --- |
| **Backlinks** |
| [Default Selected Item Layout property](https://wiki.genexus.com/commwiki/wiki?22556) |
|

---
