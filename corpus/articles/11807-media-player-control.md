---
title: "Media Player Control"
source_id: 11807
source_url: https://wiki.genexus.com/commwiki/wiki?11807
genexus_version: "18"
---

# Media Player Control

Different Multimedia sources such as audio, video, pdf in your Web Applications are a powerful tool for making your application more informative and more attractive.

Video can be stored in your database, or you can use common online video sharing services. In this context, the GX Media Player Control will handle the different kinds of sources you could want to use.

### [Using the control](#Using+the+control)

GX Media Player is a GeneXus built-in control that is available in the toolbox.

How to use the control:

1. Drag it to your panel.

`[imagen omitida: wiki id 30756]`

1. Set the Source property to your media source (This can be done programmatically or at design time).

   ```
   gxmediaPlayer1.Source = 'video.mp4'
   ```
2. Run (F5)

### [Properties](#Properties)

* Width
* Height
* Full Screen
* Media Title: A descriptive name for the media (it can be empty).
* AutoPlay: The player, when possible, starts playing the media source.
* Source: Indicates the media URI to be played
* Control Name

The implementation of this control is based on the [VIDEO HTML5](http://www.w3schools.com/html/html5_video.asp) tag and uses the [VideoJS library](http://videojs.com/) to use a Flash player when the VIDEO tag is not supported.

**Supported Sources**

The Source property supports the following sources:

* YouTube video URL
* Vimeo video URL
* Google video URL
* Local URL  (e.g: pathtourl(Blob) can be used)
* Flash
* Mp4
* Ogg

However, the supported formats depend on the browser and operating system, see this [link](https://developer.mozilla.org/en-US/docs/Web/HTML/Supported_media_formats).

### [Availability](#Availability)

Since GeneXus X Evolution 3 upgrade 8.

###


|  |
| --- |
| **Backlinks** |
| [Category:Common Controls](https://wiki.genexus.com/commwiki/wiki?5928) |

---
