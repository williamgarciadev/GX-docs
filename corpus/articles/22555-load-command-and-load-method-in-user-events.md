---
title: "Load Command and Load Method in User Events"
source_id: 22555
source_url: https://wiki.genexus.com/commwiki/wiki?22555
genexus_version: "18"
---

# Load Command and Load Method in User Events

The [Load command](https://wiki.genexus.com/commwiki/wiki?8196) and the [Grid Load method](https://wiki.genexus.com/commwiki/wiki?8814) are used within [User defined events](https://wiki.genexus.com/commwiki/wiki?8044) in [Web Panels](https://wiki.genexus.com/commwiki/wiki?6916), [SD Panels](https://wiki.genexus.com/commwiki/wiki?24829) and [Work With for Smart Devices objects](https://wiki.genexus.com/commwiki/wiki?15974) in order to force the loading of a new line into a [Grid control](https://wiki.genexus.com/commwiki/wiki?24817).

The [Web User Experience property](https://wiki.genexus.com/commwiki/wiki?22449) has to be set to "Smooth", so that the Load command and the Load method add a new line into the grid, without refreshing the whole grid in the process.

### [Scenario of use](#Scenario+of+use)

For developing a messaging page, as explained in [HowTo:Develop a messaging web page](https://wiki.genexus.com/commwiki/wiki?22527), we will need to guarantee that when a user adds a new comment, all other users who may be also editing the page will receive the first user's comments, without losing what is typed at their end.

Technically, the grid must not refresh as a whole when a [Web Notification](https://wiki.genexus.com/commwiki/wiki?22442) arrives and it is added to the comments grid.

In this case, the Load command adds a new line to the grid without refreshing the grid. So, if any other row is being edited it will be kept unchanged.

### [Note](#Note)

Consider that in particular the [Load command](https://wiki.genexus.com/commwiki/wiki?8196) can be used within [User defined events](https://wiki.genexus.com/commwiki/wiki?8044) only if the object contains one grid. One the other hand, if the object contanis more than one grid, use the [Grid Load method](https://wiki.genexus.com/commwiki/wiki?8814).


|  |
| --- |
| **Backlinks** |
| [Grid Load method](https://wiki.genexus.com/commwiki/wiki?8814) | [HowTo:Develop a messaging web page](https://wiki.genexus.com/commwiki/wiki?22527) |
| [Web User Experience property](https://wiki.genexus.com/commwiki/wiki?22449) |

---
