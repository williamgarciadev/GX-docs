---
title: "AudioRecorder external object"
source_id: 34096
source_url: https://wiki.genexus.com/commwiki/wiki?34096
genexus_version: "18"
---

# AudioRecorder external object

The AudioRecoder external object is a simple API that helps you record and save audio as a file.

|  |  |
| --- | --- |
|  |  |

## [Properties](#Properties)

### [IsRecording property](#IsRecording+property)

Indicates whether the device is currently recording (True) or not (False).

## [Methods](#Methods)

**Note**: This API defines two methods to be called in batch mode (no UI is presented to the user).

### [Start method](#Start+method)

Starts an audio recording session and returns whether the operation was successful or not (e.g. if there is another recording in progress, it will return False). The audio recorded will be saved to a local file. The recorded file path is returned by the Stop method (see bellow), and it can be assigned to an [Audio-based](https://wiki.genexus.com/commwiki/wiki?16529) attribute or variable.

|  |  |
| --- | --- |
| **Return value** | [Boolean](https://wiki.genexus.com/commwiki/wiki?4374) |
| **Parameters** | None |

### [Stop method](#Stop+method)

Stops the current audio recording session and returns the file path where the audio file was saved. Multiple calls to this method do not have any effect.

|  |  |
| --- | --- |
| **Return value** | [URL](https://wiki.genexus.com/commwiki/wiki?15668) |
| **Parameters** | None |

## [Events](#Events)

It does not have any.

## [Example](#Example)

**Note**: This sample does not include details on how to handle the UI customization aspects.

Suppose a simple scenario of a community chat. Nowadays, every messaging system has two main components:

1. Every message is shown from the bottom of the screen to the top. This can be achieved by using the [Inverse Loading property](https://wiki.genexus.com/commwiki/wiki?32660) at the grid level.
2. There is a text-field where the end users can write their text messages and then send them by tapping a button on the screen. This can be achieved by including a variable based on the [Character data type](https://wiki.genexus.com/commwiki/wiki?6777) and a [Button control](https://wiki.genexus.com/commwiki/wiki?6011) with the following behavior:

```
Event 'SendTextMessage'
  Composite
    SendTextMessage(&Text,&Username)
    Refresh
  EndComposite
EndEvent
```

Basically, the SendTextMessage procedure receives the message to send (&Text variable, it must be *inout*) and the username (&Username variable), performs the necessary checks and then sends the message and cleans the &Text variable.

Now suppose we want to incorporate a third component: the ability to send audio messages.

There are two things we need to do to implement this feature.

* **Record the audio message**  
  It can be done by including a button that starts the recording process and notifies the user in case the recording session could not be started.

```
Event 'StartRecording'
   Composite
     &HasSuccess = AudioRecorder.Start()
     If not &HasSuccess
       msg("For some reason we couldn't start recording")
     EndIf
   EndComposite
EndEvent
```

This button should be hidden once the operation is completed successfully, and another button should be displayed to stop the current recording process (as it is described in the following point).

* **Send the audio message recorded**  
  Once the end user stops recording, the current audio message will be sent.

```
Event 'StopRecording'
   Composite
     &IsRecording = AudioRecorder.IsRecording
     If &IsRecording
       &FilePath = AudioRecorder.Stop()
       &Audio.AudioURI = &FilePath
       SendAudioMessage(&Audio,&Username)
       Refresh
     EndIf
   EndComposite
EndEvent
```

The SendAudioMessage procedure is analogous to the SendTextMessage procedure. Remember that this button was shown once the end user taps on the 'StartRecording' button. For that reason, it is not possible that the 'StopRecording' event has been called without having started a recording previously. Nevertheless, in this case, we prefer to include a validation step to avoid the problem of sending an empty audio message (because the Stop method does not have effect when there is not an audio recording). Also, to be consistent, the developer must hide this button if the operation was successful and must display the button that allows the end user to start a new recording.

After applying these concepts and by adding a friendly custom UI, a developer can achieve the following results.

`[imagen omitida: wiki id 34275]`

## [Notes](#Notes)

* The audio file will be saved as MPEG-4 format with AAC encoder. This format is compatible with all the supported platforms.
* If the application is closed while there is an active audio recording session, then the recording is stopped and the audio file is discarded.
* The recorded audio can be played using the methods of the [Audio external object](https://wiki.genexus.com/commwiki/wiki?30041).

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Platforms** | SmartDevices(iOS, Android) |

## [Availability](#Availability)

This external object is available as from [GeneXus 15 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?33798,,).


|  |
| --- |
| **Backlinks** |
| [Background Modes property](https://wiki.genexus.com/commwiki/wiki?35408) | [GeneXus Core module](https://wiki.genexus.com/commwiki/wiki?31268) |
| [GeneXus Core module (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54413) | [Purpose Strings properties group](https://wiki.genexus.com/commwiki/wiki?32755) | [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) | [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) |

---
