---
title: "Default Master Page property"
source_id: 11597
source_url: https://wiki.genexus.com/commwiki/wiki?11597
genexus_version: "18"
---

# Default Master Page property

Sets the Web Master Panel to be used by default for every Web Panel object and every Transaction object.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** [Version](https://wiki.genexus.com/commwiki/wiki?7860)

### [Description](#Description)

The **Default Master Page** property is available at [version level](https://wiki.genexus.com/commwiki/wiki?7860) and by default, it is set with the 'RwdMasterPage' value, which is the name of a [Web Master Panel object](https://wiki.genexus.com/commwiki/wiki?10348) automatically created in every [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836).

In addition, every [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) and [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) offer the [Master Page property](https://wiki.genexus.com/commwiki/wiki?8156), which by default inherits and uses the [Web Master Panel object](https://wiki.genexus.com/commwiki/wiki?10348) set in the **Default Master Page** property(unless you explicitly change the [Master Page property](https://wiki.genexus.com/commwiki/wiki?8156) of the object).

### [Values](#Values)

**None** or any [Web Master Panel object](https://wiki.genexus.com/commwiki/wiki?10348) name defined in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691).

### [See Also](#See+Also)

[Master Page property](https://wiki.genexus.com/commwiki/wiki?8156)


|  |
| --- |
| **Backlinks** |
| [How to convert my application to make it responsive](https://wiki.genexus.com/commwiki/wiki?25214) | [Master Page property](https://wiki.genexus.com/commwiki/wiki?8156) | [Migration of KB with Carmine Theme to Unanimo Design System](https://wiki.genexus.com/commwiki/wiki?51821) |
| [My first Responsive Web Application](https://wiki.genexus.com/commwiki/wiki?25206) | [Web Form Defaults property](https://wiki.genexus.com/commwiki/wiki?25135) | [Category:Web Master Panel object](https://wiki.genexus.com/commwiki/wiki?10348) | [Work With for Web pattern](https://wiki.genexus.com/commwiki/wiki?25475) |

---
