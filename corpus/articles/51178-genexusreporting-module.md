---
title: "GeneXusReporting module"
source_id: 51178
source_url: https://wiki.genexus.com/commwiki/wiki?51178
genexus_version: "18"
---

# GeneXusReporting module

GeneXus provides a set of built-in [Domains](https://wiki.genexus.com/commwiki/wiki?7221) and [Structured data types](https://wiki.genexus.com/commwiki/wiki?10021) to interact with [QueryViewer](https://wiki.genexus.com/commwiki/wiki?9075) and [DashboardViewer](https://wiki.genexus.com/commwiki/wiki?36770) controls.

They are read-only and encapsulated in the GeneXusReporting module. You can find them under 'References' in the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210):

`[imagen omitida: wiki id 51180]`

In addition, you can find them in the 'Domains' tool window and in the 'Standard Variables' section.

The encapsulation of these objects in the module provides a set of benefits:

* It is clear to all the developers that these objects are maintained by GeneXus.
* Making them read-only prevents occasional errors and compatibility issues.
* Their implementation is already built and is also shipped built-in with GeneXus. So, GeneXus does not need to build (specify, generate, compile) them on every KB/Version/Environment.

The objects encapsulated in this module maintain the same GUID they had when the module didn't exist, so when installing this module the user will see these objects disappear from their old locations (QueryViewer and DashboardViewer folders under the Root module).

## [Install](#Install)

You may install the GeneXusReporting module from the [Manage Module References](https://wiki.genexus.com/commwiki/wiki?40172) dialog in the Knowledge Manager option (located in the GeneXus IDE toolbar).

Additionally, building a Knowledge Base created with a previous GeneXus version that already contained a QueryViewer or a DashboardViewer control will install the GeneXusReporting module automatically.

Finally, inserting either a QueryViewer or a DashboardViewer control in any form for the first time in a new Knowledge Base will also install this module.

## [Scope](#Scope)

**Generators:**[Java](https://wiki.genexus.com/commwiki/wiki?12258), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [.NET](https://wiki.genexus.com/commwiki/wiki?38604).

## [Troubleshooting](#Troubleshooting)

To restore a Knowledge Base to a prior state (that is, before the installation of the GeneXusReporting module) follow the steps below:

1. Open the Knowledge Base with a version of GeneXus prior to [GeneXus 17 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?49972,,).
2. Locate all the objects referencing the module, export them (so as not to lose them), and delete them.
3. Delete the GeneXusReporting module.
4. Using the Knowledge Manager, import the following files:
   * UserControls\QueryViewer\QueryViewerResources.xml
   * UserControls\DashboardViewer\DashboardViewerGxResources.xml.
5. Import the objects exported in step 2.

## [Availability](#Availability)

This feature is available since [GeneXus 17 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?49972,,).


|  |
| --- |
| **Backlinks** |
| [PivotTable Main color](https://wiki.genexus.com/commwiki/wiki?41081) | [Query Object Compatibility](https://wiki.genexus.com/commwiki/wiki?11032) | [Toc:Reporting in GeneXus](https://wiki.genexus.com/commwiki/wiki?25314) |
| [Total Experience with GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51570) |

---
