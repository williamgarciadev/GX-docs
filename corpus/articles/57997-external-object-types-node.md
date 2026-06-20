---
title: "External Object Types Node"
source_id: 57997
source_url: https://wiki.genexus.com/commwiki/wiki?57997
genexus_version: "18"
---

# External Object Types Node

Defines generic and flexible data structures within the context of an [External Object](https://wiki.genexus.com/commwiki/wiki?5669).

### [Description](#Description)

Types can be dynamically adapted to different data types without requiring specific definitions for each case. That is, the same Type can be used with different data types, which adds a layer of flexibility and reusability to the design of External Objects.

Each Type in an External Object has properties such as [Property Name](https://wiki.genexus.com/commwiki/wiki?57843), [Valid Types](https://wiki.genexus.com/commwiki/wiki?57844), [Allow Collection](https://wiki.genexus.com/commwiki/wiki?57845), and [Default Type](https://wiki.genexus.com/commwiki/wiki?57846).

To define a Types node, set the **Native Object** value in the [Type property in External Object](https://wiki.genexus.com/commwiki/wiki?53690).

### [Sample](#Sample)

Suppose you are developing an application in GeneXus and you need to implement a generic dictionary that can dynamically adapt to different types of data. To achieve this, you use External Objects.

First, create an External Object manually from the [New object dialog](https://wiki.genexus.com/commwiki/wiki?9931), called GenericDictionary, and set the value **Native Object** in the **Type Property**.

Next, define the following elements:

* Types: Create a generic type called TypeKey for the keys and another generic type called TypeValue for the values.
* Properties: Add properties called Keys and Values of type TypeKey and TypeValue, respectively, that store the dictionary elements.
* Methods: Implement the methods to add, delete, and get items from the dictionary.
* Events: It is not necessary to define any.

The GenericDictionary structure is as follows:

`[imagen omitida: wiki id 57999]`

Note that you can reference TypeKey and TypeValue within the same External Object.

The values set for the TypeKey properties are shown in the following image:

`[imagen omitida: wiki id 58000]`

After saving the created External Object, you can define a variable of the GenericDictionary data type. For example, in a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) define a &Data variable of GenericDictionary type.

Make sure to define Key Type and Value Type as required:

`[imagen omitida: wiki id 58002]`

Once you have defined the &Data variable, you can access its properties and methods by adding a period:

`[imagen omitida: wiki id 58001]`

**Note**: Keep in mind that collections of an External Object with defined Types are not allowed.

### [Availability](#Availability)

This functionality is available as Beta since [GeneXus 18 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?54244).


|  |
| --- |
| **Backlinks** |
| [Allow Collection property](https://wiki.genexus.com/commwiki/wiki?57845) | [Default Type property](https://wiki.genexus.com/commwiki/wiki?57846) | [Dictionary External Object](https://wiki.genexus.com/commwiki/wiki?58246) |
| [Category:External Object](https://wiki.genexus.com/commwiki/wiki?5669) | [Property Name property](https://wiki.genexus.com/commwiki/wiki?57843) | [Valid Types property](https://wiki.genexus.com/commwiki/wiki?57844) |

---
