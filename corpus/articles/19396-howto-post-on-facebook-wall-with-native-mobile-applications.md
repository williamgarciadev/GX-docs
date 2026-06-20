---
title: "HowTo: Post on Facebook wall with Native Mobile Applications"
source_id: 19396
source_url: https://wiki.genexus.com/commwiki/wiki?19396
genexus_version: "18"
---

# HowTo: Post on Facebook wall with Native Mobile Applications

This article shows you the steps to post on Facebook with Native Mobile Applications.

Social interaction is very important for Native Mobile Applications. With GeneXus there are many ways to communicate and send messages from your application: Email, SMS, Twitter and in GeneXus Evolution 2 Upgrade 1, there is a new feature to interact with Facebook.

Before starting this tutorial, step 1 should be completed. The rest of this document will assume that it has been done, that the Facebook App ID is known, and that your Application bundle identifier has been set in your Facebook Application.

### [Step 1: External Object](#Step+1%3A+External+Object)

To add this feature to a Native Mobile Application in GeneXus, first read [Facebook external object](https://wiki.genexus.com/commwiki/wiki?38432) article, especially its considerations and limitations.

### [Step 2: Code Example](#Step+2%3A+Code+Example)

On a User Event call the External Object to post:

```
Event 'ShareLink'
    Facebook.ShareLink("http://www.genexus.com")
Endevent
```

### [Step 3: Execution](#Step+3%3A+Execution)

When the end user executes the action 'ShareLink', a pop-up window of Facebook will be displayed with a preview of the post and the possibility to add a comment on it.

#### [Limitations](#Limitations)

* As of July 17, 2017, Facebook's Graph API only considers the link or image parameters; the others are ignored.

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Objects:** | [Work With pattern and Work With object](https://wiki.genexus.com/commwiki/wiki?15974), [Panel object](https://wiki.genexus.com/commwiki/wiki?24829). |
| **Generators:** | [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917) |

### [Availability](#Availability)

PostToWall method is no longer available since [GeneXus 15 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?36778,,). For more information, read here: [Facebook external object](https://wiki.genexus.com/commwiki/wiki?38432)


|  |
| --- |
| **Backlinks** |
| [Facebook external object](https://wiki.genexus.com/commwiki/wiki?38432) |
|

---
