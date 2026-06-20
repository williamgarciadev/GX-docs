---
title: "HowTo: Use Audio in Smart Devices"
source_id: 20114
source_url: https://wiki.genexus.com/commwiki/wiki?20114
genexus_version: "18"
---

# HowTo: Use Audio in Smart Devices

The [Audio external object](https://wiki.genexus.com/commwiki/wiki?30041) allows GeneXus users to enable audio features on their Smart Devices application.

This API can be used to:

a. Play an Audio continously, even though the user closes the application.  
b. Play an Audio but when the application closes the Audio stops.  
c. Play two Audios at the same time.

This document will explain how the (a), (b) and (c) cases are solved with GeneXus, the core functionality of the API and some examples of this feature on a Smart Devices application.

### [GeneXus Objects Involved](#GeneXus+Objects+Involved)

This API is composed of an [External Object](https://wiki.genexus.com/commwiki/wiki?17880) and a [Domain](https://wiki.genexus.com/commwiki/wiki?7221).

To solve a) GeneXus provides a *PlayBackground* method. This method will play the audio Iin the background even though the application closes.

To solve b) and c) there is one method *Play*, but this method receives a parameter extra of the Audio to be played. This parameter will be based on the domain *AudioAPISessionType*.

The possible values of this domain are:

|  |  |
| --- | --- |
| **Solo** | The current audio if any is stopped and the Audio passed by parameter will be executed. |
| **Mix** | Plays the Audio passed by parameter even though there is an Audio playing. |
| **Background** | Is like executing Audio.PlayBackground. |

The external object is as follows:

`[imagen omitida: wiki id 32308]`

The methods involved in playying a single audio are:

* **PlayBackground**(Audio, Category)  
  This method plays the Audio in the indicated Category (background, mix or solo).
* **PlayBackground**(Audio, Description)  
  This method plays the Audio in "background mode" with a description (character) as a parameter to show on the Lock screen of the device.
* **Play**(Audio, AudioAPISessionType)   
  This is a way to play an Audio with a given type.
* **Stop**  
  Stops all Audio playing.
* **Stop**(Category)  
  Stops an Audio of the given a session type (background, mix or solo).
* **IsPlaying**: Boolean    
  This method returns a boolean value. Tru if an audio of any kind is being played.
* **IsPlaying**(Category) : Boolean  
  This method returns a boolean value if an audio of the type of the parameter passed is being played.

The Audio parameter is based on the [Audio data type](https://wiki.genexus.com/commwiki/wiki?16529).

### [Samples](#Samples)

This Event plays an Audio in the background:

```
Event 'PlayBackground'
    Audio.PlayBackground(&varAudioLong)
EndEvent
```

This Event will behave like the above:

```
Event 'PlayBackground2'
    Audio.Play(&varAudio4, AudioAPISessionType.Background)
Endevent
```

This Event will execute the &AudioMix with any audio that is already playing:

```
Event 'PlayMix'
    Audio.Play(&varAudio4, AudioAPISessionType.Mix)
Endevent
```

If there was a Background Audio already playing, the Audio will be mixed.

This event will execute only the &SoloAudio, stopping any audio being played:

```
Event 'PlaySolo'
    Audio.Play(&varAudio2, AudioAPISessionType.Solo)
Endevent
```

If there is a Background Audio playing, it will be paused and resumed after the Solo Audio finishes.

This Event plays if no background Audio is being played, and plays a Background Audio if a Background Audio is already playing. It plays a Mix Audio:

```
Event 'isPlayingBackground'
    Composite
        &varBoolean = Audio.IsPlaying(AudioAPISessionType.Background)
        if &varBoolean
           Audio.Play(&varAudio4, AudioAPISessionType.Solo)
        else
           Audio.PlayBackground(&varAudioLong)
        endif
    EndComposite
Endevent
```

**Notes:**

* When using the Background option, even if the device is in "mute state", the audio will be heard.
* The Mix option is generally used to reproduce a short audio. It will potentially sound on top of an existing one. If the device is "muted" it will not be heard.

### Enabling background playback for [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

iOS requires additional permission to let the application play audio while it is not running. By default, when the application closes, the audio will stop even if it was started with PlayBackground() method.

To enable background playing in iOS, you'll need to add the 'audio' value for the [Background Modes property](https://wiki.genexus.com/commwiki/wiki?35408).


|  |
| --- |
| **Backlinks** |
| [Audio external object](https://wiki.genexus.com/commwiki/wiki?30041) |

---
