---
title: "How to create a PWA using GeneXus (GeneXus 18 Upgrade 2 or prior)"
source_id: 55046
source_url: https://wiki.genexus.com/commwiki/wiki?55046
genexus_version: "18"
---

# How to create a PWA using GeneXus (GeneXus 18 Upgrade 2 or prior)

There are two ways to create a [Progressive Web Application using GeneXus](https://wiki.genexus.com/commwiki/wiki?42600).

## [1. Using Panels and generating with GeneXus Angular Generator](#1.+Using+Panels+and+generating+with+GeneXus+Angular+Generator)

To generate a [Progressive Web Application](https://wiki.genexus.com/commwiki/wiki?42600) with [Angular](https://wiki.genexus.com/commwiki/wiki?42550) you only have to set the [Build Mode property](https://wiki.genexus.com/commwiki/wiki?49860) (offered at the generator level) to "Distribution" and define the necessary [Panels](https://wiki.genexus.com/commwiki/wiki?24829) and complementary objects.

This is the recommended option because:

* The generated solution is better.
* You model it once and the same definitions can be used to generate a Native Mobile solution.

**Note**:  To customize the generated app (title, colors, icon, display mode, etc.) you have to edit the manifest file located under mobile/Angular/Main/src.

### [Sample](#Sample)

[PlantCare - ECommerce Sample](https://wiki.genexus.com/commwiki/wiki?50476)

## [2. Using Web Panels and other Web Objects](#2.+Using+Web+Panels+and+other+Web+Objects)

To solve it in this way, you have to:

1. Create your web application as always (Use [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)s and other Web Objects).
2. Edit the main Web Panel of your application and set the [Web Application property](https://wiki.genexus.com/commwiki/wiki?42602) to "Progressive".
3. After that, related properties appear and need to be set. Set those to define the look and feel and the behavior of the PWA.
4. Build the Main Web Panel and that's it!  
     
   GeneXus will generate automatically:
   * A manifest file for your PWA.
   * A service worker which is in charge of the reliability of the application}}}
  
5. Recommended: Verify with [LightHouse](https://wiki.genexus.com/commwiki/wiki?42665) that you've got a PWA.

### [Sample](#Sample)

Here is a sample XPZ with a PWA: [PWA Sample Crowdfundme](https://wiki.genexus.com/commwiki/wiki?44181,,)
