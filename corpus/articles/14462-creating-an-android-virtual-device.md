---
title: "Creating an Android Virtual Device"
source_id: 14462
source_url: https://wiki.genexus.com/commwiki/wiki?14462
genexus_version: "18"
---

# Creating an Android Virtual Device

You do **not** have to create an Android Virtual Device ([AVD](https://wiki.genexus.com/commwiki/wiki?20431,,)) because GeneXus does it for you. By default, the first time GeneXus runs an Android application it tries to create an [AVD](https://wiki.genexus.com/commwiki/wiki?20431,,) called "*Genexus-API**X**-x86*" with the supported Android version, where **X** will be the number of the API version used (e.g. 24 for Android 7.0).

You may need to change the default AVD created by GeneXus if your application requires more/less memory, more storage, a different layout (e.g. tablet), etc. This article explains three alternatives to create your own AVD instances. Make sure to start the emulator with one of these new AVD **before** running the application from GeneXus, which automatically detects the AVD instance started (avoid starting multiple emulators). Refer to [Prototyping device selection - Android](https://wiki.genexus.com/commwiki/wiki?20441) for details.

In the following examples, an Android 7" Tablet will be created but feel free to add your customizations.

`[imagen omitida: wiki id 37535]`

### [Option 1: From avdmanager command-line tool](#Option+1%3A+From+avdmanager+command-line+tool)

1. Open Windows PowerShell or Command Prompt.
2. Open your Android SDK directory by using [cd command](https://en.wikipedia.org/wiki/Cd_(command)).

   ```
   > cd <my_android_sdk_directory>/tools/bin
   ```
3. Execute the avdmanager.bat tool with  [create avd command](https://developer.android.com/studio/command-line/avdmanager.html ) as follows.

   ```
   > C:\<my_android_sdk>\tools\bin\avdmanager create avd --name MyAndroidTablet 
                                               --packages "system-images;android-24;google_apis;x86" 
                                               --tag "google_apis" --abi "x86" --device "7in WSVGA (Tablet)"
   ```

   **Notes**:  
   -- name  
   Name of the new AVD.   
     
   -- packages, --tag, --abi   
   Must satisfy [Android Requirements](https://wiki.genexus.com/commwiki/wiki?14449) for your GeneXus installation.  
     
   -- device   
   The device name. Available devices can be listed by executing:   
   > C:\<my\_android\_sdk>\tools\bin\avdmanager list device
4. Run your new Android emulator by executing the [emulator program](https://developer.android.com/studio/run/emulator-commandline.html).

   ```
   > C:\<my_android_sdk>\tools\emulator -avd MyAndroidTablet
   ```
5. Done!

### [Option 2: From Android Studio](#Option+2%3A+From+Android+Studio)

1. Open Android Studio.  
   `[imagen omitida: wiki id 37537]`
2. Go to Tools > Android > AVD Manager.  
   `[imagen omitida: wiki id 37538]`
3. Click on the "Create Android Device.." button.  
   `[imagen omitida: wiki id 37539]`
4. Select which device you want to create (you can also customize, create new, or import one previously created).  
   As it was mentioned before, an 7" Android Tablet will be created:  
   `[imagen omitida: wiki id 37540]`
5. Select the system image. Must satisfy [Android Requirements](https://wiki.genexus.com/commwiki/wiki?14449) for your GeneXus Installation.  
   `[imagen omitida: wiki id 37541]`  
   Then, click on the "Next" button.
6. Select the name for your AVD and click on Finish.  
   `[imagen omitida: wiki id 37542]`
7. Finally, select the device previously created and click on the "Play" icon to launch it.  
   `[imagen omitida: wiki id 37543]`

### [Option 3: From AVD Manager program](#Option+3%3A+From+AVD+Manager+program)

**Warning**: These components are no longer available as of Android SDK 25.3.0.

1. Go to your [Android SDK directory](https://wiki.genexus.com/commwiki/wiki?36361) and open the Android Virtual Manager program (called *AVD Manager.exe)*. If you haven't installed the Android SDK, please follow [Android Requirements](https://wiki.genexus.com/commwiki/wiki?14449) to install it.
2. Click on the "Create..." button.  
   `[imagen omitida: wiki id 37531]`
3. Complete the options with your preferences, and click on the "OK" button.  
   Make sure that Target and CPU/ABI are under the scope of the [Android Requirements](https://wiki.genexus.com/commwiki/wiki?14449) for your GeneXus upgrade.  
   `[imagen omitida: wiki id 37532]`
4. On the AVD Manager, select your new emulator and click on the "Start..." button. In the new window displayed, click on "Launch".  
   `[imagen omitida: wiki id 37533]`  
   The new AVD will start.  
   `[imagen omitida: wiki id 37534]`
5. Done!

## [See also](#See+also)

* [Android Developer - avdmanager](https://developer.android.com/studio/command-line/avdmanager.html)
* [Android Developer - Start the Emulator from the Command Line](https://developer.android.com/studio/run/emulator-commandline.html)
* [Android Developer - Android Studio - Managing AVDs](https://developer.android.com/studio/run/managing-avds.html)


|  |
| --- |
| **Backlinks** |
| [Android Requirements](https://wiki.genexus.com/commwiki/wiki?14449) | [Android Requirements (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55100) | [Android Requirements (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?56500) |
| [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |

---
