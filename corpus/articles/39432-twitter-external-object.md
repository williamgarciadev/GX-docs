---
title: "Twitter external object"
source_id: 39432
source_url: https://wiki.genexus.com/commwiki/wiki?39432
genexus_version: "18"
---

# Twitter external object

It enables you to send tweets from your application.

|  |  |
| --- | --- |
|  |  |

**Warning**: To use this method, setting [Consumer Key and Consumer Secret](https://wiki.genexus.com/commwiki/wiki?35887) is required.  
In the settings option of your Twitter account, for iOS you need to set a Callback URL following this [documentation from Twitter](https://developer.twitter.com/en/docs/basics/developer-portal/guides/callback-urls.html); for Android, you need to set this Callback URL: https://twitter4j, and check the option "Allow this application to be used to Sign in with Twitter"***.***

## [Properties](#Properties)

It does not have any.

## [Methods](#Methods)

### [Tweet method](#Tweet+method)

It allows sending a status update (optionally with an image on the device), showing a dialog which is to be customized by the end user.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | Text:[Character(140)](https://wiki.genexus.com/commwiki/wiki?6777), [ , image:[Image](https://wiki.genexus.com/commwiki/wiki?15204) ] |

### [Follow method](#Follow+method)

It allows following a user using his/her username (without '@' (at)); maximum 15 characters.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | userName:[Character(15)](https://wiki.genexus.com/commwiki/wiki?6777) |

## [Events](#Events)

It does not have any.

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Platforms** | Smart Devices (iOS, Android) |

## [Availability](#Availability)

This external object is available as of [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?20247,,).

## [See also](#See+also)

* [HowTo: Post in Twitter with Smart Devices](https://wiki.genexus.com/commwiki/wiki?31335,,)


|  |
| --- |
| **Backlinks** |
| [GeneXus Core module](https://wiki.genexus.com/commwiki/wiki?31268) | [GeneXus Core module (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54413) | [Share external object](https://wiki.genexus.com/commwiki/wiki?29800) |
| [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) | [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) |

---
