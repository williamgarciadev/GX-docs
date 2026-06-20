---
title: "Audio external object"
source_id: 30041
source_url: https://wiki.genexus.com/commwiki/wiki?30041
genexus_version: "18"
---

# Audio external object

The audio external object provides a powerful and versatile system for you to control audio stream on smart device applications.  
It has three principal aims:

* Allow end users to choose audio sources and define when and how to play them.
* Create and manage play queues.
* Customize the functionality of the [player](https://wiki.genexus.com/commwiki/wiki?31046).

**Warning**: The methods and events provided by this [External Object](https://wiki.genexus.com/commwiki/wiki?17880) are fully available on the [client-side](https://wiki.genexus.com/commwiki/wiki?17042) of smart devices events for [panels](https://wiki.genexus.com/commwiki/wiki?24829) or [WWSD](https://wiki.genexus.com/commwiki/wiki?15974) objects and partially available on Web environments.

|  |  |
| --- | --- |
|  |  |

## [Properties](#Properties)

It does not have any.

## [Methods](#Methods)

### [Play method](#Play+method)

Plays the given audio with the specified category.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | audio:[Audio](https://wiki.genexus.com/commwiki/wiki?16529), category:AudioAPISessionType |

**Note**: Supported for Smart Devices and Web environments.

### [PlayBackground method](#PlayBackground+method)

Plays the given audio in the background, and keeps playing while the application is running in the background.  This method is considered canonical, being analogous to Play(&Audio,AudioAPISessionType.Background) with the ability to add a *description* when the audio is played.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | audio:[Audio](https://wiki.genexus.com/commwiki/wiki?16529) [, description:[Character(20)](https://wiki.genexus.com/commwiki/wiki?6777) ] |

**Note**: Supported for Smart Devices and Web environments.

### [Stop method](#Stop+method)

By default, it stops the audio playing in all categories, unless any session type is specified, in which case any audio being played in this category is stopped.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | [ category:AudioAPISessionType ] |

**Note**: Supported for Smart Devices and Web environments.

### [IsPlaying method](#IsPlaying+method)

Returns whether there is audio playing in any session type or at a certain category when it is specified.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | [ category:AudioAPISessionType ] |
|  |  |

### [GetQueue method](#GetQueue+method)

Returns the current audio queue.

|  |  |
| --- | --- |
| **Return value** | MediaQueue |
| **Parameters** | None |
|  |  |

### [GetQueueState method](#GetQueueState+method)

Get the information about the state of the current audio queue (including the position in the queue and inside the current playing item, if any).

|  |  |
| --- | --- |
| **Return value** | MediaQueueState |
| **Parameters** | None |
|  |  |

### [SetQueue method](#SetQueue+method)

Sets the current audio queue. Stops current background playback, if any.  Also, it preserves the playing status by looking for the current media item in the new queue; if it finds it, it updates the current position of that item in the queue; otherwise, it stops the queue and plays it from the beginning.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | queue:MediaQueue |
|  |  |

### [PlayQueue method](#PlayQueue+method)

Starts or resumes playback of the current audio queue (previously set).

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | None |
|  |  |

### [PauseQueue method](#PauseQueue+method)

Pauses playback of the current audio queue.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | None |
|  |  |

### [SetPlayerSettings method](#SetPlayerSettings+method)

Allows the developer to set settings indicated in the AudioPlayerSettings.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | settings:AudioPlayerSettings |
|  |  |

### [SetQueueCurrentIndex method](#SetQueueCurrentIndex+method)

Sets the current item played by its index in the current media queue. The current item playing can be obtained using the GetQueueState method.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | index:[Numeric(8.0)](https://wiki.genexus.com/commwiki/wiki?6793) |

**Note**: Behavior details:  
- If the current item was modified, the [player](https://wiki.genexus.com/commwiki/wiki?31046) reflects the change.  
- If the index does not exist in the current media queue, the call will be ignored.  
- If a song in the queue is playing when the method is invoked, that song will be aborted. Then, the selected song (by its index in the queue) starts playing from the beginning - even if the item is the same that is currently playing.  
- If you call the method with *shuffle mode* activated through *SetPlayerSettings* method, the index is that which belongs to the original queue (set by *SetQueue* method) and probably not follows the order expected (caused by the player mode).

### [SetQueueCurrentItem method](#SetQueueCurrentItem+method)

It has the same behavior as *SetQueueCurrentIndex* method, but It will set it by its MediaId instead of its index in the queue.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | mediaId:[VarChar(40)](https://wiki.genexus.com/commwiki/wiki?6778) |
|  |  |

### [iOSSetShowsMiniPlayer method](#iOSSetShowsMiniPlayer+method)

With this method is possible to indicate if the default iOS player is showed (True) or not (False) at the bottom of the screen.  
The player will be initialized with the first song paused.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | show:[Boolean](https://wiki.genexus.com/commwiki/wiki?4374) |

**Note**: Considerations:  
- This method is iOS specific and it's necessary to set [Navigation Style](https://wiki.genexus.com/commwiki/wiki?16229) in Slide mode.  
- This player is not the same that the [mini-player](https://wiki.genexus.com/commwiki/wiki?31046).  
- This default mini player (provided by iOS) can be customized by *\*.plist* file located in the generated project adding these additional lines.   
>> Customize height:  
        **<key>**GXSliderMenuCollapsedBottomPanelHeight**</key>**  
        **<integer>***numeric\_value***</integer>**  
   where *numeric\_value* is an integer expressed in dips  
>> Customize Color  
        **<key>**GXAudioAPIMiniPlayerBackgroundColor **</key>**  
        **<integer>***hex\_color***</integer>**  
   where *hex\_color*is the hexadecimal representation for a color (e.g. #29b6f6)  
In order to not overwrite It on every build, It can be added into *MainName-Info.plist* file located in *<gx\_install\_dir>/iOS/Templates/iOS\_Genexus/*directory.

### [iOSDisplayFullScreenPlayer method](#iOSDisplayFullScreenPlayer+method)

This method allows the developer to display the player in fullscreen mode.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | None |
|  |  |

### [iOSDismissFullScreenPlayer method](#iOSDismissFullScreenPlayer+method)

This method allows the developer to dismiss the player when It is in fullscreen mode (e.g. through a custom action on the player).

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | None |
|  |  |

## [Events](#Events)

### [QueueStateChanged event](#QueueStateChanged+event)

It is triggered when the current media item or the media state in playback changes.

|  |  |
| --- | --- |
| **Input** | queueState:MediaQueueState |
| **Output** | None |
|  |  |

### [QueueItemFinished event](#QueueItemFinished+event)

It is activated when the current media item has finished playing.

|  |  |
| --- | --- |
| **Input** | finishedInfo:MediaItemFinishedInfo |
| **Output** | None |
|  |  |

### [CustomActionEvent event](#CustomActionEvent+event)

It is called when the end user triggers a custom action with certain ActiontId (usually an event name) in the [player](https://wiki.genexus.com/commwiki/wiki?31046) with its associated MediaItem.

|  |  |
| --- | --- |
| **Input** | actionId:[VarChar(40)](https://wiki.genexus.com/commwiki/wiki?6778), currentItem:MediaItem |
| **Output** | None |
|  |  |

Custom action usage example:

```
Event Audio.CustomActionEvent(&actionId, &currentMediaItem)
    composite
        do Case 
            case &actionId= !"someUserAction"
                // do something
            case &actionId= !"anotherAction"
                // do something else
            otherwise
                msg(!"Unknown event", nowait)
        endCase
    endComposite
EndEvent
```

## [Domains](#Domains)

### [AudioAPISessionType domain](#AudioAPISessionType+domain)

Possible streams of audio playback.

|  |  |
| --- | --- |
| **Background** | Audio is activated even when you exit the application or lock your device (e.g. a music application). |
| **Mix** | Audio is activated even if another audio is playing in the background (e.g. a notification sound when a new message arrived). |
| **Solo** | Audio is activated, stopping any other audio and re-playing it once the audio playing in Solo mode is inactive (e.g. like a ringtone on an incoming call). |

**Note**: Solo + Mix modes mix, but Mix + Solo modes stop Mix mode.

### [MediaDuration domain](#MediaDuration+domain)

To manage time elapsed in milliseconds. It's represented by a Numeric(12.0).

### [MediaMetadataKey domain](#MediaMetadataKey+domain)

It consists of a known key set for a certain media item. All of them are recognized automatically by the device.

|  |  |
| --- | --- |
| **Artist** | The artist name. |
| **Album** | The album title. |
| **Author** | The author name. |
| **Writer** | The writer name. |
| **Composer** | The composer name. |
| **Year** | The release year (number as a string). |
| **Genre** | The genre name. |
| **TrackNumber** | The track's number on the album (number as a string). |
| **NumberOfTracks** | The number of the album's tracks (number as a string). |
| **DiscNumber** | The disc number (number as a string). |
| **AlbumArtist** | The album artist name. |

**Note**: It is a good practice to incorporate this information into each media item.

### [MediaStreamType](#MediaStreamType)

Enumerated domain with possible media stream types.

|  |  |
| --- | --- |
| **None** | No information is provided |
| **Buffered** | It indicates that the streaming content will be buffered. |
| **Live** | It indicates that the streaming content will be in real-time. |
|  |  |

### [PlaybackState domain](#PlaybackState+domain)

Enumerated domain describing the possible playback states.

|  |  |
| --- | --- |
| **None** | The initial state of the play queue. |
| **Stopped** | The play queue is stopped, resetting the current track. This means that when the queue is played again, the last track starts from the beginning. |
| **Paused** | The play queue is paused. When the queue is played again, the last track will be resumed, starting in the same position before it was paused. |
| **Playing** | The play queue is playing the current track. |
| **Error** | Indicates that an error occurred in the play queue |
| **Transitional** | Temporary states of the queue that are not any of those described above (like Buffering, Rewinding, Skipping, Fast-Forwarding, etc.) |
|  |  |

### [MediaFinishReason](#MediaFinishReason)

Enumerated domain to indicate the reason why the current audio has finished. Its values are:

|  |  |
| --- | --- |
| **Unknown** | The reason that the media item has finished is not any of the other values listed below. |
| **PlaybackCompleted** | The current audio playing mode has completed or ended normally. |
| **Stopped** | The current audio playing has stopped. |
| **Skipped** | The current audio playing has skipped. |
| **QueueReplaced** | The audio queue has changed and the current audio playing does not include that item. |
|  |  |

## [Structured Data Types](#Structured+Data+Types)

To use this API, a set of data types is provided under SmartDevicesApi/Media folder.

### [MediaItem](#MediaItem)

It is an item from a playlist.

* Id:[VarChar(40)](https://wiki.genexus.com/commwiki/wiki?6778)  
  The media item identifier.
* Uri:[URL](https://wiki.genexus.com/commwiki/wiki?15668)  
  The media item URI (e.g. web URL). It can be provided by a URL Shortener (e.g. [tiny](http://tinyurl.com/), [bitly](https://bitly.com/) or [goo.gl](https://goo.gl/))
* ContentType:[VarChar(100)](https://wiki.genexus.com/commwiki/wiki?6778)  
  The media item content type (e.g. 'audio/mpeg' for audio).
* StreamType:MediaStreamType  
  The media item stream type.
* Title:[VarChar(100)](https://wiki.genexus.com/commwiki/wiki?6778)  
  The media item title.
* Subtitle:[VarChar(100)](https://wiki.genexus.com/commwiki/wiki?6778)  
  The media item subtitle.
* Description:[VarChar(300)](https://wiki.genexus.com/commwiki/wiki?6778)  
  The media item description.
* Image:[Image](https://wiki.genexus.com/commwiki/wiki?15204)  
  The media item image (e.g. album cover).
* Duration:MediaDuration  
  The media item duration. Semantically 0 means 'infinite' or 'unknown'.
* IsFavourite:[Boolean](https://wiki.genexus.com/commwiki/wiki?4374)  
  Indicates if the media item has been marked as favourite (True) or not (False).
* Metadata:Collection( Property )  
  Defines key-value pairs to incorporate extra information for a MediaItem.   
  + Key:[VarChar(50)](https://wiki.genexus.com/commwiki/wiki?6778)  
    The metadata key. A set of keys (automatically recognized by the device) is listed in MediaMetadataKey domain, but you can add your custom keys.
  + Value:[VarChar(500)](https://wiki.genexus.com/commwiki/wiki?6778)  
    The metadata value as a string.

**Note**: The ContentType and StreamType fields are used to interact with [Google Chromecast](https://wiki.genexus.com/commwiki/wiki?31540) and there are only available on Android.  
- ContentType is the MIME type for the Uri. Its value is mandatory (by default "audio/ mpeg ")  
- StreamType can be used by the receiver app to make decisions based on its value..

### [MediaQueue](#+MediaQueue)

It represents a play queue on the system.

* Title:[VarChar(100)](https://wiki.genexus.com/commwiki/wiki?6778)  
  The media queue title.
* Items:Collection( MediaItems )  
  The media queue items.

### [MediaQueueState](#+MediaQueueState)

It provides information about the current state of the play queue.

* State:PlaybackState  
  Indicates the playback state of the queue.
* QueuePosition:[Numeric(8.0)](https://wiki.genexus.com/commwiki/wiki?6793)  
  Indicates the queue position of the currently displayed media item (starting at 1).
* TrackPosition:MediaDuration  
  Milliseconds elapsed since the start of the media item currently displayed.
* MediaId:[VarChar(40)](https://wiki.genexus.com/commwiki/wiki?6778)  
  Identifier of the current item in the media queue.

### [MediaItemFinishedInfo](#MediaItemFinishedInfo)

It is an item from a playlist.

* ItemId:[VarChar(40)](https://wiki.genexus.com/commwiki/wiki?6778)  
  Idenfier of the media item.
* QueuePosition:[Numeric(8.0)](https://wiki.genexus.com/commwiki/wiki?6793)  
  Position of the media item in the queue.
* TrackPosition:MediaDuration  
  Milliseconds elapsed for the media item.
* Reason:MediaFinishReason  
  The reason why the media item finished.

### [AudioPlayerCustomAction](#AudioPlayerCustomAction)

Defines a custom action that will be added to [player](https://wiki.genexus.com/commwiki/wiki?31046) when it is in full-screen mode.

* Id:[VarChar(40)](https://wiki.genexus.com/commwiki/wiki?6778)  
  The custom action identifier (e.g. a custom event name).
* Title:[VarChar(200)](https://wiki.genexus.com/commwiki/wiki?6778)  
  The custom action title (displayed on the screen).
* Image:[Image](https://wiki.genexus.com/commwiki/wiki?15204)  
  The custom action image (e.g. an icon).

**Note**: Images are only supported on Android generator, images must be included in the KB (external images are not supported) and to watch them it is necessary to include a reference in the SDPanel/WWSD where the player is embedded..

### [AudioPlayerSettings](#+AudioPlayerSettings)

Offers the option to enable three default modes or incorporate a set of custom actions for the [player](https://wiki.genexus.com/commwiki/wiki?31046) when it is in full-screen mode.  
The default modes are:

|  |  |
| --- | --- |
| ***Toggle Favourite*** | Allows the end user to select a song as a favorite or unfavorite.   Consequently, this action triggers *CustomActionEvent* event, where EventName has value "GXFavouriteStatusChange" and the MediaItem is that which has changed its *IsFavourite* field. |
| ***Toggles Repeat*** | Allows the end user to play the same song again, play all the queue repetitively or simply not repeat it. |
| ***Toggles Shuffle*** | Allows the end user to play the songs randomly or sequentially. |
|  |  |

* SupportsFavourite:[Boolean](https://wiki.genexus.com/commwiki/wiki?4374)  
  Enables favorite icon on the [player](https://wiki.genexus.com/commwiki/wiki?31046) and the end user can mark his/her favorites media items.
* SupportRepeat:[Boolean](https://wiki.genexus.com/commwiki/wiki?4374)  
  Enables repeat mechanisms (with its icon `[imagen omitida: wiki id 39663]`) on the [player](https://wiki.genexus.com/commwiki/wiki?31046)
* SupportShuffle:[Boolean](https://wiki.genexus.com/commwiki/wiki?4374)  
  Enables shuffle mechanism (with its icon `[imagen omitida: wiki id 39664]`) on the [player](https://wiki.genexus.com/commwiki/wiki?31046)
* CustomActions:Collection( AudioPlayerCustomAction )  
  A collection of custom actions added to the [player](https://wiki.genexus.com/commwiki/wiki?31046).

**Note**: To set a new configuration it is necessary to call *SetPlayerSettings* method (described below). This action will not take effect until the next time that the player is displayed in full-screen (if it is already shown in that mode when the method is called).

## [Notes](#Notes)

### [Smart Devices](#Smart+Devices)

* Audio in background mode can be shared with Google Cast device through [Google Cast Receiver Application Id property](https://wiki.genexus.com/commwiki/wiki?31540)
* For canonical examples, refer to [How to using AudioAPI in Smart Devices](https://wiki.genexus.com/commwiki/wiki?20114)
* On iOS, for playing audio in background mode is necessary to include the 'audio' value to the [Background Modes property](https://wiki.genexus.com/commwiki/wiki?35408).

### [Web specific](#Web+specific)

* Use standard audio formats such as mp3 or wav files; support for other file extensions depends on the browser.
* Play, PlayBackground and Pause method are available for Web environment since [GeneXus 15 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?35908,,).

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Platforms** | Web(Java, .NET), Smart Devices (iOS, Android) |

## [Availability](#Availability)

This external object is available as from [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?28265,,).

* Web support is partially added since [GeneXus 15 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?35908,,)
* SetQueueCurrentItem is available as of [GeneXus 15 Upgrade 1](https://wiki.genexus.com/commwiki/wiki?32288,,).

## [See also](#See+also)

* [Supported audio formats for Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?36060)
* [AudioController control](https://wiki.genexus.com/commwiki/wiki?31046)
* [HowTo: Use PlayAudio method from Interop external object](https://wiki.genexus.com/commwiki/wiki?17339)


|  |
| --- |
| **Backlinks** |
| [Audio data type](https://wiki.genexus.com/commwiki/wiki?16529) | [AudioController control](https://wiki.genexus.com/commwiki/wiki?31046) | [AudioRecorder external object](https://wiki.genexus.com/commwiki/wiki?34096) |
| [Background Modes property](https://wiki.genexus.com/commwiki/wiki?35408) | [GeneXus Core module](https://wiki.genexus.com/commwiki/wiki?31268) |
| [GeneXus Core module (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54413) | [Google Cast Receiver Application Id property](https://wiki.genexus.com/commwiki/wiki?31540) | [Grids with Selection By Code for Panels](https://wiki.genexus.com/commwiki/wiki?35987) | [HowTo: Use Audio in Smart Devices](https://wiki.genexus.com/commwiki/wiki?20114) |
| [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) | [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) | [Supported audio formats for Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?36060) |

---
