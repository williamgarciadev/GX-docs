---
title: "Google Analytics in Native Mobile Applications (GeneXus 18 Upgrade 2 or prior)"
source_id: 54515
source_url: https://wiki.genexus.com/commwiki/wiki?54515
genexus_version: "18"
---

# Google Analytics in Native Mobile Applications (GeneXus 18 Upgrade 2 or prior)

This article shows you the steps to use Google Analytics in Native Mobile applications.

[Google Analytics](https://wiki.genexus.com/commwiki/wiki?21718,,) is commonly used by marketers and decision makers worldwide to have as much information as possible to improve an application's UX and navigability, or just to focus on part of the application that is not receiving enough attention from users.

`[imagen omitida: wiki id 21719]`

In GeneXus, this service for Native Mobile Applications can be easily enabled.

As a result, developers and decision makers can quickly gain insight into what users do with the app: including which screens are the most used, where the app's users come from, how long they stay on each screen, and many more useful details to take into account when developing new upgrades or solving design issues.  
This is very important in order to optimize the time users spend on the application, as well as to customize ads according to their location, all of which can result in more efficient redirections from the application.

To take full advantage of this service, you can start reading [here](http://www.google.com/analytics/features/mobile.html)

`[imagen omitida: wiki id 21723]`

### [Setting Google Analytics on a Native Mobile Application](#Setting+Google+Analytics+on+a+Native+Mobile+Application)

#### [Step 1:Get Tracking ID](#Step+1%3AGet+Tracking+ID)

[HowTo: Get Google Analytics Tracking Code](https://wiki.genexus.com/commwiki/wiki?37680,,)

#### [Step 2: Enable Analytics on the Native Mobile Application](#Step+2%3A+Enable+Analytics+on+the+Native+Mobile+Application)

Once you have a tracking ID, open the Main Object of your app and set the Enable Analytics Property to True.  
This will enable another property called [Tracker Id](https://wiki.genexus.com/commwiki/wiki?42119) where you should enter the code of the previous step.  
In addition, the [Analytics Dispatch Period property](https://wiki.genexus.com/commwiki/wiki?42128) is available to set the interval (in seconds) between dispatches of collected Google Analytics data. Use 0 for immediate dispatch.

`[imagen omitida: wiki id 21722]`

**Important Note**: The tracking ID can be shared by many versions of an application, or even shared among different applications.

These settings will allow the account owner to see usage statistics of the applications that share the same tracking ID.

**Note**: As of [GeneXus 16 upgrade 2](https://wiki.genexus.com/commwiki/wiki?41525,,) to use Google Analytics, you need to set the property [Analytics Provider](https://wiki.genexus.com/commwiki/wiki?41575) = Google Analytics.
