---
title: "GeneXus for SAP Systems Fiori for Web Pattern - HowTo: Apply a List Floorplan to a Web Panel"
source_id: 42011
source_url: https://wiki.genexus.com/commwiki/wiki?42011
genexus_version: "18"
---

# GeneXus for SAP Systems Fiori for Web Pattern - HowTo: Apply a List Floorplan to a Web Panel

In addition to applying a Floorplan to a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908), you can also apply a Floorplan to a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916).

If you have never applied the Fiori pattern to your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836), read [HowTo: Apply the Fiori for Web pattern for the first time](https://wiki.genexus.com/commwiki/wiki?38862). Otherwise, while being positioned on the Patterns tab of a Web Panel, click the Select floorplan... link:

`[imagen omitida: wiki id 42015]`

It will open a new window with a list of floorplans to select one. Select one of the floorplans offered under the List floorplans node:

`[imagen omitida: wiki id 42016]`

Once selected, it will pop up a new window showing the four different options to base the floorplan on:

1. Based on a Transaction
   * This will create only the list using the attributes of the Transaction as columns.
2. Based on a [Structured Data Type (SDT)](https://wiki.genexus.com/commwiki/wiki?10021).
   * This will create the list using the first level of the SDT as columns.
3. Variables based on Attributes or Domains
   * This will create the list using the variables as columns.
4. Use custom variables
   * This will create the list using the variables as columns.

`[imagen omitida: wiki id 42017]`

After selecting one of these options, it will create **only** the list floorplan; you will need to create all the objects/code necessary to develop the logic of the Web Panel.


|  |
| --- |
| **Backlinks** |
| [GeneXus For SAP Systems - KPI Worklist Floorplan](https://wiki.genexus.com/commwiki/wiki?38645) | [GeneXus For SAP Systems - List Report Floorplan](https://wiki.genexus.com/commwiki/wiki?38572) | [GeneXus For SAP Systems - Simple Worklist Floorplan](https://wiki.genexus.com/commwiki/wiki?38636) |
| [GeneXus For SAP Systems - Simple Worklist with global action Floorplan](https://wiki.genexus.com/commwiki/wiki?38796) | [GeneXus For SAP Systems KPI Worklist Floorplan (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54915) | [GeneXus For SAP Systems List Report Floorplan (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54853) | [GeneXus For SAP Systems Simple Worklist Floorplan (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54970) |
| [GeneXus For SAP Systems Simple Worklist with global action Floorplan (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55017) |

---
