---
title: "Design System external object"
source_id: 49367
source_url: https://wiki.genexus.com/commwiki/wiki?49367
genexus_version: "18"
---

# Design System external object

Allows the application to configure, through code, aspects related to the Design System Object.

### [Properties](#Properties)

It doesn’t have any.

### [SetOption](#SetOption)

At runtime, it enables you to set the value of an option or parameter from those defined in a Design System Object. It has to be one of the values defined there. Thus, all the tokens conditioned with that value for the option will take the corresponding definitions.

Return value    None  
Parameters    Name: Character(20), Value: Character(20)

### [ClearOption](#ClearOption)

It clears the value that an option or parameter of the Design System Object had at runtime. As a result, only tokens that are not conditioned according to the option will have a value.

Return value    None  
Parameters    Name: Character(20)

### [Events](#Events)

It doesn’t have any.

Scope

Platforms: All.

### [See Also](#See+Also)

[Design System Tokens Options](https://wiki.genexus.com/commwiki/wiki?49381)

### [Availabilty](#Availabilty)

Since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?48684,,).


|  |
| --- |
| **Backlinks** |
| [Design System Tokens Options](https://wiki.genexus.com/commwiki/wiki?49381) |

---
