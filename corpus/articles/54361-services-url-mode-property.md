---
title: "Services URL Mode property"
source_id: 54361
source_url: https://wiki.genexus.com/commwiki/wiki?54361
genexus_version: "18"
---

# Services URL Mode property

Specifies how the Services URL should be treated when connecting to the back-end server.

### [Values](#Values)

|  |  |
| --- | --- |
| **Absolute** | Uses the complete URL. |
| **Host Relative** | Uses the URL relative to the current host. |

### [Scope](#Scope)

**Generators:** [Angular](https://wiki.genexus.com/commwiki/wiki?42550)  
**Level:** Generator

### [Description](#Description)

This property specifies if the absolute URL specified in the [Services URL property](https://wiki.genexus.com/commwiki/wiki?21146) is used in the generated programs to connect to the backend services, or if just the path of it.

Using just the host-relative path of the Services URL is good for staging scenarios, where the same container of the Angular frontend is used for pre-production and production environments.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

Let's suppose you have an Angular app and configure the following in your Environment:

```
Services URL = 'https://example.com/mybackend'
Services URL Mode = 'Host Relative'
```

That configuration makes the Angular frontend do requests to '/mybackend' instead of 'https://example.com/mybackend'.

Now you can deploy

* Backend services for pre-production to preprod.example.com/mybackend
* Backend services for production to example.com/mybackend
* Angular frontend to a Docker container.

and run one instance of the docker container with the Angular app on https://preprod.example.com/myapp, and another on https://example.com/myapp. Furthermore, configure a gateway so that requests to '/mybackend' that come from https://preprod.example.com are directed to preprod.example.com/mybackend, and those that come from example.com are directed to example.com/mybackend.

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?53853).


|  |
| --- |
| **Backlinks** |
| [Deploy to Azure Serverless using API Management](https://wiki.genexus.com/commwiki/wiki?49107) |

---
