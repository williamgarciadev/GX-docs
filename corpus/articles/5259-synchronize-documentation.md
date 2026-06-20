---
title: "Synchronize Documentation"
source_id: 5259
source_url: https://wiki.genexus.com/commwiki/wiki?5259
genexus_version: "18"
---

# Synchronize Documentation

The documentation included in a [GeneXus](https://wiki.genexus.com/commwiki/wiki?1756) [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) (KB) can be useful for people who do not have GeneXus but have access to a [Wiki-style](http://en.wikipedia.org/wiki/Wiki) website. End users, people who specialize in customizing software after installation and programmers who do not have the Knowledge Base at hand are just a few examples of the people who could find it useful. GeneXus lets you easily publish your KB documentation in a Wiki-style Website, making it accessible to everyone inside and outside your organization.  
  
The term "Documentation" in this document refers to Document objects and Documentation written for any object in a Knowledge Base.

### [Installing a Wiki](#Installing+a+Wiki)

First of all you need to have a Wiki, where all documents will be published.

To do so, download the lastest version of Knowloedge Base and build and deploy the project with your own environment preferences.

### [Enabling Synchronization](#Enabling+Synchronization)

Synchronization is enabled by default for all documents in your Knowledge Base. You can change this default by changing the value of the [Synchronize with External Wiki](https://wiki.genexus.com/commwiki/wiki?5257) property in Preferences. Set the value to True or False depending on whether most documents in your KB are going to be published or not, respectively. Then, you can change the value of the [Synchronize with External Wiki property](https://wiki.genexus.com/commwiki/wiki?5257) property in each document you want to set as an exception.

### [Synchronization](#Synchronization)

After you have set the publishing defaults and exceptions according to your needs, select Synchronize by right-clicking the Documentation folder in [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210). A dialog will be displayed prompting you for your Wiki Server(s) and allowing you to publish.  
  
`[imagen omitida: wiki id 5258]`  
  
Select the Add button to add a new server if you do not already have one. Add the external wiki URL, that's where you have deployed the gxwiki instance. Sample URLs depending on the generator

```
C#
http://localhost/GXwiki6.NetEnvironment/
Java
http://localhost:8080/GXwiki6JavaEnvironment/servlet/
```

In case your wiki needs authentication, set this values in the dialog and finally hit the Synchronize button.

`[imagen omitida: wiki id 20667]`  
  
By default, synchronization scans all the documents that have been changed and deleted in your KB since the last successful synchronization, and updates or deletes them from the wiki server. Forcing synchronization (selecting the Force checkbox) will mean that the change date will be ignored and all documents will be refreshed.

### [Why more than one Wiki Server?](#Why+more+than+one+Wiki+Server%3F)

The idea behind this feature is that you may have several installations, each with their separate Documentation Wiki. When you make a change in your documentation you will probably want to publish this change with all your customers.


|  |
| --- |
| **Pages** |
| [Synchronize with External Wiki property](https://wiki.genexus.com/commwiki/wiki?5257) |

---
