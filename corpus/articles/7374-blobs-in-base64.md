---
title: "Blobs in Base64"
source_id: 7374
source_url: https://wiki.genexus.com/commwiki/wiki?7374
genexus_version: "18"
---

# Blobs in Base64

The following functions get and set a Blob file content in Base64:

* ToBase64String(): Returns Blob file content in Base64.
* FromBase64String(): Loads the content in Base64 received by parameter into the Blob file.

These functions may be used as follows:

```
ContentBase64 = <att | var>.ToBase64String()
```

```
<att | var>.FromBase64String(ContentBase64)
```

ContentBase64 contains the Base64 content and could be a LongVarChar, for instance.

So far, when a Web Service with a returning Blob parameter is called, the returned value will be the Blob's file content in Base64.

```
ContentBase64 = WebServiceBlob.Execute()
```

## [Sample](#Sample)

This is an example showing how to transfer a file in Base64 format using the [File data type](https://wiki.genexus.com/commwiki/wiki?6915) and [Blob data type](https://wiki.genexus.com/commwiki/wiki?6704):

```
&File.Source = !"c:\temp\xpz\1.gif"

if &File.Exists()
 // Emulate sender
 &Blob = &File.GetAbsoluteName()
 &Content64 = &Blob.ToBase64String()
 msg(format(!"Base64 %1", &Content64),nowait)
 
 // Emulate receiver
 &File2.source = !"c:\temp\xpz\1a.gif"
 If not &File2.Exists()
  &File2.Create()
 EndIf

 &File2.FromBase64String(&Content64) // to another file
 &File2.Close()
 
 msg(format(!"Result in %1", &File2.GetAbsoluteName()),nowait)
else    
 msg(format(!"%1 does not exist", &File.Source),nowait)
endif
```

## [See Also](#See+Also)

[Blob data type](https://wiki.genexus.com/commwiki/wiki?6704)


|  |
| --- |
| **Backlinks** |
| [Blob data type](https://wiki.genexus.com/commwiki/wiki?6704) |

---
