---
title: "Video Operations External Object"
source_id: 47028
source_url: https://wiki.genexus.com/commwiki/wiki?47028
genexus_version: "18"
---

# Video Operations External Object

It allows you to edit videos, changing their quality and/or format.

|  |  |
| --- | --- |
|  |  |

## [**Methods**](#Methods)

**ApplyConversions**

Makes all the possible conversions indicated in the SDT **VideoConversionParameters**.

For example, you want to reduce the quality of a video to Low and change the format to .MP4.

```
&SDTVideoConversionParameters.ConvertFormat = True
&SDTVideoConversionParameters.TargetFormat = VideoFormat.MP4
&SDTVideoConversionParameters.ReduceQuality = True
&SDTVideoConversionParameters.TargetQuality = CameraAPIQuality.Low
&ConvertedVideo = &OriginalVideo.ApplyCinvertuibs(&SDTVideoConversionParameters)
```

**ConvertFormat**

Converts the video to the format indicated by the parameter. It returns a new video, and the original video is not altered.

```
&FormattedVideo = VideoOperations.ConvertFormat(&OriginalVideo, VideoFormat.MP4)
```

**ReduceQuality**

  Reduces the quality of the video to the new indicated quality. It returns a new video, and the original video is not altered.

```
&FormattedVideo = VideoOperations.ReduceQuality(&OriginalVideo, CameraAPIQuality.Low)
```

## [**Domains**](#Domains)

**VideoFormat**

Stores valid video conversion formats.

Values:

* M4V
* MPEG4
* QuickTime
* ThirdGenPP
* ThirdGenPP2

## [**Structured Data Types**](#Structured+Data+Types)

**VideoConversionParameters**

* ConvertFormat: Boolean

            If True, the video format change will be applied.

* TargetFormat: VideoFormat

            Defines the new video format.

* ReduceQuality: Boolean

If True, the change in format quality will be applied.

* TargetQuality: [CameraAPIQuality](https://wiki.genexus.com/commwiki/wiki?27012)

Changes the quality of the video depending on the value indicated.

## [**Scope**](#Scope)

**Object:**Attributo/Variable [Video](https://wiki.genexus.com/commwiki/wiki?16608)

**Generators:**Android, Apple

## [**Availability**](#Availability)

[GeneXus 17](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46873,,)
