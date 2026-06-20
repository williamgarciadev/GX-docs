---
title: "Internet Explorer compatibility mode property"
source_id: 8073
source_url: https://wiki.genexus.com/commwiki/wiki?8073
genexus_version: "18"
---

# Internet Explorer compatibility mode property

By default, when we are working with Internet Explorer 8, in order to work with it as with Internet Explorer 7, the GeneXus applications add a metatag; thus, the behavior of IE 8 will be like that of Internet Explorer 7.

### [Values](#Values)

|  |  |
| --- | --- |
| **IE7 Compatible** | When the application is running on IE8, it is automatically detected and the following tag is added: <meta http-equiv="X-UA-Compatible" content="IE=EmulateIE7"/>.The default value IE7 compatible is available because depending on the application, in some cases it han happen that the HTML generated could not be strictly compliant with the W3C standards. This is the default value. |
| **Do not specify** | No specific tags are added. The browser "chooses" the version according to the HTML used in the page.(1) |

### [Description](#Description)

(1) - When using GeneXus X Evolution 2 Upgrade 5 or higher and the "Do not specify" option, the following tag is added to the response to force using the latest Internet Explorer render engine. ([more information](http://www2.gxtechnical.com/portal/hgxppredirect.aspx?15,26,0,,,35521))

```
X-UA-Compatible    IE=Edge
```

The property only applies for IE8.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply changes made by this property, do a Build with this Only of the object.

### [Scope](#Scope)

**Platforms:** Web(.Net, Java)
