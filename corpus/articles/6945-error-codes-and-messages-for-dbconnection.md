---
title: "Error Codes and Messages for DBConnection"
source_id: 6945
source_url: https://wiki.genexus.com/commwiki/wiki?6945
genexus_version: "18"
---

# Error Codes and Messages for DBConnection

|  |  |  |
| --- | --- | --- |
| **Code** | **Message** | **Comments** |
| 0 | No error | No error occurred. |
| 1 | Unknown error | An unknown error occurred. This may happen when you ask for a description for an error code which does not exist. |
| 2 | No GeneXus Datastore attached | A method or property has been used on a variable which does not have an associated datastore. This is solved by previously assigning the DatastoreName property. |
| 3 | Internal error: Function call failed | The method or property has received an error when communicating a value to the data access. Usually, it is due to a non-valid or out-of-range parameter value. |

### [See Also](#See+Also)

[DBConnection Data Type](https://wiki.genexus.com/commwiki/wiki?6923)


|  |
| --- |
| **Backlinks** |
| [Connect method](https://wiki.genexus.com/commwiki/wiki?7086) | [Disconnect method](https://wiki.genexus.com/commwiki/wiki?7101) | [ErrCode Property](https://wiki.genexus.com/commwiki/wiki?6930) |
| [ErrDescription Property](https://wiki.genexus.com/commwiki/wiki?6931) | [ErrDisplay Property](https://wiki.genexus.com/commwiki/wiki?6929) |

---
