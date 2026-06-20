---
title: "iOS Launch Image property"
source_id: 31375
source_url: https://wiki.genexus.com/commwiki/wiki?31375
genexus_version: "18"
---

# iOS Launch Image property

This property sets the main image that is launched when the application starts.

Since there are different kinds of devices with several sizes and resolutions, each one must be  loaded into the same [Image object](https://wiki.genexus.com/commwiki/wiki?23387).  
There are not any limitation for the image extension.  
If the developer provides only one image, GeneXus automatically generate all smaller images than it.  
If more than one image is provided, GeneXus will automatically identify wich image is necessary for each device.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

In order to apply the changes to this property a build of the main object is needed.

### [Compatibility](#Compatibility)

For knowledge bases migrated from older versions, the properties which are replaced by this one will be visible.

### [Scope](#Scope)

[Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817)

### [Notes](#Notes)

* For more information about images sizes and resolution please refer to:
  + [Human Interface Guideline - App Icon](https://developer.apple.com/design/human-interface-guidelines/ios/icons-and-images/app-icon/)
  + [Human Interface Guideline - Launch Image](https://developer.apple.com/design/human-interface-guidelines/ios/icons-and-images/launch-screen/)
