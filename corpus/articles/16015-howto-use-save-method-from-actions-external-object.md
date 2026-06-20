---
title: "HowTo: Use Save method from Actions external object"
source_id: 16015
source_url: https://wiki.genexus.com/commwiki/wiki?16015
genexus_version: "18"
---

# HowTo: Use Save method from Actions external object

The Save method offered by the [Actions external object](https://wiki.genexus.com/commwiki/wiki?31350) allows you to execute a Save in the edit form on the end user's device. This method doesn’t expect any parameter.

`[imagen omitida: wiki id 57255]`

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908):

```
Customer
{
  CustomerId*
  CustomerName
  CustomerLastName
  CustomerBirthDate
  CustomerMsg
}
```

Apply the [Work With pattern](https://wiki.genexus.com/commwiki/wiki?15974) to the Customer Transaction:

`[imagen omitida: wiki id 57256]`

The objective in this example is to Save a new customer record and, after that, to invoke a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) that updates a field of the same record.

To achieve this, define the following Procedure (called "UpdatesCustomerMsg"):

Procedure Source:

```
For Each Customer
      CustomerMsg = "THE NEW MESSAGE"
EndFor
```

Procedure Rules:

```
Parm(CustomerId);
```

The next step consists of adding, **in the Edit Layout** (you can use the Save method only there), a new button to the Application Bar:

`[imagen omitida: wiki id 57259]`

and defining under the last predefined event:

`[imagen omitida: wiki id 57257]`

the event associated with that button:

```
Event 'Save and Update Msg'
    Composite
	   Actions.Save()
	   UpdatesCustomerMsg(CustomerId)  //Your Procedure call
    EndComposite
EndEvent
```

At runtime ―regardless of the message entered by the end user for the customer―, when the "Save and Update Msg" button is pressed, the customer record will be saved, and the "UpdatesCustomerMsg" Procedure will be called after that. Therefore, the CustomerMsg attribute will be updated for the new customer.

**Note**:  When generating the app in Apple, the button corresponding to the proposed example will not appear. This is because certain actions (such as Save and Cancel) are handled according to Apple's guidelines so that they have a native appearance and behavior. As a result, Cancel appears on the top left and Save on the top right; other special cases are Update and Delete. Therefore, duplications and/or customizations of these actions are ignored and will not be displayed at runtime.


|  |
| --- |
| **Backlinks** |
| [Actions external object](https://wiki.genexus.com/commwiki/wiki?31350) | [HowTo: Use the Cancel Method from Actions in Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?18363) |

---
