---
title: "Android Requirements (GeneXus 18 Upgrade 3 or prior)"
source_id: 55100
source_url: https://wiki.genexus.com/commwiki/wiki?55100
genexus_version: "18"
---

# Android Requirements (GeneXus 18 Upgrade 3 or prior)

This article details the requirements for developing Android applications with GeneXus and also the requirements of the target devices.

* [Automatic Installation (Recommended)](#Automatic+Installation+%28Recommended%29)
* [Manual Installation](#Manual+Installation)

+ [**Step 1** - Installing external software](#Step+1+-+Installing+external+software)
+ [**Step 2** - Installing Android components](#Step+2+-+Installing+Android+components)

- [Detailed list with the requirements of the Development Environment](#Detailed+list+with+the+requirements+of+the+Development+Environment)

+ [**Step 3** - Installing HAXM](#Step+3+-+Installing+HAXM)

* [Supported OS versions by the generated applications](#Supported+OS+versions+by+the+generated+applications)
* [Tips](#Tips)
* [Notes](#Notes)
* [Hardware Requirements](#Hardware+Requirements)
* [Offline Compilation](#Offline+Compilation)
* [See Also](#See+Also)

## [Automatic Installation (Recommended)](#Automatic+Installation+%28Recommended%29)

We provide a setup that automatically downloads and installs all Android SDK requirements. Note that you'll also be able to access this setup through the [Update Android SDK tool](https://wiki.genexus.com/commwiki/wiki?35473) menu option from Genexus IDE.

|  |
| --- |
|  |
| **Download the [Android Requirements Installer](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?35474,,)** |

## [Manual Installation](#Manual+Installation)

We discourage installing the Android SDK components manually, but it some cases it may be necessary. So we provide you with the information you'll need to do it.

### [**Step 1** - Installing external software](#Step+1+-+Installing+external+software)

* [Oracle JDK](http://www.oracle.com/technetwork/java/javase/downloads/index.html)  version 11 or [Open JDK 11](https://jdk.java.net/java-se-ri/11)  (Use the 64-bit version if you are on a 64-bit operating system).
* [**Android SDK**](https://dl.google.com/android/repository/tools_r25.2.3-windows.zip) — Only the **command line tools** are needed.

Note: It is strongly recommended to install the Android SDK (in any directory) with *no blank spaces* or *any special characters*

### [**Step 2** - Installing Android components](#Step+2+-+Installing+Android+components)

**Note**: Google Play requires that new apps target at least Android 12 (API level 31) from August 2022, and that app updates target Android 12 from November 2022. This implies that you must use [GeneXus 17 upgrade 7](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?49301,,) or higher to be able to deploy to Google Play. More information in [Play Console Help](https://support.google.com/googleplay/android-developer/answer/11926878) answer.

#### [Detailed list with the requirements of the Development Environment](#Detailed+list+with+the+requirements+of+the+Development+Environment)

| **GeneXus 18 or higher users.** | | |
| --- | --- | --- |
| **Component** | **Required Version** | Comments |
| Android SDK Tools | 26.1.1 or higher | Refer to [Update Android SDK tool](https://wiki.genexus.com/commwiki/wiki?35473) option. |
| Android SDK Platform-Tools | 31.0.3 or higher | - |
| Android SDK Build-tools | 33.0.0 exactly | - |
| Android Emulator | 30.7.3 | - |
| Android 13(API 33) | Any | - |
| - SDK Platform | 31.0.3 or higher | - |
| Android Support Repository | 45 or higher | - |
| Google Repository | 44 or higher | - |

### [**Step 3** - Installing HAXM](#Step+3+-+Installing+HAXM)

This step is only necessary if your computer has an Intel-based CPU.

Once you have finished downloading the requirements, you must install HAXM. Then, open the <Android\_SDK\_Installation\_Directory>/Extras/Intel/Hardware\_Acelerated\_Execution\_Manager directory, execute the *intelhaxm-android.exe* installer, and follow its instructions.

`[imagen omitida: wiki id 31712]`

With this configuration, you can run Android applications on your device (if it is plugged into your computer).

HAXM only works in Intel processors if the Hyper-V feature of Windows platform is turned off and VT-x is enabled in your BIOS.

* In order to check if Hyper-V is disabled, open *Control Panel > Programs > Turn Windows features on or off,* and then, in the pop-up windows, make sure that **Hyper-V** is **not** checked.
* Detailed information about how to **enable VT-x from the BIOS** can be found on [this post](http://stackoverflow.com/a/39542918) and [this one](https://github.com/intel/haxm/wiki/Installation-Instructions-on-Windows#troubleshooting) for troubleshooting.
* In case of Windows 11, the features **Windows Hypervisor Platform** and **Virtual Machine Platform** should also turned off.

## [Supported OS versions by the generated applications](#Supported+OS+versions+by+the+generated+applications)

* The generated Android application works in devices with API 21 (Android 5.0, Lollipop) or higher
* There is no "maximum" OS version supported for a given GeneXus upgrade. Generated applications will still function in OS versions released after the release of the GeneXus upgrade. However, new features of these newer OS versions will require a new GeneXus upgrade release to be fully supported.

## [Tips](#Tips)

* The GeneXus setup program searches for the Android SDK version in the Windows registry key *"HKEY\_LOCAL\_MACHINE\SOFTWARE\Wow6432Node\Android SDK Tools"* for 64 bits Windows and in *"HKEY\_LOCAL\_MACHINE\SOFTWARE\Android SDK Tools"* for 32 bits Windows.
* Once the SDK Directory is found it searches the file "*<Android\_SDK\_Installation\_Directory>\tools\source.properties"* to check that the property *"Pkg.Revision="* is 23.0.2

## [Notes](#Notes)

* If you are using an [Intel processor](http://www.cpuid.com/softwares/cpu-z.html) and the HAXM installer produces the following error:  
  `[imagen omitida: wiki id 31576]`.  
  You must check that VT-x (Virtualization) is enabled in your BIOS and that you haven't installed HyperV.
* If you are using **Parallels** to run Genexus in a Windows VM, **do NOT** place the Android SDK you use on your host machine or in your model directory. The Android Gradle Plugin does not support this, and it may lead to strange behavior while compiling (for example, your computer could stop working).
* [Solutions for the case that a 404 or 500.19 error occurs](https://wiki.genexus.com/commwiki/wiki?18398).

## [Hardware Requirements](#Hardware+Requirements)

As stated above, Android SDK requires at least 3GB of free space on your disk.

2 GB of RAM are required by default for compilation approx; this value can be changed in the [Android specific properties](https://wiki.genexus.com/commwiki/wiki?31449).

## [Offline Compilation](#Offline+Compilation)

The compilation process uses the Gradle build system which needs network connectivity to download dependencies. If your environment does not have network connectivity the build will cancel with an error similar to the following:

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

You can add the gradle *--offline* option to the [Gradle Options property for Android Generator](https://wiki.genexus.com/commwiki/wiki?36363) to force gradle to work offline and do not download any dependency. You will need to previously download all the dependencies needed and update the GeneXus installation; follow the steps detailed in [SAC #47748](https://www.genexus.com/developers/websac?es,,,47748).

## [See Also](#See+Also)

* [Android SDK installer](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?35474,,)
* [Update Android SDK tool](https://wiki.genexus.com/commwiki/wiki?35473)
* [Creating an Android Virtual Device](https://wiki.genexus.com/commwiki/wiki?14462)
* [Android - FAQ and Common Issues](https://wiki.genexus.com/commwiki/wiki?14575)
