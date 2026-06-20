---
title: "Is it possible to modify Selection Lists?"
source_id: 23900
source_url: https://wiki.genexus.com/commwiki/wiki?23900
genexus_version: "18"
---

# Is it possible to modify Selection Lists?

Though [Selection List](https://wiki.genexus.com/commwiki/wiki?23894)s are initially created by GeneXus, they may be modified like any [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) or [Panel object](https://wiki.genexus.com/commwiki/wiki?24829). Once this happens, GeneXus is no longer in charge of it, so it will not be updated when the associated table is modified (as opposed to what occurs with default lists).

If at a given time you regret having assumed a selection list, you may delete it so that in the following specification of a Transaction or WW using it, it will be created again automatically and it will return under GeneXus control again.  
  
It is possible to modify the Layout, add events, etc., ensuring that the ‘Enter’ event in Web Panels, or the ‘Select’ event in Panels, maintains its feature of returning, in the output parameter, the value selected by the user.

Upon the need to receive and/or return more parameters in a selection list, in addition to redefining its [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862), it is necessary to use the [Prompt rule](https://wiki.genexus.com/commwiki/wiki?6863) to invoke it explicitly from the objects that need it, with the new parameters.


|  |
| --- |
| **Backlinks** |
| [Selection List](https://wiki.genexus.com/commwiki/wiki?23894) |

---
