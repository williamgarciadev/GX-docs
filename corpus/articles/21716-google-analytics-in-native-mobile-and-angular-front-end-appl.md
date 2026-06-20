---
title: "Google Analytics in Native Mobile and Angular front end Applications"
source_id: 21716
source_url: https://wiki.genexus.com/commwiki/wiki?21716
genexus_version: "18"
---

# Google Analytics in Native Mobile and Angular front end Applications

This article shows you the steps to use Google Analytics in [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917) and [Angular](https://wiki.genexus.com/commwiki/wiki?42550) front end Applications.

[Google Analytics](https://wiki.genexus.com/commwiki/wiki?21718,,) is commonly used by marketers and decision makers worldwide to have as much information as possible to improve an application's UX and navigability, or just to focus on part of the application that is not receiving enough attention from users.

`[imagen omitida: wiki id 21719]`

In GeneXus, this service can be easily enabled.

As a result, you and decision makers can quickly gain insight into what end-users do with the app: including which screens are the most used, where the app's users come from, how long they stay on each screen, and many more useful details to take into account when developing new upgrades or solving design issues.  
  
This is very important in order to optimize the time end-users spend on the application, as well as to customize ads according to their location, all of which can result in more efficient redirections from the application.

To take full advantage of this service, you can start reading [Google Marketing Platform](http://www.google.com/analytics/features/mobile.html)

`[imagen omitida: wiki id 21723]`

### [Setting Google Analytics](#Setting+Google+Analytics)

#### [Step 1:Get Tracking ID](#Step+1%3AGet+Tracking+ID)

[HowTo: Get Google Analytics Tracking Code](https://wiki.genexus.com/commwiki/wiki?37680,,)

#### [Step 2: Enable Analytics](#Step+2%3A+Enable+Analytics)

Once you have a tracking ID, open the Main Object (for example [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) or [Work With](https://wiki.genexus.com/commwiki/wiki?15974)) in your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) and set the [Analytics Provider property](https://wiki.genexus.com/commwiki/wiki?41575) to Google. This will enable another property called [Tracker Id](https://wiki.genexus.com/commwiki/wiki?42119) where you must enter the code of the previous step.

In addition, the [Analytics Dispatch Period property](https://wiki.genexus.com/commwiki/wiki?42128) is available to set the interval (in seconds) between dispatches of collected Google Analytics data. Use 0 for immediate dispatch.

**Note**: The tracking ID can be shared by many versions of an application, or even shared among different applications.

These settings will allow the account owner to see usage statistics of the applications that share the same tracking ID.

### [See Also](#See+Also)

[Install Google Tag Manager Support property](https://wiki.genexus.com/commwiki/wiki?54266)


|  |
| --- |
| **Backlinks** |
| [Analytics external object](https://wiki.genexus.com/commwiki/wiki?31415) | [Analytics external object (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54509) | [Analytics external object (GeneXus 18 Upgrade 7 or prior)](https://wiki.genexus.com/commwiki/wiki?57371) |
| [Analytics Provider property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54454) | [Google Analytics in Native Mobile Applications (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54515) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |

---
