---
title: "Release Lock"
source_id: 17485
source_url: https://wiki.genexus.com/commwiki/wiki?17485
genexus_version: "18"
---

# Release Lock

To make sure you don't forget to release a lock you don't need any more, locked objects are shown in the *Team development* Locks tab.

To release a [lock](https://wiki.genexus.com/commwiki/wiki?17484) manually, select the objects in your working copy KB for which you want to release the lock, then select the Team Development contextual menu *Release Lock* option; GeneXus will contact the GXserver repository and release the locks on the selected objects.

Check the status on the Team Development output window, you should get a detail message similar to the following:

========== Release Lock started ==========

```
Contacting GeneXus Server at 'http://...'... done!
Exporting Transaction 'Invoice'...
Export File Created At: 'C:\Users\genexus\AppData\Local\Temp\tmpBD49.xpz'
GeneXus Server: Processing file...
GeneXus Server: Checking Import References...... Finished
GeneXus Server: Reading import file objects...... Finished
Released Lock in Invoice
done!
Release Lock Success
```


|  |
| --- |
| **Backlinks** |
| [Team Development Contextual Menu](https://wiki.genexus.com/commwiki/wiki?31972) |
| [Team Development Locks Section](https://wiki.genexus.com/commwiki/wiki?17509) |

---
