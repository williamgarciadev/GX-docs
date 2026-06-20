---
title: "Apple Launch Screen property"
source_id: 44952
source_url: https://wiki.genexus.com/commwiki/wiki?44952
genexus_version: "18"
---

# Apple Launch Screen property

Apple custom launch screen interface file (.storyboard). It is automatically generated if empty.

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

**Warning**: As of April 2020, all applications and application updates submitted to the Apple Store will be required to have a Launch Screen. More information at [Apple Requirements](https://wiki.genexus.com/commwiki/wiki?19478).

It allows attaching a .storyboard, which will be shown when the application is started and then will be replaced by the application once it has loaded all its startup data.

To learn more, read: [Apple - Launch Screen](<a data-saferedirecturl="https://www.google.com/url?q=https://developer.apple.com/design/human-interface-guidelines/launching%23Launch-screens&source=gmail&ust=1707483493844000&usg=AOvVaw2XYLI9f3qo51Lmjg7BJtSe" href="https://developer.apple.com/design/human-interface-guidelines/launching#Launch-screens" target="_blank">https://developer.apple.<wbr />com/design/human-interface-<wbr />guidelines/launching#Launch-<wbr />screens</a>)

If the property is empty (default value), a recommended .storyboard will be automatically created.

To create your own .storyboard, follow the steps in this documentation:  
[Apple - Understanding Auto Layout](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/index.html#//apple_ref/doc/uid/TP40010853-CH7-SW1)

**Note:** This property replaces the previous [iOS Launch Image property](https://wiki.genexus.com/commwiki/wiki?31375,,).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build All](https://wiki.genexus.com/commwiki/wiki?5691).
