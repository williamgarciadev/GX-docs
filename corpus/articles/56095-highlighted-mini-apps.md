---
title: "Highlighted Mini Apps"
source_id: 56095
source_url: https://wiki.genexus.com/commwiki/wiki?56095
genexus_version: "18"
---

# Highlighted Mini Apps

The Highlighted Mini App functionality offers a simple way to showcase specific Mini Apps within the Super App. By highlighting a Mini App, you enhance its visibility for users.

This feature is especially valuable for highlighting important or time-sensitive content, promotions, or key services.

To highlight a Mini App, you need to carry out two main actions:

**1.** Configure the highlighted [Mini Apps](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?50900,,) in the [Mini App Center](https://wiki.genexus.com/commwiki/wiki?51290).  
**2.** Retrieve the list of highlighted Mini Apps from the Super App.

These Mini Apps will appear as highlighted in a [Super App](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?50900,,) for a period of time.

### [1. Configuration in the Mini App Center](#1.+Configuration+in+the+Mini+App+Center)

To perform these actions, you must have a user with a **Provisioning Administrator**, **Organization Administrator***,* or **Super App Administrator** role.

To access this option, click on **Highlighted Mini Apps**from the Main Menu of the [Mini App Center](https://wiki.genexus.com/commwiki/wiki?51290). All currently highlighted Mini Apps will appear there. To add a new one, click on the **NEW HIGHLIGHT** button.

`[imagen omitida: wiki id 58068]`

#### [Required data](#Required+data)

The following data is required:

* **Super App:**Select, among the available options, the Super App where the Mini App will be highlighted.
* **Mini App**: Select, among the available options, the Mini App to be highlighted.
* **From Date**: The date from which you want the Mini App to be highlighted.
* **To Date:** The date until which you want the Mini App to be highlighted.

If there is more than one Mini App highlighted for a Super App, **position** can also be specified.

To access this option, click on **Highlighted Mini Apps**from the Main Menu of the Mini App Center.

`[imagen omitida: wiki id 58072]`

To rearrange Mini Apps positions, use the arrows in the first column.

Mini Apps will be displayed in the same order as they appear in the Mini App Center.

In this menu, the **status** of the Highlighted Mini App is also specified.

There are two available options:

* **Enable**: When the highlighted Mini App is Online.
* **Scheduled**: When the Mini App will be highlighted at a later date.

History of the highlighted Mini Apps is also available.

To access this option, click on **Highlighted Mini Apps**from the Main Menu of the Mini App Center and click on **HISTORY**.

`[imagen omitida: wiki id 58073]`

This will show the History of the highlighted Mini Apps from a certain Super App.

`[imagen omitida: wiki id 58074]`

The status can be:

* **Cancelled:**When the highlight was forced to end. This action can be done when editing a highlight.
* **Completed:**When the highlight time was up.

### [2. Retrieving highlighted Mini Apps](#2.+Retrieving+highlighted+Mini+Apps)

To get the highlighted Mini Apps that are active within the time frame, use one of the following methods:

* [GetFeatured method](https://wiki.genexus.com/commwiki/wiki?50959): This method returns the Mini Apps that are currently highlighted and ready to be shown to users. It ensures that the Mini Apps meeting the criteria of being within the active time frame will be properly displayed in the Super App.
* [Provisioning.GetByFilters method](https://wiki.genexus.com/commwiki/wiki?57960): This method allows you to retrieve highlighted Mini Apps using specific filters. Use the condition highlighted Equal "1" or highlighted Equal "true" to filter the highlighted Mini Apps.


|  |
| --- |
| **Backlinks** |
| [Table of contents:Mini App Center](https://wiki.genexus.com/commwiki/wiki?51290) | [Provisioning external object in GeneXusSuperApps module](https://wiki.genexus.com/commwiki/wiki?58519) |

---
