---
title: "Selection Type property (GeneXus 18 Upgrade 2 or prior)"
source_id: 54490
source_url: https://wiki.genexus.com/commwiki/wiki?54490
genexus_version: "18"
---

# Selection Type property (GeneXus 18 Upgrade 2 or prior)

Defines the behavior of the Grid's rows when they are selected.

### [Values](#Values)

|  |  |
| --- | --- |
| **Keep selection while executing** | The selection ends when the Default Action ends. |
| **Keep until new selection** | The selection ends when another selection is made. |
| **No selection** | The tapped row will not be selected. |
| **Platform Default** | Default value. Uses the platform default behavior. |

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Controls:** [Grid](https://wiki.genexus.com/commwiki/wiki?24817)

### [Description](#Description)

#### [**Values**](#Values)

|  |  |
| --- | --- |
| **Value** | **Description** |
| **Platform Default** | Default value. Uses the platform default behavior. |
| **No Selection** | The tapped row will not be selected.  • The grid's Highlighted Background color is shown while the user interacts with the control.  • The [Default Selected Item Layout](https://wiki.genexus.com/commwiki/wiki?22556) is not going to be shown even if it is defined or not.  • The [SelectionChanged Event](https://wiki.genexus.com/commwiki/wiki?36236) will not be triggered.    **Note:** Until [GeneXus 15 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?34646,,), the **No Selection** value was known as **Autodeselect**. |
| **Keep Selection While Executing** | The selection ends when the [Default Action](https://wiki.genexus.com/commwiki/wiki?20424) ends.  • If the [Default Selected Item Layout](https://wiki.genexus.com/commwiki/wiki?22556) is defined it is shown, if not, the grid's Highlighted Background color is shown.  • This value only makes sense when the [Default Action](https://wiki.genexus.com/commwiki/wiki?20424) or [SelectionChanged Event](https://wiki.genexus.com/commwiki/wiki?36236) of the Grid are defined.  • If an item is selected, and the user selects it again, the item is still going to be selected and the [Default Action](https://wiki.genexus.com/commwiki/wiki?20424) of the Grid is executed again. |
| **Keep Until New Selection** | The selection ends when another selection is done.  • If the [Default Selected Item Layout](https://wiki.genexus.com/commwiki/wiki?22556) is defined it is shown, if not, the grid's Highlighted Background color is shown.  • This value only makes sense when the [Default Selected Item Layout](https://wiki.genexus.com/commwiki/wiki?22556) is defined.  • If an item is selected, and the user selects it again, the item is going to be deselected and the [Default Action](https://wiki.genexus.com/commwiki/wiki?20424) is executed again. |

#### [**Platform Default values**](#Platform+Default+values)

##### [**For Apple:**](#For+Apple%3A)

* If the [Default Action](https://wiki.genexus.com/commwiki/wiki?20424) is defined, then the **Keep Selection While Executing** value is the default.
* If the [Default Action](https://wiki.genexus.com/commwiki/wiki?20424) is not defined and the [Default Selected Item Layout](https://wiki.genexus.com/commwiki/wiki?22556) is defined, then the **Keep Until New Selection** value is the default.

##### [**For Android:**](#For+Android%3A)

* If the [Default Action](https://wiki.genexus.com/commwiki/wiki?20424) is defined, then the **No Selection** value is the default.
* If the [Default Action](https://wiki.genexus.com/commwiki/wiki?20424) is not defined and the [Default Selected Item Layout](https://wiki.genexus.com/commwiki/wiki?22556) is defined, then the **Keep Until New Selection** value is the default.

#### [**For [Multiple Selection](https://wiki.genexus.com/commwiki/wiki?16149)**](#For+wiki%3F16149%2CGrids%2Bwith%2BMultiple%2BSelection%2Bfor%2BNative%2BMobile%2BApplications+Multiple+Selection)

* Will behave such as the **Keep Until New Selection** value.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

Take as an example the [EventDay](https://wiki.genexus.com/commwiki/wiki?22550,,) sample KB and see how different values of the Selection Type property changes the behavior of a row when it is selected. For instance in the Sessions Grid at the List level of the Work With Session:

Using the Auto Deselect value the Highlighted Background color is shown only when the user presses the row, after that the row is deselected automatically:

|  |  |  |
| --- | --- | --- |
|  |  |  |

Using the Keep Selection While Executing value, the Highlighted Background color is shown until the Default Action ends:

|  |  |  |
| --- | --- | --- |
|  |  |  |

### [Availability](#Availability)

This property is available since [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?20247,,).

### [See Also](#See+Also)

[Grids with Multiple Selection for Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?16149)  
[Default Selected Item Layout property](https://wiki.genexus.com/commwiki/wiki?22556)  
[Multiple Layouts in Panels](https://wiki.genexus.com/commwiki/wiki?23489)
