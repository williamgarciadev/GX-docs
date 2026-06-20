---
title: "How to deploy a command line procedure to AWS Lambda as a Function"
source_id: 40803
source_url: https://wiki.genexus.com/commwiki/wiki?40803
genexus_version: "18"
---

# How to deploy a command line procedure to AWS Lambda as a Function

**Deprecated**: Since  [GeneXus 17 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?49972,,) . Replaced by [AWS Lambda Functions](https://wiki.genexus.com/commwiki/wiki?51514).

This document tells you the prerequisites and steps to deploy a command line procedure to [AWS Lambda](https://aws.amazon.com/lambda/) and [AWS API Gateway](https://aws.amazon.com/api-gateway).

> "AWS Lambda lets you run code without provisioning or managing servers. You pay only for the compute time you consume - there is no charge when your code is not running." ref.: <https://aws.amazon.com/lambda/>

The main benefits of deploying to serverless platforms are the following:

* No worry about infrastructure at all.
* No need to manage, configure or install any server.
* No need to rent or buy any server.
* 24/7/365 up time for (almost) free. (You pay only if the App is used.)

## [**Technology used**](#Technology+used)

* AWS Lambda is used in order to Deploy Code that will be run in the Cloud.

## [**Restrictions**](#Restrictions)

* Deployment of command line [procedures](https://wiki.genexus.com/commwiki/wiki?6293)
* Java Generator only
* Requires AWS Account and [AWS API Key](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey)
* If using Image, Audio, Video, BlobFile data types => [Storage Provider property](https://wiki.genexus.com/commwiki/wiki?31121) must be used. This is because all App multimedia must be served from an external URL, such as Amazon S3.
* Not supported
  + File/read write access as Blob data type, Excel, PDF Reports.
* Each time the function is triggered, its execution must not last more than 5 minutes. Check for this limit and others [here](https://docs.aws.amazon.com/lambda/latest/dg/limits.html).

## [**How to use it**](#How+to+use+it)

1. Build the main command line procedure with Java Generator.
2. Select the procedure to deploy using [Deploy Applications tool](https://wiki.genexus.com/commwiki/wiki?32092).
3. From the Target Dropdown, select: "AWS Lambda Function deploy (Main Procedure Only)"
4. Set [AWS Access Key Id, AWS Secret Access Key](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey)**\*\*\***and AWS Default Region.
5. Set Application Name and Stage Name (ex: v1, v2, v3).
6. Click "Deploy".

That's it!

At the final step, GeneXus will print out the final URL.

You can use it now in the Smart Devices Generator's [Services URL property](https://wiki.genexus.com/commwiki/wiki?21146).

**Some important notes:**

\*\*\***AWS Access Key requires Custom Policy:**[IAM Serverless Policy for Serverless Deploy](https://wiki.genexus.com/commwiki/wiki?40685,,) **OR just aws:policy/AdministratorAccess**

The AWS Lambda Function deployed **must** have access to the Database (should be in the same VPC and Security Group). You will have to configure it manually in the AWS Lambda Function Console.

`[imagen omitida: wiki id 40759]`

## [See Also](#See+Also)

* <https://aws.amazon.com/lambda/pricing/> (As of September 2018: "The Lambda free tier includes 1M free requests per month and 400,000 GB-seconds of compute time per month.")
* [Serverless computing - The next evolution of Cloud Computing](https://www5.genexus.com/meeting2017/gx27.session.aspx?en,Serverless-computing-The-next-evolution-of-Cloud-Computing) *by Gonzalo Gallotti (Presented at #GX27, Spanish only, 30 mins)*
* [HowTo: Deploy mobile services to AWS Serverless using AWS Lambda and AWS API Gateway](https://wiki.genexus.com/commwiki/wiki?35355)


|  |
| --- |
| **Backlinks** |
| [Function Name Prefix property](https://wiki.genexus.com/commwiki/wiki?40679) | [HowTo: Deploy mobile services to AWS Serverless using AWS Lambda and AWS API Gateway](https://wiki.genexus.com/commwiki/wiki?35355) |

---
