---
title: "Typical architectures to model GeneXus Mission-Critical systems"
source_id: 55503
source_url: https://wiki.genexus.com/commwiki/wiki?55503
genexus_version: "18"
---

# Typical architectures to model GeneXus Mission-Critical systems

The following image shows some typical architectures to create mission-critical systems with GeneXus.

`[imagen omitida: wiki id 55504]`

Each architecture presents some benefits and challenges.

For example, the further to the right the architectures are shown in the image (and the closer they are to microservices) you will have:

* More flexibility
* More agility to deploy the systems
* Probably, more complexity (because the microservices you create have to communicate with other microservices, and in turn, they have to expose data / read exposed data).

On the other hand, in terms of data consistency, the architectures displayed further to the right, will provide less data consistency. That is, the data will be more consistent in a [monolithic system](https://wiki.genexus.com/commwiki/wiki?55516) and it will be eventually consistent the closer you get to a pure [microservices architecture](https://wiki.genexus.com/commwiki/wiki?55526).


|  |
| --- |
| **Backlinks** |
| [Toc:Modeling Complex Systems with GeneXus](https://wiki.genexus.com/commwiki/wiki?55502) |

---
