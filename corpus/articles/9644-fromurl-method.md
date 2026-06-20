---
title: "FromURL method"
source_id: 9644
source_url: https://wiki.genexus.com/commwiki/wiki?9644
genexus_version: "18"
---

# FromURL method

Initializes an Attribute/Variable control of Image, Audio, Video or BlobFile type from an URL.

### [Syntax](#Syntax)

*AttributeVariableControlName**.*****FromURL****(**<*CharacterExpression*>**)**

**Where:**  
  
*AttributeVariableControlName*Is the name of an Attribute/Variable control that shows an Image, Audio, Video, or BlobFile data type.

<*CharacterExpression*>  
     Is a string expression that must evaluate a valid URL. This format is equivalent to the [LoadBitmap function](https://wiki.genexus.com/commwiki/wiki?8458,,).

### [Description](#Description)

When used in a Transaction's attribute, GeneXus will automatically download the image or audio from the URL specified and store it in the database table. Any reference to the URL is saved. If you only need to store in the database a reference to an image URL, audio URL, video URL, or blob file URI, use the [ImageURI Property](https://wiki.genexus.com/commwiki/wiki?15205,,),, [FileURI property](https://wiki.genexus.com/commwiki/wiki?39979) or [VideoUri Property](https://wiki.genexus.com/commwiki/wiki?16608) instead.

### [Scope](#Scope)

**Data types:**[Image](https://wiki.genexus.com/commwiki/wiki?15204), [Audio](https://wiki.genexus.com/commwiki/wiki?16529), [Video](https://wiki.genexus.com/commwiki/wiki?16608), [BlobFile](https://wiki.genexus.com/commwiki/wiki?40420)  
**Generators:**[Angular](https://wiki.genexus.com/commwiki/wiki?42550), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Java](https://wiki.genexus.com/commwiki/wiki?12258),
[.NET](https://wiki.genexus.com/commwiki/wiki?38604), 
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892)

### [Samples](#Samples)

**Procedure:**

```
&image.FromUrl(!"http://images/myimage.jpg")
```

**Data Provider:**

```
{
   &MyImage.FromURL(!"http://images/myimage.jpg")
   MyImage = &MyImage
}
```

### [Availabilty](#Availabilty)

For [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)s, you can use this method in user events since [GeneXus 16 upgrade 1](https://wiki.genexus.com/commwiki/wiki?40782,,).

### [Security Tips](#Security+Tips)

* Sanitize user inputs.
* Restrict the domains the user can use on your application.


|  |
| --- |
| **Backlinks** |
| [A10:2021 - Server-side request forgery (SSRF)](https://wiki.genexus.com/commwiki/wiki?50190) | [GeneXus deprecated functions, methods, and rules](https://wiki.genexus.com/commwiki/wiki?6620) | [How to use responsive images in a web application](https://wiki.genexus.com/commwiki/wiki?31566) |
|

---
