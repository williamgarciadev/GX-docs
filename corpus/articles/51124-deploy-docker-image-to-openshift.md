---
title: "Deploy docker image to Openshift"
source_id: 51124
source_url: https://wiki.genexus.com/commwiki/wiki?51124
genexus_version: "18"
---

# Deploy docker image to Openshift

OpenShift is an orchestrator standing on Kubernetes. It has some additional security restrictions. In particular (in addition to some other differences), this platform runs any container using a ramdon [UUID](https://www.openshift.com/blog/a-guide-to-openshift-and-uids). So if the docker image is not ready to run as non-root, errors will occur.

In order to deploy to Openshift, the "Container" property = {Default, Openshift} is available in the Deploy Target Docker Image properties (only for Java and .Net). This corresponds to the DOCKER\_CONTAINER\_RUNTIME MSBuild property. For more information see [Deploy to Docker MSBuild task](https://wiki.genexus.com/commwiki/wiki?47839).

When the container is Openshift, the "Registry Image" property becomes visible. Through it, the registry of the base image {Docker hub, Redhat registry} can be selected. The corresponding MSBuild property is DOCKER\_IMAGE\_REGISTRY.

The MSBuild in this case is as follows:

```
MSbuild.exe /nologo /verbosity:normal /ToolsVersion:14.0 "c:\fullgx\gxsalto\DeploymentTargets\Docker\deploy.msbuild"
/p:DeploySource="c:\fullgx\kbaux\Deploy\NetCoreModel\Docker\DeployNet.zip"
/p:DOCKER_BASE_IMAGE=mcr.microsoft.com/dotnet/core/aspnet:6.0
/p:DOCKER_MAINTAINER="fullgxops <fullgxops@genexus.com>"
/p:DOCKER_WEBAPPLOCATION="/app"
/p:DOCKER_IMAGE_NAME="kbauxnetcoreenvironment"
/p:GENERATOR=".NET"
/p:DOCKER_CONTAINER_RUNTIME=Openshift
/p:DOCKER_IMAGE_REGISTRY=DockerHub
/t:Deploy /l:FileLogger,Microsoft.Build.Engine;logfile=c:\fullgx\temp\DeployDocker.log
```

Note that :

1. If Redhat registry is chosen, in "Base Image" property (DOCKER\_BASE\_IMAGE MSBuild property) an image from the Redhat image catalog must be entered.

To authenticate and download the base image using the docker command, it is enough to log in to the machine once; then the credentials will be saved in a credentials store ($HOME/.docker/config.json on Linux or %USERPROFILE%/.Docker/config.json on Windows). See [this](https://docs.docker.com/engine/reference/commandline/login/#privileged-user -requirement) reference. For more information about authentication when downloading images from Redhat, see [here](https://access.redhat.com/RegistryAuthentication).

2. When images are non-root, they cannot listen on ports less than 1024.  
In the case of .Net generator, when running the image, the user must use the -expose option to indicate a port that is allowed taking into account this restriction.

### [See also](#See+also)

[Deploy to Docker MSBuild task](https://wiki.genexus.com/commwiki/wiki?47839)


|  |
| --- |
| **Backlinks** |
| [Toc:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Toc:Application Deployment tool (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54334) |

---
