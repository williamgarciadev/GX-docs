---
title: "Log settings with environment variables (GeneXus 18 Upgrade 6 or prior)"
source_id: 56152
source_url: https://wiki.genexus.com/commwiki/wiki?56152
genexus_version: "18"
---

# Log settings with environment variables (GeneXus 18 Upgrade 6 or prior)

### [What are Logs?](#What+are+Logs%3F)

A Log or log history is a text file (that can be structured or unstructured) in which the events, actions, or changes that have been generated are recorded chronologically.

In general, Logs can be used for several things. For example, to Trace, Debug, or communicate diagnostics of an application.

### [Logs in GeneXus](#Logs+in+GeneXus)

The various GeneXus Logs can be configured at runtime, for example by using the [Log level property](https://wiki.genexus.com/commwiki/wiki?36304) and then doing a build.

To be able to modify some Logging Settings at Runtime in containerized environments, without having to build and deploy the WebApp, you can use the following environment variables:

| Environment variables | Description | Values | Availability |
| --- | --- | --- | --- |
| GX\_LOG\_LEVEL | Configures how many details should be added to the log. | * debug * all * info * warn * error | * Java Generator (v18 U1) * .NET Generator (v18 U2) |
| GX\_LOG\_LEVEL\_USER | Configures the detail level of the Log when using the Log API ([Log external object](https://wiki.genexus.com/commwiki/wiki?37872)); this is independent of the detail level configured in the [Log level property](https://wiki.genexus.com/commwiki/wiki?36304). | * debug * all * info * warn * error | * Java Generator (v18 U1) * .NET Generator (v18 U2) |
| GX\_LOG\_OUTPUT | Indicates where to send the result of the Log Level property. | * ConsoleAppender    (Writes to SYSOUT) * RollingFile    (Writes to File) | * Java Generator (v18 U1) * .NET Generator (v18 U2) |

### [Scope](#Scope)

**Generators**: [Java](https://wiki.genexus.com/commwiki/wiki?12258), [.NET](https://wiki.genexus.com/commwiki/wiki?38604)

### [See Also](#See+Also)

[Application Configuration using Environment Variables in .NET and Java](https://wiki.genexus.com/commwiki/wiki?53336)  
[Log output property](https://wiki.genexus.com/commwiki/wiki?39568)  
[User Log level property](https://wiki.genexus.com/commwiki/wiki?42434)  
[Log output property](https://wiki.genexus.com/commwiki/wiki?39568)
