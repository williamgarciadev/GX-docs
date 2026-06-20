---
title: "Lambda Timer-triggered functions"
source_id: 51550
source_url: https://wiki.genexus.com/commwiki/wiki?51550
genexus_version: "18"
---

# Lambda Timer-triggered functions

Timer-triggered functions are AWS Lambda functions that are invoked automatically in the Cloud according to a certain schedule. The key benefit is that a Server (Windows or Linux) does not need to be launched to run code on a timed basis.

### [Deployment steps](#Deployment+steps)

First, read [HowTo: Create a GeneXus Procedure to be deployed as an Azure or AWS Function](https://wiki.genexus.com/commwiki/wiki?47729).

To deploy the function, use the deployment tool. See [HowTo: Deploy to AWS Lambda Function](https://wiki.genexus.com/commwiki/wiki?51533).

### [Properties Configuration](#Properties+Configuration)

In the Deployment Unit, set the following properties as shown below:

1. AWS Access Key ID/AWS Secret Access Key: Enter your AWS Access Key.
2. AWS Default Region: Select your preferred region (localization) for your Deployment.
3. Function Name: It's the name used to display the application.
4. [Trigger type](https://wiki.genexus.com/commwiki/wiki?51466): Select Timer.
5. [IAM Execution Role ARN property](https://wiki.genexus.com/commwiki/wiki?51476,,): Enter the Amazon Resource Names ([ARNs](http://amazon%20resource%20names%20%28arns%29/)) path.

### [Sample](#Sample)

The configuration settings are as shown in the following image taken from an example:

`[imagen omitida: wiki id 51534]`

**Note**: You must have previously created an IAM Execution Role with the minimum permissions required for the function to execute.

### [AWS Configuration](#AWS+Configuration)

From the AWS Console UI, you must attach the trigger type for the function to be executed automatically on a timed basis.

1. Go to [AWS Lambda Console UI](https://us-east-1.console.aws.amazon.com/lambda/home).
2. Select the AWS Lambda Function.
3. Click on “Add Trigger.”  
   `[imagen omitida: wiki id 51544]`
4. Select the EventBridge option, complete the fields, and click on Add.  (You can also add the trigger through the EventBridge Console UI.)  
   `[imagen omitida: wiki id 51551]`  
   This function will be automatically executed every 10 minutes, honoring the “Schedule expression” value.

### [Availability](#Availability)

Since [GeneXus 17 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?49972,,).


|  |
| --- |
| **Backlinks** |
| [Toc:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Toc:Application Deployment tool (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54334) | [AWS Lambda Functions](https://wiki.genexus.com/commwiki/wiki?51514) |
| [Cloud-native with GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51572) |

---
