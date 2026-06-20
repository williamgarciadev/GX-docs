---
title: "RestCode variable"
source_id: 60841
source_url: https://wiki.genexus.com/commwiki/wiki?60841
genexus_version: "18"
---

# RestCode variable

Defines the HTTP status code that the API object returns to the client, allowing you to explicitly control the response based on the outcome of the operation.

**Data Type:**  
Numeric(3)

## [Description](#Description)

The &RestCode variable allows you to manually define the HTTP status code that will be included in the service response.

If no value is set, GeneXus automatically returns a default status code:

* 200 (OK) for successful responses.
* Other error codes vary depending on the type of failure detected.

You can use &RestCode to indicate specific outcomes, such as 201 Created when a resource is successfully created, or 400 Bad Request when a validation error occurs.

The &RestCode variable only accepts values of categories 2xx and 4xx. For more information, see [SAC #50865](https://www.genexus.com/developers/websac?en,,,50865)

## [Sample](#Sample)

```
Event ClientInsert.After
   If &Success
      &RestCode = 201  // Created
   Else
      &RestCode = 400  // Bad Request
   EndIf
EndEvent
```

### [Availability](#Availability)

Available since [GeneXus 17](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46066,,).


|  |
| --- |
| **Backlinks** |
| [Table of contents:First Steps with API objects](https://wiki.genexus.com/commwiki/wiki?49754) | [Standard Variables for API objects](https://wiki.genexus.com/commwiki/wiki?60834) | [Standard Variables List](https://wiki.genexus.com/commwiki/wiki?7386) |

---
