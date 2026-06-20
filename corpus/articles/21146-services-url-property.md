---
title: "Services URL property"
source_id: 21146
source_url: https://wiki.genexus.com/commwiki/wiki?21146
genexus_version: "18"
---

# Services URL property

Determines the URL where the REST Web Services of the mobile application may be found.

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

The Service URL should have a structure like this:  
<protocol>://<server\_domain>[:<port>]/<virtual\_directory>  
where  
- protocol: It can be http or https, depending on your requirements.  
- server\_domain: The domain of your webapp (it could be an IP address as well).  
- port: Optional. Port number where the server is listening.  
- virtual\_directory: The location of your REST web services.

### [Considerations](#Considerations)

See [Online Native Mobile applications architecture](https://wiki.genexus.com/commwiki/wiki?14981) for more information about the architecture and the role of Rest Services in this kind of apps.

There are Native Mobile Client apps where the Server providing the services is defined by the Client. So, the application does not actually have the server URL defined at design time. This is a common scenario for many applications where the Server-side is a product in itself.

Basically, instead of defining, at design time, where my User Interface will consume services, it is defined in a client application setting. In this case, the Services URL property should be left empty so that upon accessing the application, the end-user will be required to enter a Services URL value.

However, you should consider setting a default value for the device's services URL property because it is a requirement of Apple's approval process.

### [See Also](#See+Also)

* [Web Root property](https://wiki.genexus.com/commwiki/wiki?9287)
* [HowTo: Change the URL Services of a Native Mobile application](https://wiki.genexus.com/commwiki/wiki?16159)
* [Dynamic Services URL property](https://wiki.genexus.com/commwiki/wiki?20366)


|  |
| --- |
| **Backlinks** |
| [Deploy to Azure Serverless using API Management](https://wiki.genexus.com/commwiki/wiki?49107) | [Deploy to cloud property](https://wiki.genexus.com/commwiki/wiki?15041) | [Dynamic Services URL property](https://wiki.genexus.com/commwiki/wiki?20366) |
| [Execution for Android Using the Device](https://wiki.genexus.com/commwiki/wiki?14910) | [Execution for Android Using the Device (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?56063) | [GAM - Facebook Authentication Type](https://wiki.genexus.com/commwiki/wiki?29007) | [How to deploy a command line procedure to AWS Lambda as a Function](https://wiki.genexus.com/commwiki/wiki?40803) |
| [HowTo: Change the URL Services of a Native Mobile application](https://wiki.genexus.com/commwiki/wiki?16159) | [HowTo: Deploy mobile services to AWS Serverless using AWS Lambda and AWS API Gateway](https://wiki.genexus.com/commwiki/wiki?35355) | [HowTo: Upload a Mini App version to the Mini App Center](https://wiki.genexus.com/commwiki/wiki?53318) | [Network external object](https://wiki.genexus.com/commwiki/wiki?31310) |
| [Services URL Configuration Panel property](https://wiki.genexus.com/commwiki/wiki?49768) | [Services URL Mode property](https://wiki.genexus.com/commwiki/wiki?54361) | [SSL Pinning Pin Set property](https://wiki.genexus.com/commwiki/wiki?44258) | [Synchronization.Send method](https://wiki.genexus.com/commwiki/wiki?23604) |
|

---
