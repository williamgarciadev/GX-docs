---
title: "Show form property"
source_id: 13435
source_url: https://wiki.genexus.com/commwiki/wiki?13435
genexus_version: "18"
---

# Show form property

Specifies the moment when the object’s form is to be displayed. The options are to display them either before or after triggering event start.

### [Values](#Values)

|  |  |
| --- | --- |
| **After Start Event** | Specifies that the form is displayed after the object’s event start is triggered. |
| **Before Start Event** | Specifies that the form is displayed before the object’s event start is triggered. |
| **Use Environment property value** | This is the default value, which indicates the moment when the form will be displayed, as defined by the Show form model property. |

### [Description](#Description)

In some objects, the form is “set up” according to values received as parameters or similar situations. It is, therefore, very common for Event Start to turn off, switch on, move and change form controls, etc. It is convenient to perform these tasks before the user has a view of the form; otherwise, the user will witness how the form undergoes changes. To do so, you are provided with this property that will determine what should be done first, either drawing the form or executing event start.

#### [Note](#Note)

The property at the object level has priority over the one specified at the Environment level.

### [Scope](#Scope)

**Objects:** Transaction  
**Platforms:** Web(.Net, Java)
