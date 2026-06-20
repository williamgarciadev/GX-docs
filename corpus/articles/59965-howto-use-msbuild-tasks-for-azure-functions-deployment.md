---
title: "HowTo: Use MSBuild tasks for Azure Functions deployment"
source_id: 59965
source_url: https://wiki.genexus.com/commwiki/wiki?59965
genexus_version: "18"
---

# HowTo: Use MSBuild tasks for Azure Functions deployment

Below are the MSBuild tasks related to the deployment of [Azure Functions](https://wiki.genexus.com/commwiki/wiki?47430) in order to create the package before uploading it to Azure.  
To deploy using the [GeneXus IDE](https://wiki.genexus.com/commwiki/wiki?5272) and understand the meaning of the properties, see [HowTo: Deploy as Azure Functions](https://wiki.genexus.com/commwiki/wiki?49351).  
  
The Azure Functions can be of any trigger type. The following is an example of [Azure HTTP-triggered functions](https://wiki.genexus.com/commwiki/wiki?49266).

### [Step 1 - Create deployment project](#Step+1+-+Create+deployment+project)

This task generates the .gxdproj file. The MSBuild file used is located under the GeneXus installation.

```
MSBuild.exe "C:\Genexus\deploy.msbuild"
/p:KBPath="C:\models\TestAzureFunctions"
/p:KBEnvironment="NETSQLServerCloud"
/p:KBVersion="TestAzureFunctions"
/p:ProjectName="DeploymentDataProvider_20250425094245"
/p:TargetId="AZURE_FUNCTIONS"
/p:AZURE_FUNCTIONS_TRIGGER_TYPE="http"
/p:ObjectNames="DataProvider:DataProvider1"
/p:DeployFullPath="C:\models\TestAzureFunctions\NETSQLServerCloud\Deploy\AZURE_FUNCTIONS\DeploymentDataProvider\20250425094245"
/p:GX_PROGRAM_DIR="C:\Genexus"
/t:CreateDeploy
```

### [Step 2. Create Package](#Step+2.+Create+Package)

Generates the package .zip file. The MSBuild file used is the .gxdproj file generated in the first step. This is a local package that contains all basic artifacts and is not suitable for deployment to Azure.

```
MSBuild.exe "C:\models\TestAzureFunctions\NETSQLServerCloud\web\DeploymentDataProvider_20250425094245.gxdproj"
/p:GX_PROGRAM_DIR="C:\Genexus"
/p:TargetId="AZURE_FUNCTIONS" 
/p:AZURE_FUNCTIONS_TRIGGER_TYPE="http"
/p:AZURE_FUNCTIONS_ROUTE_PREFIX="rest"
/p:AZURE_FUNCTIONS_SESSION_STATE_PROVIDER="None"
/p:DEPLOY_TYPE="BINARIES" 
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

This step creates the package to be deployed to Azure (it customizes the package created in Step 2).  
It uses the CreateCloudPackage.msbuild script, under the GeneXus directory.

```
MSBuild.exe "C:\Genexus\CreateCloudPackage.msbuild"
/p:TargetId="AZURE_FUNCTIONS"
/p:AZURE_FUNCTIONS_TRIGGER_TYPE="http"
/p:AZURE_FUNCTIONS_ROUTE_PREFIX="rest"
/p:AZURE_FUNCTIONS_SESSION_STATE_PROVIDER="None"
/p:DEPLOY_TYPE="BINARIES" 
/p:CreatePackageScript="createpackage.msbuild"
/p:CreatePackageTarget="CreatePackage"
/p:GENERATOR=".NET"
/p:GXDeployFileProject=<Path to the .gxdproj file generated at first step>
/p:DeployFullPath="C:\models\TestAzureFunctions\NETSQLServerCloud\Deploy\AZURE_FUNCTIONS\DeploymentDataProvider\20250425094245"
/p:GX_PROGRAM_DIR="C:\Development\Trunk\Deploy\Genexus\debug"
/p:DeploySource=C:\models\TestAzureFunctions\NETSQLServerCloud\Deploy\AZURE_FUNCTIONS\DpuWithoutGAM_20220908115325.zip"
/p:DeployFileFullPath=<Path where the zip package will be copied. By default, it takes the value specied at the .gxdproj file>
/t:CreatePackage
```

**Note**: For Azure HTTP-triggered functions, it's important to set the /p:AZURE\_FUNCTIONS\_TRIGGER\_TYPE="http" property at the create deployment and create package phases.


|  |
| --- |
| **Backlinks** |
| [Table of contents:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) |

---
