---
title: "GAM - Web Backoffice"
source_id: 15935
source_url: https://wiki.genexus.com/commwiki/wiki?15935
genexus_version: "18"
---

# GAM - Web Backoffice

The [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) Backoffice is a web application that allows [GAM administrators](https://wiki.genexus.com/commwiki/wiki?15215) to manage [Repositories](https://wiki.genexus.com/commwiki/wiki?17568), [Users](https://wiki.genexus.com/commwiki/wiki?22082) [Roles](https://wiki.genexus.com/commwiki/wiki?17569), [Security Policies](https://wiki.genexus.com/commwiki/wiki?18521), etc.

### [What is the GAM Backoffice?](#What+is+the+GAM+Backoffice%3F)

The GAM Backoffice is a web application that allows you to manage Users, Roles, Security Policies, Applications, and Repository configurations related to GAM.

### [How to enable the GAM Backoffice](#How+to+enable+the+GAM+Backoffice)

To be able to work with the GAM Backoffice, you have to [activate GAM](https://wiki.genexus.com/commwiki/wiki?19946) in your Knowledge Base. Then, GeneXus will offer to automatically import the objects required to work with the GAM Backoffice.

### [How to access the GAM Backoffice](#How+to+access+the+GAM+Backoffice)

You can access the GAM Backoffice in the following ways:

* Launchpad: After pressing F5, an option to open the GAM Backoffice will appear in the Launchpad.
* GeneXus menu: Go to **Build > Run GAM Backoffice** to open the GAM Backoffice.

Once logged in, the Dashboard appears first, showing user summary statistics.

`[imagen omitida: wiki id 60975]`

On the left, you'll find the GAM Backoffice menu.

In the top-right corner, you can access the Administrator User option:

`[imagen omitida: wiki id 60976]`

### [Administrator User option](#Administrator+User+option)

The Administrator User dropdown allows the user to manage the account. It displays three options:

`[imagen omitida: wiki id 60977]`

* **My account:** You can access the account settings and details. From here you can update your name, username and advanced information such as birthday, gender, phone, and language.
* **Change Password:** You can update the account password.
* **Logout:** Sign out of the current session.

### [GAM Backoffice binaries](#GAM+Backoffice+binaries)

GeneXus includes a .zip file with the binaries that are unzipped at build time.

* [.NET](https://wiki.genexus.com/commwiki/wiki?38604): The file is unzipped in the web directory.
* [Java](https://wiki.genexus.com/commwiki/wiki?12258): The file is unzipped in a folder called GAM\_Backend, which is included in the web directory and will be copied to the servlets server afterwards.

To have the binaries working, you need to build the application, as they do not access the database. They call the APIs generated and compiled in the KB, and use the configuration files of the KB to access the GAM database.

The URL access points of the GAM Backoffice are the following:

* NET: http://<server>/<baseURL>/gam\_dashboard.aspx
* JAVA: http://<server>/<baseURL>/servlet/genexus.security.backend.gam\_dashboard

### [GAM Backoffice sources](#GAM+Backoffice+sources)

Apart from the compiled GAM Backoffice, the GeneXus objects can be imported into the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) by importing the GAM\_Web-Administration.xpz located in <GeneXus Installation>\Library\GAM.

These objects serve as [examples](https://wiki.genexus.com/commwiki/wiki?21993) of how to use of the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535).

They can be changed as needed if some requirements are not met (the GAM API is available for that purpose).

**Note**: The GeneXus objects of the .xpz file have different names from those of the compiled binaries.

* The name of the XPZ objects is gamexampleww<Entity> (for example: gamexamplewwusers).
* The name of the compiled objects is gam\_ww<Entity> (for example: gam\_wwusers).

In both cases (compiled and GAM examples), the first screen that may be displayed at runtime is the [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) login, to enter the administrator credentials.

### [Compatibility](#Compatibility)

The GAM Backoffice distributed as binaries is available since [GeneXus 16 upgrade 8](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?44913,,).

* If you open the KB with that version, and the Backoffice had already been imported, the GAMExampleWWUsers object or any other object of the Backoffice must be set as Main Object to be generated. A change has been made in the GAMHome object which doesn't reference the example objects. That's why, if you need to continue using the GAMExample objects which are in the KB, any of them must be set to Main to be generated and built when they are changed (the others are all in the call tree).
* However, when the new .xpz file is imported (which contains the examples), that object is already modified and set as Main.

For more information, see [SAC #46892](https://www.genexus.com/developers/websac?en,,,46892).

### [Distribution](#Distribution)

To deploy the GAM Backoffice distributed binaries, check the [Include GAM Backoffice property](https://wiki.genexus.com/commwiki/wiki?44996) in the deployment unit Target options of the [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092).

### [See Also](#See+Also)

[GAM - Examples - First login on a Web application](https://wiki.genexus.com/commwiki/wiki?45644)  
[Restricted access to GAM Backoffice](https://wiki.genexus.com/commwiki/wiki?18495)


|  |
| --- |
| **Pages** |
| [GAM - Authentication Types](https://wiki.genexus.com/commwiki/wiki?16508) | [GAM - Custom Authentication Type](https://wiki.genexus.com/commwiki/wiki?21751) | [GAM - External Authentication: version 1.0](https://wiki.genexus.com/commwiki/wiki?21548) |
| [GAM - External Web Services Authentication Type](https://wiki.genexus.com/commwiki/wiki?16512) | [GAM - Permissions](https://wiki.genexus.com/commwiki/wiki?15912) | [GAM - Repository](https://wiki.genexus.com/commwiki/wiki?17568) |
| [GAM - Repository Connections](https://wiki.genexus.com/commwiki/wiki?16150) | [GAM - Roles](https://wiki.genexus.com/commwiki/wiki?17569) | [GAM - Security Policies](https://wiki.genexus.com/commwiki/wiki?18521) |
| [GAM - Security Policies (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58087) | [GAM - Twitter Authentication Type](https://wiki.genexus.com/commwiki/wiki?17208) | [GAM - WeChat Authentication type](https://wiki.genexus.com/commwiki/wiki?45037) |
| [GAMExampleLogin object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?39427,GAMExampleLogin+object,) |

---
