---
title: "Launchpad Tool Window"
source_id: 52315
source_url: https://wiki.genexus.com/commwiki/wiki?52315
genexus_version: "18"
---

# Launchpad Tool Window

Launchpad is a Tool Window within the [GeneXus IDE](https://wiki.genexus.com/commwiki/wiki?5272) that shows links to run certain objects of your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836).

It is meant to facilitate the prototyping cycle, especially for web and native mobile apps and APIs.

It opens when you press F5 if you have not defined a [Startup Object](https://wiki.genexus.com/commwiki/wiki?5393) already. Also, you can select **View > Other Tool windows > Launchpad** in the GeneXus main menu and it will open.

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

For prototyping APIs, this tab shows all the [REST APIs](https://wiki.genexus.com/commwiki/wiki?46151) contained in your KB and allows you to view and interact with them from inside the IDE. It uses [Swagger](https://wiki.genexus.com/commwiki/wiki?50321,,) UI for this.

Notes:

* It requires the [Generate OpenAPI interface property](https://wiki.genexus.com/commwiki/wiki?31859) to be set to Yes.
* To use this feature in [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892) environments, an environment variable named 'GX\_CORS\_ALLOW\_ORIGIN' with value 'gx-file://.' must be set.
* To prototype secure APIs, [REST OAuth](https://wiki.genexus.com/commwiki/wiki?15910) must be enabled.


|  |
| --- |
| **Backlinks** |
| [API object security scheme](https://wiki.genexus.com/commwiki/wiki?52550) | [Developer Menu](https://wiki.genexus.com/commwiki/wiki?18484) | [GAM - Permissions](https://wiki.genexus.com/commwiki/wiki?15912) |
| [GeneXus 18 Compatibility Section](https://wiki.genexus.com/commwiki/wiki?51080) | [GeneXus 18 Compatibility Section (GeneXus 18)](https://wiki.genexus.com/commwiki/wiki?53520) | [HowTo: Access secure REST services defined via API Objects](https://wiki.genexus.com/commwiki/wiki?52864) | [HowTo: Create a Dynamic Scripted Chatbot](https://wiki.genexus.com/commwiki/wiki?52874) |
| [HowTo: My first GeneXus Java Application](https://wiki.genexus.com/commwiki/wiki?45875) | [HowTo: My first GeneXus Java Application (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55769) | [Knowledge-driven with GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51573) | [Prototyping an API with Swagger](https://wiki.genexus.com/commwiki/wiki?50008) |
| [Startup Object property](https://wiki.genexus.com/commwiki/wiki?13606) | [Unsetting a Startup Object](https://wiki.genexus.com/commwiki/wiki?5398) |

---
