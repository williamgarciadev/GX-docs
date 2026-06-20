---
title: "Calling objects from Menu Events"
source_id: 17392
source_url: https://wiki.genexus.com/commwiki/wiki?17392
genexus_version: "18"
---

# Calling objects from Menu Events

This document will guide you through an easy example of the objects that may be called, and how to call them from a [Menu object](https://wiki.genexus.com/commwiki/wiki?16321).

You can call different objects and perform numerous different actions from a Menu. Each option in a Menu can be created by right-clicking on the root\_element/Add/Item.

`[imagen omitida: wiki id 17400]`

An event will be triggered when a user taps on one of the items in the Menu. So, you want to have an Event for each Item.

To add an Event (temporary restriction) go to the Events tab and add a new event with a unique name.

To link an Event to the Item of the Menu you have the [Name property](https://wiki.genexus.com/commwiki/wiki?6985). The value of this property will be the name of the event that will be executed when the user taps on that option.

The first distinction is that an event in a Menu can call one object or make a [composite](https://wiki.genexus.com/commwiki/wiki?17389) call. It's easy to call an object, with the user tapping on the icon/tab/line (to see different ways to show a Menu read [Several ways to show a Menu](https://wiki.genexus.com/commwiki/wiki?16098)) of the item, to invoke the event and call only one object. The Composite call can help you add a more sophisticated behavior to your Menu.

### [Call Work With Pattern Instances with associated Business Component](#Call+Work+With+Pattern+Instances+with+associated+Business+Component)

For this tutorial, the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) will be used.

`[imagen omitida: wiki id 17404]`

Apply the [Work With pattern and Work With object](https://wiki.genexus.com/commwiki/wiki?15974) to the Transaction (for further information see [Applying Work With Pattern](https://wiki.genexus.com/commwiki/wiki?15975)).

Let's start with a basic example. Suppose you want an item in your Menu to call a [Work With List Node](https://wiki.genexus.com/commwiki/wiki?15984).

a. Now create a new Event on the Events tab with the following code:

```
Event 'WWSDList'
    WorkWithDevicesPerson.Person.List()
EndEvent
```

Add a new item to your Menu as shown in the image above.

For the [Name property](https://wiki.genexus.com/commwiki/wiki?6985) use the event name, in this case: WWSDList.

By tapping on this element at run-time, you'll be able to go to the list of Persons.

`[imagen omitida: wiki id 17395]`

b. Now let's call the Detail view of a WorkWith Pattern. You want to call the View Mode of the Section (General) in the [Detail node](https://wiki.genexus.com/commwiki/wiki?20433), so you can view the details on a Person.

You have to take into consideration that the Detail node of an instance of a WorkWith with associated [BC](https://wiki.genexus.com/commwiki/wiki?2416) receives a parameter; the parameter is the [PK](https://wiki.genexus.com/commwiki/wiki?20770) of the [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908). So, in your call, you have to pass the value of the PK of the Person you want to update. In this case, you will make the Event as follows:

```
Event 'WWSDDetail'
    WorkWithDevicesPerson.Person.Detail(2)
EndEvent
```

Add a new item to the Menu and set the [Name property](https://wiki.genexus.com/commwiki/wiki?6985) with WWSDDetail.

`[imagen omitida: wiki id 17396]`

### [Call the BCs of a WW in their different Modes (Insert, Update, Delete)](#Call+the+BCs+of+a+WW+in+their+different+Modes+%28Insert%2C+Update%2C+Delete%29)

Sometimes you need or want to call a Transaction directly in one of the modes that the Transaction can be called (Insert, Update, Delete). To do so, the event should be as follows:

```
Event 'TRNInsert'
    WorkWithDevicesPerson.Person.Detail.Update(2)
EndEvent
```

If you change the last part you can invoke the Transaction in Insert mode or Delete mode.

`[imagen omitida: wiki id 17397]`

### [Call any action of the Smart Device API](#Call+any+action+of+the+Smart+Device+API)

Calling objects from the Smart Device API is another way to use your Menu Items.

For this example, you will call the SendMessage method from the Interop External Object. (For more information on the Smart Device API object, read the document [HowTo: Use SendMessage method from Interop external object](https://wiki.genexus.com/commwiki/wiki?15528)).

The event programming should be:

```
Event 'SDApiCall'
    Interop.SendMessage("A message", 1234342)
EndEvent
```

Set the Name property with SDApiCall. This will invoke the SendMessage method with the parameters specified.

`[imagen omitida: wiki id 17398]`

### [Call other Menus](#Call+other+Menus)

Sometimes you can have many Menus, where one of them can call another.

Create a new Menu; set the Name property with SubMenu and save it.

Note: it makes no difference if there are no items on that Menu.

The event will be as follows:

```
Event 'SubMenu' 
    SubMenu.Call()
EndEvent
```

Add a new Item to the Menu and set the Name property with SubMenu.

### [Call an Entry Panel with no Business Component](#Call+an+Entry+Panel+with+no+Business+Component)

Let's create a new WorkWith object as shown in the following image:

`[imagen omitida: wiki id 17401]`

Create a new Event with the following code:

```
Event 'EntryPanel'
    EntryPanel.EntryPanel.Detail.Edit()
EndEvent
```

Lastly, add a new item to the Menu and set the Name property with EntryPanel.

`[imagen omitida: wiki id 17402]`

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Grammar of Events on the Client Side and Composite Command](https://training.genexus.com/en/learning/courses/genexus-for-mobile/mobile-applications-with-genexus-course-v16/grammar-of-events-on-the-client-side-and-composite-command?p=3682)  
`[imagen omitida: wiki id 20668]` [Events in Mobile Applications](https://training.genexus.com/en/learning/courses/genexus-for-mobile/mobile-applications-with-genexus-course-v16/events-in-mobile-applications-6103211?p=3673)

### [See also](#See+also)

[Composite examples](https://wiki.genexus.com/commwiki/wiki?15551)


|  |
| --- |
| **Backlinks** |
| [Category:Menu object](https://wiki.genexus.com/commwiki/wiki?16321) |

---
