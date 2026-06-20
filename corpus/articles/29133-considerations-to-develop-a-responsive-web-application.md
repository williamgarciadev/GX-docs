---
title: "Considerations to develop a Responsive Web Application"
source_id: 29133
source_url: https://wiki.genexus.com/commwiki/wiki?29133
genexus_version: "18"
---

# Considerations to develop a Responsive Web Application

To develop a [Responsive Web Applications](https://wiki.genexus.com/commwiki/wiki?25159), the following has to be taken into account:

1. [HTML Document Type property](https://wiki.genexus.com/commwiki/wiki?13517) has to be set to HTML 5.
2. [Default Theme property](https://wiki.genexus.com/commwiki/wiki?8145) has to be set to Carmine. The Carmine Theme has all the classes inspired by [Bootstrap](http://getbootstrap.com/getting-started/).

The RWDMasterpage is automatically imported when [Default Web Form Editor property](https://wiki.genexus.com/commwiki/wiki?25154) is set to Abstract Layout. 

**Note:**

The viewport meta tag is automatically added to the HTML <head> in order to have a responsive behavior:

```
   Form.Meta.AddItem(!"viewport", !'width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no')
   Form.Meta.AddItem(!"apple-mobile-web-app-capable", 'yes')
```

In addition to the required properties, the following properties are also used:

* [Default Web Form Editor property](https://wiki.genexus.com/commwiki/wiki?25154)
* [Web Form Defaults property](https://wiki.genexus.com/commwiki/wiki?25135)


|  |
| --- |
| **Backlinks** |
| [Toc:Responsive Web Design in GeneXus](https://wiki.genexus.com/commwiki/wiki?29134) |

---
