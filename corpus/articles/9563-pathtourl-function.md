---
title: "PathToURL function"
source_id: 9563
source_url: https://wiki.genexus.com/commwiki/wiki?9563
genexus_version: "18"
---

# PathToURL function

Converts a path (typically the Blob local storage path) into a URL, returning the URL under which the Blob content is accessible in the Web Server.

### [Syntax](#Syntax)

**PathToURL(***BlobAttribute***)**

**Where:**  
  
*BlobAttribute*  
    Must be a variable or attribute of Blob data type (or based on an attribute or domain of Blob data type).

**Type Returned:**  
Character (URL)

### [Scope](#Scope)

**Objects**:[Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604), 
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

It returns the URL under which the Blob content is accessible in the Web Server. You can use this function in cases where you need to know this URL. For example, when loading an image with the [LoadBitmap function](https://wiki.genexus.com/commwiki/wiki?8458,,):

```
&Url = PathToUrl(BlobAttribute)
&Logo = LoadBitmap(&Url)
```

### [Samples](#Samples)

Suppose the web application is stored in c:\webapp, and the [Blob local storage directory property](https://wiki.genexus.com/commwiki/wiki?6979) is set to c:\webapp\dir, and the URL of the application is http://server/webapp/myapp.aspx.

Variable Type:

```
&AttBlob //Blob (based on AttBlob which is of the Blob type)
&URL //C(2048)
```

Source:

```
for each where ...
    &AttBlob = AttBlob
endfor
&URL = PathToURL(&AttBlob)
```

Then, &URL will contain something like http://server/webapp/dir/file1234.jpg.

### [See Also](#See+Also)

[Blob data type](https://wiki.genexus.com/commwiki/wiki?6704)


|  |
| --- |
| **Backlinks** |
| [Blob data type](https://wiki.genexus.com/commwiki/wiki?6704) | [Security Scanner built-in tool](https://wiki.genexus.com/commwiki/wiki?46412) |
| [Security Scanner built-in tool (GeneXus 18 or prior)](https://wiki.genexus.com/commwiki/wiki?52570) |

---
