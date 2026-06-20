---
title: "HowTo: MSBuild tasks for Azure serverless deployment"
source_id: 51440
source_url: https://wiki.genexus.com/commwiki/wiki?51440
genexus_version: "18"
---

# HowTo: MSBuild tasks for Azure serverless deployment

Below are the MSBuild tasks related to the deployment of the back-end services (services of a mobile or Angular app) to Azure serverless.  
For using the [GeneXus IDE](https://wiki.genexus.com/commwiki/wiki?5272) to execute the deployment, and having a general knowledge of the meaning of the properties, see [Deploy to Azure Serverless using API Management](https://wiki.genexus.com/commwiki/wiki?49107).

### [Step 1 - Create deploy project](#Step+1+-+Create+deploy+project)

This task generates the *.gxdproj* file. The MSBuild file used is located under the GeneXus installation.

```
MSBuild.exe "C:\Genexus\deploy.msbuild"
/p:KBPath="C:\models\TestServerlessGAM"
/p:KBEnvironment="NETSQLServerCloud"
/p:KBVersion="TestServerlessGAM"
/p:ProjectName="DpuWithGAM_20220808111607"
/p:TargetId="AZURE_SERVERLESS"
/p:ObjectNames="Dashboard:Menu1"
/p:DeployFullPath="C:\models\TestServerlessGAM\NETSQLServerCloud\Deploy\AZURE_SERVERLESS\DpuWithGAM"
/p:GX_PROGRAM_DIR="C:\Genexus"
/t:CreateDeploy
```

### [Step 2. Create Package](#Step+2.+Create+Package)

Generates the package *.zip* file. The MSBuild file used is the *.gxdproj* file generated in the first step.  
This is a local package having all basic artifacts, not suitable to be deployed to Azure.

```
MSBuild.exe "C:\models\TestServerlessGAM\NETSQLServerCloud\web\DpuWithGAM_20220808111607.gxdproj"
/p:GX_PROGRAM_DIR="C:\Genexus"
/p:APPLICATION_KEY="90D4E373DDB1700F3064C9A5F3A34FE121C48EB37E877594534B745E16219C5D"
/p:INCLUDE_GAM="False"
/p:INCLUDE_GXFLOW_BACKOFFICE="True"
/p:APP_UPDATE="NONE"
/p:ENABLE_KBN="False"
/p:TARGET_JRE="9"
/p:PACKAGE_FORMAT="Automatic"
/t:CreatePackage
```

### [Step 3. Create Cloud package](#Step+3.+Create+Cloud+package)

This step creates the package to be deployed to Azure (it customizes the package created in Step 2).  
It uses the*CreateCloudPackage.msbuild* script, under the GeneXus directory.

```
MSBuild.exe "C:\Genexus\CreateCloudPackage.msbuild"
/p:TargetId="AZURE_SERVERLESS"
/p:CreatePackageScript="createpackage.msbuild"
/p:CreatePackageTarget="CreatePackage"
/p:GENERATOR=".NET"
/p:GXDeployFileProject=<Path to the .gxdproj file generated at first step>
/p:DeployFullPath="C:\models\TestServlessGAM\TestServerlessGAM\NetModel\Deploy\AZURE_SERVERLESS\DpuWithoutGAM\20220908115325"
/p:GX_PROGRAM_DIR="C:\Development\Trunk\Deploy\Genexus\debug"
/p:DeploySource="C:\models\TestServlessGAM\TestServerlessGAM\NetModel\Deploy\AZURE_SERVERLESS\DpuWithoutGAM_20220908115325.zip"
/p:DeployFileFullPath=<Path where the zip package will be copied. By default, it takes the value specied at the .gxdproj file>
/t:CreatePackage
```

### [Step 4. Deploy to Azure Serverless](#Step+4.+Deploy+to+Azure+Serverless)

It uploads the package to an Azure Function.  
Here you need to set the credentials for connecting to Azure.  
The MSBuild file used is located under <GeneXus Installation>\DeploymentTargets\AzureServerless.

```
MSBuild.exe "C:\Genexus\DeploymentTargets\AzureServerless\deploy.msbuild"
/p:TargetId="AZURE_SERVERLESS"
/p:GXDeployFileProject=<.gxdproj file Location>
/p:LANGUAGE="41" 
/p:GENERATOR=".NET"
/p:AZURE_SERVERLESS_FUNCTION_APP="HttpWinNet6"
/p:AZURE_SERVERLESS_RESOURCE_GROUP="HttpWinNet6"
/p:AZURE_SERVERLESS_SP_APP_ID="xxxxxxxxxxxxxxx"
/p:AZURE_SERVERLESS_SP_TENANT_ID="yyyyyyyyyyyyyyyyy"
/p:AZURE_SERVERLESS_SP_CREDENTIALS="zzzzzzzzzzzzzzzzzzz"
/p:AZURE_SERVERLESS_SESSION_STATE_PROVIDER="None"
/p:AZURE_SERVERLESS_GAM_CONNECTION_KEY="11111111111111111111"
/p:AZURE_APIM_SERVICE_NAME="GXAPIManagement"
/p:AZURE_APIM_RESOURCE_GROUP="apimanage"
/p:AZURE_APIM_API_ID="travel9"
/p:AZURE_APIM_API_DISPLAY_NAME="API travel9"
/p:AZURE_APIM_API_SERVICE_URL="https://httpwinnet6.azurewebsites.net"
/p:AZURE_APIM_API_PATH="travel9"
/p:AZURE_APIM_API_SUBSCRIPTION_REQUIRED="false"
/p:GX_PROGRAM_DIR="C:\Genexus"
/p:DEPLOY_TARGETS="C:\Development\Trunk3\Deploy\Genexus\Debug\DeploymentTargets\AzureServerless\azureserverless.targets" /p:DeployFullPath="C:\models\TestAPIObject3\TestServerlessGAM\NETSQLServerCloud\Deploy\AZURE_SERVERLESS\DpuWithGAM\20220808111607" 
/t:Deploy
```

**Note**: In case of setting */p:CreateCloudPackage="true"*, this steps does the 3rd Step also (it creates the cloud package).


|  |
| --- |
| **Backlinks** |
| [Toc:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Toc:Application Deployment tool (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54334) | [Cloud-native with GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51572) |
| [HowTo: Use GAM in Azure serverless architecture](https://wiki.genexus.com/commwiki/wiki?53363) |

---
