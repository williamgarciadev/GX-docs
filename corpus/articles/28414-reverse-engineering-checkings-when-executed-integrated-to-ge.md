---
title: "Reverse Engineering Checkings when executed integrated to GeneXus"
source_id: 28414
source_url: https://wiki.genexus.com/commwiki/wiki?28414
genexus_version: "18"
---

# Reverse Engineering Checkings when executed integrated to GeneXus

When the Database Reverse Engineering tool is executed within the GeneXus IDE; some extra checking are done in the current Knowledge Base regarding the physical model (Tables, Data view, Attributes, Indices and so on).

### [Warnings](#Warnings)

#### [Warning: The table is in the {0} and it was used in the analysis](#Warning%3A+The+table+is+in+the+%7B0%7D+and+it+was+used+in+the+analysis)

When selecting a Table, DBRet will check if the table has a Data View in the current KB and was not selected in the DBRet Wizard Step #2 and is related to the selection.  
For example, if it is referenced in the selection extended table as Foreign Key.

#### [Warning: The table exists in the {0}, it will be overwritten](#Warning%3A+The+table+exists+in+the+%7B0%7D%2C+it+will+be+overwritten)

There is an existing Data view in the current Knowledge Base; the user selected again the same table to be imported.

#### [Warning: The table doesn't have primary key](#Warning%3A+The+table+doesn%27t+have+primary+key)

The selected database table does not have a Primary Key; the user will need to select a Primary Key to be imported in the KB.

#### [Warning: The attribute/s ({0}) were chosen as primary key](#Warning%3A+The+attribute%2Fs+%28%7B0%7D%29+were+chosen+as+primary+key)

The attributes detailed in {0} were chosen as primary key as there is a unique index containing them.

#### [Warning: The attribute {0} is auto number and was chosen as primary key](#Warning%3A+The+attribute+%7B0%7D+is+auto+number+and+was+chosen+as+primary+key)

The selected attribute is autonumber.

#### [Warning: {0} is a FK to {1} but it's not selected](#Warning%3A+%7B0%7D+is+a+FK+to+%7B1%7D+but+it%27s+not+selected)

Table {1} was not selected in the table list.

#### [Warning: ({0}) is a foreign key, but there's no index for the attribute/s](#Warning%3A+%28%7B0%7D%29+is+a+foreign+key%2C+but+there%27s+no+index+for+the+attribute%2Fs)

The selected Index partially contains the selected attributes.

#### [Warning: The index \"{0}\" was ignored. It has the same composition of {1}](#Warning%3A+The+index+%5C%22%7B0%7D%5C%22+was+ignored.+It+has+the+same+composition+of+%7B1%7D)

Indices with the same composition are ignored.

#### [Warning: The attribute {0} was not found, the index {1} was ignored](#Warning%3A+The+attribute+%7B0%7D+was+not+found%2C+the+index+%7B1%7D+was+ignored)

Indices with attributes without Name or Key are discarded.

#### [Warning: The Index {0} was marked as unique because it is a primary key Index](#Warning%3A+The+Index+%7B0%7D+was+marked+as+unique+because+it+is+a+primary+key+Index)

The selected index is Primary Key and not duplicate.

#### [Warning: The type {0} is not supported](#Warning%3A+The+type+%7B0%7D+is+not+supported)

The selected attribute type is not supported.


|  |
| --- |
| **Backlinks** |
| [Database Reverse Engineering Wizard](https://wiki.genexus.com/commwiki/wiki?6627) |

---
