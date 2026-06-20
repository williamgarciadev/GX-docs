---
title: "gx-popup-resize-handle-class property"
source_id: 51284
source_url: https://wiki.genexus.com/commwiki/wiki?51284
genexus_version: "18"
---

# gx-popup-resize-handle-class property

Sets the class to style the image that resizes a popup.

### [Scope](#Scope)

**Level:** [Design System Style Class](https://wiki.genexus.com/commwiki/wiki?49309)

### [Description](#Description)

The class where the gx-popup-resize-handle-class property must be placed is the same as the one shown in the following example:

```
   .gx-popup-default
    {
        gx-popup-resize-handle-class: PopupResize;
    }
    .PopupResize
    {        
        content: gx-image(PopupResizeImage);
    }
```

### [Availability](#Availability)

This property is available since [GeneXus 17 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?49971,,).

### [See Also](#See+Also)

[DSO properties that begin with gx- and end with class](https://wiki.genexus.com/commwiki/wiki?55707)
