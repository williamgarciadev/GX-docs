---
title: "HowTo: Identify if an object was called from Workflow"
source_id: 14331
source_url: https://wiki.genexus.com/commwiki/wiki?14331
genexus_version: "18"
---

# HowTo: Identify if an object was called from Workflow

This document explains how to identify whether an object has been called from Workflow or not.

You only need to define a [Boolean](https://wiki.genexus.com/commwiki/wiki?4374) variable named WFCalled, then you can use this example:

```
If &WFCalled

//The object was called from Workflow

Else

......
```

**Note**: The scope for this variable is only for the objects of the first level of calls

### Availability

It's available since [GeneXus X Evolution 1](https://wiki.genexus.com/commwiki/wiki?9256,,) Upgrade 3
