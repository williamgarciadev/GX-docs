---
title: "Web Notifications and Progress UC requirements"
source_id: 27740
source_url: https://wiki.genexus.com/commwiki/wiki?27740
genexus_version: "18"
---

# Web Notifications and Progress UC requirements

Both functionalities - [Server.Socket external object](https://wiki.genexus.com/commwiki/wiki?22442), and [Progress Indicator User Control](https://wiki.genexus.com/commwiki/wiki?31275) - have the same requirements which are detailed below:

## [Client Requirements](#Client+Requirements)

* Internet Explorer 10 or higher
* Mozilla Firefox 7 or upper
* Google Chrome 14 or upper
* Safari 5
* Safari for iOS 4.2.1

## [Web Server Requirements](#Web+Server+Requirements)

### [Java](#Java)

In [Java](https://wiki.genexus.com/commwiki/wiki?12258), the implementation is based on JSR 356, Java API for WebSocket.

#### [Required:](#Required%3A)

* Java 8
* Java EE 8–compliant application server (minimum required: Tomcat 8)
* Servlet server running on JVM 1.8

### [.NET Framework](#.NET+Framework+)

#### [Software requirements:](#Software+requirements%3A)

* IIS8 or higher (Window 8 or higher / Windows Server 2012 or higher)
* [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892) 4.5 or higher

`[imagen omitida: wiki id 51517]`

* IIS8 'WebSocket' module installed. To install this module for Windows, do the following:
* In the control panel, click the Windows button
* Type: Turn windows features on or off
* Navigate to: Internet Information Services > world Wide Web services > Application Development Features
* Select “Websocket Protocol” and OK

`[imagen omitida: wiki id 51519]`

* .Net implementation uses the following assemblies

  - Microsoft.WebSockets.dll  
  - GXWebSocket.dll

## [Configuration requirements:](#Configuration+requirements%3A)

* "[Compiler Path](https://wiki.genexus.com/commwiki/wiki?9013)" .NET Generator property set to use .NET Framework v4.0 (typically under "C:\Windows\Microsoft.NET\Framework\v4.0.30319\csc.exe")
* Application Pool in IIS must be configured for running with .NET Framework v4.0
* [IIS Version Property](https://wiki.genexus.com/commwiki/wiki?17521) = IIS8.
* The web application must be Smooth (full ajax), that is Version Property "Web User Experience = Smooth

## 

## [**Troubleshooting:**](#Troubleshooting%3A)

1. Verify File "**CloudServices**.config" is present in the Deployment. This File MUST exist.

**2. Verify web.config:**

```
<httpRuntime requestValidationMode="2.0" targetFramework="4.5" />
```

//The Following Lines must NOT be present:

```
<compilation>
  <assemblies>
    <remove assembly="GXWebSocket" />
    <remove assembly="Microsoft.WebSockets" />
  </assemblies>
</compilation>
```

3. If you compile with framework 2.0, run on ASP.net 2.x, you may get this:

```
FileLoadException: Could not load file or assembly 'log4net, Version=1.2.11.0, Culture=neutral, PublicKeyToken=669e0ddf0bb1aa2a' or one of its dependencies.
The located assembly's manifest definition does not match the assembly reference. (Exception from HRESULT: 0x80131040)
SuperSocket.SocketBase.Logging.Log4NetLogFactory..ctor(String log4netConfig) +0
```

**Solution: Apply Requirements**

4. If you haven't the Web Socket Protocol installed you see the following error (or similar) in the web console:

```
Firefox can’t establish a connection to the server at
ws://localhost/WebAppName/gxwebsocket?6977921532b3f2ecd1022896025d931c6062249c.
```

5. If you have Tomcat connected with Apache, one possible solution to make the Web Notifications work is the following:

Define these entries in the Apache configuration file:

* ProxyPass /**<webapp name>**/gxwebsocket ws://127.0.0.1:8280/**<webapp name>**/gxwebsocket
* ProxyPassReverse /**<webapp name>**/gxwebsocket ws://127.0.0.1:8280/**<webapp name>**/gxwebsocket

Then enable the proxy\_wstunnel module in Apache.

### [**Limitations**](#Limitations)

* .Net Environment (Windows 10 Server) does not support more than 10 webSocket simultaneous connections .

> ```
> Windows 10      IIS v10.0
> Home:           No IIS *We Think*
> Pro:            simultaneous request execution limit of 10, allows multiple sites *We Think*
> Enterprise:     simultaneous request execution limit of 10, allows multiple sites *We Think*
> Education:      unknown at this time
> IoT Core:       unknown at this time
> ```


|  |
| --- |
| **Backlinks** |
| [Chatbot generator](https://wiki.genexus.com/commwiki/wiki?37102) | [Chatbot Generator - Troubleshooting](https://wiki.genexus.com/commwiki/wiki?41260) | [How To: Use a Progress Indicator in a Web Panel](https://wiki.genexus.com/commwiki/wiki?32779) |
| [HowTo:Develop a messaging web page](https://wiki.genexus.com/commwiki/wiki?22527) | [KB:OnlineShop (Shopping cart sample)](https://wiki.genexus.com/commwiki/wiki?27158) | [Progress external object](https://wiki.genexus.com/commwiki/wiki?39341) | [Server.Socket external object](https://wiki.genexus.com/commwiki/wiki?22442) |
|

---
