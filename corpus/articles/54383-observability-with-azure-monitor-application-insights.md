---
title: "Observability with Azure Monitor Application Insights"
source_id: 54383
source_url: https://wiki.genexus.com/commwiki/wiki?54383
genexus_version: "18"
---

# Observability with Azure Monitor Application Insights

GeneXus enables monitoring and analyzing the performance of applications using the features and capabilities of [Azure Application Insights](http://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview?tabs=net) through [instrumentation](https://learn.microsoft.com/en-us/azure/azure-monitor/app/codeless-overview#what-is-auto-instrumentation-for-azure-monitor-application-insights) for:

* .NET Web applications running elsewhere.
* Java Web containerized applications ([Deploy to Docker](https://wiki.genexus.com/commwiki/wiki?47839)). As auto-instrumentation in Java consists only on attaching a Java agent JAR to any Java 8+ application. It can be done at production using infrastructure configuration.

Assuming you have already defined the [Application Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview?tabs=net) and have access to the [Connection String](http://learn.microsoft.com/en-us/azure/azure-monitor/app/azure-web-apps-java#connection-string-and-instrumentation-key), as the figure shows, you can follow the steps below:

`[imagen omitida: wiki id 54384]`

1. Set the [Observability Provider property](https://wiki.genexus.com/commwiki/wiki?53408).
2. Deploy your application.
3. Configure the Environment Variables.
4. Analyze the data.

### [Set the Observability Provider property](#Set+the+Observability+Provider+property)

Set the [Observability Provider property](https://wiki.genexus.com/commwiki/wiki?53408) to "Azure Monitor Application Insights" value.

### [Deploy your application](#Deploy+your+application)

In Java, use the deployment engine tool to deploy your app to Docker (builds a Docker image).

### [Configure the Environment Variables](#Configure+the+Environment+Variables)

Set an environment variable pointing to the Connection String.  
  
The environment variable should be:

```
APPLICATIONINSIGHTS_CONNECTION_STRING=<Connection String>
```

For the case of containerized applications, you set the environment variable when you [run](https://docs.docker.com/engine/reference/commandline/run/) the Docker image.

If the environment variable is not set, the connection string will be calculated using a default Credential authentication flow based on the order explained [here](https://learn.microsoft.com/en-us/dotnet/api/azure.identity.defaultazurecredential?view=azure-dotnet). This applies to applications that will be deployed to Azure.

#### [Sample](#Sample)

```
docker run -p 8081:8080 -e APPLICATIONINSIGHTS_CONNECTION_STRING="InstrumentationKey=00000000-0000-0000-0000-000000000000;IngestionEndpoint=https://westus-0.in.applicationinsights.azure.com/;LiveEndpoint=https://westus.livediagnostics.monitor.azure.com/" miImageId
```

**Note:** You may need to add other environment variables, such as [APPLICATIONINSIGHTS\_ROLE\_NAME](https://learn.microsoft.com/en-us/azure/azure-monitor/app/java-standalone-config#cloud-role-name). See [here](https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-configuration?tabs=aspnetcore#opentelemetry-configurations) for more information. The app which is going to be instrumented, and its components don't have to be hosted in Azure. The instrumentation monitors your app and directs the telemetry data to an Application Insights resource using a unique token.

### [Getting Opentelemetry logs in Application Insights](#Getting+Opentelemetry+logs+in+Application+Insights)

In case of .NET and Azure Monitor, you just need to set the [Observability Provider property](https://wiki.genexus.com/commwiki/wiki?53408) to *Azure Monitor Application Insights*.  
The Operation\_id (which is the same as the trace id of Opentelemetry) will be present at the logs, and you can get the logs for each trace by filtering by the OperationId.  
The log level should be set using [GX\_LOG\_LEVEL environment variable](https://wiki.genexus.com/commwiki/wiki?53361).

`[imagen omitida: wiki id 56051]`

After selecting the OperationId, you can see the logs for that trace.

`[imagen omitida: wiki id 56052]`

**Note**: When you set [Observability Provider property](https://wiki.genexus.com/commwiki/wiki?53408) to Azure Monitor Application Insights in a .NET [Environments](https://wiki.genexus.com/commwiki/wiki?7115), the [Log output property](https://wiki.genexus.com/commwiki/wiki?39568) is ignored, and the log provider used is Azure Monitor.

### [Analyze the data](#Analyze+the+data)

After running the application, follow the steps in the [Azure documentation](https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-enable?tabs=java#confirm-data-is-flowing) to analyze the data obtained. See [Distributed tracing telemetry correlation](https://learn.microsoft.com/en-us/azure/azure-monitor/app/distributed-tracing-telemetry-correlation).  
  
`[imagen omitida: wiki id 54386]`  
  
`[imagen omitida: wiki id 54733]`

### [Scope](#Scope)

**Generator:** [Java](https://wiki.genexus.com/commwiki/wiki?12258), [.NET](https://wiki.genexus.com/commwiki/wiki?38604)

### [Availability](#Availability)

This functionality is available since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238).

### [See Also](#See+Also)

[Configuration options: Azure Monitor Application Insights for Java](https://learn.microsoft.com/en-us/azure/azure-monitor/app/java-standalone-config)


|  |
| --- |
| **Backlinks** |
| [HowTo: Observability of your GeneXus applications](https://wiki.genexus.com/commwiki/wiki?53767) | [HowTo: Observability of your GeneXus applications (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55863) | [HowTo: See trace information in applications hosted on .NET Cloud](https://wiki.genexus.com/commwiki/wiki?20541) |
| [Toc:Observability](https://wiki.genexus.com/commwiki/wiki?53765) | [Observability in GeneXus Apps](https://wiki.genexus.com/commwiki/wiki?53773) | [Observability in GeneXus Apps (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55862) | [Observability with Azure Monitor Application Insights (GeneXus 18 Upgrade 6)](https://wiki.genexus.com/commwiki/wiki?56153) |

---
