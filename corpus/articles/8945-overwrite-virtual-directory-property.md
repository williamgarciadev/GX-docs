---
title: "Overwrite virtual directory property"
source_id: 8945
source_url: https://wiki.genexus.com/commwiki/wiki?8945
genexus_version: "18"
---

# Overwrite virtual directory property

This Generator property allows you to define whether or not to attempt to create the Virtual directory upon compiling an object.

### [Values](#Values)

|  |  |
| --- | --- |
| **No** | The virtual directory is not created |
| **Yes** | The virtual directory is created when you build any object |

### [Description](#Description)

For example, when a .NET Web model is defined on a network (remote), the virtual directory is not created correctly due to insufficient rights. In this case, you can manually configure the Virtual directory with **servershare** and a username, and set the Overwrite Virtual Directory property to NO so that it is not overwritten during compilation.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply changes made by this property, do a Build with this Only of the object.

### [Scope](#Scope)

**Platforms:** Web(.Net)
