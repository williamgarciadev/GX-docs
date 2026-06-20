---
title: "Flipping The Interface for Right-to-Left (GeneXus 18 Upgrade 2)"
source_id: 54489
source_url: https://wiki.genexus.com/commwiki/wiki?54489
genexus_version: "18"
---

# Flipping The Interface for Right-to-Left (GeneXus 18 Upgrade 2)

First and foremost, the interface must be flipped from right to left.

In RTL language regions, people read and write from right to left. This means that most interface elements should be flipped in order to be displayed correctly.

Here’s an example of Facebook’s left-to-right (LTR) design vs RTL:

|  |  |
| --- | --- |
|  |  |

Notice a LTR design:

`[imagen omitida: wiki id 42328]`

needs to be mirrored

`[imagen omitida: wiki id 42329]`

When a UI is mirrored, these changes occur:

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

When using Web applications, you need two [Design System](https://wiki.genexus.com/commwiki/wiki?47375) (DSO) or [Theme](https://wiki.genexus.com/commwiki/wiki?6420) objects. One to be used with standard LTR interfaces and a second one to mirror your default. You need to apply the correct configuration on different controls and your Theme/DSO classes. For reference, you will notice a *Carmine* and *CarmineRTL* themes for such purposes.

#### [How to create your new Theme to RTL?](#How+to+create+your+new+Theme+to+RTL%3F)

* [Compare](https://wiki.genexus.com/commwiki/wiki?22685) *Carmine* and *CarmineRTL* Themes on the IDE and look for changes on directions, custom properties and apply them to your RTL Themes. A few of them are *float*, *direction*, *TextAlign*. Depending on your design you may need to change margins, paddings and so on.
* Use an external site such as [rtlcss.com](https://rtlcss.com/playground) to generate RTL CSS directly and then import it back to GeneXus.

#### [Theme to DSO](#Theme+to+DSO)

If you already have a RTL Theme follow these steps to convert it to DSO:

* Save as the RTL Theme as a DSO object, continue using the [SetTheme function](https://wiki.genexus.com/commwiki/wiki?21777) to change it dynamically.

To create a RTL DSO object:

* Save as the LRT DSO.
* Create a new empty DSO and change the Base CSS property to use Bootstrap v3 RTL.
* Add the original DSO object using an import rule into styles part of the new empty DSO, for example  
  *@include DSO\_Saved*
* Adjust classes needed or create new ones as detailed previously.
