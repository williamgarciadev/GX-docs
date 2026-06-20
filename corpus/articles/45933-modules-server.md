---
title: "Modules Server"
source_id: 45933
source_url: https://wiki.genexus.com/commwiki/wiki?45933
genexus_version: "18"
---

# Modules Server

A Modules server is a repository of [packaged and shared modules](https://wiki.genexus.com/commwiki/wiki?31376).

Packaged modules can be shared through the file system or a [Repository Manager](https://wiki.genexus.com/commwiki/wiki?46750,,).

A repository manager that stores packaged modules (see [Modules Distribution in GeneXus](https://wiki.genexus.com/commwiki/wiki?31376)) is also called a GeneXus Knowledge Matrix, due to its feature of storing assets with knowledge; it will be called this way, or simply as Matrix, in this documentation.

### [Features of a Matrix](#Features+of+a+Matrix)

A Matrix, as a repository manager, stores assets, handles versioning of those assets, and also dependency management among versions of different assets.

It holds those assets in order to share them among GeneXus users; that is, members of a project's team, a company, an ecosystem, a region in the world or even to share those assets globally with the whole GeneXus community.

`[imagen omitida: wiki id 45934]`

### [Create your Matrix](#Create+your+Matrix)

You can use [Nexus Repository OSS](https://www.sonatype.com/nexus-repository-oss) as a repository manager for this.

Follow the steps below:

1) Install Nexus OSS

The main options to install Nexus are:

* Downloading the installation from <https://www.sonatype.com/nexus-repository-oss>
* Using Docker <https://hub.docker.com/r/sonatype/nexus/>
* There are also Cloud Formation templates to have an instance of Nexus in Amazon WebServices.

2) Once installed, create a repository hosted on Maven or NuGet. You can also use the already built-in 'maven-releases' repository as shown in the image below:

`[imagen omitida: wiki id 45937]`

3) Configure your Nexus to allow [anonymous access](https://help.sonatype.com/en/anonymous-access.html) for browsing and downloading assets.

### [Prepare your GeneXus installation to publish assets](#Prepare+your+GeneXus+installation+to+publish+assets)

#### [If you have chosen a maven-hosted repository](#If+you+have+chosen+a+maven-hosted+repository)

1) You need to [Download Maven](https://maven.apache.org/download.cgi) and install it.

2) Define credentials for Publishing.

You need the credentials of a user who has permission to publish on the Matrix.

Create or modify the following file: %USERPROFILE%\.m2\settings.xml. The credentials defined in that file will be used when you publish your modules on that Matrix.

```
<settings>
   <servers>
     <server>
       <id>Example Matrix</id>
       <username>Me</username>
       <password>MyPassword</password>
    </server>
  </servers>
</settings>
```

3) Define a new server of module references in GeneXus as explained in the next section.

#### [If you have chosen a NuGet-hosted repository](#If+you+have+chosen+a+NuGet-hosted+repository)

Make sure you have NuGet installed. To do this, check if the file 'nuget.exe' is located in %userprofile%\.gxmodules\.tools. If you cannot locate it, you can download it from the official [NuGet site](https://www.nuget.org/downloads).

### [Define your own Matrix in GeneXus](#Define+your+own+Matrix+in+GeneXus)

To do so, go to the GeneXus Menu > Knowledge Manager> Manage Module References, then click on 'Add'

* Select Nexus -(NuGet or Maven) in the Server Type
* Choose a name for your server (i.e.: Example Matrix).
* Choose the repository URL (i.e.: http://mymatrix.mycompany.com/repository/maven\_releases/).
* If you select NeXus - NuGet you must fill in your Username and Password.

`[imagen omitida: wiki id 55062]`

### [Publish a module to the Matrix](#Publish+a+module+to+the+Matrix)

Refer to [Package and Publish Modules](https://wiki.genexus.com/commwiki/wiki?46751)

### [Install assets of a Matrix](#Install+assets+of+a+Matrix)

Refer to [Manage Module References](https://wiki.genexus.com/commwiki/wiki?40172) for more information related to installing and managing packaged modules.

## [Predefined Modules Servers](#Predefined+Modules+Servers)

These module servers are predefined when installing GeneXus:

### [Local](#Local)

This server shows the modules that are available in your GeneXus installation. Typically, it holds the modules that are installed by the GeneXus Setup.

### [Global Matrix](#Global+Matrix)

Its purpose is to be a repository for modules shared all over the world with the whole GeneXus community.  
In October 2020, GeneXus SA started to share some modules on it (you still can't publish modules on that Matrix).


|  |
| --- |
| **Backlinks** |
| [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238) |
| [Manage Module References](https://wiki.genexus.com/commwiki/wiki?40172) | [Manage Module References (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55064) | [Module Author property](https://wiki.genexus.com/commwiki/wiki?46757) |
| [Module Description property](https://wiki.genexus.com/commwiki/wiki?46756) | [Module License URL property](https://wiki.genexus.com/commwiki/wiki?46633) | [Module Owner property](https://wiki.genexus.com/commwiki/wiki?46754) | [Module Project URL property](https://wiki.genexus.com/commwiki/wiki?46634) |
| [Module Resources property](https://wiki.genexus.com/commwiki/wiki?45010) | [Module Server URL property](https://wiki.genexus.com/commwiki/wiki?46635) | [Module Tags property](https://wiki.genexus.com/commwiki/wiki?46636) | [Module Version property](https://wiki.genexus.com/commwiki/wiki?46755) |
| [Toc:Modules](https://wiki.genexus.com/commwiki/wiki?22414) | [Modules Distribution in GeneXus](https://wiki.genexus.com/commwiki/wiki?31376) | [Modules Server (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55061) | [Package and Publish Modules](https://wiki.genexus.com/commwiki/wiki?46751) |
| [Package and Publish Modules (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55057) | [Package Name property](https://wiki.genexus.com/commwiki/wiki?46759) |

---
