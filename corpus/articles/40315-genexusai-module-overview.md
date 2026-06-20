---
title: "GeneXusAI Module Overview"
source_id: 40315
source_url: https://wiki.genexus.com/commwiki/wiki?40315
genexus_version: "18"
---

# GeneXusAI Module Overview

GeneXusAI is an installable module that aims to simplify the integration of cognitive services most common capabilities in GeneXus.

## [What do you have to do to include these tasks?](#What+do+you+have+to+do+to+include+these+tasks%3F)

You have to install **GeneXusAI module** from the [Manage Module References](https://wiki.genexus.com/commwiki/wiki?40172) dialog on the Knowledge Manager option (located in the toolbar of GeneXus IDE). Once you installed it, you must configure your desired provider and set the appropriate properties for each task (credentials, deployment information, optional parameters, etc.).

## [Which providers are supported?](#Which+providers+are+supported%3F)

Supported providers are:

* [Watson by IBM](https://console.bluemix.net/developer/watson/documentation)
* [Cognitive Services by Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/)
* [Leonardo by SAP](https://api.sap.com/package/SAPLeonardoMLFunctionalServices)
* [Cloud AI by Google Services](https://cloud.google.com/products/ai/)
* [Machine Learning by Amazon Web Services](https://aws.amazon.com/es/machine-learning/)
* [AI Open Platform by Tencent](https://ai.qq.com/doc/index.shtml)
* [AI Brain by Baidu](https://ai.baidu.com/)
* [Aliyun Data Intelligence by Alibaba](https://ai.aliyun.com/?spm=a2c4g.11186623.1280361.27.5847271cqUafgZ)
* [ML Kit by Firebase (Google)](https://developers.google.com/ml-kit)

For detailed information, refer to the backlog in [GeneXus Cognitive API - Release notes](https://wiki.genexus.com/commwiki/wiki?40201) article.

## [Which AI tasks are available?](#Which+AI+tasks+are+available%3F)

GeneXusAI is structured as follows. Each submodule has specific procedures, domains, and structured data types that allow you to integrate your desired task.

```
GeneXusAI
├── Configuration
├── Audio
│   ├── SpeechToText
│   └── TextToSpeech
├── Custom
│   ├── Check
│   ├── Delete
│   ├── Deploy
│   ├── Evaluate
│   ├── Predict
│   └── Train
├── Image
│   ├── Classify 
│   ├── DetectFaces
│   ├── DetectObjects
│   ├── DetectScene
│   └── OCR
├── Text
│   ├── DetectLanguage
│   ├── ExtractEntitites
│   ├── KeyPhrases
│   ├── SentimentAnalysis
│   └── Translate
└── Video
    ├── Analyze
    └── Process
```

The availability of a service depends on the provider you chose (summarized in the following table), as well as its pricing, accuracy, and performance. Some empirical tests for these last two features are described on the documentation for each task. Pricing must be consulted on the provider's website.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **GeneXus AI** | |  | **Cloud-based  providers** | | | |  | **On-device  providers** | |
| **Module** | **Task** |  | **Amazon** | **Google** | **IBM** | **Microsoft** |  | **MLKit** | **CoreML** |
| **Audio** | [SpeechToText](https://wiki.genexus.com/commwiki/wiki?40169) |  | **✓** | **✓** | **✓** | **✓** |  | – | **⧖** |
| [TextToSpeech](https://wiki.genexus.com/commwiki/wiki?40170) |  | **✓** | **✓** | **✓** | **✓** |  | – | **⧖** |
| **Custom** | [Check](https://wiki.genexus.com/commwiki/wiki?44242) |  | – | **✓** | **✓** | **✓** |  | – | – |
| [Delete](https://wiki.genexus.com/commwiki/wiki?44243) |  | – | **✓** | **✓** | **✓** |  | – | – |
|  | [Deploy](https://wiki.genexus.com/commwiki/wiki?44247) |  | – | **✓** | – | **✓** |  | – | – |
|  | [Evaluate](https://wiki.genexus.com/commwiki/wiki?44244) |  | – | **✓** | – | **✓** |  | – | – |
|  | [Predict](https://wiki.genexus.com/commwiki/wiki?44245) |  | – | **v** | **✓** | **✓** |  | – | – |
|  | [Train](https://wiki.genexus.com/commwiki/wiki?44246) |  | – | **✓** | **✓** | **✓** |  | – | – |
| **Image** | [Classify](https://wiki.genexus.com/commwiki/wiki?40171) |  | **✓** | **✓** | **⚠** | **✓** |  | **⚠** | **⧖** |
| [DetectFaces](https://wiki.genexus.com/commwiki/wiki?40177) |  | **✓** | **✓** | **⚠** | **✓** |  | **⚠** | – |
| [DetectObjects](https://wiki.genexus.com/commwiki/wiki?40178) |  | **✓** | **✓** | – | **✓** |  | **⚠** | – |
| [DetectScene](https://wiki.genexus.com/commwiki/wiki?40179) |  | **✓** | **✓** | – | **✓** |  | **⚠** | – |
| [OCR](https://wiki.genexus.com/commwiki/wiki?40180) |  | **✓** | **✓** | **⚠** | **✓** |  | **⚠** | – |
| **Text** | [DetectLanguage](https://wiki.genexus.com/commwiki/wiki?40181) |  | **✓** | **✓** | **✓** | **✓** |  | **⚠** | **⧖** |
| [ExtractEntitites](https://wiki.genexus.com/commwiki/wiki?40182) |  | **✓** | **✓** | **✓** | **✓** |  | – | **⧖** |
| [KeyPhrases](https://wiki.genexus.com/commwiki/wiki?40183) |  | **✓** | **✓** | **✓** | **✓** |  | – | – |
| [SentimentAnalysis](https://wiki.genexus.com/commwiki/wiki?40184) |  | **✓** | **✓** | **✓** | **✓** |  | – | – |
| [Translate](https://wiki.genexus.com/commwiki/wiki?40185) |  | **✓** | **✓** | **✓** | **✓** |  | **⚠** | – |
| **Video** | [Analyze](https://wiki.genexus.com/commwiki/wiki?41041) |  | – | **✓** | – | **✓** |  | – | – |
| [Process](https://wiki.genexus.com/commwiki/wiki?41042) |  | – | **✓** | – | **✓** |  | – | – |
|  |  |  |  |  |  |  |  |  |  |

**Reference**:  
**+** **✓**: Available  
**+ –**: Not provided  
**+** **⧖**: Work in progress  
**+⚠**: Deprecated/Decommissioned

## [What if you want to use another service that is not provided?](#What+if+you+want+to+use+another+service+that+is+not+provided%3F)

GeneXusAI offers the most common set of functionalities available to most providers. Specific services, for a particular provider, must be developed by hand.

For **cloud-based** providers, you can consume the ReST service by using [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932), or using the [OpenAPI import tool](https://wiki.genexus.com/commwiki/wiki?31864) when the provider exposes a [Swagger descriptor](https://swagger.io/specification/) (either in YAML or JSON), or even by creating an [Native Object](https://wiki.genexus.com/commwiki/wiki?6148) that wraps the provider's library. This last alternative is the one you must use for **device-inference** providers, which must be implemented by the [Extension Library concept](https://wiki.genexus.com/commwiki/wiki?33545).

## [What do you have to do to set up a specific provider?](#What+do+you+have+to+do+to+set+up+a+specific+provider%3F)

You must fully set the &provider input parameter before calling any procedure (the AI task) with the required properties for the provider you've chosen.

For example, if you want to use [GeneXus Cognitive API - DetectFaces procedure](https://wiki.genexus.com/commwiki/wiki?40177) with Microsoft Azure Cognitive Services, you should write something like this:

```
// Instanciate the provider. In this case, Microsoft.
&provider = new() 
&provider.Name = "my-microsoft-face-recognition-instance-1"
&provider.Type = ProviderType.Microsoft

// Add the required properties. In this case, the API-Key provided by Microsoft.
&providerProperty = new()
&providerProperty.key   = PropertyKey.Key
&providerProperty.Value = !"{your_microsoft_visual_recognition_key}"
&provider.Properties.Add(&providerProperty)

// Call to GeneXusAI's procedure and get the result.
&regions = GeneXusAI.Image.DetectFaces(&image, &provider, &messages)
```

|  |  |
| --- | --- |
| **Where:** |  |
| &provider | : [Provider, GeneXusAI.Configuration](https://wiki.genexus.com/commwiki/wiki?40197) |
| &providerProperty | : [Provider.Property, GeneXusAI.Configuration](https://wiki.genexus.com/commwiki/wiki?40197) |

You can reuse the &provider definition for multiple services when they share the credentials. If you add duplicated properties, GeneXusAI will always consider the last one you added.

**Note**: Each procedure (or AI task) of GeneXusAI will have specific requirements, especially in terms of service authentication credentials (read [HowTo: Get credentials from a cloud provider for GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40204)). Detailed information can be found on the procedure's documentation you want to use.

## [Can you build a custom model in GenexusAI?](#Can+you+build+a+custom+model+in+GenexusAI%3F)

Yes. Refer to [HowTo: Build a custom model for GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?43665).

## [Why should you use GenexusAI?](#Why+should+you+use+GenexusAI%3F)

First of all, GeneXusAI encapsulates the complexity of learning specific solutions. You just only need to call a GeneXus's [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) with the required parameters, and that's all.

Maintenance is not a problem. You don't have to worry about being outdated. You just should update GeneXusAI module when you want or when it is needed.

On the other hand, imagine you already have developed a system that integrates AI in your solution, but some time later you realize that the service does not satisfy your requirements (e.g. in terms of cost, performance, etc.). If you were not using GeneXusAI, you should redesign your system (rewrite API-calls, create new structures or modify preexisting one, etc.). When you use GeneXusAI the only thing you do is to redefine your &provider input parameter with a new setting for the provider you chose.

Finally, GeneXusAI allows you to use multiple providers by defining multiple &provider instances for each provider you want to use. Then, for example, you can use [GeneXus Cognitive API - DetectFaces procedure](https://wiki.genexus.com/commwiki/wiki?40177) with Microsoft, [GeneXus Cognitive API - Classify procedure](https://wiki.genexus.com/commwiki/wiki?40171) with IBM and [GeneXus Cognitive API - Translate procedure](https://wiki.genexus.com/commwiki/wiki?40185) with Google. In this way, you can find the best balance between cost, performance, and accuracy; both for your users, your system and your business.

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators:** | [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550) |


|  |
| --- |
| **Backlinks** |
| [Table of contents:GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) |
| [HowTo: Get credentials from a cloud provider for GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40204) |

---
