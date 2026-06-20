---
title: "ApplicationBars Theme Class (GeneXus 18 Upgrade 6 or prior)"
source_id: 56454
source_url: https://wiki.genexus.com/commwiki/wiki?56454
genexus_version: "18"
---

# ApplicationBars Theme Class (GeneXus 18 Upgrade 6 or prior)

Every [Theme object](https://wiki.genexus.com/commwiki/wiki?16595) includes the ApplicationBars[Theme Class](https://wiki.genexus.com/commwiki/wiki?6246) to allow customizing the look & feel of the [Application Bar control in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?19486).  
  
`[imagen omitida: wiki id 56432]`

By setting the **ApplicationBars** Theme Class properties you can define the desired look & feel.

Remember that the **ApplicationBars** Theme Class is assigned to the [Application Bars Class property](https://wiki.genexus.com/commwiki/wiki?37518) of [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), and [Work With](https://wiki.genexus.com/commwiki/wiki?15974) objects.

### [Properties](#Properties)

* **Background Color** - Sets a color for the background of the Bar.
  + [On iOS 7](https://wiki.genexus.com/commwiki/wiki?23450,,), the background color has transparency by default. If you want no transparency, set the background color with alpha = 0.
* **Background Image** - Sets an image for the background of the Bar. See sample.
* **Status Bar Color** - Sets a color for the background of the Status Bar.
  + On Android 5 or greater, you can set the color for the status bar. The Material Design guidelines indicate that "toolbars and larger color blocks should use the primary 500 color, which should be the main color of your app. The status bar should be the darker 700 tint of your primary color".
  + On iOS this property is not taken into account.
* **Title Image** - Sets an image to show instead of the title.
* **Icon** - Sets an image of the icon shown at the left of the title (only Android). For newer Android versions, its use is not recommended (see Notes section for details).
* **Forecolor -** Sets a color for the title (if title image is not set).
* **Font** - Sets font properties for the title (if title image is not set).
* **Default Button Class** - Button class type that will be used for the buttons on the Application Bar.
* **Back Button Class** - Button class type that will be used for the back button.
* **Back Button Image** - Image that will be shown for the back button.
* **Back Button Text -** Text that will be shown where the back button appears (only Apple).

### [Samples](#Samples)

#### [Application Bars with BackgroundImage - iPhone](#Application+Bars+with+BackgroundImage+-+iPhone)

`[imagen omitida: wiki id 17890]`

#### [Application Bars with Backgroundcolor - Android](#Application+Bars+with+Backgroundcolor+-+Android)

`[imagen omitida: wiki id 17965]`

### [Standard Size for Android](#Standard+Size+for+Android)

Default: 48 dip  
Large portrait: 48 dip  
Large portrait mdpi: 56 dip  
Large landscape: 40 dip  
XLarge: 56 dip

For more information, click [here](http://developer.android.com/guide/practices/ui_guidelines/icon_design_action_bar.html).

### [Standard Size for iOS](#Standard+Size+for+iOS)

The largest size is 44 dip, except for iPhone landscape, which is 32 dip.  
Retina screens have double the pixels at 88 and 64, respectively.

For more information, click [here](http://developer.apple.com/library/ios/documentation/userexperience/conceptual/mobilehig/UIElementGuidelines/UIElementGuidelines.html#).

### [Availability](#Availability)

* Default Button Class property is available for iOS and Android as of [GeneXus X Evolution 2 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?22626,,).
* Back Button Class and Back Button Text properties are available for iOS as of [GeneXus Tilo Beta 2](https://wiki.genexus.com/commwiki/wiki?23074,,).

### [Android Limitations](#Android+Limitations)

* For the "Default Button Class", only the properties "Font Size" and "Forecolor" of the selected button class are taken.
* Back Button Image is available for Android as of [GeneXus 17 upgrade 4](https://wiki.genexus.com/commwiki/wiki?47936,,).

### [Tips](#Tips)

* On iOS, the text color of the [search box](https://wiki.genexus.com/commwiki/wiki?24805) icon for the grid control adopts the Forecolor when it is set at design time.  
  If the grid is at the top of the panel, it also adopts the background color, checking if the forecolor is dark (if not, it will be set as that).  
  Otherwise (the grid has other controls above it), it only adopts a minimalist light aspect, without a background color. In this scenario, if the forecolor of the Application Bar class is light, it will adopt it without checking if it is light or not. Maybe it is desirable to preserve the light title on the application bar, and to avoid the described behavior on the search box text, it is recommended to design two Application Bar classes: one for the text of the search box set at design time and another for the title of the application bar set at runtimethrough the ClientStart event. This action will force to adopt independent Theme Classes for the default search box control and the application bar.  
  On Android, the text color of the search box depends on the [Base Color Scheme property](https://wiki.genexus.com/commwiki/wiki?18402) value.

### [Notes](#Notes)

* The use of an icon on the application bar for Android apps is not recommended due to the introduction of [Material Design guidelines](https://wiki.genexus.com/commwiki/wiki?31004). The [developer guidelines](https://developer.android.com/reference/android/support/v7/widget/Toolbar.html) explicitly say:  
  "*In modern Android UIs developers should lean more on a visually distinct color scheme for toolbars than on their application icon. The use of application icon plus title as a standard layout is discouraged on API 21 devices and newer.*"
