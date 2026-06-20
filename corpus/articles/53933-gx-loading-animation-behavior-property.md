---
title: "gx-loading-animation-behavior property"
source_id: 53933
source_url: https://wiki.genexus.com/commwiki/wiki?53933
genexus_version: "18"
---

# gx-loading-animation-behavior property

Specifies how controls associated with a Data Provider should behave when it is loading. Controls include Form, Grid, Section, and Component.

### [Syntax](#Syntax)

gx-loading-animation-behavior: <value>;

### [Values](#Values)

|  |  |
| --- | --- |
| **compose-with-container** | Use the same behavior as the container. |
| **hide-content** | Don't show anything in the control's place until it is loaded. |
| **default** | Use the default behavior for the control in each platform. |
| **show-animation** | Show an animation instead of the control when it is loading. |
| **show-content** | Show the control without data while it is loading. |

### [Scope](#Scope)

**Generators:** [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Level:** [Design System Style Class](https://wiki.genexus.com/commwiki/wiki?49309)

### [Description](#Description)

A use case is when the [Panel](https://wiki.genexus.com/commwiki/wiki?24829) or [Grid](https://wiki.genexus.com/commwiki/wiki?24817) object is loaded and the animation is displayed, but the end user must wait until the end of the animation. This is the default behavior, which you can now select with some values.

The property is changed in the style class of the Design System Object with the values:

gx-loading-animation-behavior:**<default> <****show-animation>**  **<compose-with-container>** **<show-animation>** **<hide-content>**;

**Notes:**

* Loading Behavior works when there is no data to show.
* On Apple, Grid controls use the Show Content value by default, all other controls use Compose with Container.
* On Android, Grid, Section and Component controls use Show Animation by default.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

Set the Design System Object as shown below:

```
styles Base {

    .ShowContent {  gx-loading-animation-behavior: show-content;  }

    .HideContent {  gx-loading-animation-behavior: hide-content; }

    .ComposeWithContainer { gx-loading-animation-behavior: compose-with-container; }

    .ShowAnimation { gx-loading-animation-behavior: show-animation;}

  .PlatformDefault { gx-loading-animation-behavior: default; }

}
```
