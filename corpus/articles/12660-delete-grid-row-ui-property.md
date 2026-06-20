---
title: "Delete grid row UI property"
source_id: 12660
source_url: https://wiki.genexus.com/commwiki/wiki?12660
genexus_version: "18"
---

# Delete grid row UI property

To set that you want to alternate the two images DeleteRowImage and UndeleteRowImage for the first column in Transactions grids.

### [Values](#Values)

|  |  |
| --- | --- |
| **Alternating images** | This is the default value. |
| **Context menu - Delete** | This value would be used for backward compatibility only. It provides a contextual menu for deleting lines, but it is available as deprecated. |

### [Description](#Description)

Each row of a grid in a Transaction has a column with a control that alternates the images: DeleteRowImage and UndeleteRowImage.

The images alternate when the user clicks the mouse on the control or, if it the control has the focus, by pressing the space bar.

If you are working with Evolution 1 version a or higher, the default value for this property is "Alternating Images" and it is the recommended.

The "Context menu - Delete" value is only available for backward compatibility and is to provide a contextual menu for deleting lines.
