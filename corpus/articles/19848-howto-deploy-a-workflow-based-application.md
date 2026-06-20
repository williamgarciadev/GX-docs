---
title: "HowTo: Deploy a Workflow-based Application"
source_id: 19848
source_url: https://wiki.genexus.com/commwiki/wiki?19848
genexus_version: "18"
---

# HowTo: Deploy a Workflow-based Application

This article shows you the steps to deploy a Workflow-based application.

Just as any other GeneXus application, it needs to be deployed from the [IDE](https://wiki.genexus.com/commwiki/wiki?5587,,) and then export the set of Business Process Diagrams.

The complete process consists of three components: the binary files, the database/metadata, and the protection.

### [Deploy binary application files](#Deploy+binary+application+files)

GeneXus provides a simple mechanism to package the generated files and deploy the application.

1. Go to**[Build](https://wiki.genexus.com/commwiki/wiki?5690) > [Deploy application](https://wiki.genexus.com/commwiki/wiki?32092)** on the toolbar. This action will display a contextual window in the main section of the IDE.
2. Drag every [Business Process Diagram](https://wiki.genexus.com/commwiki/wiki?16486) from the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210) and drop them inside the "objects to deploy" form. You also need to include a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) with the property [Main program](https://wiki.genexus.com/commwiki/wiki?7407) set in True.  
   It is not necessary to include every dependency of the Business Process Diagram (such as Web Panel, [Procedures](https://wiki.genexus.com/commwiki/wiki?6293), etc.), GeneXus will include them on the package without showing them on the dialog.  
   `[imagen omitida: wiki id 52736]`
3. Set your preferred options and deploy it.  
   Refer to [this](https://wiki.genexus.com/commwiki/wiki?32092) document for detailed information.

**Note**: If you don't want to include the GXflow backoffice you can use the [Include GXflow backoffice property](https://wiki.genexus.com/commwiki/wiki?49569).

### [Update application database and metadata files](#Update+application+database+and+metadata+files)

GeneXus's [Business Process Deployer](https://wiki.genexus.com/commwiki/wiki?11607) tool makes it possible to impact the production database with the new workflow processes or with the changes made to the existing ones.

1. Go to **[Tools menu](https://wiki.genexus.com/commwiki/wiki?7575) > [Workflow](https://wiki.genexus.com/commwiki/wiki?17111) > [Create business process deploy file](https://wiki.genexus.com/commwiki/wiki?18244)** to export the [BPDiagrams](https://wiki.genexus.com/commwiki/wiki?16486).
2. Open the [BPDeployer](https://wiki.genexus.com/commwiki/wiki?11607) and import the generated file.  
   Refer to [HowTo: Impact the production database in GXflow with the Business Process Deployer](https://wiki.genexus.com/commwiki/wiki?52734) document for detailed information.  
   `[imagen omitida: wiki id 33611]`

In the production environment, workflow processes are always impacted by new processes. This fact means that the process instances that were still running will be based on the definition of the process previous to the impact. In other words, the changes made in the impact won't take effect on the running processes, only processes created after the impact is made will have the new definition.

### [Establish a connection to the new database](#Establish+a+connection+to+the+new+database)

Once the application has been deployed and impacted the production database with the Business Process Deployer, it is necessary to update the configuration files of the application to connect it to the production database.  
These files depend on the generator used:

* For  [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892) you have to update at least the following fields in the web.confige file:

```
<add key="Connection-Default-User" value="databaseUser" />
<add key="Connection-Default-Password" value="UserPassword" />
<add key="Connection-Default-DB" value="databaseName" />
<add key="Connection-Default-Schema" value="databaseSchema" />
```

* For [.NET](https://wiki.genexus.com/commwiki/wiki?38604) you have to update at least the following fields in the appsettings.json file:

```
"Connection-Default-User": "databaseUser",
"Connection-Default-Password": "UserPassword",
"Connection-Default-DB": "databaseName",
"Connection-Default-Schema": "databaseSchema",
```

* For [Java](https://wiki.genexus.com/commwiki/wiki?12258) you have to update at least the following fields in the client.cfg file:

```
CS_SCHEMA=databaseSchema
USER_ID=databaseUser
USER_PASSWORD=UserPassword
CS_DBNAME=databaseName
DB_URL=databaseURL
```

If you need to encrypt these data, you can use the [GxEncryptCMD](https://wiki.genexus.com/commwiki/wiki?45615) tool. The key needed to encrypt is located in the application.key file if you are generating with Java and in the KeyResolver.dll file if you choose .Net.

### [Protection settings](#Protection+settings)

When the application is ready to be deployed on a server, the protection must be updated with it.

### [GeneXus 15 Upgrade 8 or higher](#GeneXus+15+Upgrade+8+or+higher)

Since the introduction of the [new GXflow license scheme](https://wiki.genexus.com/commwiki/wiki?37204) in GeneXus 15 Upgrade 8, the license setup becomes a very simple task. Use the [GXflow license manager](https://wiki.genexus.com/commwiki/wiki?37207) to install the licenses. The process is the same for any platform.

### [GeneXus 15 Upgrade 7 or lower](#GeneXus+15+Upgrade+7+or+lower)

The instructions to achieve the licenses set up depend on the platform that will be executed.

#### [Windows platform](#Windows+platform)

1. Install [Business Process Deployer Setup](https://wiki.genexus.com/commwiki/wiki?19849).
2. Go to **Start > All Programs > GXflow GeneXus 15 > License Manager** and [install licenses](http://www.gxtechnical.com/gxdlsp/pub/iehelp.htm?utilities/genexus_protection_server/manual/30/proteccion.htm).
3. Copy the "protect.ini" file that resides in *C:\Program Files (x86)\GeneXus\GXflow\GXflowGx15\LicMgr* to: "C:\Windows\System32" folder and "C:\Windows\SysWOW64"  folder.
4. Install [GeneXus Protection Server](https://wiki.genexus.com/commwiki/wiki?18887,,).
5. (Only for Java) Copy and extract [this](https://www.genexus.com/developers/DownloadCenter?S,,,3637;;) file to the Tomcat´s lib directory (by default in *C:\Program Files\Apache Software Foundation\Tomcat X.Y\lib*).
6. Go to **Start > All Programs > GeneXus 15 Business Process Deployer** and deploy the processes.
7. Refer to [this](https://wiki.genexus.com/commwiki/wiki?11607) document for the instructions.

#### Linux platform

Follow these steps: [HowTo: Configuring Protection for GXflow Installed on Linux, AIX and OS400](https://wiki.genexus.com/commwiki/wiki?15724,,) to install the licenses on the same server as the application.  
Or please follow these steps: [GXflow centralized licenses configuration (GXflow on Linux)](https://wiki.genexus.com/commwiki/wiki?21728) when the licenses will be installed on a remote server (if the licenses are installed remotely, the server must be Windows).

#### [IBM iSeries (AS400) platform](#IBM+iSeries+%28AS400%29+platform)

Follow these steps: [HowTo: Configuring Protection for GXflow Installed on Linux, AIX and OS400](https://wiki.genexus.com/commwiki/wiki?15724,,) to install the licenses when it will be installed on the same server as the application at an AS400 server.


|  |
| --- |
| **Backlinks** |
| [Toc:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Toc:Application Deployment tool (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54334) | [Business Process Deployer](https://wiki.genexus.com/commwiki/wiki?11607) |
| [Business Process Deployer Command line](https://wiki.genexus.com/commwiki/wiki?27496) | [Create business process deploy file](https://wiki.genexus.com/commwiki/wiki?18244) |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [HowTo: Impact the production database in GXflow with the Business Process Deployer](https://wiki.genexus.com/commwiki/wiki?52734) |

---
