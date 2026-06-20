---
title: "Scalability and Performance of GeneXus Applications"
source_id: 45280
source_url: https://wiki.genexus.com/commwiki/wiki?45280
genexus_version: "18"
---

# Scalability and Performance of GeneXus Applications

Performance refers to a system's speed and responsiveness in completing tasks within a given timeframe, while scalability refers to its ability to handle increasing workloads without sacrificing performance.

Two commonly used approaches to address workload variations are horizontal and vertical scaling. Horizontal scaling involves adding more machines to the resource pool, while vertical scaling increases the power of existing machines by increasing CPU and RAM capacity.

Horizontal scaling not only adapts to workload fluctuations but also helps to achieve high application availability. This is done by expanding the resource pool, which ensures that the system can cope with increased demand while maintaining optimal performance.

Another technique, autoscaling (also known as auto scaling), is used in cloud computing to automatically adjust computational resources based on the current workload. It dynamically scales resources within a server farm, scaling them up or down as needed to meet demand.

GeneXus applications use these scaling approaches, often using load balancers to evenly distribute requests among machines in a cluster or farm when horizontally scaling applications or web services.

GeneXus provides support for these architectures and advanced scaling methods, allowing the combination of different solutions tailored to specific application requirements. Special considerations throughout the application lifecycle are crucial to ensure optimal performance and scalability.

This table of contents describes everything related to the performance and scalability of applications, and what considerations you need to take into account when developing, deploying, monitoring, or troubleshooting them.


* Load Balancing
  + [Why Load Balancing](https://wiki.genexus.com/commwiki/wiki?45281)
  + [Considerations for Devs and Ops](https://wiki.genexus.com/commwiki/wiki?45291)
  + [Session state handling](https://wiki.genexus.com/commwiki/wiki?45308)
    - [Server Affinity (Sticky Sessions)](https://wiki.genexus.com/commwiki/wiki?45282,,)
    - [Session Replication](https://wiki.genexus.com/commwiki/wiki?45283,,)
* [Stateless vs Statefull](https://wiki.genexus.com/commwiki/wiki?45284)
* [Containerization](https://wiki.genexus.com/commwiki/wiki?45309)
* [Management and Monitoring](https://wiki.genexus.com/commwiki/wiki?27294,,)

---
