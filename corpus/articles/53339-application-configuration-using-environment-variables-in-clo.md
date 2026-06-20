---
title: "Application Configuration using Environment Variables in Cloud Services"
source_id: 53339
source_url: https://wiki.genexus.com/commwiki/wiki?53339
genexus_version: "18"
---

# Application Configuration using Environment Variables in Cloud Services

In various scenarios, it is common practice to read configuration information from environment variables, rather than configuration files. This document details how to do this practice in Cloud Services properties.

For instance, if you configured your application to use Microsoft Azure as your [Storage Provider](https://wiki.genexus.com/commwiki/wiki?31121), you will have to set some properties like the account details and container names. These properties can also be modified at runtime via environment variables. These variables must be also prefixed with 'GX\_' and must contain the type of the service and the name of the property, all in capital letters. So, if you want to modify the Public Container Name, you can create a variable called GX\_STORAGE\_PUBLIC\_CONTAINER\_NAME with the value of your choice. For further reference of the Types and property names, you can open the generated CloudServices.config file.

#### [.NET Example for AWS S3 Storage Provider](#.NET+Example+for+AWS+S3+Storage+Provider)

```
GX_STORAGE_BUCKET_NAME=myBucketName
GX_STORAGE_STORAGE_PROVIDER_REGION=us-east-1
GX_STORAGE_STORAGE_PROVIDER_ACCESSKEYID=AKIAWXXXX
GX_STORAGE_STORAGE_PROVIDER_SECRETACCESSKEY=XXXXXXX
```

### [Property redirection](#Property+redirection)

There are cloud providers that already provide environment variables with the values to connect to the different services.  
If the provider does not provide environment variables for the purpose, you can define your own.

In any case, to use those variables, a specific file allows you to declare the mapping between the environment variables defined at the cloud provider and the configuration property. This file is called *confmapping.json* and contains a json octopus (property value) with the necessary mapping.

#### [Java Example](#Java+Example)

Amazon provides the environment variables RDS\_USERNAME and RDS\_PASSWORD (among others) where the corresponding values of the RDS are already loaded. For that case, you can have the file *confmapping.json* in the WEB-INF directory of your web app with the following json:

```
{"com.environmenttest|DEFAULT:USER_ID":"RDS_USERNAME","com.environmenttest|DEFAULT:USER_PASSWORD":"RDS_PASSWORD"}
```

When the web app wants to raise the USER\_ID property of the com.environmenttest |DEFAULT section, it will read the value of the RDS\_USERNAME environment property (and the same with the USER\_PASSWORD / RDS\_PASSWORD).

#### [.NET or .NET Framework Examples](#.NET+or+.NET+Framework+Examples)

In the case of [.NET](https://wiki.genexus.com/commwiki/wiki?38604), and [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), the *confmapping.json* should be like the following(where XXX and YYY are variables defined in the Cloud provider).

```
{"Connection-Default-DB":"XXX","Connection-Default-User":"YYY"}
```

**Note**: To test what value is being taken into account or what environment variables are set, you may use [ConfigurationManager external object](https://wiki.genexus.com/commwiki/wiki?40085).

### [See Also](#See+Also)

[Application Configuration using Environment Variables](https://wiki.genexus.com/commwiki/wiki?39459)  
[Application Configuration using Environment Variables in .NET and Java](https://wiki.genexus.com/commwiki/wiki?53336)  
[HowTo: Deploy an Application to Docker](https://wiki.genexus.com/commwiki/wiki?36951)


|  |
| --- |
| **Backlinks** |
| [Application Configuration using Environment Variables](https://wiki.genexus.com/commwiki/wiki?39459) | [Application Configuration using Environment Variables in .NET and Java](https://wiki.genexus.com/commwiki/wiki?53336) | [Table of contents:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) |
| [Table of contents:Application Deployment tool (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54334) |

---
