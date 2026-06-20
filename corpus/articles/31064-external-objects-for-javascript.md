---
title: "External Objects for Javascript"
source_id: 31064
source_url: https://wiki.genexus.com/commwiki/wiki?31064
genexus_version: "18"
---

# External Objects for Javascript

By the means of an [Native Object](https://wiki.genexus.com/commwiki/wiki?6148) the user can publish methods and properties of an external Javascript resource. As a consequence, these methods can be called from the GeneXus code. This functionality is in favor of code integration and allows accessing the functionalities given by external resources in a smooth way.

Moreover, GeneXus Events can be triggered from the Javascript code (see [HowTo: Execute GeneXus events from JS code using External Objects](https://wiki.genexus.com/commwiki/wiki?31075)).

## [Questions & Answers](#Questions+%26+Answers)

### [When should I use an External Object to map JS resources?](#When+should+I+use+an+External+Object+to+map+JS+resources%3F)

When you need to publish methods of a Javascript in order to provide an easy way in GeneXus to call those methods.

### [What about User Controls vs. External Objects?](#What+about+User+Controls+vs.+External+Objects%3F)

[Web User Controls](https://wiki.genexus.com/commwiki/wiki?27212) definitions are only needed when you need to implement a UI control. There are cases when you only need to use Javascript functions and methods in your code, but no UI is involved in the solution. In that case, you use External Objects mapped to JS.

### [What code is executed when Java (or .NET) and Javascript also is mapped to the EO?](#What+code+is+executed+when+Java+%28or+.NET%29+and+Javascript+also+is+mapped+to+the+EO%3F)

The question to answer is what code is actually executed when the EO defines a mapping for Java (or .NET) code, and for Javascript code also.

Well, it depends on the tier where the code is generated ([Event execution on the client and server side](https://wiki.genexus.com/commwiki/wiki?22529))

* If the code is generated client side, the Javascript code is triggered.
* If the code is generated server side, the Java (or .NET) code is executed.
* When only Javascript is mapped to the EO, and the code is generated server-side, it's also executed, but properties cannot be read, and the methods should not return values.

## [How to implement the interaction with JS using External Objects](#How+to+implement+the+interaction+with+JS+using+External+Objects)

* To publish JS properties and methods to be accessible from GeneXus code, you need to declare them in the External Object.
* To use the external JS resource, you have to add the reference to the HTML header, for instance, using the HeaderRawHTML Form method.
* The [Javascript External Name property](https://wiki.genexus.com/commwiki/wiki?56499) must be configured for each Property, Method, or Event, to determine the correspondence to the external Javascript source.
* If you define a variable based on the External Object in any GeneXus object, a constructor needs to be defined in the JS code.
* If you need to call a GeneXus event from a JS external code:
  + declare the event in an External Object
  + notify the GeneXus event using the **gx****.fx.obs.notify** expression within the JS external code. This is the only way to notify a GeneXus event from the Javascript (**gx** **.fx.obs.notify** definition is in the standard GeneXus js library - gxgral.js)
* Events in GeneXus are always static, so in the External Object Events definition, you have to set the IsStatic property to TRUE. The Events can be called from other events, as if they were methods.

## [Examples](#Examples)

There are many uses of External Objects for Javascript functionality; here some of them are introduced:

### [1. Implementing a Dictionary that runs server side and client side](#1.+Implementing+a+Dictionary+that+runs+server+side+and+client+side+)

Implement a dictionary, which by definition is a data type composed of a collection of (key, value) pairs, such that each possible key appears just once in the collection. One of the most interesting issues of this example is that it executes .NET or Java code on the server-side and Javascript code on the client-side.

Look at this example in [HowTo: Implement a dictionary data type using JS and server side code](https://wiki.genexus.com/commwiki/wiki?31066).

### [2. Change the page appearance on Scroll](#2.+Change+the+page+appearance+on+Scroll)

This is a canonical example where you interact with the window and execute events in GeneXus accordingly. In particular, this example shows how to interact with the [scroll event](https://developer.mozilla.org/es/docs/Web/Events/scroll).

Look at this example in [HowTo: Execute GeneXus events from JS code using External Objects](https://wiki.genexus.com/commwiki/wiki?31075).

### [3. Easy access to Window's Object methods.](#3.+Easy+access+to+Window%27s+Object+methods.)

See [How to interact with the Window Object's Methods](https://wiki.genexus.com/commwiki/wiki?31086).

### [Troubleshooting](#Troubleshooting)

1. error spc0200: External Object X does not implement method 'scroll(' for C# Web environment ).   
Specification Failed

**Cause:** The previous error is thrown if you miss assigning a Javascript External Name to an event of the EO.

2. TypeError: X is not a constructor

**Cause:** If the object in GeneXus defines a variable based on the X EO, the Javascript linked to the EO has to define a constructor function. This is because the JS code generated for the object executes the **new** command.

3. If the EO isn't working properly, use the Javascript debugging tools provided by the browser. One possible reason it doesn't work can be that the Javascript doesn't load because of syntax errors in the source code.


|  |
| --- |
| **Backlinks** |
| [Category:External Object](https://wiki.genexus.com/commwiki/wiki?5669) | [External Objects with Type property 'Native Object'](https://wiki.genexus.com/commwiki/wiki?6148) |
| [External Objects with Type property 'Native Object' (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?56447) | [Global Events](https://wiki.genexus.com/commwiki/wiki?31164) | [How to interact with the Window Object's Methods](https://wiki.genexus.com/commwiki/wiki?31086) |
| [HowTo: Execute GeneXus events from JS code using External Objects](https://wiki.genexus.com/commwiki/wiki?31075) | [HowTo: Implement a dictionary data type using JS and server side code](https://wiki.genexus.com/commwiki/wiki?31066) | [JSEvent method](https://wiki.genexus.com/commwiki/wiki?8809) |

---
