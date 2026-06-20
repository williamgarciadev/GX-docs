---
title: "DesignOps - Sample - Travel Agency web back-office"
source_id: 47052
source_url: https://wiki.genexus.com/commwiki/wiki?47052
genexus_version: "18"
---

# DesignOps - Sample - Travel Agency web back-office

This article refers to a design file for a Travel Agency web back office made with the [Sketch design tool](https://www.sketch.com/) and exported by [GxDesignOps plugin](https://wiki.genexus.com/commwiki/wiki?46875) in .gxsketch format.

## [Sample download](#Sample+download)

`[imagen omitida: wiki id 40856]` [Travel Agency Web Backoffice.gxsketch](https://wiki.genexus.com/commwiki/wiki?49397,,)

## [Importing gxsketch file](#Importing+gxsketch+file)

Basically, you must follow the instructions described in the [Design Import option](https://wiki.genexus.com/commwiki/wiki?46882) article.

Once you select the .gxsketch file from your filesystem, the Sketch to GeneXus dialog will be shown as follows:

`[imagen omitida: wiki id 47057]`

**Warning**: Remember that this Sketch file was designed for a Web environment, so do not forget to check the "Import as Web Panels" option; otherwise, the design may not look as expected for a native mobile application.

When you are sure you want to import the design file, just click on the "OK" button and the Output dialog (General tab) will show you the import progress.

`[imagen omitida: wiki id 47058]`

Once it has finished importing, check the generated panels and how they look. Also, check the theme-classes, image objects, and file objects (fonts) imported.

`[imagen omitida: wiki id 47059]`

As you may notice, there are some changes that you must do before running your application.

**Warning**: Do not expect it to be perfect. It is highly probable that you or your designer must fix something in the design file or the abstract layout or theme-class.

## [Applying manual changes](#Applying+manual+changes)

First of all, none of the generated panels have the [Main program property](https://wiki.genexus.com/commwiki/wiki?7407) set. Even if you set it for ViewCountryDetail object, you will find that your application does not include a Master Page even when the design file includes an Artboard for it.

|  |
| --- |
|  |

**Note**: GeneXus, in future releases, will try to provide mechanisms for automating every process described in this section in order to minimize manual changes.

This section aims to guide you on how you can identify which changes must be applied before running this sample.

1. The ViewMasterPage object, instead of being a web panel object, should be a [Web Master Panel object](https://wiki.genexus.com/commwiki/wiki?10348). The Import Sketch option does not support this kind of declarations yet.  
   So, you must change it manually by setting the [Type Property](https://wiki.genexus.com/commwiki/wiki?43861) as 'Master Page'.  
   `[imagen omitida: wiki id 47064]`
2. After changing the [Type Property](https://wiki.genexus.com/commwiki/wiki?43861) of ViewMasterPage object, note that GeneXus does not allow you to save the object and shows the following message:  
   **error**: One Content Placeholder control is needed in master pages  
     
   The reason is that the Web Master Panel object does not contain a Content Placeholder control. You must add it manually because Sketch Import does not recognize the corresponding Artboard as a Master Page in the first place (as it was mentioned in bullet 1).  
     
   The Content Placeholder control must be added in the third row of the Master Page layout. After adding it, save the object settings.  
   `[imagen omitida: wiki id 47065]`
3. The ViewCountryDetail web panel, by default, will have the [Master Page property](https://wiki.genexus.com/commwiki/wiki?8156) with "(none)" value. As you have defined the ViewMasterPage object as a [Web Master Panel object](https://wiki.genexus.com/commwiki/wiki?10348), you must change that property to this value.  
   `[imagen omitida: wiki id 47066]`
4. By default, the [Theme object](https://wiki.genexus.com/commwiki/wiki?16595) is set as Carmine, but the design was imported with a new Theme object named 'Travel\_Agency\_Back\_office' (although you could select Carmine object to merge it with). The Import Sketch option does not change the [Theme property](https://wiki.genexus.com/commwiki/wiki?8145) for the generated [Web Panel objects](https://wiki.genexus.com/commwiki/wiki?6916), so you must set them manually.  
   `[imagen omitida: wiki id 47067]`
5. Finally, set as True the [Main program property](https://wiki.genexus.com/commwiki/wiki?7407) of the ViewCountryDetail web panel in order to run the application.  
   `[imagen omitida: wiki id 47068]`

Despite these changes, think about how much time you would have to spend trying to design those panels, with their theme-classes, fonts, and colors.

Definitively, you have saved a lot!

## [Runtime execution](#Runtime+execution)

After applying the changes described in the previous section, and running the ViewCountryDetail web panel, you will have the following result.

|  |  |  |  |
| --- | --- | --- | --- |
| **Designer** | | **Developer** | |
| **Sketch** | **Artboard** | **GeneXus** | **Browser** |
| *Master Page* |  | *ViewCountryDetail*  **Master Page:** *ViewMasterPage* |  |
| *Country Detail* |  |

It looks great, doesn't it? And the only things you did were import the .gxsketch file and make a few changes.

## [Notes](#Notes)

* **IMPORTANT**  
  For GeneXus versions prior to build 149009, when you download the .gxsketch file, ensure it has this name before import: *Travel Agency - Back office.gxsketch*. Otherwise, several images will be imported as placeholders (blank images).

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators** | .NET, .NET Core, Java, Angular |

## [See also](#See+also)

* [Guide for designers](https://wiki.genexus.com/commwiki/wiki?46871)
* [Guide for developers](https://wiki.genexus.com/commwiki/wiki?46877)

## [Availability](#Availability)

This sample has been made for [GeneXus 17](https://wiki.genexus.com/commwiki/wiki?46873,,).


|  |
| --- |
| **Backlinks** |
| [Toc:DesignOps and GeneXus](https://wiki.genexus.com/commwiki/wiki?46870) | [Toc:GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066) | [GeneXus 18 Samples](https://wiki.genexus.com/commwiki/wiki?52693) |

---
