---
title: "Flips for Right to Left property"
source_id: 42948
source_url: https://wiki.genexus.com/commwiki/wiki?42948
genexus_version: "18"
---

# Flips for Right to Left property

Boolean value that indicates whether the image should be flipped in a right-to-left layout.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Objects:** Image  
**Platforms:** Smart Devices(IOS)

### [Description](#Description)

In [RTL](https://wiki.genexus.com/commwiki/wiki?42318) languages, some images need to be flipped horizontally, and others don't. For example, Foreign Key pickers and selectors should be automatically flipped depending on the selected language.

With this property, the developer can flip elements as needed.

### [Samples](#Samples)

Consider the disclosure indicator image

```
LTR Language
 >
RTL Language
 <
```

At Runtime for RTL it is displayed as follows:

`[imagen omitida: wiki id 42965]`

### [Availability](#Availability)

This property is available since [GeneXus 16 upgrade 4](https://wiki.genexus.com/commwiki/wiki?42755,,).
