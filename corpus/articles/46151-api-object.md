---
title: "API object"
source_id: 46151
source_url: https://wiki.genexus.com/commwiki/wiki?46151
genexus_version: "18"
---

# API object

Defines an Application Programming Interface for a set of programs like Data Providers or Procedures.

An API object groups several services that are semantically and functionally related. For each service, it declares a mapping between its external name (exposed as a service) and the internal implementation in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) (KB). It features flexibility in terms of service declaration, allowing the configuration of the HTTP method to be used when the service is REST. It also allows indicating the name and type of the parameters, offering great flexibility in parameter transformation.

It is meant for modeling an API mediation layer that clearly separates the interface from the implementation and so facilitates incremental development and the management of the evolution of an API.

### [API Interface](#API+Interface)

The API interface is declared in the 'Service Source' part of the object.

For each service of the interface, you can declare:

* Name
* Parameters
* Which GeneXus object contains the implementation and with what parameters it is called.
* Annotations for protocol-specific options.

#### [API Protocols](#API+Protocols)

The API object allows you to expose an API for the following protocols:

* REST
* gRPC (\*)

At the object level, you have properties to enable each of them.

(\*) The gRPC protocol is not supported in the [.NET Framework generator](https://wiki.genexus.com/commwiki/wiki?2892). It is in beta state in the [.NET](https://wiki.genexus.com/commwiki/wiki?38604) and [Java](https://wiki.genexus.com/commwiki/wiki?12258) generators.

### [API Object Events](#API+Object+Events)

Events can be defined in the 'Events' part of the object.

This is where you can do the following:

* Program data transformations to the service parameters, before and after calling the object that implements the service, which helps to maintain a stable API
* Manage traffic, analyze it, apply service policies. That is, for example, count service calls, log them, accept or deny access to your API.

For each API object, you can define a 'Before' and 'After' event, which will be executed before and after each service implementation.  
In addition, for each service you can define '<service name>.Before|After' events. So, every time a service is invoked, the following will be executed:

* Event 'Before'
* Event '<service>.Before'
* The object corresponding to the implementation of the service, referenced in the 'Service Source'
* Event '<service>.After'
* Event 'After'

Database access is not allowed in Events. That kind of logic should be placed in the called Procedures or Data Providers.

### [API object Variables](#API+object+Variables)

Here you can define the variables to be used in the 'Service Source' and 'Events'.

There are some standard variables of each API object:

* [&Pgmname](https://wiki.genexus.com/commwiki/wiki?8870) - It contains the name of the object.
* [&Pgmdesc](https://wiki.genexus.com/commwiki/wiki?7672) - It contains the description of the object.
* &RestMethod - It contains the [HTTP method](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?50500,,) with which the object was called. It is empty when the object is called using protocols other than REST.
* &RestCode - You may set it to customize the returned [HTTP Status Code](https://restfulapi.net/http-status-codes/).

  **Note**: The values that the &RestCode variable can take are those of the categories: 2xx and 4xx. For more information see [SAC #50865](https://www.genexus.com/developers/websac?en,,,50865).

### [API object Properties](#API+object+Properties)

These are the properties that can be set at the object level:

* Name
* Description
* [REST Protocol](https://wiki.genexus.com/commwiki/wiki?46380)
* [gRPC Protocol](https://wiki.genexus.com/commwiki/wiki?46381)
* [gRPC Package](https://wiki.genexus.com/commwiki/wiki?46382)
* [Generate OpenAPI interface property](https://wiki.genexus.com/commwiki/wiki?31859)
* OpenAPI version
* [Services base path](https://wiki.genexus.com/commwiki/wiki?46383)
* [Module/Folder](https://wiki.genexus.com/commwiki/wiki?25540)
* [Object Visibility](https://wiki.genexus.com/commwiki/wiki?22473)
* Miscellaneous
  + [Generate Object](https://wiki.genexus.com/commwiki/wiki?7633)
* Integrated Security
  + [Integrated Security Level](https://wiki.genexus.com/commwiki/wiki?15214)
  + [Permission Prefix](https://wiki.genexus.com/commwiki/wiki?17571)

## [Sample](#Sample)

This sample showcases the API called 'Client' with services to list clients, get details of a specific client, and insert a client.

This is the 'Service Source' part of the API object:

```
Client{

    List(out:&SDTClients) 
    => Core.ClientsList(&ClientCategoryCode,&SDTClients);

    GetByKey(in:&ClientId,out:&Client) 
    => Core.ClientGetbyKey(&ClientId,&Client);

    [RestMethod(POST)]
    Insert(in:&ClientId,in:&ClientName,in:&ClientAddress,out:&Messages) 
    => Core.ClientInsert(&ClientId,&ClientName,&ClientAddress,&Messages);
 }
```

Notes:

* When accessed through the Rest Protocol, List and GetByKey are accessed via HTTP 'GET' Method, and Insert is accessed via 'POST' declared with the '[RestMethod(POST)]' annotation.
* Service parameters have to be declared as in, out, or inout.
* Parameter mapping and parameter value transformations can be done using the 'Events' part as shown below.
* Overloading of services can be achieved in the REST interfaces by combining RestMethod and RestPath annotations.
* For the REST protocol, the URI is as shown below:  
  *URLBase/ModuleName/ApiObjectName/Method*  
  So, in this sample, it is similar to the following:  
  *URLBase/Core/Client/List*

Unless you use the "Services base path" property, where the URL is as shown:  
*URLBase/ServicesBasePath/Method*

* Objects referenced in the right part of each service are called using an internal protocol, even if they are exposed as services, or their [Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947) says different.

This is the 'Events' part:

```
Event Before
    Statsregister(&pgmname)
EndEvent

Event List.Before
    &ClientCategoryCode = 'Any'
EndEvent

Event Insert.Before
    if &ClientId <= 0
        &RestCode = 412
        return
    endif
EndEvent

Event GetByKey.After
    if &Client.ClientId = 0
        &Message.Type = MessageTypes.Error
        &Message.Description = format("Client %1 was not found",&ClientId)
        &Messages.Add(&Message)
        &RestCode = 404
    endif    
EndEvent
```

Notes:

* 'List.Before' initializes a variable that is not part of the API but that is required by the called object
* The Procedure associated with the Insert service (and the Insert.After event) in this sample will only be executed if &ClientId > 0

You can download the source of this sample from this article: [API Object Playground](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46152,,).

## [Consuming the ReST API](#Consuming+the+ReST+API)

When [Generate OpenAPI interface property](https://wiki.genexus.com/commwiki/wiki?31859) is enabled, GeneXus generates a .yaml with the OpenAPI specification for each API object. That file (named <apiobject's qualified name>.yaml) contains all the information related to the services exposed by the API.

Parameters in the query string (input parameters of the services) are named, separated by &, and are also case-sensitive in Java. Therefore, if you consume the API, make sure to name them using the casing declared in the .yaml so that your consumer does not depend on the generator used to provide the services.

## [General recommendations](#General+recommendations)

* To enable an API to be consumed via several protocols and guarantee multi-platform support, you should not overload the service name (you should not use the same service name for different services in an API).
* To avoid interface compatibility or stability problems, it is not recommended to use the same [Structured Data Type (SDT)](https://wiki.genexus.com/commwiki/wiki?10021) that is used in an API object in services of another type: such as Rest Data Providers, Rest Procedures or Rest Business Components, because there may be differences between the serialization of these services.  
    
  Example  
    
  In the example below, the SDT named SDTClients it is being called only by Core.ClientsList:  

  ```
       Client{
             List(out:&SDTClients)=> Core.ClientsList(&ClientCategoryCode,&SDTClients);
             }
  ```

* Currently, if you need to change the [Json Collection Serialization property](https://wiki.genexus.com/commwiki/wiki?48147) from Sequence to Wrapped, it can only be done at the SDT definition level. Therefore, if you need to control the JSON output of a collection, you must define the SDT as a collection, and not a variable marked as a collection in the API object.         
    
  Example  
    
  In the code shown below, the SDT named SDTClients is set to be a collection:  

  ```
      Client{
            List(out:&SDTClients)=> Core.ClientsList(&ClientCategoryCode,&SDTClients);
            }
  ```

  For more information, please refer to [ListCustomers service definition and declaration](https://wiki.genexus.com/commwiki/wiki?50051)

## [Troubleshooting](#Troubleshooting)

* When importing the YAML of an API Object into another KB using the [OpenAPI import tool](https://wiki.genexus.com/commwiki/wiki?31864), avoid defining variables based on SDTs marked as collections. Instead, create the variables and then mark them as collections in the API Object interface. If you do not follow this process, the generated procedures may cause cancellations during deserialization, indicating a problem with the SDT's JSON format.

## [Availability](#Availability)

* [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [.NET](https://wiki.genexus.com/commwiki/wiki?38604) generators support this object since [GeneXus 17](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46066,,).
* &RestCode standard variable has been added in [GeneXus 17 upgrade 1](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46852,,).
* [Java](https://wiki.genexus.com/commwiki/wiki?12258) generator supports this object since [GeneXus 17 upgrade 2](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?47418,,).

## [See Also](#See+Also)

[First Steps with API objects](https://wiki.genexus.com/commwiki/wiki?49754)  
[API object Syntax](https://wiki.genexus.com/commwiki/wiki?50879)  
[RestPath annotation](https://wiki.genexus.com/commwiki/wiki?50360)  
[RestMethod annotation](https://wiki.genexus.com/commwiki/wiki?50508)


|  |
| --- |
| **Pages** |
| [API object - Delete service definition and declaration](https://wiki.genexus.com/commwiki/wiki?49781) | [API object - Delete service definition and declaration (GeneXus 18 Upgrade 12 or prior)](https://wiki.genexus.com/commwiki/wiki?60083) | [API object - GetByKey service definition and declaration](https://wiki.genexus.com/commwiki/wiki?50052) |
| [API object - GetByKey service definition and declaration (GeneXus 18 Upgrade 12 or prior)](https://wiki.genexus.com/commwiki/wiki?60074) | [API object - Insert service definition and declaration](https://wiki.genexus.com/commwiki/wiki?49778) | [API object - Insert service definition and declaration (GeneXus 18 Upgrade 12 or prior)](https://wiki.genexus.com/commwiki/wiki?60081) |
| [API object - ListCustomers service definition and declaration](https://wiki.genexus.com/commwiki/wiki?50051) | [API object - ListCustomers service definition and declaration (GeneXus 18 Upgrade 12 or prior)](https://wiki.genexus.com/commwiki/wiki?60073) | [API object - Troubleshooting](https://wiki.genexus.com/commwiki/wiki?55436) |
| [API object - Update service definition and declaration](https://wiki.genexus.com/commwiki/wiki?49780) | [API object - Update service definition and declaration (GeneXus 18 Upgrade 12 or prior)](https://wiki.genexus.com/commwiki/wiki?60082) | [API object Considerations](https://wiki.genexus.com/commwiki/wiki?50053) |
| [API object security scheme](https://wiki.genexus.com/commwiki/wiki?52550) | [API object Syntax](https://wiki.genexus.com/commwiki/wiki?50879) | [Calling rest API Using Postman app](https://wiki.genexus.com/commwiki/wiki?50054) |
| [Description annotation](https://wiki.genexus.com/commwiki/wiki?56430) | [Expose API objects as MCP Server Tools](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?60860,Expose+API+objects+as+MCP+Server+Tools,) | [HowTo: Access secure REST services defined via API Objects](https://wiki.genexus.com/commwiki/wiki?52864) |
| [HowTo: Configure the API object security scheme](https://wiki.genexus.com/commwiki/wiki?52854) | [HowTo: Define an API object with a security scheme](https://wiki.genexus.com/commwiki/wiki?52840) | [HowTo: Define an API object with a security scheme (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55404) |
| [HowTo: Use Postman to access secure REST services defined via API Objects](https://wiki.genexus.com/commwiki/wiki?50055) | [Permissions by Method in the API object](https://wiki.genexus.com/commwiki/wiki?55405) | [Prototyping an API with Swagger](https://wiki.genexus.com/commwiki/wiki?50008) |
| [Remote call to API object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?55076,Remote+call+to+API+object,) | [RestCode variable](https://wiki.genexus.com/commwiki/wiki?60841) | [RestMethod annotation](https://wiki.genexus.com/commwiki/wiki?50508) |
| [RestPath annotation](https://wiki.genexus.com/commwiki/wiki?50360) | [RestServiceName variable](https://wiki.genexus.com/commwiki/wiki?60844) | [SecurityLevel annotation](https://wiki.genexus.com/commwiki/wiki?55437) |
| [SecurityPermission annotation](https://wiki.genexus.com/commwiki/wiki?55422) | [Standard Variables for API objects](https://wiki.genexus.com/commwiki/wiki?60834) |

---
