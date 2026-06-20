---
title: "Impact Analysis (GeneXus 18 latest upgrade or prior)"
source_id: 60652
source_url: https://wiki.genexus.com/commwiki/wiki?60652
genexus_version: "18"
---

# Impact Analysis (GeneXus 18 latest upgrade or prior)

When you press the F5 key, GeneXus examines the impact that the new definitions made in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) will have on the Database. It then displays a report called **Impact Analysis**, which indicates the additions or structural changes that need to be made to the Database. This report also details the SQL Statements that will be executed upon confirmation.

The following image shows an **Impact Analysis** report indicating that a new attribute (CustomerAddress) will have to be added to the CUSTOMER table:

`[imagen omitida: wiki id 31024]`

**Note**: Some symbols help you identify special situations. For example, a key symbol `[imagen omitida: wiki id 7133]` in the table structure area (on the right) indicates that the attribute is a key. An exclamation symbol `[imagen omitida: wiki id 7825]` represents a warning.

You can press the **Reorganize** button to proceed with the [Reorganization](https://wiki.genexus.com/commwiki/wiki?5288), or choose to cancel.

The term "Reorganize" refers to making changes to the Database.

When you choose to reorganize, GeneXus creates the necessary programs to change the Database and executes them, making the required changes. Next, it generates the programs corresponding to the application itself.

In the image above, only one change is shown for one table, but several changes may be detected and shown for different tables. Also, the first time you press the F5 key in a Knowledge Base, the title "Database needs to be reorganized"is replaced with "The Database tables will be created" and the**Reorganize** button is replaced with the **Create** button.

In some cases, the **Impact Analysis** report may indicate that no structural changes are needed in the Database.

Note that the reorganization script to be executed is saved as ReorganizationScript.txt. This may be useful if a DBA needs to analyze the script before it is run.
