---
title: "After function"
source_id: 8321
source_url: https://wiki.genexus.com/commwiki/wiki?8321
genexus_version: "18"
---

# After function

**Warning**: This function is maintained for backward compatibility. It is strongly recommended to use the [Triggering Events](https://wiki.genexus.com/commwiki/wiki?6840) instead of this function.

Returns a True/False if a specified event or action occurred in a Transaction.

### [Syntax](#Syntax)

**After**(*Event* | *Action*)

**Where:**  
*Event*  
   Specifies a valid event; the possible values are: [Insert](https://wiki.genexus.com/commwiki/wiki?8326), [Update](https://wiki.genexus.com/commwiki/wiki?8327) or [Delete](https://wiki.genexus.com/commwiki/wiki?8328).

*Action*  
   Describes a possible action; the possible values are: [Confirm](https://wiki.genexus.com/commwiki/wiki?8282), [Trn](https://wiki.genexus.com/commwiki/wiki?8160), [Att](https://wiki.genexus.com/commwiki/wiki?8324) or [Level(att)](https://wiki.genexus.com/commwiki/wiki?8285).

**Type returned:**  
Boolean (True or False)

### [Scope](#Scope)

**Objects:**[Transaction](https://wiki.genexus.com/commwiki/wiki?1908)

### [Description](#Description)

Returns True if a specified event or action has taken place in a Transaction. This event may be triggered because a Transaction's execution has passed a certain Level, a certain attribute has been entered, a Transaction Action has occurred, or the whole Transaction has finished.

GeneXus automatically realizes where and when a rule must be executed. However, you may force GeneXus to execute a given rule after one of the above events.

**Note**: When an After function is included in a Rule condition, the Rule will be triggered only immediately after the event occurs and nowhere else.

### [Compatibility](#Compatibility)

It’s important to highlight that this function is maintained for backward compatibility reasons. It is highly recommended that you use the [Triggering Events](https://wiki.genexus.com/commwiki/wiki?6840) instead of **After**(*Event* | *Action*) functions.

### [See Also](#See+Also)

[Triggering Events](https://wiki.genexus.com/commwiki/wiki?6840)  
[After Attribute function](https://wiki.genexus.com/commwiki/wiki?8324)


|  |
| --- |
| **Backlinks** |
| [After Action Triggering event](https://wiki.genexus.com/commwiki/wiki?8284) | [AfterComplete Triggering event](https://wiki.genexus.com/commwiki/wiki?8160) | [AfterLevel Event](https://wiki.genexus.com/commwiki/wiki?8285) |

---
