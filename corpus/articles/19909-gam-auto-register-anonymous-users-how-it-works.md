---
title: "GAM - Auto-register anonymous users - How it works"
source_id: 19909
source_url: https://wiki.genexus.com/commwiki/wiki?19909
genexus_version: "18"
---

# GAM - Auto-register anonymous users - How it works

It is possible to automatically register a user and keep it anonymous. In fact, the application generated automatically creates a "user" of [GeneXus Access Manager](https://wiki.genexus.com/commwiki/wiki?24746) using the device identifier. The user created automatically has the following characteristics:

* It is seen by the application as any other user. See [GAM - Auto-register anonymous user - Panel usage example](https://wiki.genexus.com/commwiki/wiki?19911)
* It is absolutely anonymous from a personal viewpoint. No personal data of the individual operating the device is known, requested, or saved.
* It is possible to know the device identifier.

After having used the applications as an anonymous user, if the user decides to register in the application, GAM creates a new user (with the registration details) and assigns the same UserId that the auto-registered user had.

For GeneXus 15 upgrade 10 or previous, this happens only with [Custom Authentication](https://wiki.genexus.com/commwiki/wiki?21751), [External Web Services Authentication](https://wiki.genexus.com/commwiki/wiki?16512) and [Local Authentication](https://wiki.genexus.com/commwiki/wiki?20703). Since [GeneXus 15 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?38845,,) it's valid for any [GAM Authentication Type](https://wiki.genexus.com/commwiki/wiki?16508).

This allows for any information related to the auto-registered user saved by our application to remain associated with the new user registered.

How could the auto-registered anonymous user and the registered user be combined?

In the context of the [Auto register anonymous user](https://wiki.genexus.com/commwiki/wiki?19911) consider the following case:

If the [Menu object](https://wiki.genexus.com/commwiki/wiki?16321) has [Auto-register Anonymous User property](https://wiki.genexus.com/commwiki/wiki?19912) = True, and [Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214) = None, that means that it is possible to access this Menu without entering credentials, but the user cannot be auto-registered.

Note that the Menu has an Action Item that is a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) called "SubscribeNovel":

`[imagen omitida: wiki id 55305]`

Just like the Menu that it is calling it, it has the property Integrated Security Level = None.

This means that the behavior is the same as for the Menu – this Panel object will be executed without request for login or auto-register.  
The REST service SubscribeToNovels is called from the Panel object.

`[imagen omitida: wiki id 55306]`

Note in the image that Integrated Security Level = Authentication has been set in the Procedure:

`[imagen omitida: wiki id 55307]`

Therefore, when trying to execute this service, because it requires authentication and is in the tree of calls of a Menu object that accepts the registry of anonymous users, an auto-registration will occur through the mechanism described.

Every smart device can be singularly identified by means of a DeviceId, which enables the GAM to automatically create a "user" for the device in a transparent manner. Such user will be identified by the device Id. This user is considered by the application as a registered user. Specifically, any data that the logic of the application associates with a user will be then associated with that user’s identifier that has been automatically created.

This user’s session never expires (meaning that the [OAuth token expire (minutes)](https://wiki.genexus.com/commwiki/wiki?18577) does not apply in the case of anonymous users’ sessions).  
When the user of the device decides to register ([GAM - Registration](https://wiki.genexus.com/commwiki/wiki?19913,,)) using any of the methods available, the GAM will automatically relate the new user registered to the user created for the device, maintaining the user identifier. This prevents the application from having to make changes to the user-data relations it has already established.

Note: Until GeneXus 15 upgrade 10, the registration has to be done using Local Authentication to relate the registered user to the anonymous user.


|  |
| --- |
| **Backlinks** |
| [Auto-register Anonymous User property](https://wiki.genexus.com/commwiki/wiki?19912) | [GAM - Auto-register anonymous users](https://wiki.genexus.com/commwiki/wiki?19395) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |

---
