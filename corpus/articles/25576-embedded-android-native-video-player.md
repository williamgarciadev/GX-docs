---
title: "Embedded Android native video player"
source_id: 25576
source_url: https://wiki.genexus.com/commwiki/wiki?25576
genexus_version: "18"
---

# Embedded Android native video player

This document describes the functionality provided by the Native Video Player control in Android. This control is used whenever you use a variable or attribute of type [Video](https://wiki.genexus.com/commwiki/wiki?16608)in a layout.

**1.** A progress bar is first displayed while the video is pre-loaded.

* The time it takes varies depending on multiple factors (Local storage/Remote server, video quality, client & server bandwidth, streamed or stored, etc).
* Note that the video might not be able to be played if the device does not support the codec or container of the target video. Codecs & container formats available on Android vary according to the OS's version (and in practice also to the device manufacturer). Here's a list of the  [core media format and codecs](http://developer.android.com/guide/appendix/media-formats.html#core) supported in Android.

**2.** Once the video is pre-loaded, the progress bar disappears showing a play button and a preview picture of the video (i.e. the first frame of the video).

**3.** The media controller bar appears when tapping on the video and hides after 3 seconds or when tapping on the video again.

`[imagen omitida: wiki id 25592]`

**4.** It's also possible to watch the video in fullscreen by tapping the icon on the bottom right corner.

`[imagen omitida: wiki id 25593]`

The video starts from the current position that's being played on fullscreen landscape mode.

The navigation bar is hidden on devices that support this feature (Android API >= 16).  
The system bars and media controller are toggled on and off by tapping on the video.

If the video is not able to be played with Android's framework [MediaPlayer](http://developer.android.com/reference/android/media/MediaPlayer.html), then a dialog is displayed informing that the video could not be played and asking the user to try with another video player app he/she might have installed. In that case, a list of available apps is displayed.

`[imagen omitida: wiki id 25589]`     `[imagen omitida: wiki id 25590]`


|  |
| --- |
| **Backlinks** |
| [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Video data type](https://wiki.genexus.com/commwiki/wiki?16608) |
| [Video data type (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?53910) |

---
