---
title: "Framework template for iOS User Controls or External Objects"
source_id: 32508
source_url: https://wiki.genexus.com/commwiki/wiki?32508
genexus_version: "18"
---

# Framework template for iOS User Controls or External Objects

## [Introduction](#Introduction)

When developing a User Control or External Object for any of the Apple platforms (iOS, AppleWatch or AppleTV), you may find it helpful to start off with an Xcode template.

Such Xcode template is provided by the [GeneXus SDK](https://wiki.genexus.com/commwiki/wiki?27521,,). Install de SDK, and then search for the XcodeTemplates folder under the installation directory.

## [Installing the template](#Installing+the+template)

To install de template, copy the XcodeTemplates folder from the GeneXus SDK installation directory anywhere in your Mac computer, and run the script installTemplates.sh under xcTemplates from a Terminal.app.

To check if the install succeded, go to Xcode, File > New > Proyect..., select Cross-platfotm, and under GeneXus you should see a GX Framework option.

`[imagen omitida: wiki id 32534]`

## [Configuring Xcode](#Configuring+Xcode)

### [Define GXSDK global variable](#Define+GXSDK+global+variable)

You need to define a GXSDK global variable in Xcode, pointing to the path where the GeneXus Frameworks are located (typically /Users/<user\_name>/Library/GeneXus/GeneXus/<gx\_version\_number>).

To do that, go to Xcode > Preferences... > Locations > Custom Paths(\*) and add the GXSDK path.

`[imagen omitida: wiki id 32536]`

`[imagen omitida: wiki id 32537]`

(\*) Note: *Custom Paths* option was named *Source Trees* in Xcode 7.

## [Creating the project](#Creating+the+project)

When you select the GX Framework option from the New Project dialog in Xcode, the following dialog is presented.

`[imagen omitida: wiki id 32538]`

Here you have to configure:

* **Product Name**: the name of your User Control or External Object
* **Language**: you may choose Swift or Objective-C
* **Copy config files**: if checked (default value), the .xcconfig files will be copied to the project's directory. If you uncheck this option, the files will be referenced from their original location.
* **Allow app extension API only**: if checked (default value), only extensions-enabled options will be available. You shoud probably not change this value, since using other APIs may result in your extension being incompatible with GeneXus apps.
* **Use shared umbrella header**: if checked (default value), only one header file will be created for all the supported platforms (iOS, watchOS & tvOS). Otherwise, an individual header will be created for each platform.

## [Implement your User Control or External Object](#Implement+your+User+Control+or+External+Object)

Now you need to add the implementation of your extension by subclassing the appropiate base clases. You may refer to [Creating User Controls for Apple](https://wiki.genexus.com/commwiki/wiki?18330) and [External Object for iOS Devices](https://wiki.genexus.com/commwiki/wiki?18072) for more information.

## [Build and deploy](#Build+and+deploy)

When you build your Xcode project, a framework is created. Frameworks are special folders in OS X where the implementation of the component is stored, along with all the necessary resources. If you want to learn more about frameworks, you can read all about them in Apple's [Introduction to Framework Programming Guide](https://developer.apple.com/library/content/documentation/MacOSX/Conceptual/BPFrameworks/Frameworks.html#//apple_ref/doc/uid/10000183i).

You need to build both the device and simulator instances of the framework. To do that, in Xcode select a simulator from the Schemes dropdown and build, then select a device and build again.

After that is done, you need to find the ***build*** folder in Finder. The easiest way of doing that is right-clicking the project in Xcode and then selecting Show in Finder.

The ***build*** folder will contain two additional folders: ***Debug-iphonesimulator*** and ***Debug-iphoneos***. Both subfolders contain a .framework with the implementation for each platform. You'll need to zip both frameworks, as both of them are needed.

### [User Controls](#User+Controls)

For User Controls, you'll have a .control file that you need to modify in order to use the frameworks previously created.

Add the following to your .control file:

```
<iOS_SupportFiles>
        <File>iphoneos\MyUserControl.framework.gxzip</File>
        <File>iphonesimulator\MyUserControl.framework.gxzip</File>
</iOS_SupportFiles>
<iOS_ReferencedFiles>
        <File embed="true">./UserControls/$(PLATFORM_NAME)/MyUserControl.framework</File>
</iOS_ReferencedFiles>
```

where *MyUserControl* is the name of the user control

### [External Objects](#External+Objects)

For External Objects, an [Extension Library](https://wiki.genexus.com/commwiki/wiki?33545) is needed to deploy them automatically. That is, to include the External Object's implementation in the Xcode project each time the developer performs a Build in GeneXus.

Extension Libraries are available for iOS since [GeneXus 15 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?35908,,).


|  |
| --- |
| **Backlinks** |
| [BlurredImage: sample User Control for iOS](https://wiki.genexus.com/commwiki/wiki?32558) | [Creating User Controls for Apple](https://wiki.genexus.com/commwiki/wiki?18330) | [External Object for iOS Devices](https://wiki.genexus.com/commwiki/wiki?18072) |
| [HowTo: Migrate an External Object for iOS from Evolution 3 to GeneXus 15](https://wiki.genexus.com/commwiki/wiki?33805) |

---
