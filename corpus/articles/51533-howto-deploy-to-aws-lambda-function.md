---
title: "HowTo: Deploy to AWS Lambda Function"
source_id: 51533
source_url: https://wiki.genexus.com/commwiki/wiki?51533
genexus_version: "18"
---

# HowTo: Deploy to AWS Lambda Function

This document explains how to implement a GeneXus application as an [AWS Lambda Functions](https://wiki.genexus.com/commwiki/wiki?51514).

### [Installation requirements](#Installation+requirements)

Download and run the [AWS CLI MSI installer](https://awscli.amazonaws.com/AWSCLIV2.msi).

### [Setting up the Cloud](#Setting+up+the+Cloud)

**1.** Create an AWS Account

**2.** Create an [IAM User with Access Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console)

### [Modeling in GeneXus](#Modeling+in+GeneXus)

Follow the steps below:

**1.** Create a [Deployment Unit object](https://wiki.genexus.com/commwiki/wiki?38886) and add the Procedure, taking into account the following: Add only one main Procedure to the Deployment Unit object.

* Read [HowTo: Create a GeneXus Procedure to be deployed as an Azure or AWS Function](https://wiki.genexus.com/commwiki/wiki?47729).

**2.** Select [Build > Deploy Application](https://wiki.genexus.com/commwiki/wiki?32092) and a dialog box will open with a Target Combo Box for you to choose the following value: AWS Lambda Functions.

**3.** Configure the properties by clicking on the Options link.

**Note**: In addition to configuring the [AWS Profile name property](https://wiki.genexus.com/commwiki/wiki?43834), you need to consider the following:

* Select one of the [Trigger type property](https://wiki.genexus.com/commwiki/wiki?51466) Lambda Functions.
* Fill the [IAM Execution Role ARN property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?51476,,).

**4.** Click on the Deploy button to implement in AWS.

### [Sample](#Sample)

As shown in the image, you can make the necessary settings for a timer-triggered function.

`[imagen omitida: wiki id 51534]`

In this example, the AWS Profile name property is not set, so the AWS Access Key ID and AWS Secret Access Key properties are set instead.

### [Restrictions](#Restrictions)

* [GeneXus Java Generator](https://wiki.genexus.com/commwiki/wiki?12258) only **(Highest JDK version supported: JDK21)**
  + [Java platform](https://wiki.genexus.com/commwiki/wiki?48353) must be set to**: JavaEE  (JakartaEE not supported right now)**
* Multimedia content considerations
  + If using [Image](https://wiki.genexus.com/commwiki/wiki?15204),  [Audio](https://wiki.genexus.com/commwiki/wiki?16529), [Video](https://wiki.genexus.com/commwiki/wiki?16608), [BlobFile](https://wiki.genexus.com/commwiki/wiki?40420) data types [Storage Provider property](https://wiki.genexus.com/commwiki/wiki?31121) must be used. This is because all App multimedia must be served from an external URL, such as Amazon S3.
  + FileSystem cannot be used to serve content: File/read write access as Blob data type, Excel, PDF Reports.
* Temporal restrictions:
  + [WebSession data type](https://wiki.genexus.com/commwiki/wiki?6321) not supported (coming later)
  + KB Images not supported if returned from Server Side. For example: Procedure that Returns &Image.FromImage(MyKBImage).
* **Warning**
  + DBMS Connection Pooling does not work in Serverless.
    - This is because Serverless executes one Lambda Function per Request. Therefore, every Lambda execution initializes a DB Pool. Thus, if 200 requests are received at the exact same time, 200 lambdas are woken up, and 200 connections to DB will be opened.

### [Architecture considerations](#Architecture+considerations)

If the function app uses [Image](https://wiki.genexus.com/commwiki/wiki?15204), [Audio](https://wiki.genexus.com/commwiki/wiki?16529), [Video](https://wiki.genexus.com/commwiki/wiki?16608), or [BlobFile](https://wiki.genexus.com/commwiki/wiki?40420) data types, you have to configure the [Storage Provider property](https://wiki.genexus.com/commwiki/wiki?31121) because all multimedia must be served from an external URL, such as Microsoft Azure or AWS S3.

For the same reason, using the file system to serve content is not supported; that is, to have read/write access to files (such as Blob data type, Excel, or PDF reports).

### [Under the hood](#Under+the+hood)

AWS Lambda functions are GeneXus applications that follow the structure required by the AWS Lambda Java engine.

An AWS Lambda GeneXus package looks as follows:

`[imagen omitida: wiki id 51535]`

Important notes:

* “Lib” contains the required JAR files for the Application to run.
* “com” contains the Java .class files.
* “gx-awslambda-function.json”
  + Contains the Entry point that will be executed when the lambda is woken up by the runtime. \*\*

\*\*(This should be formatted as a CODE paragraph)

```
{"entryPointClassName": "com.myapp.eventdriven.queue.handlesqsuserqueueevent"}
```

Also, note that depending on the “Trigger Type” Deployment Property, GeneXus will assign the AWS Lambda Handler property accordingly.

`[imagen omitida: wiki id 51536]`

* For a SQS Triggered Function, the Lambda Handler name is: *com.genexus.cloud.serverless.aws.handler.LambdaSQSHandler::handleRequest*
* For a Timer Triggered Function, the Lambda Handler name is: *com.genexus.cloud.serverless.aws.handler.LambdaEventBridgeHandler::handleRequest*
* For an Event Bridge Triggered Function, the Lambda Handler name is: *com.genexus.cloud.serverless.aws.handler.LambdaEventBridgeHandler::handleRequest*
* For an HTTP Triggered Function, the Lambda Handler name is: *com.genexus.cloud.serverless.aws.handler.LambdaHttpApiHandler::handleRequest*

This handler will be set automatically by GeneXus. However, in case of manual deployment, you will need to set the “Handler” accordingly.

### [Scope](#Scope)

**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Availability](#Availability)

Since [GeneXus 17 Upgrade 11](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?49972,,).


|  |
| --- |
| **Backlinks** |
| [Table of contents:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Table of contents:Application Deployment tool (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54334) | [AWS EventBridge triggered functions](https://wiki.genexus.com/commwiki/wiki?51547) |
| [AWS Lambda Functions](https://wiki.genexus.com/commwiki/wiki?51514) | [AWS Queue triggered functions](https://wiki.genexus.com/commwiki/wiki?51541) | [Cloud-native with GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51572) | [HowTo: Create a GeneXus Procedure to be deployed as an Azure or AWS Function](https://wiki.genexus.com/commwiki/wiki?47729) |
| [Lambda HTTP-triggered functions](https://wiki.genexus.com/commwiki/wiki?51552) | [Lambda Timer-triggered functions](https://wiki.genexus.com/commwiki/wiki?51550) |

---
