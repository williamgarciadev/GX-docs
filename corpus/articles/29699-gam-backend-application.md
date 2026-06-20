---
title: "GAM Backend Application"
source_id: 29699
source_url: https://wiki.genexus.com/commwiki/wiki?29699
genexus_version: "18"
---

# GAM Backend Application

The GAM Backend is a [GAM Application](https://wiki.genexus.com/commwiki/wiki?15910) defined automatically with the creation of the GAM metadata during the initialization process (for more information about this process, see [GAM repository creation for the first time from GeneXus](https://wiki.genexus.com/commwiki/wiki?29701)).

The purpose of the GAM Backend Application is to group a set of permissions related to some resources (1) of the [GAM - Examples](https://wiki.genexus.com/commwiki/wiki?21993). They are as follows:

* gamexamplechangerepository (gamexamplechangerepository\_Execute)
* gamexamplechangeyourpassword (gamexamplechangeyourpassword\_Execute)
* gamexamplewwapplications (gamexamplewwapplications\_Execute)
* gamexamplewwauthtypes (gamexamplewwauthtypes\_Execute)
* gamexamplewwconnections (gamexamplewwconnections\_Execute)
* gamexamplewwroles (gamexamplewwroles\_Execute)
* gamexamplewwsecuritypolicies (gamexamplewwsecuritypolicies\_Execute)
* gamexamplewwusers (gamexamplewwusers\_Execute)
* gamrepositoryconfiguration (gamrepositoryconfiguration\_Execute)

The main purpose of grouping these permissions is to be able to build the Menu of the GAM Backoffice in a dynamic way, using the [Action Group Control for the Web](https://wiki.genexus.com/commwiki/wiki?25631) control.

 `[imagen omitida: wiki id 29739]`

### [GAM Backend Application permits](#GAM+Backend+Application+permits)

By executing the [GAM Backoffice](https://wiki.genexus.com/commwiki/wiki?15935), going through the "Settings -> Applications" menu option, you can see *all* GAM applications, including the GAM Backend Application.

`[imagen omitida: wiki id 29741]`

As mentioned, the GAM Backend application groups a set of permissions that may be listed by clicking on the permissions option of the corresponding row, in the Applications grid.

### [GAM Backend menu](#GAM+Backend+menu)

The GAM Backend menu is dynamically built using the resources (1) mentioned above.

You can edit the GAM Backend menu definition, which consists of two menus, namely: the GAMBackendMainMenu, and the GAMBackendSettingsMenu.

`[imagen omitida: wiki id 29711]`

The GAMBackendMainMenu has the following options. One of them (the Settings option) is a menu in itself (the GAMBackendSettingsMenu).

`[imagen omitida: wiki id 29712]`

The image below shows the edition of the GAMBackendMainMenu:

`[imagen omitida: wiki id 29713]`

The following image is the GAMBackendSettingsMenu menu definition:

`[imagen omitida: wiki id 29708]`

### [Availability](#Availability)

As from [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?28265,,).


|  |
| --- |
| **Backlinks** |
|
| [GAM Backend Style Override property](https://wiki.genexus.com/commwiki/wiki?51754) | [GAM repository creation for the first time from GeneXus](https://wiki.genexus.com/commwiki/wiki?29701) | [Hardening of GeneXus Systems and Deployments with GAM](https://wiki.genexus.com/commwiki/wiki?47237) |
| [HowTo: Create New Repositories using GAM](https://wiki.genexus.com/commwiki/wiki?18642) | [HowTo: Define a Menu using GAM](https://wiki.genexus.com/commwiki/wiki?29681) | [Total Experience with GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51570) |

---
