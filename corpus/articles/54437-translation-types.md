---
title: "Translation types"
source_id: 54437
source_url: https://wiki.genexus.com/commwiki/wiki?54437
genexus_version: "18"
---

# Translation types

There are two types of translations available in GeneXus:

* Static Translation
* Run-time Translation

### [Static Translation](#Static+Translation)

This is the best-performing translation option because it is solved at specification time. The generated code already contains the static translations.

The resulting application cannot change the language at runtime, so no runtime overhead is added.

It is available for all generators (many generators only have this value for the [Translation type property](https://wiki.genexus.com/commwiki/wiki?9126)).

Having your application in different languages requires different executable applications (one for each language). If you plan to have your application translated into different languages using Static translation, you must set up a new Environment for every new language you want to translate into.

#### [**How to enable Static translation**](#How+to+enable+Static+translation)

1. Set the [Translation type property](https://wiki.genexus.com/commwiki/wiki?9126) to 'Static'.
2. Select a predefined [Language object](https://wiki.genexus.com/commwiki/wiki?7258) (in the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210) below the Localization node) you want your application to be translated into. If the language you want your application to be translated into is not predefined, create a new Language object and select it. Consider that the [Is Right To Left property](https://wiki.genexus.com/commwiki/wiki?42126) must be set to define languages read right to left.
3. Set the [Translate to language property](https://wiki.genexus.com/commwiki/wiki?13242) to the language you want your application to be translated into.
4. Specify the entire application. All fixed texts to be translated will be added to the selected Language objects.
5. Enter the translation for every fixed text into the target Language object (consider exporting the Language object so that a translator can enter the translations using the [GeneXus Translation Tool](https://wiki.genexus.com/commwiki/wiki?2135)).
6. Press F5, and that's all!

Note that if your languages reference different ISO code pages, you will need to change the Windows regional settings configuration for each language generation process.

For instance, if you have languages such as Japanese, Chinese, Thai, and so on, the Static translation process needs to correctly configure the associated [Language for non-Unicode programs](https://wiki.genexus.com/commwiki/wiki?42339) (Windows configuration). If this is a problem for your Environment, switch to Run-time translation.

### [Run-time Translation](#Run-time+Translation)

Run-time translation is available for the [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258) and [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892) generators.

It is the most versatile solution with a little performance overhead (compared to Static translation).

When using Run-time translation, you can:

* Manage a single set of executable applications running in different languages;
* Allow the end user to select the desired application language from the list of available languages;
* Add new languages to your application without changing the executable code.

**How to enable Run-time translation**

1. Set the [Translation type property](https://wiki.genexus.com/commwiki/wiki?9126) to 'Run-time'.
2. Select the predefined [Language object](https://wiki.genexus.com/commwiki/wiki?7258)s (in the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210) below the Localization node) you want your application to be translated into. If the language you want your application to be translated into is not predefined, create a new Language object and select it. Consider that the [Is Right To Left property](https://wiki.genexus.com/commwiki/wiki?42126) must be set to define languages read right to left.
3. Specify the entire application. All fixed texts to be translated will be added to the selected Language objects.
4. Enter the translation for every fixed text into the target Language objects (consider exporting the Language object so that a translator can enter the translations using the [GeneXus Translation Tool](https://wiki.genexus.com/commwiki/wiki?2135)).
5. Use the [SetLanguage function](https://wiki.genexus.com/commwiki/wiki?18757) in your code where appropriate to indicate the language to be used.
6. Press F5, and that's all!

The orientation is determined automatically according to the application language if you base your styles on a [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375) and select the 'None' value for the [Base CSS property](https://wiki.genexus.com/commwiki/wiki?49256).

In addition, if you use [Web Theme object](https://wiki.genexus.com/commwiki/wiki?6420)s, Design Systems (with a value other than 'None' in the Base CSS property), or use different Themes or Design Systems depending on the orientation, you must use the [SetLanguage function](https://wiki.genexus.com/commwiki/wiki?18757) and the [SetTheme function](https://wiki.genexus.com/commwiki/wiki?21777).

### [Availability](#Availability)

Since [GeneXus 18 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?53853), the orientation is automatically determined by the SetLanguage function when a Design System has the Base CSS property set to None.

### [See Also](#See+Also)

[Real-time translation of RTL languages](https://wiki.genexus.com/commwiki/wiki?54482)


|  |
| --- |
| **Backlinks** |
| [Table of contents:GeneXus Application Localization](https://wiki.genexus.com/commwiki/wiki?6330) | [Category:Language object](https://wiki.genexus.com/commwiki/wiki?7258) | [Translation types (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54444) |
| [Workstation Settings](https://wiki.genexus.com/commwiki/wiki?42339) |

---
