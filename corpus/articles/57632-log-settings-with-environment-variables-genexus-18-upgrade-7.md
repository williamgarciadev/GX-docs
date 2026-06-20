---
title: "Log settings with environment variables (GeneXus 18 Upgrade 7)"
source_id: 57632
source_url: https://wiki.genexus.com/commwiki/wiki?57632
genexus_version: "18"
---

# Log settings with environment variables (GeneXus 18 Upgrade 7)

### [What are Logs?](#What+are+Logs%3F)

A Log or log history is a text file (that can be structured or unstructured) in which the events, actions, or changes that have been generated are recorded chronologically.

In general, Logs can be used for several things. For example, to Trace, Debug, or communicate diagnostics of an application.

### [Logs in GeneXus](#Logs+in+GeneXus)

The various GeneXus Logs can be configured at runtime, for example by using the [Log level property](https://wiki.genexus.com/commwiki/wiki?36304) and then doing a build.

To be able to modify some Logging Settings at Runtime, without having to build and deploy the WebApp, you can use the following environment variables:

| Environment variables | Description | Values |
| --- | --- | --- |
| [GX\_LOG\_LEVEL](#GX_LOG_LEVEL) | Configures how many details should be added to the log.  In case of [Log output](https://wiki.genexus.com/commwiki/wiki?39568) = *Azure Application Insights* or[Observability Provider property](https://wiki.genexus.com/commwiki/wiki?53408) = *Azure Monitor Application Insights* (this option uses Azure App Insights as Log provider also)you can also use the following values (which are equivalent to the ones at the right hand side column):  Trace (0), Debug (1), Information (2), Warning (3), Error (4), Critical (5), and None (6). | * debug * all * info * warn * error * fatal |
| [GX\_LOG\_LEVEL\_USER](#GX_LOG_LEVEL_USER) | Configures the detail level of the Log when using the Log API ([Log external object](https://wiki.genexus.com/commwiki/wiki?37872)); this is independent of the detail level configured in the [Log level property](https://wiki.genexus.com/commwiki/wiki?36304).  In case of .NET Generator, it does not apply for [Log output](https://wiki.genexus.com/commwiki/wiki?39568) = *Azure Application Insights*. In this case the Log API takes the same value as the one specified at the GX\_LOG\_LEVEL environment variable. | * debug * all * info * warn * error * fatal |
| [GX\_LOG\_OUTPUT](#GX_LOG_OUTPUT) | Indicates where to send the result of the Log Level property. | * ConsoleAppender    (Writes to SYSOUT) * RollingFile    (Writes to File) |

Consider that when a LogLevel is specified, logging is enabled for messages at the specified level and higher.

**Sample EnvVar configuration**

```
    GX_LOG_OUTPUT: ConsoleAppender
    GX_LOG_LEVEL: INFO
    GX_LOG_LEVEL_USER: INFO
```

### [Scope](#Scope)

**Generators**: [Java](https://wiki.genexus.com/commwiki/wiki?12258), [.NET](https://wiki.genexus.com/commwiki/wiki?38604)

### [See Also](#See+Also)

[Application Configuration using Environment Variables in .NET and Java](https://wiki.genexus.com/commwiki/wiki?53336)  
[Log output property](https://wiki.genexus.com/commwiki/wiki?39568)  
[User Log level property](https://wiki.genexus.com/commwiki/wiki?42434)  
[Log output property](https://wiki.genexus.com/commwiki/wiki?39568)
