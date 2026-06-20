---
title: "FileType property"
source_id: 3116
source_url: https://wiki.genexus.com/commwiki/wiki?3116
genexus_version: "18"
---

# FileType property

Specifies the extension with which the temporary file is saved in the Blob local storage path, when retrieved from the database.

### [Description](#Description)

The FileType property can be assigned at design time, and at runtime.

Examples:

```
TXT
RTX
HTML (or HTM)
XML
AIF
AU
WAV
BMP
GIF
JPE (or JPEG, JPG  )
JFIF
TIF
MPEG
MOV/QT
AVI
EXE
PS
PDF
TGZ
PNG
ZIP
GZ
DLL
```

#### [FileType runtime property](#FileType+runtime+property)

You can use it to retrieve the file extension of a blob; or to change it, dynamically.

For retrieving the extension of the file, use the following syntax:

```
&extension = Attblob.FileType
```

The FileType property returns the actual file extension when the blob is being uploaded.  
For instance, if you have the following rule in a web transaction:

```
msg('The uploaded file is ' + Attblob.FileName + '.' + Attblob.FileType) if not Attblob.isempty() on aftervalidate;
```

When uploading the file, Attblob.FileType returns the actual file extension.  
When the file is being downloaded, the FileType is obtained from:

1. The File Type property, if it's assigned in the design model.  
2. The [File Type Attribute property](https://wiki.genexus.com/commwiki/wiki?8902) of the blob (if it has one).

Otherwise, it returns null.

You can also change the extension of a file, at the moment of downloading it.  Its goal is to change the extension that the temporary file is going to be saved with.

### [Example:](#Example%3A)

You have a blob attribute that hasn't got a File Type Attribute associated with it. You want to assign to it the .doc extension, at the moment of downloading it, so you have:

```
Event Start

    Attblob.FileType = 'DOC'

EndEvent  // Start
```

Important Note:  The value of this property is ignored if the File Type Attribute property is set.

#### [Final Considerations](#Final+Considerations)

*This extension is used also to dynamically determine the blob's Content Type*, determined automatically by GeneXus.  That is to say that, if you specify a FileType for a blob, GeneXus will infer the corresponding Content-Type for that blob. If you specify the Content-Type property for the blob, and the File Type property is also configured, the former will override the latter.

If none of them is configured, and the file has no extension (it hasn't got a FileTypeAttribute associated to it) the text/html Content Type is set by default.

Note that some documents, like JPG images can be displayed in IE using "text/html" Content-Type, but in Netscape and Mozilla Navigators the right Content-Type to show those images is "image/jpeg".  So, using those navigators, you should use some of the techniques described above, to allow the blob to have its corresponding Content-Type.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies both at run-time and at design-time.


|  |
| --- |
| **Backlinks** |
| [Category:Attribute definition](https://wiki.genexus.com/commwiki/wiki?6802) | [Blob data type](https://wiki.genexus.com/commwiki/wiki?6704) |

---
