---
title: "ControlValueChanging event"
source_id: 35768
source_url: https://wiki.genexus.com/commwiki/wiki?35768
genexus_version: "18"
---

# ControlValueChanging event

Can be used on Applications in order to execute some code while the end user is entering input data. Its aim is giving constant feedback to the user (e.g. UI effects).

### [Syntax](#Syntax)

**Event** *VarOrAtt***.ControlValueChanging(***&newVarOrAtt***)**  
*Event\_code*  
**EndEvent**

Where:

*VarOrAtt*:

Any variable or attribute control that is on a layout as an editable field (see Scope section). The value of this control will be the value before the change.

*&newVarOrAtt*:

A variable with the same type as *VarOrAtt*. Its value will be the next value that will have the *VarOrAtt* once it has been changed*.*

*Event\_code*

The code that will be executed when the event triggers (it is like any other [User Event in Smart Devices](https://wiki.genexus.com/commwiki/wiki?17614)).

### [Example](#Example)

Suppose a chat scenario where we have a button for recording while a text field is empty. If the end user starts writing on the field, the button will change for sending the message. This effect can be done very simply by adding the ControlValueChanging event in the following way.  
`[imagen omitida: wiki id 35772]`

First, we design the chat panel properly.  
`[imagen omitida: wiki id 35773]`

Then, we write the following event associated with the text-field.

```
Event &vMessage.ControlValueChanging(&vMessageNew)
    Composite
        &MessageLen = &vMessageNew.Length()
        SendButton.Visible = &MessageLen > 0
        RecButton.Visible  = &MessageLen = 0    
    EndComposite
Endevent
```

Note that there is no need for checking the value of &vMessage (which in this context is a control, not a variable), we only check the &vMessageNew variable value.

There are a lot of scenarios that can be resolved by using this event. For example, making an automatic validation of a field once a complete sequence of tokens is inserted (and if it is ok, for example, setting the focus in the next field).

### [Notes](#Notes)

* The event not only detects when the user is typing in the text field but also detects when the user pastes some content from the clipboard or deletes some selected text. In the example exposed, use [Length method](https://wiki.genexus.com/commwiki/wiki?12704) or [IsEmpty method](https://wiki.genexus.com/commwiki/wiki?9645) will have the same behavior. But, if the developer wants to operate depending on the difference of at least one character, the first option is better. A simple usage example is for updating how many characters left to fulfill a message. In such case, will only we to add a single line to the above code as follows and take some actions with that value.

  ```
  &HowManyLeft = 256 - &MessageLen
  ```
* Remember that *VarOrAtt* refers to a control, consequently, its value won't be accessible until the user ends editing (and the [ControlValueChanged event](https://wiki.genexus.com/commwiki/wiki?22676) will be triggered).
* If the field value is changed programmatically (i.e. by coding), the *ControlValueChanging* event is not going to be executed (e.g. multiple assignations of the same variable on another User event).

### [Restrictions](#Restrictions)

* Android does not differentiate the values of *VarOrAtt* and *&newVarOrAtt*, both will be the same.
* in Web, parameter &newVarOrAtt is ignored.

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Controls** | Attribute control, Variable control |
| **Data types** | Numeric, Character, VarChar, LongVarChar |
| **Interfaces** | Smart Devices, Web |

### [Availability](#Availability)

This feature is available as of [GeneXus 15 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?34646,,) in iOS and Android, and as of [GeneXus 15 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?35908,,) in Web too.

### [See also](#See+also)

* [ControlValueChanged event](https://wiki.genexus.com/commwiki/wiki?22676)
