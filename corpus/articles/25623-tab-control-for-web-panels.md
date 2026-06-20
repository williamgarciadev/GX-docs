---
title: "Tab control for Web Panels"
source_id: 25623
source_url: https://wiki.genexus.com/commwiki/wiki?25623
genexus_version: "18"
---

# Tab control for Web Panels

The Tab control is used to display a set of controls grouped in different tabs.

It is supported in [Abstract Layout](https://wiki.genexus.com/commwiki/wiki?25209)s.

Each tab has an implicit table inside that may be either a [Responsive Table](https://wiki.genexus.com/commwiki/wiki?24961) or a common [Table control](https://wiki.genexus.com/commwiki/wiki?6001) containing the controls in such tab page.

## Properties

|  |  |
| --- | --- |
| **Control Name** | Defines the name of the Tab control. |
| **Item Control Name** | Defines the name of each Tab page. |

### ["TabControl Appearance" group](#%22TabControl+Appearance%22+group)

|  |  |
| --- | --- |
| **Tab Control Class** | Sets the [Theme](https://wiki.genexus.com/commwiki/wiki?6420) class associated with the Tab control. |
| **Tab Control Visible** | Hides or shows the Tab control. |

### ["Tabs Behavior" group](#%22Tabs+Behavior%22+group)

|  |  |
| --- | --- |
| **History Management** | View [History Management property](https://wiki.genexus.com/commwiki/wiki?42228) documentation. |

### ["TabPage Appearance" group](#%22TabPage+Appearance%22+group)

|  |  |
| --- | --- |
| **Caption** | Text to be shown on the tab strip. |

#### 

## [Runtime (only) Properties](#Runtime+%28only%29+Properties)

|  |  |
| --- | --- |
| **ActivePage** | Active page index (first tab index is 1).   It's a property used to ask whether a page is active or not. |
| **ActivePageControlName** | Active page control name. |

## Methods

|  |  |
| --- | --- |
| **SelectTab(index)** | Sets, as active, the tab page indicated as parameter. |
| **HideTab(index)** | Hides the tab page indicated as a parameter. |
| **ShowTab(index)** | Shows the tab page indicated as a parameter. |

## Events

|  |  |
| --- | --- |
| **TabChanged** | Triggers an event upon selecting any tab page. |

## How to use the control

Drag the control from the toolbox to the abstract layout, as shown in the figure below:

`[imagen omitida: wiki id 25626]`

## How to configure the Tab Control style

Only for GeneXus 15, see : [How to configure the Tab Control style on the WEB](https://wiki.genexus.com/commwiki/wiki?31026)

### [Note](#Note)

The Tab control is used in the [Work With for Web pattern](https://wiki.genexus.com/commwiki/wiki?25475) when it has been generated using the [Abstract Layout](https://wiki.genexus.com/commwiki/wiki?25209). It is used specifically in View Objects, as shown below:

`[imagen omitida: wiki id 25627]`


|  |
| --- |
| **Backlinks** |
| [Accessible Name Custom property](https://wiki.genexus.com/commwiki/wiki?55469) | [Accessible Name property](https://wiki.genexus.com/commwiki/wiki?55454) | [Col Span property](https://wiki.genexus.com/commwiki/wiki?8752) |
| [Category:Common Controls](https://wiki.genexus.com/commwiki/wiki?5928) | [GeneXus Markup Language (GXML)](https://wiki.genexus.com/commwiki/wiki?46876) | [gx-elevation property](https://wiki.genexus.com/commwiki/wiki?28180) |
| [gx-focused-class property](https://wiki.genexus.com/commwiki/wiki?51849) | [History Management property](https://wiki.genexus.com/commwiki/wiki?42228) | [How to configure the Tab Control style on the WEB](https://wiki.genexus.com/commwiki/wiki?31026) | [Is Slot property](https://wiki.genexus.com/commwiki/wiki?51306) |
| [KB:OnlineShop (Shopping cart sample)](https://wiki.genexus.com/commwiki/wiki?27158) | [Row Span property](https://wiki.genexus.com/commwiki/wiki?8828) | [Tab control for Panels](https://wiki.genexus.com/commwiki/wiki?29986) | [Web Abstract Editor](https://wiki.genexus.com/commwiki/wiki?24795) |
| [Work With for Web pattern](https://wiki.genexus.com/commwiki/wiki?25475) |

---
