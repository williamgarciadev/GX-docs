---
title: "Using Custom Fonts"
source_id: 22781
source_url: https://wiki.genexus.com/commwiki/wiki?22781
genexus_version: "18"
---

# Using Custom Fonts

Many times in different applications you need to use custom Fonts. This article explains how to use them through the [Theme object](https://wiki.genexus.com/commwiki/wiki?16595).

## [Font node](#Font+node)

On the [Theme object](https://wiki.genexus.com/commwiki/wiki?16595), there is a **Fonts** node where you can incorporate custom text fonts associated with the application, that behaves the same way as [Web Fonts](https://wiki.genexus.com/commwiki/wiki?22701). This works analogously as [Transformations](https://wiki.genexus.com/commwiki/wiki?23694), giving you the ability to:

* Add new fonts by *right-clicking > Add Font* option.
* Reference them from the *Font Family* property (under *Font* properties group on Theme Classes that admit it).

|  |  |  |
| --- | --- | --- |
| **Property** | **Values** | **Description** |
| **Name** | String | Name of the font which will be referenced by theme classes. |
| **File** | Font filename | Name of the TTF file imported in the Knowledge Base. |

**Note**: The other properties (Style, Stretch, Weight, and Unicode) do not apply to Native Mobile generators because they are based on CSS style tags. On the Native Mobile generators, these customizations can be made through theme class properties.

## [Usage example](#Usage+example)

Imagine a simple panel with a “start!” button. The objective is to customize its appearance by changing its font.

`[imagen omitida: wiki id 32712]`

In order to achieve this, the following steps must be followed:

**1)** Get the font that you want and make sure that the extension is compatible with the platform.

**2)** Open the Theme object and look for the Font node. Right-click on it and chose the *Add Font* option.

`[imagen omitida: wiki id 35722]`

**3)** This action will display a dialog to import the font's source file (in this case, a TTF file called *Gameplay*).

`[imagen omitida: wiki id 35723]`

**4)**Once the font is imported, select it from the dialog and click the “ok” button. After this action, the new font will be displayed under the Font node.

`[imagen omitida: wiki id 32714]`

**5)** Look for the theme class whose font you want to change (in this case, a button class) and look for the Font Family property. In this property, select the newly added font from the combo-box.

`[imagen omitida: wiki id 35724]`

**6)** That's all. Just run your application and the text in the control will be displayed with the new font.

## [Notes](#Notes)

* *Apple only*:  If a *\***.otf* font does not work in an iOS or tvOS app, change its extension to *\*.ttf* before importing the file into the Theme. For example, rename 'fontText.otf' to 'fontText.**ttf**'.
* The file of the font must match the internal font name exactly. For example, if the font's internal name is “Claire Amoreth”, the file must be named **Claire Amoreth.ttf**.
* The Name property for the font **must** be the same that shows the font source file.  
  For example,  
  `[imagen omitida: wiki id 32715]`

## [Troubleshooting in iOS](#Troubleshooting+in+iOS)

### [Mismatch in font name](#Mismatch+in+font+name)

In a few rare cases we've found that the font is registered in iOS with a different name than the one indicated inside the TTF font file. The symptoms when this happens are clear: the controls on screen will not have the appropriate font, as specified in the corresponding Theme Class.

In such a case, the name of the font in the Theme's Fonts node must match the name registered in iOS, and not the name inside the TTF file.

To find the correct name, you should follow these steps:

1. Add the font as described above, use it in some class and then use that class in a control, build the application (make sure it is transferred to the Mac).
2. Open the generated application project in Xcode and run it from there in the simulator.
3. Once the application is loaded in the simulator, go back to Xcode and pause the application (the pause button is located bellow the code editor).
4. Now, in the Xcode console, you can list the registered fonts by providing the font family name in the following command (using "Futura” as an example here):  
   `[imagen omitida: wiki id 47249]`
5. If you are not sure about the family name, you can list all the available font families with the following command:  
   `[imagen omitida: wiki id 47250]`

### [UI Optimized Fonts](#UI+Optimized+Fonts)

Whenever a custom font is used, the iOS Flexible Client will try to use a UI optimized version of that font, if the selected font variation is not optimized for UI. This has a profund impact in performance if the font variation is widely used.

However, you may not want this UI optimization, preferring the non-optimized font anyway.

How do you know you are in such a case? If you don't see the correct font variation in the UI (you may have used the GothamRounded-Book font, for instance, but you see the text in the app with GothamRounded-Bold), run the application directly from Xcode in the Simulator, and check for a message as follows in the Xcode console:

*UI optimized font changed from '%@' to '%@'. To avoid this behavior, add a GXDisableUIOptimizedFontEnforcement key with value YES to the Info.plist.*

Note that the %@ placeholders in the message correspond to the font names and will be instanciated when you run your application.

To disable this UI optimization (be aware that it may have a performance impact), you can add the GXDisableUIOptimizedFontEnforcement key to the application's Info.plist, of type Boolean and with value YES.

This key is available as from [GeneXus 17 upgrade 1](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46852,,).

## [Scope](#Scope)

**Objects:** [Theme object](https://wiki.genexus.com/commwiki/wiki?16595)  
**Generators:** Android, Apple, Angular

## [Availability](#Availability)

This functionality is available as from [GeneXus 15](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?28265,,) Upgrade 1.


|  |
| --- |
| **Backlinks** |
| [Attribute theme-class](https://wiki.genexus.com/commwiki/wiki?37646) | [Button theme-class for Smart Devices](https://wiki.genexus.com/commwiki/wiki?37647) | [DesignOps - FAQ and Troubleshooting](https://wiki.genexus.com/commwiki/wiki?46880) |
| [HowTo: Using web fonts in Web Themes](https://wiki.genexus.com/commwiki/wiki?22701) | [Category:Theme object](https://wiki.genexus.com/commwiki/wiki?16595) |

---
