---
title: "Android Requirements (GeneXus 18 Upgrade 13 or prior)"
source_id: 60679
source_url: https://wiki.genexus.com/commwiki/wiki?60679
genexus_version: "18"
---

# Android Requirements (GeneXus 18 Upgrade 13 or prior)

This article describes the requirements for developing Android applications with GeneXus, as well as the requirements of the target devices.

**Note:** Requirements vary if you want to prototype using [GeneXus Project Navigator](https://wiki.genexus.com/commwiki/wiki?14974) or compile your app.

### [Requirements for developing an Android application](#Requirements+for+developing+an+Android+application)

#### [Automatic Installation (Recommended)](#Automatic+Installation+%28Recommended%29)

A setup that automatically downloads and installs all Android SDK requirements is provided. Note that you'll also be able to access this setup through the [Update Android SDK tool](https://wiki.genexus.com/commwiki/wiki?35473) menu option from the GeneXus IDE.

|  |
| --- |
|  |
| Download the [Android Requirements Installer](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?35474,,) |

#### [Manual Installation](#Manual+Installation)

It is not recommended to install the Android SDK components manually, but in some cases, it may be necessary. That's why the information you will need to do it is provided below.

#### [**Step 1** - Installing external software](#Step+1+-+Installing+external+software)

* [Oracle JDK](http://www.oracle.com/technetwork/java/javase/downloads/index.html) version 17 or [Open JDK 17](https://jdk.java.net/java-se-ri/17) (Use the 64-bit version if you are on a 64-bit operating system).
* [**Android SDK**](https://dl.google.com/android/repository/tools_r25.2.3-windows.zip) — Only the **command line tools** are needed.

**Note:** It is strongly recommended to install the Android SDK (in any directory) with *no blank spaces* or *any special characters.*

#### [**Step 2** - Installing Android components](#Step+2+-+Installing+Android+components)

**Note**: Starting August 31, 2024, all applications to be uploaded to Google Play must target Android 14 (API level 34). This implies that you must update your development environment to GeneXus 18 Upgrade 7, at a minimum. [SAC # 53749](https://www.genexus.com/en/developers/websac?data=53749;;), Target API level requirements for Google Play apps.

#### [Detailed list of the requirements of the Development Environment](#Detailed+list+of+the+requirements+of+the+Development+Environment)

The necessary components are available on the [Android Developer website](https://developer.android.com/).

| **Component** | **Required Version** | Comments |
| --- | --- | --- |
| Android SDK Platform-Tools | 35.0.2 or higher | - |
| Android SDK Build-tools | 35.0.0 exactly | - |
| Android Emulator | 35.2.10 or higher | - |
| Android 15(API 35) | Any | - |
| - SDK Platform | 35.0.0 or higher | - |

#### 

#### [**Step 3** - Define virtualization accelerators](#Step+3+-+Define+virtualization+accelerators)

Once you have finished installing the requirements, you must define a suitable virtualization accelerator.

Depending on your computer, you can choose one of the following virtualization accelerators:

* Windows Hypervisor Platform (WHPX)
* Android Emulator hypervisor driver (AEHD)

These virtualization accelerators will optimize performance and efficiency when running the x86 Emulator.

If possible, you should use WHPX.

When using WHPX:

* You must check that Intel VT-x (Virtualization) is enabled in your BIOS. Detailed information about how to **enable VT-x from the BIOS** can be found on [this post](http://stackoverflow.com/a/39542918) and [this one](https://github.com/intel/haxm/wiki/Installation-Instructions-on-Windows#troubleshooting) for troubleshooting.
* The following Windows features must be turned on:
  + **Hyper-V**
  + **Windows Hypervisor Platform**

To check if they are enabled, open *Control Panel > Programs > Turn Windows features on,* and then, in the pop-up windows, make sure that the corresponding checkboxes are selected.

 You can read about how to use WHPX in <https://developer.android.com/studio/run/emulator-acceleration#vm-windows-whpx>.

### [Supported OS versions by the generated applications](#Supported+OS+versions+by+the+generated+applications)

* The generated Android application works on devices with API 24 (Android 7.0) or higher.
* There is no "maximum" OS version supported for a given GeneXus upgrade. The generated applications will still work in OS versions released after the release of the GeneXus upgrade. However, the new features of these later OS versions will require a new GeneXus upgrade release to be fully supported.

### [Tips](#Tips)

* The GeneXus setup program searches for the Android SDK version in the Windows registry key *"HKEY\_LOCAL\_MACHINE\SOFTWARE\Wow6432Node\Android SDK Tools"* for 64-bit Windows and in *"HKEY\_LOCAL\_MACHINE\SOFTWARE\Android SDK Tools"* for 32-bit Windows.
* Once the SDK Directory is found, it searches the file "*<Android\_SDK\_Installation\_Directory>\tools\source.properties"* to check that the property *"Pkg.Revision="* is 23.0.2.

### [Notes](#Notes)

* If you are using **Parallels** to run GeneXus in a Windows VM, **do NOT** place the Android SDK you use on your host machine or in your model directory. The Android Gradle Plugin does not support this, and it may lead to strange behavior while compiling (for example, your computer could stop working).
* [Solutions for the case that a 404 or 500.19 error occurs](https://wiki.genexus.com/commwiki/wiki?18398).

### [Hardware Requirements](#Hardware+Requirements)

As stated above, Android SDK requires at least 3GB of free space on your disk.

Approximately 2 GB of RAM are required by default for compilation; this value can be changed in the [Android specific properties](https://wiki.genexus.com/commwiki/wiki?31449).

### [Offline Compilation](#Offline+Compilation)

The compilation process uses the Gradle build system, which needs network connectivity to download dependencies. If your environment does not have network connectivity, the build will cancel with an error similar to the following:

```
error: FAILURE: Build failed with an exception.
error:
error: * What went wrong:
error: A problem occurred configuring root project 'Android'.
error: > Could not resolve all artifacts for configuration ':classpath'.
error: > Could not resolve com.android.tools.build:gradle:3.4.1.
error: Required by:
error: project :
error: > Could not resolve com.android.tools.build:gradle:3.4.1.
error: > Could not get resource 'https://dl.google.com/dl/android/maven2/com/android/tools/
build/gradle/3.4.1/gradle-3.4.1.pom'.
error: > Could not GET 'https://dl.google.com/dl/android/maven2/com/android/tools/build/
gradle/3.4.1/gradle-3.4.1.pom'.
```

You can add the Gradle *--offline* option to the [Gradle Options property for Android Generator](https://wiki.genexus.com/commwiki/wiki?36363) to force Gradle to work offline and not download any dependency. You will need to previously download all the dependencies needed and update the GeneXus installation; follow the steps detailed in [SAC #47748](https://www.genexus.com/developers/websac?es,,,47748).

## [See Also](#See+Also)

[Android SDK installer](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?35474,,)  
[Update Android SDK tool](https://wiki.genexus.com/commwiki/wiki?35473)  
[Creating an Android Virtual Device](https://wiki.genexus.com/commwiki/wiki?14462)  
[Android - FAQ and Common Issues](https://wiki.genexus.com/commwiki/wiki?14575)
