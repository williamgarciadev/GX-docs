---
title: "Create Database Options property"
source_id: 9016
source_url: https://wiki.genexus.com/commwiki/wiki?9016
genexus_version: "18"
---

# Create Database Options property

Specifies if the Database Creation/Reorganization proccess will have a user intervention or will take other actions in the Reorganization proccess.

### [Description](#Description)

#### [Values](#Values)

The possible parameter values of the creation/reorganization proccess are:

|  |  |
| --- | --- |
| **-nogui** | The user intervention is not allowed (dialogs will be turned off). |
| **-force** | The control on the .GEN and .EXP files is avoided (not recomended). The creation/reorganization is forced. |
| **-noverifydatabaseschema** | Do not verify the database schema in the creation/reorganization proccess. If, for any reason you do not want the database schema to be verified, use this parameter when running the creation/reorganization. |
| **-recordcount** | This parameter will count records in all tables to be created/reorganized, display the results and stop. This may be used to estimate how long the creation/reorganization may take. |
| **-ignoreresume** | In some failure recovery situations you may want to start over and run the creation/reorganization process from the very beginning. Use of this parameter makes the creation/reorganization process to execute while ignoring any resume information. |
| **-donotexecute** | It's usefull for environments where you need the creation/reorganization to be generated/compiled but not executed and after the impact is done you want to perform a build all and deploy creation/reorganization and application programs to another place. |

There are two preferences where this value can be set: "Create Database Options" and "Reorganization Options" for reorganizations that are run directly from GeneXus.

The default value for the property is: **-nogui  -noverifydatabaseschema**

#### [Note](#Note)

Commands can be combined; you must separe each option with a whitespace as is shown in the *Create Database Options default value*. For example, if you want to combine the *nogui*, *force* and *ignoreresume* options, the property should be set as:

```
-nogui -force -ignoreresume
```

Both properties are Generator Properties and you can found them under Build Process/Advanced.

The next reorganization operation will use the property value change.

### [See Also](#See+Also)

[Features of Reorganizations](https://wiki.genexus.com/commwiki/wiki?3154)  
[Reorganization Options property](https://wiki.genexus.com/commwiki/wiki?36454)


|  |
| --- |
| **Backlinks** |
| [Export Reorganization](https://wiki.genexus.com/commwiki/wiki?34476) | [Features of Reorganizations](https://wiki.genexus.com/commwiki/wiki?3154) | [Reorganization Options property](https://wiki.genexus.com/commwiki/wiki?36454) |

---
