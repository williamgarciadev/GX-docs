---
title: "Cloud-native with GeneXus 18"
source_id: 51572
source_url: https://wiki.genexus.com/commwiki/wiki?51572
genexus_version: "18"
---

# Cloud-native with GeneXus 18

To get the best experiences you require a system that supports them at every moment, a modern system that adapts to the business needs.

The system may require the support of millions of users or transactions and to scale up or down according to the business seasons. It may be an enormous system with subsystems or just a small app. Not every subsystem may require the same cadence of updates, and some installations may not require the entire system. For a proper operation, you also need to define how you answer to trouble when it arises. And last but not least, you will need to define how you handle the security and privacy of all.

So you need to define aspects of performance, scalability, flexibility, security, privacy, and observability. You need to model your system and its evolution.

With GeneXus 18 you have the flexibility to build modern, highly complex and highly scalable, secure solutions that take full advantage of the cloud.

## [High Scalability in the Cloud](#High+Scalability+in+the+Cloud)

GeneXus 18 increases its support for Serverless Computing so that applications can be flexible and scale indefinitely. You now can develop and deploy functions that work as services (FaaS), non-relational databases (NoSQL), and communicate microservices through Message Queues provided also as services by the cloud providers. Specific emphasis was put on all these leading providers as Amazon Webservices and Microsoft Azure.

### [NoSQL Databases](#NoSQL+Databases)

Even though GeneXus already supported NoSQL databases or services for Caching, Event handling, Object storage, and Full-text search, and these increase the scalability of systems, now GeneXus 18 goes a step further and supports NoSQL databases as [Data Stores](https://wiki.genexus.com/commwiki/wiki?7117). That means that in GeneXus they can be accessed through [For Each](https://wiki.genexus.com/commwiki/wiki?24744) commands, [Data Providers](https://wiki.genexus.com/commwiki/wiki?5270) as they were a Relational DBMS.

The first one to support of this kind is [DynamoDB](https://wiki.genexus.com/commwiki/wiki?50659).

### [Serverless Functions](#Serverless+Functions)

[Procedures](https://wiki.genexus.com/commwiki/wiki?6293), can be deployed as functions. Those functions are triggered by HTTP, REST, and Messages in Queues, among others.

[AWS Lambda Functions](https://wiki.genexus.com/commwiki/wiki?51514), [Lambda HTTP-triggered functions](https://wiki.genexus.com/commwiki/wiki?51552), [Lambda Timer-triggered functions](https://wiki.genexus.com/commwiki/wiki?51550), [AWS EventBridge triggered functions](https://wiki.genexus.com/commwiki/wiki?51547), [AWS Queue triggered functions](https://wiki.genexus.com/commwiki/wiki?51541), [HowTo: Deploy to AWS Lambda Function](https://wiki.genexus.com/commwiki/wiki?51533)

[Azure Functions](https://wiki.genexus.com/commwiki/wiki?47430), [HowTo: Deploy as Azure Functions](https://wiki.genexus.com/commwiki/wiki?49351), [Azure timer triggered functions](https://wiki.genexus.com/commwiki/wiki?49264), [Azure Http-triggered functions](https://wiki.genexus.com/commwiki/wiki?49266), [Service Bus and Queue Storage triggered Azure functions](https://wiki.genexus.com/commwiki/wiki?49355), [HowTo: Monitor Azure Functions](https://wiki.genexus.com/commwiki/wiki?49260)

### [Serverless Service Backend](#Serverless+Service+Backend)

[Data Providers](https://wiki.genexus.com/commwiki/wiki?5270), Rest [APIs](https://wiki.genexus.com/commwiki/wiki?46151), and a whole backend can be deployed on serverless environments.

[Deploy mobile services to AWS Serverless using AWS Lambda and AWS API Gateway](https://wiki.genexus.com/commwiki/wiki?35355)

[Deploy to Azure Serverless using API Management](https://wiki.genexus.com/commwiki/wiki?49107), [HowTo: MSBuild tasks for Azure serverless deployment](https://wiki.genexus.com/commwiki/wiki?51440), [HowTo: Deploy static files to Azure Storage in Serverless deploy](https://wiki.genexus.com/commwiki/wiki?50142)

### [Flexible Configurations](#Flexible+Configurations)

So that you can set configuration in deployment or runtime and that the application can adapt to settings in runtime, a new API has been provided to read any environment variable (EnvVar) in runtime.

### [High Scalability Sample](#High+Scalability+Sample)

So that you can easily try some of these features, we have prepared a sample KB that models a solution with a highly scalable architecture, and also code to create the underlying infrastructure.

`[imagen omitida: wiki id 51399]`

[FestivalTickets - High Scalability Sample](https://wiki.genexus.com/commwiki/wiki?51266)

## [Security](#Security)

As systems get more complex and critical, security and privacy get more important and difficult to implement in every component and the whole lifecycle. Hence, modeling security is key and therefore GAM is now more robust than ever and it completed the support for leading identity providers. Furthermore, the overall security aspects of the generated code have been improved, so applications built with GeneXus 18 will be more secure than ever with less effort.

Integration with Identity Providers is key for delegating proper credentials handling and single-sign-on to them. GeneXus 18 adds the support of OpenID connect, which enables so the support for identity providers like Okta and Oracle, among others. With this, GeneXus 18 completes the support of mainstream protocols: OpenID Connect, OAuth 2.0, and SAML.

Multi-factor authentication (2FA, OTP, TOTP) and Biometric Authentication are authentication methods that are also key when it comes to proper identity handling and even avoiding remembering passwords. GeneXus 18 adds the support of each of them.

[OpenID Connect (OIDC)](https://wiki.genexus.com/commwiki/wiki?49183), [2FA](https://wiki.genexus.com/commwiki/wiki?48254),[OTP](https://wiki.genexus.com/commwiki/wiki?48197), [TOTP](https://wiki.genexus.com/commwiki/wiki?49974), [Biometrics](https://wiki.genexus.com/commwiki/wiki?43466)

## [Latest Technology](#Latest+Technology)

To take the most out of the cloud, and according to our Future Proof promise, GeneXus 18 generates code for the latest technologies not just in the front, but also in the backend.

### [Java](#Java)

To build the generated applications, a new build system has been implemented which is based on Gradle and that integrates with package repositories from Maven. Furthermore, code is generated in a consistent folder structure that corresponds to how the application has been modeled in GeneXus; code is generated in UTF 8 and now supports JDK 17 (LTS) for compilation.

### [.NET](#.NET)

The .NET Generator generates .NET 6 (LTS), and is the evolution of the .NET Framework generator. We encourage you to move your environments to .NET 6 so that you can take advantage of the latest features in GeneXus, the latest advances in the Microsoft platform, and the Cloud.

[.NET Generator Standard Classes](https://wiki.genexus.com/commwiki/wiki?51442)

### [Repository Manager integration](#Repository+Manager+integration)

Standard classes and third-party classes are now taken from Nuget or Maven public repositories, this allows us to evolve the generators much faster, and allow you to update components much faster than ever. You don't need to get an update of GeneXus to get the latest security patches for those packages.

Furthermore, in .NET, [External objects](https://wiki.genexus.com/commwiki/wiki?5669) can refer to packages instead of fixed files.

(\*) future upgrades will include this in the rest of the generators also. Generally speaking, the use of repository managers will be increased in several areas.

[.NET Package ID property](https://wiki.genexus.com/commwiki/wiki?51647), [.NET Package Version property](https://wiki.genexus.com/commwiki/wiki?51648)

### [New RDBMS for China](#New+RDBMS+for+China)

As it is important for enterprises in China to base their mission-critical solutions 100% on Chinese technology, GeneXus 18 adds support for [Dameng](https://wiki.genexus.com/commwiki/wiki?50988), in accordance with its Future Proof promise.

### [OpenAPI](#OpenAPI)

Both, importing or providing REST Services support now the OpenAPI 3 specification.

Furthermore, the OpenAPI specification of REST Services now includes security specifications, so integrating to third parties the APIs provided by your solution is now faster too.

[OpenAPI version property](https://wiki.genexus.com/commwiki/wiki?49531,,)


|  |
| --- |
| **Backlinks** |
| [Automated DevOps with GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51574) | [Toc:GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066) | [Knowledge-driven with GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51573) |

---
