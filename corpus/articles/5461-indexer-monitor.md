---
title: "Indexer Monitor"
source_id: 5461
source_url: https://wiki.genexus.com/commwiki/wiki?5461
genexus_version: "18"
---

# Indexer Monitor

The [Full-Text Search](https://wiki.genexus.com/commwiki/wiki?5277) capability requires internal use of the index of all the elements that make up a Knowledge Base to quickly report search results. Because large volumes of information can take a long time to index, the user can monitor the process to know its status, and can even pause the process and resume it at any time. To access the monitor view, open the Indexer Monitor option in the Tools menu.

It should be noted that while the process is in Running (incomplete) status, a search may give partial results. The user is alerted of this by a warning icon shown in the search window.

`[imagen omitida: wiki id 5462]` `[imagen omitida: wiki id 5463]`

The following situations should be considered:

* When you click Pause, the indexer will be paused for the currently opened Knowledge Base and user. The process will continue in this paused state until you click Resume, even if you close the Knowledge Base and reopen it. If another user opens the KB, the status may be different.
* When you resume, indexing starts where it stopped when it was paused.
* During massive updates (Imports, for example), indexing may be automatically paused. If automatically paused, it will resume automatically when the process causing the pause ends.

Tip: To know what the index status is (i.e., whether the indexer is running or not) use the View/Tool Windows/Indexer Monitor option.

Note:

"The *FTIndex subdirectory, within a KB directory, saves the KB full text indexes. ( if the kb has a lot of objects / versions ) that folder may growth considerably. If you don't want consume that disk space, you can stop that process and delete the directory FTIndex. ( In such case you can't use the “Search” inside of that kb )*"


|  |
| --- |
| **Backlinks** |
| [Knowledge Manager Import](https://wiki.genexus.com/commwiki/wiki?3179) |

---
