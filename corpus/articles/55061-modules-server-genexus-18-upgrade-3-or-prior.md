---
title: "Modules Server (GeneXus 18 Upgrade 3 or prior)"
source_id: 55061
source_url: https://wiki.genexus.com/commwiki/wiki?55061
genexus_version: "18"
---

# Modules Server (GeneXus 18 Upgrade 3 or prior)

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

2) Once installed, create a maven hosted repository. You can also use the already built-in 'maven-releases' repository.

`[imagen omitida: wiki id 45937]`

3) Configure your Nexus to allow [anonymous access](https://help.sonatype.com/repomanager3/system-configuration/user-authentication/anonymous-access#) for browsing and downloading assets.

### [Prepare your GeneXus installation to publish assets](#Prepare+your+GeneXus+installation+to+publish+assets)

1) [Download Maven](https://maven.apache.org/download.cgi) and install it.

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

#### [3) Define a new server of module references in GeneXus as explained in the next section.](#3%29+Define+a+new+server+of+module+references+in+GeneXus+as+explained+in+the+next+section.)

### [Define a Matrix in GeneXus](#Define+a+Matrix+in+GeneXus)

To do so, go to the GeneXus Menu > Knowledge Manager> Manage Module References, then click on 'Add'

* Select Nexus in the Server Type
* Choose a name for your server (i.e.: Example Matrix).
* Choose the repository URL (i.e.: http://mymatrix.mycompany.com/repository/maven\_releases/).

`[imagen omitida: wiki id 45935]`

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
