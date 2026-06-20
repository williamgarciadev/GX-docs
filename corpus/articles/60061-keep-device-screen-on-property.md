---
title: "Keep Device Screen On property"
source_id: 60061
source_url: https://wiki.genexus.com/commwiki/wiki?60061
genexus_version: "18"
---

# Keep Device Screen On property

Keeps the screen active, ensuring continuous visibility in your application.

## [Scope](#Scope)

**Objects:** [Panel](https://wiki.genexus.com/commwiki/wiki?24829)  
**Generators:**[Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453)

## [Description](#Description)

When enabled, this property prevents the screen from entering sleep mode or turning off automatically due to user inactivity. This ensures that critical information remains visible at all times, enhancing the overall user experience.

The device screen remains on while the application is active. It is especially useful for applications that require constant display of information, such as dashboards, monitoring systems, or real-time logistics apps.

### [Important Considerations](#Important+Considerations)

* Keeping the screen continuously on will increase battery consumption. Therefore, it is recommended to use this property only in panels where it is strictly necessary.
* It is advisable to inform the application user about the potential impact on battery life.
* On some devices, the operating system’s power-saving mode may override this property to optimize battery usage, affecting its expected behavior.
* This property can be enabled from the panel's properties window.

## [Availability](#Availability)

Since [GeneXus 18 Upgrade 13](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?59630,,).
