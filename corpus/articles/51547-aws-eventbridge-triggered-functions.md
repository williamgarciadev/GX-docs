---
title: "AWS EventBridge triggered functions"
source_id: 51547
source_url: https://wiki.genexus.com/commwiki/wiki?51547
genexus_version: "18"
---

# AWS EventBridge triggered functions

Amazon EventBridge is a serverless event bus service that delivers a stream of real-time data from your applications to AWS Lambda functions.

When you configure the [Trigger type property](https://wiki.genexus.com/commwiki/wiki?51466) of a [Deployment Unit object](https://wiki.genexus.com/commwiki/wiki?38886) to "Event Bridge," triggers will respond to messages from the event bus service.

### [Deployment steps](#Deployment+steps)

First, read [HowTo: Create a GeneXus Procedure to be deployed as an Azure or AWS Function](https://wiki.genexus.com/commwiki/wiki?47729).

To deploy the function, use the deployment tool. See [HowTo: Deploy to AWS Lambda Function](https://wiki.genexus.com/commwiki/wiki?51533).

### [Properties Configuration](#Properties+Configuration)

In the Deployment Unit, set the following properties as shown below:

1. AWS Access Key ID/AWS Secret Access Key: Enter your AWS Access Key.
2. AWS Default Region: Select your preferred region (localization) for your Deployment.
3. Function Name: It's the name used to display the application.
4. [Trigger type](https://wiki.genexus.com/commwiki/wiki?51466): Select EventBridge.
5. [IAM Execution Role ARN property](https://wiki.genexus.com/commwiki/wiki?51476,,): Enter the Amazon Resource Names ([ARNs](http://amazon%20resource%20names%20%28arns%29/)) path.

### [Sample](#Sample)

The configuration settings are as shown in the following image taken from an example:

`[imagen omitida: wiki id 51548]`

**Note**: You must have previously created an IAM Execution Role with the minimum permissions required for the function to execute.

### [AWS Configuration](#AWS+Configuration)

From the AWS Console UI, attach the queue trigger type for the function to be executed automatically when a new EventBridge event is created.

1. Go to [AWS Lambda Console UI](https://us-east-1.console.aws.amazon.com/lambda/home).
2. Select the AWS Lambda Function.
3. Click on “Add Trigger”.  
   `[imagen omitida: wiki id 51544]`
4. Select the EventBridge option, complete the fields, and click on Add. (You can also add the trigger through the EventBridge Console UI.)  
   `[imagen omitida: wiki id 51549]`

### [Availability](#Availability)

Since [GeneXus 17 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?49972,,).


|  |
| --- |
| **Backlinks** |
| [Toc:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Toc:Application Deployment tool (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54334) | [AWS Lambda Functions](https://wiki.genexus.com/commwiki/wiki?51514) |
| [Cloud-native with GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51572) |

---
