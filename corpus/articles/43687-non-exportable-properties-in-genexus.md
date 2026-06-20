---
title: "Non exportable properties in GeneXus"
source_id: 43687
source_url: https://wiki.genexus.com/commwiki/wiki?43687
genexus_version: "18"
---

# Non exportable properties in GeneXus

Some properties in a Knowledge Base are not exported when the environment is exported to a xpz, and they are not sent to genexus server when a Knowledge Base is uploaded.

The KB generator properties that are not exported are:

* Servlet Directory
* Static Content Directory Seen From Client
* Web Root

The data store properties that are not exported are:

* Server Name
* Database Name
* User Id
* User Password
* Use Trusted Connection
* Custom Jdbc Url
* Use Custom Jdbc Url

The "Integrated security" properties that are not exported are:

* Security Client Secret
* Security Client ID
* Security Client Encription Key

Mobile properties

* Key Store File
* Key Alias
* Store Password
* Key Password
* Apple Distribution Method

For more information: [SAC #37075](https://www.genexus.com/developers/websac?en,,,37075)
