---
title: "GetInternalURI method"
source_id: 52480
source_url: https://wiki.genexus.com/commwiki/wiki?52480
genexus_version: "18"
---

# GetInternalURI method

Returns a URI of the Image object that can be interpreted by other layers or components of the generated application.

### [Syntax](#Syntax)

*ImageName*.**GetInternalURI()**

**Where:**  
*ImageName*  
    [Image object](https://wiki.genexus.com/commwiki/wiki?23387) defined inside the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836).

**Type Returned:**  
Character

### [Scope](#Scope)

**Objects:**[Image object](https://wiki.genexus.com/commwiki/wiki?23387)   
**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

The returned string is a URI in the form of 'gximage://<*image name*>', where *image name* is the [Qualified Name](https://wiki.genexus.com/commwiki/wiki?22477) of an Image object.

This method is especially—and not exclusively—useful when you need to assign a reference of an Image Object to a variable, and that Image varies by Style, Language, Density, Layer, or Design System Options at runtime.

The client side of the applications may need to show the right image depending on the context information (i.e., Design System option Dark or Light) and this context may not be available in every application layer. Therefore, this method is useful when you need to get a reference of the image in a moment or layer where not all the context information is available.

In those scenarios, the use of this method will provide better results than the use of the [FromImage method](https://wiki.genexus.com/commwiki/wiki?7697) or [Link method](https://wiki.genexus.com/commwiki/wiki?23387).

### [Sample](#Sample)

Suppose GeneXusLogo is an image that varies by [Design System Tokens Options](https://wiki.genexus.com/commwiki/wiki?49381) Dark and Light, and you want to show the corresponding one in the UI Control &MyImage, depending on the context.

In that case, program the following:

```
Event 'MyEvent'
   &MyImage.ImageURI = image:GeneXusLogo.GetInternalURI()
EndEvent
```

A variation of this case in a scenario with a [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) could be the following:

Create a Data provider called 'GetLogo' that returns an SDT with a 'Logo' item.

```
SDTLogo
{
    Logo
    {
        ImageUri = image:GeneXusLogo.GetInternalURI()
    }
}
```

Then use that in a Panel.

```
Event 'MyEvent'
   &SDTLogo = &GetLogo()
   &MyImage.ImageURI = &SDTLogo.Logo
EndEvent
```

### [See Also](#See+Also)

* [Design System Object - How to change an image according to the Design System Object option](https://wiki.genexus.com/commwiki/wiki?48694)
* [Static content base URL property](https://wiki.genexus.com/commwiki/wiki?9010)


|  |
| --- |
| **Backlinks** |
| [Design System Object - How to change an image according to the Design System Object option](https://wiki.genexus.com/commwiki/wiki?48694) |

---
