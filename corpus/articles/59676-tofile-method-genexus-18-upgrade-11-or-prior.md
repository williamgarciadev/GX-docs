---
title: "ToFile method (GeneXus 18 Upgrade 11 or prior)"
source_id: 59676
source_url: https://wiki.genexus.com/commwiki/wiki?59676
genexus_version: "18"
---

# ToFile method (GeneXus 18 Upgrade 11 or prior)

Returns all the HTML body in a File.

### [Syntax](#Syntax)

**&***VarBasedOnExtendedDataType***.ToFile(***FileName***)**  
  
**Where:**  
  
*FileName*  
     It is the path to the file.

### [Scope](#Scope)

**Extended Data Types:** [HttpClient](https://wiki.genexus.com/commwiki/wiki?6932), [HttpRequest](https://wiki.genexus.com/commwiki/wiki?6933)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Samples](#Samples)

**HttpClient:**

```
&httpclient.execute("GET","/servlet/clients")
&httpclient.ToFile(“c:\htmls\clients.html”)
```

It returns the HTML code of the webpanel clients in the clients.html file.

**HttpRequest:**

```
&httprequest.ToFile(“c:\files\clients.json”)
```

In a main procedure with call protocol HTTP, it saves a file received by a webservice call.

### [Security tips](#Security+tips)

Do not use user's inputs concatenations or sanitize the user's entries to avoid path traversal or path manipulation vulnerability risks.

### [See Also](#See+Also)

[HttpClient Data Type](https://wiki.genexus.com/commwiki/wiki?6932)  
[HttpRequest Data Type](https://wiki.genexus.com/commwiki/wiki?6933)  
[Execute method](https://wiki.genexus.com/commwiki/wiki?7047)
