---
title: "AlternateText property"
source_id: 8685
source_url: https://wiki.genexus.com/commwiki/wiki?8685
genexus_version: "18"
---

# AlternateText property

Used to display a text when an image does not appear in the browser. Some browsers do not support images. Others do, but there could be a slow connection so you may prefer not to display images or to load them 'upon request'.

### [Syntax](#Syntax)

**control.** AlternateText = Text   

Type returned: Text

**Where:**  
*Text*  
    Is a text that will appear if the image us not shown in the browser.

### [Scope](#Scope)

**Objects:** Transaction, Web Panel  
**Platforms:** Web(.Net, Java)  
**Controls:** Image

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies both at run-time and at design-time.

### [Samples](#Samples)

Suppose that the image do not appear in its place. Then:

```
&Image.AlternateText = "Image not available"
```

...could be one solution of warning.
