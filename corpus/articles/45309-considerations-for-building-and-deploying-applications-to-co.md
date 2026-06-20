---
title: "Considerations for building and deploying applications to containers"
source_id: 45309
source_url: https://wiki.genexus.com/commwiki/wiki?45309
genexus_version: "18"
---

# Considerations for building and deploying applications to containers

This article groups some special considerations and references for building, deploying, and running applications in containerized environments.

The most popular containerization ecosystems are Docker and Kubernetes (Docker as a containerization layer and K8N as an orchestration layer). Most cloud providers provide platforms with containerization or orchestration layers based on those technologies or others (eg.: [AWS ECS](https://aws.amazon.com/ecs/), [AWS Fargate](https://aws.amazon.com/fargate/))

### [Development](#Development)

While creating your application with GeneXus, several aspects have to be taken into account. When the applications run in a containerized ecosystem, they scale horizontally and run behind a load balancer, so take into account these [Load balancing considerations](https://wiki.genexus.com/commwiki/wiki?45291).

### [Deployment](#Deployment)

To deploy applications, GeneXus provides a tool window and also MSBuild tasks to [deploy the application to Docker containers](https://wiki.genexus.com/commwiki/wiki?36951).

### [Stateless vs Stateful](#Stateless+vs+Stateful)

Most containerized environments are by default stateless, but they also have configuration options for [Session state handling](https://wiki.genexus.com/commwiki/wiki?45308).  
Note that Stateful does not mean a loss in performance: Read [Stateless vs Statefull](https://wiki.genexus.com/commwiki/wiki?45284) for more information.

### [See Also](#See+Also)

* [HowTo: Deploy an Application to a Kubernetes cluster](https://wiki.genexus.com/commwiki/wiki?45416)
* [Application Configuration using Environment Variables](https://wiki.genexus.com/commwiki/wiki?39459)


|  |
| --- |
| **Backlinks** |
| [Toc:Scalability and Performance of GeneXus Applications](https://wiki.genexus.com/commwiki/wiki?45280) |

---
