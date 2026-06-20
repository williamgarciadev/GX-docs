---
title: "Allow Selection property"
source_id: 8680
source_url: https://wiki.genexus.com/commwiki/wiki?8680
genexus_version: "18"
---

# Allow Selection property

In a web application, it highlights the selected Grid row with a color for performing actions with it.

### [Syntax](#Syntax)

**control.** AllowSelection   

**Where:**  
*control*  
    Is the name of a grid control inserted in the form.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Controls:** [Grid](https://wiki.genexus.com/commwiki/wiki?24817)

### [Description](#Description)

In a [Grid](https://wiki.genexus.com/commwiki/wiki?24817), created within a [Web Panel Web Layout](https://wiki.genexus.com/commwiki/wiki?8132) or [Transaction Web Layout](https://wiki.genexus.com/commwiki/wiki?8057), enabling the Allow Selection property as True allows the end-user to mark a row inside the Grid to work with it. This automatically sets the [Allow Hovering property](https://wiki.genexus.com/commwiki/wiki?43237) to its default value of True as well.

Default value: False.

Multiple selection is not supported. Only the selection of one line at a time is allowed.

You can use the arrow keys *Up* and *Down* to move between rows. Take into account the following considerations when using the arrow keys:

* You can select the Grid row with the ENTER key.
* The Grid [OnLineActivate event](https://wiki.genexus.com/commwiki/wiki?12223) is triggered if it is programmed in the object; otherwise, the Object's [Enter event](https://wiki.genexus.com/commwiki/wiki?8167) (if programmed) is triggered.
* When both the mouse hover and arrow keys are used for movement, priority is given to the 'mouse hover' action.
* When the Allow Selection property is enabled, the arrow keys automatically serve to select the Grid item.
* By default, you must select at least one line (with the mouse) to be "located" in the Grid and iterate it with the arrows of the keyboard; Use *Grid.SetFocus ()* method to avoid having to make the first click.
* If you click outside the Grid or in any other field outside the Grid, the Grid is no longer iterable as it assumes that the focus has been removed.
* Sort in Client Side of Grids is not supported.

**Note**: The option to iterate within the grid using the arrow keys (Up and Down) has been available since [GeneXus 15 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?35908,,).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies both at runtime and at design time.

### [See Also](#See+Also)

[Allow Hovering property](https://wiki.genexus.com/commwiki/wiki?43237)  
[HoveringColor property](https://wiki.genexus.com/commwiki/wiki?8681)  
[SelectionColor property](https://wiki.genexus.com/commwiki/wiki?8682,,)


|  |
| --- |
| **Backlinks** |
| [Allow Hovering property](https://wiki.genexus.com/commwiki/wiki?43237) | [HoveringColor property](https://wiki.genexus.com/commwiki/wiki?8681) | [How to configure the Selection and Hovering behavior for Grids in the Abstract Layout](https://wiki.genexus.com/commwiki/wiki?29090) |
| [OnLineActivate event](https://wiki.genexus.com/commwiki/wiki?12223) |

---
