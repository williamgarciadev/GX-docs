---
title: "GeneXus for SAP Systems First Application (GeneXus 18 Upgrade 3 or prior)"
source_id: 54653
source_url: https://wiki.genexus.com/commwiki/wiki?54653
genexus_version: "18"
---

# GeneXus for SAP Systems First Application (GeneXus 18 Upgrade 3 or prior)

First, create a [New Knowledge Base](https://wiki.genexus.com/commwiki/wiki?9596) called "Travel Agency". In the back end box, select the following:

* **Prototyping Environment:** Java generator.
* **Data Source:** The default DBMS, which is SQL Server.

`[imagen omitida: wiki id 53393]`

Press the ‘Create’ button and GeneXus will start the Knowledge Base creation process.

`[imagen omitida: wiki id 53391]`

When the Knowledge Base has been created, you will see that the contents of the IDE have changed:

`[imagen omitida: wiki id 53392]`

* The [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210) now displays a tree structure, where all the defined objects will be shown.
* The Output window now displays a report of the actions performed and their results.

### [Initialize Fiori](#Initialize+Fiori+)

After the KB is created, in order to generate the UI using the Fiori Design system, you must initialize the resources for Fiori by selecting **Tools > Fiori > Initialize Fiori 3.0.**

This option will import all the needed resources to work with the pattern Fiori.
