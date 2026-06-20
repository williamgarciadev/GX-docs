---
title: "Font Category property"
source_id: 27784
source_url: https://wiki.genexus.com/commwiki/wiki?27784
genexus_version: "18"
---

# Font Category property

Applies automatic adjustments to letter spacing and line height for every font size, the ability to specify text style semantically such as Body, Footnote, etc. and text that responds appropriately when user change their preferred text size settings.

### [Values](#Values)

|  |  |
| --- | --- |
|  | Empty value (default). |
| **Body** | Used for general text. |
| **Caption1** | Used for standard titles. |
| **Caption2** | Used for alternative titles. |
| **Footnote** | Used for notes. |
| **Headline** | Used for heading texts. |
| **Subheadline** | Used for subtitles. |

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Level:** [Theme Class](https://wiki.genexus.com/commwiki/wiki?6246)

### [Description](#Description)

The main scenario for this feature is a simple way to have readable text.

### [A simple way to have readable text](#A+simple+way+to+have+readable+text)

To allow this the OS:

* Makes automatic adjustments to letter spacing and line height for every font size.
* Has the ability to specify text style semantically such as Body, Footnote, etc.

### [In GeneXus](#In+GeneXus)

To handle this in GeneXus, the Font Category property was implemented within the properties group 'Font' of the classes in the [Themes for Smart Devices](https://wiki.genexus.com/commwiki/wiki?16595).

This property gives the fonts semantics regarding the intent with which it will be used and then, on this basis, to calculate the default values of the existing properties (Font Weight, Font Size, etc) and set the font properties that are not configurable from GeneXus (letter spacing or line height for example), or the properties configurable at runtime by the user of the device (Text Size).

For example, when Font Category property uses one of this values and:

* Font Size property is empty or 0dip, then it will take the value corresponding to the selected category and the size that the user has configured on his device. Note that 0dip may be useful to override an inherited value of another parent class.
* Font Weight and Font Style properties are empty, Normal/Bold and Normal/Italic will be used respectively for Font Weight and Font Style based on the selected category.

### [Notes](#Notes)

* As of [GeneXus 15 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?36355,,) when Font Size property is set and the font family is a custom font, an application running on iOS 11 or higher will take its value as a base according to user font size preference (instead of predefined font size). For example, if Font Size property = 20, every option of Font Category property will be adjusted from that value (i.e. 20).   
  For iOS applications, it is recommended to keep Font Size property as empty for built-in fonts (managed by the OS) and specify a base font size for custom fonts.

### [Availability](#Availability)

Font Category property is available as from

* [GeneXus X Evolution 2 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?22626,,) for iOS
* [GeneXus X Evolution 3 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?27678,,) for Android

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Run the main object.


|  |
| --- |
| **Backlinks** |
| [Attribute theme-class](https://wiki.genexus.com/commwiki/wiki?37646) | [Button theme-class for Smart Devices](https://wiki.genexus.com/commwiki/wiki?37647) |

---
