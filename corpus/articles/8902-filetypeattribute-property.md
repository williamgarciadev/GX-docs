---
title: "FileTypeAttribute property"
source_id: 8902
source_url: https://wiki.genexus.com/commwiki/wiki?8902
genexus_version: "18"
---

# FileTypeAttribute property

Identifies an attribute that holds the extension of a Blob data type attribute.

### [Description](#Description)

It is available only for [Blob data type](https://wiki.genexus.com/commwiki/wiki?6704) attributes. The possible values for this property are any [Character data type](https://wiki.genexus.com/commwiki/wiki?6777) or [VarChar data type](https://wiki.genexus.com/commwiki/wiki?6778) attribute of the same table which the Blob attribute belongs to.

A Blob data type attribute may store files. Those files may be all of the same type (i.e. Word documents, pictures in a specified format, etc.) or heterogeneous. When working with heterogeneous files you should store the "file type" (extension) in a different attribute (because the extension isn't stored with the blob itself). In other words, the Blob data type attribute stores the file content and the File Type Attribute stores the file type (or extension).

Examples:

TXT      
RTX      
HTML (or HTM)  
XML      
AIF      
AU      
WAV      
BMP      
GIF      
JPE (or JPEG, JPG  )    
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

Every time the Blob data type attribute is assigned (either in the user interface or by an assignment command) the value of the FileTypeAttribute is automatically assigned too. That is to say that, the File Type Attribute is assigned when you upload a blob from a Web Interface (a Web Transaction), a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293), or a [Business Component](https://wiki.genexus.com/commwiki/wiki?5846) in a batch mode (from a Procedure). The default value is (none), stating that no attribute holds the file type.

Constraints on the File Type Attribute:

* It must be of Character or VarChar (not [LongVarChar data type](https://wiki.genexus.com/commwiki/wiki?7371)).
* It must belong to the same table the referencing attribute belongs to.
* It should not be a [formula](https://wiki.genexus.com/commwiki/wiki?5861).
* It cannot be used as the FileTypeAttribute or FileNameAttribute of any other Blob attribute.
* Not Supported for GUI applications.

#### [Note](#Note)

If the File Type Attribute property is assigned with any value, the corresponding attribute assigned to this property cannot be explicitly modified through a web transaction.


|  |
| --- |
| **Backlinks** |
| [Category:Attribute definition](https://wiki.genexus.com/commwiki/wiki?6802) | [Blob data type](https://wiki.genexus.com/commwiki/wiki?6704) | [FileType property](https://wiki.genexus.com/commwiki/wiki?3116) |

---
