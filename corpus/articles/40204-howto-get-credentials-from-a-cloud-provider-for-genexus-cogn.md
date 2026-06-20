---
title: "HowTo: Get credentials from a cloud provider for GeneXus Cognitive API"
source_id: 40204
source_url: https://wiki.genexus.com/commwiki/wiki?40204
genexus_version: "18"
---

# HowTo: Get credentials from a cloud provider for GeneXus Cognitive API

This article explains how to get the configuration credentials needed to use the [GeneXusAI](https://wiki.genexus.com/commwiki/wiki?40315) Module.

**Note**: For security reasons, as a best practice you should put your credentials into configuration files or environment variables and then read their values from them. Avoid pasting your credentials in your code..

### [Step 1 - Access to provider console](#Step+1+-+Access+to+provider+console)

Login on your AI provider with your credentials (with previous registration).

* [Alibaba Aliyun console](http://home.console.aliyun.com)
* [Amazon Web Services console](https://console.aws.amazon.com)
* [Baidu Cloud Environment console](https://login.bce.baidu.com/)
* [Google Cloud AI console](https://console.developers.google.com/apis/credentials)
* [IBM Bluemix console](https://console.bluemix.net/)
* [Microsoft Azure portal](https://portal.azure.com/)
* [SAP Leonardo functional services](https://api.sap.com/package/SAPLeonardoMLFunctionalServices) (sandbox) or [SAP Cockpit console](https://cockpit.hanatrial.ondemand.com/) (trial/production)
* [Tencent AI console](https://ai.qq.com/console/home)
* [Google Cloud AI console (enable ML Kit API by Firebase)](https://console.cloud.google.com/apis/library/mlkit.googleapis.com)

### [Step 2 - Select the AI service](#Step+2+-+Select+the+AI+service)

After login, you will be redirected to the developer console. Then, from the dashboard, create/enable a new resource for your desired AI task (you can filter services by name). This action usually asks you for a resource *name*, a *region*, and other *general settings* for the service you are creating (such information depends on the provider you use).

#### [Regions supported by provider](#Regions+supported+by+provider)

|  |  |
| --- | --- |
| **Alibaba** | 'Chinese-East-2' (a.k.a 'cn-shanghai') |
| **Amazon** | 'US Standard/US East (N. Virginia)' (a.k.a. 'us-east-1') |
| **Baidu** | 'Beijing' |
| **Google** | N/A |
| **IBM** | 'US South' or 'Dallas' |
| **Microsoft** | 'West US' (except for Video, which uses 'West US 2') |
| **MLKit** | N/A |
| **SAP** | 'Frankfurt' (production/trial) |
| **Tencent** | N/A |

If you do not set the region properly a [GXAI5000 error](https://wiki.genexus.com/commwiki/wiki?40188) will be raised with an '*Authentication Failed*' message

#### [Credentials by task](#Credentials+by+task)

The following table summarizes which service credentials you need (by name) for each task in GeneXusAI. For detailed information, refer to the procedure description page.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Module** | **Task** | |  |  |  | | --- | --- | --- | | **Provider** | **Service** | **Credentials** | |
| **Audio** | [SpeechToText](https://wiki.genexus.com/commwiki/wiki?40169) | |  |  |  | | --- | --- | --- | | **Alibaba** | 智能语音交互 | Id, Key, SecretKey | | **Amazon** | Transcribe | Key, SecretKey | | **Baidu** | 百度语音 | Id, Key, SecretKey | | **Google** | Cloud Speech-to-text API | Key | | **IBM** | Speech To Text | Key | | **Microsoft** | Speech | Key | | **MLKit** | ML Kit API | - | | **SAP** | N/A | - | | **Tencent** | 语音识别 | Id, Key | |
| [TextToSpeech](https://wiki.genexus.com/commwiki/wiki?40170) | |  |  |  | | --- | --- | --- | | **Alibaba** | 智能语音交互 | Id, Key, SecretKey | | **Amazon** | Polly | Key, SecretKey | | **Baidu** | 百度语音 | Id, Key, SecretKey | | **Google** | Cloud Text-to-speech API | Key | | **IBM** | Text To Speech | Key | | **Microsoft** | Speech | Key | | **MLKit** | ML Kit API | - | | **SAP** | N/A | - | | **Tencent** | 音合成 | Id, Key | |
| **Custom** | [Check](https://wiki.genexus.com/commwiki/wiki?44242) | |  |  |  | | --- | --- | --- | | **Alibaba** | N/A | - | | **Amazon** | N/A | - | | **Baidu** | N/A | - | | **Google** | Auto ML Service-Account JSON | Key | | **IBM** | Visual Recognition | Key | | **Microsoft** | Custom Vision Training | Key | | **MLKit** | ML Kit API | - | | **SAP** | Sandbox | Key | | **Tencent** | N/A | - | |
|  | [Delete](https://wiki.genexus.com/commwiki/wiki?44243) | |  |  |  | | --- | --- | --- | | **Alibaba** | N/A | - | | **Amazon** | N/A | - | | **Baidu** | N/A | - | | **Google** | Auto ML Service-Account JSON | Key | | **IBM** | Visual Recognition | Key | | **Microsoft** | Custom Vision Training | Key | | **MLKit** | ML Kit API | - | | **SAP** | Sandbox | Key | | **Tencent** | N/A | - | |
|  | [Deploy](https://wiki.genexus.com/commwiki/wiki?44247) | |  |  |  | | --- | --- | --- | | **Alibaba** | N/A | - | | **Amazon** | N/A | - | | **Baidu** | N/A | - | | **Google** | Auto ML Service-Account JSON | Key | | **IBM** | Visual Recognition | Key | | **Microsoft** | Custom Vision Training | Key | | **MLKit** | ML Kit API | - | | **SAP** | Sandbox | Key | | **Tencent** | N/A | - | |
|  | [Evaluate](https://wiki.genexus.com/commwiki/wiki?44244) | |  |  |  | | --- | --- | --- | | **Alibaba** | N/A | - | | **Amazon** | N/A | - | | **Baidu** | N/A | - | | **Google** | Auto ML Service-Account JSON | Key | | **IBM** | Visual Recognition | Key | | **Microsoft** | Custom Vision Training | Key | | **MLKit** | ML Kit API | - | | **SAP** | Sandbox | Key | | **Tencent** | N/A | - | |
|  | [Predict](https://wiki.genexus.com/commwiki/wiki?44245) | |  |  |  | | --- | --- | --- | | **Alibaba** | N/A | - | | **Amazon** | N/A | - | | **Baidu** | N/A | - | | **Google** | Auto ML Service-Account JSON | Key | | **IBM** | Visual Recognition | Key | | **Microsoft** | Custom Vision Prediction | Key | | **MLKit** | ML Kit API | - | | **SAP** | Sandbox | Key | | **Tencent** | N/A | - | |
|  | [Train](https://wiki.genexus.com/commwiki/wiki?44246) | |  |  |  | | --- | --- | --- | | **Alibaba** | N/A | - | | **Amazon** | N/A | - | | **Baidu** | N/A | - | | **Google** | Auto ML Service-Account JSON | Key | | **IBM** | Visual Recognition | Key | | **Microsoft** | Custom Vision Training | Key | | **MLKit** | ML Kit API | - | | **SAP** | Sandbox | Key | | **Tencent** | N/A | - | |
| **Image** | [Classify](https://wiki.genexus.com/commwiki/wiki?40171) | |  |  |  | | --- | --- | --- | | **Alibaba** | 用户 | Key, SecretKey | | **Amazon** | Rekognition | Key, SecretKey | | **Baidu** | 视觉技术 | Id, Key, SecretKey | | **Google** | Cloud Vision | Key | | **IBM** | Visual Recognition | Key | | **Microsoft** | Computer Vision | Key | | **MLKit** | ML Kit API | Id, Key | | **SAP** | Sandbox | Key | | **Tencent** | 多标签识别 | Id, Key | |
| [DetectFaces](https://wiki.genexus.com/commwiki/wiki?40177) | |  |  |  | | --- | --- | --- | | **Alibaba** | 用户 | Key, SecretKey | | **Amazon** | Rekognition | Key, SecretKey | | **Baidu** | 视觉技术 | Id, Key, SecretKey | | **Google** | Cloud Vision | Key | | **IBM** | Visual Recognition  (deprecated on Sep 12th, 2019) | Key | | **Microsoft** | Computer Vision | Key | | **MLKit** | ML Kit API | Id, Key | | **SAP** | Sandbox | Key | | **Tencent** | 人脸检测与分析 | Id, Key | |
| [DetectObjects](https://wiki.genexus.com/commwiki/wiki?40178) | |  |  |  | | --- | --- | --- | | **Alibaba** | N/A | - | | **Amazon** | Rekognition | Key, SecretKey | | **Baidu** | N/A | - | | **Google** | Cloud Vision | Key | | **IBM** | N/A | - | | **Microsoft** | Computer Vision | Key | | **MLKit** | ML Kit API | Id, Key | | **SAP** | N/A | - | | **Tencent** | 物体识别 | Id, Key | |
| [DetectScene](https://wiki.genexus.com/commwiki/wiki?40179) | |  |  |  | | --- | --- | --- | | **Alibaba** | 用户 | Key, SecretKey | | **Amazon** | Rekognition | Key, SecretKey | | **Baidu** | 视觉技术 | Id, Key, SecretKey | | **Google** | Cloud Vision | Key | | **IBM** | N/A | - | | **Microsoft** | Computer vision | Key | | **MLKit** | ML Kit API | Id, Key | | **SAP** | N/A | - | | **Tencent** | 场景识别 | Id, Key | |
| [OCR](https://wiki.genexus.com/commwiki/wiki?40180) | |  |  |  | | --- | --- | --- | | **Alibaba** | 用户 | Key, SecretKey | | **Amazon** | Rekognition | Key, SecretKey | | **Baidu** | 视觉技术 | Id, Key, SecretKey | | **Google** | Cloud Vision | Key | | **IBM** | Visual Recognition  (deprecated on Sep 12th, 2019) | Key | | **Microsoft** | Computer vision | Key | | **MLKit** | ML Kit API | Id, Key | | **SAP** | Sandbox | Key | | **Tencent** | 通用OCR | Id, Key | |
| **Text** | [DetectLanguage](https://wiki.genexus.com/commwiki/wiki?40181) | |  |  |  | | --- | --- | --- | | **Alibaba** | N/A | - | | **Amazon** | Comprehend | Key, SecretKey | | **Baidu** | 通用翻译 | Id, Key, SecretKey | | **Google** | Cloud Translation | Key | | **IBM** | Language Translator | Key | | **Microsoft** | Translator Text | Key | | **MLKit** | ML Kit API | Id, Key | | **SAP** | Sandbox | Key | | **Tencent** | 语种识别 | Id, Key | |
| [ExtractEntitites](https://wiki.genexus.com/commwiki/wiki?40182) | |  |  |  | | --- | --- | --- | | **Alibaba** | N/A | - | | **Amazon** | Comprehend | Key, SecretKey | | **Baidu** | 自然语言 | Id, Key, SecretKey | | **Google** | Cloud Natural Language | Key | | **IBM** | Natural Language Understanding | Key | | **Microsoft** | Text Analytics | Key | | **MLKit** | ML Kit API | - | | **SAP** | N/A | - | | **Tencent** | 专有名词 | Id, Key | |
| [KeyPhrases](https://wiki.genexus.com/commwiki/wiki?40183) | |  |  |  | | --- | --- | --- | | **Alibaba** | 用户 | Key, SecretKey | | **Amazon** | Comprehend | Key, SecretKey | | **Baidu** | 自然语言 | Id, Key, SecretKey | | **Google** | Cloud Natural  Language | Key | | **IBM** | Natural Language Understanding | Key | | **Microsoft** | Text Analytics | Key | | **MLKit** | ML Kit API | - | | **SAP** | N/A | - | | **Tencent** | N/A | - | |
| [SentimentAnalysis](https://wiki.genexus.com/commwiki/wiki?40184) | |  |  |  | | --- | --- | --- | | **Alibaba** | 用户 | Key, SecretKey | | **Amazon** | Comprehend | Key, SecretKey | | **Baidu** | 自然语言 | Id, Key, SecretKey | | **Google** | Cloud Natural Language | Key | | **IBM** | Natural Language Understanding | Key | | **Microsoft** | Text Analytics | Key | | **MLKit** | ML Kit API | - | | **SAP** | N/A | - | | **Tencent** | 专有名词 | Id, Key | |
| [Translate](https://wiki.genexus.com/commwiki/wiki?40185) | |  |  |  | | --- | --- | --- | | **Alibaba** | 用户 | Key, SecretKey | | **Amazon** | Translate | Key, SecretKey | | **Baidu** | 通用翻译 | Id, Key, SecretKey | | **Google** | Cloud Translation | Key | | **IBM** | Language Translator | Key | | **Microsoft** | Translator Text | Key | | **MLKit** | ML Kit API | Id, Key | | **SAP** | Sandbox | Key | | **Tencent** | 文本翻译 | Id, Key | |
| **Video** | [Analyze](https://wiki.genexus.com/commwiki/wiki?41041) | |  |  |  | | --- | --- | --- | | **Alibaba** | 内容安全 | Id, Key, SecretKey | | **Amazon** | N/A | - | | **Baidu** | 视频内容分析 | Key, SecretKey | | **Google** | Video Intelligence | Key | | **IBM** | N/A | - | | **Microsoft** | Video Indexer | Key, Account | | **MLKit** | ML Kit API | - | | **SAP** | N/A | - | | **Tencent** | N/A | - | |
| [Process](https://wiki.genexus.com/commwiki/wiki?41042) | |  |  |  | | --- | --- | --- | | **Alibaba** | 内容安全 | Id, Key SecretKey | | **Amazon** | N/A | - | | **Baidu** | 视频内容分析 | Key, SecretKey | | **Google** | Video Intelligence | Key | | **IBM** | N/A | - | | **Microsoft** | Video Indexer | Key, Account | | **MLKit** | ML Kit API | - | | **SAP** | N/A | - | | **Tencent** | N/A | - | |
|  |  |  |

### [Step 3 - Generate and set the credentials](#Step+3+-+Generate+and+set+the+credentials)

Once your service has been created, the provider shows you the credentials you need. Also, these credentials will be located in a "Resource Management" section (or similar) in the provider's webpage in case you want to retrieve them again or regenerate them when it is needed. Once you get the credentials values, you simply set it properly on the corresponding [Provider.Property field](https://wiki.genexus.com/commwiki/wiki?40197).

For example, for an **API-key** **scenario**, you can write a code like this:

```
&provider = new()

&provider.Name = !"{your_environment_name}"
&provider.Type = ProviderType.[Amazon|Baidu|Google|IBM|Microsoft|MLKit|SAP|Tencent]

&providerProperty= new()
&providerProperty.key = GeneXusAI.Configuration.PropertyKey.Key
&providerProperty.Value = !"{your_api_key_value}" // LINE (*)
&provider.Properties.Add(&providerProperty)
```

|  |  |
| --- | --- |
| **Where:** |  |
| *&provider* | : [Provider, GeneXusAI.Configuration](https://wiki.genexus.com/commwiki/wiki?40197) |
| *&providerProperty* | : [Provider.Property, GeneXusAI.Configuration](https://wiki.genexus.com/commwiki/wiki?40197) |

Please note that "{your\_api\_key\_value}" value should not be pasted into your production code. As a best practice, you should read it from a configuration file or environment variable. For example, you can create a JSON file called '*provider.settings.json*' with the following structure:

```
{
    "name":"{your_provider_name}",
    "key":"{your_api_key_value}"
}
```

Then, you can attach this file to your Knowledge Base as a File object, set the extraction properties (for copying it to the appropriate location) and read the credentials as follows:

```
&settingFile.Source = !"path/to/provider.settings.json"
&jsonString = &file.ReadAllText()       // read configuration file
&jsonProperties.FromJson(&jsonString)   // parse json structure
&myApiKey = &jsonProperties.Get(!"key") // get "{your_api_key_value}" value
```

Finally, you can replace **LINE (\*)** with the following sentence:

```
&providerProperty.Value = &myApiKey
```

### [Step 4 - Execute your AI task](#Step+4+-+Execute+your+AI+task)

You will be able to execute your AI task!

**Notes:**

* For **SAP Leonardo**, Sandbox key can be retrieved on each API service by the "Show API Key" option and will be the same no matter what service you choose. For such reason, the documentation does not specify which service you should use (e.g. *Inference Service for Optical Character Recognition (OCR)* if you use GeneXusAI.Image.OCR task) due to the API key will be the same for every service.
* For **IBM Watson**, when you create a new resource, ensure to choose 'US South' region. Those services that allow authentication by username/password are maintained for backward compatibility (new instances will give you a key, not a username/password).
* For **Google Cloud AI**, you must create a single project and enable each API you desire to use. Then, on the "Credentials" option, you will able to create an API key for all those APIs you enabled.

### [Availability](#Availability)

* This document applies since [GeneXus 16](https://wiki.genexus.com/commwiki/wiki?35351,,).
* Google Cloud AI provider is available since [GeneXus 16 upgrade 1](https://wiki.genexus.com/commwiki/wiki?40782,,).


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) | [GeneXus Cognitive API - Analyze procedure](https://wiki.genexus.com/commwiki/wiki?41041) |
| [GeneXus Cognitive API - Process procedure](https://wiki.genexus.com/commwiki/wiki?41042) | [GeneXusAI Module Overview](https://wiki.genexus.com/commwiki/wiki?40315) | [PropertyKey domain](https://wiki.genexus.com/commwiki/wiki?40196) |

---
