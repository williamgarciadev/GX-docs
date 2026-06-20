---
title: "HowTo: Take up the full height of a page"
source_id: 30640
source_url: https://wiki.genexus.com/commwiki/wiki?30640
genexus_version: "18"
---

# HowTo: Take up the full height of a page

Suppose that you have the following design for a web page in a [Responsive Web Applications](https://wiki.genexus.com/commwiki/wiki?25159), where the left component should take the full height of the page:

`[imagen omitida: wiki id 30641]`

In this example, a [Work With object](https://wiki.genexus.com/commwiki/wiki?15974) is displaying the filter panel on the left-hand side of the screen and the idea for it is to take the full height of the page as the picture shows:

`[imagen omitida: wiki id 30648]`

This [Responsive Table](https://wiki.genexus.com/commwiki/wiki?24961) that contains the filter (*&CountryName*) is associated with the *AdvancedContainer* class.

The solution is to use [Viewport units](https://wiki.genexus.com/commwiki/wiki?30636). So, assign the value 100vh to the height property of the *AdvancedContainer* class, which implies taking the full height of the page.

`[imagen omitida: wiki id 30646]`

Configuring the height to be 100% of the container does not cause the intended effect. It would look as follows:

`[imagen omitida: wiki id 30647]`


|  |
| --- |
| **Backlinks** |
| [Using relative length units on the web](https://wiki.genexus.com/commwiki/wiki?30636) |

---
