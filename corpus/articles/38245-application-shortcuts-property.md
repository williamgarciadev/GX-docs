---
title: "Application Shortcuts property"
source_id: 38245
source_url: https://wiki.genexus.com/commwiki/wiki?38245
genexus_version: "18"
---

# Application Shortcuts property

Specifies user-initiated actions for the application.

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

The *Application Shortcuts property* is available under the [Main object properties](https://wiki.genexus.com/commwiki/wiki?17817).

With this property, you can define some actions that can be triggered directly from the home screen by the end user. Some use cases of shortcut actions are listed below. There can be many more depending on your application needs.

* **Email:** *New email, Inbox, Search email*
* **Camera:** *Take selfie, Record video*
* **Maps:***Take me home*, *Share location*, *Search nearby*, *Request service at my location*
* *etc...*

In GeneXus, simply create a [Menu object](https://wiki.genexus.com/commwiki/wiki?16321) whose items will be the actions displayed in the shortcut widget. Also, you can associate an icon with each action by using the [Image property](https://wiki.genexus.com/commwiki/wiki?9846) of the Action node, and change its label through its [Description property](https://wiki.genexus.com/commwiki/wiki?7446).

The icon defined in the [Image property](https://wiki.genexus.com/commwiki/wiki?9846) can be set by using:

1. **Predefined icons**  
   Each platform has a predefined list of icons. For using them, you must add the "*gx*" prefix to the system icon name in the [Image property](https://wiki.genexus.com/commwiki/wiki?9846). That is:  
   [iOS icon](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticontype) (e.g. *gx**Location**\_TakeMeHome*).
2. **Custom icons**  
   Simply add an [Image object](https://wiki.genexus.com/commwiki/wiki?23387) to the Knowledge Base, and reference it from the [Image property](https://wiki.genexus.com/commwiki/wiki?9846). Remember that the icon will not be displayed with colors.

Finally, set in the *Application Shortcut property* the [Menu object](https://wiki.genexus.com/commwiki/wiki?16321) previously created. In iOS devices, the actions available are displayed when the end user uses [3D Touch](https://developer.apple.com/ios/3d-touch/) (applying pressure on the screen when selecting the application icon).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [Samples](#Samples)

First, create a [Menu object](https://wiki.genexus.com/commwiki/wiki?16321) and define your application shortcuts. In this case, you will create four actions: *play a new game*, *view the user profile*, *display the user playlist*, and *go to the chatroom*.  
`[imagen omitida: wiki id 38248]`

Next, associate a custom icon with each action and customize its description. For instance, in the *PanelChat* action, change the Image and Description properties as follows:  
`[imagen omitida: wiki id 38249]`

Finally, set the MenuShortcut object (previously created) in the Application Shortcuts property of our Main object. `[imagen omitida: wiki id 38250]`

At runtime, the end user will be able to display every action you have defined and select any of them to open it.  
`[imagen omitida: wiki id 38252]`

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770). |

### [Compatibility](#Compatibility)

Available for Android as of Genexus 17 upgrade 3.
Available for Apple as of Genexus 15 upgrade 10.

### [See Also](#See+Also)

* [Menu object](https://wiki.genexus.com/commwiki/wiki?16321)
* [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817)
* [Apple Developers - Home Screen Quick Actions](https://developer.apple.com/ios/human-interface-guidelines/extensions/home-screen-actions/)
* [Apple Developers - UIApplicationShortcutIconType](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticontype)
