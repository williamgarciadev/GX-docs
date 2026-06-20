---
title: "DesignOps - Export design - Sketch"
source_id: 46875
source_url: https://wiki.genexus.com/commwiki/wiki?46875
genexus_version: "18"
---

# DesignOps - Export design - Sketch

Designers can send designs made in [Sketch format](https://www.sketch.com/) to developers. Then, developers can import these designs using the [Design Import option](https://wiki.genexus.com/commwiki/wiki?46882) in the [GeneXus IDE](https://wiki.genexus.com/commwiki/wiki?5272).

The designer can send what is necessary to the developers using traditional mechanisms (email, shared resource, etc.), or they can also install the [GeneXus Plugin for Sketch](https://github.com/genexuslabs/sketchdesignops), which allows you to send the designs.

## [How to send a Sketch design manually](#How+to+send+a+Sketch+design+manually)

When a designer sends a design it should include the .sketch file (the design), including images and fonts in separate folders. These files are usually sent separately.

The developer needs to store the .sketch file in a folder that also includes every image under a folder named exactly the same as the .sketch file and suffixed with "Image". The same process must be applied to fonts with a folder suffixed with "Fonts."

For instance, if you save your design as MyFirstDesign.sketch, then every image must be shared with the developer in a directory named /MyFirstDesignImages and every font in a directory named /MyFirstDesignFonts.

```
/Designs
   MyFirstDesign.sketch
   /MyFirstDesignImages
      Image1.png
      Image1@2x.png
      Image1@3x.png
      ... // All exported images, in general by using the export tool of Sketch
   /MyFirstDesignFonts
      Font1.ttf
      Font2.ttf
      ... // All used fonts
```

Now the developer can import the .sketch file into GeneXus (located in the directory where the images and fonts folders are placed) using the [Design Import option](https://wiki.genexus.com/commwiki/wiki?46882).

## [How to send a Sketch design by using GeneXus Plugin for Sketch](#How+to+send+a+Sketch+design+by+using+GeneXus+Plugin+for+Sketch)

Instead of sending all this information in separate structures, GeneXus created a .gxsketch format to avoid missing some pieces of information when the designer sends information from Sketch to GeneXus.

The .gxsketch format is quite simple; it is just a zip file with the Sketch file, plus images, fonts, and screenshots for each artboard in the Sketch file. You can explore the content with any zip client like 7Zip, WinZip, WinRar, etc.

So, the contents are as follows:

|  |  |  |
| --- | --- | --- |
| **Sketch** | *filename*.sketch file | The design (Artboards, Symbols, etc.) |
| **Images** | *filename*Images folder | The images used by the designer. Remember to mark as exportable the images that you want to be imported in GeneXus. |
| **Fonts** | *filename*Fonts folder | The fonts used by styles in the Sketch file. |
| **Screenshots** | gx-preview folder | One image per artboard. Used by Sketch Inspector in the IDE to preview the design to developers. |

Now you can share your .gxsketch file with a developer who can use the [Design Import option](https://wiki.genexus.com/commwiki/wiki?46882) for importing it into GeneXus.

### [Installing GeneXus Plugin for Sketch](#Installing+GeneXus+Plugin+for+Sketch)

Refer to [GeneXus Plugin for Sketch](https://wiki.genexus.com/commwiki/wiki?46967).

## [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

## [See also](#See+also)

[Guide for designers](https://wiki.genexus.com/commwiki/wiki?46871)  
[Design Import option](https://wiki.genexus.com/commwiki/wiki?46882)  
[Required configuration for Amazon S3 bucket](https://wiki.genexus.com/commwiki/wiki?54610)


|  |
| --- |
| **Backlinks** |
| [Design Import option](https://wiki.genexus.com/commwiki/wiki?46882) | [Design Import option (GeneXus 18 Upgrade 4)](https://wiki.genexus.com/commwiki/wiki?55439) | [DesignOps - FAQ and Troubleshooting](https://wiki.genexus.com/commwiki/wiki?46880) |
| [DesignOps - Other samples](https://wiki.genexus.com/commwiki/wiki?47103) | [DesignOps - Sample - Travel Agency mobile front-end](https://wiki.genexus.com/commwiki/wiki?47029) | [DesignOps - Sample - Travel Agency web back-office](https://wiki.genexus.com/commwiki/wiki?47052) | [DesignOps - Sample - Travel Agency web front-end](https://wiki.genexus.com/commwiki/wiki?49441) |
| [Toc:DesignOps and GeneXus](https://wiki.genexus.com/commwiki/wiki?46870) | [GeneXus Plugin for Sketch](https://wiki.genexus.com/commwiki/wiki?46967) |

---
