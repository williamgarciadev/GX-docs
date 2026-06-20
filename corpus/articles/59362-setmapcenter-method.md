---
title: "SetMapCenter method"
source_id: 59362
source_url: https://wiki.genexus.com/commwiki/wiki?59362
genexus_version: "18"
---

# SetMapCenter method

Indicates the center of the Map in a Grid whose Control Type property = Maps, using the GeoPoint data type.

## [Syntax](#Syntax)

```
GridControlName.SetMapCenter(AttOrVarGeoPoint,[Number])
```

**Where:**

*Grid**Control**Name*  
    Is the name of a [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) with its Control Type property = Maps (included in a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)).

*AttOrVarGeoPoint*    
    Is an [attribute](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7240,,) or [variable](https://wiki.genexus.com/commwiki/wiki?7375) based on the [GeoPoint data type](https://wiki.genexus.com/commwiki/wiki?58058) that indicates the coordinates where the map will be centered.

*Number*  
    This optional parameter indicates the Zoom level.

## [Scope](#Scope)

**Controls:**[Grid](https://wiki.genexus.com/commwiki/wiki?24817) (Control Type: [Maps](https://wiki.genexus.com/commwiki/wiki?15309))  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

## [Sample](#Sample)

```
composite
   &GeoPoint.FromString("POINT( -56.1701774597168 -34.91676309400329)")
   Grid1.SetMapCenter(&GeoPoint,8)
endcomposite
```
