---
title: "TLS Services"
source_id: 39253
source_url: https://wiki.genexus.com/commwiki/wiki?39253
genexus_version: "18"
---

# TLS Services

The evolution of the SSL (Secure Socket Layer) protocol to TLS (Transport Layer Security) may cause services that were correctly consumed under SSL to stop working when the configuration is changed to TLS, particularly when using TLS version 1.2.

TLS protocol support is implemented in the base software:  
    .NET Framework 4.6  
    Java JDK 1.8

Therefore, service clients may stop working when the service migrates to the TLS 1.2 protocol, depending on the framework/sdk used by the client (consumer).

The errors that can occur are similar to the following:

```
The underlying connection was closed: An unexpected error occurred on a send.
```

```
WARN  GeneXus.Http.Client.GxHttpClient - Error Execute System.Net.WebException: The request was aborted: Could not create SSL/TLS secure channel.
   at System.Net.HttpWebRequest.GetResponse()
   at GeneXus.Http.Client.GxHttpClient.Execute(String method, String name)
```

```
ERROR GxHttpClient [] - Error Execute Exception: System.Net.WebException 
Message: A conexão subjacente estava fechada: Erro inesperado em um envio. 
Source: System em System.Net.HttpWebRequest.GetResponse() 
    em GeneXus.Http.Client.GxHttpClient.Execute(String method, String name)
```

```
Nested Exception
Exception: System.IO.IOException
Message: EOF inesperado ou 0 bytes recebidos do fluxo de transporte.
Source: System
  em System.Net.FixedSizeReader.ReadPacket(Byte[] buffer, Int32 offset, Int32 count)
  em System.Net.Security.SslState.StartReadFrame(Byte[] buffer, Int32 readBytes, AsyncProtocolRequest asyncRequest)
  em System.Net.Security.SslState.StartReceiveBlob(Byte[] buffer, AsyncProtocolRequest asyncRequest)
  em System.Net.Security.SslState.CheckCompletionBeforeNextReceive(ProtocolToken message, AsyncProtocolRequest asyncRequest)
  em System.Net.Security.SslState.StartSendBlob(Byte[] incoming, Int32 count, AsyncProtocolRequest asyncRequest)
```

The way to solve these errors will depend on the platform/language and how these services are invoked. The different alternatives are detailed below.

## [.NET Framework Generator](#.NET+Framework+Generator)

In [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892) you can follow two different paths:

* A: Change general settings in the web.config file, or
* B: Use the CSHARP command to change settings at some specific point in your programs.

### [A - Change settings in web.config](#A+-+Change+settings+in+web.config)

This option is valid if you have .NET framework 4.6.1 or higher (which requires Windows Server 2008 SP2 or higher)

```
<system.web>
  <httpRuntime targetFramework="4.6.1"/>
</system.web>
```

**Note**: 4.6.2 is already set by default as of [GeneXus 17 upgrade 4](https://wiki.genexus.com/commwiki/wiki?47936,,).

### [B - Change settings using CSHARP command](#B+-+Change+settings+using+CSHARP+command)

#### [1.  The service is invoked using [External Object / Web Service](https://wiki.genexus.com/commwiki/wiki?6154)](#1.+The+service+is+invoked+using+wiki%3F6154%2CExternal%2BObject%253A%2BWSDL%2B-%2BWeb%2BService+External+Object+%2F+Web+Service)

In this case, there are two scenarios:   
  1.1 - If the Environment property [Use Native Soap](https://wiki.genexus.com/commwiki/wiki?13446) = **True**, it is solved with code embedded in the GeneXus source itself. Before invoking the service, enter these lines:

```
csharp System.Net.ServicePointManager.SecurityProtocol = System.Net.SecurityProtocolType.Tls;
&ExternalObject.method(...)
```

  1.2 - If the Environment property [Use Native Soap](https://wiki.genexus.com/commwiki/wiki?13446) = **False**, add this line before invoking the service, in the GeneXus code.

```
csharp System.Net.ServicePointManager.SecurityProtocol = System.Net.SecurityProtocolType.Tls12 | System.Net.SecurityProtocolType.Tls11 | System.Net.SecurityProtocolType.Tls;
&ExternalObject.method(...)
```

Framework 4.0 or higher is required.  
With Framework 3.5 or lower, find the module that implements TLS 1.2 and install it.

#### [2. The service is invoked with [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932)](#2.+The+service+is+invoked+with+wiki%3F6932%2CHttpClient%2Bdata%2Btype+HttpClient+data+type)

In this case, you must configure the settings described in item 1.2.

```
csharp System.Net.ServicePointManager.SecurityProtocol = System.Net.SecurityProtocolType.Tls12 | System.Net.SecurityProtocolType.Tls11 | System.Net.SecurityProtocolType.Tls;
&httpclient.WriteStartElement("SOAP-ENV:Envelope")
&httpclient.WriteAttribute("xmlns:SOAP-ENV", "...")
```

## [Java Generator](#Java+Generator)

With JDK 1.8 or higher 1.7 u131 there are no additional requirements, as TLS v1.2 is used by default. This applies whether the service is consumed with [External Object: WSDL - Web Service](https://wiki.genexus.com/commwiki/wiki?6154) or with [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932).

With JDK 1.7 lower u131 it doesn't work; although TLS v1.2 is supported, the default value is TLS v1. To make it work, you should change the default value to Tls v1.2.

It is possible by configuring the Virtual Machine:

-Dhttps.protocols=TLSv1.2

Another way to do the same is to add the following native code to GeneXus source:

```
java try { 
    java javax.net.ssl.SSLContext ctx = javax.net.ssl.SSLContext.getInstance("TLSv1.2");
    java ctx.init(null, null, null);
    java javax.net.ssl.SSLContext.setDefault(ctx); 
java } catch (Exception e) {
java }
&ExternalObject.method(...)
```

Important: This code changes the default for the entire Web server.

For versions lower than JDK1.7, you should find out if it is possible to install the TLS protocol support.

## [IOS (Offline)](#IOS+%28Offline%29)

If a TLS service is invoked from an Offline Panel, it is recommended that it runs under IOS 11. Even though support for 802.1X authentication is available as of iOS 9, some issues have been reported until version 11, so this is the recommended version.

## [Android (Offline)](#Android+%28Offline%29)

As mentioned in the Java section, Java 8 is required; therefore, there are no issues in this platform.
