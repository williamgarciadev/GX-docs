---
title: "GeneXus Framework for SAP Leonardo"
source_id: 41858
source_url: https://wiki.genexus.com/commwiki/wiki?41858
genexus_version: "18"
---

# GeneXus Framework for SAP Leonardo

In GeneXus, we have a module called GeneXusAI, where we integrate the most common Artificial Intelligence (AI) functions provided by various cloud providers.

One of these providers is SAP with its SAP Leonardo solution.

In particular, we developed a [Knowledge Base (KB)](https://wiki.genexus.com/commwiki/wiki?1836) which we named GeneXus Framework for SAP Leonardo, where we included examples of the use of the free services available in the  [SAP API Business Hub](https://api.sap.com/landingPage.html) within [Business Services](https://api.sap.com/#/shell/businessservice), in the section [SAP Leonardo ML - Functional Services](https://api.sap.com/#/shell/discover/contentpackage/SAPLeonardoMLFunctionalServices).

SAP Leonardo is presented as “your digital innovation system, bringing new technologies and services together to help businesses power their digital transformation”.

It is an API that includes REST services which can be consumed for different purposes, basically covering the following areas:

* Internet of Things
* Machine Learning
* Blockchain

We call this KB GeneXus Framework for SAP Leonardo ([see the Framework running](http://labsnet.genexuscloud.com/GXSAPLeonardoFWK/FioriBaseObjects.FioriLaunchpad.aspx)), which is not only used to show the possibilities of GeneXus and SAP Leonardo together but also as a starting point to study the code of each example and easily replicate it to the needs of each developer. Although today we include the examples/services that will be detailed below, it is incremental and we will continue to add more examples/services. In the same way, each time you can include what is considered as its development, use together, GeneXus, OpenAPI Import and GeneXusAI, as SAP releases new services.

Below we explain the examples included in the Knowledge Base that can be obtained by two ways:

* Creating a new KB from GeneXus Server and choosing [this KB](https://samples.genexusserver.com/v16/kbdashboard.aspx?GeneXusFrameworkSAPLeonardoV1) (V1 for GX16)

or

* Import [this xpz](https://wiki.genexus.com/commwiki/wiki?42374,,) (V1 for GX16) to your KB (in this case you should already have [GeneXus SDK for SAP Leonardo](https://wiki.genexus.com/commwiki/wiki?39906) in your KB).

`[imagen omitida: wiki id 40039]`

**OCR**

Service used: [Optical Character Recognition (OCR) API](https://api.sap.com/shell/discover/contentpackage/SAPLeonardoMLFunctionalServices/api/ocr_api?section=RESOURCE)  
Optical Character Recognition service takes an uploaded file and returns the text characters detected in the input.

Running:  
You enter images that contain some text but in .jpeg, .jpe, or .png format and then for each loaded image you can select the Recognize option.

You can select some parameters in order to change the behavior of the recognition service and when you press confirm, you invoke the SAP Leonardo service which converts the image to text.

`[imagen omitida: wiki id 40040]`

**Scene Text**

Service used: [Scene Text Recognition](https://api.sap.com/api/scene_text_recognition_api)  
Localizes and extracts text from natural images and scenes.

Running:  
An image is entered and when selected the Detect texts option, it is sent to the SAP Leonardo service, which detects texts in the image indicating the text, in txt format and its position within the image. The application, according to this position, marks the texts in the image.

`[imagen omitida: wiki id 40651]`

**Image Classification**

Service used: [Image Classifier Service](https://api.sap.com/shell/discover/contentpackage/SAPLeonardoMLFunctionalServices/api/image_classification_api)  
Detects the dominant objects present in an image from a set of 1000 categories such as trees, animals, food, vehicles, people, and more.

See also [Retraining Service for image classification](https://api.sap.com/shell/discover/contentpackage/SAPLeonardoMLFunctionalServices/api/retraining_service_imgc_api)

Running:  
Images are entered in jpg, jpe, jpeg, png, gif, bmp, tif or tiff format and then for each loaded image you can select the option Classify.

`[imagen omitida: wiki id 40041]`

**Similarity Image**

Service used: [Image Feature Extraction API](https://api.sap.com/shell/discover/contentpackage/SAPLeonardoMLFunctionalServices/api/img_feature_extraction_api) y [Similarity Scoring API](https://api.sap.com/shell/discover/contentpackage/SAPLeonardoMLFunctionalServices/api/similarity_scoring_api?section=RESOURCE)  
Image Feature Extraction API  
Is capable of extracting feature vectors for any given image which can be used for comparison, informational retrieval, clustering or further processing.

Similarity Scoring API  
Compares vectors using a similarity score (cosine distance) ranging from -1 to 1. The similarity score is calculated based on the cosine similarity of the vectors. The vectors retrieved from the "image feature extraction" and "document feature extraction" services can be used as inputs for this service.

Running:  
You enter pairs of images in different formats, such as .jpeg, .png, .tif or .bmp and then for each pair of loaded images you can select the Compare option.

This option calls the Image Feature Extraction service for each image with which it obtains the vector of characteristics of each, then sends both vectors to the Similarity Scoring service and returns the similarity between them.

`[imagen omitida: wiki id 40042]`

**Text Classification**

Service used: [Product Text Classification API](https://api.sap.com/shell/discover/contentpackage/SAPLeonardoMLFunctionalServices/api/product_text_classification_api)  
The model for this service was obtained by training a text classifier on approximately 300k Icecat product texts. There are 50 categories available: All-in-One PCs workstations, LED TVs, NAS & storage servers, PCs workstations, USB cables, USB flash drives, antivirus security software, cable interface gender adapters, computer monitors, digital cameras, fiber optic cables, flat panel spare parts, graphics cards, ink cartridges, internal hard drives, keyboards, laser LED printers, laser toner & cartridges, memory modules, mice, mobile phone cases, motherboards, mounting kits, multifunctionals, network switches, networking cables, networking cards, notebook cases, notebook spare parts, notebooks, other, power adapters & inverters, power cables, printer kits, printer scanner spare parts, processors, projection screens, projector mounts, rechargeable batteries, screen protectors, servers, smartphones, software licenses upgrades, solid state drives, tablet cases, tablets, thin clients, uninterruptible power supplies (UPSs), warranty & support extensions, washing machines.

Running:  
In this example, we enter a product, but where the important thing, that is, based on what we will classify it, is its description. Once entered, we click on the Classify option and the system invokes the Product Text Classification service and classifies it based on its description.

`[imagen omitida: wiki id 40043]`

**Face Detection**

Service used: [Face Detection API](https://api.sap.com/api/face_detection_api)  
Detects faces in images and, if any, returns bounding box per face for every image.

Running:  
A photo is entered and when Detect Faces is selected, the image is sent to the SAP Leonardo service, which identifies the number of faces in the image and indicates the position of each one. The application marks the faces, according to this position, in the image.

`[imagen omitida: wiki id 40649]`

**Language Detection**

Service used: [Language Detection API](https://api.sap.com/shell/discover/contentpackage/SAPLeonardoMLFunctionalServices/api/language_detection_api)  
An API to detect the language of any given string of text data.

Running:  
In the box 'Text to Detect Language' a phrase is entered in any language, by pressing Detect Language, this text is sent to SAP Leonardo who infers the language in which it is written indicating an index of certainty.

`[imagen omitida: wiki id 40044]`

**Multilanguage Chat**

Service used: [Translation API](https://api.sap.com/shell/discover/contentpackage/SAPLeonardoMLFunctionalServices/api/translation_api)  
Translation API translates multiple translation units from a source language into multiple target languages.

Running:  
In order to show through a use case, the functioning of the SAP Leonardo translation service, a multi-language chat is implemented, also taking advantage of the GeneXus [Web Notification](https://wiki.genexus.com/commwiki/wiki?36952,,) feature.

When executing the application, from different computers (in order to emulate this by running on a single computer, you can raise the application in different browsers, where each emulate a user), the user language of the application is indicated on each computer and at this moment you can start sending messages, writing them in the 'My message' box and pressing SEND.

The system takes the message and invokes the SAP Leonardo translation service, setting as the source language the one indicated on the page and as the target language English. Then it performs the broadcast of said message to each connected user. Upon receipt, the message will be displayed in the Chat box, but previously, the message received is sent to the translation service of SAP Leonardo to translate it from English (language in which it is received) to the Language indicated by each Client.

`[imagen omitida: wiki id 40045]`
