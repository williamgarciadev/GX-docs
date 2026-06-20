---
title: "GxSoapHandlers mechanism for extending Location Data type"
source_id: 39413
source_url: https://wiki.genexus.com/commwiki/wiki?39413
genexus_version: "18"
---

# GxSoapHandlers mechanism for extending Location Data type

A Soap service is consumed from an environment with the Use Native Soap property set to True. Also, a mechanism is provided that allows you to do something similar to the location data type, extending its functionalities without the need to load this type of data with language specifics.

## [.NET](#.NET+)

Allows you to modify or add data in a SOAP service request to add credentials and certificates, change URLs, etc.  
For example, to change the URI Service of a Web Service that will be called you can follow the steps below:

### [1. Configuration](#1.+Configuration)

For this implementation to take effect, you must edit the web.config and add the line.

```
    <add key="NativeChannelConfigurator" value="GxSoapHandler"/>
```

### [2. GeneXus code](#2.+GeneXus+code)

You must also set a Configuration (NonStandard) property to the location data type, and there send the necessary parameters that you want to add/modify, either as a string, SDT, or object.  
In this case, to change the URI of the service, go to this Configuration property and program something like this:

```
    &location = GetLocation("WS_eFactura")
    &location.Configuration= "https://efactura.dgi.gub.uy:443/efactura/ws_efactura". //passing the NewUriService

    // Load a sample Invoice
    &pWS_eFacturaData.xmlData.FromString("")
    &pWS_eFacturaDataResult = &WS_eFactura.EFACRECEPCIONSOBRE(&pWS_eFacturaData)
    &longvar = &pWS_eFacturaDataResult.ToXml()
```

### [3. Building the Assembly](#3.+Building+the+Assembly)

An assembly called GxSoapHandler.dll will be invoked before the service call and this is where the parameters sent by the GeneXus program will be overwritten.  
It must be created and deployed; to do so, check the repo [GxSoapHandlerNet](https://github.com/genexuslabs/DotNetClasses/tree/master/dotnet/src/extensions/ws/src/GxSoapHandler) and Build/Run the GxSoapHandler.csproj, taking the following considerations into account:

1. Include a reference to **KBNamespace**.Programs.Common.dll in GxSoapHandler.csproj and replace ISdtWS\_eFacturaDummy in GxSoapHandler.cs with the correct web service name.
2. Edit the GxSoapHandler.cs; for example, if you only want to overwrite the URL, you can program it like this:

   ```
   using System;
   using System.ServiceModel;
   using GeneXus.Programs;
   using GeneXus.Utils;
   using System.ServiceModel.Description;

   public class GxSoapHandler
   {
       public void Setup( string eoName, GxLocation loc, object serviceClient)
       {
           if (eoName == "WS_eFactura" ) 
           {
               string NewUriService = loc.Configuration.ToString();
               ClientBase<ISdtService1> svc = serviceClient as ClientBase<ISdtService1>;
               svc.Endpoint.Address = new System.ServiceModel.EndpointAddress(NewUriService);  //changes the service URI
           }
       }
   }
   ```
3. Build the assembly with one of the following commands:  

   ```
   msbuild /t:restore;build /p:Configuration=Release dotnet\src\extensions\ws\src\GxSoapHandler\GxSoapHandler.csproj
   ```

   or  

   ```
   dotnet build -c Release dotnet\src\extensions\ws\src\GxSoapHandler\GxSoapHandler.csproj
   ```
4. Copy dotnet\src\extensions\ws\src\GxSoapHandler\bin\Release\net462\GxSoapHandler.dll to the web\bin folder.

#### [**Troubleshooting**](#Troubleshooting)

If the following error appears at Build time:

```
 error NU1105: Unable to find project information for 'C:\...\DotNetClasses\dotnet\src\dotnetframework\GxClasses\GxClasses.csproj'.
```

Open the Visual Studio console and run a restore command of this project.

## [JAVA](#JAVA)

It allows you to add data to the SOAP request, for example, to send a SAM-L token for authentication.

This is implemented through an external jar. If the classpath contains a class called com.genexus.util.GXSoapHandler, a static method of that class called setHandlers will be invoked before the service call.  
   
This method has the following parameters:

```
public static void setHandlers(Integer remoteHandle, com.genexus.ModelContext context, String serviceName, javax.xml.ws.BindingProvider bProvider)
```

Download a sample project: <https://github.com/genexuslabs/GxSoapHandlerJava>


|  |
| --- |
| **Backlinks** |
| [Location data type](https://wiki.genexus.com/commwiki/wiki?6981) |

---
