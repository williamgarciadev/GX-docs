---
title: "Facebook external object"
source_id: 38432
source_url: https://wiki.genexus.com/commwiki/wiki?38432
genexus_version: "18"
---

# Facebook external object

The Facebook external object allows you to share content on Facebook and retrieve some user information from its platform.

|  |  |
| --- | --- |
|  |  |

## [Properties](#Properties)

### [AccessToken property](#AccessToken+property)

Allows the developer to get the Access Token associated to an end-user logged-in via Facebook. With this token, the developer is able to get user's data from Facebook by using [Facebook's GraphAPI REST Services](https://developers.facebook.com/docs/graph-api). The information that can be queried depends on the [permissions of the application](https://developers.facebook.com/docs/facebook-login/permissions/) (if the end user accepts them). The access information is given in an SDT called FacebookAccessToken.

Once the end user logins on the GeneXus application using Facebook (e.g. by using [Facebook Button control](https://wiki.genexus.com/commwiki/wiki?31841) or [GAM authentication using Facebook](https://wiki.genexus.com/commwiki/wiki?29007)), the developer can request Graph API services using [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932). See an example on [HowTo: Request data from Facebook using Graph API and Access Token](https://wiki.genexus.com/commwiki/wiki?38437).

## [Methods](#Methods)

### [PostToWall method](#PostToWall+method)

Allows the end user to make a post on its Facebook's wall.

**Warning**: This method is deprecated as of [GeneXus 15 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?36778,,) because the Facebook’s framework has been internal changed (only link and picture paramteres are considered, other are ignored). Use Share methods instead.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | name:[Character(20)](https://wiki.genexus.com/commwiki/wiki?6777), caption:[Character(20)](https://wiki.genexus.com/commwiki/wiki?6777), description:[Character(20)](https://wiki.genexus.com/commwiki/wiki?6777), link:[Character(20)](https://wiki.genexus.com/commwiki/wiki?6777), picture:[Character(20)](https://wiki.genexus.com/commwiki/wiki?6777) |

**Note**: The link and picture parameters are URLs, and you cannot set both at the same time.

### [ShareLink method](#ShareLink+method)

Allows the end user to share any link on Facebook.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | link:[URL](https://wiki.genexus.com/commwiki/wiki?15668) |

### [ShareImage method](#ShareImage+method)

Allows the end user to share an image on Facebook.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | image:[Image](https://wiki.genexus.com/commwiki/wiki?15204) |

### [ShareVideo method](#ShareVideo+method+)

Allows the end user to share any video on Facebook.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | video:[Video](https://wiki.genexus.com/commwiki/wiki?16608) |

## [Events](#Events)

It does not have any.

## [Structured Data Types](#Structured+Data+Types)

### [FacebookAccessToken](#FacebookAccessToken)

* AccessToken:[Character(300)](https://wiki.genexus.com/commwiki/wiki?6777)  
  Facebook's access token.
* ApplicationId:[Character(300)](https://wiki.genexus.com/commwiki/wiki?6777)  
  Application identifier on Facebook developer site.
* UserId:[Character(300)](https://wiki.genexus.com/commwiki/wiki?6777)  
  User identifier on Facebook's system.
* Permissions:Collection([Character(20)](https://wiki.genexus.com/commwiki/wiki?6777))  
  List of Facebook's granted permissions.
* DeclinedPermissions:Collection([Character(20)](https://wiki.genexus.com/commwiki/wiki?6777))  
  List of Facebook's declined permissions.
* ExpirationDate:[DateTime](https://wiki.genexus.com/commwiki/wiki?7370)  
  Date until the access token can be used (then, it must be renewed).
* LastRefreshDate:[DateTime](https://wiki.genexus.com/commwiki/wiki?7370)  
  Last date when the developer renews the access token.

## [Notes](#Notes)

* To be able to post/share content on Facebook, the application must be registered on the [Facebook developer site](https://developers.facebook.com/) and have a Facebook Application created. For detailed information, refer to [HowTo: Register a Facebook App](https://wiki.genexus.com/commwiki/wiki?19399).
* Every link must have the following notation: http://<domain>[:<port>]/<path>.
* The feature can be used without the native application installed on the target device (except for sharing images). In such case, it will be displayed a web view of the Facebook app.
* The end user cannot post images without the Facebook app installed. This problem is avoided if the end user installs the Facebook native application on its device. Check the app on [iTunes](http://itunes.apple.com/gb/app/facebook/id284882215?mt=8) or [PlayStore](https://play.google.com/store/apps/developer?id=Facebook)
* The first time the application tries to post/share content on a user's wall, it will request the user to allow the Facebook Application to post on his wall. If the end user denies the request, the message cannot be posted.

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Platform** | Smart Devices(Android, iOS). |

## [Availability](#Availability)

This external object is available as from [GeneXus X Evolution 3 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?27678,,).

* Share methods are available as of [GeneXus 15 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?36778,,).
* AccessToken property is available as of [Genexus 15 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?38023,,)

## [See also](#See+also)

* [HowTo: Request data from Facebook using Graph API and Access Token](https://wiki.genexus.com/commwiki/wiki?38437)
* [HowTo: Post on Facebook wall with Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?19396)


|  |
| --- |
| **Backlinks** |
| [Client Token property](https://wiki.genexus.com/commwiki/wiki?51723) | [GeneXus Core module](https://wiki.genexus.com/commwiki/wiki?31268) | [GeneXus Core module (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54413) |
| [HowTo: Post on Facebook wall with Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?19396) | [HowTo: Request data from Facebook using Graph API and Access Token](https://wiki.genexus.com/commwiki/wiki?38437) | [Share external object](https://wiki.genexus.com/commwiki/wiki?29800) | [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) |
| [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) |

---
