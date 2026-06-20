---
title: "GeneXus for SAP Systems Security"
source_id: 33842
source_url: https://wiki.genexus.com/commwiki/wiki?33842
genexus_version: "18"
---

# GeneXus for SAP Systems Security

To solve the authentication and authorization for the web and mobile applications [GeneXus for SAP Systems](https://wiki.genexus.com/commwiki/wiki?33616) uses the [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) that is a [Role Based Access Control (RBAC)](https://wiki.genexus.com/commwiki/wiki?17808) module integrated with GeneXus.

In this particular case, in which you are using Fiori, you have to follow some extra steps:

1) Select the Preferences tab in the KB Explorer:

`[imagen omitida: wiki id 40564]`

2) Open the **Patterns** node and select the **Fiori for Web** nested node:

`[imagen omitida: wiki id 40565]`

3) Once there, open the Security Tab:  
  
`[imagen omitida: wiki id 40566]`

4) Then, right-click the Security node, and select from the contextual menu: **Enable GAM Integration**

`[imagen omitida: wiki id 40567]`

5) Next, you have to set the Version's [Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214) to Authorization:

`[imagen omitida: wiki id 40569]`

Finally, your project has the whole package, all the power of GAM with the looks of the pattern Fiori.

`[imagen omitida: wiki id 40600]`


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus for SAP Systems](https://wiki.genexus.com/commwiki/wiki?33616) |

---
