---
title: "User defined event"
source_id: 8044
source_url: https://wiki.genexus.com/commwiki/wiki?8044
genexus_version: "18"
---

# User defined event

Apart from the standard GeneXus events, you can define your own specific events called *User defined events*.

A User defined event triggers an action whenever a key or button is pressed, or when an Action is selected from the [Action Bar](https://wiki.genexus.com/commwiki/wiki?24521,,).

The shortcut key combination associated with the user event is optional, If no shortcut key is defined, the only way that the event is triggered is when user presses the associated button.

### [Syntax](#Syntax)

**Event** *user\_event\_name* [*key* ]  
**EndEvent**  
  
**Where:**  
*user\_event\_name*Name of the user event  
  
*key*Number of function key associated with the event. Optional.

### [Examples](#Examples)

#### [Web Panel](#Web+Panel)

You could have defined the following:

```
Event 'Create Supplier' 6
    &No = 0
    CreateSupplier.Call('INS',&No)
    refresh
EndEvent
```

This is a user-defined event called 'Create Supplier', and F6 will be the shortcut key that will trigger the Create Supplier event. This event calls the Suppliers transaction, which receives as parameters the Insert mode and a numeric variable whose assigned value is equal to 0. After calling the Transaction, the Refresh command is executed, indicating that the grid must be loaded again, since a new supplier has been added (otherwise the newly inserted supplier will not be displayed because this data did not exist when the first load was executed).

#### [Transaction](#Transaction)

Prints an invoice by pressing the corresponding button associated with the event.

```
Event 'Print Invoice'
    PrintInvoince.Call(InvoiceNumber)
Endevent
```

In Transactions you may select the level at which the event will be triggered by means of the [Level Sentence](https://wiki.genexus.com/commwiki/wiki?18742).

### [Scope](#Scope)

**Objects** [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)

### [See also](#See+also)

[Global Events](https://wiki.genexus.com/commwiki/wiki?31164)   
[Level Sentence](https://wiki.genexus.com/commwiki/wiki?18742) (only to be used in Transactions).


|  |
| --- |
| **Backlinks** |
| [Button control](https://wiki.genexus.com/commwiki/wiki?6011) | [Design Import option (GeneXus 18 Upgrade 4)](https://wiki.genexus.com/commwiki/wiki?55439) |
| [Event Execution comparison between Smooth and compatible models](https://wiki.genexus.com/commwiki/wiki?25296) | [Event Execution Scheme](https://wiki.genexus.com/commwiki/wiki?22472) | [Events in Transactions](https://wiki.genexus.com/commwiki/wiki?8042) | [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) |
| [HowTo:Develop a messaging web page](https://wiki.genexus.com/commwiki/wiki?22527) | [Load command](https://wiki.genexus.com/commwiki/wiki?8196) | [Load Command and Load Method in User Events](https://wiki.genexus.com/commwiki/wiki?22555) | [Runtime external object](https://wiki.genexus.com/commwiki/wiki?33076) |
| [Web Panels events](https://wiki.genexus.com/commwiki/wiki?8178) | [Web User Experience property](https://wiki.genexus.com/commwiki/wiki?22449) |

---
