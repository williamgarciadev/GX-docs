---
title: "Flipping The Interface for Right-to-Left"
source_id: 54467
source_url: https://wiki.genexus.com/commwiki/wiki?54467
genexus_version: "18"
---

# Flipping The Interface for Right-to-Left

In RTL language regions, people read and write from right-to-left (RTL). This means that most interface elements should be flipped in order to be displayed correctly.

Here’s an example of Facebook’s left-to-right (LTR) design vs RTL:

|  |  |
| --- | --- |
|  |  |

Note how in the following schematic the LTR design is mirrored:

|  |  |
| --- | --- |
|  |  |

When a User Interface is mirrored, these changes occur:

* Text fields icons are displayed on the opposite side of a field.
* Navigation buttons are displayed in reverse order.
* Icons that communicate direction, like arrows, paging are mirrored.
* Text (if it is translated to an RTL language) is aligned to the right.

These items are not mirrored:

* Icons or Images that don’t communicate direction, such as a camera.
* Numbers, such as those on a clock and phone numbers.
* Charts and graphs (X and Y axes always appear in the same orientation).
* Video controls and timeline indicators (already discussed).
* Clocks.
* Music notes and sheet music.

### [Native Mobile](#Native+Mobile)

When using [Native Mobile Generator](https://wiki.genexus.com/commwiki/wiki?14451) this is automatically done by the platform. The GeneXus application will notice it is using a RTL language so the mirroring will happen when needed.

### [Web](#Web)

Web applications using [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375) (DSO) with the [Base CSS property](https://wiki.genexus.com/commwiki/wiki?49256) set to "None" are generated with the ["dir" attribute](https://caniuse.com/?search=html%20dir%20attribute) to match the language direction of the application. However, it is important to make sure that the applied styles follow the corresponding guidelines for proper display in each case.

#### [Theme to Design System Object](#Theme+to+Design+System+Object)

If you already have a RTL [Theme](https://wiki.genexus.com/commwiki/wiki?6420) follow these steps to convert it to [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375) (DSO):

* Save the RTL Theme as a DSO object.
* Select the value None in the [Base CSS property](https://wiki.genexus.com/commwiki/wiki?49256) to change it dynamically. If you select a value other than None in Base CSS property, continue using the [SetTheme function](https://wiki.genexus.com/commwiki/wiki?41978) to change it dynamically.

When using Web applications that use Theme Objects with a value other than None in the Base CSS property, you need two Theme Objects. One to be used with standard LTR interfaces and a second one to mirror your default. You need to apply the correct configuration on different controls and your Theme classes.

#### [How to create your Theme to RTL?](#How+to+create+your+Theme+to+RTL%3F)

* [Compare](https://wiki.genexus.com/commwiki/wiki?22685) the Themes on the IDE and look for changes on directions, custom properties and apply them to your RTL Themes. A few of them are *float*, *direction*, *TextAlign*. Depending on your design you may need to change margins, paddings and so on.
* Use an external site such as [rtlcss.com](https://rtlcss.com/playground) to generate RTL CSS directly and then import it back to GeneXus.

#### [How to create your RTL DSO object?](#How+to+create+your+RTL+DSO+object%3F)

* Create a new empty DSO and change the Base CSS property to use Bootstrap v3 RTL.
* Adjust classes needed or create new ones as detailed previously.

### [See Also](#See+Also)

[HowTo: Add RTL styles](https://wiki.genexus.com/commwiki/wiki?42319)  
[GeneXus Application Localization](https://wiki.genexus.com/commwiki/wiki?6330)


|  |
| --- |
| **Backlinks** |
| [Flipping The Interface for Right-to-Left (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54489) | [Toc:Getting ready for Right-to-Left Development](https://wiki.genexus.com/commwiki/wiki?42322) |

---
