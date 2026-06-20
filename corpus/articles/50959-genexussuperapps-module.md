---
title: "GeneXusSuperApps Module"
source_id: 50959
source_url: https://wiki.genexus.com/commwiki/wiki?50959
genexus_version: "18"
---

# GeneXusSuperApps Module

The **GeneXusSuperApps** module is intended for developing [Super Apps](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?50900,,) with GeneXus.

### [Functionalities](#Functionalities)

The GeneXusSuperApps module provides several key functionalities that enable the effective development and management of Super Apps.

These functionalities include the ability to:

* Allow the Super App to query the [Mini App](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?50900,,) catalog in the [Mini App Center](https://wiki.genexus.com/commwiki/wiki?51290), filtering by several criteria.
* Allow a Super App to load a Mini App and transition to it.
* Manage the Mini App cache.

### [Module Components](#Module+Components)

The **GeneXusSuperApps** module is composed of two [External Object](https://wiki.genexus.com/commwiki/wiki?5669)s:

1. [MiniApps External Object](https://wiki.genexus.com/commwiki/wiki?58517)
2. [Provisioning External Object](https://wiki.genexus.com/commwiki/wiki?58519)

**Note**: The External objects are only available when running in a Super App. If the application is not a Super App or called from a Mini App, all methods will fail.

### [How to install the module](#How+to+install+the+module)

Install GeneXusSuperAppmoduleusing the [Manage Module References](https://wiki.genexus.com/commwiki/wiki?40172) dialog from the Knowledge Manager option (located in the GeneXus IDE toolbar).

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Generator:** | [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453) |

### [Availability](#Availability)

This module is available since [GeneXus 18 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?54240).

### [See Also](#See+Also)

[GeneXusMiniApps Module](https://wiki.genexus.com/commwiki/wiki?52076)


|  |
| --- |
| **Backlinks** |
| [GeneXus 18 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?54242) | [GeneXusMiniApps Module](https://wiki.genexus.com/commwiki/wiki?52076) | [Highlighted Mini Apps](https://wiki.genexus.com/commwiki/wiki?56095) |
| [HowTo: Create a Super App](https://wiki.genexus.com/commwiki/wiki?50906) | [Table of contents:Mini App Center](https://wiki.genexus.com/commwiki/wiki?51290) | [MiniApps external object in GeneXusSuperApps module](https://wiki.genexus.com/commwiki/wiki?58517) |
| [Native Mini App Cache Management and Update Policies](https://wiki.genexus.com/commwiki/wiki?56775) | [Provisioning external object in GeneXusSuperApps module](https://wiki.genexus.com/commwiki/wiki?58519) | [Provisioning.GetByFilters method](https://wiki.genexus.com/commwiki/wiki?57960) |

---
