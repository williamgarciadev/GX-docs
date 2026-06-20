---
title: "GXflow Authentication Preference Group"
source_id: 13226
source_url: https://wiki.genexus.com/commwiki/wiki?13226
genexus_version: "18"
---

# GXflow Authentication Preference Group

This menu allows you to set the schema to be used to authenticate users.

`[imagen omitida: wiki id 52827]`

### [Preferences](#Preferences)

* #### [**Authentication Schema:**](#Authentication+Schema%3A)

  + **GXflow**: Standard schema. The verification is performed on the users defined in the system.
  + **[Windows](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?20437,,)**: The user currently logged into Windows operating system is used.
  + **External**: A customized mechanism is used to verify the users.
  + **GeneXus Access Manager:** The GAM mechanism is used to verify the users.
    - It is recommended to keep this property set to "Default" so that the authentication type is determined by the "Repository default authentication type" property in GAM.

* **Default value**: GXflow

* **Authentication Program**: Only visible if the authentication schema is external.

<Procedure\_name> must be as shown below:

.NET: <Class Name Fullyqualified>,<Assembly Name>

Ex: “GeneXus.Programs.aauthenticationProcedure,aauthenticationProcedure.dll”

JAVA: procedure class name

The procedure specified here has to be as follows:

**parm(**in:*&UserId*, in:*&UserPassword*, out:*&error***)**;

where:

*&UserId*

is based on the WorkflowUserId domain

- *&UserPassword*

is based on WorkflowPassword domain

- *&error* is Numeric (4): returns the result of the user evaluation. The engine also verifies if the user is nominated.

Possible values to return are as follows:

0: Valid user and password.

9998: Incorrect user or password

9995: Access denied

**Note:** You must be responsible for compiling the procedure.


|  |
| --- |
| **Backlinks** |
| [Table of contents:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [Workflow Client Settings](https://wiki.genexus.com/commwiki/wiki?15097) |

---
