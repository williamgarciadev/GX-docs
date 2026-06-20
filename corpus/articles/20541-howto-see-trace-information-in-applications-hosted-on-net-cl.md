---
title: "HowTo: See trace information in applications hosted on .NET Cloud"
source_id: 20541
source_url: https://wiki.genexus.com/commwiki/wiki?20541
genexus_version: "18"
---

# HowTo: See trace information in applications hosted on .NET Cloud

Sometimes errors occur in your applications and debugging them is necessary. For instance, when you are developing [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892) applications hosted on GeneXus' Servers (i.e. using [Cloud prototyping](https://wiki.genexus.com/commwiki/wiki?15046)) the [Log level property](https://wiki.genexus.com/commwiki/wiki?36304) is very useful, and you can have all the information you need to solve all these issues.

### [How to see the log file in an application hosted on .NET Cloud?](#How+to+see+the+log+file+in+an+application+hosted+on+.NET+Cloud%3F)

The following properties need to be set on the .NET Framework Generator:

* Log level property = Any value other than Off
* [Log output property](https://wiki.genexus.com/commwiki/wiki?39568) = ASP.NET trace

Once enabled, a new property in the web.config will be available under system.web:

```
<trace enabled="true" localOnly="false" />
```

If the localOnly value is set to false, the log can be accessed by the following URL:

http://apps3.genexusx.com/<VirtualDirectory>/trace.axd

The log is similar to the one shown below:

`[imagen omitida: wiki id 20543]`

**Note:**

In cloud environments, the generation of log files may vary depending on the service used. Often, the use of archives is avoided due to the complexity of maintenance in environments with multiple balanced servers. In addition, the management of multiple microservices may require centralised visualisation of logs.

There are several tools and services available for this task, beyond trace.axd. For example, GeneXus, which has advanced [Observability](https://wiki.genexus.com/commwiki/wiki?53765), allows logs to be generated and sent to cloud services such as [Azure Application Insights](https://wiki.genexus.com/commwiki/wiki?54383). With Opentelemetry, it is also possible to direct application logs to any compatible backend for centralised viewing.

It is relevant to note that this functionality is exclusively available for [.NET](https://wiki.genexus.com/commwiki/wiki?38604), and not for .NET Framework, due to the progressive discontinuation of the latter in terms of support and compatibility with emerging technologies such as Opentelemetry.


|  |
| --- |
| **Backlinks** |
| [HowTo: Emulate SSO without using GAM remote authentication](https://wiki.genexus.com/commwiki/wiki?38116) | [Log external object](https://wiki.genexus.com/commwiki/wiki?37872) | [Log level property](https://wiki.genexus.com/commwiki/wiki?36304) |
| [Log level property (GeneXus 18 upgrade 6)](https://wiki.genexus.com/commwiki/wiki?56151) | [Log output property](https://wiki.genexus.com/commwiki/wiki?39568) | [Log output property (GeneXus 18 Upgrade 0 or prior)](https://wiki.genexus.com/commwiki/wiki?53419) | [Log output property (GeneXus 18 upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?56148) |
| [Log output property (GeneXus 18 Upgrade 7)](https://wiki.genexus.com/commwiki/wiki?57249) | [User Log level property](https://wiki.genexus.com/commwiki/wiki?42434) |

---
