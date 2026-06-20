---
title: "GeneXus Server Azure - Generate Sources (.NET)"
source_id: 53679
source_url: https://wiki.genexus.com/commwiki/wiki?53679
genexus_version: "18"
---

# GeneXus Server Azure - Generate Sources (.NET)

In order to use Azure DevOps solution building features, your GeneXus [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) can be exported as .NET source code.

Once the sources are generated, you may synchronize your project with [Azure Repos](https://learn.microsoft.com/en-us/azure/devops/repos/get-started/what-is-repos?view=azure-devops) using the [Synchronize to Git task](https://wiki.genexus.com/commwiki/wiki?53681).

The following pipeline job has to be added to your pipeline definition:

```
  - job: GenerateSources
    steps:
      - script: >
          $(MSBUILD) "$(BL_PATH)\deploy.msbuild" /t:CreateDeploy /p:KBPath="$(KB_PATH)" 
          /p:KBEnvironment="$(KBENVIRONMENT)" /p:DeploymentUnit="$(DEPLOYMENT_UNIT)" 
          /p:ProjectName="$(DEPLOY_NAME)" /p:TargetId="AZURE_SERVERLESS" 
          /p:ObjectNames="DeploymentUnitCategory:$(DEPLOYMENT_UNIT)"
          /p:DEPLOY_TARGETS="$(BL_PATH)\DeploymentTargets\AzureServerless\azureserverless.targets" 
          /p:DeployFullPath="$(KB_PATH)\NetModel\Deploy\AZURE_SERVERLESS\$(DEPLOYMENT_UNIT)\$(DEPLOY_NAME)" 
          /p:WebSourcePath="$(KB_PATH)\NetModel\web" /p:GX_PROGRAM_DIR="$(BL_PATH)" /p:INCLUDE_GAM="False" 
          /p:INCLUDE_GXFLOW_BACKOFFICE="False" /p:DEPLOY_TYPE="SOURCES" 
          /p:APPLICATION_KEY="$(APPLICATION_KEY)" /p:TimeStamp="$(DEPLOY_NAME)"
        name: CreateSources

      - script: >  
          $(MSBUILD) /ToolsVersion:4.0 "$(KB_PATH)\NetModel\web\$(DEPLOY_NAME).gxdproj" /t:CreatePackage 
          /p:GX_PROGRAM_DIR="$(BL_PATH)" /p:AZURE_PUBLISH_SETTINGS="$(PUBLISH_SETTINGS)" 
          /p:APPLICATION_KEY="$(APPLICATION_KEY)" /p:DEPLOY_TYPE="SOURCES" /p:TimeStamp="$(DEPLOY_NAME)"
          /p:INCLUDE_GAM="False" /p:INCLUDE_GXFLOW_BACKOFFICE="False"
        name: PackageSources
      
      - script: >
          $(MSBUILD) "$(BL_PATH)\CreateCloudPackage.msbuild" /p:TargetId="AZURE_SERVERLESS" 
          /p:CreatePackageScript="createpackage.msbuild" /p:CreatePackageTarget="CreatePackage" 
          /p:DeployFullPath="$(KB_PATH)\NetModel\Deploy\AZURE_SERVERLESS\$(DEPLOYMENT_UNIT)\$(DEPLOY_NAME)" 
          /p:WebSourcePath="$(KB_PATH)\NetModel\web" /p:ProjectName="$(DEPLOY_NAME)" 
          /p:DeploymentUnit="$(DEPLOYMENT_UNIT)" /p:GX_PROGRAM_DIR="$(BL_PATH)"  
          /p:APPLICATION_KEY="$(APPLICATION_KEY)" /p:INCLUDE_GAM="False" 
          /p:INCLUDE_GXFLOW_BACKOFFICE="False" /p:APP_UPDATE="NONE" /p:ENABLE_KBN="False" /p:TARGET_JRE="9" 
          /p:PACKAGE_FORMAT="Automatic" /p:DEPLOY_TYPE="SOURCES" /p:TimeStamp="$(DEPLOY_NAME)" 
          /p:DeploySource="$(KB_PATH)\NetModel\Deploy\AZURE_SERVERLESS\$(DEPLOY_NAME).zip" 
          /t:CreatePackage
        name: AdditionalResources
```

It is recommended that you set up your pipeline dependency to the Build step. Additionally, you may add an unconditional job trigger.  
That can be accomplished by adding the following snippet to your job:

```
    dependsOn: BuildKnowledgeBase
    condition: or(succeeded(), eq(${{parameters.forceSources}}, True))
```

Parameter definition can be added as a root tag anywhere in your pipeline, as follows:

```
parameters:
- name: forceSources
  displayName: Force Generate Sources
  type: boolean
  default: false
  values:
  - true
  - false
```

### [Variables](#Variables)

There are no specific variable definitions required for the task. See [GeneXus Server Azure Configuration](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?52099,,) for the generic variables required.

### [See Also](#See+Also)

[Package Type property](https://wiki.genexus.com/commwiki/wiki?53373)


|  |
| --- |
| **Backlinks** |
| [GeneXus Server Azure - Synchronize to Git](https://wiki.genexus.com/commwiki/wiki?53681) |

---
