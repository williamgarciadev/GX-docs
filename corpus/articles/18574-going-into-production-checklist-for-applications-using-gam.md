---
title: "Going into production: checklist for Applications using GAM"
source_id: 18574
source_url: https://wiki.genexus.com/commwiki/wiki?18574
genexus_version: "18"
---

# Going into production: checklist for Applications using GAM

This checklist shows the tasks you need to perform after testing an application that uses [GAM](https://wiki.genexus.com/commwiki/wiki?14960), in order to put the application into production.

The idea is to mitigate risks that compromise the security of the application.

Pursuing the purpose of protecting the privacy of the company and keeping the information secure, the decision on how to configure the following items depends on the severity and characteristics of the application.

* Set up HTTPS protocol in the Application Server.

This is essential in case of SD Applications. In case of WEB Applications it is essential to have HTTPS at least in all objects where passwords are entered, like the login and registration Panels.

* Change [Administrator](https://wiki.genexus.com/commwiki/wiki?15215) Password.

The password of administrator users of GAM repository has to be changed using [GAM Backend](https://wiki.genexus.com/commwiki/wiki?15935).

* Change "Gamadmin" user password.

This is the password of the [administrator of the Repositories](https://wiki.genexus.com/commwiki/wiki?18617).

* Delete all users defined for testing purposes.
* Create new [Repository Connections](https://wiki.genexus.com/commwiki/wiki?16150).

By default, the GAM [Connection User](https://wiki.genexus.com/commwiki/wiki?15217) is <version\_name>, the connection user password needs to be changed when the application is going into production.

* In production time, when the application is deployed, the gxmetadata directory (with all its contents) should not be deployed for security.  
  That means that the "gxmetadata" directory should be deleted from the deployment (except the files <main\_object>.<plataform>.json and the gxversion.json file). The appid.json file is necessary to be kept if dynamic services URL are used.

The web server should not serve the connection.gam file.

* The [GAM Backend](https://wiki.genexus.com/commwiki/wiki?15935) should be private, so as only Administrator users can execute these [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916).

The Web Panels of the Web Backoffice have the code to keep this privacy (see: [Access restricted to GAM Backend](https://wiki.genexus.com/commwiki/wiki?18495)).

If you don't use the [GAM backend binaries](https://wiki.genexus.com/commwiki/wiki?15935) distributed binaries to take into production, but compile the [GAM - Examples](https://wiki.genexus.com/commwiki/wiki?21993), consider that the Web Panels "GAMExampleRecoverPasswordStep1" and "GAMExampleRecoverPasswordStep2" have to be edited and changed as suggested in [GAM: A way to solve Forgot Password](https://wiki.genexus.com/commwiki/wiki?16923), they should not be left as they are distributed (they are examples consolidated in GAM\_Examples folder).

The same happens with the GAMExampleRegisterUser, GAMExampleUpdateRegisterUser and the GAMExampleChangePassword Panels.

* Regarding the [Native Mobile architecture](https://wiki.genexus.com/commwiki/wiki?16052),

Actions programmed by GeneXus users are translated into [REST Web Services](https://wiki.genexus.com/commwiki/wiki?14573) calls in general. So REST services need to be protected as well as SD objects. Make a search in the KB by "Rest Protocol= True", so you can easily find all the REST services and check the [Permissions](https://wiki.genexus.com/commwiki/wiki?15912) configuration for each of them.

Depending on the security needed:

* Do not use [Client Side Caching](https://wiki.genexus.com/commwiki/wiki?17403,,) in SD applications.
* Configure the following in the [Repository](https://wiki.genexus.com/commwiki/wiki?18463,,):
  + [UserRememberMeType property](https://wiki.genexus.com/commwiki/wiki?18584) (None, Login, Authentication, Both). The most secure value is "None".
  + [User Remember Me Timeout](https://wiki.genexus.com/commwiki/wiki?18586) (days)
  + [User Recovery Password Key Timeout](https://wiki.genexus.com/commwiki/wiki?18590) (minutes)
  + Minimum Amount Of Characters In Login
  + [Login Attempts To Lock User](https://wiki.genexus.com/commwiki/wiki?18592)
  + [Login attempts to lock session Repository property](https://wiki.genexus.com/commwiki/wiki?18593)
  + [GAM Unblock User Timeout property](https://wiki.genexus.com/commwiki/wiki?18926)
  + [Give WEB Anonymous Session](https://wiki.genexus.com/commwiki/wiki?16414)
  + [User Session Cache Timeout (seconds)](https://wiki.genexus.com/commwiki/wiki?18582). It's advisable to be set with a value less or equal to 30 seconds.
  + [Session Expires On IP Change property](https://wiki.genexus.com/commwiki/wiki?18925)
  + [User Activation Method Repository property](https://wiki.genexus.com/commwiki/wiki?18932). It's not advisable to set to "Automatic" value.
  + [User Automatic Activate TimeOut property](https://wiki.genexus.com/commwiki/wiki?18934)
  + Check the [Default Security Policy](https://wiki.genexus.com/commwiki/wiki?18521) of GAM Repository, and the [Repository Default Role](https://wiki.genexus.com/commwiki/wiki?17569).
  + [Cache Timeout (minutes) Repository Property](https://wiki.genexus.com/commwiki/wiki?21863).
* Configure the following in all the [Security Policies](https://wiki.genexus.com/commwiki/wiki?18521) defined in the Repository:
  + [Web Session timeout (minutes)](https://wiki.genexus.com/commwiki/wiki?16338)
  + [Allow Multiple Concurrent Web Sessions Security Policy Property](https://wiki.genexus.com/commwiki/wiki?18939). The most secure value is "No".
  + [OAuth token expire (minutes)](https://wiki.genexus.com/commwiki/wiki?18577)
  + [OAuth token maximum renovations](https://wiki.genexus.com/commwiki/wiki?19324)
  + Period change password (days)
  + [Minimum Time to Change Passwords Security Policy](https://wiki.genexus.com/commwiki/wiki?18942)
  + Minimum Length Of The Password
  + Minimum Numeric Characters Password
  + Minimum Upper Case Characters Password
  + Minimum Special Characters Password
  + [Maximum Password History Entries](https://wiki.genexus.com/commwiki/wiki?18579)

* In case of SD Applications, take into consideration setting [Single User Access](https://wiki.genexus.com/commwiki/wiki?17242) property.

### [See Also](#See+Also)

[Security recommendations for Smart Devices Applications](https://wiki.genexus.com/commwiki/wiki?20744,,)  
[OWASP Top 10 Security Risks](https://owasp.org/Top10/)  
[OWASP 2013 Top 10 in GeneXus Applications](https://wiki.genexus.com/commwiki/wiki?21889,,)  
[GAM - Applications deployment](https://wiki.genexus.com/commwiki/wiki?21219)  
[GAM - Deploy Tool](https://wiki.genexus.com/commwiki/wiki?18608)


|  |
| --- |
| **Backlinks** |
| [A07:2021 - Identification and authentication failures](https://wiki.genexus.com/commwiki/wiki?50187) | [GAM - Applications deployment](https://wiki.genexus.com/commwiki/wiki?21219) | [Toc:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |
| [Hardening of GeneXus Systems and Deployments with GAM](https://wiki.genexus.com/commwiki/wiki?47237) | [Secure Native Mobile applications architecture](https://wiki.genexus.com/commwiki/wiki?16052) |

---
