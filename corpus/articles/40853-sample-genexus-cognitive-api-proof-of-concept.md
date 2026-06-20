---
title: "Sample: GeneXus Cognitive API proof of concept"
source_id: 40853
source_url: https://wiki.genexus.com/commwiki/wiki?40853
genexus_version: "18"
---

# Sample: GeneXus Cognitive API proof of concept

This article refers to the proof of concept made during the [GeneXus Meeting #28 conference](https://gx28.genexus.com/session/ia-para-todos-con-genexus/EN) about GeneXusAI.

## [Sample download](#Sample+download)

`[imagen omitida: wiki id 40856]` [Sample - GeneXusAI PoC](https://wiki.genexus.com/commwiki/wiki?46073,,)  
`[imagen omitida: wiki id 40856]` [Sample - GeneXusAI PoC (up to GeneXus 16 Upgrade 8)](https://wiki.genexus.com/commwiki/wiki?40855,,)

**Note**: It is highly important to install GeneXusAI built-in module **before importing** the *GeneXusAI\_Sample.xpz* file into your Knowledge Base.

## [GeneXusAI built-in module installation](#GeneXusAI+built-in+module+installation)

1. Go to Knowledge Base option from the GeneXus Toolbar.  
2. Click on [Manage Module References](https://wiki.genexus.com/commwiki/wiki?40172).  
3. Look for GeneXusAI module on the displayed list.  
4. Click on the "Install" button.

You could see the installation process on the 'General' option of the output section. Once installed, you can import the *GeneXusAI\_Sample.xpz* file using the [Knowledge Manager Import](https://wiki.genexus.com/commwiki/wiki?3179).

## [Sample content](#Sample+content)

The Knowledge Base includes:

* **GXAI\_SD menu**  
  The main object, organized in three Tabs.
* **Panels folder**
  + ***SampleAudio panel***:The first tab on the Menu which adds Audio module's AI task ([SpeechToText](https://wiki.genexus.com/commwiki/wiki?40169) and [TextToSpeech](https://wiki.genexus.com/commwiki/wiki?40170)).
  + ***SampleImage panel***: The second tab on the Menu which adds Image module's AI task ([DetectFaces](https://wiki.genexus.com/commwiki/wiki?40177) and [OCR](https://wiki.genexus.com/commwiki/wiki?40180)).
  + ***SampleText panel***: The third tab on the Menu which adds Text module's AI task ([Translate](https://wiki.genexus.com/commwiki/wiki?40185), [DetectLanguage](https://wiki.genexus.com/commwiki/wiki?40181) and [SentimentAnalysis](https://wiki.genexus.com/commwiki/wiki?40184)).
* **Utilities folder**
  + ***GetProvider procedure***: Get a provider configuration from a name.
  + ***SquareRegions procedure***: Transform rectangular regions (as [OutputRegion data type](https://wiki.genexus.com/commwiki/wiki?40194)) to square regions (based on outputSquare data type, included on this sample). It is used with DetectFaces and OCR for drawing the detected areas using [SD Image Map control](https://wiki.genexus.com/commwiki/wiki?17823) over a Grid control.
  + ***AddDelay function***: A simple function used for displaying the output phrase of [SpeechToText](https://wiki.genexus.com/commwiki/wiki?40169) word by word.
  + ***GetBlobUrl procedure***: A helper function that takes a blob as input and retrieves the URL on the server-side. This object is not used by default. See Notes section for detailed information about its purpose.

## [Runtime execution](#Runtime+execution)

The application is a simple proof of content for some GeneXusAI task. It is distributed in three tabs representing each available submodule: Audio, Image, and Text.

### [1st tab: Audio module](#1st+tab%3A+Audio+module)

|  |  |
| --- | --- |
|  | This first tab allows you to execute the Audio module tasks: [SpeechToText procedure](https://wiki.genexus.com/commwiki/wiki?40169) and [TextToSpeech procedure](https://wiki.genexus.com/commwiki/wiki?40170).  As a user, you can input your text and tap on the TextToSpeech button for synthesizing the voice and listening to it. Analogously, you can record your voice with the SpeechToText button a transcribe it, which transcription will be displayed on the same edit field that you input text. Besides, for TextToSpeech, you can format your input text using SSML tags. The 'quotes' button on the top right will format your text with some of these tags (with *prosody* and *say-as*) once you had copied a segment of your text to the clipboard. When you listen the result will appreciate how the output voice changes.  This panel, in addition to GeneXusAI, only use Audio and AudioRecorder external objects for playing and recording audio streams. There is also two effects that you might consider attractive for an application: 1) Audio recording/playing progress, and 2) Word-by-word displaying result |

### [2nd tab: Image module](#2nd+tab%3A+Image+module)

|  |  |
| --- | --- |
|  | This second tab allows you to execute two Image module tasks: [GeneXus Cognitive API - DetectFaces procedure](https://wiki.genexus.com/commwiki/wiki?40177) and [GeneXus Cognitive API - OCR procedure](https://wiki.genexus.com/commwiki/wiki?40180).  As a user, first you must take a picture or select a photo from your gallery. Once displayed on the screen, you can execute DetectFaces or OCR tasks from their respective buttons in order to identify faces or text on that image.  This panel, besides the usage of Camera and PhotoLibrary external object for upload an image, it uses [SD Image Map control](https://wiki.genexus.com/commwiki/wiki?17823) for drawing rectangles over a background image (in this case, our picture). Due to the limitations of such controls, rectangular regions (top, left, width and height) retrieved from GeneXusAI are transformed to squares (top, left, size) that best fits the original rectangle. Also, this panel allows you to edit the faces/text tags with your own content (as you were tagging a picture on your social media app). |

### [3rd tab: Text module](#3rd+tab%3A+Text+module)

|  |  |
| --- | --- |
|  | This third tab allows you to execute three Text module tasks: [GeneXus Cognitive API - DetectLanguage procedure](https://wiki.genexus.com/commwiki/wiki?40181), [GeneXus Cognitive API - Translate procedure](https://wiki.genexus.com/commwiki/wiki?40185) and [GeneXus Cognitive API - SentimentAnalysis procedure](https://wiki.genexus.com/commwiki/wiki?40184).  As a user, you can input a text and tap on the Translate button for displaying the language to be translated or tap on the thumb up/down button for analyzing the sentiment of your input opinion. In this last case, the result will be a happy face (when the score is higher than 0.5), a sad face (when the score is lower than 0.5) or both at the same time (when the score is exactly 0.5). The translation will take the input language 'automatically' calling the DetectLanguage procedure for identifying the language where your text has been written. |

## [Notes](#Notes)

* If you are working with GeneXus 16 Upgrade 0 you must send every media content to the server-side and get its URL. To achieve such aim there is a *GetBlobUrl procedure* object. You simply call it and reset the media content to it.  
    
  For example, if you have an assignment like this:

  ```
  &image = Camera.TakePhoto()
  ```

  You must add the following lines before calling a GeneXusAI task:

  ```
  &image = Camera.TakePhoto()
  /*NEW*/ &blob = &image
  /*NEW*/ &blob = GetBlobUrl(&blob)
  /*NEW*/ &image = &blob
  ```

  The same lines applies for Images and Audio media data types.  
  Refer to [SAC#44045](https://www.genexus.com/es/developers/websac?data=44045;;) for detailed information.

## [See also](#See+also)

* [AI for everyone with GeneXus, GX #28, Proof of concept video](https://youtu.be/v2kGhwE__po?t=1235).


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) |

---
