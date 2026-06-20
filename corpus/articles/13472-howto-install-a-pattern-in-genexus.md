---
title: "HowTo: Install a Pattern in GeneXus"
source_id: 13472
source_url: https://wiki.genexus.com/commwiki/wiki?13472
genexus_version: "18"
---

# HowTo: Install a Pattern in GeneXus

In order to install a [Pattern](https://wiki.genexus.com/commwiki/wiki?2814) in GeneXus, you need to follow these instructions:

**1.** Copy the complete folder name associated to the pattern to the **<GX\_Installation\_Path>\Packages\Pattern** folder.

**2.** Run GeneXus with the **/install** option, for example: "C:\Program Files\ARTech\GeneXus\GeneXusXev2\genexus /install", in order to register new the components.

**3.** The next time you start GeneXus, you should find the new component listed in the Extensions Manager.

If the pattern was not correctly installed, the following message will appear when opening a KB:

```
Knowledge Base at 'C:\SalesKB' contains items that GeneXus doesn't know how to handle and will therefore be inaccessible.
It is likely that the Knowledge Base has been previously opened with a GeneXus installation which had extensions that are not present in the current one.
These items are:
* 'PatternName' - 'PatternName' (GUID 59daae39-26ff-4c45-bd11-7e9671b088c5)
   Provided by 'Pattern Provider' (GUID df0eb164-d030-4b53-b022-0ea225fb61d6).
Working on this Knowledge Base may lose information related to these unknown items.
Do you want to continue?"
```
