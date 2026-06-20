---
title: "Selection Type property"
source_id: 24120
source_url: https://wiki.genexus.com/commwiki/wiki?24120
genexus_version: "18"
---

# Selection Type property

Defines the behavior of the Grid's rows when they are selected.

### [Values](#Values)

|  |  |
| --- | --- |
| **Keep selection while executing** | The selection ends when the Default Action ends. |
| **Keep until new selection** | The selection ends when another selection is made. |
| **No selection** | The tapped row will not be selected. |
| **Platform Default** | Default value. Uses the platform default behavior. |

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)  
**Controls:** [Grid](https://wiki.genexus.com/commwiki/wiki?24817), [Tabular Grid](https://wiki.genexus.com/commwiki/wiki?54449)

### [Description](#Description)

This property sets the behavior of the Grid's rows when they are selected.

The default value is **Platform Default**.

Below are described the possible values the property can take.

|  |  |
| --- | --- |
| **Value** | **Description** |
| **Platform Default** | Default value. Uses the platform's default behavior. **For Apple:**   * If the [Default Action property](https://wiki.genexus.com/commwiki/wiki?20424) is configured, the **Keep Selection While Executing** value is the default. * If the [Default Action property](https://wiki.genexus.com/commwiki/wiki?20424) is not configured and the [Default Selected Item Layout property](https://wiki.genexus.com/commwiki/wiki?22556) is set, the **Keep Until New Selection** value is the default.   **For Android:**   * If the [Default Action property](https://wiki.genexus.com/commwiki/wiki?20424) is configured, the **No Selection** value is the default. * If the [Default Action property](https://wiki.genexus.com/commwiki/wiki?20424) is not configured and the [Default Selected Item Layout property](https://wiki.genexus.com/commwiki/wiki?22556) is set, the **Keep Until New Selection** value is the default. |
| **No Selection** | The tapped row will not be selected.    • The grid's Highlighted Background color is shown while the user interacts with the control.  • The [Default Selected Item Layout property](https://wiki.genexus.com/commwiki/wiki?22556) will not be shown regardless if it is defined or not.  • The [SelectionChanged Event](https://wiki.genexus.com/commwiki/wiki?36236) will not be triggered.  **Note**: Until [GeneXus 15 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?34646,,), the **No Selection** value was known as **Autodeselect**. |
| **Keep Selection While Executing** | The selection ends when the [Default Action](https://wiki.genexus.com/commwiki/wiki?20424) ends.    • If the [Default Selected Item Layout property](https://wiki.genexus.com/commwiki/wiki?22556) is configured, this value is shown; otherwise, the grid's Highlighted Background color is shown.  • This value only makes sense when the [Default Action property](https://wiki.genexus.com/commwiki/wiki?20424) or [SelectionChanged Event](https://wiki.genexus.com/commwiki/wiki?36236) of the Grid are defined.  • If an item is selected, and the user selects it again, the item is still going to be selected and the [Default Action property](https://wiki.genexus.com/commwiki/wiki?20424) of the Grid is executed again. |
| **Keep Until New Selection** | The selection ends when another selection is done.    • If the [Default Selected Item Layout property](https://wiki.genexus.com/commwiki/wiki?22556) is configured this is shown; otherwise, the Grid's Highlighted Background color is shown.  • This value only makes sense when the [Default Selected Item Layout property](https://wiki.genexus.com/commwiki/wiki?22556) is set.  • If an item is selected, and the user selects it again, the item is deselected and the [Default Action property](https://wiki.genexus.com/commwiki/wiki?20424) is executed again. |

#### 

**Note**: For [Grids with Multiple Selection for Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?16149) the behavior will correspond to the **Keep Until New Selection** value.

####

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

Take as an example the [EventDay](https://wiki.genexus.com/commwiki/wiki?22550,,) sample KB and see how different values of the Selection Type property change the behavior of a row when it is selected. For instance, in the Sessions Grid at the List level of the Work With Session:

When using the No Selection value the Highlighted Background color is shown only when the user taps on the row; after that, the row is deselected automatically:

`[imagen omitida: wiki id 54499]`

When using the Keep Selection While Executing value, the Highlighted Background color is shown until the Default Action ends:

`[imagen omitida: wiki id 54500]`

### [See Also](#See+Also)

[Grids with Multiple Selection for Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?16149)  
[Default Selected Item Layout property](https://wiki.genexus.com/commwiki/wiki?22556)  
[Multiple Layouts in Panels](https://wiki.genexus.com/commwiki/wiki?23489)


|  |
| --- |
| **Backlinks** |
| [HowTo: Use a Matrix Grid Control](https://wiki.genexus.com/commwiki/wiki?25139) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |
| [Select method](https://wiki.genexus.com/commwiki/wiki?36234) | [Select method (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54486) | [Selection Type property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54490) | [SelectionChanged Event](https://wiki.genexus.com/commwiki/wiki?36236) |
| [SelectionChanged Event (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54483) | [Tabular Grid control](https://wiki.genexus.com/commwiki/wiki?54449) |

---
