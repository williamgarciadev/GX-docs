---
title: "Deploy to docker containers: taking properties from configuration file"
source_id: 51122
source_url: https://wiki.genexus.com/commwiki/wiki?51122
genexus_version: "18"
---

# Deploy to docker containers: taking properties from configuration file

The DOCKER\_BASE\_IMAGE and DOCKER\_WEBAPPLOCATION properties can be taken from a configuration file and you can avoid adding their definitions to the MSBuild execution (for more information about these properties see [Deploy to Docker MSBuild task](https://wiki.genexus.com/commwiki/wiki?47839)).

The mechanism is as follows:

1. If the DOCKER\_BASE\_IMAGE and DOCKER\_WEBAPPLOCATION (or DOCKER\_APPLOCATION) properties are specified when the MSBuild is run, they are taken from there.

2. If both or either of them are empty the "BuildEnvironment" property is verified, which indicates the configuration file (.json) that should be read to extract the information from these properties.

The BuildEnvironment property indicates the environment to which this build corresponds.  
  
For example, if you have / p: BuildEnvironment = dev, it looks for docker.dev.json, which must be in the root of GeneXus.

The file format must be the same as the docker.prod.json that is distributed with GeneXus (1).

If the file cannot be found, an error similar to the following occurs:

"Taking default values ​​for Base Image and Image WebApp Location from docker.dev.json file.  
Configuration file not found and default parameters not set. Base Image and Image WebApp Location cannot be empty."

3. If at least one of the properties (DOCKER\_BASE\_IMAGE and DOCKER\_WEBAPPLOCATION/DOCKER\_APPLOCATION) in the MSBuild command is not referenced and the BuildEnvironment property is not indicated, by default docker.prod.json is read and the user is warned:

"Taking default values ​​for Base Image and Image WebApp Location from docker.prod.json file."

(1)The docker.prod.json file looks as follows:

```
{
    "Images": {
        ".NET Framework": "genexus/dotnet:4.6.2",
        ".NET": "mcr.microsoft.com/dotnet/aspnet:6.0",
        "C#": "genexus/dotnet:4.6.2",
        ".NET Core": "mcr.microsoft.com/dotnet/aspnet:6.0",
        "Java": "tomcat:10-jdk15-openjdk-oracle"
    },
    "CMDAppImages": {
        ".NET Framework": "genexus/dotnet:4.6.2",
        ".NET": "mcr.microsoft.com/dotnet/aspnet:6.0",
        "C#": "genexus/dotnet:4.6.2",
        ".NET Core": "mcr.microsoft.com/dotnet/aspnet:6.0",
        "Java": "openjdk:15"
    },
    "WebAppLocation": {
        ".NET Framework": "c:/inetpub/wwwroot/",
        ".NET": "/app",
        "C#": "c:/inetpub/wwwroot/",
        ".NET Core": "/app",
        "Java": "/usr/local/tomcat/webapps/"
    },
    "AppLocation": {
        ".NET Framework": "/app",
        ".NET": "/app",
        "C#": "/app",
        ".NET Core": "/app",
        "Java": "/usr/src/myapp"
    }
}
```

Note: The .json file is read considering the "Generator" MSBuild property. This property must be set using the same casing as in the configuration file.

Otherwise, the MSBuild execution throws the error: "The given key was not present in the dictionary."

Example:

```
MSbuild.exe /nologo /verbosity:normal /ToolsVersion:14.0 "c:\genexus\DeploymentTargets\Docker\deploy.msbuild" /p:DeploySource="c:\kbaux\Deploy\JavaModel\Docker\kbauxJavaEnvironmentDeploy.war" /p:DOCKER_MAINTAINER="fullgxops <fullgxops@genexus.com>" /p:DOCKER_IMAGE_NAME="kbauxjavaenvironment" /p:GENERATOR="Java" /p:BuildEnvironment=dev /t:Deploy /l:FileLogger,Microsoft.Build.Engine;logfile=c:\fullgx\temp\DeployDocker.log
```

## [See also](#See+also)

[Deploy to Docker MSBuild task](https://wiki.genexus.com/commwiki/wiki?47839)


|  |
| --- |
| **Backlinks** |
| [Toc:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Toc:Application Deployment tool (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54334) |

---
