---
title: "Map Type property in attributes/variables based on Geography data types"
source_id: 41338
source_url: https://wiki.genexus.com/commwiki/wiki?41338
genexus_version: "18"
---

# Map Type property in attributes/variables based on Geography data types

Sets the type of map to display.

### [Values](#Values)

|  |  |
| --- | --- |
| **Hybrid** | Displays a mixture of normal and satellite views. |
| **Satellite** | Displays Google Earth satellite images. |
| **Standard** | Displays the default road map view. |

### [Scope](#Scope)

**Controls:** Attribute/Variable   
**Level:** [Attribute](https://wiki.genexus.com/commwiki/wiki?7240), [Variable](https://wiki.genexus.com/commwiki/wiki?7375)

### [Description](#Description)

The Map Type property applies to attributes/variables based on the Geography, Geopoint, Geoline, etc. data types.

The attribute/variable control can be inserted in [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)s and [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)s.

This property determines the type of map that can be displayed. It is an interface that defines the display and usage of map tiles; the different Values are given by the Maps Platform provided.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at runtime.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build with this Only](https://wiki.genexus.com/commwiki/wiki?5693) of the object.
