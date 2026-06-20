---
title: "Encrypt Offline Database property"
source_id: 35539
source_url: https://wiki.genexus.com/commwiki/wiki?35539
genexus_version: "18"
---

# Encrypt Offline Database property

[Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?20286) store the local database in the device's file system. By default, both Android and iOS encrypt the file system, so that the database file cannot be accessed without the users' passcode. An attacker wanting to access the local database will not be able to do so without the passcode, but the device's owner can read it easily.

This property is available in the [Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509) and adds an extra encryption layer so that not even the device's owner can read the local database.

## [Values](#Values)

|  |  |
| --- | --- |
| **False** (default) | The offline database won't be encrypted. |
| **True** | The offline database will be encrypted |

## [Description](#Description)

When the user installs the application and launches it for the first time, the offline database is created. If the **Encrypt Offline Database** is set to **True**, then a random encryption key is generated locally on the device and stored securely. That key is used to encrypt the local database.

### [Technology used](#Technology+used)

To encrypt the database we are using the [SQLCipher](https://wiki.genexus.com/commwiki/wiki?35632,,) open source project ([BSD-style license](https://www.zetetic.net/sqlcipher/license)), both in Android and iOS.  
More information at [External utilities used by Genexus generated iOS applications](https://wiki.genexus.com/commwiki/wiki?25150), [External utilities used by GeneXus generated Android applications](https://wiki.genexus.com/commwiki/wiki?25098).

### [Encryption key](#Encryption+key)

The encryption key is generated locally in the device, stored securely and never shown to the user.

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Objects** | [Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509) |
| **Generators** | iOS, Android |

### [Availability](#Availability)

This property is available since [GeneXus 15 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?34646,,).

## [Limitations](#Limitations)

As of the current version, the following limitations apply:

* Encrypting an existing application's database (or decrypting if already encrypted) does not work. If you want to do this, you need to install a new version of the application.
* Preloading the offline database is not supported if the database is encrypted.

## [See also](#See+also)

* [Offline Native Mobile applications architecture](https://wiki.genexus.com/commwiki/wiki?22221)
* [Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509)


|  |
| --- |
| **Backlinks** |
| [External utilities used by GeneXus generated Android applications](https://wiki.genexus.com/commwiki/wiki?25098) | [External utilities used by Genexus generated iOS applications](https://wiki.genexus.com/commwiki/wiki?25150) |
| [Offline Database Object properties](https://wiki.genexus.com/commwiki/wiki?25196) |

---
