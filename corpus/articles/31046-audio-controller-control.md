---
title: "Audio Controller control"
source_id: 31046
source_url: https://wiki.genexus.com/commwiki/wiki?31046
genexus_version: "18"
---

# Audio Controller control

To handle [audio](https://wiki.genexus.com/commwiki/wiki?30041) in applications, it is important to have a media player that allows end users to maximize their experience and at the same time makes it simple for developers.

The purpose of the Audio Controller control is to display all the standard media buttons associated with their functionality (such as Play, Pause, and Stop) and incorporate advanced features and flexibility for customization.

`[imagen omitida: wiki id 55721]`

## [Modes](#Modes)

|  |  |  |
| --- | --- | --- |
| **Android** | **iOS** |  |
|  |  | **Mini player** |
|  |  | **Full-Screen player** |

## [Previous button behavior](#Previous+button+behavior)

The *previous button* has two possible states according to the progress of the song.

* **Start again**: If the song is playing for at least three seconds, the previous button restarts the current song from the beginning.
* **Previous song**: If the song does not reach the first three seconds playing, the previous button returns to the previous song.

If the song tops the queue, the previous button is enabled after three seconds playing.

## [Appearance customization](#Appearance+customization)

When GeneXus detects that an Audio Controller has been embedded into a layout, it will automatically create a new super-class in the [themes](https://wiki.genexus.com/commwiki/wiki?16595) called AudioController with the following properties:

|  |  |
| --- | --- |
| **Mini Player** | |
| ***Title Label Class*** | A TextBlock sub-class to apply to the *Title* of the [MediaItem](https://wiki.genexus.com/commwiki/wiki?30041) that is being played and displayed in the mini player. |
| ***Subtitle Label Class*** | Analogous to Title Label Class for the *Subtitle.* |
| ***Image Class*** | An Image sub-class to apply to the *Image* of the [MediaItem](https://wiki.genexus.com/commwiki/wiki?30041) that is being played and displayed in the mini player. |
| ***Play / Pause Button Class*** | A Button sub-class to apply to the Play and Pause buttons in the mini player. |

|  |  |
| --- | --- |
| **Full-Screen Player** | |
| ***Title Label Class*** | Analogous to *Title Label Class*in the mini player for the full-screen player. |
| ***Subtitle Label Class*** | Analogous to *Subtitle Label Class*in the mini player for the full-screen player. |
| ***Image Class*** | Analogous to *Image Class*in the mini player for the full-screen player. |
| ***Play / Pause Button Class*** | Analogous to *Play / Pause Button Class* in the mini player for the full-screen player. |
| ***Other Buttons Class*** | A Button sub-class to apply to other buttons in the full-screen player – such as Rewind and Forward. |

**Note**: Not all properties for theme sub-classes are considered. The table below shows which properties are considered for each sub-class mentioned above.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **From...** | ***TextBlock  sub-class*** | ***Image  sub-class*** | ***Button  sub-class*** |
|  | **Are considered...** | *Forecolor  Font      Family      Size      TextDecoration         Weight, Style       Category* | *Margin       Top       Bottom         Right       Left  ScaleType  Placeholder Image  Image Loading Indicator*  **Limitation**: Only for Android | *Margin       Top       Bottom         Right         Left  Forecolor* |

### [Customization example](#Customization+example)

First, create the associated classes for each field required in the AudioController super-class.

`[imagen omitida: wiki id 31078]`

Next, set these classes in their corresponding fields:

`[imagen omitida: wiki id 31076]`

Finally, you will obtain the following result in the Audio Controller control:

|  |  |  |
| --- | --- | --- |
| **Android** | **iOS** |  |
|  |  | **Mini player** |
|  |  | **Full-Screen player** |

## [Quick access](#Quick+access)

An application with an Audio Controller control automatically enables a player's quick access when a queue is set. In this widget, the current song will be displayed with its information and progress state.

|  |  |
| --- | --- |
| **Android  (from the toolbar)** | **iOS  (from the control center)** |
|  |  |

**Warning**: This special player managed by the OS (operative system) must not be confused with the player provided by GeneXus. The AudioController control only displays the *title*, *subtitle,*and *image* of a media item. The *mini mode* adds the *play/pause* state button and the *full mode* also includes buttons such as back, forward, repeat, shuffle, etc.

## [Notes](#Notes)

* When the device is locked while playing a media item and audio is interrupted (e.g. by a phone call), the behavior will be as follows:
  + In iOS 10 or higher versions, the audio will be resumed automatically when it is restored.
  + In iOS 9 or lower versions, the audio must be resumed manually using the play button on the player once the interruption has finished.
* In iOS, the developer must enable the audio *background playback mode* in order to allow the end user to use the player outside the application. This process can be done by adding the 'audio' value to the [Background Modes property](https://wiki.genexus.com/commwiki/wiki?35408).

## [Scope](#Scope)

**Objects**: [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974)      
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)


|  |
| --- |
| **Backlinks** |
| [Accessible Name Control property](https://wiki.genexus.com/commwiki/wiki?55456) | [Accessible Name Custom property](https://wiki.genexus.com/commwiki/wiki?55469) | [Audio external object](https://wiki.genexus.com/commwiki/wiki?30041) |
| [Background Modes property](https://wiki.genexus.com/commwiki/wiki?35408) | [Google Cast Receiver Application Id property](https://wiki.genexus.com/commwiki/wiki?31540) | [Image Class property](https://wiki.genexus.com/commwiki/wiki?40348) |
| [Other Buttons Class property](https://wiki.genexus.com/commwiki/wiki?40350) | [Play/Pause Button Class property](https://wiki.genexus.com/commwiki/wiki?40349) | [Subtitle Label Class property](https://wiki.genexus.com/commwiki/wiki?40347) | [Category:Theme object](https://wiki.genexus.com/commwiki/wiki?16595) |
| [Title Label Class property](https://wiki.genexus.com/commwiki/wiki?40346) |

---
