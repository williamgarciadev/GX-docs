---
title: "Slide Navigation Style"
source_id: 21285
source_url: https://wiki.genexus.com/commwiki/wiki?21285
genexus_version: "18"
---

# Slide Navigation Style

The **Slide navigation style** has gained popularity because many apps are using it, including Gmail, Facebook, and Youtube. Many other apps use this navigation style to provide a better user experience.

For example, consider the main Menu to be available from any layout, regardless of the invocation depth level you are in. You're always able to slide right to have the main menu appear.

GeneXus integrates this navigation style, enabling users to utilize its intuitive functionalities to their advantage.

### [How to develop GeneXus apps that have Slide navigation style](#How+to+develop+GeneXus+apps+that+have+Slide+navigation+style)

The only thing needed is to define that the Slide navigation style is going to be used for a certain platform.

To implement the Slide navigation style in your GeneXus app, follow these simple steps:

1. Go to Customization > Platforms in the KB Explorer:

`[imagen omitida: wiki id 57872]`

2. Choose the Slide navigation style

`[imagen omitida: wiki id 21289]`

Once this is done, your application will use this navigation style.

### [About Slide navigation style](#About+Slide+navigation+style)

When the application starts up, the first screen you see is the **first item** of your Menu structure.

In this screen, you have the following interaction options:

`[imagen omitida: wiki id 21286]`

By sliding right or tapping on the Menu icon at the top left corner, you can go to the Menu.

The Menu will appear on almost all screens.

`[imagen omitida: wiki id 21287]`

By tapping on the menu button at the top right corner or sliding left in any part of the screen, the Menu will hide again.

By tapping on any of the options, it will take you to the object.

### [Considerations about ClientStart Event in Slide Navigation Style](#Considerations+about+ClientStart+Event+in+Slide+Navigation+Style)

In applications using Slide Navigation Style, the behavior of the ClientStart event differs between Android and iOS:

* **Android:** The ClientStart event of the Slide Panel is triggered each time a new panel is loaded in the main target. This occurs because the Slide Panel is recreated for each new navigation.
* **iOS:** The ClientStart event is triggered only once when the Slide Panel is initially loaded. It does not trigger again for subsequent navigations.

**Notes:**

* To achieve consistent behavior across platforms, use the Slide.Start event for initialization code related to the Slide Navigation, as it is executed only once when the application starts.
* Use ClientStart for panel-specific initialization code, but be aware of the platform-specific behavior differences.

### [Customization](#Customization)

Customizing the menu grid UI follows the same process as other navigation styles.

The Menu object has a Class property to assign a theme class to it.

According to [Google Specifications](https://www.google.com/design/spec/patterns/navigation-drawer.html#navigation-drawer-specs), the size of the Slide Menu must not be changed.

### [Scope](#Scope)

**Generator:** [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453)

### [Availability](#Availability)

This feature is available for iOS as of [GeneXus X Evolution 2 Upgrade 3](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?22061,,) and for Android as of [GeneXus X Evolution 2 Upgrade 4](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?22626,,).

### [See it in action](#See+it+in+action)

[RecursosUX](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?23280,,)

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]`  [Slide Navigation Style in Universitario de Deportes](http://www.youtube.com/watch?v=3ZHh3MHwm6c)


|  |
| --- |
| **Backlinks** |
| [Application Colors Properties group](https://wiki.genexus.com/commwiki/wiki?28621) | [ClientStart event](https://wiki.genexus.com/commwiki/wiki?24044) |
| [Navigation Style property](https://wiki.genexus.com/commwiki/wiki?16229) |
| [Slide.Start event](https://wiki.genexus.com/commwiki/wiki?25585) |

---
