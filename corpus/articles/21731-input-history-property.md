---
title: "Input History property"
source_id: 21731
source_url: https://wiki.genexus.com/commwiki/wiki?21731
genexus_version: "18"
---

# Input History property

Assists the application user to enter information in a field, by remembering the last values entered in it so the user can select one of those and save them to input information.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453)  
**Controls:** Attribute/Variable (Control Type: Edit)

### [Description](#Description)

The default value for this property is True.

This property indicates whether to assist the application user, or not, in entering information in a field. This is done by remembering what has been entered in a field on a screen. By recalling this, the next time a user enters information in that field the app will show the last values entered, allowing the user to select one of the previous values and save them to input information.

### [Considerations](#Considerations)

* This property doesn't work for Date-based fields.
* When the [Is Password property](https://wiki.genexus.com/commwiki/wiki?8803) is set to yes, the Input History property is disabled.
* A value is "saved" for the input history when an action is executed on the screen the field is on.

### [Samples](#Samples)

`[imagen omitida: wiki id 21732]`
