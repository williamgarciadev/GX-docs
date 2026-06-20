---
title: "Connect to server property"
source_id: 8536
source_url: https://wiki.genexus.com/commwiki/wiki?8536
genexus_version: "18"
---

# Connect to server property

Allows controlling at which moment the generated programs establish connection with the server.

### [Values](#Values)

|  |  |
| --- | --- |
| **At first request** | The application will try to establish connection immediately after sending the first request to the server. This option is recommended for applications that do not access the server very frequently. In this case, the user could work with the application without establishing connection with the server only if the application does not require this to be done. This is the default value. |
| **At application startup** | The application will try to establish connection as a part of the initialization process (before the main object is displayed). This option is recommended in applications that are (totally or almost totally) server dependent. |

### [Description](#Description)

#### [Note:](#Note%3A)

If an application is generated with the At application Startup option and later it is changed to the At first request value, you must force generate all programs. Total regeneration is not necessary when changing the value from At first request to At application startup.

#### [Technologies to Access Data:](#Technologies+to+Access+Data%3A+)

ADO.NET, JDBC

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply changes made by this property, do a Build with this Only of the object.

### [Scope](#Scope)

**Platforms:** Web(.Net, Java)


|  |
| --- |
| **Backlinks** |
| [DBMS Options for JDBC Technology](https://wiki.genexus.com/commwiki/wiki?9070) | [UserId function](https://wiki.genexus.com/commwiki/wiki?8518) |

---
