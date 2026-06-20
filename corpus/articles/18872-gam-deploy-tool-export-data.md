---
title: "GAM Deploy Tool: Export Data"
source_id: 18872
source_url: https://wiki.genexus.com/commwiki/wiki?18872
genexus_version: "18"
---

# GAM Deploy Tool: Export Data

One of the purposes of [GAM Deploy Tool](https://wiki.genexus.com/commwiki/wiki?18608) is to allow administrators of [GAM Manager Repository](https://wiki.genexus.com/commwiki/wiki?18617) to export data from an existing [GAM Repository](https://wiki.genexus.com/commwiki/wiki?17568) and [import data](https://wiki.genexus.com/commwiki/wiki?21974) into another Repository, of the same [GAM](https://wiki.genexus.com/commwiki/wiki?14960) datastore, or another one.

The following sections explain the Export deploy process of GAM Deploy Tool.

### [How to export data from a Repository](#How+to+export+data+from+a+Repository)

1. Execute [GAM Deploy Tool](https://wiki.genexus.com/commwiki/wiki?18608). Run it from GeneXus options (Tools -> GAM -> Create Deploy File), or as a standalone tool (execute GamDeployTool.exe).  
When executing it from GeneXus options, the export is done from the GAM datastore which corresponds to the current environment.

2. The first screen asks for the DBMS connection settings.

There you need to enter the connection settings of the GAM datastore.

`[imagen omitida: wiki id 18874]`

3. In the second step you are asked to enter the credentials of [GAM Manager Repository](https://wiki.genexus.com/commwiki/wiki?18617) administrator (gamadmin user).

`[imagen omitida: wiki id 18875]`

4. Afterwards you are asked to specify the Repository of GAM database from where data is going to be retrieved.

`[imagen omitida: wiki id 18876]`

5. There is the option of doing a full export, or a custom export (the latter option asks the user to specify further information later).

`[imagen omitida: wiki id 18877]`

6. Finally, specify the path and package name where the information is going to be saved.

`[imagen omitida: wiki id 18878]`

The file .gpkg generated is a zipped file which includes the following:

* Data in json format
* Configuration files

### [See also](#See+also)

[GAM Deploy Tool - Import Users](https://wiki.genexus.com/commwiki/wiki?22017,,)  
[GAM Deploy Tool : Creating connection.gam file](https://wiki.genexus.com/commwiki/wiki?18610)


|  |
| --- |
| **Backlinks** |
| [GAM - Deploy Tool](https://wiki.genexus.com/commwiki/wiki?18608) | [GAM Deploy Tool: Import Data](https://wiki.genexus.com/commwiki/wiki?21974) | [GAM Manager Repository](https://wiki.genexus.com/commwiki/wiki?18617) |
| [GAM options in GeneXus toolbar](https://wiki.genexus.com/commwiki/wiki?19947) | [HowTo: Update a repository from a GAM deploy tool package](https://wiki.genexus.com/commwiki/wiki?20929) |

---
