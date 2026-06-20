---
title: "GXflow Process Definition"
source_id: 10153
source_url: https://wiki.genexus.com/commwiki/wiki?10153
genexus_version: "18"
---

# GXflow Process Definition

Through this application, process administrator users can visualize and control the process definitions existing in the system.

The following figure shows the Process Definition application interface:

`[imagen omitida: wiki id 52381]`

The following sections describe the different components making up this application.

### [Actions](#Actions)

* **Enable**: it allows enabling definitions that are currently disabled. Each process definition may have only one of its versions active, all the time. This implies that when a process definition version is enabled, the previously active version (if any) will be automatically disabled.
* **Disable**: it allows disabling process definitions. This implies that the users will not be able to create new processes of the disabled definitions. The processes that were created before the corresponding process definition was disabled are not affected in any aspect.
* **Toggle State**: It enables the process if it is disabled and disables the process if it is enabled.
* **View Diagram**: It displays the process diagram.

### [Process Definition Grid](#Process+Definition+Grid)

This grid has the following options:

`[imagen omitida: wiki id 52012]` It allows selecting the columns that should be visible.

`[imagen omitida: wiki id 52013]` It allows refreshing the grid.

It is possible to sort some columns by clicking on their title.

This grid has the following columns:

**Id**: Process Definition Id

**Name**: Process definition name.

**Version**: Process definition version number.

**State**: Process definition current state.

The possible statuses of a process definition are as follows:  
• Enabled: creating new processes based on the definition is possible.  
• Disabled: creating new processes based on the definition is not possible.

**Created**: Process definition creation date.

**Updated**: Date of the last process definition update.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [GXflow Process Manager](https://wiki.genexus.com/commwiki/wiki?17857) | [HowTo: Use GXflow Entry Point User Control](https://wiki.genexus.com/commwiki/wiki?10721) |

---
