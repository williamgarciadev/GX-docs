---
title: "HowTo: Deploy Frontend applications to Azure Blob Storage"
source_id: 49878
source_url: https://wiki.genexus.com/commwiki/wiki?49878
genexus_version: "18"
---

# HowTo: Deploy Frontend applications to Azure Blob Storage

This article shows you the steps to deploy [Angular](https://wiki.genexus.com/commwiki/wiki?42550) applications to [Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/#overview), using the [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) from inside the [GeneXus IDE](https://wiki.genexus.com/commwiki/wiki?5272), or [Msbuild](https://wiki.genexus.com/commwiki/wiki?41321,,) commands.

The solution is based on [MSBuild Tasks](https://wiki.genexus.com/commwiki/wiki?3908), which allow you to easily extend, customize, and automate your deployments in a CI/CD pipeline.

In this document, you'll see how to deploy an
[Angular](https://wiki.genexus.com/commwiki/wiki?42539) application to Azure Blob Storage using MSBuild tasks.

First, execute the*deploy.msbuild* script to create the *.gxdproj* file, and run the script to build the project, as explained in the Steps 1 and 2 of [HowTo: Deploy Frontend applications to a Cloud Provider Object Storage](https://wiki.genexus.com/commwiki/wiki?49877).

The third step is to upload the package.

You have to execute the *deploy.msbuild* script which is available under the DeploymentTargets folder in the GeneXus installation (as explained in  [HowTo: Deploy Frontend applications to a Cloud Provider Object Storage](https://wiki.genexus.com/commwiki/wiki?49877)).

In the case of Azure, the properties to add are as follows:

* **STATICFRONTEND\_AZURE\_STORAGE\_ACCOUNT**: Storage account name
* **STATICFRONTEND\_AZURE\_STORAGE\_ACCOUNT\_KEY**: Storage account key
* **STATICFRONTEND\_AZURE\_SP\_APP\_ID**: Service principal Application ID
* **STATICFRONTEND\_AZURE\_SP\_TENANT\_ID**: Service principal Tenant ID
* **STATICFRONTEND\_AZURE\_SP\_CREDENTIALS**: Service principal credentials

Other properties should be passed as well:

* **GXDeployFileProject:**The path to the *.gxdproj* file generated in the "Create Front end Project" step (see [HowTo: Deploy Frontend applications to a Cloud Provider Object Storage](https://wiki.genexus.com/commwiki/wiki?49877)).
* **STATICFRONTEND\_PROVIDER:** It should be"azureblobstorage"
* **ProjectName**: Name of the generated .gxdproj file. By default, it is "DeploymentUnit\_<TimeStamp>.gxdproj".
* **DeployFullPath**: Full path to the package built in [HowTo: Deploy Frontend applications to a Cloud Provider Object Storage](https://wiki.genexus.com/commwiki/wiki?49877) step.
* **GX\_PROGRAM\_DIR**: GeneXus installation directory.

### [Sample](#Sample)

```
C:\Windows\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe /nologo /verbosity:minimal /ToolsVersion:4.0 "C:\Development\Trunk\Genexus\DeploymentTargets\StaticFrontEnd\deploy.msbuild" /p:STATICFRONTEND_PROVIDER="azureblobstorage"
/p:STATICFRONTEND_AZURE_STORAGE_ACCOUNT="storagetest"
/p:STATICFRONTEND_AZURE_STORAGE_ACCOUNT_KEY="********"
/p:STATICFRONTEND_AZURE_SP_APP_ID="**********"
/p:STATICFRONTEND_AZURE_SP_TENANT_ID="***********"
/p:STATICFRONTEND_AZURE_SP_CREDENTIALS="*******"
/p:DeployFullPath="C:\models\TestAngular\TestAngular\NetCoreSQLServer1004\Deploy\STATICFRONTEND\DeploymentUnit2\20220107171829"
/p:GX_PROGRAM_DIR="C:\Development\Trunk\GeneXus"
/p:ProjectName="myproject" 
/t:Deploy
```

### [See Also](#See+Also)

[Build and deploy a static website to Azure Storage Static Websites: setting up the cloud](https://wiki.genexus.com/commwiki/wiki?49887)


|  |
| --- |
| **Backlinks** |
| [Toc:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Toc:Application Deployment tool (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54334) | [Build and deploy a static website to Azure Storage Static Websites: setting up the cloud](https://wiki.genexus.com/commwiki/wiki?49887) |
| [HowTo: Deploy Frontend applications to a Cloud Provider Object Storage](https://wiki.genexus.com/commwiki/wiki?49877) |

---
