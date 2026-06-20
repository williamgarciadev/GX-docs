---
title: "Generating in COBOL"
source_id: 14124
source_url: https://wiki.genexus.com/commwiki/wiki?14124
genexus_version: "18"
---

# Generating in COBOL

### [Software Requirements](#Software+Requirements)

Specific software is required to compile and execute the applications generated with the COBOL generator.

1. In iSeries you must have GX library installed. It can be obtained [here](https://www.genexus.com/developers/DownloadCenter?en,,,3047;;).
2. Also, you must have an iSeries connection to transfer the programs. The connection may be TCP/IP or through Client Access.
3. To work in iSeries, the user must have the rights described in [Necessary permits to work](https://wiki.genexus.com/commwiki/wiki?14127) and [Permits/Approvals required for GX library](https://wiki.genexus.com/commwiki/wiki?14128).

### [Steps to be followed](#Steps+to+be+followed)

1. Create a model selecting the COBOL generator.
   1. Select File/New/Knowledge Base (CTRL + CAPS LOCK + N)
   2. Select a Name and Location for the KB. Next, press Create with default options
   3. Go to preferences, select the Environment, and change the following properties:
      * User Interface: Windows
      * Language: COBOL/400 (the Data Source will change to iSeries Native)
      * Target Path: you can leave it as is but we recommend changing it to something similar to COBiSeries<Id>
      * Name: you can leave it as is but we recommend changing it to something similar to COBiSeries
   4. Select Generator and update the following properties:
      * Server Name: iSeries IP or Name
      * User: iSeries User
      * Password: iSeries Password
   5. Select Default Data Store, right-click, and Change Data Store: iSeries Native
2. In the DBMS options, type the name of the programs and data library to be created in iSeries.
3. Select the transfer method to be used for the transfer. TCP/IP is recommended since it is the fastest according to the tests performed.
4. Once this has been set up, the model can be created in iSeries.
5. Once the programs have been specified and generated, transfer them to iSeries. For this, you must go to the Run or F5 option and select the programs you want to transfer. Next, the programs are sent to iSeries for them to be compiled. Once the programs have been transferred and compiled, they can be executed from the iSeries commands line.
6. If you want to see the developer menu associated with this model, type gx/gx Program\_Library\_name

### [Going Live](#Going+Live)

Use the GXimpdbr command. For further details on how to execute this command, we suggest reading [here](https://wiki.genexus.com/commwiki/wiki?14125).

### [See Also](#See+Also)

[COBOL Generator Properties](https://wiki.genexus.com/commwiki/wiki?13999)


|  |
| --- |
| **Backlinks** |
| [GeneXus Standard Classes](https://wiki.genexus.com/commwiki/wiki?18859) |

---
