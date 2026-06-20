---
title: "Columns Grids property"
source_id: 8753
source_url: https://wiki.genexus.com/commwiki/wiki?8753
genexus_version: "18"
---

# Columns Grids property

Allows indicating how many columns the FreeStyle Grid is going to have at execution time.

### [Syntax](#Syntax)

**control.** Columns = value

### [Description](#Description)

If you enter a value other than 1, the Freestyle Grid is going to show the records in as many columns as it was specified in the property. If the property value is 0, the Freestyle Grid will have as many columns as records result from the associated query. This property value is 1.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies both at run-time and at design-time.

### [Scope](#Scope)

**Objects:** Transaction, Web Panel  
**Platforms:** Web(.Net, Java)  
**Controls:** FreeStyle Grid
