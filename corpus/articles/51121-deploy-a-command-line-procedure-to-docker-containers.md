---
title: "Deploy a command-line procedure to Docker containers"
source_id: 51121
source_url: https://wiki.genexus.com/commwiki/wiki?51121
genexus_version: "18"
---

# Deploy a command-line procedure to Docker containers

This document explains some considerations to make when deploying command-line procedures in a Docker container.

If your deployment unit has only one object, and this object is a main procedure with [Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947) = "Command line," the Dockerfile generated adds an EntryPoint to be able to execute this procedure when the image is run.

While running the MSBuild, you have to set the DOCKER\_BASE\_IMAGE property with an adequate value for that purpose. See [Deploy to Docker MSBuild task](https://wiki.genexus.com/commwiki/wiki?47839) for more information.

In this case, the *GXDeployFileProject* property is mandatory. If no value is assigned to it in Java, the MSBuild execution throws an error.

For .NET, it throws the following warning: Missing or invalid *GXDeployFileProject* property. It should be set for command-line deployments.

### [See also](#See+also)

[Deploy to Docker MSBuild task](https://wiki.genexus.com/commwiki/wiki?47839)


|  |
| --- |
| **Backlinks** |
| [Toc:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Toc:Application Deployment tool (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54334) |

---
