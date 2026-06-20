---
title: "Progressive Web Applications in GeneXus"
source_id: 42600
source_url: https://wiki.genexus.com/commwiki/wiki?42600
genexus_version: "18"
---

# Progressive Web Applications in GeneXus

[Progressive web apps](https://developers.google.com/web/progressive-web-apps/) are a hybrid of regular web pages (or websites) and a mobile application. They combine the flexibility of the web with the experience of a native application.

Their main aim is reaching more clients by giving them a deeply engaging user experience when they land in the web site.

In fact, PWAs allow getting a native-like experience from the web.

### [Features of a PWA](#Features+of+a+PWA)

Progressive Web Apps are installable and live on the user's home screen, without the need for an app store.  
  
The main feature of Progressive Web Apps are:

#### [Reliable](#Reliable)

* Load instantly and never show the "downasaur" (meaning unable to connect to the internet), even in uncertain network conditions.  
  When launched from the user’s home screen, [service workers](https://developers.google.com/web/fundamentals/primers/service-workers/) enable a Progressive Web App to load instantly, regardless of the network state.

#### [Fast](#Fast)

* Respond quickly to user interactions with silky smooth animations and no janky scrolling.

#### [Engaging](#Engaging)

* Feel like a natural app on the device, with immersive user experience.  
  For this feature, PWAs have a [web app manifest](https://developers.google.com/web/fundamentals/web-app-manifest/) file which tells the browser about the web application and how it should behave when 'installed' on the user's mobile device or desktop. Having a manifest is required by Chrome to show the [Add to Home Screen prompt](https://developers.google.com/web/fundamentals/app-install-banners/).

### [Example](#Example)

The following is a PWA application. Note that you have the option to install the application locally.

`[imagen omitida: wiki id 42642]`

After having installed it, the application can be accessed directly from the Application Chrome menu (and a shortcut is created):

`[imagen omitida: wiki id 42645]`

It will be launched as follows (without a navigation bar):

`[imagen omitida: wiki id 42644]`

### [Temporary Limitations](#Temporary+Limitations)

* Only one main per KB can be Progressive (this limitation is only for web, not for Angular)
* Only relative paths supported in [Static content base URL property](https://wiki.genexus.com/commwiki/wiki?9010)

### [Availability](#Availability)

This feature is available since [GeneXus 16 upgrade 5](https://wiki.genexus.com/commwiki/wiki?43446,,).


* [How to create a PWA using GeneXus](https://wiki.genexus.com/commwiki/wiki?42601)
* Properties
  + Solution with Panels, Menus, WorkWith (Angular)
    - [Build Mode property](https://wiki.genexus.com/commwiki/wiki?49860)
    - [Web Frontend Application property](https://wiki.genexus.com/commwiki/wiki?54265)
    - [Web Frontend Application Name property](https://wiki.genexus.com/commwiki/wiki?54258)
    - [Web Frontend Application Short Name property](https://wiki.genexus.com/commwiki/wiki?54259)
    - [Web Frontend Application Description property](https://wiki.genexus.com/commwiki/wiki?54260)
    - [Web Frontend Display Mode property](https://wiki.genexus.com/commwiki/wiki?54261)
    - [Web Frontend Background Color property](https://wiki.genexus.com/commwiki/wiki?54262)
    - [Web Frontend Theme Color property](https://wiki.genexus.com/commwiki/wiki?54263)
    - [Web Frontend Application Icon property](https://wiki.genexus.com/commwiki/wiki?54264)
  + Solution with Web Panels, Web objects (.NET, Java)
    - [Web Application property](https://wiki.genexus.com/commwiki/wiki?42602)
    - [Web Application Name property](https://wiki.genexus.com/commwiki/wiki?42603)
    - [Web Application Short Name property](https://wiki.genexus.com/commwiki/wiki?42604)
    - [Web Application Description property](https://wiki.genexus.com/commwiki/wiki?42605)
    - [Primary Text Direction property](https://wiki.genexus.com/commwiki/wiki?42607)
    - [Display property](https://wiki.genexus.com/commwiki/wiki?42608)
    - [Background Color property](https://wiki.genexus.com/commwiki/wiki?42609)
    - [Theme Color property](https://wiki.genexus.com/commwiki/wiki?42610)
    - [Prefer Related Applications property](https://wiki.genexus.com/commwiki/wiki?42611)
    - [Web Application Icon property](https://wiki.genexus.com/commwiki/wiki?42612)
    - [Android Alternative App property](https://wiki.genexus.com/commwiki/wiki?42613)
    - [Android Alternative App Identifier property](https://wiki.genexus.com/commwiki/wiki?43798)
    - [iOS Alternative App property](https://wiki.genexus.com/commwiki/wiki?42614)
    - [Offline Object property](https://wiki.genexus.com/commwiki/wiki?42615)
* [Using LightHouse to validate your PWA](https://wiki.genexus.com/commwiki/wiki?42665)

###

---
