---
title: "Deploy to Docker MSBuild task"
source_id: 47839
source_url: https://wiki.genexus.com/commwiki/wiki?47839
genexus_version: "18"
---

# Deploy to Docker MSBuild task

To deploy to Docker, there are MSBuild scripts to set up the package and build the Docker image.

Docker is an external target and, as for all external targets, the deployment is performed using the [GitHub deployment targets](https://github.com/genexuslabs/deployment-targets) solution.

It is possible to set up a package with all the necessary files ready to build the Docker image, or do both—create the package and build the image.

That depends on the CI pipeline you need to define. If you do not have the Docker requirements to build the Docker image in the machine where the GeneXus application is built, you can just set up the package and move it to a location where you can run the Docker engine.

This document explains the separate steps to create the package and build the image. Consider that all these steps can be done inside GeneXus also using the [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092)

**Summary**

* [Create package](#Create+package)
* [Build the Docker image](#Build+the+Docker+image)

+ [Note](#Note+)

* [Availability](#Availability)

After having run the two basic MSBuild scripts, as described in [Application Deployment MSBuild tasks](https://wiki.genexus.com/commwiki/wiki?42073) (create deployment and create package), you can execute the following MSBuild scripts to have a Docker image built.

## [Create package](#Create+package)

This step creates a package that is suitable for doing a Docker build and then a Docker run. By default, a context folder is created below the root directory of the DeploySource indicated as a property of the MSBuild. You can change it using the DeployDirectory property.

Note that the configuration of Kubernetes (K8S) is optional as well as Redis configuration.

```
MSBuild.exe  /ToolsVersion:4.0 "C:\Genexus\CreateCloudPackage.msbuild"
/p:TargetId="DOCKER"
/p:CreatePackageScript="createpackage.msbuild"
/p:CreatePackageTarget="CreatePackage"
/p:GXDeployFileProject=<path to the .gxdproj file>
/p:DeploySource="C:\models\Testdeploy3\NETSQLServer003\Deploy\DOCKER\DeploymentUnit3_20220428101527.zip"
/p:WebSourcePath="C:\models\Testdeploy3\NETSQLServer003\web"
/p:ProjectName="DeploymentUnit3_20220428101527"
/p:DeploymentUnit="DeploymentUnit3"
/p:GX_PROGRAM_DIR="C:\Genexus"
/p:DOCKER_CONTAINER_RUNTIME="Default"
/p:DOCKER_IMAGE_REGISTRY="DockerHub"
/p:DOCKER_MAINTAINER="Sabrina <Sabrina@example.com>"
/p:DOCKER_WEBAPPLOCATION="/app"
/p:K8S_GENERATE_KUBERNETES="True"
/p:K8S_NAMESPACE="default"
/p:K8S_INITIAL_REPLICAS="2"
/p:K8S_SERVICE_TYPE="LoadBalancer"
/p:K8S_ENABLE_REDIS="True"
/p:DOCKER_ENVVARS=""
/t:CreatePackage
```

Then, the assembled package consists of:

* Application binaries
* Dockerfile

Specifically, in the case of NET Web and CMD app, the context directory contains the Dockerfile plus a temp directory containing the entire decompressed application.

When Kubernetes is activated, you will have, for example:

`[imagen omitida: wiki id 51130]`

In the case of Java Web, you will have the .War file plus the Dockerfile. And for CMD apps, the context folder will contain the JAR file of the application, plus the Dockerfile and the Drivers directory will all the dependencies.

`[imagen omitida: wiki id 51131]`

Therefore, if you copy that entire directory on any machine that has Docker daemon, you can build and run the image.

## [Build the Docker image](#Build+the+Docker+image)

After you have set up the package, you can build and get a Docker image by executing the following MSBuild:

```
MSBuild.exe /ToolsVersion:4.0 "C:\Genexus\DeploymentTargets\Docker\deploy.msbuild" 
/p:DOCKER_IMAGE_NAME="nameprojectnetsqlserver" 
/p:DeploySource="C:\models\NameProject\NETSQLServer003\Deploy\DOCKER\DeploymentUnit_20220430215655.zip" 
/p:CreateCloudPackage ="false"
/t:Deploy
```

In order to run the Docker image, you have to push it to a registry and run it using the docker run command.

### [Note](#Note+)

For compatibility issues, the deploy.msbuild script under DeploymentTargets\Docker folder, can still be used to do both tasks (generate the package and build the docker image)  
The **CreateCloudPackage**property is used for that purpose. If it's not assigned or it's true, the package will be created.  
Only when it's false, the package is not created and only a build of the image is done (which should have been created in a previous step).

## [Availability](#Availability)

The division of the Docker deployment in two steps is supported since [GeneXus 17 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?49971,,)

Since GeneXus 18 Upgrade 6 using DOCKER\_WEBAPPLOCATION property is the same as using DOCKER\_APPLOCATION.


|  |
| --- |
| **Backlinks** |
| [Toc:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Toc:Application Deployment tool (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54334) | [Deploy a command-line procedure to Docker containers](https://wiki.genexus.com/commwiki/wiki?51121) |
| [Deploy docker image to Openshift](https://wiki.genexus.com/commwiki/wiki?51124) | [Deploy to docker containers: taking properties from configuration file](https://wiki.genexus.com/commwiki/wiki?51122) |
| [HowTo: Deploy an Application to Docker](https://wiki.genexus.com/commwiki/wiki?36951) | [HowTo: Deploy an Application to Docker (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54337) | [Observability with Azure Monitor Application Insights](https://wiki.genexus.com/commwiki/wiki?54383) | [Observability with Azure Monitor Application Insights (GeneXus 18 Upgrade 6)](https://wiki.genexus.com/commwiki/wiki?56153) |

---
