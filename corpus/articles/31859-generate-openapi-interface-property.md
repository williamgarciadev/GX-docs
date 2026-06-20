---
title: "Generate OpenAPI interface property"
source_id: 31859
source_url: https://wiki.genexus.com/commwiki/wiki?31859
genexus_version: "18"
---

# Generate OpenAPI interface property

Declares whether the Rest web services in GeneXus will have their Open API documentation in a file called default.yaml, located under the application directory.

### [Values](#Values)

|  |  |
| --- | --- |
| **No** | The Open API interface documentation won't be generated. |
| **Use Environment property value** | The value configured for the Environment (under the Back end node > Generator) will be used. |
| **Yes** | The Open API interface will be generated for this REST service. |

### [Scope](#Scope)

**Objects:** [Business Component](https://wiki.genexus.com/commwiki/wiki?5846), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270), [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [API](https://wiki.genexus.com/commwiki/wiki?46151), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974)

### [Description](#Description)

The default value for the property at Generator level is:

* Yes, if the KB or environment is created with GeneXus 18 or higher
* No, otherwise.

The default value for the property at object level is: Use Environment property value.

The default.yaml file is updated when any of these objects is generated:

* [Procedures as Rest Web Services in GeneXus](https://wiki.genexus.com/commwiki/wiki?21467)
* [Data Providers as Rest Web Services in GeneXus](https://wiki.genexus.com/commwiki/wiki?28216)
* [Business Components as Rest web services in GeneXus](https://wiki.genexus.com/commwiki/wiki?28214)
* [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)
* [Work With pattern and Work With object](https://wiki.genexus.com/commwiki/wiki?15974)

When working with the [API object](https://wiki.genexus.com/commwiki/wiki?46151) an independent Yaml is generated.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691).

### [See Also](#See+Also)

[Documenting RESTFul services](https://wiki.genexus.com/commwiki/wiki?30776)  
[Rest web services in GeneXus](https://wiki.genexus.com/commwiki/wiki?28213)  
[Open API](http://openapis.org/)


|  |
| --- |
| **Backlinks** |
| [Category:API object](https://wiki.genexus.com/commwiki/wiki?46151) | [API object security scheme](https://wiki.genexus.com/commwiki/wiki?52550) | [Azure Http-triggered functions](https://wiki.genexus.com/commwiki/wiki?49266) |
| [Calling rest API Using Postman app](https://wiki.genexus.com/commwiki/wiki?50054) | [Deploy to Azure Serverless using API Management](https://wiki.genexus.com/commwiki/wiki?49107) | [Documenting RESTFul services](https://wiki.genexus.com/commwiki/wiki?30776) |
| [GeneXus 18 Compatibility Section](https://wiki.genexus.com/commwiki/wiki?51080) | [GeneXus 18 Compatibility Section (GeneXus 18)](https://wiki.genexus.com/commwiki/wiki?53520) |
| [Getting information from the Swagger UI docs](https://wiki.genexus.com/commwiki/wiki?30785) | [HowTo: Access secure REST services defined via API Objects](https://wiki.genexus.com/commwiki/wiki?52864) | [HowTo: Deploy mobile services to AWS Serverless using AWS Lambda and AWS API Gateway](https://wiki.genexus.com/commwiki/wiki?35355) | [HowTo: Upload an image, video, or audio file via an API object](https://wiki.genexus.com/commwiki/wiki?51411) |
| [Launchpad Tool Window](https://wiki.genexus.com/commwiki/wiki?52315) | [OpenAPI import tool](https://wiki.genexus.com/commwiki/wiki?31864) | [OpenAPI import tool (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54370) |
| [Prototyping an API with Swagger](https://wiki.genexus.com/commwiki/wiki?50008) | [RestPath annotation](https://wiki.genexus.com/commwiki/wiki?50360) |

---
