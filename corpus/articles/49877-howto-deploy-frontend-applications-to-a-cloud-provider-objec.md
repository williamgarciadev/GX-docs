---
title: "HowTo: Deploy Frontend applications to a Cloud Provider Object Storage"
source_id: 49877
source_url: https://wiki.genexus.com/commwiki/wiki?49877
genexus_version: "18"
---

# HowTo: Deploy Frontend applications to a Cloud Provider Object Storage

This article shows you the steps to deploy your Frontend application to a Cloud Provider Object Storage. To do so, you can use the [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) from inside the [GeneXus IDE](https://wiki.genexus.com/commwiki/wiki?5272) or [Msbuild](https://wiki.genexus.com/commwiki/wiki?41321,,) commands.

### [Deploy using Application Deployment tool inside GeneXus](#Deploy+using+Application+Deployment+tool+inside+GeneXus)

**1.** In GeneXus, go through the "Deploy Application" contextual menu option after having created the [Deployment Unit object](https://wiki.genexus.com/commwiki/wiki?38886) containing the main objects of your app

`[imagen omitida: wiki id 49880]`

**2.** Select the "Static Front end" option from the Targets combo box.

**3.** From the Properties dialog, select a Front end Deployment target (AWS S3, or Azure Blob Storage).  
Depending on the target selected, you have to enter different options.  
**4.** Finally, press the deployment button.

`[imagen omitida: wiki id 49879]`

If you wish, you can just create the deploy package by checking "Only Package". In this case, you will have the package under the Deploy\STATICFRONTEND\<DeploymentUnit> directory of the KB.

### [MSBuild tasks to deploy to a Cloud Provider Object Storage](#MSBuild+tasks+to+deploy+to+a+Cloud+Provider+Object+Storage)

The Application Deployment tool is based on MSBuild tasks. Using those tasks, you can automate deployment.

In the case of Frontend applications, three MSBuild scripts are executed to perform the deployment.

**1. Create Front end Project**

GeneXus provides a script called *deploy.msbuild* (located at the root of the GeneXus installation) which is used to create a deployment project for Frontend applications, when the Target deployment (TargetId) is "STATICFRONTEND".

This step creates a file called *<ProjectName>.gxdproj* (an MSBuild script) which contains a list of the selected objects of the Deployment Unit object, and some environment properties for the deployment. This *gxdproj* file is used as input of the MSBuild task that deploys to the cloud.

Properties to add to the MSBuild execution:

* **TargetId**: STATICFRONTEND
* **DEPLOY\_TARGETS:** Reference to .targets file where the validations are implemented (staticfrontend.targets).
* **KBPath**: Path to the Knowledge Base
* **KBVersion**: Name of the version to be set as active
* **KBEnvironment**: Name of the environment in that version
* **DeploymentUnit:** Name of the deployment unit
* **ProjectName**: Name of the generated .gxdproj file. By default, it is "DeploymentUnit\_<TimeStamp>.gxdproj".
* **ObjectNames**: Names and types of the objects to deploy (deployment units can also be selected) (ref: [How to specify an object list in a MSBuild task](https://wiki.genexus.com/commwiki/wiki?44328)). This parameter is optional if you specify the DeploymentUnit property.
* **Outputpath**: Where the .gxdproj is saved. The gxdproj file is saved under $KB.Location$\$Model.TargetPath$\web if Outputpath is not defined.

#### [Sample](#Sample)

```
C:\Windows\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe /noconsolelogger /nologo /logger:DeployLogger,"C:\Development\Trunk\Genexus\GeneXus.Deploy.MSBuild.Tasks.dll"
/verbosity:quiet /ToolsVersion:4.0 "C:\Development\Trunk\Genexus\deploy.msbuild"
/p:TargetId ="STATICFRONTEND"
/p:DEPLOY_TARGETS="C:\Development\Trunk\Genexus\DeploymentTargets\StaticFrontEnd\staticfrontend.targets"
/p:KBPath="C:\models\TestAngular\TestAngular"
/p:KBEnvironment="NetSQLServer1"
/p:KBVersion="TestAngular"
/p:DeploymentUnit="DeploymentUnit2"
/p:ProjectName="myproject"
/p:ObjectNames="SDPanel:Panel1"  
/t:CreateDeploy
```

**2. Create Package**

The build of the project is triggered by the *CreateFrontendPackage.msbuild* script, which receives the parameters explained below.

* **GXDeployFileProject:** The path to the .gxdproj file generated in the "Create Front end Project" step (including the name of the file).
* **ProjectRootDirectory:** The path to the directory under the KB, where the Angular application is generated (it is always under the mobile\Angular folder). E.g: "C:\models\TestAngular\TestAngular\NetSQLServer005\mobile\Angular"
* **GenExtensionName:** The name of the Front end generator (e.g.:Angular)
* **DeploymentScript:**Each Front end generator should have its own script for packaging (building the application). This should be specified at the DeploymentScript msbuild property.
* **GX\_PROGRAM\_DIR:** GeneXus program directory.

#### [Sample](#Sample)

```
C:\Windows\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe /noconsolelogger /nologo /logger:DeployLogger,"C:\Development\Trunk\Genexus\GeneXus.Deploy.MSBuild.Tasks.dll" /verbosity:minimal /ToolsVersion:4.0 "C:\Development\Trunk\Genexus\CreateFrontendPackage.msbuild" /p:GXDeployFileProject="C:\models\TestAngular\TestAngular\NetSQLServer005\web\DeploymentUnit1_20220614182207.gxdproj"
/p:ProjectRootDirectory="C:\models\TestAngular\TestAngular\NetSQLServer005\mobile\Angular" 
/p:GenExtensionName="Angular"
/p:DeploymentScript="deploy.angular.msbuild"
/p:GX_PROGRAM_DIR="C:\Development\Deploy\Genexus"
/t:CreatePackage
```

**Note**: In the case of
[Angular](https://wiki.genexus.com/commwiki/wiki?42539), the DeploymentScript is "deploy.angular.msbuild" and is declared at the angular.generator file. The deploy.angular.msbuild is located at GenExtensions\SmartDevices\Angular\deploy under the GeneXus installation.

**3. Deploy to the Cloud Provider**

The solution to deploy the Frontend of an application is extensible and available at Github ([StaticFrontEnd deployment target](https://github.com/genexuslabs/deployment-targets/tree/beta/src/StaticFrontEnd)). Those files are in your GeneXus installation, under the DeploymentTarget folder.

There's a built-in solution for deploying to AWS S3 and to Azure Blob Storage.

In this step, the application is built and everything is set up for distribution.

It has a deploy.msbuild script which includes the .target file depending on the STATICFRONTEND\_PROVIDER property value (it can be "aws3" or "azureblobstorage"). Depending on the Provider, different properties are needed in order to deploy to that cloud.

For details on how to execute this step, see [HowTo: Deploy Frontend applications to Azure Blob Storage](https://wiki.genexus.com/commwiki/wiki?49878).

### [Temporal Limitation](#Temporal+Limitation)

At the moment, only one main object must be deployed to each Storage.

### [Availability](#Availability)

Since [GeneXus 17 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?49956,,)

### [See Also](#See+Also)

Consider that in most cases you have to configure the CORS. See the following for more details:  
[HowTo: Deploy Angular Frontend applications using serverless backend](https://wiki.genexus.com/commwiki/wiki?49963)


|  |
| --- |
| **Backlinks** |
| [Toc:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Toc:Application Deployment tool (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54334) |
| [How to deploy an app generated by Angular Generator](https://wiki.genexus.com/commwiki/wiki?44771) | [HowTo: Deploy Angular Frontend applications using serverless backend](https://wiki.genexus.com/commwiki/wiki?49963) | [HowTo: Deploy Frontend applications to Azure Blob Storage](https://wiki.genexus.com/commwiki/wiki?49878) |
| [HowTo: Deploy static files to Azure Storage in Serverless deploy](https://wiki.genexus.com/commwiki/wiki?50142) |

---
