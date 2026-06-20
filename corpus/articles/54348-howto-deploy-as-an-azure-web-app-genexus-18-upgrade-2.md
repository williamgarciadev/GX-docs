---
title: "HowTo: Deploy as an Azure Web App (GeneXus 18 Upgrade 2)"
source_id: 54348
source_url: https://wiki.genexus.com/commwiki/wiki?54348
genexus_version: "18"
---

# HowTo: Deploy as an Azure Web App (GeneXus 18 Upgrade 2)

The [Build > Deploy Application](https://wiki.genexus.com/commwiki/wiki?32092) menu option allows you to deploy a web application as an Azure WebApp (formerly known as an Azure WebSite).

The following document explains the process of creating an Azure WebApp from the Azure portal and deploying your GeneXus web application there.

### [Step 1](#Step+1)

If you are deploying on a .NET [Environment](https://wiki.genexus.com/commwiki/wiki?7115), make sure that you have [MSDeploy](https://www.iis.net/downloads/microsoft/web-deploy) installed on your machine.

### [Step 2](#Step+2)

Go to the [Azure portal](https://portal.azure.com) and follow the instructions provided there to create a new WebApp:

`[imagen omitida: wiki id 31458]`

### [Step 3](#Step+3)

Under the Runtime Stack combo use the following table to select the right stack for your environment.

| Environment | Runtime stack |
| --- | --- |
| [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892) (C#) | ASP.NET V4.7 (or higher) |
| [Java](https://wiki.genexus.com/commwiki/wiki?12258) | Tomcat 9.0 |
| [.NET](https://wiki.genexus.com/commwiki/wiki?38604) | .NET 5 |

  
It will take a few seconds for the WebApp to be created. After that, you will have the settings and data of your recently created WebApp.

### [Step 4](#Step+4)

Click on the "Get Publish Profile" link to download the .PublishSettings file, which contains the credentials needed to deploy the recently created WebApp. Remember that GeneXus will ask for that file afterwards.

`[imagen omitida: wiki id 31459]`

That's it from the Azure portal.

### [Step 5](#Step+5)

Now, go to GeneXus and select **Build > Deploy Application**in the main menu.

`[imagen omitida: wiki id 31460]`

### [Step 6](#Step+6)

At the [Publish Settings File property](https://wiki.genexus.com/commwiki/wiki?46406), you have to enter the *.publishProfile* file you downloaded in step 3 of this document. Select that file and that's it: GeneXus will gather all the necessary information to transfer your web app to the cloud.

Note that you can then manage other app settings at the Azure portal.

**Note:** If you are deploying to
[.NET](https://wiki.genexus.com/commwiki/wiki?38604) in Linux, you need to set the Startup Command under the Configuration panel to:

```
dotnet bin/GxNetCoreStartup.dll
```

### [Step 7](#Step+7)

Run the application.

Once the application gets deployed, you can access it by going to your web app URL plus your object. For instance, if you have deployed a WebPanel called Hello, add *hello.aspx* to your URL if your deploy was either
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892) or
[.NET](https://wiki.genexus.com/commwiki/wiki?38604). If it's
[Java](https://wiki.genexus.com/commwiki/wiki?12258), make sure you add servlet/<java package name>.<object name>
