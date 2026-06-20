---
title: "GAM use Example: Private web application"
source_id: 15923
source_url: https://wiki.genexus.com/commwiki/wiki?15923
genexus_version: "18"
---

# GAM use Example: Private web application

This is a basic sample, based on  [Lab Application](http://www2.gxtechnical.com/portal/hgxpp001.aspx?15,8,8,O,E,0,,3310e).

In this case, the idea is to make the application private, using [GeneXus Access Manager](https://wiki.genexus.com/commwiki/wiki?24746).

Only authorized users will be able to access the pages of this application.

Steps to follow:  
  
1. Set [Enable Integrated Security Property](https://wiki.genexus.com/commwiki/wiki?14706) = True.

2. Run GAM Backoffice and define users and security policies for this application. See [GAM Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935) for more details.

3. Create a "login object" which will be displayed to the user when the security session expires or when it does not exist (or any other security failure happens).  
The "login object" (named "FootballLoginGAM" in this example), will use [GAM API](https://wiki.genexus.com/commwiki/wiki?16535) to implement security.

The easiest way to program this object is to make a "Save as" of GAMExampleLogin Object (which is provided by GAM Examples) and make the necessary changes.

`[imagen omitida: wiki id 15926]`

4. Define "FootballLoginGAM" as the login object. Set [Login Object for Web Property](https://wiki.genexus.com/commwiki/wiki?15590) = FootballLoginGAM.

5. Only authorized users will be able to access this application.

[Default Integrated Security Level Property](https://wiki.genexus.com/commwiki/wiki?15214) has to be set to "Authentication" value, because all the objects of the KB will be secure.  
The only object with no security required is "FootballLoginGAM", that is to say, that "FootballLoginGAM" will have [Integrated Security Level Property](https://wiki.genexus.com/commwiki/wiki?15214) = None.

`[imagen omitida: wiki id 15927]`

6. Rebuild All, and only authorized users will access the webpanels of the application. The "login object" look&feel for this example is shown in the image:

`[imagen omitida: wiki id 15925]`

### [See Also](#See+Also)

[GAM Use Example: Public Application With Some Private Components](https://wiki.genexus.com/commwiki/wiki?15772)


|  |
| --- |
| **Backlinks** |
| [GAM - Authentication Scenarios](https://wiki.genexus.com/commwiki/wiki?15937) |

---
