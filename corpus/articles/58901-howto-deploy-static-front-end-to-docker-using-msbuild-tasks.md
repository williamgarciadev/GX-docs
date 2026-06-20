---
title: "HowTo: Deploy Static Front end to Docker using MSBuild Tasks (GeneXus 18 Upgrade 6 or prior)"
source_id: 58901
source_url: https://wiki.genexus.com/commwiki/wiki?58901
genexus_version: "18"
---

# HowTo: Deploy Static Front end to Docker using MSBuild Tasks (GeneXus 18 Upgrade 6 or prior)

This article shows you the steps to deploy a Static Front end application to Docker. If you want to do it using the Application Deployment tool inside GeneXus, see [HowTo: Deploy Frontend applications to Docker containers](https://wiki.genexus.com/commwiki/wiki?51104).

The [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) is based on [MSBuild Tasks](https://wiki.genexus.com/commwiki/wiki?3908). Using those tasks, you can automate deployment.

In the case of Frontend applications, three MSBuild scripts are executed to perform the deployment.

### [Step 1. Create Front end Project](#Step+1.+Create+Front+end+Project)

GeneXus provides a script called *deploy.msbuild* (located at the root of the GeneXus installation) which is used to create a deployment project for Frontend applications, when the Target deployment (TargetId) is "STATICFRONTEND." This step creates a file called *<ProjectName>.gxdproj* (an MSBuild script) which contains a list of the selected objects of the Deployment Unit object, and some environment properties for the deployment. This gxdproj file is used as input for the MSBuild task that creates the package.

Properties to add to the MSBuild execution:

**TargetId**: STATICFRONTEND  
**DEPLOY\_TARGETS**: Reference to *.targets* file where the validations are implemented (staticfrontend.targets).  
**KBPath**: Path to the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836)  
**KBVersion**: Name of the version to be set as active  
**KBEnvironment**: Name of the environment in that version  
**DeploymentUnit**: Name of the deployment unit  
**ProjectName**: Name of the generated *.gxdproj* file. By default it is "DeploymentUnit\_<TimeStamp>.gxdproj".  
**ObjectNames**: Names and types of the objects to deploy (deployment units can also be selected) (ref: How to specify an object list in a MSBuild task). This parameter is optional if you specify the DeploymentUnit property.  
**Outputpath**: Where the *.gxdproj* is saved. The gxdproj file is saved under $KB.Location$\$Model.TargetPath$\web if Outputpath is not defined.

```
MSBuild.exe  /ToolsVersion:4.0 "C:\Genexus\deploy.msbuild"
/p:KBPath="C:\models\TestAngular\TestAngular"
/p:KBEnvironment="NETSQLServer"
/p:KBVersion="TestAngular"
/p:DeploymentUnit="DeploymentUnit1"
/p:ProjectName="DeploymentUnit1_20220616193203"
/p:TargetId="STATICFRONTEND"
/p:ObjectNames="WorkWithDevices:WorkWithDevicesPerson"
/p:DEPLOY_TARGETS="C:\Development\Trunk\Deploy\Genexus\debug\DeploymentTargets\StaticFrontEnd\staticfrontend.targets"
/t:CreateDeploy
```

### [Step 2. Create Front end Package](#Step+2.+Create+Front+end+Package)

This step creates a folder containing all the necessary artifacts to build the Docker image.  
The directory can be specified using the *DeployDirectory* MSBuild property. By default, the folder is named "context" and is located under Deploy\STATICFRONTEND\<DeploymentUnit>\context directory of the KB.

**GXDeployFileProject**: The path to the .gxdproj file generated in the "Create Front end Project" step (including the name of the file).   
**ProjectRootDirectory**: The path to the directory under the Knowledge Base, where the Angular application is generated (it is always under the mobile\Angular folder). For example: "C:\models\TestAngular\TestAngular\NetSQLServer005\mobile\Angular"  
**GenExtensionName**: The name of the Front end generator (for example, Angular).  
**DeploymentScriptDocker**: Each Front end generator should have its own script for packaging to Docker. This should be specified at the DeploymentScriptDocker MSBuild property. In the case of Angular, it is deploy.angular.docker.msbuild, located under <GeneXus installation>\GenExtensions\SmartDevices\Angular\deploy directory.  
**STATICFRONTEND\_DOCKER\_APPLOCATION**: (required) It's the location inside the Docker image where the app will be located.  
**STATICFRONTEND\_PROVIDER**: In this case, it has to be "Docker."  
**GX\_PROGRAM\_DIR**: GeneXus program directory.

```
MSBuild.exe /ToolsVersion:4.0 "C:\Genexus\CreateFrontendPackage.msbuild"
/p:GXDeployFileProject="C:\models\TestAngular\TestAngular\NETSQLServer003\Web\DeploymentUnit1_20220616193203.gxdproj"
/p:ProjectRootDirectory="C:\models\TestAngular\TestAngular\NETSQLServer003\mobile\Angular"
/p:GenExtensionName="Angular" 
/p:STATICFRONTEND_DOCKER_APPLOCATION="app"
/p:DeploymentScriptDocker="deploy.angular.docker.msbuild"
/p:STATICFRONTEND_PROVIDER="docker"
/p:GX_PROGRAM_DIR="C:\Genexus"
/t:CreatePackage
```

### [Step 3. Build Image](#Step+3.+Build+Image)

This step creates the Docker container (builds the Docker image). In order to run the image, you should push it to a registry and run it afterwards.

**STATICFRONTEND\_PROVIDER**: In this case, it has to be "Docker."  
**DeployFullPath**: Where the package to build is located.  
**GX\_PROGRAM\_DIR**: GeneXus program directory.  
**GXDeployFileProject**: The path to the .gxdproj file generated in the "Create Front end Project" step (including the name of the file).   
**STATICFRONTEND\_DOCKER\_IMAGE\_NAME**: The Docker image name. It has to be a valid Docker image name in order to be pushed to any registry.

```
MSBuild.exe /ToolsVersion:4.0 "C:\Genexus\DeploymentTargets\StaticFrontEnd\deploy.msbuild"
/p:STATICFRONTEND_PROVIDER="docker"
/p:GX_PROGRAM_DIR="C:\Genexus"
/p:DeployFullPath="C:\models\TestAngular\TestAngular\NETSQLServer003\Deploy\STATICFRONTEND\DeploymentUnit1\20220616202241"
/p:GXDeployFileProject="C:\models\TestAngular\TestAngular\NETSQLServer003\Web\DeploymentUnit1_20220616193203.gxdproj" 
/p:STATICFRONTEND_DOCKER_IMAGE_NAME="testangular:1.0" 
/t:Deploy
```

To run the Docker image, you can check first if it was created successfully, using the Docker images command:

`[imagen omitida: wiki id 51117]`

Then you can run it locally if you wish, using Docker desktop or the command line. The Docker container runs at port 80, but it can be changed by editing the nginx.conf template, as explained in [HowTo: Deploy Frontend applications to Docker containers](https://wiki.genexus.com/commwiki/wiki?51104)

`[imagen omitida: wiki id 51118]`

The application always runs under the "app" directory, as shown in the image.

`[imagen omitida: wiki id 51119]`

### [Troubleshooting](#Troubleshooting)

An effective way to troubleshoot these applications is to check the network traffic at the web developer tools in the browser (F12). The CORS error can be seen there, for instance.  
Errors at the Docker image itself can be inspected using Docker desktop.

### [Scope](#Scope)

**Generators:**[Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Availability](#Availability)

Since [GeneXus 17 Upgrade 11](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?49972,,).
