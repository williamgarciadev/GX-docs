---
title: "Server-side Events in Native Mobile Applications"
source_id: 24234
source_url: https://wiki.genexus.com/commwiki/wiki?24234
genexus_version: "18"
---

# Server-side Events in Native Mobile Applications

Server-side events, also known as System Events, include Start, Refresh, and Load.

Leaving aside the [caching](https://wiki.genexus.com/commwiki/wiki?18602) (for now you will assume no caching is enabled), two invocations to the server have to be done to load each layout on a device: one loads the plain part (also known as fixed-part), and the other loads the grid (if any). This means that two base tables could be involved (the fixed-part and the grid). Therefore, two [data providers](https://wiki.genexus.com/commwiki/wiki?5270) are internally created by GeneXus (shown in the navigation report). The first one will include in it the logic programmed into the Start and Refresh events, and the second one the logic of the Load event, respectively (as well as the [conditions and orders](https://wiki.genexus.com/commwiki/wiki?24805) specified in the "Conditions" selector).

### [Start event](#Start+event)

[Start event](https://wiki.genexus.com/commwiki/wiki?8043) is executed the first time that a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) or a [Work With pattern and Work With object](https://wiki.genexus.com/commwiki/wiki?15974) node is opened on a device (further ahead you will see a Detail with a multiple-section case). It is not executed again unless the panel is excited and opened again.

### [Refresh event](#Refresh+event)

[Refresh event](https://wiki.genexus.com/commwiki/wiki?8195,,) is executed following the Start (unless it is not the first time, in which case Start is not executed, and Refresh is). Since the navigation of the fixed part of the form and the grid are separated, each will have (if attributes) its [Base Table](https://wiki.genexus.com/commwiki/wiki?6347). Therefore, the Refresh event accesses the fixed-part base table to get the plain information. Note that if there is no record meeting the conditions, then the Refresh event code will not run.

Grid information cannot be accessed inside the Refresh, except when the grid is based on an SDT.

### [Load event](#Load+event)

[Load event](https://wiki.genexus.com/commwiki/wiki?8188) is the last of the system events executed. It is executed only if there is a grid on the layout. When the Grid has a [Base Table](https://wiki.genexus.com/commwiki/wiki?6347), the Load event is executed as many times as registers of the base table exist, and if it is based on variables it is executed once, just as in a web panel. If the grid is based on an SDT variable, the Load event is not executed.

#### [Are variables persistent?](#Are+variables+persistent%3F)

Remember that, as in any GeneXus object, variables defined within the objects are global inside it. So, a variable assigned into the Refresh event will be visible inside Load. However, the values assigned in the client will not be seen by the server. This is a temporary limitation. For values assigned in client to persist, you will have to call, inside the client event, a rest procedure (on web server) to save values in a session variable, in order to later get them in the Refresh or Load (for example, if the client event executes a Refresh command immediately). The same applies to variables inserted in the layout (as opposed to what occurs in the case of web panels).

### [Example](#Example)

To understand this better, see an example:

Suppose you have a [Menu object](https://wiki.genexus.com/commwiki/wiki?16321) that allows you to list all the real estate properties managed by a Real Estate Agency (calling the List node of the WWSD related to Property Transaction). As you call a List, its layout will have a grid, so the two data providers mentioned above will be created and executed for retrieving the data to be loaded onto the device screen.

`[imagen omitida: wiki id 24235]`

What happens when the user calls this List of Properties?

1. User taps on the menu item “List of Properties”, and the corresponding event is executed on the client-side (calling WorkWithDevicesProperty in its List node).
2. A call to the Data Provider (REST request) is executed in order to retrieve the info corresponding to the plain part of the List.
3. If the info has to be retrieved from the database, a call to it is done.
4. Database retrieves the information asked by the Data Provider on Web Server.
5. Data Provider retrieves to the client (REST response) the data needed to load the plain part of the layout.
6. The plain part of the layout is drawn on the device screen.
7. Steps 2 to 6 are executed, for the Data Provider retrieving the grid information.

It is important to point out the difference between a panel (like List or Detail) and a web panel: the fixed part and grid navigations are separated, and the screen corresponding to the fixed part is drawn independently from what occurs on the grid. If there are attributes, there will be two base tables. So, if you want to have all the loaded real estate properties displayed on the fixed part of the grid, you cannot do the same you would do in a web panel: add a &total variable set to 0 in the refresh, which is increased in the Load event every time it is run.

`[imagen omitida: wiki id 24259]`

The fixed part of the Work With will be drawn before invoking the Data Provider that returns the lines, and therefore the variable will always show value 0. There is another problem with caching, but you can read [Native Mobile Applications Caching](https://wiki.genexus.com/commwiki/wiki?18602).

So, a solution to show the number of records could be to add a For Each command in the Refresh event in order to count them.

## [Load example](#Load+example)

You have to load a variable on the grid, depending on whether the Property received more than a specific number of visits, in order to classify it as one of the most visited. In addition, if the Property was listed during the last couple of days, you want to display an image indicating it is a new property

`[imagen omitida: wiki id 24255]`

To do so, see the [Load example](https://wiki.genexus.com/commwiki/wiki?24296).


|  |
| --- |
| **Backlinks** |
| [Back event](https://wiki.genexus.com/commwiki/wiki?24950) | [Calls to Elements in Work Withs from Native Mobile Applications Events](https://wiki.genexus.com/commwiki/wiki?17160) | [Determining the Base Table for the Form and Grid in Panels](https://wiki.genexus.com/commwiki/wiki?24807) |
| [Directory Data Type Static properties](https://wiki.genexus.com/commwiki/wiki?27388) | [Do Case command](https://wiki.genexus.com/commwiki/wiki?31605) | [Event Triggering Order in Panels](https://wiki.genexus.com/commwiki/wiki?17614) |
| [GUID data type](https://wiki.genexus.com/commwiki/wiki?31772) | [Load event](https://wiki.genexus.com/commwiki/wiki?8188) | [Msg function](https://wiki.genexus.com/commwiki/wiki?31635) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |
| [Category:Native Mobile Applications Events](https://wiki.genexus.com/commwiki/wiki?17042) | [Network external object](https://wiki.genexus.com/commwiki/wiki?31310) | [Refresh command in Panels](https://wiki.genexus.com/commwiki/wiki?25060) |

---
