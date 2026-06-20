---
title: "HowTo: Use Confirm method from Interop external object"
source_id: 17334
source_url: https://wiki.genexus.com/commwiki/wiki?17334
genexus_version: "18"
---

# HowTo: Use Confirm method from Interop external object

The Confirm method offered by the [Interop external object](https://wiki.genexus.com/commwiki/wiki?23734) prompts a message dialogue and makes it possible to execute actions according to the user's confirmation or denial of the message.

The method prompts a message dialogue with two buttons for the user to tap: one button to confirm and another button to cancel.

If the method is executed inside a [Composite command](https://wiki.genexus.com/commwiki/wiki?17389) and the user confirms the prompted message, the following actions in the Composite command are going to be executed. Otherwise, the execution of the Composite command stops.

`[imagen omitida: wiki id 54740]`

The method can be called with one parameter or with three parameters.

In the first case, the buttons' captions are not specified. In the second case, you can send the buttons' captions as parameters.

### [How it works](#How+it+works)

Below is an example of how the method is used and its behavior depending on the selected option. For this purpose, the [LightCRM KB](https://wiki.genexus.com/commwiki/wiki?21779,,) is used.

Suppose the insertion of a meeting has to be confirmed every time the user wants to do so. In this case, the Confirm method is going to be called in the same Event that is used for inserting new meetings.

First, in the WorkWith tab of the Meeting [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908), select the Section(General) node under the Detail node. Next, select the Events section.

`[imagen omitida: wiki id 54746]`

Since user confirmation is required when saving, edit the 'Save' event as shown below:

```
Event 'Save'
    Composite
        Interop.Confirm("Confirm this meeting?")
        GeneXus.SD.Actions.Save()
        return
    EndComposite
EndEvent
```

An alternative option (with specific buttons) may be as follows:

```
Event 'Save'
    Composite
        &HasConfirmed = Interop.Confirm("Confirm this meeting?", "Yes, sure", "No, thanks")

        If &HasConfirmed
            GeneXus.SD.Actions.Save()
            return
        Else
            Msg("Your meeting was not saved")
        EndIf
    EndComposite
EndEvent
```

`[imagen omitida: wiki id 45399]`


|  |
| --- |
| **Backlinks** |
| [Confirm function](https://wiki.genexus.com/commwiki/wiki?31634) | [Interop external object](https://wiki.genexus.com/commwiki/wiki?23734) |
| [Interop external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55183) |

---
