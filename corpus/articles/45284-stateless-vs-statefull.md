---
title: "Stateless vs Statefull"
source_id: 45284
source_url: https://wiki.genexus.com/commwiki/wiki?45284
genexus_version: "18"
---

# Stateless vs Statefull

A stateless app is an application that does not save client data generated in one session for use in the next session with that client. Each session is carried out as if it was the first time and responses are not dependent upon data from a previous session.

A stateful app is an application that *does* save client data generated in one session for use in the next session with that client.

There is an industry-wide discussion about what is better for performance and [horizontal] scalability: A stateless or a stateful application.

### [FAQ](#FAQ)

***Q**: Can GeneXus Applications be stateless?  
**A***: A Web page that shows data typically Yes. A rest Application typically Yes. Complex business applications are typically not stateless (they typically store some session info between requests). This document goes into the details: [Load balancing considerations](https://wiki.genexus.com/commwiki/wiki?45291)  
  
***Q**: If Not,  does this mean that they require Server Affinity?*   
**A**: No. (Session, Cache or any data may be replicated or moved to an external point)

***Q**: If an application is not stateless, does this mean that it will have scalability or performance issues?*   
**A**: No.  
Refs:

* "…industry should move to architectures based on stateful application servers…"   
  <https://storage.googleapis.com/pub-tools-public-publication-data/pdf/03de87e2856b06a94ffae7dca218db2d4b9afd39.pdf>
* <https://www.infoworld.com/article/3106416/containerizing-stateful-applications.html>

***Q**: Can GeneXus guarantee that the applications are scalable?*   
**A**: No, it depends on how they are architectured, developed, and deployed.

More information at [Load balancing considerations](https://wiki.genexus.com/commwiki/wiki?45291) and [Session state handling](https://wiki.genexus.com/commwiki/wiki?45308).


|  |
| --- |
| **Backlinks** |
| [Considerations for building and deploying applications to containers](https://wiki.genexus.com/commwiki/wiki?45309) | [Toc:Scalability and Performance of GeneXus Applications](https://wiki.genexus.com/commwiki/wiki?45280) |

---
