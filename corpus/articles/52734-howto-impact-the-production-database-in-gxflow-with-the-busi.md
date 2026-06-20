---
title: "HowTo: Impact the production database in GXflow with the Business Process Deployer"
source_id: 52734
source_url: https://wiki.genexus.com/commwiki/wiki?52734
genexus_version: "18"
---

# HowTo: Impact the production database in GXflow with the Business Process Deployer

This article explains how to make an impact analysis on a production database using the [Business Process Deployer](https://wiki.genexus.com/commwiki/wiki?11607) tool.

### [Step 1](#Step+1)

Export your Business Process Diagrams from the [IDE](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?5587,,) by selecting **Tools > Workflow > [Create business process deploy file](https://wiki.genexus.com/commwiki/wiki?18244).**

`[imagen omitida: wiki id 50967]`

Note: In case you are using a DBMS whose driver is not distributed by GeneXus, and it is necessary to execute reorganizations to update the database structure, you need to copy the driver into the reorganization folders inside the .bpd file. These folders are located within the 'Reorgs' folder inside the .bpd. To do this, you can open the .bpd file using WinRAR or 7-Zip.

### [Step 2](#Step+2)

Once the diagrams have been exported, run the *Business Process Deployer. T*o do so, go to **Start > Programs > GXflowX > Business Process Deployer** and the following sequence of wizards will appear.

### [Step 3](#Step+3)

In the first one, select the deployment file created in Step 1.

`[imagen omitida: wiki id 50968]`

### [Step 4](#Step+4)

Next, set your deployment preferences.

`[imagen omitida: wiki id 33806]`

* **Create new version of business processes:** A new version of the business processes is created. This option is recommended to avoid changing the flow of active processes that are running with a previous version of the business processes.
* **Automatically detect and execute needed reorganizations:** The version in the database will be automatically detected and all the needed reorganizations will be executed.
* **Force workflow tables creation:** When you force the creation of workflow tables, the tables will be overwritten and no reorganizations will be done. All the processes that are running will be lost, so it is not advisable if you are in a production state. Also, if your licenses are local, they will be lost. Therefore, it is recommended to uninstall them first, then create the tables, and finally request them again.
* **Execute needed reorganizations assuming a specific current workflow runtime version:** You must select the current version in the database and all the needed reorganizations will be executed.

### [Step 5](#Step+5)

This step will vary depending on the environment you are using. If your deployment file is for a *Java environment*, an *Execution* section will be displayed and, in the *additional classpath* field, you must indicate at least the \*.jar file of JTDS (located in *<GeneXus installation>\gxjava\drivers*). If your application uses other external Java resources, you must include them too. When your file is for a *.NET Framework or .NET Environment*, the *Execution* section is not displayed and a "Use Windows NT integrated security" option is available to authenticate to the database.

`[imagen omitida: wiki id 50969]`

* Below is an example of a classpath you might need: C:\KBs\<KBName>\JavaSQLServer\Web\dependencies\bcprov-jdk18on-1.75.jar;C:\KBs\<KBName>\JavaSQLServer\Web\dependencies\bcutil-jdk18on-1.75.jar;C:\KBs\<KBName>\JavaSQLServer\Web\dependencies\commons-collections4-4.4.jar;C:\KBs\<KBName>\JavaSQLServer\Web\dependencies\commons-io-2.11.0.jar;C:\KBs\<KBName>\JavaSQLServer\Web\dependencies\commons-lang-2.6.jar;C:\KBs\<KBName>\JavaSQLServer\Web\dependencies\GeneXus.jar;C:\KBs\<KBName>\JavaSQLServer\Web\dependencies\gxclassR-4.4.0.jar;C:\KBs\<KBName>\JavaSQLServer\Web\dependencies\gxcommon-4.4.0.jar;C:\KBs\<KBName>\JavaSQLServer\Web\dependencies\gxwrappercommon-4.4.0.jar;C:\KBs\<KBName>\JavaSQLServer\Web\dependencies\gxwrapperjavax-4.4.0.jar;C:\KBs\<KBName>\JavaSQLServer\Web\dependencies\jtds-1.2.jar;C:\KBs\<KBName>\JavaSQLServer\Web\dependencies\log4j-api-2.21.1.jar;C:\KBs\<KBName>\JavaSQLServer\Web\dependencies\log4j-core-2.21.1.jar;C:\KBs\<KBName>\JavaSQLServer\Web\dependencies\mssql-jdbc-10.2.0.jre8.jar;C:\KBs\<KBName>\JavaSQLServer\Web\dependencies\xercesImpl-2.12.2.jar;C:\KBs\<KBName>\JavaSQLServer\Web\build\libs\wfcache.jar;

### [Step 6](#Step+6)

Finally, click on the *Deploy* button to start the deployment process.

`[imagen omitida: wiki id 32293]`

`[imagen omitida: wiki id 33808]`

### [See Also](#See+Also)

[HowTo: Deploy a Workflow-based Application](https://wiki.genexus.com/commwiki/wiki?19848)  
[Business Process Deployer Command line](https://wiki.genexus.com/commwiki/wiki?27496)  
[HowTo: Enable Log for GXflow BPDeployer](https://wiki.genexus.com/commwiki/wiki?51046)


|  |
| --- |
| **Backlinks** |
| [Business Process Deployer](https://wiki.genexus.com/commwiki/wiki?11607) | [Table of contents:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [HowTo: Deploy a Workflow-based Application](https://wiki.genexus.com/commwiki/wiki?19848) |

---
