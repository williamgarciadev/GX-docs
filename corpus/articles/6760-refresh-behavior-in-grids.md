---
title: "Refresh Behavior in grids"
source_id: 6760
source_url: https://wiki.genexus.com/commwiki/wiki?6760
genexus_version: "18"
---

# Refresh Behavior in grids

If the Automatic Refresh property is set to "No", user action is needed to make the grid load the records that satisfy the conditions entered.  
Depending on whether the grid has a base table or not, there are two possible user actions to make the grid refresh after entering the filters:

* Pressing the Enter key (only if the grid has a base table)
* Clicking on a button or image to trigger the search.

### [Refresh behavior after entering grid filters (only if the grid has a base table)](#Refresh+behavior+after+entering+grid+filters+%28only+if+the+grid+has+a+base+table%29)

If the grid has a base table, the filters in the form (variables related with conditions) are automatically identified, so that when the user changes any of these variables, that action is detected, and it is assumed that the user wants to apply the filters immediately .

Of course we are assuming that the Automatic Refresh object property is set to "No".

The behavior is as follows:

1. If the user presses Enter immediately after changing any variable condition, a Refresh of the page will be executed, loading all the filtered records. The Enter event won't be executed even if it is defined.
2. If the user clicks on a control associated with a user event immediately after changing a variable condition, the user event will be executed and a Refresh will be executed afterwards. This is for the purpose of forcing the grid to be loaded with the filtered records. Note that although the user event is executed on the client side (without the need for evaluating in the server), the Refresh event will cause the conditions to be evaluated in the server and the grid to be loaded as expected.

Important Note:

If a web control is associated with an Enter Event, and the user clicks on that control after entering any variable condition, the following will happen:

1. The Refresh event will be executed
2. The Enter event won't be executed (so that the event associated with the clicked control won't be executed)
3. The grid will be loaded with the records which satisfy the conditions.

### [Refresh behavior after entering grid filters (grids which do not have a base table)](#Refresh+behavior+after+entering+grid+filters+%28grids+which+do+not+have+a+base+table%29)

In this case, changes in filters related with the grid cannot be detected, so the user's intention to load the grid from the entered filters cannot be known in advance. The following possibilities are available to make the grid load after entering the filters:

1. Pressing the enter key if the Enter Event is defined in the source of the webpanel. This is due to the [Enter Key Behavior](https://wiki.genexus.com/commwiki/wiki?6761)

Note that in this case the Enter Event code is also executed. The Enter Event is not generally used for this purpose.

2. Clicking on a button or image to trigger the search after entering the filters.

The user event associated to that button or image has to refresh the grid by taking into account the filters entered. Thus, one possibility is to associate it to the Refresh event.

`[imagen omitida: wiki id 7345]`

`[imagen omitida: wiki id 7346]`

Another possibility is that we use the refresh command inside the user event associated to that button. Suppose the user event is "Search", the event may be as follows:

Event "Search"  
     refresh  
EndEvent

Note that if the event executes on the server side, it forces a refresh at any rate. See [this link](https://wiki.genexus.com/commwiki/wiki?6563,,) to clarify that idea.

### [Notes](#Notes)

- The refresh on a Grid based on variables loses the state of it.   
- The refresh on a Grid based on SDT, only loses the state of the blob items.

See also: [Automatic Refresh Grid](https://wiki.genexus.com/commwiki/wiki?6744)


|  |
| --- |
| **Backlinks** |
| [Automatic Grid Refresh](https://wiki.genexus.com/commwiki/wiki?6744) | [Enter Key Behavior](https://wiki.genexus.com/commwiki/wiki?6761) |

---
