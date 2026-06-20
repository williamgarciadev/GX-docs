---
title: "Development Team ID property"
source_id: 30100
source_url: https://wiki.genexus.com/commwiki/wiki?30100
genexus_version: "18"
---

# Development Team ID property

Apple's Team ID to be included in the generated Xcode project.

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

The Apple's Developer Team ID property to be used for the generated Xcode project.

It must be set when the [Execution Type property](https://wiki.genexus.com/commwiki/wiki?18658) is *iOS Device (Mac)* and you intend to run the application on a phisycal device.

Note: if you don't set this property in GeneXus you'll have to set it in Xcode.

#### [How to know my Team-ID?](#How+to+know+my+Team-ID%3F)

1. Login to [**Apple's Developers**](http://developer.apple.com/) site

|  |
| --- |
|  |

2. Go to the "Membership" tab

|  |
| --- |
|  |

3.  There you can find the Team-ID associated with you Apple-ID.

|  |
| --- |
|  |

4. Copy the 10-characters string that appears in Team-ID field to the GeneXus' **Development Team ID property.**This Team ID will be used as a prefix for the [Bundle Id](https://wiki.genexus.com/commwiki/wiki?17380) of your application.

When GeneXus sends the information associated with your iOS application to the Mac computer, this Team ID will appear in XCode under General section of your project.

|  |
| --- |
|  |

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770). |

### [See Also](#See+Also)

* [HowTo: Publish an application to the Apple App Store](https://wiki.genexus.com/commwiki/wiki?18958)


|  |
| --- |
| **Backlinks** |
| [Apple Bundle Identifier property](https://wiki.genexus.com/commwiki/wiki?37617) | [Execution Type property](https://wiki.genexus.com/commwiki/wiki?18658) | [GAM - Apple Authentication type](https://wiki.genexus.com/commwiki/wiki?44478) |
| [HowTo: Deep Linking on Native Mobile](https://wiki.genexus.com/commwiki/wiki?36163) | [HowTo: Publish an application to the Apple App Store](https://wiki.genexus.com/commwiki/wiki?18958) | [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817) |

---
