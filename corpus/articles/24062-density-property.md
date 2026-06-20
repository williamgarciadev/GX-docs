---
title: "Density property"
source_id: 24062
source_url: https://wiki.genexus.com/commwiki/wiki?24062
genexus_version: "18"
---

# Density property

This property allows us to use different images depending on the density of the device screen.

### [Values](#Values)

|  |  |
| --- | --- |
| **Unknown** | Equal to hdpi for Android and mdpi (1x) for iOS. For compatibility with previous versions of GeneXus (do not use for new images since densities are inconsistent among platforms). |
| **75% (ldpi Android, .75x Web)** | Low density (120dpi) |
| **125% (Windows, 1.25x Web)** |
| **150% (hdpi Android, Windows, 1.5x Web)** | High-density screens (240dpi) |
| **100% (mdpi Android, 1x iOS, Windows, 1x Web)** | Medium-density (160dpi). Baseline. (Non retina images for iOS) |
| **200% (xhdpi Android, 2x iOS, Windows, 2x Web)** | Extra high-density screens (320dpi). (2x Retina images for iOS) |
| **300% (xxhdpi Android, 3x iOS, 3x Web)** | Extra-extra-high-density screens (480dpi) (3x Retina images for iOS) |
| **400% (xxxhdpi Android, Windows, 4x Web)** | Extra-extra-extra-high-density screens (640dpi) |

### [Description](#Description)

For example, Smart Devices applications, especially for Android, are executed on a great number of different devices from different makers and characteristics, with different screen sizes (in cm), resolution (pixels) and densities (the number of pixels per physical unit of length, expressed in dpi).

**Android note:**While including all density variants is not mandatory, it's highy recommended to do so. If a particular density is not available for an image, then the closest one will be automatically scaled. This may, however, produce visual artifacts. To create alternative bitmaps for different densities, you should follow the 3:4:6:8:12 scaling ratio. For example, if you have a bitmap drawable that's 48x48 pixels for medium-density screen (the size for a launcher icon), all the different sizes should be:

* 36x36 for low-density (LDPI)
* 48x48 for medium-density (MDPI)
* 72x72 for high-density (HDPI)
* 96x96 for extra high-density (XHDPI)
* 144x144 for extra extra high-density (XXHDPI)

Check [HowTo: Use different images depending on the theme, language and density of the screen](https://wiki.genexus.com/commwiki/wiki?23754) to know how to use this property.

**iOS note:** The different densities of an image are only considered when they are included in the compiled application.

### [Scope](#Scope)

**Objects:** Image  
**Platforms:** Web(.Net, Java), Smart Devices(Android, IOS)

### [See Also](#See+Also)

[How to use responsive images in a web application](https://wiki.genexus.com/commwiki/wiki?31566)


|  |
| --- |
| **Backlinks** |
| [Getting Started with tvOS](https://wiki.genexus.com/commwiki/wiki?40787) | [How to use responsive images in a web application](https://wiki.genexus.com/commwiki/wiki?31566) |
| [HowTo: Use different images depending on the theme, language and density of the screen](https://wiki.genexus.com/commwiki/wiki?23754) | [Category:Image object](https://wiki.genexus.com/commwiki/wiki?23387) | [Images in Panels](https://wiki.genexus.com/commwiki/wiki?31379) |

---
