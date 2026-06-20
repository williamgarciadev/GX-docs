---
title: "GXflow license scheme"
source_id: 37204
source_url: https://wiki.genexus.com/commwiki/wiki?37204
genexus_version: "18"
---

# GXflow license scheme

The [GXflow](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?4179,,) licensing scheme is very versatile, it adapts to the requirements of different companies and the production lifecycle of your inbox driven applications.

This document contains two sections. The first details the license types you may use and where to store them depending on your needs. The second is specific for users that are updating systems to [GeneXus 15 Upgrade 8](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?36778,,) or higher.

Note that you don't require GXflow licenses for [running](https://wiki.genexus.com/commwiki/wiki?5692) a [Business Process Diagram object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?16486,,) in [Prototyper Mode](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?13607,,) while you don't need to log in with different Users and Roles. So if you're just doing your first steps with GXflow you may skip this document.

## [GXflow license types and license protection methods](#GXflow+license+types+and+license+protection+methods)

### [License types (Products)](#License+types+%28Products%29)

Depending on your plan, the licenses can be for two different products or types.

#### [*GXflow*](#GXflow)

This product or plan handles nominated licenses used by GXflow.

A nominated license is associated with a specific user, and only that user can use the license.

#### [*GXflow Corporate*](#GXflow+Corporate)

This product or plan handles corporate licenses, which are not nominated.

A corporate license allows using GXflow in your applications without user restrictions. Any user who enters the application will be authorized when this license is used.

Example of how these products or types are shown in the license manager:

`[imagen omitida: wiki id 52022]`

Please contact your distributor or Sales representative for more details regarding the plans or how your plan relates to these products or types.

### [License Protection methods (Native or Protection Server)](#License+Protection+methods+%28Native+or+Protection+Server%29)

Licenses can be handled with two different methods or mechanisms, each storing licenses in different locations, depending on your needs. Two options are available: Native (default) and Protection Server.

#### [Native](#Native)

The licenses are stored in the database, specifically one of the GXflow engine.

#### [Protection Server](#Protection+Server)

The licenses are stored using specific functions of the operating system, via [GeneXus Protection](https://wiki.genexus.com/commwiki/wiki?7353) (9.7.2.14 or higher).

#### [Recommendations](#Recommendations)

The Native protection method is recommended when the application is installed on a Platform as a Service environment ([PaaS](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?32096,,)) or on an environment that needs horizontal scalability; more than that, in most of those cases it is the only one that is suitable for those scenarios. Because of infrastructure and networking issues, this is also the one that is easier to install and set up, especially in non-Windows servers (Linux, AIX, iSeries, etc).

The Protection Server protection method is recommended for development and testing stages, where licenses are shared for different prototypes and databases are temporary. This method requires registering some COM Dlls which is not possible to do in PaaS servers.

So, generally speaking, Native is recommended for production environments while Protection Server is more appropriate for prototyping.

If a load balancer is being used, the following should be taken into account:

1. Licenses installed on one node will not automatically appear on the other nodes.
2. Actions performed on users (nominate or innominate) will also not be reflected on the other nodes.
3. The application server must be restarted for the changes to take effect. If not restarted, the changes may take up to 30 minutes to be applied.
4. When installing licenses, it is recommended to shut down all nodes except the one where the licenses are being installed, and start them again once the licenses have been successfully installed.

Note for developers: The license protection method is, once selected, stored in the database; so take into account that you have to set it again after operations that delete the selection (eg.: 'Create workflow tables')

### [Requesting, installing, updating Licenses and license information; nominating Users](#Requesting%2C+installing%2C+updating+Licenses+and+license+information%3B+nominating+Users)

All operations around native licenses are handled using the [GXflow License Manager](https://wiki.genexus.com/commwiki/wiki?37207).

To use [Protection Server](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?18887,,) licenses, you must change the license protection setting in the GXflow License Manager. Read [GXflow centralized licenses configuration (GXflow on Windows)](https://wiki.genexus.com/commwiki/wiki?21761) for more information. Then, almost all operations around Protection Server licenses can be handled using the [GXflow License Manager](https://wiki.genexus.com/commwiki/wiki?37207) too.

It is possible to change the method you are using by uninstalling your current licenses and requesting them again with the other method.

## [Updating from GeneXus 15 Upgrade 7 or lower (to GeneXus 15 Upgrade 8 or higher)](#Updating+from+GeneXus+15+Upgrade+7+or+lower+%28to+GeneXus+15+Upgrade+8+or+higher%29)

GeneXus 15 Upgrade 8 features scalability, stability and usability improvements related to GXflow, specifically to GXflow license management. Licenses can now be stored in the database to improve scalability and ability to run in Platform as a Service ([PaaS](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?32096,,)) environments and a new license manager has been introduced to easily handle the licenses no matter on what environment, operating system or DBMS you are running.

The following steps will help you to update your licenses.

1. Read the section above "GXflow license types and license protection methods" carefully.
2. Save (export) the Users before uninstalling, so you don't need to type them in again later.
3. Uninstall your GXflow Client licenses
4. Enter the [GXflow License Manager](https://wiki.genexus.com/commwiki/wiki?37207) of your GXflow installations and choose the license protection method that fits your needs.
5. Ask for Licenses
   * If you own a GXflow Corporate license plan, you must ask now for
     + GXflow Corporate licenses (Read the section above "GXflow license types and license protection methods").
     + Gxflow licenses (Required only for systems developed with GeneXus 15 Upgrade 7 or previous.)
6. Import Users

### [New License Manager](#New+License+Manager)

To handle this new license scheme (native method), a new web-based license manager is used, where you can execute all the actions needed to manage GXflow licenses (Request, Install, Uninstall, Change, etc.)

`[imagen omitida: wiki id 52023]`

This new license manager is installed as part of the GXflow Client.

`[imagen omitida: wiki id 52024]`

It is also possible to access the license manager without entering the GXflow Client by adding the following to the end of the URL:

#### [Java: com.gxflow.wflicensemanager](#Java%3A+com.gxflow.wflicensemanager)

.NET Frameowork or .NET: wflicensemanager.aspx

Check [this document](https://wiki.genexus.com/commwiki/wiki?37207) for detailed information on how to work in this new license manager.

### [Compatibility](#Compatibility)

In Linux, [storing licenses in the local file system](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?15724,,) is discontinued. Refer to the section "License Protection methods (Native or Protection Server)" for the new options available.

### [FAQ](#FAQ)

#### [What happens if a nominated user stops being part of the processes?](#What+happens+if+a+nominated+user+stops+being+part+of+the+processes%3F)

You can disable him from participating in the processes, this releases a license for a new user if you are using the nominated plan. The previous user is maintained in order to ensure the record integrity.

#### [Is it possible to share the license with more than one system?](#Is+it+possible+to+share+the+license+with+more+than+one+system%3F)

Yes, it is, but these systems must access the same license server and all systems cannot have more users nominated than the amount corresponding to the license package purchased.

#### [Why, using the GXflow Login panel, do I cannot log in with the WADMINISTRATOR user to the GXflow standard client?](#Why%2C+using+the+GXflow+Login+panel%2C+do+I+cannot+log+in+with+the+WADMINISTRATOR+user+to+the+GXflow+standard+client%3F)

As of [GeneXus 15 Upgrade 8](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?36778,,), if you do not have GXflow licenses, you cannot log in to GXflow Standard Client using the WFADMINISTRATOR user (neither with any other user) using GXflow's login panel. When you [run](https://wiki.genexus.com/commwiki/wiki?5692) a [Business Process Diagram object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?16486,,) with [Execution mode property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?13607,,) set to "Standard Client", that action opens the GXflow Standard client, so in that case, you need to install at least one license to be able to log in.

Logging in to the GXflow Standard Client with WFADMINISTRATOR (or any other user) in prototyping scenarios can be useful when you want to log in using different roles.

Note: You don't require GXflow licenses for [running](https://wiki.genexus.com/commwiki/wiki?5692) a [Business Process Diagram object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?16486,,) in [Prototyper Mode](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?13607,,) (while you don't need to log in with different Users and Roles).

Note: You can still log in using WFADMINISTRATOR via [GAM](https://wiki.genexus.com/commwiki/wiki?14960)'s Login or via a Custom Login Panel that uses GXflow's API.

#### [Who can handle Licenses?](#Who+can+handle+Licenses%3F+)

No login is required when no license is installed. As soon as at least one license is installed, a user with a GXflow Administrator role (eg. WFADMINISTRATOR) can request and handle the licenses.


|  |
| --- |
| **Backlinks** |
|
| [GeneXus 18 BPM Suite Release Notes](https://wiki.genexus.com/commwiki/wiki?51076) | [Table of contents:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |
| [GXflow centralized licenses configuration (GXflow on Linux)](https://wiki.genexus.com/commwiki/wiki?21728) | [GXflow centralized licenses configuration (GXflow on Windows)](https://wiki.genexus.com/commwiki/wiki?21761) | [KB:GXflow Demo](https://wiki.genexus.com/commwiki/wiki?52541) | [GXflow license troubleshooting](https://wiki.genexus.com/commwiki/wiki?42990) |
| [HowTo: Deploy a Workflow-based Application](https://wiki.genexus.com/commwiki/wiki?19848) | [HowTo: Work with GXflow license manager](https://wiki.genexus.com/commwiki/wiki?37207) |

---
