---
title: "Using LightHouse to validate your PWA"
source_id: 42665
source_url: https://wiki.genexus.com/commwiki/wiki?42665
genexus_version: "18"
---

# Using LightHouse to validate your PWA

[Lighthouse](https://developers.google.com/web/tools/lighthouse/) is an automated tool for improving the quality of your [Progressive Web Apps](https://wiki.genexus.com/commwiki/wiki?42600). It can be easily run from Chrome DevTools.

Running under HTTPS is mandatory, and all the redirections have to be done to HTTPS, so you have to add the following rule for redirection in the web.config file:

```
<system.webServer>
    ...
   <rewrite>
     <rules>
       <clear />
       <rule name="Redirect to https" stopProcessing="true">
        <match url=".*" />
         <conditions>
           <add input="{HTTPS}" pattern="off" ignoreCase="true" />
         </conditions>
        <action type="Redirect" url="https://{HTTP_HOST}{REQUEST_URI}" redirectType="Permanent" appendQueryString="false" />
       </rule>
     </rules>
   </rewrite>
 </system.webServer>
```


|  |
| --- |
| **Backlinks** |
| [How to create a PWA using GeneXus](https://wiki.genexus.com/commwiki/wiki?42601) | [How to create a PWA using GeneXus (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?55046) | [Toc:Progressive Web Applications in GeneXus](https://wiki.genexus.com/commwiki/wiki?42600) |

---
