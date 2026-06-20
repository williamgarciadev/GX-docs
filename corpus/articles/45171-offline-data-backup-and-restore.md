---
title: "Offline Data backup and restore"
source_id: 45171
source_url: https://wiki.genexus.com/commwiki/wiki?45171
genexus_version: "18"
---

# Offline Data backup and restore

To solve a completely offline SD application scenario, it is useful to have the possibility of backing-up and then restoring the application's local database.

### [GeneXus.SD.Offline.DataBase external object](#GeneXus.SD.Offline.DataBase+external+object)

It is an external object defined in the [GeneXus Core module](https://wiki.genexus.com/commwiki/wiki?31268)

#### [Backup Method](#Backup+Method)

This method performs a backup of the local database and all its resources including:

* the .sqlite file
* all binary files referenced from the database (blobs, images, etc.)
* the synchronization hashes
* the database's MD5 hash value.

**Syntax**

```
&Result = DataBase.Backup(&Path)
```

Where:

* &Result is based on the ResultCode domain (see below)
* &Path is a String variable with the URI of the backup file

**Example**

```
&path = Directory.ExternalFilesPath + "/backups/DB15012020.zip"
&result = Database.Backup(&path)
```

#### [Restore Method](#Restore+Method)

Performs a restore of a previously created backup.

It leaves the database operational so that the user can keep using the application after the restoration.

**Syntax**

```
&Result = DataBase.Restore(&Path)
```

Where:

* &Result is based on the ResultCode domain (see below)
* &Path is a String variable with the URI of the backup file

**Example**

```
&path = Directory.ExternalFilesPath + "/backups/DB15012020.zip"
&result = Database.Restore(&path)
```

#### [ResultCode domain](#ResultCode+domain)

The domain used to return the operation result.

Valid values are:

| Code | Message |
| --- | --- |
| 0 | Success |
| 1 | Application is not offline |
| 2 | Path is not correct / Backup file not found |
| 3 | Database structure does not match |
| 9 | Internal error |

### [Considerations](#Considerations)

#### [Concurrency](#Concurrency)

The backup and restore operation should not be performed while there are other operations accessing or modifying the database. The behavior in those cases is undefined and will probably create some inconsistencies.

#### [Synchronization](#Synchronization)

The backup and restore operations should be used with care if the application also has synchronization. Since the records added or deleted by the restore operation are not sent to the server, there could be cases where information is lost. Also when restoring a backup, the synchronization hashes restored on the device may no longer exist in the server (depending on the [Minimum Time Between Table Purges property](https://wiki.genexus.com/commwiki/wiki?31160)), which may be a problem when the device tries to synchronize again.


|  |
| --- |
| **Backlinks** |
| [Toc:Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22228) |
| [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) | [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) |

---
