---
title: "GAM Google Authentication Type (X Evolution 3 upgrade 3 or prior)"
source_id: 20020
source_url: https://wiki.genexus.com/commwiki/wiki?20020
genexus_version: "18"
---

# GAM Google Authentication Type (X Evolution 3 upgrade 3 or prior)

For X Evolution 3 upgrade 4 or upper, see [GAM Google Authentication Type](https://wiki.genexus.com/commwiki/wiki?29013).

Using [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) you can authenticate on Google site, just by following these steps:

1. You need to create a "Google client application" in Google site and obtain Client Id and Client Secret for that application.

Go to the following link: https://code.google.com/apis/console

2. There go to API Access, as shown in the figure:

`[imagen omitida: wiki id 20024]`

3. Then you need to create an OAuth Application. Fill in a Product Name and press next:

`[imagen omitida: wiki id 20025]`

4. In Client Id Settings check box, select "Application Type" = Web Application.

5. Finally, you need to go through "Edit Settings", and change the Redirect URIs. There you may specify the complete URI of your application, including the artech.security.api.agamextauthinput object, as the figure shows:

`[imagen omitida: wiki id 20026]`

Example:

* In case of java: http://apps2.genexusx.com/Ide1b858bf3b044ba0ac777119780e4370/servlet/artech.security.api.agamextauthinput
* In case of NET: http://apps3.genexusx.com/Idea13f73cb4b24ddf860df9973132aa39/agamextauthinput.aspx
* In case of Ruby: http://apps2.genexusx.com/Id0d35da4dfc3343f0ad08f80a74e8ff4b/gxruby/gamextauthinput

6. In GeneXus, define a new Authentication Type = Google using the [GAM Backoffice](https://wiki.genexus.com/commwiki/wiki?15935).

Enter Cliend Id and Client Secret obtained in Google site.

`[imagen omitida: wiki id 20028]`

Important note:

In case of java and .NET you need to enter the complete site URL in CallBack URL. That is, in the example: http://apps2.genexusx.com/Ide1b858bf3b044ba0ac777119780e4370/servlet.  
In case of Ruby you need to specify in SITE URL only the server, not the complete URL, for example: http://apps2.genexusx.com

### [How to login using Google account in WEB applications](#How+to+login+using+Google+account+in+WEB+applications)

In case of Web Applications, the GamExampleLogin object (which is part of the GAM example library) includes automatically a button by which the user can login to Google.  
This button is included dynamically, as the Google Authentication Type is detected to be defined in the GAM Repository.

`[imagen omitida: wiki id 20038]`

The following code is associated to the "Google" Button:

```
Event &ButtonGoogle.Click
GAMRepository.LoginGoogle()
EndEvent
```

### [How to login using Google account in SD applications](#How+to+login+using+Google+account+in+SD+applications)

The following code is used for that purpose:

```
Event 'Google'
 SDActions.LoginExternal("google", &User, &Password)
EndEvent
```

### [See Also](#See+Also)

[GAM Facebook Authentication Type](https://wiki.genexus.com/commwiki/wiki?16516,,)  
[GAM - Twitter Authentication Type](https://wiki.genexus.com/commwiki/wiki?17208)  
[Additional Scope Property for GAM Google / Facebook Authentication Types](https://wiki.genexus.com/commwiki/wiki?21584,,)
