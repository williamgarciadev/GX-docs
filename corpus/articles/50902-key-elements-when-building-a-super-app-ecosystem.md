---
title: "Key elements when building a Super App ecosystem"
source_id: 50902
source_url: https://wiki.genexus.com/commwiki/wiki?50902
genexus_version: "18"
---

# Key elements when building a Super App ecosystem

In building a Super App, there are three key components to take into consideration:

* [Key elements to create a Super App](https://wiki.genexus.com/commwiki/wiki?51288,,)
* [Key elements to create a Mini App](https://wiki.genexus.com/commwiki/wiki?51289)
* [Mini App Center](https://wiki.genexus.com/commwiki/wiki?51290) (the provisioning server of Mini Apps to each Super App)

## [How are these elements related in each stage?](#How+are+these+elements+related+in+each+stage%3F)

### [Development Stage](#Development+Stage)

The Super App must connect with the Mini App Center through its API in order to get the list of approved Mini Apps and expose them to the user in the UI.

It will probably expose some services (API) to their Mini Apps, for example, Pay(), GetUserId(). Those services must be implemented within the Super App.

`[imagen omitida: wiki id 52075]`

### [Deployment Stage](#Deployment+Stage)

The Super App (the application itself) would be deployed in each store (Google Play, Apple Store).

The Mini App (more precisely, its metadata with front-end information) will be uploaded to the Mini App Center. The backend services will be deployed on the server of each Mini App.

Upon approval by the Super App owner, the Mini App will be visible in the Super App, based on design and discovery criteria.

`[imagen omitida: wiki id 52074]`

### [Runtime](#Runtime)

The Super App accesses the Mini App Center to obtain the list of available Mini Apps in order to present them to the user in the Super App UI, in accordance with the implemented search and discovery criteria.

When the user selects a Mini App, the metadata is downloaded from the Mini App Center and the application is executed within the context of the Super App. The starts navigating through the Mini App, which the user could eventually invoke to resources/services of the Super App.

`[imagen omitida: wiki id 52072]`


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Super Apps and Mini Apps](https://wiki.genexus.com/commwiki/wiki?50899) |

---
