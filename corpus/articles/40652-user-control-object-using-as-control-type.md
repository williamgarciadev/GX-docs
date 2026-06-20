---
title: "User Control Object - Using as Control Type"
source_id: 40652
source_url: https://wiki.genexus.com/commwiki/wiki?40652
genexus_version: "18"
---

# User Control Object - Using as Control Type

Many times you want to create a [User Control object](https://wiki.genexus.com/commwiki/wiki?39356) and show it within the [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) of an attribute or variable.

To achieve it, you need to do the following:

**1)** Create a [User Control object](https://wiki.genexus.com/commwiki/wiki?39356)

**2)** Set its [Is Control Type property](https://wiki.genexus.com/commwiki/wiki?40584) = True

When you enable the [Is Control Type property](https://wiki.genexus.com/commwiki/wiki?40584), the [Data Type Filter property](https://wiki.genexus.com/commwiki/wiki?40654) appears in order to indicate the data type for which this control is appropriate.

**3)** Indicate which [HTML element](https://www.w3schools.com/html/html_elements.asp) of the control Layout is the one that maintains the value of the control. To carry out this, in the **Screen Template** tab of the user control, you have to include the expression {{DataElement}} in the desired tag:

```
<input type="number" {{DataElement}}></input>
```

This means that the [value property](https://www.w3schools.com/tags/att_value.asp) of the input [HTML element](https://www.w3schools.com/html/html_elements.asp) will have the value of the User Control created.  
  
Note: Only the HTML elements that natively support the value property can "maintain" the control value (the HTML Tags available for the value property are as follows: <button>, <input>, <li>, <option>, <progress>, <param>). Also, HTML elements that receive the value from a JQuery plugin may be used to maintain the value of a User Control.

## [Assigning a value to the User Control](#Assigning+a+value+to+the+User+Control)

In order to set a value for the control, you only need to set a value for the associated variable or attribute.

## [Reading a User Control value](#Reading+a+User+Control+value)

To read the control value, simply access the value of the associated variable or attribute.

## [Example](#Example)

This example contains two [User Control object](https://wiki.genexus.com/commwiki/wiki?39356)s and designs a login for an application without considering security.

There is a LogIn [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) that asks for the following data:

* Company
* Username
* Password

These data are entered through three variables included on the screen and each one has its Control Type property configured with the pre-designed User Control objects. After the user completes the data and presses the Confirm button, another Web Panel is called to display the data sent by parameter.

[Download the xpz file with the User Control Object and DataElement usage example](https://wiki.genexus.com/commwiki/wiki?48415,,)


|  |
| --- |
| **Backlinks** |
| [Toc:Design Systems](https://wiki.genexus.com/commwiki/wiki?40108) |

---
