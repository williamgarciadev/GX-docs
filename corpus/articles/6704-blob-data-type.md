---
title: "Blob data type"
source_id: 6704
source_url: https://wiki.genexus.com/commwiki/wiki?6704
genexus_version: "18"
---

# Blob data type

The [Blob data type](https://wiki.genexus.com/commwiki/wiki?6704) allows you to store images, spreadsheets, videos, audio files, and any other type of documents in the database, taking advantage of the different integrity and control mechanisms provided by the DMBS.

There is a way to save blob fields automatically in the database using a web interface (web transaction). There is also an easy way to display a blob field in the web form: a [File Upload control](https://wiki.genexus.com/commwiki/wiki?30574) control is generated, and, optionally, an embedded window in which the content (image, video, etc) is shown.

Note: Using  [BlobFile data type](https://wiki.genexus.com/commwiki/wiki?40420) instead of Blob data type, the data can be stored using any [external storage](https://wiki.genexus.com/commwiki/wiki?31120). Because of its advantages, it is strongly recommended to use Blobfile instead of Blob.

**Summary:**

* [Displaying Blobs](#Displaying+Blobs)
* [When does the blob store heterogeneous types of files](#When+does+the+blob+store+heterogeneous+types+of+files)

+ [File Type Attribute Property](#File+Type+Attribute+Property)
+ [File Type Runtime property](#File+Type+Runtime+property)
+ [File Name Attribute Property](#File+Name+Attribute+Property)
+ [Managing different Content Types](#Managing+different+Content+Types)

- [ContentType Property](#ContentType+Property)

* [Retrieving the name of the file](#Retrieving+the+name+of+the+file)
* [Display control properties](#Display+control+properties)

+ [Width / Height](#Width+%2F+Height)
+ [Display](#Display)

- [Note:](#Note%3A+)

+ [LinkTarget](#LinkTarget)
+ [Parameters](#Parameters)

* [Environment Properties](#Environment+Properties)

+ [Blob Local Storage Path](#Blob+Local+Storage+Path)
+ [Temporary Media Directory](#Temporary+Media+Directory)

* [Example](#Example)
* [Functions](#Functions)
* [Appendix](#Appendix)
* [Scope](#Scope)
* [See also](#See+also)

## [Displaying Blobs](#Displaying+Blobs)

A blob in the web form can be visualized automatically as an image, video, audio, document, etc, depending on the content of the blob field. It can be displayed as a link, to allow the user to click on it and display the blob, or it can be shown embedded in the web form.

To insert or update blob fields in the database, a file selection dialog appears, which enables the end user to browse the file system structure of the client PC (where the Internet browser is running). The process of uploading the file is then automatic. The user chooses a file that will be uploaded to the server and saved in the database.  
The file selection dialog is shown by clicking a "browse" button associated to an edit control in which the selected file is loaded. This is known as an "upload control", and it's shown in the following image:

`[imagen omitida: wiki id 6708]`

And in runtime you will see:

`[imagen omitida: wiki id 6707]`

The file selected is uploaded temporarily to a directory in the web server, and then, on the next POST (when the user confirms the transaction) it is saved in the database.

## [When does the blob store heterogeneous types of files](#When+does+the+blob+store+heterogeneous+types+of+files)

In some cases, it is necessary to work with different types of files, for example, the same database field contains Word documents, photographs in JPG and GIF format, and video files.

As a result, in some cases, it may be necessary to capture and save the extension of the files while uploading them, so this knowledge is available when you download the same files.

Having the file extension helps in many cases in which the Internet navigator need to know the file format in order to display it, or in cases in which the WebServer prohibits uploading files without extension.

There is a way of automatically capturing the Name and Extension of the file that is being uploaded. This information will also be used when the file is downloaded.

The main goal is to be able to run the application in servers that have a maximum level of security and don't allow uploading files without extension.

In sum, you have two alternatives if you want to keep heterogeneous files in the same field of the table (docs, jpgs, xmls, etc):

1. Define the blob as it is. When the file is uploaded and downloaded, a temporary file without extension will be saved in the file system of the WebServer. When it is downloaded, as the file has no extension, it may be necessary to assign a content type (\*) to it, in order to give the navigator a hint about the file's format. Some navigators (like IE) don't need that hint.
2. If you have a WebServer with very strict security policies (like Windows 2003 server using IIS), by default, it won't allow files without extension to be uploaded. In that case it is better to configure the [***FileTypeAttribute***](https://wiki.genexus.com/commwiki/wiki?8902) and [***FileNameAttribute***](https://wiki.genexus.com/commwiki/wiki?3122,,) blob properties in order to enable the blob's extension and name to be captured when it is uploaded. The file will be saved temporarily with the corresponding extension. In addition, when downloading (getting) the blob, it will also be saved with this extension, and its original name.

`[imagen omitida: wiki id 6711]`

Let's look at the attribute properties:

### [File Type Attribute Property](#File+Type+Attribute+Property)

It is available only for blob type attributes. The possible values for this property are any char or varchar attribute of the same table which the blob attribute belongs to. This property identifies an attribute that holds the extension of a Blob data type attribute. A Blob data type attribute may store files. Those files may all be the same type of files (i.e. Word documents, pictures in a specified format, etc.) or they may be heterogeneous. When working with heterogeneous files you should store the "file type" (extension) in a different attribute (because the extension isn't stored with the blob itself). In other words, the Blob data type attribute stores the file content and the File Type Attribute stores the file type (or extension).

Every time the Blob data type attribute is assigned (either in the user interface or by an assignment command) the value of the FileTypeAttribute is also automatically assigned. That is to say that the FileTypeAttribute is assigned when you upload a blob from a Web Interface (a Web Transaction), a procedure or a Business Component in a batch mode (from a procedure).

The default value is (none), stating that no attribute holds the file type.

Constraints on the FileTypeAttribute:

* It must be Character or VarChar (not Long Varchar) data type.
* It must belong to the same table that the referencing attribute belongs to.
* It should not be a formula.
* It cannot be used as the FileTypeAttribute or FileNameAttribute of any other Blob attribute.

*Note:* If the FileTypeAttribute property is assigned with a value, the corresponding attribute assigned to this property cannot be explicitly modified through a web transaction.

### [File Type Runtime property](#File+Type+Runtime+property)

As we've already explained the [FileType property](https://wiki.genexus.com/commwiki/wiki?3116), let's now look at the FileType runtime property. You can use it to retrieve the file extension of a blob, or change it dinamically by using the following sintax:  
  
&extension = Attblob.FileType  
  
The FileType property returns the actual file extension, when the blob is being uploaded.

For instance, if you have the following rule in a web transaction:  
  
msg('The uploaded file is ' + Attblob.FileName + '.' + Attblob.FileType) if not Attblob.isempty() on aftervalidate;  
  
When uploading the file, Attblob.FileType returns the actual file extension.

When the file is being downloaded, the FileType is obtained from:  
  
1. The FileType property, if it's assigned in the design model.  
2. The FileTypeAttribute property of the blob (if it has one).  
  
Otherwise, it returns null.

### [File Name Attribute Property](#File+Name+Attribute+Property)

##### 

The FileNameAttribute property identifies an attribute that holds the File Name of a Blob data type attribute. A Blob data type attribute can store files. The attribute stores the file content but not it's original name. You should set this property if you want to keep track of the original file name.  
  
Every time the Blob data type attribute is assigned (either in the user interface or by an assignment command) the value of the FileNameAttribute is also automatically assigned.

The default value is (none), stating that the original file name is lost.  
  
Constraints on the FileNameAttribute:

* It must be Character or VarChar (not Long Varchar) data type
* It must belong to the same table that the referencing attribute belongs to.
* It should not be a formula
* It cannot be used as the FileTypeAttribute or FileNameAttribute of any other Blob attribute.

*Note:* When downloading the file, it is temporary saved with its original name (which is taken from the FileNameAttribute), plus a random number. So that each file is given a different name, in order to be able to run the application in multiuser and concurrent environments.

### [Managing different Content Types](#Managing+different+Content+Types)

Content Types are a means of identifying web pages, images, and multimedia files on the Web and in email messages. They allow web browsers and email clients to display content in a correct and safe way. In the case of blobs, it may be necessary to set their Content Type, especially for certain kind of files, or for certain Internet navigators. Commonly used content types include text/html, image/jpeg, model/vrml, video/quicktime, etc.  
  
It's important to note that GeneXus automatically generates the corresponding Content Type of each blob, based on the extension it has. But there are ways to change this Content Type, if the user wants to.

There are two ways to do this in GeneXus:

**ContentType**property (design and runtime control property)

`[imagen omitida: wiki id 6718]` `[imagen omitida: wiki id 6712]`

#### [ContentType Property](#ContentType+Property)

It indicates the content type that should be associated with the Blob. For example, the content type of .wav documents is generally audio/wav, for an .xml file it's text/xml, etc.  
  
The Content Type depends on the browser, and that's why the GeneXus user is given the possibility of setting it programmatically. However, the corresponding Content Type is actually determined at runtime by the generated program.  
That is to say, in most cases you only need to set the File Type properties or nothing at all, if the blob has a FileTypeAttribute associated to it. This is because GeneXus automatically determines the Content Type, from this information.  
  
The [ContentType Property](https://wiki.genexus.com/commwiki/wiki?3125,,) should be used when the extension doesn't allow unique identification of the Content Type, or when the GeneXus user wants to set it depending on the end user's browser.

## [Retrieving the name of the file](#Retrieving+the+name+of+the+file)

You can query the name of the file by using the FileName property (runtime property). This is a ReadOnly property, which allows you to know the name of the file associated to a blob. When uploading the file, it returns the name of the file which is being uploaded. For instance, if you have the following rule in a web transaction:

msg('The uploaded file is ' + Attblob.FileName + '.' + Attblob.FileType) if not Attblob.isempty() on aftervalidate;

When uploading the file, Attblob.FileName returns the actual file name. On the contrary, when downloading a file (if it is in a webpanel, for instance), the value returned by the property is based on the value stored in the FileNameAttribute exclusively. This is because the blob by itself doesn't store any information other than the binary file. It doesn't store the extension or the name of the file.

## [Display control properties](#Display+control+properties)

### [Width / Height](#Width+%2F+Height)

Determines the width / height of the blob control in the form.

### [Display](#Display)

It indicates the way the blob content is going to be displayed in the form. It's available in design model and at runtime. The possible values are:

`[imagen omitida: wiki id 6707]`

`[imagen omitida: wiki id 6713]`

#### [Note:](#Note%3A+)

If you define a different value than 0 or 1 (only in runtime) in the property, the blob will not be displayed either Inline or Link.

### [LinkTarget](#LinkTarget)

When the display property is set to "Link", by this property you can choose to show the blob content in a separate window.  
For example: blobatt.linktarget = '\_blank'

### [Parameters](#Parameters)

When the display property is set to "Inline", and the blob content can't be managed by the Internet browser without providing additional information to it, the Parameters property has to be used to provide the necessary information to the browser.  
For example, if you want to display a video in mpg format, in the IE (Internet Explorer), you have to have the following settings:

(This example runs in Windows Media Player)  
blobatt.parameters = '<param name="Filename" value="' + pathtourl( blobatt) + '">' +  
'<param name="AutoStart" value="True">' +  
'<param name="ShowControls" value="True">' +  
'<param name="ShowStatusBar" value="True">' +  
'<param name="ShowDisplay" value="False">' +  
'<param name="AutoRewind" value="True">'

*Note:* The Internet browsers need to know which application to use to display certain type of files. That is what the ContentType property is for. For example, in the case of IE, when the content is .mpg, the ContentType should not be video/mpg (as it would be by default), but application/x-mplayer2. In these special cases, the ContentType refers to the application which should show the content instead of the real content type of the file.

## [Environment Properties](#Environment+Properties)

### [Blob Local Storage Path](#Blob+Local+Storage+Path)

This environment property is used to set the web server path where files are temporarily saved when retrieved from the database. That is to say, when you Get data, a temporary file is saved in the Blob Local Storage Path. The extension of the saved file depends on the value of the Blob property called File Type.

The Blob Local Storage Path must be accessible from the virtual directory (ie, if the virtual directory is C:\resin-2.0.2\webapps\test an acceptable value for the property would be: C:\resin-2.0.2\webapps\test\resources\rtrepository).

### [Temporary Media Directory](#Temporary+Media+Directory)

This environment property is used to set the web server path where files are temporarily saved when loaded in the database. That is to say, when a Blob is added or updated, it is temporarily saved in this directory.

The Temporary Media Directory must be accessible from the virtual directory.

## [Example](#Example)

Let's see an example in which we use the Blob data type. We create a Country transaction, with attributes CountryId, CountryName, CountryFlag, and CountryAnthem. The latter two are of the blob type, so that we can store the flag of the country, and its national anthem.

`[imagen omitida: wiki id 33109]`

We now go to the properties of the blob-type attributes, and in the File Type property, we set png for CountryFlag, and wav for CountryAnthem:

`[imagen omitida: wiki id 33110]`   `[imagen omitida: wiki id 33111]`

Finally, we press F5, and in the Country transaction we insert the country Uruguay, along with its flag and national anthem:

`[imagen omitida: wiki id 33112]`  
  
*Notes***:**

## [Functions](#Functions)

##### [[PathToURL function](https://wiki.genexus.com/commwiki/wiki?9563)](#wiki%3F9563%2CPathToURL%2Bfunction+PathToURL+function)

## [Appendix](#Appendix)

I. In general, Internet Explorer doesn't respect the Content Type returned by web servers and uses a variety of strategies to automatically detect the content type of files.  
  
This means that different browsers have different behaviors. For example, when a blob field is displayed as a download (link), and a Content Type is specified, IE determines how to display the blob in the form by using the above strategies. Therefore, the Content Type is only considered as a hint for the browser.  
This doesn't happen with Mozilla, which always considers the specified Content Type. Therefore, we recommend reading the corresponding documentation so as to know beforehand what the expected behavior is for the application.  
  
Our tests produced the following results:  
  
1. When the blob is displayed as a link, the Content Type is ignored by IE. It has its own rules for identifying the content type and ignores the one specified by the user. The same happens with Netscape. Consequently, the file will be correctly displayed in the HTML only if the file type can be identified by the browser. To solve this, give the file an extension through the FileType property when saving it temporarily. This problem doesn't exist in Mozilla FireFox.  
  
2. If you set the FileType property, the blob is temporarily saved in the server with an extension. In this case, the web server decides how to display the content through MIME Types, so the specified Content Type is ignored. Blobs that are Word documents, for example, are correctly viewed only if they are displayed as links, and they have an associated extension or "FileType" (the same happens with Excel worksheets).  
  
3. In some cases, when the blob display is Inline and has an associated extension (File Type), IE can't display the content, while Netscape and Mozilla try to download it (for example, it happens with .doc, .xls, .pdf).  
  
4. If the display is Inline and you work with File Type or Content Type, IE, Netscape and Mozilla all consider the specified Content Type, except in the case of Word documents and some other exceptions. Some MIME types, like graphics, can be displayed inside the browser. Others, such as word processing documents, require an external helper application in order for them to be displayed.  
  
The following table shows some Content Types which are assigned automatically, given a File Type (an associated extension).

|  |  |  |
| --- | --- | --- |
| **FileType** | **Content-Type** |  |
| TXT | text/plain | |
| RTX | text/richtext | |
| HTML/HTM | text/html | |
| XML | text/xml | |
| AIF | audio/x-aiff | |
| AU | audio/basic | |
| WAV | audio/wav | |
| BMP | image/bmp | |
| GIF | image/gif | |
| JPE/JPEG/JPG | image/jpeg | |
| JFIF | image/pjpeg | |
| TIF | image/tiff | |
| MPEG | video/mpeg | |
| MOV/QT | video/quicktime | |
| AVI | video/x-msvideo | |
| EXE | application/octet-stream | |
| PS | application/postscript | |
| PDF | application/pdf | |
| TGZ | application/x-compressed | |
| PNG | image/x-png | |
| ZIP | application/x-zip-compressed | |
| GZ | application/x-gzip | |
| DLL | application/x-msdownload | |

II. Changing the Temporary Media Directory and Blob Local Storage Path at runtime  
  
You can change the Temporary Media Directory and the Blob Local Storage Path at runtime for the Java generator by changing the client.cfg. For example:  
TMPMEDIA\_DIR=C:\Program Files\Apache Software Foundation\Tomcat 5.0\webapps\YIBLOB\TempMedia  
  
CS\_BLOB\_PATH=C:\Program Files\Apache Software Foundation\Tomcat 5.0\webapps\YIBLOB\media

Note

When the blob's content is restricted to images, video or audio, the use of [Image](https://wiki.genexus.com/commwiki/wiki?15204), [Video](https://wiki.genexus.com/commwiki/wiki?16608) or [Audio](https://wiki.genexus.com/commwiki/wiki?16529) data types should be considered instead the blob data type.

* **FileType** property (design and runtime property)
* **0: Inline:** The blob is displayed in the form, above the upload control.
* **1: Link:** An image is displayed with a link to the Blob.
* For security reasons, there are two different properties. However, GeneXus users may set them to point to the same physical directory. The Blob Local Storage Path will always be accesible to the user.
* The application must have read / write permissions for these directories
* In NET generator, by default, the Temp Media directory and Blob Local Storage path properties are considered to be the WEB folder under the model directory.
* In Java generator, both directories must exist. That is to say, they are not automatically created by GeneXus.

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Objects** | [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) |
| **Languages** | .NET, Java |
|  |  |

## [See also](#See+also)

[Blobs in Base64](https://wiki.genexus.com/commwiki/wiki?7374)


|  |
| --- |
| **Backlinks** |
| [Blob data type](https://wiki.genexus.com/commwiki/wiki?6704) | [Blob local storage directory property](https://wiki.genexus.com/commwiki/wiki?6979) |
| [Blobs in Base64](https://wiki.genexus.com/commwiki/wiki?7374) | [Data Type property](https://wiki.genexus.com/commwiki/wiki?7232) | [Data types list](https://wiki.genexus.com/commwiki/wiki?6779) | [Files external object](https://wiki.genexus.com/commwiki/wiki?44917) |
| [FileTypeAttribute property](https://wiki.genexus.com/commwiki/wiki?8902) | [FileUpload command examples](https://wiki.genexus.com/commwiki/wiki?47224) | [FromString method](https://wiki.genexus.com/commwiki/wiki?12694) |
| [HowTo: Deploy an Application to a Kubernetes cluster](https://wiki.genexus.com/commwiki/wiki?45416) | [IsEmpty method](https://wiki.genexus.com/commwiki/wiki?9645) | [LinkTarget property](https://wiki.genexus.com/commwiki/wiki?8812) | [Load balancing considerations](https://wiki.genexus.com/commwiki/wiki?45291) |
| [PathToURL function](https://wiki.genexus.com/commwiki/wiki?9563) | [Security Scanner built-in tool](https://wiki.genexus.com/commwiki/wiki?46412) | [Security Scanner built-in tool (GeneXus 18 or prior)](https://wiki.genexus.com/commwiki/wiki?52570) | [SetEmpty method](https://wiki.genexus.com/commwiki/wiki?9646) |
| [Temp media directory property](https://wiki.genexus.com/commwiki/wiki?7628) | [ToString method](https://wiki.genexus.com/commwiki/wiki?7090) |

---
