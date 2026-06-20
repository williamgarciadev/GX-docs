---
title: "Font All Caps property (GeneXus 18 Upgrade 6 or prior)"
source_id: 56518
source_url: https://wiki.genexus.com/commwiki/wiki?56518
genexus_version: "18"
---

# Font All Caps property (GeneXus 18 Upgrade 6 or prior)

Shows text in All Caps.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453)  
**Level:** [Theme Class](https://wiki.genexus.com/commwiki/wiki?6246)

### [Description](#Description)

This property is available for the Button and Tab Page [Theme Classes](https://wiki.genexus.com/commwiki/wiki?6246).

It sets whether the text is shown using all capital letters or not. Therefore, when the property is set to True, all letters are capitalized, and when the property is set to False, text appears as it was written or stored.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

In the following [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) there are 2 buttons:

`[imagen omitida: wiki id 41534]`

* One button has:
  1. Its [Caption property](https://wiki.genexus.com/commwiki/wiki?4633) set to 'All Caps'
  2. Its [Class property](https://wiki.genexus.com/commwiki/wiki?8741) set to Button1 (and the Button1 Theme Class has its **Font All Caps property** set to True).
* Another button has:

1. Its [Caption property](https://wiki.genexus.com/commwiki/wiki?4633) set to 'Camel Case'
2. Its [Class property](https://wiki.genexus.com/commwiki/wiki?8741) set to Button2 (and the Button2 Theme Class has its **Font All Caps property** set to False).

At runtime, the caption of the first button is 'ALL CAPS' and the other is 'Camel Case':

`[imagen omitida: wiki id 41535]`

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770).
