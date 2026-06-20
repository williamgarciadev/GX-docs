---
title: "Continuous Delivery"
source_id: 44672
source_url: https://wiki.genexus.com/commwiki/wiki?44672
genexus_version: "18"
---

# Continuous Delivery

Continuous Delivery is achieved when [Continuous Integration](https://wiki.genexus.com/commwiki/wiki?38331) also includes the automation of the package assembling so that it can then be published to production with one click.

To achieve this GeneXus offers the [Deployment Unit object](https://wiki.genexus.com/commwiki/wiki?38886) that allows you to separate the deploy from each part of the application to take to production, and thus be able to deploy certain parts without having to carry everything together.

For example, you could have the backend in a [Deployment Unit object](https://wiki.genexus.com/commwiki/wiki?38886) and the rest services in another [Deployment Unit object](https://wiki.genexus.com/commwiki/wiki?38886). So, if you need to make a change in the backend, but you don't have the services ready to release yet, then you can deploy only the backend.

Also, the Deployment Units allow to save all the necessary objects so that this backend works correctly and the next time the backend is deployed, everything related will be taken into account again.

Therefore, using the Deployment Units in conjunction with [GeneXus Server](https://wiki.genexus.com/commwiki/wiki?31337,,) and the Jenkins plugin it is possible to [automate the deploy of the deploy](https://wiki.genexus.com/commwiki/wiki?44704,,).


|  |
| --- |
| **Backlinks** |
| [Continuous Deployment](https://wiki.genexus.com/commwiki/wiki?44673) | [Toc:DevOps in GeneXus](https://wiki.genexus.com/commwiki/wiki?38363) |

---
