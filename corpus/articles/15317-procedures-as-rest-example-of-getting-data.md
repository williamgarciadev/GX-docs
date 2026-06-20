---
title: "Procedures as REST: Example of getting data"
source_id: 15317
source_url: https://wiki.genexus.com/commwiki/wiki?15317
genexus_version: "18"
---

# Procedures as REST: Example of getting data

The following example shows a REST GeneXus procedure that returns information about a Customer, given its Identification.

The GeneXus procedure (called "GetCustomer") is declared as REST by setting the following properties:

* Expose as web service = True
* Rest Protocol = True

`[imagen omitida: wiki id 15324]`

The code is very simple, as shown below:

Parm Rule:

```
parm(in:&CustomerId,out:&CustomerName,out:&CustomerBirthDate,out:&CustomerPayDate);
```

Source Code:

```
for each
 where CustomerId = &CustomerId
 &customerName = CustomerName
 &CustomerBirthDate = CustomerBirthDate
 &CustomerPayDate = CustomerPayDate
endfor
```

The GeneXus client can be as follows:

```
&httpclient.Host =&host // &httpclient is an HTTPClient variable data type
&httpclient.Port = &port
&httpclient.BaseUrl = &baseurl //Example: /webappname/rest/
 
&customersdt.CustomerId= &customerId
&body = &customersdt.ToJson()
 
&httpclient.AddHeader('Content-type','application/json')
&httpclient.AddString(&body)
 
&httpclient.Execute('POST','GetCustomer')
 &lvc = &httpclient.ToString()
```

Since the response is in Json format:

{"CustomerBirthDate":"1989-06-03","CustomerName":"Francisco","CustomerPayDate":"1995-03-21T18:54:00"}

the result should be processed using , loading the Json response in an SDT ([Structure SDT Object](https://wiki.genexus.com/commwiki/wiki?10021)) with the corresponding structure.

#### [**Notes:**](#Notes%3A)

* The Json code (in the example, the variable *&body*) must include only the items declared as parameters in the parm rule.
* The values in the Json code have to be CamelCase as defined in the parm rule of the REST procedure.

#### [How is a REST procedure object called from a general REST client?](#How+is+a+REST+procedure+object+called+from+a+general+REST+client%3F)

In general, set the following:

|  |  |
| --- | --- |
|  | Sample |
| URL | http://localhost:8080/applicationname/rest/GetCustomer |
| Body parameter | Content-Type: application/json; charset=UTF-8  {"CustomerId":1} |
| Method | Post |

`[imagen omitida: wiki id 26280]`

Based on the example that calls a 'GetCustomer' object, a sample request is as follows:

```
POST /Demo20140425U4JavaScriptEnvironment1/rest/GetCustomer HTTP/1.1
Content-Length: 17
Content-Type: application/json; charset=UTF-8
Host: localhost:8181
Connection: Keep-Alive
User-Agent: Apache-HttpClient/4.3.1 (java 1.5)
{"CustomerId":1}
```

And the response is as follows:

```
HTTP/1.1 200 OK
Server: Apache-Coyote/1.1
Set-Cookie: JSESSIONID=D737067FECD79CD466F29877D3B74375; Path=/Demo20140425U4JavaScriptEnvironment1/; HttpOnly
Last-Modified: Wed, 23 Jul 2014 06:29:04 GMT
Content-Type: application/json;charset=UTF-8
Transfer-Encoding: chunked
Date: Wed, 23 Jul 2014 06:29:05 GMT

58
{"CustomerName":"miura","CustomerBirthDate":"2014-07-01","CustomerPayDate":"2014-07-01"}
0
```

### [See Also](#See+Also)

[Rest web services in GeneXus](https://wiki.genexus.com/commwiki/wiki?28213)


|  |
| --- |
| **Backlinks** |
| [REST Protocol property](https://wiki.genexus.com/commwiki/wiki?37254) | [Toc:Rest web services in GeneXus](https://wiki.genexus.com/commwiki/wiki?28213) |

---
