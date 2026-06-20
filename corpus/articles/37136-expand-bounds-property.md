---
title: "Expand Bounds property"
source_id: 37136
source_url: https://wiki.genexus.com/commwiki/wiki?37136
genexus_version: "18"
---

# Expand Bounds property

Indicates how much the content can be expanded.

## [Values](#Values)

|  |  |
| --- | --- |
| **Background Only** | Default value. The container control will expand only its background, not its content. Embedded controls can be expanded and allow scroll on them (if the control admits it). |
| **Background & Content** | The container control will expand both background and content, allowing embedded controls be positioned on the expanded area. |
| **None** | The container control won't be expanded. This value disables [Expand Bounds Directions property](https://wiki.genexus.com/commwiki/wiki?37138) and [Expand Bounds Limit property](https://wiki.genexus.com/commwiki/wiki?37137). |

## [Description](#Description+)

Let's analyze the behavior in each case running a simple app on an iPhone X, focused on landscape mode where *unsafe areas* (green color) appear on both sides of the screen (because of the presence of the notch). Suppose we've got a WorkWithDevicesCountry object whose List node is defined as the following image. We'll display the effect of varying Expand Bounds property for the Main Table on the layout.

`[imagen omitida: wiki id 37183]`

### [None value](#None+value)

The control is not expanded and remains in the safe area of the screen.

`[imagen omitida: wiki id 37165]`

### [Background only](#Background+only)

The background of the control (Main Table) is expanded beyond the unsafe area but not its content (Grid's rows content  ).  
This fact is evidenced by remaining the original padding on both sides on the screen (appreciable only on the left, but also it's on the right) only respect the flag icon.

`[imagen omitida: wiki id 37166]`

### [Background & content](#Background+%26+content)

The background of the control (Main Table) and its content (Grid's rows content) are expanded beyond the unsafe area.   
This fact is evidenced by the absence of paddings.

`[imagen omitida: wiki id 37167]`

## [Run-time/Design-time](#Run-time%2FDesign-time)

This property applies only at design-time.

## [Scope](#Scope)

**Controls:** [Grid control](https://wiki.genexus.com/commwiki/wiki?24817), [Tab control](https://wiki.genexus.com/commwiki/wiki?29986), [Canvas control](https://wiki.genexus.com/commwiki/wiki?22452), [Table control](https://wiki.genexus.com/commwiki/wiki?6001)  
**Platforms:** Smart Devices(IOS)

## [Availability](#Availability)

This property is available as of [GeneXus 15 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?36778,,)

## [See also](#See+also)

* [Expand Bounds Limit property](https://wiki.genexus.com/commwiki/wiki?37137)
* [Expand Bounds Directions property](https://wiki.genexus.com/commwiki/wiki?37138)


|  |
| --- |
| **Backlinks** |
| [Expand Bounds Directions property](https://wiki.genexus.com/commwiki/wiki?37138) | [Expand Bounds Limit property](https://wiki.genexus.com/commwiki/wiki?37137) | [Toc:Flex Layout Container](https://wiki.genexus.com/commwiki/wiki?35354) |
| [Layout Behavior properties group](https://wiki.genexus.com/commwiki/wiki?37135) |

---
