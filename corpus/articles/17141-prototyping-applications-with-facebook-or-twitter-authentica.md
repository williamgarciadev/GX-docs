---
title: "Prototyping applications with Facebook or Twitter Authentication locally"
source_id: 17141
source_url: https://wiki.genexus.com/commwiki/wiki?17141
genexus_version: "18"
---

# Prototyping applications with Facebook or Twitter Authentication locally

In order to test your application using [GAM Facebook Authentication](https://wiki.genexus.com/commwiki/wiki?29007) ([GAM](https://wiki.genexus.com/commwiki/wiki?14960)) or [Twitter Authentication](https://wiki.genexus.com/commwiki/wiki?17208) you need to host your application in a public URL under port 80. The same happens with Twitter (the Site URL can't´be localhost).

When prototyping, one solution is to [deploy to cloud](https://wiki.genexus.com/commwiki/wiki?15046) using apps2.genexus.com server (where an Apache web server which listens on port 80 is installed).

This is a linux server so Ruby as well as Java applications can be run on this server. In case of Java applications Apache redirects the HTTP requests to Tomcat server.

Another solution is to use a public web server of your own.

If you don´t have a web server public to internet, an alternative is to make some changes in your machine where you prototype. This alternative helps when testing applications locally (web applications using the local web server or smart devices applications using an emulator).

If you need to test an application with iPhone or iPad for instance, or any other device for which you can´t use an emulator, you need to use a public web server anyway.

### [See Also](#See+Also)

[Testing Facebook / Twitter authentication for NET WEB applications](https://wiki.genexus.com/commwiki/wiki?17148)  
[Testing Facebook / Twitter authentication for SD applications using Android Emulator](https://wiki.genexus.com/commwiki/wiki?17191)  
[Testing Facebook / Twitter authentication for Java applications locally](https://wiki.genexus.com/commwiki/wiki?17149,,)  
[Testing Facebook / Twitter authentication for Ruby applications locally](https://wiki.genexus.com/commwiki/wiki?17201,,)


|  |
| --- |
| **Backlinks** |
| [Testing Facebook / Twitter authentication for SD applications using Android Emulator](https://wiki.genexus.com/commwiki/wiki?17191) | [Testing Facebook / Twitter authentication for WEB - NET applications](https://wiki.genexus.com/commwiki/wiki?17148) |

---
