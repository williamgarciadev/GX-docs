---
title: "Populate Data property"
source_id: 46340
source_url: https://wiki.genexus.com/commwiki/wiki?46340
genexus_version: "18"
---

# Populate Data property

Allows controlling whether data population should be run as part of the build process.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Level:** [Environment](https://wiki.genexus.com/commwiki/wiki?7115)

### [Description](#Description)

By default, when a transaction has [Data Provider property in Transactions](https://wiki.genexus.com/commwiki/wiki?29597) = True and [Used to property](https://wiki.genexus.com/commwiki/wiki?29584) = 'Populate Data', a data population process is executed at build time.

In certain scenarios (e.g.: when the database is not reachable at build time), you may not want it to be executed. In that case, you can set this property to False.


|  |
| --- |
| **Backlinks** |
| [Toc:Automatic data population associated with Transactions](https://wiki.genexus.com/commwiki/wiki?32706) | [Used to property](https://wiki.genexus.com/commwiki/wiki?29584) |

---
