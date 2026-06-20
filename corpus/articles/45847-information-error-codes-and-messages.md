---
title: "Information Error Codes and messages"
source_id: 45847
source_url: https://wiki.genexus.com/commwiki/wiki?45847
genexus_version: "18"
---

# Information Error Codes and messages

The following list shows the **nfo** messages that can be displayed at Specification time.

| Code | Message |
| --- | --- |
|  | |
| **nfo0001** | **This object has client-side events only, no data providers will be generated.** |
|  | Indicates that the panel has no events to evaluate on the server and therefore it does not require generating a [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270) to load data. |
|  | |
| **nfo0002** | **This step will be executed after reorganization of ''%1'' is completed.** |
|  | When the reorganization of a table requires two steps, this message is shown in the second step to indicate which table must be previously reorganized to perform it. For example, when a reorganization swaps the name of two tables. |
|  |  |
| **nfo0003** | **The reorganization for this table makes the schema not backward compatible.** |
|  | Notifies whether a certain database reorganization may cause the current programs to be incompatible with the new DB schema. Read more in [Scenario of backward compatible reorganizations](https://wiki.genexus.com/commwiki/wiki?48715). |
|  |  |
| **nfo0004** | **%1 was associated to Data view %2.** |
|  | Notifies in the [IAR](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?31023,,) that a table that was previously associated with a [Data View](https://wiki.genexus.com/commwiki/wiki?1914) is no longer associated with it.   This occurs either when you implicitly remove the table from the Data View's [Associated table property (in Data Views)](https://wiki.genexus.com/commwiki/wiki?8063) or if you change the composition of the primary key for that Table. |
|  |  |
| **nfo0005** | **This table is reorganized using a conversion program.** |
|  | Indicates that a table needs to be reorganized, and this reorganization involves the use of a conversion program (creation of temporary tables). |
|  |  |
| **nfo0006** | **Attribute ''%1'' of type embedding changed dimensions. Its current content will be reset.** |
|  | Indicates (in an [Impact Analysis](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?31023,,)) that, since an attribute based on the [Embedding data type](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?59216,,) has changed its dimensions, the content of that attribute will be reset (NULL if the field allows nulls, or empty if it does not). Therefore, you may want to implement a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) to recalculate the embeddings after performing this [Reorganization](https://wiki.genexus.com/commwiki/wiki?5288). |

## Availability

Information messages have been available since [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?45624,,).

## [See also](#See+also)

[Specification Error Codes and Messages](https://wiki.genexus.com/commwiki/wiki?5933)


|  |
| --- |
| **Backlinks** |
| [Table of contents:Coded Messages](https://wiki.genexus.com/commwiki/wiki?47288) | [Disabled warnings property](https://wiki.genexus.com/commwiki/wiki?8009) |
| [Packaged Module Management Error Codes and messages](https://wiki.genexus.com/commwiki/wiki?46761) | [Packaged Modules Management messages (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55022) | [Warnings treated as errors property](https://wiki.genexus.com/commwiki/wiki?8010) |

---
