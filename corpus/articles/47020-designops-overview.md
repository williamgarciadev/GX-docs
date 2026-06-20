---
title: "DesignOps - Overview"
source_id: 47020
source_url: https://wiki.genexus.com/commwiki/wiki?47020
genexus_version: "18"
---

# DesignOps - Overview

GeneXus improves the synergy between designers and developers in order to create a good-looking application in record time.

The main idea resides in defining responsibilities for each role. As obvious as it may seem, Designers know about user experience and interactions while Developers know how to code and make the application functional. They both use different tools, different points of view, different processes, etc. When one role is missing or both roles start mixing responsibilities, early problems during the development cycle may arise and that is what GeneXus aims to simplify.

**Content**  

* [**What do you (as a designer) have to do for designing an app?**](#What+do+you+%28as+a+designer%29+have+to+do+for+designing+an+app%3F)
* [**What do you (as a developer) have to do for integrating a design?**](#What+do+you+%28as+a+developer%29+have+to+do+for+integrating+a+design%3F)
* [**What do you have to know before starting with DesignOps in GeneXus?**](#What+do+you+have+to+know+before+starting+with+DesignOps+in+GeneXus%3F)
* [**Why should you use GeneXus for facilitating interaction between designers and developers?**](#Why+should+you+use+GeneXus+for+facilitating+interaction+between+designers+and+developers%3F)
* [**Availability**](#Availability)

## [**What do you (as a designer) have to do for designing an app?**](#What+do+you+%28as+a+designer%29+have+to+do+for+designing+an+app%3F)

Currently, GeneXus offers support for importing a design model made with the [Sketch design tool](https://www.sketch.com/) and [Figma design tool](https://www.figma.com/) (other tools will be available in the future). There is a [guide for designers](https://wiki.genexus.com/commwiki/wiki?46871) you must follow and an [article of best practices](https://wiki.genexus.com/commwiki/wiki?46874) for making the interaction with the developer easier. Remember to be tidy and keep your design simple in order to achieve a good result on the first try.

## [**What do you (as a developer) have to do for integrating a design?**](#What+do+you+%28as+a+developer%29+have+to+do+for+integrating+a+design%3F)

GeneXus offers a [Design Import option](https://wiki.genexus.com/commwiki/wiki?46882) tool for initializing the UI of your application. If you reimport a design, it will override changes that you probably had made by hand, so be careful. Remember that the result may not be perfect due to different reasons (aspects not modeled in the design file, platform gaps, etc.) but it should be easy for you to fix those details when you run it the first time. GeneXus only generates the GeneXus objects that are represented in the design files. On the other hand, the data content of the application is initialized by the examples given in the design files, and it is your responsibility to fill that data with real data. GeneXus only imports the UI; the business logic depends on you.

## [**What do you have to know before starting with DesignOps in GeneXus?**](#What+do+you+have+to+know+before+starting+with+DesignOps+in+GeneXus%3F)

Designers and Developers speak different languages. Both roles should read the articles that GeneXus offers in order to better understand each world. The following table shows you a set of terms that you both (designer and developers) will start to use frequently and where each of them has a unique relationship.

|  |  |
| --- | --- |
| **Design term** | **Developer term** |
| Symbol / Component | Stencil |
| Artboard / Main-Frame | (Web) Panel |
| Link / Interaction | Call |
| Style | Theme Class / Style Class |
| Color Variable | Color Palette Item / Color Token |
| Group / Frame Layer | Table  Canvas (when there is overlapping)  Control (when a convention is applied: Combo-Box, Check-Box, Radio-Button, etc.) |
| Text Layer | Readonly Variable  TextBlock (when Static convention is applied)  Read-Write Variable (when Input convention is applied) |
| List | Vertical Grid |
| Carousel | Horizontal grid |

So, for example, if you are a developer and you notice that after importing a design there are some controls that should be together in a table, check with the designer if he/she groups that layers in the design. This process of importing a design by the developer and checking it with the designer to fix it will be part of your development process until you both achieve a good result. It is recommended that you start by designing a single panel, import it, and check the generated object (both at design time and runtime). Next, iterate until you are satisfied with the result before designing a new artboard, and so on until you have a fully functional application.

## [**Why should you use GeneXus for facilitating interaction between designers and developers?**](#Why+should+you+use+GeneXus+for+facilitating+interaction+between+designers+and+developers%3F)

GeneXus' philosophy is to automate everything that can be automated. In our experience, the process of developing the UI of an application takes the most part of the development cycle. If the UI design is in the hands of an expert (the designer) there are two advantages: 1) The application will have a professional look & feel, and 2) The developer will have a set of panels previously created that may require minimal changes and then they can focus on the business logic.

## [**Availability**](#Availability)

DesignOps facilities are available as of [GeneXus 17](https://wiki.genexus.com/commwiki/wiki?46873,,).

* As of [GeneXus 17 upgrade 1](https://wiki.genexus.com/commwiki/wiki?46852,,):  
  - Color Variables are supported.
* As of [GeneXus 17 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?49971,,)  
  - Figma provider is supported.


|  |
| --- |
| **Backlinks** |
| [Design System Object - Fundamental bases](https://wiki.genexus.com/commwiki/wiki?48675) | [Design System Object - How to provide style data to your controls](https://wiki.genexus.com/commwiki/wiki?48685) | [DesignOps - FAQ and Troubleshooting](https://wiki.genexus.com/commwiki/wiki?46880) |
| [Toc:DesignOps and GeneXus](https://wiki.genexus.com/commwiki/wiki?46870) |

---
