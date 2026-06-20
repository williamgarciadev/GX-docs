---
title: "Default Selected Item Layout property"
source_id: 22556
source_url: https://wiki.genexus.com/commwiki/wiki?22556
genexus_version: "18"
---

# Default Selected Item Layout property

Indicates which layout of a Grid row must be displayed when it is tapped on, to show more or less information, and also to enable new actions only available when the row is selected.

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Controls:** [Grid](https://wiki.genexus.com/commwiki/wiki?24817)

### [Samples](#Samples)

Consider the [EventDay](https://wiki.genexus.com/commwiki/wiki?22550,,) application, where there is a WorkWithDevicesSpeakers object with a Grid in which all the event’s speakers are loaded.

Suppose that after selecting a speaker from the grid –by tapping on it–, you want instead of calling the Detail, showing a brief biography of the speaker, and an arrow-shaped image to access further information on the speaker if desired.

|  |  |  |
| --- | --- | --- |
| **Normal** |  | **"Cimas Alejandro" selected** |
|  |  |  |

Therefore, you need two layouts for each item or line of the grid: One that is used when the line is not selected, and another one to use when it is selected.

To create a new layout on the Grid of the Speakers List level, you have to:

* Click on the upper right corner of the Grid.
* In the menu that is displayed click on “Add New Item Layout”.

`[imagen omitida: wiki id 22568]`

* Enter the name desired for the new Layout (i.e., "SelectedItem"). Note: In this example, the default layout is also renamed as “Item”.
* Organize the Layout as wanted (Add/Move/Remove elements). In this example, a brief biography of the speaker is shown, and an arrow-shaped image to access further information on the speaker if desired.

`[imagen omitida: wiki id 22569]`

* Select the Grid of the Speakers List level and set its [Default Action property](https://wiki.genexus.com/commwiki/wiki?20424) as“<none>”, so that it will not go to the Detail level when we tap on a row. Next, set the [Default Selected Item Layout property](https://wiki.genexus.com/commwiki/wiki?22556) as “SelectedItem”, which is the layout created.

`[imagen omitida: wiki id 22570]`

* Run (F5) and see the result.

Additionally, to continue having access to the Detail level, create the following event on the arrow-shaped image of the SelectedItem layout:

```
Event Image1.Tap
    WorkWithDevicesSpeaker.Speaker.Detail(SpeakerId)
EndEvent
```

Consideration: For the [Default Selected Item Layout property](https://wiki.genexus.com/commwiki/wiki?22556) to work, the Grid’s Default Layout must be different from the layout configured in that property.

### [Availability](#Availability)

This property is available since [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?20247,,).

### [See Also](#See+Also)

[EventDay KB](https://wiki.genexus.com/commwiki/wiki?22550,,)  
[Multiple Layouts per Row](https://wiki.genexus.com/commwiki/wiki?22545)  
[Work With pattern and Work With object](https://wiki.genexus.com/commwiki/wiki?15974)  
[Work With Pattern Settings](https://wiki.genexus.com/commwiki/wiki?17353)  
[Work With Detail Node](https://wiki.genexus.com/commwiki/wiki?15985)  
[Work With List Node](https://wiki.genexus.com/commwiki/wiki?15984)


|  |
| --- |
| **Backlinks** |
| [Default Selected Item Layout property](https://wiki.genexus.com/commwiki/wiki?22556) | [Deselect method](https://wiki.genexus.com/commwiki/wiki?36235) |
| [Deselect method (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54487) | [Grids with Selection By Code for Panels](https://wiki.genexus.com/commwiki/wiki?35987) |
| [Multiple Layouts per Row](https://wiki.genexus.com/commwiki/wiki?22545) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Select method](https://wiki.genexus.com/commwiki/wiki?36234) | [Select method (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54486) |
| [Selection Type property](https://wiki.genexus.com/commwiki/wiki?24120) | [Selection Type property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54490) |

---
