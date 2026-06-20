---
title: "AWS Lambda Functions"
source_id: 51514
source_url: https://wiki.genexus.com/commwiki/wiki?51514
genexus_version: "18"
---

# AWS Lambda Functions

Lambda Functions are based on a serverless execution model that allows running workloads in the cloud in a simple, auto-scalable and low-cost manner. In the Serverless model, unlike traditional models, you are charged only per execution.

Its main benefits are as follows:

* An event-based Lambda function facilitates communication between decoupled services. These functions are automatically executed by the platform upon the occurrence of an event.
* It automatically scales to support the rate of incoming requests without any manual configuration.
* Its payment model is pay-per-use. When you use Lambda functions, you only pay for the requests served and for the computing time required to execute the code. More information at [AWS Lambda Pricing](https://aws.amazon.com/lambda/pricing/?nc1=h_ls).

### [Scenarios](#Scenarios)

The objective is to solve scenarios that involve event-driven data processing, where this processing runs and scales automatically on the cloud-managed infrastructure.

Data processing can react to different types of [triggers](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-concepts.html#gettingstarted-concepts-trigger), such as a timer, queue, service bus, HTTP, etc.

For example, a function can be triggered in the integration of two systems that interact asynchronously by publishing a message in the queue (for example, an e-commerce purchase). The function must process the purchase data for stock or credit checking, in an asynchronous way.

See how to implement them in GeneXus:

* [AWS Queue triggered functions](https://wiki.genexus.com/commwiki/wiki?51541)
* [AWS EventBridge triggered functions](https://wiki.genexus.com/commwiki/wiki?51547)
* [Lambda Timer-triggered functions](https://wiki.genexus.com/commwiki/wiki?51550)
* [Lambda HTTP-triggered functions](https://wiki.genexus.com/commwiki/wiki?51552)

### [How to deploy Lambda Functions](#How+to+deploy+Lambda+Functions)

See [HowTo: Deploy to AWS Lambda Function](https://wiki.genexus.com/commwiki/wiki?51533).

### [Scope](#Scope)

**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Availability](#Availability)

Since [GeneXus 17 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?49972,,).


|  |
| --- |
| **Backlinks** |
| [Toc:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Toc:Application Deployment tool (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54334) | [Cloud-native with GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51572) |
| [How to deploy a command line procedure to AWS Lambda as a Function](https://wiki.genexus.com/commwiki/wiki?40803) | [HowTo: Create a GeneXus Procedure to be deployed as an Azure or AWS Function](https://wiki.genexus.com/commwiki/wiki?47729) | [HowTo: Deploy to AWS Lambda Function](https://wiki.genexus.com/commwiki/wiki?51533) | [Trigger type property](https://wiki.genexus.com/commwiki/wiki?51466) |
| [Trigger type property (GeneXus 18 upgrade 4)](https://wiki.genexus.com/commwiki/wiki?54594) |

---
