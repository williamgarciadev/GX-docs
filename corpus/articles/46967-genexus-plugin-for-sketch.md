---
title: "GeneXus Plugin for Sketch"
source_id: 46967
source_url: https://wiki.genexus.com/commwiki/wiki?46967
genexus_version: "18"
---

# GeneXus Plugin for Sketch

**Deprecated**: Since June 2022. Out of maintenance.

A plugin for [Sketch tool](https://www.sketch.com/) to simplify the exchange of Sketch assets and design between designers and developers,

## [Installation](#Installation)

1. Download the latest version of the plugin from [Github: SketchDesignOps](https://github.com/genexuslabs/sketchdesignops/releases) on your Mac.
2. Double-click on the .sketchplugin file.

### [Configure Export Options](#Configure+Export+Options)

To start sharing with developers, the designer must configure the way of sharing. At this moment there are two options:  
1) A shared folder.  
2) An AWS S3 bucket.

The designer can configure the export options by executing Plugins > GxDesignOps > Configuration inside Sketch.

`[imagen omitida: wiki id 46973]`

|  |  |
| --- | --- |
| **Name** | **Description** |
| **Send Preview for Pages** | For each artboard on each page, send an embedded screenshot. For big Sketch files, this can take time and increase the .gxsketch file size. |
| **Send fonts used.** | This option allows you to send the used fonts embedded.  Take into account that probably the first designs you want to send will always be the fonts, but once you know for sure that developers already have the necessary fonts you can avoid sending them embedded every time. |
| **Enable S3 Sharing** | AWS S3 is going to be used as the mechanism to send designs to developers. |
| **Queue Path** | A shared folder is used to send the design to the developers. The queue path must end on / |

### [Exporting by using the Plugin](#Exporting+by+using+the+Plugin)

After the plugin has been configured, the designer has 2 options to share the design:

1) Send the GeneXus format to the design queue (.gxsketch).  
Go to Plugins > GxDesignOps > Send GeneXus Format option.

2) Send only the Sketch file (.sketch) -- faster but incomplete information, no images, previews, or fonts are included.  
Go to Plugins > GxDesignOps > Send only Sketch File option.

Any option will show a dialog to confirm the copy.

`[imagen omitida: wiki id 46974]`

The result is shown in the dialog itself.

`[imagen omitida: wiki id 46976]`

## [See also](#See+also)

[Export from Sketch](https://wiki.genexus.com/commwiki/wiki?46875)


|  |
| --- |
| **Backlinks** |
| [DesignOps - Export design - Sketch](https://wiki.genexus.com/commwiki/wiki?46875) | [Table of contents:DesignOps and GeneXus](https://wiki.genexus.com/commwiki/wiki?46870) |

---
