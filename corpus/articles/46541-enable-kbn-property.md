---
title: "Enable KBN property"
source_id: 46541
source_url: https://wiki.genexus.com/commwiki/wiki?46541
genexus_version: "18"
---

# Enable KBN property

Indicates that the Native Mobile application services being deployed must be available to use with the iOS Knowledge Base Navigator (KBN).

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Generators:** [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Level:** Deploy Target Options

### [Description](#Description)

When set to True, additional metadata files are added to the deploy, the files required by the KBN.

The default value is False, meaning that the metadata required by the KBN will not be deployed.

`[imagen omitida: wiki id 46583]`

If these metadata files are not included (value set to False) and the user tries to add the application services to the KBN, the following error will be displayed:

`[imagen omitida: wiki id 46605]`

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [Availability](#Availability)

This property is available since [GeneXus 17](https://wiki.genexus.com/commwiki/wiki?46066,,).

### [See Also](#See+Also)

[GeneXus Project Navigator](https://wiki.genexus.com/commwiki/wiki?14974)  
[Deployment and Prototyping in the Apple Platform](https://wiki.genexus.com/commwiki/wiki?16234)  
[HowTo: Version Your Native Mobile Application](https://wiki.genexus.com/commwiki/wiki?17223)


|  |
| --- |
| **Backlinks** |
| [Toc:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Toc:Application Deployment tool (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54334) | [Hardening of GeneXus Systems and Deployments with GAM](https://wiki.genexus.com/commwiki/wiki?47237) |
| [HowTo: Deploy mobile services to AWS Serverless using AWS Lambda and AWS API Gateway](https://wiki.genexus.com/commwiki/wiki?35355) | [HowTo: Deploy static files to Azure Storage in Serverless deploy](https://wiki.genexus.com/commwiki/wiki?50142) |

---
