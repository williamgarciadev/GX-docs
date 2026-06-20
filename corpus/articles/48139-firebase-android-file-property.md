---
title: "Firebase Android File property"
source_id: 48139
source_url: https://wiki.genexus.com/commwiki/wiki?48139
genexus_version: "18"
---

# Firebase Android File property

Indicates the configuration file to use for Firebase in Android. This file can be obtained in the Firebase Console.

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453)

### [Description](#Description)

This property is available after setting the main object [Analytics Provider property](https://wiki.genexus.com/commwiki/wiki?41575) to 'Firebase'.

Firebase is configured in the Firebase Console and downloaded as a file.

To use that configuration in a GeneXus-generated application:

* Add the downloaded file to the KB as a File object.
* Add a reference to that File object in this property.
* Note that the [Android Package Name property](https://wiki.genexus.com/commwiki/wiki?17814) in the main object must be the same as the one referenced in the File.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770).

### [Availability](#Availability)

This property is available since [GeneXus 17 upgrade 4](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?47936,,).


|  |
| --- |
| **Backlinks** |
| [Analytics Provider property](https://wiki.genexus.com/commwiki/wiki?41575) | [Analytics Provider property (GeneXus 18 or prior)](https://wiki.genexus.com/commwiki/wiki?57765) | [Analytics Provider property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54454) |
| [Analytics Provider property (GeneXus 18 Upgrade 3)](https://wiki.genexus.com/commwiki/wiki?57763) | [Enable Firebase Crashlytics property](https://wiki.genexus.com/commwiki/wiki?48141) |

---
