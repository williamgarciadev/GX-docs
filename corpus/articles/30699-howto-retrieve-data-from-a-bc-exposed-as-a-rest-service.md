---
title: "HowTo: Retrieve data from a BC exposed as a Rest service"
source_id: 30699
source_url: https://wiki.genexus.com/commwiki/wiki?30699
genexus_version: "18"
---

# HowTo: Retrieve data from a BC exposed as a Rest service

This document explains how to retrieve data from a [Business Component](https://wiki.genexus.com/commwiki/wiki?5846) exposed as a [Rest web services in GeneXus](https://wiki.genexus.com/commwiki/wiki?28213).

First, see the basic guidelines:

#### [**1. How are the Rest services called in GeneXus?**](#1.+How+are+the+Rest+services+called+in+GeneXus%3F)

Use the [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932).

#### [**2. Which HTTP method should be used to retrieve the data?**](#2.+Which+HTTP+method+should+be+used+to+retrieve+the+data%3F)

The HTTP method used for retrieving the data is the GET HTTP method.

#### [**3. What kind of information is exposed by the web service, so it can be consumed?**](#3.+What+kind+of+information+is+exposed+by+the+web+service%2C+so+it+can+be+consumed%3F)

You can get a record by giving its Primary Key.

However, since [GeneXus X Evolution 2](https://wiki.genexus.com/commwiki/wiki?15152,,) you *cannot* retrieve all the data of a table (you can't execute a GET of all the records, e.g: <url base>/rest/Products), nor get the data from a given Foreign Key (<url base>/rest/Invoices?ClientId=234), or the data for a given Description Attribute (e.g:<url base>/rest/Products?ProductName=SmartPhone). This restriction on the information provided by the Rest BC is due to security reasons.

#### [**4. Which is the URL format to execute the GET?**](#4.+Which+is+the+URL+format+to+execute+the+GET%3F)

*<server uri>/rest/<module>/<bc name>/<param1>,<param2>,..,<paramN>*

**Where:**

*<param1>,<param2>,..,<paramN>*   
      Is the compound Primary Key.

### [Samples](#Samples)

The following figure shows the Invoice Business Component transaction that is exposed as a Rest web service:

`[imagen omitida: wiki id 30703]`

In this example, we want to get the Invoice whose InvoiceId=5

#### [Sample code](#Sample+code)

```
&httpclient.Host= &server
&httpclient.Port = &port
&httpclient.BaseUrl = &urlbase
&httpclient.Execute('GET','Invoice/5')

if &httpclient.StatusCode = 200
    &result = &httpclient.ToString()
else
   msg("There was an error retrieving the data: " + &httpclient.StatusCode.ToString())
endif
```

Download the sample from [Sample GET data using a Rest BC](https://wiki.genexus.com/commwiki/wiki?30733,,)

**Notes:**

* If more than one parameter should be passed in the URL, they need to be separated by commas.
* If the service URI is *http://localhost/TestRESTFullGX.NetEnvironment/rest/Invoice*, the BASE URL is: */TestRESTFullGX.NetEnvironment/rest/*
* Error handling is managed by querying the HTTP Status Code after the invocation. For example, this error can occur if the data doesn't exist: {"error":{"code":"404","message":"Data with the specified key could not be found."}}.

### [See Also](#See+Also)

[Business Components as Rest web services in GeneXus](https://wiki.genexus.com/commwiki/wiki?28214)


|  |
| --- |
| **Backlinks** |
| [HowTo: Update data using a BC exposed as a Rest service](https://wiki.genexus.com/commwiki/wiki?30701) | [Toc:Rest web services in GeneXus](https://wiki.genexus.com/commwiki/wiki?28213) |

---
