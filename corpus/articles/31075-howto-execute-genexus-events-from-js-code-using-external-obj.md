---
title: "HowTo: Execute GeneXus events from JS code using External Objects"
source_id: 31075
source_url: https://wiki.genexus.com/commwiki/wiki?31075
genexus_version: "18"
---

# HowTo: Execute GeneXus events from JS code using External Objects

The following example shows how to execute GeneXus events from Javascript code using [Native Objects](https://wiki.genexus.com/commwiki/wiki?6148).

In particular, in this example, you can learn how to interact with the browser and trigger a GeneXus event in response to a Javascript event ([the scroll event](https://developer.mozilla.org/en-US/docs/Web/Events/scroll)). The scroll event is fired when the document view has been scrolled. In GeneXus, you can define an event handler for window scrolling.

The purpose of this article is to learn about [External Objects for Javascript](https://wiki.genexus.com/commwiki/wiki?31064), see how to trigger GeneXus Events from external Javascript resources, how to handle Javascript events from GeneXus Code.

For example, if your web pages have a fixed header (with absolute position), you can make the header shrink when the pixels scrolled in the current document (vertically) reach a certain value. On the other hand, the header can expand again when the window is scrolled by the user and the pixels do not reach that value.

|  |
| --- |
|  |

First, define the Javascript (changeonscroll.js) as follows:

`[imagen omitida: wiki id 31089]`

**Note**:

1. The **shrinkOnHeight property** determines the pixels that the window should scroll until an event is fired.
2. The function is triggered when the document is ready, and an event listener is added using the JQuery **on** method. The main idea is to attach an event handler to the scroll event.
3. Inside that function (the event handler), you notify the GeneXus event using the gx.fx.obs.notify expression. The only way to notify a GeneXus event from the Javascript is by using the gx.fx.obs.notify method (which is defined in the standard GeneXus js library - gxgral.js).

### [External object definition](#External+object+definition)

The External object has the [Javascript External Name property](https://wiki.genexus.com/commwiki/wiki?56499) set to Changeonscroll.

* If you define a variable based on ChangeOnScroll External Object in any object, a constructor of Changeonscroll needs to be defined in the JS code.
* Events in GeneXus are always static, so you have to set the IsStatic property to True.

`[imagen omitida: wiki id 53530]`

Remember that events are always static, so the property **shrinkOnHeight** is defined as static as well, and the **Javascript External Name property** is set to shrinkOnHeight because that's the name of the property in the JS source.

`[imagen omitida: wiki id 53532]`

The Javascript External Name property of the event is the name used in the Javascript definition to map to the GeneXus event.

`[imagen omitida: wiki id 53531]`

It can be useful to namespace your events, so you don't unintentionally disconnect events that you didn't or couldn't know about.

### [Using the External Object from GX code](#Using+the+External+Object+from+GX+code)

First, add the reference to the JS in the HTTP headers of the page. Use [Javascript Referenced files property](https://wiki.genexus.com/commwiki/wiki?37851,,).

Otherwise, do the following:

```
Event Start
    Form.HeaderRawHTML += '<script type="text/javascript" src="Changeonscroll.js"></script>'
Endevent
```

**Note:** Another way is to do

```
Event Start
       Form.JScriptSrc.Add("Changeonscroll.js")
Endevent
```

Since **shrinkOnHeight** is a static property, you don't need to define a variable based on the External object, and the assignment to it is static:

`[imagen omitida: wiki id 53529]`

So, the start event is as follows:

```
Event Start
    Form.HeaderRawHTML += '<script type="text/javascript" src="Changeonscroll.js"></script>'
    changeonscroll.shrinkOnHeight = 20
Endevent
```

The events in GeneXus will be the following:

`[imagen omitida: wiki id 53528]`

```
Event changeonscroll.scrolltoShrink
//here code the handler for the event
    content.Class = StyleClass:TableContainer
Endevent

Event changeonscroll.scrolltoExpand
//here code the handler for the event
   content.Class = StyleClass:TableContainer1
Endevent
```

Download from [Change on scroll sample](https://wiki.genexus.com/commwiki/wiki?31097,,).

### [See Also](#See+Also)

[HowTo: Implement a dictionary data type using JS and server side code](https://wiki.genexus.com/commwiki/wiki?31066)


|  |
| --- |
| **Backlinks** |
| [External Objects for Javascript](https://wiki.genexus.com/commwiki/wiki?31064) | [How to interact with the Window Object's Methods](https://wiki.genexus.com/commwiki/wiki?31086) |

---
