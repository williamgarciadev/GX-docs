---
title: "API object security scheme"
source_id: 52550
source_url: https://wiki.genexus.com/commwiki/wiki?52550
genexus_version: "18"
---

# API object security scheme

The [API object](https://wiki.genexus.com/commwiki/wiki?46151) has a security scheme that allows you to configure [authentication](https://wiki.genexus.com/commwiki/wiki?18456,,) and [authorization](https://wiki.genexus.com/commwiki/wiki?17918).

Security in API objects through [GAM](https://wiki.genexus.com/commwiki/wiki?24746) works in the same way as in other objects that expose REST services. That is to say, you must enable the model security by setting the [Enable Integrated Security property](https://wiki.genexus.com/commwiki/wiki?14706) to True at the KB [version level](https://wiki.genexus.com/commwiki/wiki?7860) and selecting [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691). Then, in the API object, you must configure the [Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214) by specifying whether you want Authentication or Authorization.

## [Secure REST API](#Secure+REST+API)

In your API object, you have to set [REST Protocol property](https://wiki.genexus.com/commwiki/wiki?37254) = True.

*Detailed steps at:* [HowTo: Define an API object with a security scheme](https://wiki.genexus.com/commwiki/wiki?52840)

Furthermore, the GAM Authentication and Authorization scenarios in the API object use the [OAuth 2.0 protocol](https://en.wikipedia.org/wiki/OAuth). Therefore, in the GAM Backend [applications](https://wiki.genexus.com/commwiki/wiki?15910) you have to select the "Allow authentication v.2.0?" and the "Can get user roles?" checkboxes.

*Detailed steps at:* [HowTo: Configure the API object security scheme](https://wiki.genexus.com/commwiki/wiki?52854)

### [Prototype the REST API](#Prototype+the+REST+API)

In your API object, make sure that [Generate OpenAPI interface property](https://wiki.genexus.com/commwiki/wiki?31859) = Yes. After that, press F5, and GeneXus will generate the YAML file with the security information.

Now, you can use features like the [Launchpad Tool Window](https://wiki.genexus.com/commwiki/wiki?52315) to prototype the REST API. When using those tools, you must paste the Client Id and Client Secret information taken from the [GAM Backend](https://wiki.genexus.com/commwiki/wiki?15935).

**Note:** You should keep in mind that the Client Id is the Application Identifier in GAM ([GAM - Applications](https://wiki.genexus.com/commwiki/wiki?15910)), and you can have more than one Client Id in GAM.

*Detailed steps at:* [HowTo: Access secure REST services defined via API Objects](https://wiki.genexus.com/commwiki/wiki?52864)

### [See Also](#See+Also)

[HowTo: Define an API object with a security scheme](https://wiki.genexus.com/commwiki/wiki?52840)  
[HowTo: Configure the API object security scheme](https://wiki.genexus.com/commwiki/wiki?52854)  
[HowTo: Access secure REST services defined via API Objects](https://wiki.genexus.com/commwiki/wiki?52864)


|  |
| --- |
| **Backlinks** |
| [Toc:First Steps with API objects](https://wiki.genexus.com/commwiki/wiki?49754) | [HowTo: Access secure REST services defined via API Objects](https://wiki.genexus.com/commwiki/wiki?52864) | [HowTo: Configure the API object security scheme](https://wiki.genexus.com/commwiki/wiki?52854) |
| [HowTo: Define an API object with a security scheme](https://wiki.genexus.com/commwiki/wiki?52840) | [HowTo: Define an API object with a security scheme (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55404) |

---
