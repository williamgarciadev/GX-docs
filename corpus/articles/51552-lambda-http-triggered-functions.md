---
title: "Lambda HTTP-triggered functions"
source_id: 51552
source_url: https://wiki.genexus.com/commwiki/wiki?51552
genexus_version: "18"
---

# Lambda HTTP-triggered functions

Lambda HTTP-triggered functions are Lambda functions that can be invoked through an HTTP(s) endpoint remotely instead of a typical trigger type such as queue, EventBridge.

Below are GeneXus objects that can be deployed as HTTP Functions:

1. HTTP services
   1. Procedures, Business Components, Data Providers exposed as Rest services.
   2. API objects.
2. Mobile back-end services (Angular, iOS, Android)
   1. An entire back-end service can be deployed as a Lambda HTTP-triggered function. However, the recommeded way for deploying is [HowTo: Deploy mobile services to AWS Serverless using AWS Lambda and AWS API Gateway](https://wiki.genexus.com/commwiki/wiki?35355)[HTTP APIs using Lambda & API Gateway](https://wiki.genexus.com/commwiki/wiki?35355).

### [Deployment steps](#Deployment+steps)

First, read [HowTo: Create a GeneXus Procedure to be deployed as an Azure or AWS Function](https://wiki.genexus.com/commwiki/wiki?47729).

To deploy the function, use the deployment tool. See [HowTo: Deploy to AWS Lambda Function](https://wiki.genexus.com/commwiki/wiki?51533).

### [Properties Configuration](#Properties+Configuration)

In the [Deployment Unit](https://wiki.genexus.com/commwiki/wiki?38886), set the following properties as shown below:

1. AWS Access Key ID/AWS Secret Access Key: Enter your AWS Access Key.
2. AWS Default Region: Select your preferred region (localization) for your Deployment.
3. Function Name: It's the name used to display the application.
4. [Trigger type](https://wiki.genexus.com/commwiki/wiki?51466): Select Http.
5. [IAM Execution Role ARN property](https://wiki.genexus.com/commwiki/wiki?51476,,): Enter the Amazon Resource Names ([ARNs](http://amazon%20resource%20names%20%28arns%29/)) path.

### [Sample](#Sample)

The configuration settings are as shown in the following image taken from an example:

`[imagen omitida: wiki id 51554]`

**Note**: You must have previously created an IAM Execution Role with the minimum permissions required for the function to execute.

### [AWS Configuration](#AWS+Configuration)

From the AWS Console UI, you must attach the trigger type for the function to be executed automatically on a timed basis.

1. Go to [AWS Lambda Console UI](https://us-east-1.console.aws.amazon.com/lambda/home).
2. Select the AWS Lambda Function
3. Go to Tab “Configuration” and select “Function URL.”
4. Click on “Create function URL”.  
   `[imagen omitida: wiki id 51555]`
5. Click on Save

After this step is completed, AWS will show the endpoint URL. Typically, the endpoint has the following pattern:

https://cvbcvbcvbcvbcxvb.lambda-url.us-east-1.on.aws/


|  |
| --- |
| **Backlinks** |
| [Toc:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Toc:Application Deployment tool (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54334) | [AWS Lambda Functions](https://wiki.genexus.com/commwiki/wiki?51514) |
| [Cloud-native with GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51572) |

---
