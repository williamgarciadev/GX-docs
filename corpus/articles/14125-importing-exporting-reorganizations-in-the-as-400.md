---
title: "Importing/Exporting Reorganizations in the AS/400"
source_id: 14125
source_url: https://wiki.genexus.com/commwiki/wiki?14125
genexus_version: "18"
---

# Importing/Exporting Reorganizations in the AS/400

#### Introduction

This document describes the exportation facilities for the creation/reorganization of the database done by GeneXus in the AS/400 environment.

From the GeneXus point of view, the creation and reorganization processes are equal, this is why this document uses the word "reorganization" to cover both concepts.

The facility to export a reorganization was implemented intending to satisfy two types of requirement brought forward by GeneXus users:

1. The facility to develop the application in a machine different than the production one. This need was brought forward by companies that have in their possesion one machine for production and one machine for development, and software houses.
2. Make available a test environment in the AS/400. This was mostly asked for by companies that only have one machine handling development and production.

#### The Importing/Exporting Basic Principles

Each time a reorganization is performed a save file is generated containing all the necessary objects needed to execute the reorganization process again in the same machine (over different libraries) or in a different machine.

The generated save file always has the same name (GXSAVF) and it is stored in the programs library.

The exportation process consists in saving (e.g.: on tape), moving (to another library) or renaming the generated save file after each reorganization. This a user task.

The importation process, on the other hand, consists in restoring the objects from the save file and executing them. To do this, the GXIMPDBR command is made available by GeneXus.

It is not necessary the compiler (RPG or COBOL) in the production machine, the exported objects are already compiled.

#### Exporting the reorganization

The reorganization exportation is a semi-automatic process. GeneXus automatically saves all the required objects for the reorganization, this is the last step taken for each reorganization. If the reorganization cannot be saved, the process is considered to be incomplete.

Once the reorganization has finished, the user should follow the procedure to transfer the save file (GXSAVF) to the machine where the production model is (it may be the same machine).

#### Importing the reorganization

The process of importing the reorganization consists in restoring the objects from the save file and executing them over the production libraries. To do this, the following command must be invoked (GXIMPDBR):

GX/GXIMPDBR PGMLIB(*pgmlib*) SAVLIB(*opgmlib*) DEV(\*SAVF) SAVF(*savflib*/*savfname*)

**where:**

*pgmlib*  
   Is the target programs library (production library). In case, this library does not exist, GeneXus will automatically create it and another screen will be displayed where you will be prompted for the data library name.

*opgmlib*  
   Is the name of the development library where the reorganization to be imported was generated.

*savflib*  
   Is the name of the library where the save file is stored.

*savfname*  
   Is the name of the save file (usually named GXSAVF)

Command GXIMPDBR can be submitted (except for the case when a new database is created, if the command is submitted and the data library doesn’t exist, the command cancels).

The following considerations should taken into account, though:

* The user who executes the command doesn’t need to have ALLOBJ authorization.
* Because the command is submitted, there is no output to the screen. You may see the job status in the Job List.
* Even in the cases when the command is not submitted, there is no screen output when the job ends the following message is display: "This database reorganization was just executed successfully".

#### Requirements

To import a reorganization it is necessary to have \*ALLOBJ authorization (e.g.: QSECOFR). This is necessary because the restoration process makes use of some RSTOBJ command parameters that require this authorization.

If the importation is performed in a different machine than the development one, both machines must have the same version of the OS/400 operating system, or at least, the development machine OS/400 version must be prior to the production machine one.


|  |
| --- |
| **Backlinks** |
| [Generating in COBOL](https://wiki.genexus.com/commwiki/wiki?14124) | [Generating in RPG](https://wiki.genexus.com/commwiki/wiki?14095) |

---
