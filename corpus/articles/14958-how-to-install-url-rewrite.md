---
title: "How to install URL Rewrite"
source_id: 14958
source_url: https://wiki.genexus.com/commwiki/wiki?14958
genexus_version: "18"
---

# How to install URL Rewrite

URL Rewrite is a requirement for publishing Rest Services (generated with .NET)

**How to install it?**

**1. In case of IIS7 / 7.5**(distributed by Windows 7, Vista and 2008) **and 8** (distributed by Windows 8), you have to follow these steps:

a. Go to this URL <http://www.iis.net/download/URLRewrite> and click 'Install':

`[imagen omitida: wiki id 14954]`

b. Select 'URL Rewrite' and click 'Install' button:

`[imagen omitida: wiki id 14956]`

c. Click 'Accept' button:

`[imagen omitida: wiki id 14957]`

**Important:** If the dialog change to Web platform 3.0

`[imagen omitida: wiki id 15137]`

It's **strongly recommended**,  in the first step (a), download and run the setup locally

`[imagen omitida: wiki id 15138]`

If Rest pages doesn't work properly, given the 404 error, means that an IIS configuration is pending.

```
"%WINDIR%\Microsoft.Net\Framework\v3.0\Windows Communication Foundation\ServiceModelReg.exe" –i
```

Or it is required browser directory permission on IIS. for more information see [URLRewrite - Common issues](https://wiki.genexus.com/commwiki/wiki?18398)

**2. In case of IIS5 or IIS6** (distributed by Windows XP, Windows 2003) , you have to follow these steps:

a.Download IIRF from <http://iirf.codeplex.com/> (Windows XP needed version 2.0.1.15)

b. Install as explained in <http://dotnetzip.herobo.com/Iirf20Help/html/6b426152-704a-4907-b87e-2e1938a89cad.htm> (Installing IIRF), To sum up, it implied:

       b1. Unzip the files  
       b2. IIRF.dll file permissions, depending on the operating system:  
**Windows Xp -->** user ASPNET

`[imagen omitida: wiki id 14982]`  
**Windows 2003 -->** IIS\_WPG group

`[imagen omitida: wiki id 14983]`

      b3. Include this file (IIRF.dll) such as ISAPI Filter: **Default Web Site -> properties -> isapi filters -> Add** y alli seleccionar la IIRF.dll.

`[imagen omitida: wiki id 14984]`

      b4. Include Mime type: **Virtual directory -> properties-> Http Headers -> MIME Types** , include **extension = .json, mimetype: text/plain**

`[imagen omitida: wiki id 14985]`

      b5. Include .svc extension in aspnet\_isapidll. It means **Virtual Directory -> properties-> configuration -> mappings**: .svc extension with aspnet\_isapi.dll.   
             It may already exist, by default

`[imagen omitida: wiki id 14986]`

      b6. Configure permissions of .SVC with Limit to=GET, HEAD, POST, DEBUG. Like the following picture:

`[imagen omitida: wiki id 17187]`

Note:In order to deploy an application under IIs 6 or lower, the iirf.ini file must e included. This file has the rewrite rules and is generated when IIIS version property is set to "IIS 6 or lower"


|  |
| --- |
| **Backlinks** |
| [Android - FAQ and Common Issues](https://wiki.genexus.com/commwiki/wiki?14575) | [GeneXus 18 hardware and software requirements](https://wiki.genexus.com/commwiki/wiki?30900) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54300) |
| [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 3)](https://wiki.genexus.com/commwiki/wiki?54649) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55768) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 6)](https://wiki.genexus.com/commwiki/wiki?56187) |
| [GXflow Software Requirements](https://wiki.genexus.com/commwiki/wiki?18393) | [GXflow Software Requirements (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55579) |
| [URLRewrite - Common issues](https://wiki.genexus.com/commwiki/wiki?18398) |

---
