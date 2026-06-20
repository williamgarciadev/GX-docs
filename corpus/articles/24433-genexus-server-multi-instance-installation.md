---
title: "GeneXus Server multi-instance installation"
source_id: 24433
source_url: https://wiki.genexus.com/commwiki/wiki?24433
genexus_version: "18"
---

# GeneXus Server multi-instance installation

This document explains how to install more than one instance of [GeneXus Server](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?31337,,).

### [How to install another GeneXus Server instance](#How+to+install+another+GeneXus+Server+instance)

More than one GeneXus Server instance can be installed on the same server machine.

In fact, all instances will need only one license to be installed on the same server. Please refer to [Compatibility for GeneXus Server Licenses](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?21802,,) for more information on how to share a license between different versions and upgrades.

Using the Setup you will be able to install another GeneXus Server instance as described in the [GeneXus Server Installation Manual](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?25890,,).

`[imagen omitida: wiki id 58820]`

**Notes**:

* GeneXus Server cannot use centralized licenses (installed on a license server and shared with other machines); that is, a license may only be used locally on the server machine where it is installed.
* It is important to make sure each application pool associated with a GeneXus Server installation uses the same Windows user so that the same local license is shared.
