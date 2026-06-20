---
title: "Audio data type"
source_id: 16529
source_url: https://wiki.genexus.com/commwiki/wiki?16529
genexus_version: "18"
---

# Audio data type

Stores or references any type of audio files (mp3, wav, etc.). An Audio-based attribute or variable can be loaded from both the FromURL method (specifying an URL, local or remote, where the audio file is stored) and setting its AudioURI property. If the value sent to FromURL is a remote URL, the audio will be downloaded and saved in the DB upon making an Insert. If what is needed is just a reference to the Audio stored in a local or remote location, the AudioURI property has to be assigned. These audios can be stored in any of the databases supported by GeneXus without having to specify its file name or extension. Therefore, any audio file can be reproduced by dragging any variable or attribute defined with the Audio data type to the form.

## [Properties](#Properties)

|  |  |
| --- | --- |
| **AudioName** | Gets the Audio name. |
| **AudioType** | Gets the Audio Type. The AudioType is the extension of the audio file (e.g. mp3, wav, etc.). |
| **AudioURI** | Sets or gets the Audio URL. This URL can be:  - A relative path, which will be resolved with the current host.  - An absolute path to an external audio on the web.  - A local path by using *file://* protocol.  When you *set* the AudioURI property, the internal Blob with the audio will be set to empty.  For example,  ``` // Example &MyAudio.FromUrl(MyAudioAttributeWillBeErasedInNextLine) &MyAudio.AudioURI = "http://www.myaudiofiles/audio.mp3" // audio.mp3 will be MyAudio ```  On the other hand, when you want to *get* the value of this property, GeneXus always returns the absolute URL specified. |

## [Methods](#Methods)

### [FromURL](#FromURL)

Loads the current audio instance (blob) with the URI indicated in the parameter. After calling this method, the AudioURI property has the absolute URL specified.

**Return value**: None  
**Parameters**: AudioSource : URL

For example,

```
&audio.FromURL('http://www.myband.com/song.mp3')
msg(&audio.AudioURI) // it will print 'http://www.myband.com/song.mp3' text
```

**Note**: For Audio-based attributes, the audio media content will be downloaded from the URL specified and will be automatically stored in the database.

### [SetEmpty](#SetEmpty)

Sets the current audio-based attribute/variable to an empty value (without audio content or reference to any audio source).

**Return value**: None  
**Parameters**: None

### [IsEmpty](#IsEmpty)

Returns True if the current audio-based attribute/variable has not a reference to a stored audio.

**Return value**: Boolean  
**Parameters**: None

## [Examples](#Examples)

### [1. Structuring](#1.+Structuring)

A company wants to save songs of its bands albums; to do so, you only have to write the following:

```
SongId     Numeric(4.0)
SongName   Character
SongAudio  Audio
```

In the SongAudio field, any type of audio can be stored (mp3, wav, etc).

### [2. Inserting an audio into the DB from an existing URL](#2.+Inserting+an+audio+into+the+DB+from+an+existing+URL)

Suppose you have an audio file in your file system or in a web URL and you want to store it in your database. Your audio file is file:///c:/myfolder/song.mp3 (the URL must be accessible from your server if it is a local URL).

```
&Song.SongId = 1
&Song.SongAudio.FromURL('file:///c:/myfolder/song.mp3')
&Song.Save()
```

### [3. Inserting a reference into the DB from an external audio](#3.+Inserting+a+reference+into+the+DB+from+an+external+audio)

You want to reference an external audio, for example:  http://myband/myalbum/mysong.mp3

```
&Song.SongId = 1
&Song.SongAudio.AudioURI = 'http://myband/myalbum/mysong.mp3'
&Song.Save()
```

## [FAQ](#FAQ)

### [How to convert from Blob to Audio in your DB?](#How+to+convert+from+Blob+to+Audio+in+your+DB%3F)

Most likely, you have many Blob attributes in your DB to store audio and you want to start using the new data type. The only thing you have to do is change the type from Blob to Audio in your attribute definition and GeneXus will perform a reorganization, taking into account the FileType, FileTypeAttribute and FileNameAttribute properties.

### [How to convert from Blob to Audio and vice versa programmatically?](#How+to+convert+from+Blob+to+Audio+and+vice+versa+programmatically%3F)

You can directly assign a Blob to an Audio and vice versa. Remember that the conversion from Blob to Audio will work depending on the kind of mime type of your Blob and the FileType, FileTypeAttribute and FileNameAttribute properties. In some cases, it may happen that the Audio is not reproduced in the user interface.

### [How to convert from Char|VarChar to Audio in my DB?](#How+to+convert+from+Char+VarChar+to+Audio+in+my+DB%3F)

In some cases, we could have a Character attribute in our DB with URL. What would happen if you wanted to start using the new Audio Data Type without losing your existing data? GeneXus supports the reorganization from Char|VarChar to Audio and vice versa.

### [Upon selecting the "Record an Audio" option of the Audio data type, the message "No apps can perform this actions" appears. (Android)](#Upon+selecting+the+%22Record+an+Audio%22+option+of+the+Audio+data+type%2C+the+message+%22No+apps+can+perform+this+actions%22+appears.+%28Android%29)

The Audio data type has an "intent" to call any app with record audio capability installed on the device. The error is triggered when no apps of this type were found. In order to not depend on this third-party app, you can use the Audio EXO.

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Objects** | Attributes, Variables |
| **Generators** | .NET, .NET Core, Java, Angular |

## [See also](#See+also)

* [Supported audio formats for Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?36060)
* [Audio streaming in Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?16498)
* [Audio external object](https://wiki.genexus.com/commwiki/wiki?30041)


|  |
| --- |
| **Backlinks** |
| [Audio external object](https://wiki.genexus.com/commwiki/wiki?30041) | [Audio streaming in Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?16498) | [AudioRecorder external object](https://wiki.genexus.com/commwiki/wiki?34096) |
| [Blob data type](https://wiki.genexus.com/commwiki/wiki?6704) | [BlobFile data type](https://wiki.genexus.com/commwiki/wiki?40420) | [Customization of Multimedia Fields](https://wiki.genexus.com/commwiki/wiki?20117) | [Data Type Filter property](https://wiki.genexus.com/commwiki/wiki?40654) |
| [Data Type property](https://wiki.genexus.com/commwiki/wiki?7232) | [Data types list](https://wiki.genexus.com/commwiki/wiki?6779) | [External Storage for Multimedia](https://wiki.genexus.com/commwiki/wiki?31120) | [FromURL method](https://wiki.genexus.com/commwiki/wiki?9644) |
| [GeneXus Markup Language (GXML)](https://wiki.genexus.com/commwiki/wiki?46876) | [HowTo: Deploy an Application to a Kubernetes cluster](https://wiki.genexus.com/commwiki/wiki?45416) | [HowTo: Deploy to AWS Lambda Function](https://wiki.genexus.com/commwiki/wiki?51533) | [HowTo: Upload an image, video, or audio file via an API object](https://wiki.genexus.com/commwiki/wiki?51411) |
| [HowTo: Use Audio in Smart Devices](https://wiki.genexus.com/commwiki/wiki?20114) | [IsEmpty method](https://wiki.genexus.com/commwiki/wiki?9645) | [Load balancing considerations](https://wiki.genexus.com/commwiki/wiki?45291) | [Purpose Strings properties group](https://wiki.genexus.com/commwiki/wiki?32755) |
| [Security Scanner built-in tool](https://wiki.genexus.com/commwiki/wiki?46412) | [SetEmpty method](https://wiki.genexus.com/commwiki/wiki?9646) | [SpeechToText procedure](https://wiki.genexus.com/commwiki/wiki?40169) | [Supported audio formats for Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?36060) |
| [TextToSpeech procedure](https://wiki.genexus.com/commwiki/wiki?40170) |

---
