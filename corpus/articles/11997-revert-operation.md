---
title: "Revert Operation"
source_id: 11997
source_url: https://wiki.genexus.com/commwiki/wiki?11997
genexus_version: "18"
---

# Revert Operation

The Revert operation is used to restore a [Development Version](https://wiki.genexus.com/commwiki/wiki?5684) to a previously known state (a [Frozen Version](https://wiki.genexus.com/commwiki/wiki?5681)). It overwrites the target with the source content. All information in the target is lost and replaced with information in the source.

The Revert operation can be performed from a Development Version as well as from a Frozen Version.  
   
The command always includes two versions: a frozen version and a development version, and what it does is to make the state of the development version equal to the state of the frozen version.  
   
If the Revert operation is activated from a frozen version, the development version reverted is that which is superordinated to the frozen version. When it is performed from a development version, the frozen version used is that which is superordinated to the development version. Note that, as a consequence, the Revert command cannot be invoked from the main development version because it doesn't have a superordinated version.

`[imagen omitida: wiki id 12000]`
