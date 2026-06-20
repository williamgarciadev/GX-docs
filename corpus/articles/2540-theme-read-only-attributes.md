---
title: "Theme Read-Only Attributes"
source_id: 2540
source_url: https://wiki.genexus.com/commwiki/wiki?2540
genexus_version: "18"
---

# Theme Read-Only Attributes

### [Introduction](#Introduction)

Normally, in order for users of Web applications to be able to quickly distinguish which fields are editable and which are read-only just by looking at them, the two types of fields have to be differentiated, for example, by giving editable fields a "3D" frame and read-only fields a "flat" frame.

### [Description](#Description)

A "ReadOnlyAttribute" class is automatically created, as a child of the "Attribute" class, so that the attributes or variables that will be read-only in runtime will be automatically associated to such class.  
  
The behavior differs depending on whether or not the attribute/variable is located in the form's flat level.

#### [Attribute/variable in the form's flat level](#Attribute%2Fvariable+in+the+form%27s+flat+level)

Upon associating a control to the "Attribute" class, if the control is editable, the generated application will use the "Attribute" class; if not, it will use the class known as "ReadOnlyAttribute."  
  
If the user assigns a class "X" and the control is read-only, it will be associated in runtime to the "ReadOnlyX" class.  
  
Every time you create a new class under Attribute (named X), the corresponding ReadOnlyX class is automatically created.

### [Attribute/variable in Grids/FreeStyle Grids](#Attribute%2Fvariable+in+Grids%2FFreeStyle+Grids)

Here the behavior changes depending on whether the attribute/variable in runtime is read-only or not, and whether it is associated with the default class or not.

Assuming that the attribute/variable is associated with the default class (which would be indicated in the property dialog of the variable with a black asterisk next to the class value):

* If it is not read-only (i.e., it is editable), in runtime it will inherit the settings of the class associated to the attribute/variable.
* If it is read-only, in runtime it will inherit the properties of the Grid in which it is located.

Assuming that the attribute/variable is associated to a non-default class (which would be indicated in the property dialog of the variable with a gray asterisk next to the class value):

* If it is not read-only (i.e., it is editable), in runtime it will take the settings of the associated class.
* If it is read-only, in runtime, it will inherit the properties of the "ReadOnlyX" class, where "X" is the class that was assigned during design.

Summarizing, if the attribute/variable within the [Grid](https://wiki.genexus.com/commwiki/wiki?24817) or [FreeStyle Grid](https://wiki.genexus.com/commwiki/wiki?6058) is associated to a default class, it will only take the settings of that class if it is editable in runtime. If it is not editable, it will inherit it from the Grid. If it is not associated with a default class, it will always take the settings of that class (whether it is editable or read-only; if read-only, it will remain associated to a ReadOnlyX)  
  
Important Note: If the "none" class is associated to the attribute/variable, the latter will alway inherit the configuration of the grid. For this reason, if it is editable, it is not possible to give it a "3D" effect.
