---
title: "Offline Database reorganization"
source_id: 27121
source_url: https://wiki.genexus.com/commwiki/wiki?27121
genexus_version: "18"
---

# Offline Database reorganization

As mentioned in the document [Offline Database Object Table selection](https://wiki.genexus.com/commwiki/wiki?23561), this object is in charge of selecting the tables that the device is going to use in order to work Offline. But how and when are these tables created in the device? How are they reorganized when the table model changes?

The objective of this document is to answer these questions.

### [Smart Devices Impact Analysis](#Smart+Devices+Impact+Analysis)

Once the Offline Database object determines the selected Tables, GeneXus makes a Smart Devices Impact Analysis that shows all the selected tables and their creation statements.

`[imagen omitida: wiki id 27122]`

### [When is this impact analysis called?](#When+is+this+impact+analysis+called%3F)

This impact analysis is always made after the first Build operation of the application when Offline architecture is selected.

After that, it is called in the following situations:

* On every model change: Any modification to model Create/Update/Delete tables or attributes.
* When table references change: For example, when your application makes reference to a table that was not referenced before.
* Every time the Rebuild All action is executed.
* Manually: Using the [Create Offline Database](https://wiki.genexus.com/commwiki/wiki?27123) action from the Build menu.

### [Reorganization files](#Reorganization+files)

After the Impact Analysis is done, reorganization files are created for each Smart Device generator enabled for the [Native Mobile Generator](https://wiki.genexus.com/commwiki/wiki?14451).

These files include the routines to create the database in the device once the application is installed.

### [Offline Local Database Reorganization](#Offline+Local+Database+Reorganization)

The Offline local database is created when the application is launched for the first time in the device. In order to do this, the reorganization files must be created as they include the database creation routines.

After that, every time the offline database model changes, the reorganization files re-create the local database tables from scratch1, **losing all their existing data**. The exception here is the *GXPendingEvents* table, where the pending events (those that were not syncrhonized) will be copied into the new database, in order to be sent  to the server in the next sync process. To learn more, read [SynchronizationEventsAPI external object](https://wiki.genexus.com/commwiki/wiki?23606,,)

1 To know whether the database needs to be re-created, the MD5 of the ReorganizationScript.txt is compared.

### [Important considerations](#Important+considerations)

1. It is very important that you have the Reorganization files generated and compiled before you run your application in the device. Otherwise, several errors may occur, and your application may even crash as a result of not having these files.
2. As Reorganization files are generated for every Smart Device generator that is enabled, when enabling a new Smart Device generator, the Impact Analysis may not be done and therefore the reorganization files may not be created. In summary, every time you enable a new Smart Device generator you must run a Rebuild All or the [Create Offline Database](https://wiki.genexus.com/commwiki/wiki?27123) action manually.
3. Having more than one Offline main object is not supported, as only one reorganization program is kept by each Smart Device Generator.

### [See also](#See+also)

* [Create Offline Database](https://wiki.genexus.com/commwiki/wiki?27123)
* [Offline Database Object Table selection](https://wiki.genexus.com/commwiki/wiki?23561)
* [Offline Database Object Navigation Report](https://wiki.genexus.com/commwiki/wiki?23568)
* [Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509)


|  |
| --- |
| **Backlinks** |
| [Create Offline Database](https://wiki.genexus.com/commwiki/wiki?27123) | [Category:Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509) | [Toc:Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22228) |

---
