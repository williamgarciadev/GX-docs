---
title: "HowTo: Embedding YouTube videos in an Android application"
source_id: 21923
source_url: https://wiki.genexus.com/commwiki/wiki?21923
genexus_version: "18"
---

# HowTo: Embedding YouTube videos in an Android application

Sometimes it is more comfortable for users to display videos inside the application instead of launching another app to play the video.  
To do so, the Android generator uses the native [YouTube Android Player API](https://developers.google.com/youtube/android/player/) to display embedded YouTube videos in your application.

This article shows an example of how to use this feature and explains some facts about it.

### [Step 1: Getting the developer key](#Step+1%3A+Getting+the+developer+key)

The application developer must obtain a **developer key** by [registering the app](https://developers.google.com/youtube/android/player/register).  
This key is **required** to be able to use the YouTube control on Android.

### [Step 2: Create the Transaction object](#Step+2%3A+Create+the+Transaction+object)

Create a simple [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) with an Attribute of type [Video](https://wiki.genexus.com/commwiki/wiki?16608), as shown in the image.  
In this example, we named the transaction as "Tx" (general purpose).

`[imagen omitida: wiki id 35345]`

### [Step 3: Create the panels of the application](#Step+3%3A+Create+the+panels+of+the+application)

Apply the [Work With pattern for Smart Devices](https://wiki.genexus.com/commwiki/wiki?15975) on the Tx transaction object.  
Then, in the WWSD object, set its *Main program property* to True.

### [Step 4: Setting some properties](#Step+4%3A+Setting+some+properties)

Now it's time to add the developer key.

For this, select the WWSD object declared as "main". Then, navigate through the tree properties to *Main Object Properties > Android* and look for **Android YouTube API Key property**to set its value with your key (obtained in step 1).  
Schematically:

`[imagen omitida: wiki id 35344]`

### [Step 5: Modifying layouts](#Step+5%3A+Modifying+layouts)

Make sure to **set an appropriate height** for the control.

Do this by using the **Rows style property** of the Section(General) level table in the *WorkWithDevicesTx object*.  
As shown below, we do this by choosing the percentage option.  
Also, keep in mind that it's not possible to play videos if YouTube control's height is larger than the actual layout area's height. This may happen if the layout has a scroll, and the video height is bigger than the exact layout height.  
  
**Important Note**: As the Android YouTube Player API reference says:

> *"While videos are playing, this View has a **minimum size of 200x110 dp**. If you make the view any smaller, videos will automatically stop playing."*

This means your video control needs to have that minimum size to be able to play YouTube videos. (In some cases that you have the video inside a table or grid, you need even more width for it to work correctly, for example, 500dpx110dp.

### [Step 6: Adding Youtube videos](#Step+6%3A+Adding+Youtube+videos)

Finally, launch the [Developer Menu](https://wiki.genexus.com/commwiki/wiki?18484) and go to the Tx transaction link (it can be used in mobile browsers taking advantage of RWD - Responsive Web Design).  
After that, you can add Youtube videos by setting the URL link in the UserVideo attribute and confirming the data.

`[imagen omitida: wiki id 32679]`

### [Step 7: Done!](#Step+7%3A+Done%21)

Run the *WorkWithDevicesTx object* and check out your application on an Android device.  
You can see the embedded videos getting the detail of a record by tapping on a row.

### [Snapshots](#Snapshots)

`[imagen omitida: wiki id 32680]`

### [Notes](#Notes)

* The device must have installed a Youtube application.
* This feature supports *start time* through two possibilities indicated in the URL:
  + For common and short links using **"t" string query** with start-time in Hours/Minutes/Seconds  
    Example: http://www.youtube.com/watch?v=*<video\_ID>*&**t=*<Hours>h<Minutes>m<Seconds>s***
  + For embed links using **"start" string query** with the start-time in seconds  
    Example: http://www.youtube.com/**embed**/*<video\_ID>?***start=*<Seconds>***
* It can only display one Youtube Player for each panel.

### [Availability](#Availability)

From version [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?30062,,)

### [See also](#See+also)

* [Video data type](https://wiki.genexus.com/commwiki/wiki?16608)
* [Developer Menu](https://wiki.genexus.com/commwiki/wiki?18484)


|  |
| --- |
| **Backlinks** |
| [Android Google Services API Key property](https://wiki.genexus.com/commwiki/wiki?37267) | [Video data type](https://wiki.genexus.com/commwiki/wiki?16608) |
| [Video data type (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?53910) |

---
