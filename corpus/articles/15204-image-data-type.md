---
title: "Image data type"
source_id: 15204
source_url: https://wiki.genexus.com/commwiki/wiki?15204
genexus_version: "18"
---

# Image data type

The purpose of this data type is to store or reference any type of image files (jpg, bmp, png, etc).

Images can be stored in any of the databases supported by GeneXus without having to specify the file name or type (jpg, bmp, etc.).

An image can be loaded from both an image predefined in the [KB](https://wiki.genexus.com/commwiki/wiki?2428) (using the FromImage method) and a URL (local or remote using the FromURL method). If the value sent to FromURL is a remote URL, the image will be downloaded and saved in the DB upon making an Insert. If what is needed is just a reference to the Image stored in a local or remote location, the ImageURI property has to be assigned.

Therefore, any image can be displayed by dragging any variable or attribute defined with the Image data type to the form. In other words, GeneXus performs the image rendering without any intervention from the user.

### [Properties](#Properties)

|  |  |
| --- | --- |
| ImageName | Gets the image name (Character). |
| ImageType | Gets the Image Type. The Image Type Domain is the extension of the image. For example: jpg, ico, png, etc. |
| ImageURI | Sets/Gets the Image URL  **Set**  You can set a relative path, which will be resolved with the current host.  You can set an absolute path to an external image on the web.  You can set a local path by using file:// protocol  When you set the ImageURI property, the internal Blob with the image will be set to empty.  **For example:**   ``` &image.FromImage(myImageWillbeErasedInNextLine) &image.ImageURI = "http://www.myimages/image.jpg" ```   In this case, image.jpg will be the image in the data.  **Get:**  GeneXus always returns the absolute URL to the image. |

\*These properties are inaccessible by Smart Devices events

### [Methods](#Methods)

|  |  |
| --- | --- |
| FromImage(*imageobjectname*) | Loads the current instance with the image given in the Image Object parameter  After calling this method the ImageURI property has the following value:  <imageobjectname>.<extension>  The <imageobjectname>.<extension> is calculated by GeneXus depending on the theme and language. |
| FromURL(*imageURL*) | Loads the current instance with the image given in the *ImageURL* parameter.  This indicates that the internal Blob holding the image must be loaded from the URI indicated in the *ImageURL* parameter.  After calling this method, the ImageURI property has the absolute URL to the image.  For example:   ``` &image.FromURL('www.myimage.com/company.jpg') msg(&image.ImageURI)  // will print www.myimage.com/company.jpg ```   **Note:** The image will be downloaded from the URL specified and will be automatically stored in the database (applies only to attributes). |
| SetEmpty/IsEmpty | Returns True if there aren´t an image or a reference to an a stored image. |

### [Samples](#Samples)

#### [1. Structuring](#1.+Structuring)

A company wants to save photos of its employees; to do so, you only have to write the following:

```
EmployeeId     Numeric(4.0)
EmployeeName   Character
EmployeeImage  Image
```

In the EmployeImage field, any type of photos can be saved (jpg, png, etc).

#### [2. Inserting an image into the DB from an existing image in my KB](#2.+Inserting+an+image+into+the+DB+from+an+existing+image+in+my+KB)

The FromImage method can only be used when extracting an image from a known KB. Suppose you have an image in your KB called CompanyNameImage.

So, you write the following code:

```
&Company.CompanyId = 1
&Company.CompanyLogo.FromImage(CompanyNameImage)
&Company.Save()
```

#### [3. Inserting an image into the DB from an existing URL](#3.+Inserting+an+image+into+the+DB+from+an+existing+URL)

Suppose you have an image in your file system or in a web URL and you want to store it in your database. Your image is file:///c:/myfolder/logo.jpg (the URL must be accessible from your server if it is a local URL).

```
&Company.CompanyId = 1
&Company.CompanyLogo.FromURL('file:///c:/myfolder/logo.jpg')
&Company.Save()
```

#### [4. Inserting a reference into the DB from an external image](#4.+Inserting+a+reference+into+the+DB+from+an+external+image)

You want to reference an external image:

```
&Company.CompanyId = 1
&Company.CompanyLogo.ImageURI = 'http://www.events.genexus.com/gxdis/style000001/s/00000000160000003715.jpg'
&Company.Save()
```

#### [5. How to convert from Blob to Image in your DB](#5.+How+to+convert+from+Blob+to+Image+in+your+DB)

Most likely, you have many Blob attributes in your DB to store images and you want to start using the new data type.

The only thing you have to do is change the type from Blob to Image in your attribute definition and GeneXus will perform a reorganization, taking into account the FileType, FileTypeAttribute and FileNameAttribute properties.

#### [6. How to convert from Blob to Image and vice versa programmatically](#6.+How+to+convert+from+Blob+to+Image+and+vice+versa+programmatically)

You can directly assign a Blob to an Image and vice versa. Remember that the conversion from Blob to Image will work depending on the kind of mime type of your Blob and the FileType, FileTypeAttribute and FileNameAttribute properties. In some cases, it may happen that the image is not displayed in the user interface.

#### [7. How to convert from Char|VarChar to Image in my DB](#7.+How+to+convert+from+Char+VarChar+to+Image+in+my+DB)

In some cases we could have a Character attribute in our DB with URL. What would happen if you wanted to start using the new image data type without losing your existing data?

GeneXus supports the reorganization from Char|VarChar to Image and vice versa.

### [Image in data base](#Image+in+data+base)

The image is stored in the data base as 2 separate fields. One is a Blob, and the other is a string with same name and postfix "\_GXI". The composition of this field is explained in [SAC 31266](http://www2.gxtechnical.com/portal/hgxppredirect.aspx?15,26,0,,,31266).

### [Scope](#Scope)

**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:**[Attribute](https://wiki.genexus.com/commwiki/wiki?7240), [Variable](https://wiki.genexus.com/commwiki/wiki?7375)

### [See also](#See+also)

[Image manipulation API](https://wiki.genexus.com/commwiki/wiki?39415)


|  |
| --- |
| **Backlinks** |
| [Actions external object](https://wiki.genexus.com/commwiki/wiki?31350) | [Audio external object](https://wiki.genexus.com/commwiki/wiki?30041) | [Blob data type](https://wiki.genexus.com/commwiki/wiki?6704) |
| [BlobFile data type](https://wiki.genexus.com/commwiki/wiki?40420) | [Camera external object](https://wiki.genexus.com/commwiki/wiki?31296) | [Camera external object (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?53919) | [Contacts external object](https://wiki.genexus.com/commwiki/wiki?31276) |
| [Customization of Multimedia Fields](https://wiki.genexus.com/commwiki/wiki?20117) | [Data Type Filter property](https://wiki.genexus.com/commwiki/wiki?40654) | [Data Type property](https://wiki.genexus.com/commwiki/wiki?7232) | [Data types list](https://wiki.genexus.com/commwiki/wiki?6779) |
| [DesignOps - Guide for designers](https://wiki.genexus.com/commwiki/wiki?46871) | [External Storage for Multimedia](https://wiki.genexus.com/commwiki/wiki?31120) | [Facebook external object](https://wiki.genexus.com/commwiki/wiki?38432) | [FromURL method](https://wiki.genexus.com/commwiki/wiki?9644) |
| [GeneXus Cognitive API - Classify procedure](https://wiki.genexus.com/commwiki/wiki?40171) | [GeneXus Cognitive API - DetectFaces procedure](https://wiki.genexus.com/commwiki/wiki?40177) | [GeneXus Cognitive API - DetectObjects procedure](https://wiki.genexus.com/commwiki/wiki?40178) | [GeneXus Cognitive API - DetectScene procedure](https://wiki.genexus.com/commwiki/wiki?40179) |
| [GeneXus Cognitive API - OCR procedure](https://wiki.genexus.com/commwiki/wiki?40180) | [GeneXus Markup Language (GXML)](https://wiki.genexus.com/commwiki/wiki?46876) |
| [HowTo: Deploy an Application to a Kubernetes cluster](https://wiki.genexus.com/commwiki/wiki?45416) | [HowTo: Deploy to AWS Lambda Function](https://wiki.genexus.com/commwiki/wiki?51533) | [HowTo: Upload an image, video, or audio file via an API object](https://wiki.genexus.com/commwiki/wiki?51411) | [HowTo: Use Camera external object in GeneXus](https://wiki.genexus.com/commwiki/wiki?31298) |
| [HowTo: Use Camera external object in GeneXus for Native Mobile apps (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?53920) | [HowTo: Use the Image Map Control](https://wiki.genexus.com/commwiki/wiki?17823) | [HowTo: Use the Maps Control Type in a Panel Grid](https://wiki.genexus.com/commwiki/wiki?54097) | [HowTo: Using PhotoLibrary external object for Smart Devices](https://wiki.genexus.com/commwiki/wiki?26933) |
| [Image Annotations](https://wiki.genexus.com/commwiki/wiki?45373) | [Image manipulation API](https://wiki.genexus.com/commwiki/wiki?39415) | [Image manipulation API (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55714) |
| [Image theme-class](https://wiki.genexus.com/commwiki/wiki?20460) | [IsEmpty method](https://wiki.genexus.com/commwiki/wiki?9645) | [Load balancing considerations](https://wiki.genexus.com/commwiki/wiki?45291) |
| [Manual Synchronization Code Sample](https://wiki.genexus.com/commwiki/wiki?22543) | [Maximum Upload Size property](https://wiki.genexus.com/commwiki/wiki?44940) | [Medium Image Upload Size property](https://wiki.genexus.com/commwiki/wiki?24115) | [PhotoLibrary external object](https://wiki.genexus.com/commwiki/wiki?39397) |
| [Pin Image Attribute property](https://wiki.genexus.com/commwiki/wiki?42213) | [Pin Image Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42214) | [Purpose Strings properties group](https://wiki.genexus.com/commwiki/wiki?32755) | [Reorganization Error Codes and Messages](https://wiki.genexus.com/commwiki/wiki?5952) |
| [Security Scanner built-in tool](https://wiki.genexus.com/commwiki/wiki?46412) | [SetEmpty method](https://wiki.genexus.com/commwiki/wiki?9646) | [Share external object](https://wiki.genexus.com/commwiki/wiki?29800) | [Small Image Upload Size property](https://wiki.genexus.com/commwiki/wiki?24116) |
| [Twitter external object](https://wiki.genexus.com/commwiki/wiki?39432) | [Using appcfg to upload an application to Google App Engine](https://wiki.genexus.com/commwiki/wiki?32213) |

---
