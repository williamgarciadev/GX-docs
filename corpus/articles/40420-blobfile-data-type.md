---
title: "BlobFile data type"
source_id: 40420
source_url: https://wiki.genexus.com/commwiki/wiki?40420
genexus_version: "18"
---

# BlobFile data type

It stores or references all file types (image, audio, video, pdf, excel, etc.), regardless of their format. The data can be stored locally or by using any [external storage](https://wiki.genexus.com/commwiki/wiki?31120) media.

## [Properties and Methods](#Properties+and+Methods)

The properties and methods are similar to those available for [Image data type](https://wiki.genexus.com/commwiki/wiki?15204), [Audio data type](https://wiki.genexus.com/commwiki/wiki?16529) and [Video data type](https://wiki.genexus.com/commwiki/wiki?16608).

### [Properties](#Properties)

|  |  |
| --- | --- |
| FileName | Gets the file name (Character). It refers to the base name of the file, i.e. it does not return the extension. |
| FileType | Gets the file Type. It indicates the extension of the file: txt, jpg, pdf, etc.  You should keep in mind that the extension is not the same as the ContentType. ContentType is an HTTP Header for the browser to interpret. For example: application/json, image/jpg, text/javascript, text/css.  In addition, you can programmatically set the ContentType based on the FileType. (e.g. If FileType="html" then ContentType="text/html"). |
| FileURI | Sets/Gets the FileURI  **Set**:  You can set a relative path. It will be solved within the current host.  You can set a local path by using file:// protocol.  When you set the URI property, the internal binary file stored in the DB will be set to empty.  Example:   ``` &Blobfile.FromURL(myFileWillbeErasedInNextLine) &Blobfile.FileURI = "http://www.myfiles/file.pdf" ```   In this case, the .pdf file will be the file in the data.  **Get**:  It always returns the absolute URI to the file. |

### [Methods](#Methods)

|  |  |
| --- | --- |
| FromURL(*FileURL*) | It loads the current instance with the file given in parameter FileURL.  The internal binary holding the file is loaded from the FileURL indicated.  After calling this method, the URI property has the filename and extension of the FileURL specified.  For example:   ``` &Blobfile.FromURL('www.myfiles.com/myfile.pdf') msg(&Blobfile.FileURI) // will print myfile.pdf ``` |
| SetEmpty/IsEmpty |  |

## [How does it work?](#How+does+it+work%3F)

The File can be loaded from a URI (local or remote) using the FromURL method. If the value passed to FromURL is a remote URL, then the file is downloaded (and saved to the DB if necessary).

If you simply want to have a reference to the file that is somewhere, remote or local, all you needto do is assign the URI property.

## [How is it stored in the DB?](#How+is+it+stored+in+the+DB%3F)

The BlobFile data type is automatically stored as more than one field in the DB (similar to the way in which [Image data type](https://wiki.genexus.com/commwiki/wiki?15204), [Audio data type](https://wiki.genexus.com/commwiki/wiki?16529) and [Video data type](https://wiki.genexus.com/commwiki/wiki?16608) are stored).  
  
The structure saved in the DB is the following:

* Attribute\_Name (Binary is stored here)
* Attribute\_Name\_GXI (where the URI is stored) (GXI = GeneXus Identifier)

When the URI is assigned, Attribute\_Name\_GXI is assumed to be an external file (in this case the full URI is stored). If the file was loaded using the FromURL method, then the relative path is saved there (so the file name and type are known).

When a file is stored, the file name is stored in the GXI field as follows:

gxdbfile: <file name> \_ <token>. <file extension>

The prefix "gxdbfile:"  indicates to GeneXus that it is a file, and not a relative URL.  
The token allows you to identify the file univocally. GeneXus generates a GUID.

## [What is the difference beetwen Blob data type and BlobFile data type?](#What+is+the+difference+beetwen+Blob+data+type+and+BlobFile+data+type%3F)

The difference between Blob and BlobFile data types is the way in which they are stored in the database. As a result, BlobFile may be stored in any [external storage](https://wiki.genexus.com/commwiki/wiki?31120), whereas Blob data type may not.

## [Reorganizations](#Reorganizations)

The following reorganizations are supported:

* From Blob to BlobFile  -> The binary file is copied, and the GXI\_Attribute\_Name is obtained through the name of the original blob file.
* From Character to BlobFile -> The GXI\_Attribute\_Name is set from the character attribute.
* From BlobFile to Blob -> The GXI\_Attribute\_Name field is removed.
* From BlobFile to Character -> The field is assigned, if possible, using the GXI\_Attribute\_Name value. Otherwise, it's left empty.

## [Availability](#Availability)

* Since [GeneXus 15 upgrade 12](https://wiki.genexus.com/commwiki/wiki?39737,,) in [Java](https://wiki.genexus.com/commwiki/wiki?12258), [.NET](https://wiki.genexus.com/commwiki/wiki?49815,,), and [Apple](https://wiki.genexus.com/commwiki/wiki?14917)
* Since [GeneXus 16](https://wiki.genexus.com/commwiki/wiki?35351,,) in [.NET Core](https://wiki.genexus.com/commwiki/wiki?49825,,)
* Since [GeneXus 16 upgrade 9](https://wiki.genexus.com/commwiki/wiki?45275,,) in [Android](https://wiki.genexus.com/commwiki/wiki?14453)
* Since [GeneXus 18 upgrade 1](https://wiki.genexus.com/commwiki/wiki?51081) in [Angular](https://wiki.genexus.com/commwiki/wiki?42550)


|  |
| --- |
| **Backlinks** |
| [Blob data type](https://wiki.genexus.com/commwiki/wiki?6704) | [External Storage for Multimedia](https://wiki.genexus.com/commwiki/wiki?31120) | [Files external object](https://wiki.genexus.com/commwiki/wiki?44917) |
| [FileURI property](https://wiki.genexus.com/commwiki/wiki?39979) | [FromURL method](https://wiki.genexus.com/commwiki/wiki?9644) | [HowTo: Deploy to AWS Lambda Function](https://wiki.genexus.com/commwiki/wiki?51533) |
| [HowTo: Upload an image, video, or audio file via an API object](https://wiki.genexus.com/commwiki/wiki?51411) | [Interop external object](https://wiki.genexus.com/commwiki/wiki?23734) | [Interop external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55183) | [IsEmpty method](https://wiki.genexus.com/commwiki/wiki?9645) |
| [Load balancing considerations](https://wiki.genexus.com/commwiki/wiki?45291) | [SetEmpty method](https://wiki.genexus.com/commwiki/wiki?9646) |

---
