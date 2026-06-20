---
title: "RestServiceName variable"
source_id: 60844
source_url: https://wiki.genexus.com/commwiki/wiki?60844
genexus_version: "18"
---

# RestServiceName variable

Identifies the name of the service (API object entry point) currently running. It is useful for tracing, logging, or applying access controls based on the invoked service.

**Data Type:**  
Character(256)

## [Description](#Description)

The &RestServiceName variable holds the name of the service currently running within the API object.

For example, if the object defines an entry point called SNumData, the value of &RestServiceName will be “SNumData”.

You can use this value for traceability, auditing, or security purposes, enabling you to distinguish which service was called during execution.

## [Sample](#Sample)

```
// Service Source
MyApi
{
    RestMethod(POST)
    SNumData(in:&num, out:&Data) => procOutData(&num, &Data);
}

// Events
Event Before
    CheckSecurityAccess(&User, &RestServiceName)  // e.g., "SNumData"
EndEvent

Event After
    &Service = &RestServiceName
    If &Service <> "List"
        LogService(&Service, &CurrentUser)
    EndIf
EndEvent
```

### [Availability](#Availability)

Available since [GeneXus 18 Upgrade 14](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?59631,,) and [GeneXus Next](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?57864,,).


|  |
| --- |
| **Backlinks** |
| [Table of contents:First Steps with API objects](https://wiki.genexus.com/commwiki/wiki?49754) | [Standard Variables for API objects](https://wiki.genexus.com/commwiki/wiki?60834) | [Standard Variables List](https://wiki.genexus.com/commwiki/wiki?7386) |

---
