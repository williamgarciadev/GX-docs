---
title: "Multidex Build property"
source_id: 35886
source_url: https://wiki.genexus.com/commwiki/wiki?35886
genexus_version: "18"
---

# Multidex Build property

Specifies whether or not we want to make use of a special build option in Android called MultiDex.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Description](#Description)

This enables building apps with over the limit of 64k methods (which can be reached easily when using many third-party extensions like Facebook, Twitter, etc).  
The default value is **True**.

This feature avoids building error:

UNEXPECTED TOP-LEVEL EXCEPTION:  
com.android.dex.DexIndexOverflowException: method ID not in [0, 0xffff]: **65536**

#### [Notes](#Notes)

* As of [GeneXus 15 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?34646,,) this property belongs to [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817). In previous upgrades can be found at [Android specific properties](https://wiki.genexus.com/commwiki/wiki?31449).
* Up to [GeneXus 16 upgrade 1](https://wiki.genexus.com/commwiki/wiki?40782,,) the default value was False.

### [Availability](#Availability)

This property is available since [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?27605,,).


|  |
| --- |
| **Backlinks** |
| [Android specific properties](https://wiki.genexus.com/commwiki/wiki?31449) | [Gradle Options property for Android Generator](https://wiki.genexus.com/commwiki/wiki?36363) | [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817) |

---
