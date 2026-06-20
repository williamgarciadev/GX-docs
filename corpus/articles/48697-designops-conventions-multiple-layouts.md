---
title: "DesignOps - Conventions - Multiple Layouts"
source_id: 48697
source_url: https://wiki.genexus.com/commwiki/wiki?48697
genexus_version: "18"
---

# DesignOps - Conventions - Multiple Layouts

When you design multiple Artboards or Main-Frames representing variations of the same screen (displayed in different devices), GeneXus will join them in the same Panel object with multiple layouts.

## [Description](#Description)

Designs of a screen for multiple platforms, devices, and orientations can be imported into GeneXus by following a token sequence convention described in the [Grammar section](https://wiki.genexus.com/commwiki/wiki?48697) and then adding a suffix to the Artboard's name.

As a result, you can design multiple Artboards as follows:

|  |
| --- |
|  |

Then, GeneXus will hierarchically display those Artboards or Main-Frames in the [Design Import option](https://wiki.genexus.com/commwiki/wiki?46882).

|  |
| --- |
|  |

All those Artboards or Main-Frames will be rendered in the same Panel object with all its variants.

|  |
| --- |
|  |

**Warning**: This feature only applies to Panel objects (not Web Panel objects), so the "*Import as Web Panel*" option in the [Design Import option](https://wiki.genexus.com/commwiki/wiki?46882) dialog must be **cleared** before loading/importing the design.

**Note**: GeneXus will generate the appropriate layouts based on the conventions you used, and at runtime, it will take them in precedence order (taking always the more specific for each platform).

## [Grammar](#Grammar)

The token sequence convention for multiple layouts must follow this grammar:

|  |  |  |
| --- | --- | --- |
| convention | := | PANEL\_NAME separator platform |
| platform | := | device  | 'Web' device  | 'Android' device  | 'Apple' device |
| device | := | orientation  | 'Phone' orientation  | 'Tablet' orientation  | 'Watch'  | 'TV' |
| orientation | := | ''  | 'Landscape' |
| separator | := | ''  | *any non-alphanumeric character except slash ("/")* |

### [Example & Invalid combinations](#Example+%26+Invalid+combinations)

For example, if the panel you are designing is called "Attraction Panel", the grammar allows you to define the following layouts:

|  |  |  |
| --- | --- | --- |
| **Artboard / Main-Frame Name** | |  |
| Attraction Panel |  |  |
| Attraction Panel | - Landscape |  |
| Attraction Panel | - Phone |  |
| Attraction Panel | - Phone Landscape |  |
| Attraction Panel | - Tablet |  |
| Attraction Panel | - Tablet Landscape |  |
| Attraction Panel | - Watch | ← INVALID: Doesn't make sense without indicating the target device. |
| Attraction Panel | - Watch Landscape | ← INVALID: Same reason as 'Watch". |
| Attraction Panel | - TV | ← INVALID: Doesn't make sense without indicating the target device. |
| Attraction Panel | - TV Landscape | ← INVALID: Same reason as "TV". |
| Attraction Panel | - Web |  |
| Attraction Panel | - Web Landscape | ← INVALID: Doesn't make sense. |
| Attraction Panel | - Web Phone |  |
| Attraction Panel | - Web Phone Landscape |  |
| Attraction Panel | - Web Tablet | ← INVALID: Doesn't make sense, you will use "Web" instead. |
| Attraction Panel | - Web Tablet Landscape | ← INVALID: Same as "Web Tablet". |
| Attraction Panel | - Web Watch | ← INVALID: Doesn't make sense. |
| Attraction Panel | - Web Watch Landscape | ← INVALID: Same as "Web Watch". |
| Attraction Panel | - Web TV | ← INVALID: Doesn't make sense. |
| Attraction Panel | - Web TV Landscape | ← INVALID: Same as "Web TV". |
| Attraction Panel | - Android |  |
| Attraction Panel | - Android Landscape |  |
| Attraction Panel | - Android Phone |  |
| Attraction Panel | - Android Phone Landscape |  |
| Attraction Panel | - Android Tablet |  |
| Attraction Panel | - Android Tablet Landscape |  |
| Attraction Panel | - Android Watch | ← INVALID: GeneXus doesn't support it. |
| Attraction Panel | - Android Watch Landscape | ← INVALID: Same as "Android Watch". |
| Attraction Panel | - Android TV | ← INVALID: GeneXus doesn't support it. |
| Attraction Panel | - Android TV Landscape | ← INVALID: Same as "Android TV". |
| Attraction Panel | - Apple |  |
| Attraction Panel | - Apple Landscape |  |
| Attraction Panel | - Apple Phone |  |
| Attraction Panel | - Apple Phone Landscape |  |
| Attraction Panel | - Apple Tablet |  |
| Attraction Panel | - Apple Tablet Landscape |  |
| Attraction Panel | - Apple Watch |  |
| Attraction Panel | - Apple Watch Landscape | ← INVALID: Doesn't make sense. |
| Attraction Panel | - Apple TV |  |
| Attraction Panel | - Apple TV Landscape | ← INVALID: Doesn't make sense. |

## [Considerations & Best Practices](#Considerations+%26+Best+Practices)

* If you don't define an Artboard or Main-Frame as a root layout (that is, without token suffix conventions), GeneXus will define a layout of type "*Any, Default Orientations*" with an empty Main Table.

  **Best Practice**:  
  Define at least one layout per panel without following token suffix conventions to generate it as a base layout.
* If two or more layouts of the same panel share a control (that is, a layer with the same semantics on every layout), GeneXus will consider only the definition of one of them.

  **Best Practice**:  
  If your design defines the same control in every layout for a panel (with the same semantics), make sure your control definition is the same on every layout; in other words, you must ensure that the properties on every duplicated layer are identical (for example, anchors, dimensions, alignments, styles, links, etc). Otherwise, consider renaming the layer that varies in a specific layout.
* If you define a link between two Artboards or Main-Frames representing variations of the same panel, GeneXus will not generate the call.

  **Best Practice**:  
  Avoid defining links between Artboards or Main-Frames that represent variations of the same panel; there is no value in those links.
* If you define an Artboard or Main-Frames following an invalid token combination, GeneXus will ignore the generation of that panel and will display a message as follows:  
  *> Artboard '{artboard-name}' ignored (layout convention '{token-combination}' not supported)*

  **Best Practice**:  
  Check the grammar convention for defining multiple layouts and check if the token sequence is supported by GeneXus.
* The convention matching process is case-insensitive and admits multiple non-alphanumeric characters as separators, except for "/" (slash) which is reserved for folder packaging.

  **Best Practice**:  
  Separate the token suffix sequence with a non-alphanumericcharacter. For instance, avoid "Attraction Panel Android" (ambiguous) or "Attraction Panel / Android" (wrong); instead, use "Attraction Panel - Android" to indicate that the Artboard or Main-Frame is the "Android" variation of a panel named "Attraction Panel".
* Each platform will take the most specific layout you define and the layout without convention will be applied when the target platform does not match any other layout you have defined.

  **Best Practice**:  
  Depending on your needs, you have to decide which will be better to define without convention. Remember that GeneXus will display the most specific layout that applies to the target platform.  
  So, for example, if you define your Phone artboard/main-frame without convention and your Web artboard with the "Web" convention, GeneXus will define an "Any Platform" layout with your Phone design and an "Any Web" with your Web design. Then, every time the end-user opens the application in the browser, the "Any Web" will always be displayed (both on Desktop or Mobile browsers). If you want to display the Phone design in a mobile browser, then you should define your Web artboard without convention (making it more general) and your Phone design with the "Phone" convention (making it more specific).

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators** | Android, Apple, Angular |

## [See also](#See+also)

* [Guide for designers](https://wiki.genexus.com/commwiki/wiki?46871)
* [Conventions](https://wiki.genexus.com/commwiki/wiki?46872)
* [Sample: Travel Agency multi-experience (Sketch)](https://wiki.genexus.com/commwiki/wiki?49453,,)
* [Sample: Plant Care multi-experience (Figma)](https://wiki.genexus.com/commwiki/wiki?53960,,)

## [Availability](#Availability)

These conventions are available as of [GeneXus 17 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?48247,,).


|  |
| --- |
| **Backlinks** |
| [DesignOps - Conventions - Multiple Layouts](https://wiki.genexus.com/commwiki/wiki?48697) | [Toc:DesignOps and GeneXus](https://wiki.genexus.com/commwiki/wiki?46870) |

---
