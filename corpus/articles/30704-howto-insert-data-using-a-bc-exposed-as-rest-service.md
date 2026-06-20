---
title: "HowTo: Insert data using a BC exposed as Rest service"
source_id: 30704
source_url: https://wiki.genexus.com/commwiki/wiki?30704
genexus_version: "18"
---

# HowTo: Insert data using a BC exposed as Rest service

This document explains how to insert new data using a [Business Component](https://wiki.genexus.com/commwiki/wiki?5846) exposed as a Rest web service in GeneXus.

First, see the basic guidelines:

#### [**1. How are the Rest services called in GeneXus?**](#1.+How+are+the+Rest+services+called+in+GeneXus%3F)

Use the HttpClient data type.

#### [**2. Which HTTP method is used to insert new data?**](#2.+Which+HTTP+method+is+used+to+insert+new+data%3F)

The HTTP method used for inserting new data is the HTTP POST method.

#### [**3. How are the parameters going to be passed in the call?**](#3.+How+are+the+parameters+going+to+be+passed+in+the+call%3F)

All the parameters for inserting new data using the BC (except the PK parameters) need to be included in the body of the HTTP request. The message body should be in JSON format and contains the structure of the Business Component as it comes when it makes an HTTP GET.

The easiest way to build the body with the correct format is by defining a [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021) based on the BC structure and using the method to format it to a valid JSON string.

That JSON string needs to be added to the body of the HTTP request before executing the POST to the service.

#### [**4. Which is the URL format to execute the POST?**](#4.+Which+is+the+URL+format+to+execute+the+POST%3F)

*<server uri>/rest/<module>/<bc name>/<param1>,<param2>,..,<paramN>*

**Where:**

*<param1>,<param2>,..,<paramN>*  
      Is the compound Primary Key.

If the Primary Key is autonumbered, just use 0 in the URL.

### [Samples](#Samples)

Consider the Product Business Component Transaction that is exposed as a Rest web service, as shown in the figure below:

`[imagen omitida: wiki id 30705]`

In this example, you want to insert a new Product, whose ProductId is 5.

#### [Sample code](#Sample+code)

You have defined a ProductSDT Structured Data Type based on the Product structure, as shown in the figure below:

`[imagen omitida: wiki id 30706]`

Then, the code would be as follows:

```
&httpclient.Host= &server
&httpclient.Port = &port
&httpclient.BaseUrl = &urlbase

&productSDT.ProductName = "Samsung Galaxy"
&productSDT.ProductPrice = 22

&httpclient.AddString(&productSDT.ToJson())
&httpclient.AddHeader('content-type','application/json')
&httpclient.Execute('POST','Product/5')

if &httpclient.StatusCode = 201
    msg("Data successfully added")
else
   msg("There was an error retrieving the data: " + &httpclient.StatusCode.ToString())
endif
```

Download the sample from [Sample insert data using a Rest BC](https://wiki.genexus.com/commwiki/wiki?30732,,)

**Notes:**

* Do not forget to add the *'content-type:application/json'* header.
* If more than one parameter should be passed in the URL (a compound PK), they need to be separated by commas.
* If the service URI is *http://localhost/TestRESTFullGX.NetEnvironment/rest/Product*, the BASE URL is: */TestRESTFullGX.NetEnvironment/rest/*
* Error handling is managed by querying the HTTP Status Code after the invocation.

### [See Also](#See+Also)

[Business Components as Rest web services in GeneXus](https://wiki.genexus.com/commwiki/wiki?28214)


|  |
| --- |
| **Backlinks** |
| [OpenAPI import tool](https://wiki.genexus.com/commwiki/wiki?31864) | [OpenAPI import tool (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54370) |
| [Toc:Rest web services in GeneXus](https://wiki.genexus.com/commwiki/wiki?28213) |

---
