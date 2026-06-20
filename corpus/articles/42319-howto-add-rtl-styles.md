---
title: "HowTo: Add RTL styles"
source_id: 42319
source_url: https://wiki.genexus.com/commwiki/wiki?42319
genexus_version: "18"
---

# HowTo: Add RTL styles

At least 200 million Internet users speak a language that is written from right to left. GeneXus allows you to incorporate [RTL](https://wiki.genexus.com/commwiki/wiki?42318) styles so that your applications can reach those markets.

Learn the importance of RTL styles and how to add them to your development. Follow these steps.

* Review the [Workstation Settings](https://wiki.genexus.com/commwiki/wiki?42339) needed.
* Review the [Default KB language and Database Collation](https://wiki.genexus.com/commwiki/wiki?42336) needed for internationalization.
* [Localize](https://wiki.genexus.com/commwiki/wiki?6330) your product accordingly using the [Language object](https://wiki.genexus.com/commwiki/wiki?7258).
* Create an RTL [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375) and set the correct [Base CSS property](https://wiki.genexus.com/commwiki/wiki?49256). You can also create [Web Theme object](https://wiki.genexus.com/commwiki/wiki?6420) and also set the correct [Base Style property](https://wiki.genexus.com/commwiki/wiki?38230).   

  **Note**: If you base your styles on a [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375) and select the value None in the [Base CSS property](https://wiki.genexus.com/commwiki/wiki?49256), GeneXus will automatically generate the necessary for your application to be displayed in LTR or RTL depending on the language of the application. Furthermore, ​browsers running applications using Design System require 'dir' attribute support ([HTML attribute: dir](https://caniuse.com/?search=html%20dir%20attribute),  [CSS Logical Properties](https://caniuse.com/?search=logical%20properties)). See [SAC #52783](https://www.genexus.com/en/developers/websac?data=52783;;) for more information.
* Review all the steps from:
  + [Getting ready for Right-to-Left Development](https://wiki.genexus.com/commwiki/wiki?42322)
* Thoroughly test your RTL generated application to make sure everything looks right.
* Deploy and iterate.


|  |
| --- |
| **Backlinks** |
| [Flipping The Interface for Right-to-Left](https://wiki.genexus.com/commwiki/wiki?54467) | [HowTo: Add RTL styles (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54443) |
| [Real-time translation of RTL languages](https://wiki.genexus.com/commwiki/wiki?54482) | [Category:RTL](https://wiki.genexus.com/commwiki/wiki?42318) |

---
