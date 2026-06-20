---
title: "HowTo: Deploy an Application to Docker (GeneXus 18 Upgrade 2 or prior)"
source_id: 54337
source_url: https://wiki.genexus.com/commwiki/wiki?54337
genexus_version: "18"
---

# HowTo: Deploy an Application to Docker (GeneXus 18 Upgrade 2 or prior)

Use the steps described in this article to easily deploy and run [Java](https://wiki.genexus.com/commwiki/wiki?12258), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892) and [.NET](https://wiki.genexus.com/commwiki/wiki?38604) generated applications in a Docker Container.

Note that these steps help you to deploy the generated programs, not the database. To deploy the database, refer to [Export Reorganization](https://wiki.genexus.com/commwiki/wiki?34476). For further options, refer to [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092).

Software Requirements:

* [Docker for Windows](https://wiki.genexus.com/commwiki/wiki?39548,,) (\*)

### [Steps to deploy to Docker](#Steps+to+deploy+to+Docker)

**1.** Before you deploy your application for the first time to a specific target (eg.: production), creating a new [Environment](https://wiki.genexus.com/commwiki/wiki?7115) in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) is recommended, so that it:

* runs locally in the Tomcat or IIS of the computer used to work with GeneXus and
* is connected to the target (e.g.: production) database

**2.** Build All

**3.** Go to the Build menu and select the [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) option

**4.** In the Deployment screen:

**1.** Select the Main objects to be included in the deployment

**2.** In Target, select the option "Docker Image"

**3.** Set the following properties as indicated below (All fields have default values):

**1.** [Docker base image property](https://wiki.genexus.com/commwiki/wiki?37047): The image that is used as a base to create the new one

**2.** [Maintainer name property](https://wiki.genexus.com/commwiki/wiki?37048): The name of the Author of the image; it's set as part of the metadata of the image

**3.** [Docker Environment variables property](https://wiki.genexus.com/commwiki/wiki?40607): All the environment variables you wish the image to have already instanced

**4.** [Image WebApp location property](https://wiki.genexus.com/commwiki/wiki?37049): The path inside the docker image where the application runs

**5.** [Docker image name property](https://wiki.genexus.com/commwiki/wiki?37050): The name of the generated docker image

**5.** Click on the Deploy button to create the Docker Image. The Ouput sends feedback about the process and the location of the generated files.

Now run the following command, in the Windows command prompt, to list the Docker images, including the one you created in the previous steps

```
docker images
```

### [Steps to run the Docker Image](#Steps+to+run+the+Docker+Image)

#### [Java](#Java)

[Java](https://wiki.genexus.com/commwiki/wiki?12258) environments generate images based on Linux. To run a container based on the previously created image - positioned at the directory where the Dockerfile is, execute the following command. See ([run command](https://docs.docker.com/engine/reference/commandline/run/)).

```
docker run --rm -p 9999:8080 <Docker image name>
```

**Where:**

*--rm*  
      Indicates that the container is deleted once it is shut down

*-p 9999:8080*  
      Indicates that the port 8080 (Tomcat default) of the container is exposed as 9999 on the host

*<Docker image name>*  
      Is the one created in the previous step

After successfully running this command, you can access the application's main object at http://localhost:9999/servlet/<Java package name>.<qualified object's name>.

#### [.NET Framework (C#)](#.NET+Framework+%28C%23%29)

[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892) (C#) environments generate images based on Windows. To run a container based on the previously created image, execute the following command - positioned at the directory where the Dockerfile is.

```
docker run --rm -p 9999:80 <Docker image name>
```

**Where:**

*--rm*  
      Indicates that the container is deleted once it is shut down

*-p 9999:80*  
      Indicates that the port 80 (IIS default) of the container is exposed as 9999 on the host

*<Docker image name>*  
      Is the one created in the previous step

**Note**: After a while, an error will be shown in the output, but you can ignore it (.ref <https://github.com/Microsoft/aspnet-docker/issues/69>)

```
ERROR ( message:Cannot find requested collection element. )
Applied configuration changes to section "system.applicationHost/applicationPools" for "MACHINE/WEBROOT/APPHOST" at configuration commit path "MACHINE/WEBROOT/APPHOST"
```

After successfully running this command, you can access the application's main object at http://localhost:9999/<qualified object's name>.aspx.

#### [.NET](#.NET)

[.NET](https://wiki.genexus.com/commwiki/wiki?38604) environments generate images based on Linux. To run a container based on the previously created image, execute the following command.

```
docker run --rm -p 9999:80 <Docker image name>
```

**Where:**

*--rm*  
      Indicates that the container is deleted once it is shut down

*-p 9999:80*   
      Indicates that the port 80 (web default) is exposed as 9999 on the host

*<Docker image name>*  
      Is the one created in the previous step

After successfully running this command, you can access the application's main object at http://localhost:9999/<qualified object's name>.aspx.

### [Restrictions](#Restrictions)

* Using default Docker base images
  + [Protocol specification property](https://wiki.genexus.com/commwiki/wiki?8079) must not be set to HTTPS in
    [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892) and
    [.NET](https://wiki.genexus.com/commwiki/wiki?38604)
  + Sites are accessed via HTTP
* Deployment package (war) created in Java is compatible with Tomcat 8.x
* Deployment package created in [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892) or [.NET](https://wiki.genexus.com/commwiki/wiki?38604) is compatible with IIS 8 (or higher)

### [See Also](#See+Also)

[Troubleshooting deployment to Docker Containers](https://wiki.genexus.com/commwiki/wiki?36955,,)  
[Application Deployment MSBuild tasks](https://wiki.genexus.com/commwiki/wiki?42073)

### [FAQ](#FAQ)

#### [**1) I already have my own images where I want my apps to run. Can I deploy my app to those?**](#1%29+I+already+have+my+own+images+where+I+want+my+apps+to+run.+Can+I+deploy+my+app+to+those%3F)

Yes, you can. You can change the default base image to be used by Genexus in the [Docker base image property](https://wiki.genexus.com/commwiki/wiki?37047). There you can set your own image and the docker client will try to pull it from a registry if it's not available on your computer. Keep in mind that the [image WebApp location](https://wiki.genexus.com/commwiki/wiki?37049) property might also be necessary to be changed.

Since [GeneXus 16 upgrade 9](https://wiki.genexus.com/commwiki/wiki?45275,,), you can generate the dockerfile even without the 'Docker for windows' requirement. For that, use this feature and select the option to deploy to docker as usual.   
A warning will appear, 'warning: Dockerfile successfully created, but no docker image was generated because Docker client was not found.' in that case.

Since [GeneXus 17 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?49971,,) if you want to just create the package, use the "Only Package option" in GeneXus (or the [Deploy to Docker MSBuild task](https://wiki.genexus.com/commwiki/wiki?47839) msbuild) If you try to build the image and don't have docker engine up and running, you will get an error.
