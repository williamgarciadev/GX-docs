---
title: "Expand Bounds Directions property"
source_id: 37138
source_url: https://wiki.genexus.com/commwiki/wiki?37138
genexus_version: "18"
---

# Expand Bounds Directions property

Indicates in which directions the control can be expanded.

## [Values](#Values)

|  |  |
| --- | --- |
| **Top** | Expand in the top edge direction. |
| **Left** | Expand in the left edge direction. |
| **Bottom** | Expand in the bottom edge direction. |
| **Right** | Expand in the right edge direction. |

## [Description](#Description+)

Values for this property must be set separated by a comma (","). It must have at least one value set (by default, it has all of them set).

For example, if  
Expand Bound Directions := Bottom, Right  
the runtime behavior will be as follows.

|  |  |
| --- | --- |
| **Portrait** | **Landscape** |
|  |  |

## [Notes](#Notes)

* [Expand Bounds property](https://wiki.genexus.com/commwiki/wiki?37136) with *None* value is equivalent to do not have (hypothetically) any value set in this property.

## [Run-time/Design-time](#Run-time%2FDesign-time)

This property applies only at design-time.

## [Scope](#Scope)

**Controls:** [Grid control](https://wiki.genexus.com/commwiki/wiki?24817), [Tab control](https://wiki.genexus.com/commwiki/wiki?29986), [Canvas control](https://wiki.genexus.com/commwiki/wiki?22452), [Table control](https://wiki.genexus.com/commwiki/wiki?6001)  
**Platforms:** Smart Devices(IOS)

## [Availability](#Availability)

This property is available as of [GeneXus 15 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?36778,,)

## [See also](#See+also)

* [Expand Bounds property](https://wiki.genexus.com/commwiki/wiki?37136)
* [Expand Bounds Limit property](https://wiki.genexus.com/commwiki/wiki?37137)
* [Default Layout Orientation property](https://wiki.genexus.com/commwiki/wiki?23398)


|  |
| --- |
| **Backlinks** |
| [Expand Bounds Limit property](https://wiki.genexus.com/commwiki/wiki?37137) | [Expand Bounds property](https://wiki.genexus.com/commwiki/wiki?37136) | [Layout Behavior properties group](https://wiki.genexus.com/commwiki/wiki?37135) |

---
