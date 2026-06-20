---
title: "Application Deployment MSBuild tasks"
source_id: 42073
source_url: https://wiki.genexus.com/commwiki/wiki?42073
genexus_version: "18"
---

# Application Deployment MSBuild tasks

The  [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) is based on [MSBuild Tasks](https://wiki.genexus.com/commwiki/wiki?3908), which allow you to easily extend and/or customize your deployments. Using those tasks, you can automate deployment.

The following document lists those tasks and details how to use them in order to either extend what GeneXus does or automate your deployments.

### [CreateDeployProject](#CreateDeployProject)

The CreateDeployProject task will analyze what GeneXus objects must be included in the deployment based on the call tree of every selected object (or every main object if none). The output of this task is an MSBuild script with the extension .gxdproj that will hold every environment property and object (with its properties) needed for a successful deployment.

GeneXus provides a script called Deploy.msbuild (located at the root of GeneXus installation) which is used by GeneXus itself and it's a great starting point for automating your calls. Use the following command to create a deployment project of every main in your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836).

```
msbuild.exe <GX Installation directory>\deploy.msbuild /p:KBPath=<Path to your Knowledge Base>
```

This will create the deploy project (.gxdproj) file for the trunk version of the mentioned Knowledge Base for every main object in that version. There are a few properties you can add to change this behavior.

**KBVersion:** The name of the version to set as active

**KBEnvironment:** The name of the environment in that version

**ProjectName:** It will be the name of the generated .gxdproj file. If you leave this parameter empty, the DeploymentUnit parameter is taken to give a name to the gxdproj (concatenated with a timestamp value). If both, ProjectName and DeploymentUnit are empty, the name of the gxdproj will be "MSBuildDeployment" concatenated with a timestamp.

**ObjectNames:** The names (with their types) of the objects to deploy (deployment units can also be selected) (ref.: [How to specify an object list in a MSBuild task](https://wiki.genexus.com/commwiki/wiki?44328)). If you leave this parameter empty, all the main objects of the KB are included in the deployment.

**APPLICATION\_KEY:** The new encryption key to set for your deployed application

**ApplicationServer**

**TARGET\_JRE:** (Java only) the version of the Java runtime where the deployed app will run. (Default is 9)

**PACKAGE\_FORMAT:** (Java only) whether the engine must create a WAR or an EAR. (Default is 'Automatic', the engine decides based on the selected objects)

**SelectedObjectsOnly**: When set to True the deploy engine will not calculate the call tree of selected objects. Only the selected ones will be deployed.

**TargetId**: Default will be "Local", but you can set any of the supported Deploy Application Targets.

**SourcePath:** Defaults to the KB directory\model. The gxdproj file is saved under <**SourcePath**>\web if Outputpath is not defined.

**Outputpath**: Where the .gxdproj is saved.

You can also use the **CallTreeLogFile** property to get a log of the objects call tree.

### [Sample](#Sample)

```
MSbuild.exe /nologo /verbosity:minimal /ToolsVersion:14.0 "c:\GeneXus\deploy.msbuild" 
/p:KBPath="c:\fullgx\kbaux" 
/p:KBEnvironment=NetEnvironment 
/p:KBVersion=kbaux 
/p:ProjectName=DeployNet16 
/p:ObjectNames="TestDeployUnit1" 
/p:GX_PROGRAM_DIR="c:\fullgx\gxsaltostable" 
/p:TimeStamp=DeployNet16 
/p:Application_Key=863B7BE7A26B4276942E2C50FA1E0EAC 
/p:ApplicationServer="IIS8" /p:TargetId="Local" 
/p:SourcePath="c:\fullgx\kbaux\CSharpModel" 
/p:AppName="DeployNet16" 
/p:SelectedObjectsOnly="false" 
/l:FileLogger,Microsoft.Build.Engine;logfile=c:\fullgx\temp\CreateDeploy.log
/p:CallTreeLogFile=c:\temp\CallTree.log
/t:CreateDeploy
```

The generated .gxdproj file is another MSBuild script which contains the needed info to create the packaged application.

### [CreatePackage](#CreatePackage)

To generate the package (it can be a zip file in case of C# and .NET Core or a war/jar/ear in case of Java), you need to execute the generated script as follows:

```
msbuild.exe <Full path>\MSBuildDeployment_20190123103151.gxdproj
```

In this case, you can also set properties to tell the engine where the generated package will be deployed.

**DeployFullPath**: Full path to which a copy of packaged files will be copied to. You can use this path to compare different deployments.

Take a look at the generated .gxdproj file to see the defaults for **DeployFullPath** and **DeployFileFullPath** properties.

    <!-- Destination paths -->  
    <PropertyGroup>  
        <DeployFileFullPath>$(SourcePath)\Deploy\$(DeployTarget)</DeployFileFullPath>  
        <DeployFullPath>$(DeployFileFullPath)\$(DeploymentUnit)\$(TimeStamp)</DeployFullPath>  
    </PropertyGroup>

### [Deploy to external targets](#Deploy+to+external+targets)

GeneXus can also help you deploy to any of the supported cloud providers (deployment targets).

Every supported target is listed under the DeploymentTargets folder under the GeneXus installation. All of these targets have a **deploy.msbuild** file with a default task called **Deploy**.

### [Sample](#Sample)

```
MSBuild.exe /nologo /verbosity:minimal /ToolsVersion:4.0 "c:\GeneXus\DeploymentTargets\Docker\deploy.msbuild" 
/p:DOCKER_BASE_IMAGE="tomcat:9-jdk11" 
/p:DOCKER_MAINTAINER="seba <seba@example.com>" 
/p:DOCKER_WEBAPPLOCATION="/usr/local/tomcat/webapps/" 
/p:DOCKER_IMAGE_NAME="k8sdeployjavaenvironment" 
/p:DOCKER_ENVVARS=""
/p:GENERATOR="Java" 
/p:APPLICATION_NAME="DeploymentUnit2_20200130131103" 
/p:DEPLOY_PATH="C:\GXmodels\junk\K8SDeploy\JavaModel\Deploy\DOCKER\DeploymentUnit2\20200130131103" 
/t:Deploy
```

In sum, when the target is not local, the execution is in the following order.  
Now, take AWSECS as an example.

1. The task CreateDeploy of the script deploy.msbuild of the GeneXus root is executed by msbuild, to which the **Target Id** and the **deploy targets** must be passed as properties, eg:

```
MSbuild.exe /nologo /verbosity:minimal /ToolsVersion:14.0 "c:\GeneXus\deploy.msbuild"
/p:KBPath="c:\fullgx\kbaux"
/p:KBEnvironment=NetEnvironment
/p:KBVersion=kbaux
/p:ProjectName=DeployNet16
/p:TargetId="AWSECS" 
/p:DEPLOY_TARGETS="C:\Genexus\DeploymentTargets\AWSECS\aws.targets"
/p:SourcePath="c:\fullgx\kbaux\CSharpModel"
/p:AppName="DeployNet16" /t:CreateDeploy
```

As a result, the gxdproj file is obtained, where you will see the **DeployTarget** (TargetId information)and **DeployTargetTask** (DEPLOY\_TARGETS information)properties.

2. The task CreatePackage of the gxdproj generated scripted is executed via msbuild. As a result you get a package on the local machine.

3. The Deploy task of the deploy.msbuild (located under <GX>\DeploymentTargets\AWSECS) is executed to deploy to the Paas.

### [Tip](#Tip)

Generate the [GeneXus Log](https://wiki.genexus.com/commwiki/wiki?23257) when you deploy using the Application deployment tool inside de GeneXus IDE, in order to see in the log, the msbuild tasks that are executed.

### [See Also](#See+Also)

[MSBuild Tasks](https://wiki.genexus.com/commwiki/wiki?3908)  
[Team Development MSBuild Tasks](https://wiki.genexus.com/commwiki/wiki?24612,,)  
[Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092)  
[How to specify an object list in a MSBuild task](https://wiki.genexus.com/commwiki/wiki?44328)


|  |
| --- |
| **Backlinks** |
| [Toc:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Toc:Application Deployment tool (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54334) | [Automated DevOps with GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51574) |
| [Azure CosmosDB-triggered functions](https://wiki.genexus.com/commwiki/wiki?54574) | [Customize GeneXus Deployment capabilities](https://wiki.genexus.com/commwiki/wiki?45672) | [Deploy to Docker MSBuild task](https://wiki.genexus.com/commwiki/wiki?47839) |
| [How to specify an object list in a MSBuild task](https://wiki.genexus.com/commwiki/wiki?44328) | [HowTo: Create a deployment pipeline for an application using GXflow](https://wiki.genexus.com/commwiki/wiki?49176) | [HowTo: Deploy an Application to Docker](https://wiki.genexus.com/commwiki/wiki?36951) |
| [HowTo: Deploy an Application to Docker (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54337) | [HowTo: Deploy static files to Azure Storage in Serverless deploy](https://wiki.genexus.com/commwiki/wiki?50142) | [MSBuild Tasks](https://wiki.genexus.com/commwiki/wiki?3908) |
| [MSBuild Tasks (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?53867) | [MSBuild Tasks (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54112) | [Packaging Java sources](https://wiki.genexus.com/commwiki/wiki?54656) | [Reorganization Deployment MSBuild Tasks](https://wiki.genexus.com/commwiki/wiki?42568) |

---
