---
title: "Storage Provider property"
source_id: 31121
source_url: https://wiki.genexus.com/commwiki/wiki?31121
genexus_version: "18"
---

# Storage Provider property

Determines the storage provider for Multimedia files used in the Knowledge Base. It allows selecting among different external storage providers.

### [Values](#Values)

|  |  |
| --- | --- |
| **Amazon S3** | Amazon Simple Storage Service and compatible services. |
| **Amazon S3 V1 (Legacy)** | Amazon Simple Storage Service V1 (Legacy) - This service definition is from the deprecated AWS S3 V1 Java SDK. It is recommended that you avoid using this version in new projects due to possible security and performance improvements in later versions. Only use this legacy version if there are specific project requirements. |
| **Microsoft Azure** | Microsoft Azure Storage Service. |
| **Google Cloud Storage** | Google Cloud Platform Storage Service. |
| **IBM Cloud Object Storage** | IBM Cloud Object Storage Service (IBM COS). |
| **Local** | This is the default value. Multimedia files (audios, videos, and images) are stored locally. |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** Generator

### [Description](#Description)

Depending on the Storage Provider used, different additional properties are available to configure the storage location. These properties are grouped under the Services section.

It's a generator and object property.

`[imagen omitida: wiki id 56620]` At the attribute level, you can configure Use External Storage Provider Property = **{True, False}** for each multimedia attribute. Its main purpose is to determine if one multimedia field will use the same Storage Provider Property settings configured at the generator level. If False is selected, the Local value is assumed.  
It cannot be configured for multimedia variables; in this case, the generator's property value will be used.

Below are the cases for each of the storage providers supported.

#### [Amazon S3 / Amazon S3 V1 (Legacy)](#Amazon+S3+%2F+Amazon+S3+V1+%28Legacy%29)

Use this to access Amazon S3 or any compatible object storage service. Some compatible services are Min.IO, Oracle, and IBM COS (IBM Cloud Object Storage), among others.

The Amazon S3 value points to the [SDK v2](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-s3.html) implementation, while Amazon S3 (Legacy) relates to the previous [SDK v1](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/welcome.html) implementation.

[Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836)s (KBs) that are upgraded from previous versions will automatically adopt Amazon S3 (Legacy) as their default value.

|  |  |
| --- | --- |
| [Storage Access Key ID](https://wiki.genexus.com/commwiki/wiki?56617) | S3 Access Key ID (\*) |
| [Storage Secret Access Key](https://wiki.genexus.com/commwiki/wiki?56619) | S3 Secret Access Key (\*) |
| [Bucket Name property](https://wiki.genexus.com/commwiki/wiki?45733) | To upload your (multimedia) data, first create a bucket in one of the AWS regions. It's a repository where you can store data grouped by folders. You can then upload any number of objects to the bucket. Click [here](http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html) for more information. If the bucket doesn't exist, the application creates it, unless the user has no privileges to do so. |
| [Folder Name property](https://wiki.genexus.com/commwiki/wiki?45734) | A folder inside the Bucket structure. If it doesn't exist, it is created by the application. A folder with the same name as that of the table is created under the Folder specified in this property, along with another folder that has the same name as the multimedia attribute. The multimedia file is stored under the latter folder. |
| [Privacy property (Object Ownership)](https://wiki.genexus.com/commwiki/wiki?59170) /  [Privacy property of Amazon S3 V1 Storage Provider](https://wiki.genexus.com/commwiki/wiki?48407) | Specifies whether stored multimedia resources are Public or Private; that is, if they can be accessed publicly (by everyone) or privately. If Private, a Signed URL will be automatically generated. In **Amazon S3 V1 (Legacy)**, ACLs allow you to control permissions on a per-object basis. In **Amazon S3** with SDK v2, if ACLs are enabled, control is still per object; if ACLs are disabled, permissions are applied at the bucket level, causing all objects to inherit the bucket's privacy settings. This means that methods such as *UploadPrivate* become redundant in public buckets since any upload will be publicly accessible. |
| [URL Expiration property (Storage Provider)](https://wiki.genexus.com/commwiki/wiki?48408) | Expiration value (in minutes) after which a signed (private) URL will become invalid; it defaults to 24 hours. |
| [Storage Region property](https://wiki.genexus.com/commwiki/wiki?57379) | To reduce data latency in your applications, most Amazon Web Services offer a regional endpoint to make your requests. Click [here](http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region) for more information. |
| [Storage Endpoint property](https://wiki.genexus.com/commwiki/wiki?57446) | Enables fast transfers of files over long distances between your client and an S3 bucket. The possible values are Standard, Accelerated, Dual-Stack Accelerated, and Custom Endpoint. For more information, click [here](http://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration.html).  Prerequisites: Transfer Acceleration must be enabled on the bucket. |
| [Storage Custom Endpoint](https://wiki.genexus.com/commwiki/wiki?48409) | Provides a custom entry point for working with services compatible with Amazon S3 SDK. Required only if 'Storage Endpoint' Property = 'Custom Endpoint'. |

(\*) If these properties are left empty, they will be instantiated at runtime from [environment settings in the Amazon EC2 instance](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html). Alternatively, if the environment variable STORAGE\_AWSS3\_USE\_IAM is set to true, IAM will be used for authentication, regardless of whether the Storage Access Key ID and Storage Secret Access Key are configured.

#### [IBM Cloud Object Storage](#IBM+Cloud+Object+Storage)

|  |  |
| --- | --- |
| [Access Key property](https://wiki.genexus.com/commwiki/wiki?45731) | Access Key credentials required to connect to the Storage Provider. |
| [Secret Key property](https://wiki.genexus.com/commwiki/wiki?45732) | Secret Key credentials required to connect to the Storage Provider. |
| [Bucket Name property](https://wiki.genexus.com/commwiki/wiki?45733) | A repository where you can store data grouped by folders. |
| [Folder Name property](https://wiki.genexus.com/commwiki/wiki?45734) | A folder inside the Bucket structure. If it doesn't exist, it is created by the application. |
| [Privacy property](https://wiki.genexus.com/commwiki/wiki?59172) | Specifies whether stored multimedia resources are Public or Private; that is, if they can be accessed publicly (by everyone) or privately. If Private, a Signed URL will be automatically generated. |
| [URL Expiration property (Storage Provider)](https://wiki.genexus.com/commwiki/wiki?48408) | Expiration value (in minutes) after which a signed (private) URL will become invalid; it defaults to 24 hours. |
| [Storage Location property](https://wiki.genexus.com/commwiki/wiki?45735) | Open Stack user's password. |
| [Storage Endpoint property](https://wiki.genexus.com/commwiki/wiki?45736) | URL to access the server. |

Note that this Storage provider is only available in Java. In .NET and .NET Framework, you may use Amazon S3 storage provider to connect to IBM COS.

#### [Microsoft Azure](#Microsoft+Azure)

|  |  |
| --- | --- |
| Public Container Name | A repository where you can store data. |
| Private Container Name | A repository where you can store data. Used for storing [Excel files](https://wiki.genexus.com/commwiki/wiki?2476) and handling private files. See [Storage Provider API](https://wiki.genexus.com/commwiki/wiki?32087). |
| Account Name | An Azure storage account provides a unique namespace to store and access your Azure Storage data. |
| [Privacy property](https://wiki.genexus.com/commwiki/wiki?59172) | Specifies whether stored multimedia resources are Public or Private; that is, if they can be accessed publicly (by everyone) or privately. If Private, a Signed URL will be automatically generated. |
| [URL Expiration property (Storage Provider)](https://wiki.genexus.com/commwiki/wiki?48408) | Expiration value (in minutes) after which a signed (private) URL will become invalid; it defaults to 24 hours. |
| Access Key | Access Key credentials required to connect to the Storage Provider. |

Click [here](https://azure.microsoft.com/en-us/documentation/services/storage/) for more information about Azure Storage.

#### [Google Cloud Storage](#Google+Cloud+Storage)

|  |  |
| --- | --- |
| [Bucket Name property](https://wiki.genexus.com/commwiki/wiki?45733) | A repository where you can store data grouped by folders. |
| [Folder Name property](https://wiki.genexus.com/commwiki/wiki?45734) | A folder inside the Bucket structure. If it doesn't exist, it is created by the application. |
| [Privacy property](https://wiki.genexus.com/commwiki/wiki?59172) | Specifies whether stored multimedia resources are Public or Private; that is, if they can be accessed publicly (by everyone) or privately. If Private, a Signed URL will be automatically generated. |
| [URL Expiration property (Storage Provider)](https://wiki.genexus.com/commwiki/wiki?48408) | Expiration value (in minutes) after which a signed (private) URL will become invalid; it defaults to 24 hours. |
| Service Account Key | The entire contents of the .json file generated as service account key. To get the service account key, open the [Google console](https://console.cloud.google.com), go through API Manager/Credentials, and then Create Credentials/Service account key. The service account key should belong to the Storage Admin role: |
| Project Id | ID of the project. |
| Application Name | Name of the application sent in every request header. |

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build with this Only](https://wiki.genexus.com/commwiki/wiki?5693) of the object.

### [Configuration file](#Configuration+file)

The CloudServices.config file is updated when any property is changed. Unless you change the Storage Provider, there's no need to do any build.
Implementation Details:
When the CloudServices.config file is found in the web application, multimedia files are stored using the settings declared in that file. On the other hand, if the file isn't found, multimedia files are stored in the database.
The file is read-only once the application starts. Therefore, if you change the file settings you need to restart the web application.

### [See Also](#See+Also)

[External Storage for Multimedia](https://wiki.genexus.com/commwiki/wiki?31120) for more detailed information.  
[URL Expiration property (Storage Provider)](https://wiki.genexus.com/commwiki/wiki?48408)  
[Storage Custom Endpoint property (Storage Provider)](https://wiki.genexus.com/commwiki/wiki?48409)  
[Required configuration for Amazon S3 bucket](https://wiki.genexus.com/commwiki/wiki?54610)


|  |
| --- |
| **Backlinks** |
| [Access Key property](https://wiki.genexus.com/commwiki/wiki?45731) | [Application Configuration using Environment Variables in Cloud Services](https://wiki.genexus.com/commwiki/wiki?53339) | [Bucket Name property](https://wiki.genexus.com/commwiki/wiki?45733) |
| [Configuration.ExternalStorage External Object](https://wiki.genexus.com/commwiki/wiki?45913) | [Extension Library concept for Extending GeneXus for Native Mobile](https://wiki.genexus.com/commwiki/wiki?33545) | [External Storage for Multimedia](https://wiki.genexus.com/commwiki/wiki?31120) | [Folder Name property](https://wiki.genexus.com/commwiki/wiki?45734) |
| [GeneXus 18 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?54243) | [GeneXus Cognitive API - Train procedure](https://wiki.genexus.com/commwiki/wiki?44246) |
| [How to deploy a command line procedure to AWS Lambda as a Function](https://wiki.genexus.com/commwiki/wiki?40803) | [HowTo: Deploy an Application to a Kubernetes cluster](https://wiki.genexus.com/commwiki/wiki?45416) | [HowTo: Deploy as Azure Functions](https://wiki.genexus.com/commwiki/wiki?49351) | [HowTo: Deploy mobile services to AWS Serverless using AWS Lambda and AWS API Gateway](https://wiki.genexus.com/commwiki/wiki?35355) |
| [HowTo: Deploy to AWS Lambda Function](https://wiki.genexus.com/commwiki/wiki?51533) | [Load balancing considerations](https://wiki.genexus.com/commwiki/wiki?45291) | [Privacy property](https://wiki.genexus.com/commwiki/wiki?59172) | [Privacy property (Object Ownership)](https://wiki.genexus.com/commwiki/wiki?59170) |
| [Privacy property of Amazon S3 V1 Storage Provider](https://wiki.genexus.com/commwiki/wiki?48407) | [Secret Key property](https://wiki.genexus.com/commwiki/wiki?45732) | [SpeechToText procedure](https://wiki.genexus.com/commwiki/wiki?40169) | [Storage Access Key ID property](https://wiki.genexus.com/commwiki/wiki?56617) |
| [Storage Endpoint property](https://wiki.genexus.com/commwiki/wiki?45736) | [Storage Endpoint property (Amazon S3)](https://wiki.genexus.com/commwiki/wiki?57446) | [Storage Location property](https://wiki.genexus.com/commwiki/wiki?45735) | [Storage Provider API](https://wiki.genexus.com/commwiki/wiki?32087) |
| [Storage Provider property (GeneXus 18 Upgrade 10 or prior)](https://wiki.genexus.com/commwiki/wiki?59174) | [Storage Provider property (GeneXus 18 Upgrade 8 or prior)](https://wiki.genexus.com/commwiki/wiki?57448) | [Storage Secret Access Key property in Generator](https://wiki.genexus.com/commwiki/wiki?56619) |

---
