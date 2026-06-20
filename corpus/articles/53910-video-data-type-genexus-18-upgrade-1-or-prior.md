---
title: "Video data type (GeneXus 18 Upgrade 1 or prior)"
source_id: 53910
source_url: https://wiki.genexus.com/commwiki/wiki?53910
genexus_version: "18"
---

# Video data type (GeneXus 18 Upgrade 1 or prior)

Stores or references any type of video files (avi, mp4, etc). Video can be stored in any of the databases supported by GeneXus without having to specify the file name or type (avi, wmv, etc.).

A Video attribute or variable can be loaded from both the FromUrl method (specifying an URL, local or remote, where the video file is stored) and setting its VideoURI property.

If the value sent to FromURL is a remote URL, the video will be downloaded and saved in the DB upon making an Insert. If what is needed is just a reference to the Video stored in a local or remote location, the VideoURI property has to be assigned.

Therefore, any video file can be reproduced by dragging any variable or attribute defined with the Video data type to the form.

### [Properties](#Properties)

|  |  |
| --- | --- |
| VideoName | Gets the Video name |
| VideoType | Gets the Video Type. The VideoType is the extension of the video file. For example: avi, wmv, etc. |
| VideoURI | Sets/Gets the Video URL  **Set**  You can set a relative path, which will be resolved with the current host.  You can set an absolute path to an external video on the web.  You can set a local path by using file:// protocol  When you set the VideoURI property, the internal Blob with the video will be set to empty.  For example:   ``` &video.FromUrl(myVideoWillbeErasedInNextLine) &video.VideoURI = "http://www.myvideofiles/video.avi" ```   In this case, video.avi will be the video in the data.  **Get**  GeneXus always returns the absolute URL to the Video. |

### [Methods](#Methods)

|  |  |
| --- | --- |
| FromURL(videoURI) | Loads the current instance with the video given in the videoURI parameter.  This indicates that the internal Blob holding the video must be loaded from the URI indicated in the videoURI parameter.  After calling this method, the VideoURI property has the absolute URL specified.  For example:   ``` &video.FromURL('www.myband.com/video.avi') msg(&video.VideoURI)  // will print www.myband.com/video.avi ```   **Note**: The video will be downloaded from the URL specified and will be automatically stored in the database (applies only to attributes). |
| SetEmpty/IsEmpty | Returns True if there isn't a video or a reference to an a stored video. |

### [Considerations](#Considerations)

* Videos are not [cached](https://wiki.genexus.com/commwiki/wiki?18602) in Smart Devices.
* Videos are always broadcasted via streaming. There is only an exception when the Smart Device application has an [Offline architecture](https://wiki.genexus.com/commwiki/wiki?22228) and the VideoURI is not a direct link to the video file (for instance: a link to a Youtube video). If that is the case, the Video files are stored inside the device, so that they can be played in the device whether it is connected or not to the internet.
* [Reference for video formats supported in iOS](https://developer.apple.com/library/ios/documentation/miscellaneous/conceptual/iphoneostechoverview/MediaLayer/MediaLayer.html)
* [Reference for video formats supported in Android](http://developer.android.com/guide/appendix/media-formats.html)

### [Samples](#Samples)

#### [1. Structuring](#1.+Structuring)

A company wants to save songs of its bands albums; to do so, you only have to write the following:

```
SongId     Numeric(4.0)
SongName   Character
SongVideo  Video
```

In the SongVideo field, any type of video can be stored (avi, mp4, etc).

#### [2. Inserting a video into the DB from an existing URL](#2.+Inserting+a+video+into+the+DB+from+an+existing+URL)

Suppose you have a video file in your file system or in a web URL and you want to store it in your database. Your video file is file:///c:/myfolder/video.avi (the URL must be accessible from your server if it is a local URL).

```
&Song.SongId = 1
&Song.SongVideo.FromURL('file:///c:/myfolder/video.avi')
&Song.Save()
```

#### [3. Inserting a reference into the DB from an external video](#3.+Inserting+a+reference+into+the+DB+from+an+external+video)

You want to reference an external video, for example:  http://myband/myalbum/myvideo.avi

```
&Song.SongId = 1
&Song.SongVideo.VideoURI = 'http://myband/myalbum/myvideo.avi'
&Song.Save()
```

#### [4. How to convert from Blob to Video in your DB](#4.+How+to+convert+from+Blob+to+Video+in+your+DB)

Most likely, you have many Blob attributes in your DB to store video and you want to start using the new data type.

The only thing you have to do is change the type from Blob to Video in your attribute definition and GeneXus will perform a reorganization, taking into account the FileType, FileTypeAttribute and FileNameAttribute properties.

#### [5. How to convert from Blob to Video and vice versa programmatically](#5.+How+to+convert+from+Blob+to+Video+and+vice+versa+programmatically)

You can directly assign a Blob to a Video and vice versa. Remember that the conversion from Blob to Video will work depending on the kind of mime type of your Blob and the FileType, FileTypeAttribute and FileNameAttribute properties. In some cases, it may happen that the Video is not reproduced in the user interface.

#### [6. How to convert from Char|VarChar to Video in my DB](#6.+How+to+convert+from+Char+VarChar+to+Video+in+my+DB)

In some cases we could have a Character attribute in our DB with URL. What would happen if you wanted to start using the new Video Data Type without losing your existing data?

GeneXus supports the reorganization from Char|VarChar to Video and vice versa.

### [Scope](#Scope)

**Objects:**Attributes, Variables  
**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [See also](#See+also)

[Embedded Android native video player](https://wiki.genexus.com/commwiki/wiki?25576)  
[HowTo: Embedding YouTube videos in an Android application](https://wiki.genexus.com/commwiki/wiki?21923)
