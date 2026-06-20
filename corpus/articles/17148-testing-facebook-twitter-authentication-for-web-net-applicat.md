---
title: "Testing Facebook / Twitter authentication for WEB - NET applications"
source_id: 17148
source_url: https://wiki.genexus.com/commwiki/wiki?17148
genexus_version: "18"
---

# Testing Facebook / Twitter authentication for WEB - NET applications

How to test [Facebook Authentication Type](https://wiki.genexus.com/commwiki/wiki?16516,,)/ [GAM - Twitter Authentication Type](https://wiki.genexus.com/commwiki/wiki?17208) for NET WEB applications, taking into account the considerations explained in [Prototyping applications with Facebook or Twitter Authentication](https://wiki.genexus.com/commwiki/wiki?17141).

In order to test Facebook or Twitter authentication, the URL of the application should not be "localhost" and shouldn´t have reference to the port (for example, <http://localhost:8080> is not a valid URL, neither <http://localhost>, nor <http://server:8080>).

### [I. Recommendation: Use the cloud for prototyping : apps3.genexusx.com](#I.+Recommendation%3A+Use+the+cloud+for+prototyping+%3A+apps3.genexusx.com)

### [II. If you want to test locally](#II.+If+you+want+to+test+locally)

You need to make some changes in hosts file of the PC.

1. Edit hosts file (C:\Windows\System32\drivers\etc)

Add the following line:

127.0.0.1       gamtestnet.com

2. Define facebook application in Facebook site (<http://developers.facebook.com/>):

`[imagen omitida: wiki id 17150]`

###### [Figure 1.](#Figure+1.)

When a user logs in the GeneXus application using Facebook (clicks on the Facebook button of the GAMExampleLogin web object), GAM redirects to Facebook site where the user has to enter his credentials. After this step, Facebook redirects to a URL where GAM does some checks and redirects again to the application.

The site URL specified in the definition of the Facebook application (in Facebook web site, figure 1) is the base URL where Facebook will return after the user has logged in (GAM application is going to be found at this location). Facebook determines that this URL has to be the same as the base URL of the application which made the call to Facebook.

So, note that the site URL (Figure 1) is the same es the web root defined in GeneXus model (Figure 2):

`[imagen omitida: wiki id 17154]`

###### [Figure 2.](#Figure+2.)

3. Define facebook application in GAM Backend as the following (after you have obtained the Client Id and Client Secret provided by Facebook in the previous step):

`[imagen omitida: wiki id 17151]`

###### [Figure 3](#Figure+3)

Note that here you need to specify the complete URL including the web application name.

### [See Also](#See+Also)

[Testing Facebook / Twitter authentication for SD applications using Android Emulator](https://wiki.genexus.com/commwiki/wiki?17191)  
[Testing Facebook / Twitter authentication for Java applications locally](https://wiki.genexus.com/commwiki/wiki?17149,,)  
[Testing Facebook / Twitter authentication for Ruby applications locally](https://wiki.genexus.com/commwiki/wiki?17201,,)


|  |
| --- |
| **Backlinks** |
| [Prototyping applications with Facebook or Twitter Authentication locally](https://wiki.genexus.com/commwiki/wiki?17141) | [Testing Facebook / Twitter authentication for SD applications using Android Emulator](https://wiki.genexus.com/commwiki/wiki?17191) |

---
