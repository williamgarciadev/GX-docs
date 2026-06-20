---
title: "FileURI property"
source_id: 39979
source_url: https://wiki.genexus.com/commwiki/wiki?39979
genexus_version: "18"
---

# FileURI property

Sets/Gets the FileURI.

### [Scope](#Scope)

**Level:** [Attribute](https://wiki.genexus.com/commwiki/wiki?7240), [SDT member](https://wiki.genexus.com/commwiki/wiki?10021)

### [Description](#Description)

This property is available for attributes based on the [BlobFile data type](https://wiki.genexus.com/commwiki/wiki?40420) as well as for members of [Structured Data Types](https://wiki.genexus.com/commwiki/wiki?10021) based on the [BlobFile data type](https://wiki.genexus.com/commwiki/wiki?40420), too.

**Set**:  
You can set a relative path. It will be resolved within the current host.  
You can set a local path by using file:// protocol  
When you set the URI property, the internal binary file stored in the DB will be set to empty.

**Get**:

It always returns the absolute URI to the file.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at runtime.

### [Samples](#Samples)

Procedure:

```
&Blobfile.FileURI = "http://www.myfiles/file.pdf"
```

Data Provider:

```
{
   MyBlobFile
   {
      FileUri = "http://www.myfiles/file.pdf"
   }
}
```

### [See Also](#See+Also)

[BlobFile data type](https://wiki.genexus.com/commwiki/wiki?40420)


|  |
| --- |
| **Backlinks** |
| [FromURL method](https://wiki.genexus.com/commwiki/wiki?9644) |

---
