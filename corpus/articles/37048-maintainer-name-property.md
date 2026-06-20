---
title: "Maintainer name property"
source_id: 37048
source_url: https://wiki.genexus.com/commwiki/wiki?37048
genexus_version: "18"
---

# Maintainer name property

Name of the maintainer of the deployed image.

### [Scope](#Scope)

**Level:** Deploy Target Options

### [Description](#Description)

This property sets a maintainer label in the created [Docker image](https://wiki.genexus.com/commwiki/wiki?37050).

It is used to set contact information, usually an email of the author (eg.: me@example.com).

To retrieve the maintainer of an image, you can use

```
Docker inspect <docker image name>
```

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [Availability](#Availability)

This property is available since [GeneXus 15 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?36778,,).

### [See Also](#See+Also)

* [HowTo: Deploy an Application to Docker](https://wiki.genexus.com/commwiki/wiki?36951)
* [Docker Reference](https://docs.docker.com/engine/reference/builder/)


|  |
| --- |
| **Backlinks** |
| [HowTo: Deploy an Application to Docker](https://wiki.genexus.com/commwiki/wiki?36951) | [HowTo: Deploy an Application to Docker (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54337) |

---
