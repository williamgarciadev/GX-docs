---
title: "HowTo: Deploy an Application to Docker"
source_id: 36951
source_url: https://wiki.genexus.com/commwiki/wiki?36951
genexus_version: "18"
---

# HowTo: Deploy an Application to Docker

Use the steps described in this article to easily deploy and run [Java](https://wiki.genexus.com/commwiki/wiki?12258), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892) and [.NET](https://wiki.genexus.com/commwiki/wiki?38604) generated applications in a Docker Container.

Note that these steps help you to deploy the generated programs, not the database. To deploy the database, see [Export Reorganization](https://wiki.genexus.com/commwiki/wiki?34476). For further options, see [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092).

## [Software Requirements](#Software+Requirements)

* [Docker Desktop](https://docs.docker.com/get-docker/)

## [Steps to deploy to Docker](#Steps+to+deploy+to+Docker)

**1.** Before you deploy your application for the first time to a specific target (e.g., production), creating a new [environment](https://wiki.genexus.com/commwiki/wiki?7115) in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) is recommended, so that it:

* Runs locally in the Tomcat or IIS of the computer used to work with GeneXus, and
* Is connected to the target (e.g., production) database.

**2.** Select Build All.

**3.** Go to the Build menu and select the [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) option.

**4.** In the Deployment screen:

**1.** Select the Main objects to be included in the deployment.

**2.** In Target, select the option "Docker Image".

**3.** Set the following properties as indicated below (All fields have default values):

**1.** [Docker base image property](https://wiki.genexus.com/commwiki/wiki?37047): Image that is used as a base to create the new one

**2.** [Maintainer name property](https://wiki.genexus.com/commwiki/wiki?37048): Name of the Author of the image; it's set as part of the metadata of the image

**3.** [Docker Environment variables property](https://wiki.genexus.com/commwiki/wiki?40607): All the environment variables you wish the image to have already instanced

**4.** [Image WebApp location property](https://wiki.genexus.com/commwiki/wiki?37049): Path inside the docker image where the application runs

**5.** [Docker image name property](https://wiki.genexus.com/commwiki/wiki?37050): Name of the generated docker image

**5.** Click on the Deploy button to create the Docker Image. The Output sends feedback about the process and the location of the generated files.

Now run the following command, in the Windows command prompt, to list the Docker images, including the one you created in the previous steps.

```
docker images
```

## [Steps to run the Docker Image locally](#Steps+to+run+the+Docker+Image+locally)

The following descriptions only apply when working on the developer's local machine.

### [Java](#Java)

[Java](https://wiki.genexus.com/commwiki/wiki?12258) environments generate images based on Linux. To run a container based on the previously created image, from the directory where the Dockerfile is located, execute the following command. See ([run command](https://docs.docker.com/engine/reference/commandline/run/)).

```
docker run --rm -p 9999:8080 <Docker image name>
```

Where:

*--rm*  
      Indicates that the container is deleted once it is shut down

*-p 9999:8080*  
      Indicates that the port 8080 (Tomcat default) of the container is exposed as 9999 on the host

*<Docker image name>*  
      Is the one created in the previous step

After successfully running this command, you can access the application's main object at http://localhost:9999/servlet/<Java package name>.<qualified object's name>.

### [.NET Framework (C#)](#.NET+Framework+%28C%23%29)

[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892) (C#) environments generate images based on Windows. To run a container based on the previously created image, execute the following command from the directory where the Dockerfile is located.

```
docker run --rm -p 9999:80 <Docker image name>
```

Where:

*--rm*  
      Indicates that the container is deleted once it is shut down

*-p 9999:80*  
      Indicates that the port 80 (IIS default) of the container is exposed as 9999 on the host

*<Docker image name>*  
      Is the one created in the previous step

**Note**: After a while, an error will be shown in the output but you can ignore it (.ref <https://github.com/Microsoft/aspnet-docker/issues/69>).

```
ERROR ( message:Cannot find requested collection element. )
Applied configuration changes to section "system.applicationHost/applicationPools" for "MACHINE/WEBROOT/APPHOST" at configuration commit path "MACHINE/WEBROOT/APPHOST"
```

After successfully running this command, you can access the application's main object at http://localhost:9999/<qualified object's name>.aspx.

### [.NET](#.NET)

[.NET](https://wiki.genexus.com/commwiki/wiki?38604) environments generate images based on Linux. To run a container based on the previously created image, execute the following command.

```
docker run --rm -p 9999:8080 -e ASPNETCORE_URLS="http://*:8080" <Docker image name>
```

Where:

*--rm*  
      Indicates that the container is deleted once it is shut down

*-p 9999:8080*  
      This binds port 8080 of the container to TCP port 9999 on all interfaces (address 0.0.0.0) on the host. See [publish or export port](https://docs.docker.com/reference/cli/docker/container/run/#publish).

*-e ASPNETCORE\_URLS*

     The parameter

```
-e ASPNETCORE_URLS
```

**is required for .NET 8** as it specfies the host and port Docker uses for HTTP connections for ASP.NET Core.

*<Docker image name>*  
      Is the one created in the previous step

### [Compatibility considerations](#Compatibility+considerations)

Default ASP.NET Core port changed its default. [Check the official documentation](https://learn.microsoft.com/en-us/dotnet/core/compatibility/containers/8.0/aspnet-port#reason-for-change).  
So this will not work:

docker run --rm -it -p 8000:80 <my-app>  
  
Since this breaking change there are some neccesary changes in the way the container is started. See [recommended actions](https://learn.microsoft.com/en-us/dotnet/core/compatibility/containers/8.0/aspnet-port#recommended-action).

Two alternatives are:

1. Use the "entrypoint" option to override the default ENTRYPOINT of the image (at the dockerfile).  Set the exposed port of the application.

```
docker run --rm -p <hostPort>:<ContainerPortPublished> --name <containerName> --entrypoint dotnet <imageName> bin/GxNetCoreStartup.dll <virtualPath> <localPath> <ContainerPortExposed>
```

GxNetCoreStartup.dll receives as parameter the virtualPath, LocalPath, and port.  
Example: docker run --rm -p 81:8080 --name mycontainer --entrypoint dotnet user/test:3.0 bin/GxNetCoreStartup.dll testvp /app 8080  
In this example the application will run at http://localhost:81/testvp/<webpanel>.aspx

2. Use the ASPNETCORE\_URLS environment variable.

```
docker run --rm -p 9999:8080 -e ASPNETCORE_URLS="http://*:8080" <Docker image name>
```

### [Notes](#Notes)

**Accesing a remote server**

To access a remote database server using a non-fully-qualified hostname from the container, you may need to specify a DNS search prefix. For example, if the DataStore server name is 'SqlServerSrv,' and the fully qualified name is 'mycompany.local.SqlServerSrv,' you can specify the prefix as follows:

```
docker run --rm -p 9999:5000 -e ASPNETCORE_URLS="http://*:5000" --dns-search mycompany.local <Docker image name>
```

After successfully running this command, you can access the application's main object at http://localhost:9999/<qualified object's name>.aspx.

**Having the application run in a virtual directory**

In NET generator, you can execute:

docker run --rm -p <hostPort>:**<ContainerPortPublished> --**name <containerName> --entrypoint dotnet <imageName> bin/GxNetCoreStartup.dll <virtualPath> <localPath> **<ContainerPortExposed>**

### [Restrictions](#Restrictions)

* Using default Docker base images
  + In the [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892) and
    [.NET](https://wiki.genexus.com/commwiki/wiki?38604) generators, it is essential to ensure that you have an SSL certificate. If such a certificate is not available, it is advisable to avoid setting the [Protocol specification property](https://wiki.genexus.com/commwiki/wiki?8079) to HTTPS to prevent the generation of timeout messages.
  + Sites are accessed via HTTP

## [See Also](#See+Also)

[Troubleshooting deployment to Docker Containers](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?36955,,)  
[Application Deployment MSBuild tasks](https://wiki.genexus.com/commwiki/wiki?42073)

## [FAQ](#FAQ)

#### [**1) I already have my own images where I want my apps to run. Can I deploy my app to those?**](#1%29+I+already+have+my+own+images+where+I+want+my+apps+to+run.+Can+I+deploy+my+app+to+those%3F)

Yes, you can. You can change the default base image to be used by GeneXus in the [Docker base image property](https://wiki.genexus.com/commwiki/wiki?37047). There you can set your own image and the Docker client will try to pull it from a registry if it's not available on your computer. Keep in mind that the [image WebApp location](https://wiki.genexus.com/commwiki/wiki?37049) property might also need to be changed.

You can generate the Dockerfile even without the 'Docker for Windows' requirement. For that purpose, use this feature and select the option to deploy to Docker as usual.   
A warning will appear, 'warning: Dockerfile successfully created, but no docker image was generated because Docker client was not found.' in that case.

If you want to just create the package, use the "Only Package option" in GeneXus (or the [Deploy to Docker MSBuild task](https://wiki.genexus.com/commwiki/wiki?47839)). If you try to build the image and don't have the Docker engine up and running, you will get an error.


|  |
| --- |
| **Backlinks** |
| [Application Configuration using Environment Variables](https://wiki.genexus.com/commwiki/wiki?39459) | [Application Configuration using Environment Variables in .NET and Java](https://wiki.genexus.com/commwiki/wiki?53336) | [Application Configuration using Environment Variables in Cloud Services](https://wiki.genexus.com/commwiki/wiki?53339) |
| [Table of contents:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Table of contents:Application Deployment tool (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54334) | [Considerations for building and deploying applications to containers](https://wiki.genexus.com/commwiki/wiki?45309) | [Continuous Deployment](https://wiki.genexus.com/commwiki/wiki?44673) |
| [Deploy Application Targets](https://wiki.genexus.com/commwiki/wiki?42079) | [Docker base image property](https://wiki.genexus.com/commwiki/wiki?37047) | [Docker Environment variables property](https://wiki.genexus.com/commwiki/wiki?40607) |
| [Docker Image App location property](https://wiki.genexus.com/commwiki/wiki?37049) | [Docker image name property](https://wiki.genexus.com/commwiki/wiki?37050) | [HowTo: Deploy an Application to Docker (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54337) |
| [HowTo: Set up the environment to test Observability (using Grafana)](https://wiki.genexus.com/commwiki/wiki?56829) | [HowTo: Setup the environment to test Observability (using AWS CloudWatch)](https://wiki.genexus.com/commwiki/wiki?57258) | [HowTo: Watch .NET logs using OpenTelemetry (with SigNoz)](https://wiki.genexus.com/commwiki/wiki?57281) | [Maintainer name property](https://wiki.genexus.com/commwiki/wiki?37048) |

---
