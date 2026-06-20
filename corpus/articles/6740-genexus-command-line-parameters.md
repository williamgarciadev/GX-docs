---
title: "GeneXus command line parameters"
source_id: 6740
source_url: https://wiki.genexus.com/commwiki/wiki?6740
genexus_version: "18"
---

# GeneXus command line parameters

GeneXus.exe can be started with a set of arguments from the command line. Syntax and arguments are described in this document.

### [Syntax](#Syntax)

```
genexus [@argfile] [/KB|kb:<value>] [/Culture|c:<value>] [/Install[+|-]] [/NoLastKB[+|-]] [/MeasureCommandTime[+|-]] 
          [/NoWorkspace[+|-]] [/IDEStyle:is<value>] [/help|?|h] [/version|v]
```

|  |  |
| --- | --- |
| @argfile | Reads arguments from a file. |
| /KB:<value> | [URI](http://en.wikipedia.org/wiki/Uniform_Resource_Identifier) of Knowledge Base (Default is ""). |
| /Culture:<value> | Not implemented yet. |
| /Install[+|-] | It may be used after each install Packages and User Controls. |
| /NoLastKB[+|-] | This indicates that the Last KB opened will not be opened. |
| /MeasureCommandTime[+|-] | Time consumption data (timestamp) will appear in the general output. |
| /NoWorkspace[+|-] | Opens GeneXus without restoring the saved workspace; that is, a default workspace is loaded and changes to it are saved as a new workspace when GeneXus is closed. |
| /IDEstyle:<value> IDEStyle, values: blue, silver, black, red | This indicates the IDE color scheme to be used. |
| /help | Shows usage. |
| /version | Shows the current GeneXus version. |
| /NoRecentObjects | Opens a Knowledge Base without opening the objects that were open when the Knowledge Base was closed. |

### [Example](#Example)

To run GeneXus using the "*noLastKB*" parameter you should execute the following:

```
"<GeneXus_Complete_Installation_Path>\Genexus.exe" /noLastKb
```

### [Note](#Note)

**[+|-]** arguments indicate if the option will be taken into account or not, for example, /NoLastKB will have the same behavior as not indicating the option. It is especially useful when programming actions in batch processes.


|  |
| --- |
| **Backlinks** |
| [Creating User Controls for Android](https://wiki.genexus.com/commwiki/wiki?18674) |

---
