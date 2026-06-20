---
title: "Composite examples"
source_id: 15551
source_url: https://wiki.genexus.com/commwiki/wiki?15551
genexus_version: "18"
---

# Composite examples

This document shows examples of [Composite command](https://wiki.genexus.com/commwiki/wiki?17389).

### [Samples](#Samples)

**Example 1**

This example shows how GeneXus automatically creates the Delete system event for the Neighborhood [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908).

```
Neighborhood
{
   NeighborhoodId*
   NeighborhoodName
   NeighborhoodInfo
}
```

```
Event 'Delete'
    Composite
        WorkWithDevicesNeighborhood.Neighborhood.Detail.Delete(NeighborhoodId)
        Return
   EndComposite
EndEvent
```

When the end user clicks on the Delete button, the Neighborhood Transaction’s WorkWithDevicesNeighborhood calls the Delete function associated with it. If for whatever reason the deletion is not successful, the [Return command](https://wiki.genexus.com/commwiki/wiki?31353) that follows will not be executed (that is to say, it won’t return to the List) and the control will remain in the View.

**Example 2**

This example solves the update of a client's e-mail, sending that client an SMS if the action is successful. The following Transaction is going to be used:

`[imagen omitida: wiki id 17352]`

1. Create a Procedure that receives a &ClientId and &ClientEMail by parameter, to then update the email and return &messages from the standard Messages domain:

```
For each
    where ClientId    = &ClientId
          ClientEMail = &ClientEmail
    when duplicate
          &Message.Type = MessageTypes.Error
          &Message.Description = "Email duplicated" + str(&ClientId)
          &Messages.Add(&Message)
          return
EndFor
```

The ClientEmail is a candidate key (unique), and this Procedure has to update it. If another e-mail has the same value, it is reported as an error in the &messages variable because "when duplicate" is an exception, and Composite only checks for exceptions.

2. [Applying Work With Pattern](https://wiki.genexus.com/commwiki/wiki?15975) to the Client Transaction.

Add the actions:

a. Add a new action called CheckEMail by right-clicking and selecting Insert Action.

b. Next, set the button’s caption with CheckEMail.  
  
`[imagen omitida: wiki id 17292]`

c. This Procedure receives &ClientId and &ClientEMail by parameter.

3. Now, the user event has to be coded. Using a context menu, select Go To Event and write this code:

```
Event 'UpdateEmail'
    Composite
           UpdateEMail.Call(ClientId,&ClientEmail,&messages)
           Interop.SendMessage("Your Email has been updated successfully in my database",ClientMobilePhone)
    EndComposite
EndEvent
```

As you can see, a code block called [Composite command](https://wiki.genexus.com/commwiki/wiki?17389) has been opened. Its code will be executed in sequence, like a composition.

The first instruction makes the call to the created Procedure and then Interop is invoked to send a notification to the device. See [HowTo: Use SendMessage method from Interop external object](https://wiki.genexus.com/commwiki/wiki?15528) for more information.

If an error occurred in the call to the UpdateEmail Procedure, the control wouldn’t move forward to Interop and would return as if the Exit command had been executed instead. Also, it would continue to do so if there were a larger sequence of actions.

Writing:

```
Composite
    UpdateEMail.Call(ClientId,&ClientEmail,&Messages)
    Interop.SendMessage("Your Email has been updated successfully in my database",ClientMobilePhone)
EndComposite
```

...is equivalent to:

```
UpdateEMail.Call(ClientId,&ClientEmail,&Messages)
For &message in &messages
    If &message.Type = MessageTypes.Error
        msg(&message.Description)
        Exit
    else
        Interop.SendMessage("Your Email has been updated successfully in my database",ClientMobilePhone)
        Exit
    EndIf
EndFor
```

**Note:** It’s important to remember that, when calling a Procedure, the &Messages variable doesn’t have to be specifically mentioned. However, in the Procedure it has to be declared as OUTPUT and its name has to be exactly "Messages".

```
Parm(parm1, parm2, …parmn, Out:&Messages);
```

### [Batch operations](#Batch+operations)

As usual, calls to a [Business Component](https://wiki.genexus.com/commwiki/wiki?5846) in batch mode within the [Composite command](https://wiki.genexus.com/commwiki/wiki?17389) are made with a variable based on the Business Components, such as an update:

```
Composite
    &Cliente.Load(5)
    &Cliente.Name = "Wayne, Bruce"
    &Cliente.Save()
EndComposite
```

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Events in mobile applications](https://training.genexus.com/en/learning/courses/genexus-for-mobile/mobile-applications-with-genexus-course-v16/events-in-mobile-applications-6103211?p=3673)


|  |
| --- |
| **Backlinks** |
| [Calling objects from Menu Events](https://wiki.genexus.com/commwiki/wiki?17392) | [Composite command](https://wiki.genexus.com/commwiki/wiki?17389) |
| [Tabs offered in Panel and Work With objects](https://wiki.genexus.com/commwiki/wiki?16847) |

---
