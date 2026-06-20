---
title: "Custom Render property"
source_id: 11407
source_url: https://wiki.genexus.com/commwiki/wiki?11407
genexus_version: "18"
---

# Custom Render property

Uses a custom user control for rendering grids. Applies to all selection and grid tab objects.

### [Scope](#Scope)

**Objects:** Web Panel  
**Platforms:** Web(.Net, Java)

### [Description](#Description)

Displaying structured information in web applications has become an important requirement in today's applications. The more intuitive the data, the better users can understand it. In addition, extra functionalities like filtering, sorting, and paging greatly enhance the user's experience which is a key factor for the success of our applications.

Let's see some examples of well-designed data structures we are getting used to seeing in web applications.  
  
ExtJS Grid

`[imagen omitida: wiki id 11408]`

TableSorter: TableSorter is a jQuery plugin for turning a standard HTML table with THEAD and TBODY tags into a sortable table without page refreshes. TableSorter can successfully parse and sort many types of data including linked data in a cell.

`[imagen omitida: wiki id 11411]`

Flexigrid: Lightweight but rich data grid with resizable columns and a scrolling data to match the headers, plus an ability to connect to an XML-based data source using Ajax to load the content. Similar concept to that of the Ext Grid but based on jQuery, which makes it lightweight and follows the jQuery mantra of running with the least amount of configuration.

`[imagen omitida: wiki id 11412]`

As of GeneXus X Evolution 1, the grid control has a new property named Custom Render that lets you select a user control that was implemented for that purpose.

### [How to use it](#How+to+use+it)

It is very simple; just select your grid and change Custom Render property to an available control from the list. For example, suppose you have implemented the following custom renders:

`[imagen omitida: wiki id 11851]`

If you select the gxui.GridExtension that is part of gxui Library, the next time you execute your web panel you will see that the grid looks as follows:

`[imagen omitida: wiki id 11853]`

The standard grid has been replaced by this control and all information was also loaded in it.

### [FAQ](#FAQ)

* ****How can you implement your own custom render control?****
  + You can follow the sample described [here](https://wiki.genexus.com/commwiki/wiki?11850,,).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.


|  |
| --- |
| **Backlinks** |
| [Align Content property](https://wiki.genexus.com/commwiki/wiki?36110) | [Align Items property](https://wiki.genexus.com/commwiki/wiki?36111) | [Arrows Color property](https://wiki.genexus.com/commwiki/wiki?41604) |
| [Flex Direction property](https://wiki.genexus.com/commwiki/wiki?36107) | [Toc:Flex Layout Container](https://wiki.genexus.com/commwiki/wiki?35354) | [Flex Wrap property](https://wiki.genexus.com/commwiki/wiki?36109) |
| [HowTo: Use Horizontal Grid control in Web Panels](https://wiki.genexus.com/commwiki/wiki?30594) | [Indicator Symbol property](https://wiki.genexus.com/commwiki/wiki?41603) | [Justify Content property](https://wiki.genexus.com/commwiki/wiki?36108) |

---
