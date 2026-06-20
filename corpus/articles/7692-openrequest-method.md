---
title: "OpenRequest method"
source_id: 7692
source_url: https://wiki.genexus.com/commwiki/wiki?7692
genexus_version: "18"
---

# OpenRequest method

When used with the XmlWriter extended data type, it sends an XML in the http request´s body. When used with the XmlReader extended data type, it is used in a web procedure (WebProc, procedure "main" and HTTP protocol) to read an XML included in the http request´s body.

### [Syntax](#Syntax)

*XmlDataType*.**OpenRequest**(HttpRequest)

**Where:**

*XmlDataType*  
     is XmlReader or XmlWriter extended data type.

### [Scope](#Scope)

**Extended data types:** [XMLWriter Data Type](https://wiki.genexus.com/commwiki/wiki?6938), [XMLReader Data Type](https://wiki.genexus.com/commwiki/wiki?6928)  
**Generators:** 
[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892),
[Java](https://wiki.genexus.com/commwiki/wiki?12258),
Ruby (up to GeneXus X Evolution 3),
Visual FoxPro (up to GeneXus X Evolution 3)

### [Samples](#Samples)

Client program:

```
// &Client is HttpClient type
// &Writer is XMLWriter type
// &Reader is XMLReader type

// Define the host and the the port where make the request
&client.host = "localhost"
&client.port = 88

// Adding the XML to request
&Writer.openRequest(&Client)
&Writer.WriteStartElement("Parameters")
&Writer.WriteElement("a", &A)
&Writer.WriteElement("b", &B)
&Writer.WriteEndElement()
&Writer.Close()

// Make POST to the WebProc
&Client.Execute("POST", "/servlet/awebproc")

// Read the XML than return and loaded in the internal variables
&Reader.OpenResponse(&client)
&Reader.Read()
&Reader.Read()

&a = Val(&Reader.Value)
&Reader.Read()   
&b = Val(&Reader.Value)
&Reader.Close()
```

Program server (WebProc):

```
// &Request is HttpRequest type
// &Response is HttpResponse type
// &Writer is XMLWriter type
// &Reader is XMLReader type

// Read the XML's parameters
&Reader.OpenRequest(&Request)
&Reader.Read()
&Reader.Read()
&a = Val(&Reader.Value)
&reader.read()   
&b = Val(&Reader.Value)
&Reader.Close()

// Add 1 to each value
&a = &a + 1 &b = &b + 1

// Write parameters into response
&Writer.openResponse(&Response)
&Writer.WriteStartElement("Parameters")
&Writer.WriteElement("a", &a)
&Writer.WriteElement("b", &b)
&Writer.WriteEndElement()
&Writer.Close()
```

### [See Also](#See+Also)

[ExcelDocument data type](https://wiki.genexus.com/commwiki/wiki?2476)  
[WordDocument Data Type](https://wiki.genexus.com/commwiki/wiki?2478,,)  
[XMLWriter Data Type](https://wiki.genexus.com/commwiki/wiki?6938)  
[XMLReader Data Type](https://wiki.genexus.com/commwiki/wiki?6928)


|  |
| --- |
| **Backlinks** |
| [XMLWriter Data Type](https://wiki.genexus.com/commwiki/wiki?6938) |

---
