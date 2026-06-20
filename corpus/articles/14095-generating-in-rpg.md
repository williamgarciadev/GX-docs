---
title: "Generating in RPG"
source_id: 14095
source_url: https://wiki.genexus.com/commwiki/wiki?14095
genexus_version: "18"
---

# Generating in RPG

#### [Software Requirements](#Software+Requirements)

You must have a specific software for the compilation and execution of the applications generated with RPG generator.

1. In the iSeries you must have GX library installed. It can be obtained [here](https://www.genexus.com/es/developers/downloadcenter?data=3047;).
2. You must have an iSeries connection to be able to transfer the programs. The connection may be TCP/IP or it may be through Client Access.
3. To be able to work in the iSeries the user must have the rights detailed, see "[Necessary permits to work](https://wiki.genexus.com/commwiki/wiki?14127)" and "[Approvals required for GX library](https://wiki.genexus.com/commwiki/wiki?14128)".

#### [Steps to be followed](#Steps+to+be+followed)

1. Create a model selecting the RPG generator.
   1. Select File/New/Knoledge Base (CTRL+CAPSLOCK+N)
   2. Select a Name and Location for the KB then press Create with default options
   3. Go to preferences, Select the Environment and change the following properties:
      * User Interface: Windows
      * Language: RPG/400 (the Data Source will change to iSeries Native)
      * Target Path: you can leave it as is but we recommend changing it to something similar to RPGiSeries<Id>
      * Name: you can leave it as is but we recommend changing it to something similar to RPGiSeries
   4. Select Generator and update the following properties:
      * Server Name: iSeries IP or Name
      * User: iSeries User
      * Password: iSeries Password
   5. Select Default Data Store, rigth click and Change Data Store: iSeries Native
2. In the DBMS options, type the name of the programs and data library to be created in the iSeries.
3. Select the transfer method to be used for the transfer. TCP/IP is recommended since it is the fastest according to the tests performed.
4. Once this has been setup, the model can be created in the iSeries.
5. Once the programs have been specified and generated, you must transfer them to the iSeries. For this, you must go to the Run or F5 option and select the programs you want to transfer. Thereupon, the programs are sent to the iSeries for them to be compiled. Once the programs have been transferred and compiled they can be executed from the iSeries commands line.
6. If you want to see the developer menu associated to this model, you must type  gx/gx Program\_Library\_name

#### [Going Live](#Going+Live)

Use the GXimpdbr command. For further details on how to execute this command, we suggest reading [here](https://wiki.genexus.com/commwiki/wiki?14125).

#### [See Also](#See+Also)

[RPG Generator Properties](https://wiki.genexus.com/commwiki/wiki?14000,,)


|  |
| --- |
| **Backlinks** |
| [GeneXus Standard Classes](https://wiki.genexus.com/commwiki/wiki?18859) |

---
