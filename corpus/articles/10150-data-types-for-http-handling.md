---
title: "Data Types for Http Handling"
source_id: 10150
source_url: https://wiki.genexus.com/commwiki/wiki?10150
genexus_version: "18"
---

# Data Types for Http Handling

#### [Scope](#Scope)

**Objects:** [Procedures](https://wiki.genexus.com/commwiki/wiki?6293), [Transactions](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panels](https://wiki.genexus.com/commwiki/wiki?6916)  
**Languages:** .NET, Java, Visual Basic, Visual FoxPro

#### [Purpose](#Purpose)

In order to handle HTTP protocol GeneXus provides the following [data types](https://wiki.genexus.com/commwiki/wiki?6560):

* [HttpClient](https://wiki.genexus.com/commwiki/wiki?6932), which allows you to build a request, send it to a URL and read the results.
* [HttpResponse](https://wiki.genexus.com/commwiki/wiki?6934) and [HttpRequest](https://wiki.genexus.com/commwiki/wiki?6933), which allow you to read the request's data and record the response.

#### [Interaction with XML](#Interaction+with+XML)

These objects enable interaction with XMLReader and XMWriter objects. The following methods are used for this:

&XMLReader.openResponse(HttpClient)  
It is used in any object to read whatever was returned by a request as XML.

&XMLWriter.openRequest(HttpClient)  
It is used to send an XML in the body of an http request.

&XMLWriter.openResponse(HttpResponse)  
It is used to write an xml which will be returned in the body of the http response.

&XMLReader.openRequest(HttpRequest)  
It is used to read an xml which comes in the body of the http request.

#### [Example](#Example)

This example shows how a GeneXus object calls another one via http, by transferring its parameters in an XML and by receiving the same also in an XML.

The XML to be sent has the following format:

<parameters>  
   <a>value</a>  
   <b>value</b>  
</parameters>

The returned XML is the same, with the  ‘A’ and ‘B’ values modified.

##### [The 'Client' Program will be the following:](#The+%27Client%27+Program+will+be+the+following%3A)

&Client,  HttpClient type  
&Writer,  XMLWriter type  
&Reader, XMLReader type

```
// Defines the host and the port to which the request will be made  
&client.host = "localhost"
&client.port = 88  

// Adds the XML to the request
&writer.openRequest(&client)
&writer.WriteStartElement("parameters")
&writer.WriteElement("a", &A)
&writer.WriteElement("b", &B)
&writer.WriteEndElement()
&writer.close()

// Makes the POST to the webproc
&client.execute("POST", "/servlet/awebproc")

// Reads the returned XML and load it in the internal variables.   
&reader.openResponse(&client)
&reader.read()

&reader.read()
&a = val(&reader.value)

&reader.read()    
&b = val(&reader.value)

&reader.close()
```

##### [The 'Server' Program will be the following WebProc:](#The+%27Server%27+Program+will+be+the+following+WebProc%3A)

&Request,   HttpRequest type  
&Response, HttpResponse type  
&Writer,      XMLWriter type  
&Reader,     XMLReader type

```
// Reads the XML parameters. 
&reader.openRequest(&Request)
&reader.read()
&reader.read()
&a = val(&reader.value)
&reader.read()    
&b = val(&reader.value)
&reader.close()

// Adds one to each value  
&a = &a + 1
&b = &b + 1

// Records the parameters in the response
&writer.openResponse(&Response)
&writer.WriteStartElement("parameters")
   &writer.WriteElement("a", &A)
   &writer.WriteElement("b", &B)
&writer.WriteEndElement()

&writer.close()
```

#### [See Also](#See+Also)

[XmlReader](https://wiki.genexus.com/commwiki/wiki?6928)  
[XmlWriter](https://wiki.genexus.com/commwiki/wiki?6938)
