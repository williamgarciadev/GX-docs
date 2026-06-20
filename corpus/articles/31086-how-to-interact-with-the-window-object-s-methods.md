---
title: "How to interact with the Window Object's Methods"
source_id: 31086
source_url: https://wiki.genexus.com/commwiki/wiki?31086
genexus_version: "18"
---

# How to interact with the Window Object's Methods

Using [External Objects for Javascript](https://wiki.genexus.com/commwiki/wiki?31064), you can interact with the [Window Object](http://www.w3schools.com/jsref/obj_window.asp) from the GeneXus code. Also, it exposes some methods that can be called from the GeneXus code; for example:

* alert method : Displays an alert box with a message and an OK button.
* prompt method : Displays a dialog box that prompts the visitor for input.

In this case, we don't have any associated external javascript. The Javascript External Name of the EO has to be **window**.

`[imagen omitida: wiki id 31098]`

We need to define the methods (alert and prompt), which have to be static methods, along with their parameters.

`[imagen omitida: wiki id 31099]`

### [How to call the window methods](#How+to+call+the+window+methods)

```
Event 'alert'
    ExternalObjectWindow.alert('Read the license agreement first.')
Endevent

Event 'promptnow'
    &outdata = ExternalObjectWindow.prompt(' ')
Endevent
```

Note that we don't define a variable based on the External Object type because the methods we are calling are static. And, if your External Object's method has a return value it cannot be invoked from any event that has any server side code, like calling a Procedure object (the Procedure cannot be called on the same event that is calling the method wich returns a value).

Download the sample from [Window Object interaction sample](https://wiki.genexus.com/commwiki/wiki?31100,,).

### [See also](#See+also)

[How to execute GeneXus events from JS code using External Objects](https://wiki.genexus.com/commwiki/wiki?31075)

[How to implement a dictionary data type using JS and server side code](https://wiki.genexus.com/commwiki/wiki?31066)


|  |
| --- |
| **Backlinks** |
| [External Objects for Javascript](https://wiki.genexus.com/commwiki/wiki?31064) |

---
