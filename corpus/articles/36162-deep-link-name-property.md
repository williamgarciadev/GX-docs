---
title: "Deep Link Name property"
source_id: 36162
source_url: https://wiki.genexus.com/commwiki/wiki?36162
genexus_version: "18"
---

# Deep Link Name property

Indicates which resource of the deep link will be served by the entry panel when the application manages automatic deep linking scenario.

### [Description](#Description)

The value of this property must be the complete name of the resource, including suffix or prefix. For example:

* For web resources in the same Knowledge Base: *gx:<local\_resource\_name>* (selectable by clicking on `[imagen omitida: wiki id 36391]`)
* For .NET environment generated or external resources: *<resource\_name>.aspx*
* For JAVA environment generated or external resources:  *com.<knowlege\_base>.<resource\_name>*

#### Syntax

Deep Link Name  :=  <name> [ ; <name> ] \*

where <name> is the web resource which the panel will serve.

#### [Notes](#Notes)

* As of [GeneXus 15 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?36355,,) the following features have been added:
  + Multiple deep link names could be defined for the same panel.
  + Web resources selection in the same KB. In this case, a reference to this resource is created, so cross reference diagram includes it.
  + Deep Link name property is case insensitive

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [Samples](#Samples)

If we have a Smart Device Panel called SDViewProduct which serves the URL: http://www.mystore.com/viewproduct.aspx?1 (i.e. ViewProduct web panel)  
then:  
- The "http://www.mystore.com/" will be the value of [Deep Link Base URL property](https://wiki.genexus.com/commwiki/wiki?36161).  
- The SDViewProduct panel must have 'gx:ViewProduct' set on *Deep Link Name property*, or alternatively 'viewproduct.aspx'.*-*The SDViewProduct panel must have a parm rule for receiving the product id (i.e. parm(in:&ProductId)).

Refer to [HowTo: Deep Linking on Native Mobile](https://wiki.genexus.com/commwiki/wiki?36163) for detailed concepts.

### [Availability](#Availability)

This property is available since [GeneXus 15 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?35908,,).

### [Scope](#Scope)

**Objects:** Panel for Smart Devices, Work With for Smart Devices  
**Platforms:** Smart Devices(Android, IOS)


|  |
| --- |
| **Backlinks** |
| [HowTo: Deep Linking on Native Mobile](https://wiki.genexus.com/commwiki/wiki?36163) |

---
