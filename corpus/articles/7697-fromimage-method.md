---
title: "FromImage method"
source_id: 7697
source_url: https://wiki.genexus.com/commwiki/wiki?7697
genexus_version: "18"
---

# FromImage method

Changes images in run-time.

### [Syntax](#Syntax)

FromImage(*<ImageName>* | *<String Expression>*)

**Where:**  
*<ImageName>*  
      Is the name of an Image object stored in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836).

*<StringExpression>*  
     Is a string expression that must evaluate to a valid image URL.

### [Scope](#Scope)

**Data type:**[Bitmaps](https://wiki.genexus.com/commwiki/wiki?7701,,)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Samples](#Samples)

**Example 1**

Applies to [Bitmap data type](https://wiki.genexus.com/commwiki/wiki?7701,,) Variables and Image controls. If &Bitmap is a Bitmap data type variable, the following code will change the image displayed by it to MyNewImage.

```
&Bitmap.FromImage(MyNewImage)
```

**Example 2**

Applies to Bitmap data type Variables and Image controls. If &Bitmap is a Bitmap data type variable and &Image is a character variable whose value is "MyNewImage" the following code will change the image displayed by it to MyNewImage.

```
&Bitmap.FromImage(&Image)
```

**Note**: For Smart Devices applications, you can use this method into user event since [GeneXus 16 upgrade 1](https://wiki.genexus.com/commwiki/wiki?40782,,)

### [See Also](#See+Also)

[Image object](https://wiki.genexus.com/commwiki/wiki?23387)


|  |
| --- |
| **Backlinks** |
| [GetInternalURI method](https://wiki.genexus.com/commwiki/wiki?52480) | [How to use responsive images in a web application](https://wiki.genexus.com/commwiki/wiki?31566) |

---
