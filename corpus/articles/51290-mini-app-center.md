---
title: "Mini App Center"
source_id: 51290
source_url: https://wiki.genexus.com/commwiki/wiki?51290
genexus_version: "18"
---

# Mini App Center

The Mini App Center is an essential part of the [Super Apps](https://wiki.genexus.com/commwiki/wiki?50900,,) and [Mini Apps](https://wiki.genexus.com/commwiki/wiki?50900,,) architecture. It is a provisioning server where the Super App is declared and the Mini App definitions are stored to be later reached and loaded from the Super App.

When an organization decides to create a Super App, it must contact a sales representative in order to create a Mini App Center (because it is not possible to load the Mini Apps without the MiniApp Center).

This provisioning server provides the following functionalities:

* Registration of organizations, their members, and permissions. For instance, the definition of who may upload Mini Apps of a given Super App.
* Provision of digital signatures to be included in the Super App packaging.
* Provision of the services to search for Mini Apps for a given Super App. This is distributed through the [GeneXusSuperApps Module](https://wiki.genexus.com/commwiki/wiki?50959,,). These searches can be done by:
  + Keywords
  + Location
  + Relevance in a specific time period.
* Access management for Mini App releases (registration, release for review, enabling it for production). In other words, uploading and managing Mini Apps and their versions. Developers can easily upload their Mini Apps and their subsequent versions through the Mini App Center.
* Sign the metadata of a Mini App with the private key of the Super App. This is done automatically when a new Mini App version is uploaded.
* Review and approval process: The Super App owner has the authority to review and accept/reject the submitted Mini Apps and their versions to ensure quality control and adherence to guidelines.
* Additional administrative activities: The Mini App Center facilitates several administrative tasks related to managing the Mini Apps ecosystem, such as monitoring usage, generating reports, and configuring settings.


* [Organizations, Members and Permissions](https://wiki.genexus.com/commwiki/wiki?53309)
* Super App
  + [HowTo: Create a Super App on the Mini App Center](https://wiki.genexus.com/commwiki/wiki?53316)
  + [HowTo: Upload a Super App version to the Mini App Center](https://wiki.genexus.com/commwiki/wiki?56085)
  + [HowTo: Obtain a Super App Version Public Key](https://wiki.genexus.com/commwiki/wiki?57522)
* Mini Apps
  + [HowTo: Create a Mini App on the Mini App Center](https://wiki.genexus.com/commwiki/wiki?53317)
  + [HowTo: Upload a Mini App version to the Mini App Center](https://wiki.genexus.com/commwiki/wiki?53318)
  + [Submit a Mini App version for review](https://wiki.genexus.com/commwiki/wiki?53314)
  + [Mini App review and approval](https://wiki.genexus.com/commwiki/wiki?53315)
  + [Featured Mini Apps](https://wiki.genexus.com/commwiki/wiki?56095)
* API Reference
  + Platform
  + Organization
  + Super App
  + Mini App
* [Mini App Center installation](https://wiki.genexus.com/commwiki/wiki?55056,,)

---
