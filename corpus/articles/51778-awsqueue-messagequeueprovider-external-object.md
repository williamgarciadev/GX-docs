---
title: "AWSQueue.MessageQueueProvider external object"
source_id: 51778
source_url: https://wiki.genexus.com/commwiki/wiki?51778
genexus_version: "18"
---

# AWSQueue.MessageQueueProvider external object

The *MessageQueueProvider* is an external object of the[Queue API](https://wiki.genexus.com/commwiki/wiki?51771) located under the AWSQueue module. It allows you to establish a connection to an [Amazon Simple Queue Service](https://aws.amazon.com/sqs/), by passing its credentials.

To send or receive messages from AWS SQS, first you have to establish a connection using the method of this external object. It returns a [MessageQueue](https://wiki.genexus.com/commwiki/wiki?51736) that must be used to process the queue (produce and consume messages).  
  
This guarantees that only the AWS SQS dependencies are downloaded to your machine and taken to the deployment.

`[imagen omitida: wiki id 51780]`

## [Properties](#Properties)

It doesn't have any.

## [Methods](#Methods)

### [Connect](#Connect)

Static method that allows instantiating a Queue from dynamic data.

**Return value**   [MessageQueue](https://wiki.genexus.com/commwiki/wiki?51736)  
**Parameters**     AWSBasicCredentials:AWSBasicCredentials, queueURL:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), ErrorMessages:[GeneXus.Common.Messages](https://wiki.genexus.com/commwiki/wiki?40335), Success:[Boolean](https://wiki.genexus.com/commwiki/wiki?4374).

**Note**: AWSBasicCredentials is an SDT (AccessKey, SecretKey, Region) defined in the AWSCore module.  
If you leave the AccessKey and SecretKey empty (that is, use the connect method that does not receive the AWSBasicCredentials), you are expected to be using an [IAM Role](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html).

**Return value**   [MessageQueue](https://wiki.genexus.com/commwiki/wiki?51736)  
**Parameters**     queueURL:VarChar, ErrorMessages:[GeneXus.Common.Messages](https://wiki.genexus.com/commwiki/wiki?40335), Success:Boolean.

To connect to the queue without hard-coding the credentials and use Environment variables, click [here](https://wiki.genexus.com/commwiki/wiki?51928).

## [Events](#Events)

It doesn't have any.

## [See Also](#See+Also)

[HowTo: Connect to a Queue](https://wiki.genexus.com/commwiki/wiki?51761)

### [Availability](#Availability)

This feature is available since [GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066).


|  |
| --- |
| **Backlinks** |
| [Table of contents:Asynchronous messaging APIs](https://wiki.genexus.com/commwiki/wiki?51735) | [HowTo: Connect to a Queue](https://wiki.genexus.com/commwiki/wiki?51761) | [HowTo: Send and receive messages from SQS](https://wiki.genexus.com/commwiki/wiki?51926) |
| [Queue API domains](https://wiki.genexus.com/commwiki/wiki?51928) |

---
