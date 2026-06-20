---
title: "Accessible Name property (GeneXus 18 Upgrade 8 or prior)"
source_id: 57813
source_url: https://wiki.genexus.com/commwiki/wiki?57813
genexus_version: "18"
---

# Accessible Name property (GeneXus 18 Upgrade 8 or prior)

Indicates the way in which an Accessible Name (label for an element) will be completed.

### [Values](#Values)

|  |  |
| --- | --- |
| **Based on Control** | The Accessible Name's value is taken from the description of a Text Block control. |
| **Custom** | The Accessible Name's value is entered directly by setting it. This is the default value. |

### [Scope](#Scope)

**Generators:** [Angular](https://wiki.genexus.com/commwiki/wiki?42550)  
**Controls:** Attribute/Variable, [Button](https://wiki.genexus.com/commwiki/wiki?6011), [Canvas](https://wiki.genexus.com/commwiki/wiki?22452), [Flex](https://wiki.genexus.com/commwiki/wiki?40521), [Grid](https://wiki.genexus.com/commwiki/wiki?24817), [Image](https://wiki.genexus.com/commwiki/wiki?5939), [Tab](https://wiki.genexus.com/commwiki/wiki?25623), [Table](https://wiki.genexus.com/commwiki/wiki?6001)

### [Description](#Description)

When the Accessible Name property is set to "Custom", the [Accessible Name Custom property](https://wiki.genexus.com/commwiki/wiki?55469) is offered to complete the Accessible Name.

When the Accessible Name property is set to "Based on Control", the [Accessible Name Control property](https://wiki.genexus.com/commwiki/wiki?55456) is offered to select the Text Block whose description will be used as the Accessible Name.

### [Accessibility problems that are solved with this property and its related properties](#Accessibility+problems+that+are+solved+with+this+property+and+its+related+properties)

The following typical problems can be solved by using this property and its related properties:

#### [Buttons with only an image](#Buttons+with+only+an+image)

When Button controls are used only with images and with empty Captions, they do not have a visible description for the action they represent to screen readers. Indicating an Accessible Name with the action they represent solves the problem.

#### [Buttons with a Caption that does not describe the action](#Buttons+with+a+Caption+that+does+not+describe+the+action)

When Button controls have captions that do not provide information about the action that is performed when the button is pressed, these controls do not correctly describe what they represent to screen readers.

An example of this is a "user configuration" button, where the Caption property of the button is the user's initials. Using "User Configuration" as the Accessible Name will allow screen readers to correctly understand the action the button performs when pressed, while visually maintaining the user's initials.

#### [Editable variables that do not have a Label](#Editable+variables+that+do+not+have+a+Label)

When using an Attribute/Variable control with properties Read only = False and Label Position = None, these controls do not have a visible description.

Adding the Accessible Name for these controls provides descriptions for them.

#### [Containers with Accessible Role = Region](#Containers+with+Accessible+Role+%3D+Region)

Containers that have Accessible Role = Region need to have an Accessible Name specified in order to describe the contents of the region. In this case, it is preferable to use the Accessible Name = "Based on Control" when the region description is contained in a Text Block control.

**Note**: This property does not impact in any way the performance or functionality of the controls in which it is used; it only provides semantics for them.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

In [Sample PlantCare](https://apps-angular.genexus.com/Plantcare2/PlantCareHome/PlantCareHome-Level_Detail), the following Accessible Names are visually highlighted in the controls:

`[imagen omitida: wiki id 55662]`

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239).

### [See Also](#See+Also)

[Accessible Role property](https://wiki.genexus.com/commwiki/wiki?55453)
