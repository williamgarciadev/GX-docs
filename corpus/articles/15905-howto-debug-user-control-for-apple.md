---
title: "HowTo: Debug User Control for Apple"
source_id: 15905
source_url: https://wiki.genexus.com/commwiki/wiki?15905
genexus_version: "18"
---

# HowTo: Debug User Control for Apple

**Warning**: Since [GeneXus 16](https://wiki.genexus.com/commwiki/wiki?35351,,), it is strongly recommended to create a [User Control object](https://wiki.genexus.com/commwiki/wiki?39356). However, what it is explained in this article is still valid.

The following document explains the steps to follow in order to debug your User Control or External Object for
Native Mobile applications; in this case the
[Apple](https://wiki.genexus.com/commwiki/wiki?14917) [Environment](https://wiki.genexus.com/commwiki/wiki?7115).

**1.** The first thing is to have an implementation of your User Control or External Object (it could be empty).

**2.** Copy the lib to the *UserControls* folder in your GeneXus environment.

**3.** Build the project from GeneXus in order to transfer the whole project to your Mac.

**4.** Once in the Mac, open the associated Xcode project; by detault it is located under */Users/UserName/Documents/Projects/KnowledgeBaseName/DashboardName*

**5.** Delete the reference to the External Object or UC library and add a reference to the Xcode project.

**6.** Add the External Object | UC project as a dependency in order to get it built.

**7.** Now you can insert the required breakpoints in the desired classes and the application will stop there during the debug session.

### [See Also](#See+Also)

[User Controls for Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?15301)  
[External Objects for Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?17880)


|  |
| --- |
| **Backlinks** |
| [Category:User Controls for Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?15301) |

---
