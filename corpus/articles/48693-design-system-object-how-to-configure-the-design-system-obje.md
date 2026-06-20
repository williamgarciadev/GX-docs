---
title: "Design System Object - How to configure the Design System Object option"
source_id: 48693
source_url: https://wiki.genexus.com/commwiki/wiki?48693
genexus_version: "18"
---

# Design System Object - How to configure the Design System Object option

So as not to complicate the design by adding a specific option, suppose that to switch from one mode to another the user will click on the hero image.

To this end, add an event:

`[imagen omitida: wiki id 48640]`

There you will change the mode. How?

To configure the options at any time, there is an external object included in the GeneXus module:

`[imagen omitida: wiki id 48641]`

Do the following:

`[imagen omitida: wiki id 48642]`

Add the .Form class to the styles of the [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375), which is used by default in the Main table:

```
    .Form
    {
        background-color: $colors.Surface;
    }
```

And test it:

`[imagen omitida: wiki id 48643]`

### [Availability](#Availability)

Since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?48684,,).


|  |
| --- |
| **Backlinks** |
| [Toc:Design Systems](https://wiki.genexus.com/commwiki/wiki?40108) |

---
