---
title: "ImageURI property"
source_id: 15205
source_url: https://wiki.genexus.com/commwiki/wiki?15205
genexus_version: "18"
---

# ImageURI property

Allows storing a reference to an image URL in the database and getting the absolute URL to the image.

### [Syntax](#Syntax)

**control.** ImageURI   

**ImageURI =**<*StringExpression*>

#### [**Where:**](#Where%3A+)

*StringExpression* is a string expression that must evaluate to a valid image URL.

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** [Attribute](https://wiki.genexus.com/commwiki/wiki?7240), [Variable](https://wiki.genexus.com/commwiki/wiki?7375)

### [Description](#Description)

The ImageURI property applies to [Image data type](https://wiki.genexus.com/commwiki/wiki?15204) variables and attributes, providing a flexible and efficient way to handle images in your applications.

It is possible to use this property for both SET and GET operations.

When used in SET operations, it allows you to define the location of the image using a URL, which can be a relative path, an absolute path to an external image, or a local path using the file:// protocol. This significantly reduces the storage space in the database and improves performance, since only the URL is stored instead of the complete image data.

In GET operations, GeneXus always returns the absolute URL of the image, ensuring consistent and complete access. This property also facilitates dynamic image handling, allowing updates without modifying the application code. In addition, it empties the internal Blob containing the image data when setting a new URL.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at runtime.

### [Samples](#Samples)

#### [**Set**](#Set)

**Sample #1**

```
&CustomerPhoto.ImageURI = 'http://www.google.com/images/logos/ps_logo2.png'
```

**Sample #2**

```
&image.FromImage(myImageWillbeErasedInNextLine)
&image.ImageURI = "http://www.myimages/image.jpg"
```

In this sample, the ImageURI property is set to the URL http://www.myimages/image.jpg. The image data previously stored in the &image variable will be cleared, and the ImageURI property will now hold the reference to the external image.

#### [**Get**](#Get)

```
&url = CustomerPhoto.ImageUri
```

In this example, the ImageURI property of the CustomerPhoto attribute is assigned to the &url variable, which implies that only the URI of the image is being read, which typically contains metadata such as location or access URL. This operation does not retrieve the byte content of the image. That is, it doesn't download or process the image itself, and therefore no temporary image files are created on disk or stored in the local directory configured for blobs.


|  |
| --- |
| **Backlinks** |
| [FromURL method](https://wiki.genexus.com/commwiki/wiki?9644) |

---
