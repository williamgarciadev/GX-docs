---
title: "Launchpad Tool Window (GeneXus 18 latest upgrade or prior)"
source_id: 60884
source_url: https://wiki.genexus.com/commwiki/wiki?60884
genexus_version: "18"
---

# Launchpad Tool Window (GeneXus 18 latest upgrade or prior)

Launchpad is a Tool Window within the [GeneXus IDE](https://wiki.genexus.com/commwiki/wiki?5272) that shows links to run certain objects of your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836).

It is meant to facilitate the prototyping cycle, especially for web and native mobile apps and APIs.

You can select **View > Other Tool windows > Launchpad** in the GeneXus main menu and it will open.

In addition, when you press F5, the Launchpad will open if you have not defined a [Startup Object](https://wiki.genexus.com/commwiki/wiki?5393) already (this does not apply when generating Native Mobile or frontend Angular apps, since in these cases a Startup Object must be defined).

In addition, when you press F5, the Launchpad will open if you have not defined a [Startup Object](https://wiki.genexus.com/commwiki/wiki?5393) already (this does not apply when generating Native Mobile or frontend Angular apps, since in these cases a Startup Object must be defined).

The Launchpad contains three Tabs:

### [1. WEB APPS](#1.+WEB+APPS)

This tab shows web apps or pages you may want to prototype and lets you execute them in your default browser with just a click.

Specifically, it shows [Main objects](https://wiki.genexus.com/commwiki/wiki?5770) and some recently created objects that are not main so that you can prototype them.

The objects shown are web apps or pages that can run on a browser (i.e. they are generated with [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)).

### 2. NATIVE APPS

For native apps, this tab offers:

* For [Apple](https://wiki.genexus.com/commwiki/wiki?14917): QR Code to download the [KBN](https://wiki.genexus.com/commwiki/wiki?18653), QR Codes, and "Copy" button to access your apps.
* For [Android](https://wiki.genexus.com/commwiki/wiki?14453): QR Codes and "Copy" button to access your apps.

### [3. APIS](#3.+APIS)

For prototyping APIs, this tab shows all the [REST APIs](https://wiki.genexus.com/commwiki/wiki?46151) contained in your KB and allows you to view and interact with them from inside the IDE. It uses [Swagger](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?50321,,) UI for this.

Notes:

* It requires the [Generate OpenAPI interface property](https://wiki.genexus.com/commwiki/wiki?31859) to be set to Yes.
* To use this feature in [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892) environments, an environment variable named 'GX\_CORS\_ALLOW\_ORIGIN' with value 'gx-file://.' must be set.
* To prototype secure APIs, [REST OAuth](https://wiki.genexus.com/commwiki/wiki?15910) must be enabled.
