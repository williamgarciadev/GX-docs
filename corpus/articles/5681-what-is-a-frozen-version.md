---
title: "What is a Frozen Version?"
source_id: 5681
source_url: https://wiki.genexus.com/commwiki/wiki?5681
genexus_version: "18"
---

# What is a Frozen Version?

An application life cycle reaches several "milestones" that are important to people working on (or with) it. The application entering the Test phase, Quality assurance or Production are just a few examples of these milestones. It is important, in the development process, to keep track of these milestones and save the application state for several reasons. They let you answer questions like:

* What is in Production?
* What is installed in Customer X?
* What changes where made between the Test phase and Production?

In GeneXus these milestones are called Frozen Versions. They are read-only photos of an application at a given time. In [Software Configuration Management](http://en.wikipedia.org/wiki/Software_configuration_management) the term "label" is also used to identify a frozen version.

There can be as many frozen versions as are needed in a Knowledge Base.

The purpose of frozen versions is to reflect important milestones (deployment, installation in Customer X, etc.) in an application's life cycle. A version in GeneXus is a read-only copy of an application. It's like a printed photo, which can be observed and/or analyzed but not modified.  
  
To create a new Frozen Version, open the [Knowledge Base Versions tool window](https://wiki.genexus.com/commwiki/wiki?5687), right-click on the first node of the tree (it has the same name as your Knowledge Base) and select "Freeze". Fill the New Frozen Version dialog and press Enter. The time it takes to create a frozen version is proportional to the size of your application.

###### 

###### [Fig 1. Freezing a version (creating a new Frozen Version)](#Fig+1.+Freezing+a+version+%28creating+a+new+Frozen+Version%29)

The action of creating a new Frozen Version is called "Freezing" a version.  
  
The above guidelines tell you how to create a new version from what is known as the [development versions](https://wiki.genexus.com/commwiki/wiki?5684). You cannot create a frozen version from another frozen version.  
  
Frozen Versions can be used to :

* Analyze (not modify) objects, properties, environments, etc.
* As a source or target of a Database Impact Analysis Report
* To create the database
* To regenerate all programs

**Import Backup**

When an [Import](https://wiki.genexus.com/commwiki/wiki?3179) is performed over a Knowledge Version, if the Automatic Backup property is set to True, a special Frozen Version is created to backup the current Development Version. This new Frozen Version will have only one action available to execute: [Revert](https://wiki.genexus.com/commwiki/wiki?5685,,). By executing this action, the active Development Version will be changed to the Import Frozen Version status or other Development Version status.

***Tip:***

Versions with “pending changes” (that is, with objects that were changed since the last Impact Database was run) cannot be frozen. If you attempt to execute the freeze action, the following message appears: “Changes have been made since the last Build of Environment '.Net/Java Environment'. You must execute Build All before freezing.”


|  |
| --- |
| **Backlinks** |
| [Automatic Backup property](https://wiki.genexus.com/commwiki/wiki?5617) | [Create Knowledge Base from GeneXus Server](https://wiki.genexus.com/commwiki/wiki?22416) |
| [Defining versions for each application release](https://wiki.genexus.com/commwiki/wiki?20945) |
| [Knowledge Base Versions tool window](https://wiki.genexus.com/commwiki/wiki?5687) | [Knowledge Manager Import](https://wiki.genexus.com/commwiki/wiki?3179) | [Migration of KB with Carmine Theme to Unanimo Design System](https://wiki.genexus.com/commwiki/wiki?51821) |
| [Revert Operation](https://wiki.genexus.com/commwiki/wiki?11997) | [Team Development Versions Dialog](https://wiki.genexus.com/commwiki/wiki?21051) | [What is a Development Version?](https://wiki.genexus.com/commwiki/wiki?5684) |
| [What is the Trunk?](https://wiki.genexus.com/commwiki/wiki?5683) |

---
