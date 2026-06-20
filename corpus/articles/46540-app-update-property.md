---
title: "App Update property"
source_id: 46540
source_url: https://wiki.genexus.com/commwiki/wiki?46540
genexus_version: "18"
---

# App Update property

Indicates if the deployment to be performed corresponds to a native mobile application update, and what type of update is going to be performed.

### [Values](#Values)

|  |  |
| --- | --- |
| **Major Change** | The application requires a major update (binaries need to be updated). The JSON files indicating the version change should be included in the deploy. |
| **Minor Change** | The application requires a minor update (metadata only, no native binary changes required). The JSON files indicating the version change should be included, as well as the zipped metadata to be read by the application running on the users devices. |
| **None** | The application is not being updated (it may be the first update or a services-only update that does not affect the native applications) or no native mobile application is being deployed. No additional metadata will be included. |

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Level:** Deploy Target Options

### [Description](#Description)

Defines the type of update that will be performed for the deployed Native Mobile application.

For more information on how application updates work, please take a look at [HowTo: Version Your Native Mobile Application](https://wiki.genexus.com/commwiki/wiki?17223).

`[imagen omitida: wiki id 46567]`

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [Availability](#Availability)

This property is available since [GeneXus 17](https://wiki.genexus.com/commwiki/wiki?46066,,).

### [See Also](#See+Also)

[HowTo: Version Your Native Mobile Application](https://wiki.genexus.com/commwiki/wiki?17223)


|  |
| --- |
| **Backlinks** |
| [Toc:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Toc:Application Deployment tool (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54334) | [Hardening of GeneXus Systems and Deployments with GAM](https://wiki.genexus.com/commwiki/wiki?47237) |
| [HowTo: Deploy mobile services to AWS Serverless using AWS Lambda and AWS API Gateway](https://wiki.genexus.com/commwiki/wiki?35355) | [HowTo: Deploy static files to Azure Storage in Serverless deploy](https://wiki.genexus.com/commwiki/wiki?50142) | [HowTo: Version Your Native Mobile Application](https://wiki.genexus.com/commwiki/wiki?17223) |

---
