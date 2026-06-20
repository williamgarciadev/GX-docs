---
title: "HowTo: Deploy mobile services to AWS Serverless using AWS Lambda and AWS API Gateway"
source_id: 35355
source_url: https://wiki.genexus.com/commwiki/wiki?35355
genexus_version: "18"
---

# HowTo: Deploy mobile services to AWS Serverless using AWS Lambda and AWS API Gateway

This document tells you the prerequisites and steps to deploy applications (REST APIs) to [AWS Lambda](https://aws.amazon.com/lambda/) and [AWS API Gateway](https://aws.amazon.com/api-gateway).

> "AWS Lambda lets you run code without provisioning or managing servers. You pay only for the compute time you consume - there is no charge when your code is not running." ref.: <https://aws.amazon.com/lambda/>

> "Amazon API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale." ref.: <https://aws.amazon.com/api-gateway>

The main benefits of deploying to serverless platforms are the following:

* No worry about infrastructure at all.
* No need to manage, configure or install any web server.
* No need to rent or buy any server.
* 24/7/365 up time for (almost) free. (You pay only if the App is used. )

### [Technology used](#Technology+used)

* AWS Lambda is used in order to Deploy Code that will be run in the Cloud.
* AWS API Gateway for Deploying REST Services.
* AWS Cloudfront for CDN
* AWS S3 for Storage
* AWS IAM for Credentials
* Swagger definition for describing the API generated for our Application.

### [Deployment Support](#Deployment+Support)

* Service Backend for REST based Applications ([Apple](https://wiki.genexus.com/commwiki/wiki?14917),
  [Angular](https://wiki.genexus.com/commwiki/wiki?42550),
  [Android](https://wiki.genexus.com/commwiki/wiki?14453))
* API Objects

### [Restrictions](#Restrictions)

* [GeneXus Java Generator](https://wiki.genexus.com/commwiki/wiki?12258) only (Highest JDK version supported: JDK11)
* Multimedia content considerations
  + If using Image, Audio, Video, BlobFile data types => [Storage Provider property](https://wiki.genexus.com/commwiki/wiki?31121) must be used. This is because all App multimedia must be served from an external URL, such as Amazon S3.
  + Cannot use FileSystem to serve content: File/read write access as Blob data type, Excel, PDF Reports.
* Temporal restrictions:
  + [WebSession data type](https://wiki.genexus.com/commwiki/wiki?6321) not supported (coming later)
  + ~~GAM not supported. (coming later)~~ Supported since [GeneXus 17 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?49971,,).
  + KB Images not supported if returned from Server Side. Ex: Procedure that Returns &Image.FromImage(MyKBImage)
  + [Enable KBN property](https://wiki.genexus.com/commwiki/wiki?46541) not supported
  + [App Update property](https://wiki.genexus.com/commwiki/wiki?46540) not supported
  + [Dynamic Services URL property](https://wiki.genexus.com/commwiki/wiki?20366) and [SetApplicationServerURL](https://wiki.genexus.com/commwiki/wiki?31310) not supported
* Max number of 600 services can be deployed per AWS Region.
* **Beware**
  + DBMS Connection Pooling does not work in Serverless.
    - This is because Serverless executes one Lambda Function per Request. So every Lamdba execution initialize a DB Pool. Thus, if 200 request are received at the exact same time, 200 lambdas are waken up, and 200 connections to DB will be opened.

### [How to use it](#How+to+use+it)

1. Create AWS Serverless Infraestructure. [Link](https://wiki.genexus.com/commwiki/wiki?49718,,)
2. Ensure Property [Generate OpenAPI interface property](https://wiki.genexus.com/commwiki/wiki?31859) is set to "Yes" at Generator Level and [OpenAPI version property](https://wiki.genexus.com/commwiki/wiki?49531,,) = OpenAPI 3.0
3. ReBuild your GeneXus JAVA Application
4. Using [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092), select the Main Objects to Deploy. It must be a Smart Device Main Application or API Object.
5. From the Target Dropdown, select: "AWS Serverless Deploy"
6. Fill required Deployment properties (obtained from Step (1), from the Stack Outputs):
   * AWS Access Key Id
   * AWS Secret Access Key
   * AWS Default Region
   * IAM Role Name
   * Application Name
   * Stage Name
7. Click "Deploy"

That's it!

At the final step, GeneXus will print out the final URL.

You can use it now in the Smart Devices Generator's [Services URL property](https://wiki.genexus.com/commwiki/wiki?21146) or directly for APIObjects.

**Important notes:**

* **Database Access**

The AWS Lambda Function deployed **must** have access to the Database (should be in the same VPC and Security Group). You will have to configure it manually in the AWS Lambda Function Console.

`[imagen omitida: wiki id 40759]`

### [Troubleshooting](#Troubleshooting)

AWS Lambda supports up to JDK11. You need either compile with JDK11 (or lower), or use any JDK but set  "Compiler Options" property to: "-source 1.8 -target 1.8"

> com/kbaux/GXApplication has been compiled by a more recent version of the Java Runtime (class file version 61.0), this version of the Java Runtime only recognizes class file versions up to 55.0","errorType":"java.lang.UnsupportedClassVersionError

### [Availability](#Availability)

Since [GeneXus 17 upgrade 7](https://wiki.genexus.com/commwiki/wiki?49301,,).

### [See Also](#See+Also)

<https://aws.amazon.com/api-gateway/pricing/> (As of September 2018: "The Amazon API Gateway free tier includes one million API calls received per month for up to 12 months.")  
<https://aws.amazon.com/lambda/pricing/> (As of September 2018: "The Lambda free tier includes 1M free requests per month and 400,000 GB-seconds of compute time per month.")  
[Serverless computing - The next evolution of Cloud Computing](https://www5.genexus.com/meeting2017/gx27.session.aspx?en,Serverless-computing-The-next-evolution-of-Cloud-Computing) *by Gonzalo Gallotti (Presented at #GX27, Spanish only, 30 mins)*  
[How to deploy a command line procedure to AWS Lambda as a Function](https://wiki.genexus.com/commwiki/wiki?40803)


|  |
| --- |
| **Backlinks** |
| [Toc:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Toc:Application Deployment tool (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54334) | [Cloud-native with GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51572) |
| [Deploy Application Targets](https://wiki.genexus.com/commwiki/wiki?42079) | [Function Name Prefix property](https://wiki.genexus.com/commwiki/wiki?40679) |
| [How to deploy a command line procedure to AWS Lambda as a Function](https://wiki.genexus.com/commwiki/wiki?40803) | [HowTo: Deploy Frontend applications to Docker containers](https://wiki.genexus.com/commwiki/wiki?51104) | [Lambda HTTP-triggered functions](https://wiki.genexus.com/commwiki/wiki?51552) |

---
