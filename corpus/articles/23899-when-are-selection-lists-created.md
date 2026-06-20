---
title: "When are selection lists created?"
source_id: 23899
source_url: https://wiki.genexus.com/commwiki/wiki?23899
genexus_version: "18"
---

# When are selection lists created?

[Selection List](https://wiki.genexus.com/commwiki/wiki?23894) are created during specification time, more precisely:

* when generating for **Web**: upon specifying transactions (in the build), the web panel (or work panel) GX00nn objects will appear, with nn being a sequential number. For the example shown in [Selection List](https://wiki.genexus.com/commwiki/wiki?23894), web panels GX0010 and GX0020 will be created, each implementing a selection list of customers and countries respectively.

* when generating for **Smart Devices**: upon specifying the Work With pattern for Smart Devices applied to the transaction with a FK (in our case, the Customer transaction), the Panel for Smart Devices GX0020sd object will be created, equivalent to the GX0020 object for web/win (in the example mentioned, the selection list of countries, which corresponds to the *CountryId* FK). In Smart Devices, selection lists are created only for FKs.

We can disable the creation of selection lists in web generators by modifying the value of the Environment/Generator property: *Generate prompt programs*, whose predefined value is *Yes*. We can also modify it at the version level, which will have an effect on all generators.

**Note:** The Smart Devices generator does not include this property yet, so it can be turned off only at the whole Environment level or at the version level.


|  |
| --- |
| **Backlinks** |
| [Selection List](https://wiki.genexus.com/commwiki/wiki?23894) |

---
