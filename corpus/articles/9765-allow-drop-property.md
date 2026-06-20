---
title: "Allow Drop property"
source_id: 9765
source_url: https://wiki.genexus.com/commwiki/wiki?9765
genexus_version: "18"
---

# Allow Drop property

Adds a new grid row with content dragged from another control. The grid must have \_no\_ base table.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Controls:** FreeStyle Grid, Grid

### [Description](#Description)

Default value: False.

By setting this property to True, the user can drag information from another control to the grid, and it will be automatically loaded as a new line.

Since the loading is triggered from the client side and there is no base table, you have to save this information (for example, in a session) so as not to lose it in the next POST to the server.

The drag & drop operation can be implemented between controls in different web components.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [See Also](#See+Also)

[Developing Drag and Drop in Web Panels](https://wiki.genexus.com/commwiki/wiki?5579)  
[Allow Drag property](https://wiki.genexus.com/commwiki/wiki?9766)  
[Drag event in Web](https://wiki.genexus.com/commwiki/wiki?9642)  
[Drop event in Web](https://wiki.genexus.com/commwiki/wiki?9643)


|  |
| --- |
| **Backlinks** |
| [Allow Drag property](https://wiki.genexus.com/commwiki/wiki?9766) | [Developing Drag and Drop in Web Panels](https://wiki.genexus.com/commwiki/wiki?5579) | [Free Style Grid Properties](https://wiki.genexus.com/commwiki/wiki?9760) |

---
