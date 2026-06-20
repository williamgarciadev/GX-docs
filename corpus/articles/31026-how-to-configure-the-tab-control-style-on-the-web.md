---
title: "How to configure the Tab Control style on the WEB"
source_id: 31026
source_url: https://wiki.genexus.com/commwiki/wiki?31026
genexus_version: "18"
---

# How to configure the Tab Control style on the WEB

The [Tab control for Web Panels](https://wiki.genexus.com/commwiki/wiki?25623) appearance can be configured using the following properties:

## [Tab Control Class property](#Tab+Control+Class+property)

It's a control property that determines the Theme Class that will be associated with the Tab control. The predetermined class for Tab controls is "Tab", but you can create other classes under the Tab class in the Theme. See the pictures below.

`[imagen omitida: wiki id 31029]`

## [TabPage Class](#TabPage+Class)

The control's tab pages can be styled using class properties which are grouped under the Tab Class (or any of its descendants).

These properties are as follows:

* **Tab Item Class**: Configure the style of the tab control's tab pages.
* **First Tab Item Class**: Configure the style of the tab control's first tab page.
* **Last Tab Item Class**: Configure the style of the tab control's last tab page.
* **Tab Strip Class**: Sets the style for the strip containing all the tab pages. It's a Section class.

`[imagen omitida: wiki id 31034]`

## [How to change the effects on hover, focus, and selection of the tab pages](#How+to+change+the+effects+on+hover%2C+focus%2C+and+selection+of+the+tab+pages)

Tab pages can change their style when the user hovers over any them, or when he selects or sets the focus on a tab page.

This is achieved using the following class properties which are grouped under the TabPage class:

* Selected Class
* Hovered Class
* Focused Class

These classes should be TabPage classes or their descendants.

`[imagen omitida: wiki id 31035]`

### [Example](#Example)

Suppose that you need to have the tab control shown in the following picture:

`[imagen omitida: wiki id 31041]`

The Tab Control Class property is "TabSessions" in this example. The TabSessions class has the following associations:

* Tab Item Class = TabPageSessions
* First Tab Item Class = TabPageSessions
* Last Tab Item Class= TabPageSessions
* Tab Strip Class = TabSessionStrip

The TabPageSessions and the TabSessionStrip property have the background color set to #458686 and the following font properties:

.TabPageSessions  
{  
    background-color: #458686;  
  *text-decoration: none;  
    color: white;  
    text-transform: uppercase;*  
}

The TabPageSessions "Selected Class property" is set to TabPageSessionsSelected class. This class sets the ForeColor property to black, as it is the desired design for the selected tab pages.

`[imagen omitida: wiki id 31037]`


|  |
| --- |
| **Backlinks** |
| [Tab control for Web Panels](https://wiki.genexus.com/commwiki/wiki?25623) |

---
