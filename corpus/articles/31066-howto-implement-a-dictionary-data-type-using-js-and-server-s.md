---
title: "HowTo: Implement a dictionary data type using JS and server side code"
source_id: 31066
source_url: https://wiki.genexus.com/commwiki/wiki?31066
genexus_version: "18"
---

# HowTo: Implement a dictionary data type using JS and server side code

In this article you can learn how to implement a dictionary (a data type composed of a collection of (key, value) pairs, so that each possible key appears just once in the collection).

The operations associated with this data type include adding a pair to the collection, removing a pair from the collection, changing an existing pair and searching for a value associated with a particular key.

This implementation is done using external resources, and the interaction is solved in GeneXus using [Native Objects](https://wiki.genexus.com/commwiki/wiki?6148).

One of the most interesting aspects of this example is that it runs .NET or Java code on the server-side and Javascript code on the client-side. See [Event execution on the client and server side](https://wiki.genexus.com/commwiki/wiki?22529) for details on this topic.

So, if the code is generated server-side, it executes the .NET or Java code (depending on the platform it runs); otherwise, if it's generated client-side, it executes the Javascript code.

### [Purpose of this example](#Purpose+of+this+example)

* Learn about [External Objects for Javascript](https://wiki.genexus.com/commwiki/wiki?31064).
* Understand the two options available for running External Objects (server-side vs. client-side), depending on where the code is generated.

Note that this is an example of using a Native Object, and the implementation of the solution is not the main aspect to consider.

Some aspects to consider first:

#### [Server-side code](#Server-side+code)

In this case, the server-side code is part of the platform data type definitions. For the .NET Framework, it's the Dictionary data type (note that the namespace is System.Collections.Generic). For Java, the data type used is [Hashtable](https://docs.oracle.com/javase/8/docs/api/java/util/Hashtable.html). All this is reflected in the External object definition, in the .NET External Name and Java External Name properties. See the picture below.

#### [Client-side code](#Client-side+code+)

The Javascript code is defined in this case as an external source (Dictionary.js) and it is referenced in the [Javascript External Name property](https://wiki.genexus.com/commwiki/wiki?56499) of the External Object. As in Javascript, an object is an associative array (called hash in some languages); it stores key-value pairs, so the JS source uses the [Javascript object key list](https://developer.mozilla.org/es/docs/Web/JavaScript/Referencia/Objetos_globales/Object/keys) to implement the solution.

See the picture below that shows External Object properties definition:

`[imagen omitida: wiki id 31079]`

### [Client-side definition of the External Object](#Client-side+definition+of+the+External+Object)

From now on, focus on the client-side definition of the External Object. The Javascript source that defines the Dictionary object looks as follows (note the properties and method definitions to map them to the properties and methods definitions of the External Object afterward).

`[imagen omitida: wiki id 31081]`

To publish those properties and methods, you need to define them in the External Object.  
For example, the Keys property is defined as non-static, and its Javascript External Name property is set to **Keys**.  
Inside the Dictionary.js source, the **Keys** is defined as follows:

*get keys () {  
            return Object.keys(dictionary);  
        },*

Note that this is an example and the JS code can be programmed in many different ways.

`[imagen omitida: wiki id 31082]`

In the same manner, the methods to be published are defined in the External Object. For example, GetItem is a non-static method, mapped to the getItem Javascript method (through the Javascript External Name property).

*getItem: function (key) {  
            return dictionary[key];  
        },*

`[imagen omitida: wiki id 31083]`

### [How to use the External Object in GeneXus Code](#How+to+use+the+External+Object+in+GeneXus+Code)

First, to use the external JS resource, you have to add the reference to the HTML header, as shown in the code below:

```
Event Start
    Form.HeaderRawHTML += '<script type="text/javascript" src="Dictionary.js"></script>'
EndEvent
```

Since the following code runs client-side, the Javascript is invoked to execute it:

```
Event "X"
&Dictionary.SetItem("Evolution3CodeName", "Tilo") //&Dictionary is a variable based on Dictionary EO data type.
&Dictionary.SetItem("GeneXus15CodeName", "Salto")
EndEvent
```

And the following, by definition, runs server-side, so it executes Java or .NET depending on the platform.

```
Event "X"
For each Versions
//code here
Endfor 
&Dictionary.SetItem("Evolution3CodeName", "Tilo")
&Dictionary.SetItem("GeneXus15CodeName", "Salto")
EndEvent
```

Download sample from [Dictionary Sample](https://wiki.genexus.com/commwiki/wiki?31085,,).


|  |
| --- |
| **Backlinks** |
| [External Objects for Javascript](https://wiki.genexus.com/commwiki/wiki?31064) | [How to interact with the Window Object's Methods](https://wiki.genexus.com/commwiki/wiki?31086) | [HowTo: Execute GeneXus events from JS code using External Objects](https://wiki.genexus.com/commwiki/wiki?31075) |

---
