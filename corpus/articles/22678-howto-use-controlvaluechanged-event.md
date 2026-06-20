---
title: "HowTo: Use ControlValueChanged event"
source_id: 22678
source_url: https://wiki.genexus.com/commwiki/wiki?22678
genexus_version: "18"
---

# HowTo: Use ControlValueChanged event

For this tutorial the [LightCRM (X Evolution 2)](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?21779,,) sample will be used to exercise the use of the [ControlValueChanged event](https://wiki.genexus.com/commwiki/wiki?22676).

The objective is that the insertion of the data of a Contact in this app should be done progressively, only when you completed the previous data the next inputs are going to appear.

### [Step1: Prepare the Screen](#Step1%3A+Prepare+the+Screen)

On the object WorkWithDevicesContact Section General Edit layout, set the property visible to false for the following controls.

Table2, Table3, ContactEmail, CompanyName.

After adding the ContactName automatically the ContactEmail will appear and after completing the ContactEmail the CompanyName attribute will appear.

### [Step2: Add the behavior](#Step2%3A+Add+the+behavior)

Program the following events:

```
Event ContactName.ControlValueChanged
    Composite
        &isEmpty = IsEmpty(ContactName)
        if &isEmpty
           Msg("You have to complete the Contact Name to continue")
        else
           Table2.Visible = 1
           ContactEmail.Visible = 1
        endif
    EndComposite
EndEvent
```

```
Event ContactEmail.ControlValueChanged
    Composite
        &isEmpty = IsEmpty(ContactEmail)
        if &isEmpty
           Msg("A Complete email is required to continue")
        else
           Table3.Visible = 1
           CompanyName.Visible = 1
        endif
    EndComposite
EndEvent
```

The IsEmpty Procedure has the following source:

```
if &varChar.IsEmpty()
   &bollIsEmpty = true
else
   &bollIsEmpty = false
endif
```

And rules:

```
parm(in: &varChar, out: &bollIsEmpty);
```

### [End](#End)

Done! The example can be accessed from [LightCRM (X Evolution 2)](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?21779,,).

The user is forced to enter a Name and Email to be able to complete all the form of the Contact. This is one of the many scenarios in which the Control Value Changed Event can be used.


|  |
| --- |
| **Backlinks** |
| [ControlValueChanged event](https://wiki.genexus.com/commwiki/wiki?22676) |

---
