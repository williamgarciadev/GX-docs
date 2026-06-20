---
title: "HowTo: Generate GAM trace"
source_id: 50469
source_url: https://wiki.genexus.com/commwiki/wiki?50469
genexus_version: "18"
---

# HowTo: Generate GAM trace

Applications that use [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) can generate trace information to help when troubleshooting.

The administrator user of the [GAM Applications](https://wiki.genexus.com/commwiki/wiki?15910) can configure the [Repository](https://wiki.genexus.com/commwiki/wiki?17568) and GAM settings to generate trace information about the execution of the GAM libraries.

### [Steps to Enable Repository Tracing in GAM](#Steps+to+Enable+Repository+Tracing+in+GAM)

When running the [GAM Backoffice](https://wiki.genexus.com/commwiki/wiki?15935), the Repository settings can be edited, and the Enable tracing option can be configured to generate debug information by setting the value "1 - Debug":

`[imagen omitida: wiki id 58292]`

Tracing can be enabled with global scope in GAM Configurations. In this menu, the Enable tracing property has to be "1 - Debug".

`[imagen omitida: wiki id 58293]`

When the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535) is used, the code to start generating trace in a given repository is as follows:

```
&GAMRepository.EnableTracing = &EnableTracing //&GAMRepository is GAMRepository data type. &EnableTracing is based on GAMTracing domain.
```

The tracing information is added to the standard output.

For the
[GeneXus Java Generator](https://wiki.genexus.com/commwiki/wiki?12258), it can be found in Tomcat's stdout log file (it depends on the standard output of the servlets server).

For the
[GeneXus .NET Generator](https://wiki.genexus.com/commwiki/wiki?38604), the following property has to be configured:

* Log Level >= 4 (Info)  
  The trace location depends on the following properties:
* Log Output
* Log File

### [How to enable Trace from an Environment Variable](#How+to+enable+Trace+from+an+Environment+Variable)

Set the following Environment Variable: **GX\_GAM\_LOG\_LEVEL  = 1**

This environment variable enables the General Trace and the Trace of all repositories.

### [See Also](#See+Also)

[GAM - Troubleshooting](https://wiki.genexus.com/commwiki/wiki?22815)  
[HowTo: Generate trace of GAM Deploy Tool](https://wiki.genexus.com/commwiki/wiki?26297)


|  |
| --- |
| **Backlinks** |
| [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [HowTo: Generate GAM trace (GeneXus 18 Upgrade 10 or prior)](https://wiki.genexus.com/commwiki/wiki?58291) |

---
