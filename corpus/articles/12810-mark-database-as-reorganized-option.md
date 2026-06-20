---
title: "Mark Database as Reorganized Option"
source_id: 12810
source_url: https://wiki.genexus.com/commwiki/wiki?12810
genexus_version: "18"
---

# Mark Database as Reorganized Option

#### [Where is this option?](#Where+is+this+option%3F)

Tools Menu - Advanced - Mark Database as Reorganized Option

#### [What does this option do?](#What+does+this+option+do%3F)

This option internally updates the DB schema without running the reorganization process. If this option is used and no changes to DB schema were made (i.e. there is no pending reorganization) the following message appears: “Current environment database is already up to date”.

If changes to DB structure were made since the last reorganization was run (i.e. there is a pending reorganization) the following message appears:  “Current environment database schema is not up to date. If you choose Yes, GeneXus will assume that the environment database already has the expected schema and you will not be able reorganize it later. Once the developer chooses "Yes" the DB schema is internally updated without running the reorganization programs and that reorganization cannot be run later.

#### [Scenarios](#Scenarios)

Once changes are made to DB structure (e.g. new transactions were added, attributes were changed, etc.) a [DB reorganization process](https://wiki.genexus.com/commwiki/wiki?5288) is run in order to update the DB schema. There are, however, scenarios where developers do not want or need this process to be run, as the DB schema is updated, for example, by another application. A list of possible scenarios follows:

* A new developer is added to a team where all developers point to the same test Database.

The "Mark database as reorganized" option should be selected after executing the [New Knowledge Base From Server option](https://wiki.genexus.com/commwiki/wiki?10625,,).

* All environments in the application point to the same Database.

This is the case of the same application generated for different generators (Java, .Net, Ruby, etc.) but using the same DBMS. Only one of the environments actually executes the reorganization.

#### [Notes](#Notes)

* This process is similar to the process known as “copy model” (cpymdl).
* You should use this option instead of setting the [Reorganize server tables property](https://wiki.genexus.com/commwiki/wiki?8955) to No in most of the scenarios above. It is faster as there is no Impact Analysis Report.
