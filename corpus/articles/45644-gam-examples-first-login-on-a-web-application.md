---
title: "GAM - Examples - First login on a Web application"
source_id: 45644
source_url: https://wiki.genexus.com/commwiki/wiki?45644
genexus_version: "18"
---

# GAM - Examples - First login on a Web application

"GAMExampleLogin" is the sample object that allows users to log in. It is executed automatically when there is no valid session.

When executing the "GAMExampleLogin" for the first time, you have to consider some aspects:

      1. Initial Execution

If you execute this object (or the "GAMHome" object, which will redirect to the "GAMExampleLogin" if you are not logged in), you will be asked to configure a [Home Object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?34429,,) for your application.

      2. Login Process

First, you will be asked to enter your credentials in the GAMExampleLogin object:

`[imagen omitida: wiki id 51748]`

       3. Home Object Configuration

Then, the "GAMHome" object is executed, where you are asked to enter the Home Object:

`[imagen omitida: wiki id 51749]`

#### [**Purpose of Configuring a Home Object**](#Purpose+of+Configuring+a+Home+Object)

The purpose of configuring a Home object is to set in the GAM database which object to return when there isn't any caller of the "GAMExampleLogin" object. That is to say, if A is executed and needs authentication, the execution flow returns to A after a successful login. But if the GAMExampleLogin has no object to redirect, a Home Object is needed to end the execution flow.

### [See Also](#See+Also)

[GAMExampleLogin object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?39427,,)


|  |
| --- |
| **Backlinks** |
| [Category:GAM - Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935) | [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |

---
