---
title: "HowTo: Download a file using HTTP Protocol"
source_id: 14144
source_url: https://wiki.genexus.com/commwiki/wiki?14144
genexus_version: "18"
---

# HowTo: Download a file using HTTP Protocol

This article describes how to manage file downloads easily in your application.

If you want a user event to prompt the user to save or run a file like the following:

`[imagen omitida: wiki id 14147]`

All you need to do is:

* Create a
  [Procedure](https://wiki.genexus.com/commwiki/wiki?6293) with the following property values:
  + [Main program property](https://wiki.genexus.com/commwiki/wiki?7407) = TRUE
  + [Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947) = HTTP

To add data to the Http response header, the GeneXus object should be callable using the Http protocol. To make a procedure callable by the Http protocol, the above setting is necessary.  
Below is a sample for downloading a file.

### [Procedure Source](#Procedure+Source)

```
/*
Get &contenttype, &filename and &filepath from the context (Websession, Database, etc). 
Do not receive them via parm because of security reasons (Path transversal).
*/
&HttpResponse.AddHeader(!"Content-Type", &contenttype) //&contenttype could be 'application/x-zip-compressed'
&HttpResponse.AddHeader(!"Content-Disposition", !"attachment;filename="+&filename) //&filename could be 'download.zip'
&HttpResponse.AddFile(&filepath) //&filepath could be 'C:\temp\download.zip'
&HttpResponse.AddHeader(!"Pragma", !"public")
&HttpResponse.AddHeader(!"Cache-Control", !"max-age=0")
```

### [How to Call the Download within GeneXus:](#How+to+Call+the+Download+within+GeneXus%3A)

```
Event 'Download'
  ProcedureHTTPDownload.Link()   
EndEvent
```

### [Considerations](#Considerations)

Be sure that the application has full access to *&filepath*. It will fail if the application cannot access to the *&filepath* (if not, it will throw Access Denied Exception)

### [See Also](#See+Also)

[Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947)


|  |
| --- |
| **Backlinks** |
| [Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947) |

---
