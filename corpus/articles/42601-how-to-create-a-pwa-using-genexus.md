---
title: "How to create a PWA using GeneXus"
source_id: 42601
source_url: https://wiki.genexus.com/commwiki/wiki?42601
genexus_version: "18"
---

# How to create a PWA using GeneXus

There are two ways to create a [Progressive Web Application using GeneXus](https://wiki.genexus.com/commwiki/wiki?42600).

## [1. Using Panels and generating with GeneXus Angular Generator](#1.+Using+Panels+and+generating+with+GeneXus+Angular+Generator)

To generate a [Progressive Web Application](https://wiki.genexus.com/commwiki/wiki?42600) with [Angular](https://wiki.genexus.com/commwiki/wiki?42550), you only have to set the [Build Mode property](https://wiki.genexus.com/commwiki/wiki?49860) (offered at the generator level) to "Distribution" and define the necessary [Panels](https://wiki.genexus.com/commwiki/wiki?24829) and complementary objects.

This is the recommended option because:

* The generated solution is better.
* You model it once and the same definitions can be used to generate a Native Mobile solution.

To customize the generated app (title, colors, icon, display mode, etc.), first, you have to set the [Web Frontend Application property](https://wiki.genexus.com/commwiki/wiki?54265)to *"*Progressive*"* at the [Main](https://wiki.genexus.com/commwiki/wiki?5770) object level ([Panels](https://wiki.genexus.com/commwiki/wiki?24829), [Menus](https://wiki.genexus.com/commwiki/wiki?16321) and/or [WorkWith](https://wiki.genexus.com/commwiki/wiki?15974) object). Then, a set of properties will be displayed to configure the required details:

* [Web Frontend Application Name property](https://wiki.genexus.com/commwiki/wiki?54258)
* [Web Frontend Application Short Name property](https://wiki.genexus.com/commwiki/wiki?54259)
* [Web Frontend Application Description property](https://wiki.genexus.com/commwiki/wiki?54260)
* [Web Frontend Display Mode property](https://wiki.genexus.com/commwiki/wiki?54261)
* [Web Frontend Background Color property](https://wiki.genexus.com/commwiki/wiki?54262)
* [Web Frontend Theme Color property](https://wiki.genexus.com/commwiki/wiki?54263)
* [Web Frontend Application Icon property](https://wiki.genexus.com/commwiki/wiki?54264)

### [Sample](#Sample)

[PlantCare - ECommerce Sample](https://wiki.genexus.com/commwiki/wiki?50476)

## [2. Using Web Panels and other Web Objects](#2.+Using+Web+Panels+and+other+Web+Objects)

To solve it in this way, follow the steps below:

1. Create your web application as usual (Use [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)s and other Web Objects).

2. Edit the main Web Panel of your application and set the [Web Application property](https://wiki.genexus.com/commwiki/wiki?42602) to "Progressive".  
  
3. After that, related properties appear and need to be set. Set those to define the look and feel and the behavior of the PWA.

* [Web Application Name property](https://wiki.genexus.com/commwiki/wiki?42603)
* [Web Application Short Name property](https://wiki.genexus.com/commwiki/wiki?42604)
* [Web Application Description property](https://wiki.genexus.com/commwiki/wiki?42605)
* [Primary Text Direction property](https://wiki.genexus.com/commwiki/wiki?42607)
* [Display property](https://wiki.genexus.com/commwiki/wiki?42608)
* [Background Color property](https://wiki.genexus.com/commwiki/wiki?42609)
* [Theme Color property](https://wiki.genexus.com/commwiki/wiki?42610)
* [Prefer Related Applications property](https://wiki.genexus.com/commwiki/wiki?42611)
* [Web Application Icon property](https://wiki.genexus.com/commwiki/wiki?42612)
* [Android Alternative App property](https://wiki.genexus.com/commwiki/wiki?42613)
* [Android Alternative App Identifier property](https://wiki.genexus.com/commwiki/wiki?43798)
* [iOS Alternative App property](https://wiki.genexus.com/commwiki/wiki?42614)
* [Offline Object property](https://wiki.genexus.com/commwiki/wiki?42615)

4. Build the Main Web Panel, and that's it!  
     
   GeneXus will automatically generate the following:

* A manifest file for your PWA.
* A service worker which is in charge of the reliability of the application.

5. Recommended: Verify with [LightHouse](https://wiki.genexus.com/commwiki/wiki?42665) that you've got a PWA.

### [Sample](#Sample)

Here is a sample XPZ with a PWA: [PWA Sample Crowdfundme](https://wiki.genexus.com/commwiki/wiki?44181,,)


|  |
| --- |
| **Backlinks** |
| [How to create a PWA using GeneXus (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?55046) | [Toc:Progressive Web Applications in GeneXus](https://wiki.genexus.com/commwiki/wiki?42600) | [Web Frontend Application Description property](https://wiki.genexus.com/commwiki/wiki?54260) |
| [Web Frontend Application Icon property](https://wiki.genexus.com/commwiki/wiki?54264) | [Web Frontend Application Name property](https://wiki.genexus.com/commwiki/wiki?54258) | [Web Frontend Application Short Name property](https://wiki.genexus.com/commwiki/wiki?54259) | [Web Frontend Background Color property](https://wiki.genexus.com/commwiki/wiki?54262) |
| [Web Frontend Display Mode property](https://wiki.genexus.com/commwiki/wiki?54261) | [Web Frontend Theme Color property](https://wiki.genexus.com/commwiki/wiki?54263) |

---
