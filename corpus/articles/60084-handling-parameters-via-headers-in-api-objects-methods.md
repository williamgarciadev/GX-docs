---
title: "Handling parameters via headers in API Objects methods"
source_id: 60084
source_url: https://wiki.genexus.com/commwiki/wiki?60084
genexus_version: "18"
---

# Handling parameters via headers in API Objects methods

When defining methods inside an [API object](https://wiki.genexus.com/commwiki/wiki?46151), you may need to use parameters as shown in the examples:

1. [ListCustomers](https://wiki.genexus.com/commwiki/wiki?50051)
2. [GetByKey](https://wiki.genexus.com/commwiki/wiki?50052)
3. [Insert](https://wiki.genexus.com/commwiki/wiki?49778)
4. [Update](https://wiki.genexus.com/commwiki/wiki?49780)
5. [Delete](https://wiki.genexus.com/commwiki/wiki?49781)

In certain scenarios, it might be more convenient to send these parameters through the HTTP request headers. This is useful for passing specific contextual information, such as user preferences, language settings, or various flags to enable or disable certain features.  
  
Defined services within the API Object can explicitly declare which parameters should be obtained from the HTTP request headers by using the **[Header]**tag.

```
[ Header("Accept-Language", &Language) ]
[ Header("X-Debug-Mode", &DebugMode) ]
[ Header("X-Verbose", &VerboseFlag) ]
[ Header("GX-User", &UserId) ]

GetInfo(in:&Language, in:&DebugMode, in:&VerboseFlag, in:&UserId, in:&RepositoryId, out:&Data)
=> GetData(&Language, &DebugMode, &VerboseFlag, &UserId, &RepositoryId, &Data);
```

During service execution, GeneXus will automatically extract the value for each variable (&Language, &DebugMode, &VerboseFlag, and &UserId) from the corresponding header in the HTTP request, while the variable RepositoryId will be obtained in the usual way.

### [Compatibility with other Knowledge Bases](#Compatibility+with+other+Knowledge+Bases)

When calling a service using HTTP requests, the corresponding headers must be added.

```
&HTTPClient.AddHeader(GX-User, &UserId)
```

On the other hand, when the module containing the API Object is imported from another Knowledge Base, no syntax changes are required, ensuring compatibility and ease of integration.

```
Module.APIObject.Method(parm1, parm2, etc…)
```

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Availability](#Availability)

This feature is available since [GeneXus 18 Upgrade 13](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?59630,,).


|  |
| --- |
| **Backlinks** |
| [API object - Delete service definition and declaration](https://wiki.genexus.com/commwiki/wiki?49781) | [API object - GetByKey service definition and declaration](https://wiki.genexus.com/commwiki/wiki?50052) | [API object - Insert service definition and declaration](https://wiki.genexus.com/commwiki/wiki?49778) |
| [API object - ListCustomers service definition and declaration](https://wiki.genexus.com/commwiki/wiki?50051) | [API object - Update service definition and declaration](https://wiki.genexus.com/commwiki/wiki?49780) | [Table of contents:First Steps with API objects](https://wiki.genexus.com/commwiki/wiki?49754) |

---
