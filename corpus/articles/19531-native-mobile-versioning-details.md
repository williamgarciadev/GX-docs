---
title: "Native Mobile Versioning Details"
source_id: 19531
source_url: https://wiki.genexus.com/commwiki/wiki?19531
genexus_version: "18"
---

# Native Mobile Versioning Details

Due to the architecture of the Native Mobile applications generated with GeneXus, it is possible to update only part of them when changes have to be distributed. This flexibility gives us an increased response speed.

The changes you make to the applications could affect the services layer, the metadata and/or other components packaged in the distributed binaries.

This document explains which changes in the Knowledge Base imply certain types of changes in the applications.

### [**Requirements**](#Requirements)

The following documents must be read first:

* [Online Native Mobile applications architecture](https://wiki.genexus.com/commwiki/wiki?14981)
* [HowTo: Version Your Native Mobile Application](https://wiki.genexus.com/commwiki/wiki?17223)

### [**Negligible change - Changes to the service layer without changing its interface**](#Negligible+change+-+Changes+to+the+service+layer+without+changing+its+interface)

Any change to the services (without changing its interface) can be made without updating the version of the binary sent to the store. Once distributed, they are automatically reflected in the connected applications.

Examples:

* Changes to the Start or Refresh event of a Native Mobile object.
* Changes to the REST procedures or REST Data Providers called from Native Mobile Objects Actions (everything except for changes to the parm).

### [**Minor change - Changes to the metadata**](#Minor+change+-+Changes+to+the+metadata)

Any change that affects the application's metadata requires updating the application that is executed on the devices. It can be done with a Minor Change and therefore the binaries sent to the store don’t have to be updated.

The connected applications detect the change, update the metadata, and keep on running with its new version.

Examples:

* New Action (new button). It can even call a new screen/layout.
* Changes to an Action (changes in parameters of calls to procs).
* Control is associated with a User Control that is already used in another part of the application in the previous version.
* Adding or deleting a column to a grid or any field to a screen.
* Changing a user control theme-class.
* Enabling/disabling Caching.
* Changing the Control property of the Dashboard.
* Changes to Themes.
* Change to the parm of a REST procedure or REST Data Provider called from Native Mobile Objects Actions.

### [**Major change - Changes to other components packaged in the binary**](#Major+change+-+Changes+to+other+components+packaged+in+the+binary)

Any change that doesn’t involve the metadata but affects the binaries requires a redistribution of the application to the store.

Examples:

* A new image (in Layout, Action, Background, Theme, etc.).
* A new User Control or External Object (a control starts referencing a User Control that is NOT used in the rest of the application, and therefore is not packaged).
* Changing the main object (so that instead of a dashboard it is an SD panel).
* Changing the GeneXus version.

### [**FAQ**](#FAQ)

* #### Q: *Is it applicable to both Android and Apple?* A: Yes, and this is verified when the application is executed or takes focus (comes to foreground).


|  |
| --- |
| **Backlinks** |
| [HowTo: Version Your Native Mobile Application](https://wiki.genexus.com/commwiki/wiki?17223) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |

---
