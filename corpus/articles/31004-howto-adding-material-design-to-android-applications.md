---
title: "HowTo: Adding Material Design to Android applications"
source_id: 31004
source_url: https://wiki.genexus.com/commwiki/wiki?31004
genexus_version: "18"
---

# HowTo: Adding Material Design to Android applications

Due to the diversity offered by the Android platform, it is challenging to design applications that fit a particular ecosystem. To this end, GeneXus15 incorporates features in the [Android Generator](https://wiki.genexus.com/commwiki/wiki?14453) to help developers follow [Material Design](http://www.google.com/design/spec/material-design/introduction.html) guidelines. This Android offering allows developers to customize the *Look & Feel* of applications as from version 5 of this platform (*a.k.a* Lollipop) and make them more user-friendly with an optimized UX.

These functionalities are offered by GeneXus in two ways: *customizable through properties* and *provided by default.*

For this purpose, the [Sales](https://wiki.genexus.com/commwiki/wiki?23672) sample will be used to explain and show all of them, making a comparison of the results using GeneXus X.

`[imagen omitida: wiki id 31135]`

## [Customizable through properties](#Customizable+through+properties)

A set of properties helps developers meet all the aesthetic requirements of their application, such as colors and shadows.

### [1) General appearance](#1%29+General+appearance)

When designing an application, a developer usually wants to set certain colors in some sections of the application and keep them unchanged.  
To this end, seven properties are provided under the [Application Colors](https://wiki.genexus.com/commwiki/wiki?28621) group that helps them achieve that goal.

#### [Editable fields](#Editable+fields)

Three properties specially devoted to customizing the color aspect of those fields by entering data from the device to the central system.

`[imagen omitida: wiki id 31150]`

Also, to follow the standards, their appearance has been improved. Note how text fields are shown as a floating line, instead the traditional one.  
Similar changes are applied to other controls, such as check box, radio-button, etc.

#### [Action bar](#Action+bar)

The upper section is the most important design element of any application. Its visual appeal can determine if the end user feels comfortable with the developed system, and whether he/she will continue to use it.  
The *Primary Color property* helps developers to define the main color of the application that identifies their brand and, together with the *Primary Color Dark property,* it is enough to determine the general color aspect of the entire application.  
According to the guidelines, this color must be 700 tints darker than the primary one.

`[imagen omitida: wiki id 31132]`

In addition, the color of the icons embedded in the application bar can be customized through the *Action Tint property.*This color should be lighter than the primary color, for developers to easily ensure color harmony for the application.

#### [Activation signals](#Activation+signals)

A single property allows developers to change the color of those controls when enabled by the end user (e.g. a tap on a button or a text confirm in a modal window). This behavior was provided by default in Android 4 operating system (or previous versions), in order to break the application's color harmony. As from Android 5, these controls can be customized.

`[imagen omitida: wiki id 31133]`

### [2) Status bar color](#2%29+Status+bar+color)

Even though the status bar color can be statically set using the described *primary color dark* property (under [Application Colors group](https://wiki.genexus.com/commwiki/wiki?28621)), it may be desirable to change it dynamically under certain conditions (e.g. depending on the panel viewed or some events activated by the end user). To do this, a new property for Themes has been added under [Application Bars class](https://wiki.genexus.com/commwiki/wiki?17879) named *Status Bar color*. This allows developers to dynamically change the class associated with the application bar (including the status bar) just by assigning it when certain conditions are satisfied - e.g. depending on the panel viewed.

A possible usage could be to hide the application bar when the end user swipes up on the screen and contrast the status bar against the background. When the end user swipes down, it makes it appear normally.

`[imagen omitida: wiki id 31137]`

Note how the status bar changes its color in response to the event. This means that the *Primary Color Dark* *property*will not take effect if the *Status Bar color property* is set.

### [3) Elevation](#3%29+Elevation)

A simple action powered by Android adds shadows to individual controls and gives the end user the impression that some controls are stacked onto others (and consequently, more or less relevant) depending on their functionality. To simplify the task for developers, GeneXus has incorporated the [Elevation property](https://wiki.genexus.com/commwiki/wiki?28180) for some controls under its corresponding themes class to give this effect.

Note how the table that represents a product item casts a shadow, as does the button embedded in it. This indicates end users that there is an item with a clickable button on it.

`[imagen omitida: wiki id 31138]`

This concept may be familiar to those developers who use [ZOrder property](https://wiki.genexus.com/commwiki/wiki?22510) for [Canvas](https://wiki.genexus.com/commwiki/wiki?22452) to add this overlay effect on the application's controls.  
Both properties can be considered siblings and they are usually used together. While Elevation casts shadows, ZOrder allows developers to set which control belongs to a particular tier when two (or more) controls have the same elevation.

### [4) Tab strip customization](#4%29+Tab+strip+customization)

In previous versions of GeneXus, this customization of the [tab strip](https://wiki.genexus.com/commwiki/wiki?31145,,) was limited to [Tab page classes](https://wiki.genexus.com/commwiki/wiki?25638) that are not designed to follow the Material Design guidelines. Since [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?28265,,), developers only need to set three properties.

`[imagen omitida: wiki id 31148]`

## [Provided by default](#Provided+by+default)

This is a set of effects whose behavior is based on customizable properties.

### [1) Touch ripples](#1%29+Touch+ripples)

Sometimes it is tough for end users to notice when a tappable gesture on their devices has taken effect. Touch Ripples is a simple visual effect offered by Android to notify end users that the device has interpreted their requests successfully. When the end user taps on a control that has an event associated with it, a highlighted circle will be expanded from the touch point to the control borders, filling it completely and finally triggering its event.

`[imagen omitida: wiki id 31139]`

### [2) Task color](#2%29+Task+color)

As is well known, Android devices provide three physical/capacitive buttons, each one dedicated to a particular action. The *Home* and *Back* buttons are self-explanatory, but the third button always creates controversy. Most people often call it *Overview,*  as it allows end users to view quickly which applications were closed recently and, optionally, restore them to continue using them.  
As from Android Lollipop, the task list is shown as mobile Chrome's tab switcher, using a cascade of an overlapping task with full-screen thumbnails, colored top bar, its icon, and label. With GeneXus, the *Task color* of the application in the overview will match the [Application Bar](https://wiki.genexus.com/commwiki/wiki?17879) background color that the developer has set.

`[imagen omitida: wiki id 31140]`

### [3) Slide menu](#3%29+Slide+menu)

When the [Navigation Style](https://wiki.genexus.com/commwiki/wiki?16229) is Slide, the left drawer automatically set its size following the guidelines and leaves a shadow in the right section when to display it.  
Also, if [Header Row](https://wiki.genexus.com/commwiki/wiki?29843) is enabled, the drawer reaches the status bar preserving its opacity.

`[imagen omitida: wiki id 31557]`

## [Scope](#Scope)

**Languages:** .NET, Java

**SD Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453)

## [Availability](#Availability)

This property is available since[GeneXus 15](https://wiki.genexus.com/commwiki/wiki?28265,,)


|  |
| --- |
| **Backlinks** |
| [ApplicationBars Theme Class](https://wiki.genexus.com/commwiki/wiki?17879) | [ApplicationBars Theme Class (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?56454) | [DateTime picker for Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?34167) |
| [gx-elevation property](https://wiki.genexus.com/commwiki/wiki?28180) |

---
