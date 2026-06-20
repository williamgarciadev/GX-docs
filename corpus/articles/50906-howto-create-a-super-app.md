---
title: "HowTo: Create a Super App"
source_id: 50906
source_url: https://wiki.genexus.com/commwiki/wiki?50906
genexus_version: "18"
---

# HowTo: Create a Super App

This document describes the steps to create a [Super App](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?50900,,) within GeneXus. The Super App can be any Native Mobile application, online or offline, generated with GeneXus.

If you already have an application that is not developed with GeneXus technology and want to convert it into a Super App, read the [GeneXus´s GitHub documentation](https://github.com/genexus-colab/gx-super-app), because GeneXus licenses the necessary technology to achieve it.

**Note:** The code snippets and images included in this document are obtained from the [Verdant Bank Knowledge Base sample](https://wiki.genexus.com/commwiki/wiki?56766).

## [Steps to create a Super App with GeneXus](#Steps+to+create+a+Super+App+with+GeneXus)

Suppose you have already developed an application that provides certain functionalities, and you want specific functionalities or services to be provided through [Mini Apps](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?50900,,). To do this, you must transform the application into a Super App. The steps are described below:

### [Getting Started](#Getting+Started)

Before developing a Super App, you have to contact a sales representative in order to create a [Mini App Center](https://wiki.genexus.com/commwiki/wiki?51290) (because, without the Mini App Center, it will not be possible to upload the Mini Apps that will be executed within the context of a Super App).

Then you will need a Super App Administrator account in the Mini App Center, that will allow you to manage your Super App and the Mini Apps (developed by your organization or by third parties).

The steps here are:

1. [Register your Organization](https://wiki.genexus.com/commwiki/wiki?53309)
2. [Define the Super App and the version](https://wiki.genexus.com/commwiki/wiki?53316)
3. [Obtain the Public Key for the Super App version](https://wiki.genexus.com/commwiki/wiki?57522)

### [Creating your Super App](#Creating+your+Super+App)

In the Super App's Knowledge Base, you must:

#### [1. Install the GeneXus Super App Module](#1.+Install+the+GeneXus+Super+App+Module)

The [GeneXusSuperApps Module](https://wiki.genexus.com/commwiki/wiki?50959) must be installed from Knowledge Manager > Manage Module References.

#### 

It is made up of two External Objects:

* **Provisioning**: To interact with the Mini App Center services in order to get the Mini Apps.
* **MiniApps**: To load and manage the Mini Apps.

#### 

#### [2. Get and show the Mini Apps](#2.+Get+and+show+the+Mini+Apps)

It is assumed that you have already created an application, so you have a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) or [Menu object](https://wiki.genexus.com/commwiki/wiki?16321) declared as [Main Object](https://wiki.genexus.com/commwiki/wiki?5770). This application will act as a Super App.

The next step is to add the functionality to access the Mini Apps. Add the code for this in the Panel where you will show the Mini Apps.

```
Event Refresh
      &AllMiniApps = GeneXusSuperApps.Provisioning.GetByText('', &start, &count)
      &FeaturedMiniAppCollection = GeneXusSuperApps.Provisioning.GetFeatured(&start, &count)
endevent

Event GridMainMiniApps.Load
      &MiniAppName = !"QR Code"
      &MiniAppIcon.FromImage(image:icon_QRCode)
      load
      For &MiniApp in &AllMiniApps
      	  &MiniAppName = &MiniApp.Name
          &MiniAppIcon = &MiniApp.Icon
          load
      endfor
endevent

Event GridThisWeek.Load
      For &FeaturedMiniApp in &FeaturedMiniAppCollection
      	  &MiniAppThisWeekEntryPoint = &FeaturedMiniApp.EntryPoint
      	  &MiniAppThisWeekImage = &FeaturedMiniApp.Banner
      	  load
      endfor
endevent
```

**Note:** The methods of the [GeneXusSuperApps Module](https://wiki.genexus.com/commwiki/wiki?50959) can only be invoked from user events (client-events). In order to be invoked from a server event (such as Start, Refresh, or Load as in this example), the Panel must be offline or referenced from an offline Procedure object. This is a temporary limitation.

At the end of the process, in runtime, the application (Super App) will show something like this:

`[imagen omitida: wiki id 50909]`

#### [3. Create a Super App Object](#3.+Create+a+Super+App+Object)

The next step implies the creation of a [Super App object](https://wiki.genexus.com/commwiki/wiki?53457), which comprises two essential parts: Properties and [Super App Source](https://wiki.genexus.com/commwiki/wiki?53457).

`[imagen omitida: wiki id 50910]`

#### [3.1. Set the Super App Properties](#3.1.+Set+the+Super+App+Properties)

In the [Properties section](https://wiki.genexus.com/commwiki/wiki?53457), you will configure various properties, including:

1. Specify the Main object that will serve as the Super App.
2. Provide the credentials required to access the Mini App Center.
3. Set the registered Version ID for this particular Super App within the provisioning system.

When you build the Main object, the build process will note that this is a Super App, and it will generate the necessary configuration. As a result, when the application runs, it will operate seamlessly as a Super App, connecting to the designated provisioning server for retrieving the list of Mini Apps published for that particular Super App version.

`[imagen omitida: wiki id 50911]`

3.2. Implement the communication interface for the Mini Apps

To learn more about this topic, see the following link: [Super App API](https://wiki.genexus.com/commwiki/wiki?58207).

The final step is to do a Build, and then test and deploy the Super App.


|  |
| --- |
| **Backlinks** |
| [GeneXus Super App News and Roadmap](https://wiki.genexus.com/commwiki/wiki?53536) | [Table of contents:GeneXus Super Apps and Mini Apps](https://wiki.genexus.com/commwiki/wiki?50899) |
| [Super App API](https://wiki.genexus.com/commwiki/wiki?58207) |

---
