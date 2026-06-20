---
title: "Static content cache expiration property"
source_id: 18332
source_url: https://wiki.genexus.com/commwiki/wiki?18332
genexus_version: "18"
---

# Static content cache expiration property

Property that allows the caching of static resources of a GeneXus Web application. This allows that when a user enters a GeneXus application, resources are loaded once and will not be reloaded again.

#### [It translates into:](#It+translates+into%3A)

* Significant improvement in performance, especially in cases where objects have multiple resouces (many images, javascript files, css, etc).
* Reducing HTTP traffic.

Static resources are:

* Images (gif, png, bmp, jpg, jpeg, etc).
* Javascript files (js).
* Style Sheets (CSS).

### [Value](#Value)

**Value in hours.**

Default Value = 36 hours

### [Advanced](#Advanced)

For situations where a file (eg gxgral.js, messages.eng.js, gxcfg.js, etc.) has been updated manually and want to force the clients to re-download the resource, you can enter and edit web.config or gxcfg.config value "GX\_BUILD\_NUMBER" by a higher number. With this, the next time you visit a Web page, the browser will force the download of these resources previously cached.

### [Scope](#Scope)

**Languages**

* .NET, IIS 7 or higher.
* JAVA, Servet 2.4 (Tomcat 5.5 or higher).
* Ruby (up to GeneXus X Evolution 3)

**Interfaces**: Web
