---
title: "Resource Name Property"
source_id: 11434
source_url: https://wiki.genexus.com/commwiki/wiki?11434
genexus_version: "18"
---

# Resource Name Property

The ResourceName property allows you to indicate the object to be run upon calling a service. In this use scenario you can run a Web Service generated with different generators.

### [Syntax](#Syntax)

**&***DataType***.ResourceName**  
  
**Type Returned:**   
Numeric

### [Description](#Description)

It means that you could change the webservice name, programming the location datatype or using the location.xml.

For example if you have the same webservices provided in Net and Java , in the following urls:

```
http://server1:port1/app/awebservice.aspx       (Net Url)
http://server2:port2/app/servlet/awebservice    (Java Url)
```

Yuu could inspect the Java Wsdl implementation of the webservice in order to create the external object (http://server2:port2/app/servlet/awebservice?wsdl). And after that invoke the Net implementation, just programming

```
&location = getlocation( '<External_Object_Name>' ) // get location information
&location.host = "server1"
&location.port = port1
&location.BaseUrl = "/app/"
....
&location.ResourceName = "awebservice.aspx" // set the ObjectName to call if needed.
```

```
<GXLocations>
       <GXLocation name="<External_Object_Name>">
            <Common>
                 <Host>server1</Host>
                 <port>port1</port>
                 <BaseURL>/app/</BaseURL>
                 ....
                 <ResourceName>awebservice.aspx</ResourceName>
           </Common>
       </GXLocation>
</GXLocations>
```

### [Scope](#Scope)

**Data Type:** [Location](https://wiki.genexus.com/commwiki/wiki?6981)  
**Languages:** .NET, Java

### [See Also](#See+Also)

[Location Data Type](https://wiki.genexus.com/commwiki/wiki?6981)  
[Locations](https://wiki.genexus.com/commwiki/wiki?6981)


|  |
| --- |
| **Backlinks** |
| [Location data type](https://wiki.genexus.com/commwiki/wiki?6981) |

---
