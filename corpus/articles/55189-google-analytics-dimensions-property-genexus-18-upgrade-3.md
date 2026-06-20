---
title: "Google Analytics Dimensions property (GeneXus 18 Upgrade 3)"
source_id: 55189
source_url: https://wiki.genexus.com/commwiki/wiki?55189
genexus_version: "18"
---

# Google Analytics Dimensions property (GeneXus 18 Upgrade 3)

An SDT containing the dimensions to send on pageviews. Each property in the SDT is a dimension, and the value of the property, the dimension's value.

### [Scope](#Scope)

**Controls:** [Google Analytics Control](https://wiki.genexus.com/commwiki/wiki?11847)

### [Description](#Description)

When using the [Google Analytics Control](https://wiki.genexus.com/commwiki/wiki?11847) you can specify an SDT containing a list of dimensions to discriminate further when doing the site analysis.

Each property in the SDT is a *dimension*, and the value of the property, it's value, they must be preconfigured within the Google Analytics Console. Make sure to review the [Google Analytics site documentation](https://developers.google.com/analytics/devguides/collection/analyticsjs/custom-dims-mets) on [dimensions](https://support.google.com/analytics/answer/6086074?hl=en).

From the GeneXus side, create an SDT with items Key / Value (both character datatypes) and assign whatever you want in runtime (it applies to the PageView Track event). Each SDT item is a dimension and you must keep the conventions detailed on the Google Site, where the dimensions properties starts with the *dimension* prefix and then references an index.  
Make sure to assign the *Dimensions* User Control property to the associated SDT variable.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at run-time.

### [Samples](#Samples)

Consider the following code snippet:

```
&GADimensions.dimension1 = !"Some value"
&GADimensions.dimension2 = !"Some other value"
&GADimensions.dimension3 = !"Again some salue"
&GADimensions.dimension4 = !"Again some other value"
```

On the Google Analytics side, you will need to create the custom dimensions and make sure to match the correct index the following sample image shows that *dimension4* will be displayed as "GXUpgrade".

`[imagen omitida: wiki id 48420]`

The assigned properties will automatically be detailed as expected. You will be able to analyze the data by the defined dimensions.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build with this Only](https://wiki.genexus.com/commwiki/wiki?5693) of the object.

### [Availability](#Availability)

This property is available since [GeneXus 17 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?48247,,).

### [See Also](#See+Also)

[Google Analytics Control](https://wiki.genexus.com/commwiki/wiki?11847)
