---
title: "Video Control"
source_id: 47391
source_url: https://wiki.genexus.com/commwiki/wiki?47391
genexus_version: "18"
---

# Video Control

Specific control that allows you to show Attributes/Variables of Video data type, as well as to play videos automatically, change the playback speed, etc., keeping the same properties and methods as an Attribute/Variable of Video type whose Control Type property is set to Edit.

## [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

## [Properties](#Properties)

* [Autoplay](https://wiki.genexus.com/commwiki/wiki?47167,,)
* [Placeholder Image](https://wiki.genexus.com/commwiki/wiki?47169,,)
* [Playback Rate](https://wiki.genexus.com/commwiki/wiki?47166,,)
* [Play In Full Screen](https://wiki.genexus.com/commwiki/wiki?47168,,)
* [Show Playback Controls](https://wiki.genexus.com/commwiki/wiki?47165,,)
* [Thumbnail Attribute](https://wiki.genexus.com/commwiki/wiki?47170,,)
* VideoName: Returns the name of the video.
* VideoType: Returns the type of video that is, the extension of the video file, such as .avi, .wmv, etc.
* VideoURI: Returns the absolute URL of the video. It can also be used to set the external video path or a local path using the protocol *file://*.

```
&Video.VideoURI = "http: //www.myvideofiles/video.avi"
```

## **Methods**

**FromURL**

Assigns the indicated value to the attribute/variable.

**SetEmpty**

Assigns the empty value of the Video data type.

**IsEmpty**

Returns True if the Attribute/Variable is empty; otherwise, it returns False.

## 

## [Compatibility](#Compatibility)

[Reference for video formats supported in iOS](https://developer.apple.com/library/ios/documentation/miscellaneous/conceptual/iphoneostechoverview/MediaLayer/MediaLayer.html)

[Reference for video formats supported in Android](http://developer.android.com/guide/appendix/media-formats.html)

## [Availability](#Availability)

This Attribute/Variable is available since [GeneXus 17 upgrade 1](https://wiki.genexus.com/commwiki/wiki?46852,,).
