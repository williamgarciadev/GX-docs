---
title: "Standard Variables for API objects"
source_id: 60834
source_url: https://wiki.genexus.com/commwiki/wiki?60834
genexus_version: "18"
---

# Standard Variables for API objects

[Standard Variables](https://wiki.genexus.com/commwiki/wiki?7386) provide access to predefined values that GeneXus reserves for use in different [objects](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1866,,). If you try to create a variable using one of these names, GeneXus automatically applies the standard definition and does not allow you to modify its type or redefine it.

In [API objects](https://wiki.genexus.com/commwiki/wiki?46151), standard variables are used within the Events section.

**Available standard variables in API object events:**

* &[RestCode](https://wiki.genexus.com/commwiki/wiki?60841): Sets the HTTP status code returned by the endpoint. If not configured, GeneXus assigns a default code, such as 200 (OK), to indicate success.
* &[RestServiceName](https://wiki.genexus.com/commwiki/wiki?60844): Identifies the name of the service (API object entry point) currently running. It is useful for tracing, logging, or applying access controls based on the invoked service.


|  |
| --- |
| **Backlinks** |
| [Table of contents:First Steps with API objects](https://wiki.genexus.com/commwiki/wiki?49754) | [Standard Variables for API Objects (GeneXus 18 Upgrade 13 or prior)](https://wiki.genexus.com/commwiki/wiki?60839) |

---
