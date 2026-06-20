---
title: "Enable Show Password property"
source_id: 35577
source_url: https://wiki.genexus.com/commwiki/wiki?35577
genexus_version: "18"
---

# Enable Show Password property

Its purpose is to show a button to the right of the field that allows viewing the user's password in plain text.

### [Syntax](#Syntax)

**control.** EnableShowPassword   

Type returned: Boolean

**Where**  
*control*Name of the edit control.

Values

|  |  |
| --- | --- |
| **False (default)** | The button that allows showing the password in plain text and vice versa is not displayed. |
| **True** | A button is displayed next to the password to show it in plain text and vice versa. |

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Description](#Description)

It applies to fields in a form of editable type (not read-only) when the [Is Password property](https://wiki.genexus.com/commwiki/wiki?8803) is enabled. Pressing the button when the password is in plain text hides it (asterisks are displayed instead of characters).

`[imagen omitida: wiki id 35630]`

#### [Tips](#Tips)

Remember that If you use a Numeric-based field in your password, by default its picture will be "ZZZ**9**". In such case, you will see a dot symbol like this at rutnime:

`[imagen omitida: wiki id 36205]`

In order to fix this problem, change the Picture property value of that Numeric field to "ZZZ**Z**".

`[imagen omitida: wiki id 36206]`

Design Time

`[imagen omitida: wiki id 35605]`

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [Availability](#Availability)

This property is available since [GeneXus 15 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?34646,,).

### [Scope](#Scope)

**Objects:** Panel for Smart Devices, Transaction, Web Panel, Work With for Smart Devices, Menu for Smart Devices  
**Platforms:** Web(.Net, Java), Smart Devices(Android)
