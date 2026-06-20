---
title: "Design Import option (GeneXus 18 Upgrade 4 or prior)"
source_id: 55439
source_url: https://wiki.genexus.com/commwiki/wiki?55439
genexus_version: "18"
---

# Design Import option (GeneXus 18 Upgrade 4 or prior)

The **Design Import** option allows you to create [GeneXus objects](https://wiki.genexus.com/commwiki/wiki?1866) from a user interface design made with a designer tool (e.g. [Sketch design toolkit](https://www.sketch.com/) or [Figma design toolkit](https://www.figma.com)). In order to achieve a good result, the designer must follow a set of [designer rules](https://wiki.genexus.com/commwiki/wiki?46871).

## [Start the Design Import](#Start+the+Design+Import)

From the GeneXus toolbar, go to: **Tools > Application Integration > Design Import**

`[imagen omitida: wiki id 50558]`

## [Design to GeneXus initial dialog](#Design+to+GeneXus+initial+dialog)

Once the dialog is open, you will see the following options.  
`[imagen omitida: wiki id 51760]`

### [1. File](#1.+File)

It allows you to select your design file by indicating a file path or a file URL.

|  |  |
| --- | --- |
| **Notes** | |
| **1)** | File path must have any of these extensions: .sketch, .gxsketch, .sketchcloud, .gxsketchcloud.  Also, the file path can be indicated by browsing your file system using the  button. |
| **2)** | File URL must reference any of these domains: www.figma.com/file/\*.  Also, the file URL could reference a publicly accessible file and must force the download once clicking on it (e.g. https://files.genexus.com/pub/TravelAgencySample.gxsketch). For more information, please refer to [FAQ and Troubleshooting section](https://wiki.genexus.com/commwiki/wiki?46880). |

### [2. Style](#2.+Style)

By default, once you select a design file, it will suggest you create a new [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375) based on the file name you want to import. However, you can choose another new name or even select one of your current Design System objects in order to override the style-classes inferred from the design.

### [3. Import as Web Panels](#3.+Import+as+Web+Panels)

Check it if you want to import your design as Web Panels; otherwise, GeneXus will import them as Panels (Mobile or Angular). If you import your design as mobile panels, it will also create a Menu object that you can use for navigating into every imported panel. Take into account that importing a design file for mobile as Web Panels (or vice versa) may lead to an unexpected user interface.

### [4. Load option](#4.+Load+option)

This option will load a preview of the design file, and while it is loading it will display the inspection progress.  
`[imagen omitida: wiki id 51757]`

## [Design to GeneXus preview dialog](#Design+to+GeneXus+preview+dialog)

After you load a design file, GeneXus will show you a preview of what it is going to import. The dialog displays the information in two sections: on the left side, a tree structure of objects to be imported, and on the right side, it will load contextual information of what you select. Also, you can check (or uncheck) those objects that you want to import (or not) into your Knowledge Base.

`[imagen omitida: wiki id 51758]`

### [1. Panels](#1.+Panels)

For a Panel node, the dialog will display two tabs.

#### Composition tab

Shows you a preview of the panel (when it is available) and a tree structure with every control in the layout.

#### Code tab

Shows an XML representation for the target panel. The document always starts with an opening <Root> tag which is preceded by top-level tags for defining:

|  |  |
| --- | --- |
| <Controls> | Describes the Layout definition by using the [GeneXus Markup Language (GXML)](https://wiki.genexus.com/commwiki/wiki?46876) format. |
| <Variables> | Describes the set of Variable definitions. |
| <Code> | Describe the code for every [User defined event](https://wiki.genexus.com/commwiki/wiki?8044) inferred from the design as a raw string. |
| <SDTs> | Describes the set of [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021) definition in case there are variables based on them. |
| <DataProviders> | Describes the set of [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) definitions in case there are SDTs defined and populated with data. |
| **NOTE:** Every Structured Data Type and Data Provider object will be created under a folder in your Knowledge Base. | |

### [2. Stencils](#2.+Stencils)

Similar to a Panel node. These objects will be created under a "Stencil" folder in your Knowledge Base.

### [3. Images](#3.+Images)

For an Image node, the dialog will display a preview of the image to be imported in the Composition tab.

### [4. Design System](#4.+Design+System)

The Design System node will display every token/style to be imported. Both tokens and styles will be rendered in their own tab with the proper syntax.

## [Import your design](#Import+your+design)

Once you decide to import the design into your Knowledge Base, you simply click on the "OK" button and you can see the import progress on the Output Window (General view).

`[imagen omitida: wiki id 46901]`

After the importing process has finished, you will see the new objects in the KB Explorer.

`[imagen omitida: wiki id 49610]`

The Design System object will have a set of classes prefixed with "ExternalDesign" where every new theme-class inferred from the design file will inherit. Also, if custom Fonts were added, GeneXus will create its corresponding File object in the Knowledge Base, create the appropriate [@font-face rule](https://wiki.genexus.com/commwiki/wiki?49338) in the DesignSystem object, and set that font-face in the appropriate [Style Class](https://wiki.genexus.com/commwiki/wiki?49309).

Since [GeneXus 17 Upgrade 9](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?49956,,), the design file is saved in the KB as a [File object](https://wiki.genexus.com/commwiki/wiki?5852). Notice that the name of the file has the suffix "+backup":

`[imagen omitida: wiki id 50543]`

If the file exists, it is overwritten allowing you to check/recover versions from the History, and to do a "Save content as..." if you want to dump the file to the filesystem.

## [Notes](#Notes)

* When importing from Figma for the first time, it will ask you for the [Figma Token](https://www.figma.com/developers/api#access-tokens) that can access that file. If you do not have a Figma account or you do not have access to the Figma File, please ask your designer to get it.

  |  |
  | --- |
  |  |

    
  Also, you can change the Figma Token at any time if it is required (e.g. for new design files) and you can click on the "Access Token" label in order to learn how to get a new token.

## [See Also](#See+Also)

[Guide for designers](https://wiki.genexus.com/commwiki/wiki?46871)  
[Guide for developers](https://wiki.genexus.com/commwiki/wiki?46877)  
[GeneXus Markup Language (GXML)](https://wiki.genexus.com/commwiki/wiki?46876)  
[Export design](https://wiki.genexus.com/commwiki/wiki?46875)
