---
title: "Packaging .NET sources"
source_id: 54683
source_url: https://wiki.genexus.com/commwiki/wiki?54683
genexus_version: "18"
---

# Packaging .NET sources

The [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) provides the option to package .NET sources. This can be useful, for example, to upload the source code to GitHub or integrate it into the build process within an organization's workflow.

The following details the steps to have the .NET sources:

1. In the Application Deployment tool, you must select Local or Microsoft Azure Serverless (backend services)  as the Target.
2. Set the [Package Type property](https://wiki.genexus.com/commwiki/wiki?53373) with the "Sources" value.

When you choose the Sources value, the deployment creates a structure with two directories:

* **src:**Contains the generated sources and C-Sharp projects to assemble the binaries.
* **web:**Root directory of the web application. It contains configuration files, images, JavaScripts, styles, and resources in general that the application needs to run.

In the src\build directory, there is a solution file named: <DeploymentUnitName>.sln.

When compiling <DeploymentUnitName>.sln, all the binaries needed to run the application are created in the web\bin directory.

To build those binaries, you just need to execute the command:

```
dotnet publish src\build\<NameDeploymentUnit>.sln --output web\bin
```

To force all dependencies to be resolved:

```
dotnet build --force src\build\<NameDeploymentUnit>.sln --output web\bin
```

### [Availability](#Availability)

This functionality is available since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238).


|  |
| --- |
| **Backlinks** |
| [Toc:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Building Azure Serverless from sources](https://wiki.genexus.com/commwiki/wiki?55350) | [Building Azure Serverless from sources (GeneXus 18 Upgrade 7)](https://wiki.genexus.com/commwiki/wiki?56809) |
| [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238) | [Package Type property](https://wiki.genexus.com/commwiki/wiki?53373) |

---
