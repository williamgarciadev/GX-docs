---
title: "Interop.Open method"
source_id: 23733
source_url: https://wiki.genexus.com/commwiki/wiki?23733
genexus_version: "18"
---

# Interop.Open method

Open a given URL, using the appropriate application installed on the device.

### [Syntax](#Syntax)

```
Interop.Open(<URL>)
```

The *<URL>* parameter is the URL that will be opened.

**Type returned**  
None

### [Examples](#Examples)

#### [Open a tweet URL directly from Twitter app](#Open+a+tweet+URL+directly+from+Twitter+app)

```
Event 'OpenTweetGenexus'
Composite
  &AppInstalled = Interop.CanOpen("twitter://user?screen_name=GeneXus")
  if &AppInstalled
   Interop.Open("twitter://user?screen_name=GeneXus")
  endif
EndComposite
EndEvent
```

The URL "twitter://user?screen\_name=GeneXus" will be opened in the Twitter app.

#### [Open another app from our own, or ask to install it](#Open+another+app+from+our+own%2C+or+ask+to+install+it)

```
Event 'OpenAnotherApp'
Composite
  &AppId = 'com.genexus.genexusmeeting'
  &AppUrl = 'market://details?id='+&AppId.trim()
   Interop.Open(&AppUrl)
EndComposite
EndEvent
```

In this example, we want to call another application from our App. In this case, we are calling this app: <https://play.google.com/store/apps/details?id=com.genexus.genexusmeeting>. When we execute this, the Google Play will open with the option to either install this app or open it, if it´s already installed.

#### [Make a phone call](#Make+a+phone+call)

```
Event &phone.Tap
    composite
        ....
        Interop.Open('tel:' + &phone)
    endcomposite
EndEvent
```

In this case, when the user taps on the &Phone variable, we want to do something else before dialing to that number. By this way, we are overlapping the [Phone domain](https://wiki.genexus.com/commwiki/wiki?14639) default behavior.

### [Availability](#Availability)

As from [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?20247,,)

### [Scope](#Scope)

|  |  |
| --- | --- |
| Objects: | [Objects for Native Mobile applications development](https://wiki.genexus.com/commwiki/wiki?20087) only in user events |
| Platforms: | Android and iOS |

### [See also](#See+also)

* [Interop external object](https://wiki.genexus.com/commwiki/wiki?23734)
* [Interop.CanOpen method](https://wiki.genexus.com/commwiki/wiki?23732)
* <http://tips.genexus.com/2014/01/como-enviar-mensajes-de-whatsapp-traves.html>

### [Sample](#Sample)

* [EventDay](https://wiki.genexus.com/commwiki/wiki?22550,,)


|  |
| --- |
| **Backlinks** |
| [Interop external object](https://wiki.genexus.com/commwiki/wiki?23734) | [Interop external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55183) | [Interop.CanOpen method](https://wiki.genexus.com/commwiki/wiki?23732) |

---
