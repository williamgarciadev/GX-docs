---
title: "Tools - Options - Build"
source_id: 24030
source_url: https://wiki.genexus.com/commwiki/wiki?24030
genexus_version: "18"
---

# Tools - Options - Build

You can configure certain features related to Specification and Generation tasks (among others) by selecting **Tools > Options**in the main GeneXus Menu and clicking on the **Build node**.

### [After Build section](#After+Build+section)

If desired, the Specifier and Generator can be run in parallel mode.

|  |  |
| --- | --- |
| * **Close Generator property** | Indicates whether to close the Generator background process after building. Default value: "False". |
| * **Close Specifier property** | Indicates whether to close the Specifier background process after building. Default value: "False". |

### [Misc section](#Misc+section)

|  |  |
| --- | --- |
| * **Background Specification property** | The Background Specification feature is used to speed up the building process as it allows you to specify the objects when they are saved and reuse this specification during the build process. |
| * **Build with this only property** | This property makes it possible to force the generation of a non-main object and has two possible values: “Force generation” indicates that even though the object doesn't have any changes that require generation, it will be generated anyway. The “Check” (default) value will have the object checked for changes, and if changes are found it will be generated; otherwise, it won't. |
| * **Call tree for Build property** | This property allows the call tree in the Build process to be configured. One possible value is "Stop on Main Objects", which indicates that after F5/Build only those objects that have been changed since the last build and may be reached by the "StartUp Object/Developer Menu" will be re-generated, provided there isn’t a Main object between them. The "Full" value does not cut the call tree, even when there’s a Main object between the "StartUp Object" and the object that was modified (both the Main and the modified object are generated). |
| * **Concurrent Generation property** | When this option is not activated (False value), upon performing the Build, all the necessary elements are specified first. The generator will start working on the generation of whatever is needed only after the specifier has completed its task. When the option is activated (True value), the specifier and the generator will run concurrently. As the specifier processes objects and generates its specs, it “informs” the generator for the latter to generate such objects. This allows for a better use of PCs with more than one core. The default value is False. |
| * **Concurrent Generation Instances property** | Sets the number of concurrent generator instances. |
| * **Concurrent Specification Instances property** | Sets the number of concurrent specifier instances. |
| * **Detailed Navigation property** | The detailed navigation report includes more information than the standard one. It offers analysts more information on how the program will be generated (i.e.: triggered actions). The drawback is that it takes longer to generate this type of navigation information. The default value is False. |
| * **Specification Type property** | Verifies changes occurred in the program source and tables used by the object. If changes are detected, then a "Full" specification of the object is to be performed. It is very important to bear in mind that the date of the machine must always be correct. Otherwise, the mechanism will not work, or worse yet: it will function incorrectly. The default value is "Full".  This option has been removed as of GeneXus 17 Upgrade 8. See [SAC #50624](https://www.genexus.com/en/developers/websac?data=50624) for more details. |

### [See Also](#See+Also)

[Multiple Concurrent Generator and Specifier Instances](https://wiki.genexus.com/commwiki/wiki?25808)


|  |
| --- |
| **Backlinks** |
| [Background Specification](https://wiki.genexus.com/commwiki/wiki?24026) | [Call tree for build option](https://wiki.genexus.com/commwiki/wiki?18996) | [Category:IDE Configuration Options](https://wiki.genexus.com/commwiki/wiki?6772) |
| [Multiple Concurrent Generator and Specifier Instances](https://wiki.genexus.com/commwiki/wiki?25808) |

---
