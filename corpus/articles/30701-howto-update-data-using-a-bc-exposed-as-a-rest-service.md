---
title: "HowTo: Update data using a BC exposed as a Rest service"
source_id: 30701
source_url: https://wiki.genexus.com/commwiki/wiki?30701
genexus_version: "18"
---

# HowTo: Update data using a BC exposed as a Rest service

This document explains how to update data using a [Business Component](https://wiki.genexus.com/commwiki/wiki?5846) exposed as a [Rest web services in GeneXus](https://wiki.genexus.com/commwiki/wiki?28213) in GeneXus.

First, see the basic guidelines:

#### [**1. How are the Rest services called in GeneXus?**](#1.+How+are+the+Rest+services+called+in+GeneXus%3F)

Use the [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932).

#### [**2. What are the HTTP methods used to update data?**](#2.+What+are+the+HTTP+methods+used+to+update+data%3F)

Two methods have to be executed:

1. Get the data using its PK with the HTTP GET verb and keep the MD5 hash associated with the data. It's very similar to what is explained in [HowTo: Retrieve data from a BC exposed as a Rest service](https://wiki.genexus.com/commwiki/wiki?30699).
2. Update the data using the HTTP PUT verb. In addition to all the data of the table structure, the gx\_md5\_hash has to be included in the body of the HTTP Request. The reason is that you must mimic the pseudo-conversational dialog used by GeneXus when using the Transaction. To update a record you need to use the HTTP PUT verb with the entire Business Component structure in the body including the Hash value. The hash value is used for concurrency control. The body of the message should be in JSON format and contain the structure of the Business Component as it comes when it makes an HTTP GET.  
   Similar to the HTTP POST, the PK values have to be added to the query string when the HTTP PUT verb is executed.

### [Samples](#Samples)

Suppose you need to update an Invoice (which is a two-level transaction). Note that the BC is exposed as a Rest Service.

`[imagen omitida: wiki id 30723]`

In this example, the Invoice is updated by adding a new line to it.

As explained before, there are two steps to follow:

1. GET the record that's going to be updated (InvoiceId=1), and retrieve the gx\_md5\_hash data along with all the other data of the record. The data is retrieved using the &HTTClient.ToString method, and temporarily stored in a string variable called &result.

   ```
   &httpclient.Host= &server
   &httpclient.Port = &port
   &httpclient.BaseUrl = &urlbase
   &httpclient.Execute('GET','Invoice/1')

   if &httpclient.StatusCode = 200
       &result = &httpclient.ToString()
   else
      msg("There was an error retrieving the data: " + &httpclient.StatusCode.ToString())
   endif
   ```
2. Add the previous code to the code to retrieve the HTTP response after getting the data (including the HASH data) and store it in an SDT structure. This structure looks as follows (it's based on the Invoice structure, but it also includes a field for the gx\_md5\_hash):

`[imagen omitida: wiki id 30725]`

```
&httpclient.Host= &server
&httpclient.Port = &port
&httpclient.BaseUrl = &urlbase
&httpclient.Execute('GET','Invoice/1')

if &httpclient.StatusCode = 200
    &result = &httpclient.ToString()

    &invoicesdt.FromJson(&result)  //&invoicesdt already contains the gx_md5_hash information loaded

    &invoicesdtlevel = new()  //Adding a new line...
    &invoicesdtlevel.InvoiceLineCod = 4
    &invoicesdtlevel.ProductCod = 1
    &invoicesdt.InvoiceLevel.Add(&invoicesdtlevel)
    
    &addstring = &invoicesdt.ToJson() //to JSON format..
    &httpclient.AddString(&addstring)
    &httpclient.AddHeader('content-type','application/json') //Adding the necessary headers
    &httpclient.Execute('PUT','Invoice/1')

   if &httpclient.StatusCode = 200
       msg("Data successfully added")
   else
       msg("There was an error udapting the data: " + &httpclient.StatusCode.ToString())
    endif

else
   msg("There was an error retrieving the data: " + &httpclient.StatusCode.ToString())
endif
```

Note that in this example, the PK is sent in the body as well. This is necessary until [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?20247,,) only.

Download the sample from [Sample Update Rest services](https://wiki.genexus.com/commwiki/wiki?30727,,)

**Notes:**

* If more than one parameter should be passed in the URL (a compound PK), they need to be separated by commas.
* If the URI service is *http://localhost/TestRESTFullGX.NetEnvironment/rest/Product*, the BASE URL is: */TestRESTFullGX.NetEnvironment/rest/*
* Error handling is managed by querying the HTTP Status Code after the invocation.

### [Troubleshooting](#Troubleshooting)

#### [**1. If the execution throws the error:**](#1.+If+the+execution+throws+the+error%3A)

*{"error":{"code":"500","message":"The incoming message has an unexpected message format 'Raw'. The expected message formats for the operation are '**Xml**'; '**Json**'. This can be because a WebContentTypeMapper has not been configured on the binding. See the documentation of WebContentTypeMapper for more details."}}*

The reason is that you missed the appropriate header in the request. Add 'content-type: application/json' header.

* Using the [TCPtrace](http://www.tcptrace.org/) or any other similar tool is very useful to see the HTTP traffic and detect any possible failures. It's very easy to use as it works like a proxy. Just redirect the call to the port and host where TCPtrace listens and the TCPtrace should point to your service URL.
* In addition, if you need more information about any error, you can print the output of the call, using the following HTTPClient data type methods:

```
    &httpclient.Execute('PUT','Invoice/1')
    &httpstatus = &httpclient.StatusCode
    msg('Http status: ' + &httpstatus,status)
    &result = &httpclient.ToString()
    msg('Output: ',status)
    msg('=========',status)
    msg(&result,status)
```

The following would be printed:

```
Http status: 200
Output:
=========
{"InvoiceCod":1,"InvoiceDate":"2016-03-01","CustomerCod":"C56A4180-65AA-42EC-A945-5FD21DEC0538","CustomerName":"juan","InvoiceLevel":[{"InvoiceLineCod":1,"ProductCod":1,"ProductName":"product1","ProductPrice":12.0000},{"InvoiceLineCod":4,"ProductCod":1,"ProductName":"product1","ProductPrice":12.0000}],"gx_md5_hash":"4C921FA040E330D0EF68F96354420A79"}
```

**Note**: GeneXus provides the [OpenAPI import tool](https://wiki.genexus.com/commwiki/wiki?31864) for consuming a Rest service, whether it's been generated by GeneXus or not.


|  |
| --- |
| **Backlinks** |
| [Toc:Rest web services in GeneXus](https://wiki.genexus.com/commwiki/wiki?28213) |

---
