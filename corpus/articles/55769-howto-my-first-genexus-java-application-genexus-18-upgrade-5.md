---
title: "HowTo: My first GeneXus Java Application (GeneXus 18 Upgrade 5 or prior)"
source_id: 55769
source_url: https://wiki.genexus.com/commwiki/wiki?55769
genexus_version: "18"
---

# HowTo: My first GeneXus Java Application (GeneXus 18 Upgrade 5 or prior)

To generate your GeneXus application in Java, the following is required:

* Oracle JDK or Open JDK 1.8 or higher
* Apache Tomcat (7.0.67 or higher) installed from setup

Below are the steps to follow:

**Step 1:** Create a new [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) and in the Prototyping Environment Combo Box select: **Java Environment**.

`[imagen omitida: wiki id 53981]`

**Step 2:** Create a new [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) (Company).

`[imagen omitida: wiki id 53982]`

**Step 3:**Be sure to configure the [Tomcat path property](https://wiki.genexus.com/commwiki/wiki?48354) and [Tomcat version property](https://wiki.genexus.com/commwiki/wiki?48352). Also make sure that your Tomcat is running.

`[imagen omitida: wiki id 54711]`

**Step 4:** Press F5 or select **Build > Run Developer Menu**.

`[imagen omitida: wiki id 53983]`

**Step 5:** Set the Database information properties and press the Finish button.

`[imagen omitida: wiki id 45879]`

**Step 6:** GeneXus will start the [Build process](https://wiki.genexus.com/commwiki/wiki?5692) and show an [Impact Analysis](https://wiki.genexus.com/commwiki/wiki?31023). Press Create.

`[imagen omitida: wiki id 53984]`

The generated application will be displayed in the [Launchpad Tool Window](https://wiki.genexus.com/commwiki/wiki?52315).

`[imagen omitida: wiki id 53985]`

`[imagen omitida: wiki id 53986]`

## [Considerations](#Considerations)

* To install Tomcat, using a setup file is recommended instead of a zip file. Otherwise, you must [change Windows Registry values for Tomcat](https://wiki.genexus.com/commwiki/wiki?21926).

`[imagen omitida: wiki id 45883]`

* Both [Servlet directory property](https://wiki.genexus.com/commwiki/wiki?9122) and [Static content directory seen from client property](https://wiki.genexus.com/commwiki/wiki?9124) depend on Windows registry values for Tomcat.

## [See Also](#See+Also)

[Manually configuring Tomcat](https://wiki.genexus.com/commwiki/wiki?21382)  
[GeneXus 18 hardware and software requirements](https://wiki.genexus.com/commwiki/wiki?30900)  
[SAC #31319: Consequences of setting Servlet Directory property with a non-Default value](https://www.genexus.com/es/developers/websac?data=31319)
