---
title: "Theme Value Settings"
source_id: 2541
source_url: https://wiki.genexus.com/commwiki/wiki?2541
genexus_version: "18"
---

# Theme Value Settings

Edit Controls in Free Style Grids

If there is an edit control within the [Free Style Grid](https://wiki.genexus.com/commwiki/wiki?6058), the order of precedence regarding the configuration of the controls in runtime is:

1. Configuration of the edit control, either with the configuration values given in the control itself, or through a class associated to the control.
2. Configuration of the Free Style grid cell.
3. Configuration of the Free Style grid itself, with the values given either in the control or in a class associated to the Free Style grid (that is to say, LinesBackColor, LinesBackColorEven properties, etc.).

Important Note:  If you want the "edit control" in the Free Style grid to inherit the context settings, "the none" class has to be specified, and the rest of the configuration values must be set to default. If the control is read-only and has an associated default class, it also inherits the settings of the grid.

### [Fill Property of Attributes/Variables](#Fill+Property+of+Attributes%2FVariables)

If the fill property of an attribute/variable has a False value, the backcolor given in the control's associated class is not considered (i.e., in that case the backcolor is inherited from the context in which the control is found). If the value of the property is set to True, and the backcolor has a default value in both the control and class, (it does not have a value explicitly associated to it) the backcolor is inherited from the context (i.e., from the backcolor of the attribute/variable container control).
