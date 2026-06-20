---
title: "Build and deploy a static website to Azure Storage Static Websites: setting up the cloud"
source_id: 49887
source_url: https://wiki.genexus.com/commwiki/wiki?49887
genexus_version: "18"
---

# Build and deploy a static website to Azure Storage Static Websites: setting up the cloud

To deploy an [Angular](https://wiki.genexus.com/commwiki/wiki?42550) application to Azure Storage Websites, use the Application deployment tool as explained in [HowTo: Deploy Frontend applications to Azure Blob Storage](https://wiki.genexus.com/commwiki/wiki?49878).

This document shows the steps to prepare the cloud infrastructure, so as to perform the deployment afterwards. Basically, we will create an Azure Storage account where the static files will reside, and a [CDN](https://docs.microsoft.com/en-us/azure/cdn/cdn-overview).

### [Setting up the Storage Account](#Setting+up+the+Storage+Account)

You can host a static website by enabling the static website feature on an Azure blob storage account.

1. To access Azure Storage, you'll need an Azure subscription.  
2. Every access to Azure Storage takes place through a storage account. See Create a [Storage account](https://docs.microsoft.com/en-gb/azure/storage/common/storage-account-create?tabs=azure-portal).

The first step is to configure your storage account to host a static website in the Azure portal. When you configure your account for static website hosting, Azure Storage automatically creates a container named $web. The $web container will contain the files for your static website. See [Configure static web site hosting](https://docs.microsoft.com/en-gb/azure/storage/blobs/storage-blob-static-website-host#configure-static-website-hosting).

Navigate to your storage account within Azure, click on the static website menu option, and set the following:

* Static Website: Enabled
* Index Document name: index.html
* Error Document path: index.html

Click on Save.

Once you’ve enabled a static website within your storage account, your storage account will contain a container called $web; this is the container where the deployment will upload the Angular build files.

 As part of the process, you’ll also have been assigned a primary endpoint. Note the primary endpoint; this is the URL to the new website, and it will be necessary when configuring the CDN you will create next.

`[imagen omitida: wiki id 49888]`

`[imagen omitida: wiki id 49889]`

`[imagen omitida: wiki id 49891]`

To get the Access Key (to fill in the "Storage Account Key" property at deployment), go through the Access Keys pane of the Storage account.

`[imagen omitida: wiki id 49892]`

At deployment, all of the files from your distribution folder are uploaded to the $web container.

### [Creating a CDN](#Creating+a+CDN)

To test that everything works, you can access the application using the *primary endpoint* URL, for example.

However, since Static websites have some limitations, you'll probably have to use [Azure Content Delivery Network](https://docs.microsoft.com/en-us/azure/cdn/cdn-overview) (Azure CDN).

First, define a CDN profile, and a CDN endpoint whose "origin hostname" should be the same as the static website endpoint previously defined.

Select your storage account and go through the Azure CDN menu option on the left-hand pane. Next, enter the required data and select "create."

`[imagen omitida: wiki id 50005]`

The result will be as follows:

`[imagen omitida: wiki id 49999]`

### [Configure URL Rewrite rule to fall back to index.html](#Configure+URL+Rewrite+rule+to+fall+back+to+index.html)

Since Angular is a Single Page Application (SPA), you will need a URL Rewrite rule that returns the app’s root index.html file for any request to a path that isn’t an actual file. See the detailed explanation [here](https://angular.io/guide/deployment#routed-apps-must-fallback-to-indexhtml).

So, go through the Rules Engine option on the left-hand pane of the CDN endpoint and define a rule as shown in the figure:

`[imagen omitida: wiki id 50006]`

For more information, read the [Azure documentation](https://docs.microsoft.com/en-us/azure/storage/blobs/static-website-content-delivery-network?WT.mc_id=Portal-Microsoft_Azure_Support#remove-content-from-azure-cdn).

### [Accessing the application](#Accessing+the+application)

The application can be accessed using the CDN endpoint URL. Find the endpoint URL for the CDN endpoint by going back to the endpoint overview. Copy the ‘Endpoint hostname’ in your browser.

### [See Also](#See+Also)

[Redirect users to Https](https://docs.microsoft.com/en-us/azure/cdn/cdn-standard-rules-engine#redirect-users-to-https)  
[CDN troubleshoot endpoint](https://docs.microsoft.com/en-us/azure/cdn/cdn-troubleshoot-endpoint)


|  |
| --- |
| **Backlinks** |
| [HowTo: Deploy Frontend applications to Azure Blob Storage](https://wiki.genexus.com/commwiki/wiki?49878) |

---
