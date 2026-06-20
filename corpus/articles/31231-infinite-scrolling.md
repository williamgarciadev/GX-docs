---
title: "Infinite scrolling"
source_id: 31231
source_url: https://wiki.genexus.com/commwiki/wiki?31231
genexus_version: "18"
---

# Infinite scrolling

A grid can potentially display a great amount of data. To give the user flexibility and make it easier to find information, as well as to save resources (bandwidth), the data is usually displayed in pages. So, the user can move backwards and forwards to browse the various grid pages.

An alternative to the [Paging in apps](https://wiki.genexus.com/commwiki/wiki?31280) feature is to use infinite scrolling.

In the infinite (also called continuous) scrolling pattern, the first page is shown with a subset of the data, which is brought on demand from the server as the user scrolls in the grid or page.  
So, this pattern eliminates the paging buttons by creating the effect of an infinitely scrolling page that scrolls new data as the user scrolls to the bottom of a page or the grid.

Paging, as well as infinite scrolling, are solutions for the same problem, which is to give the user the possibility to navigate through data on demand without wasting bandwidth resources.

A remarkable advantage of using infinite scrolling is that the user remains on the same panel, so selecting data to perform various actions (for example, selecting records to be deleted) could be much easier because all the data is on the same panel.

### [Infinite scrolling in Smart Devices apps](#Infinite+scrolling+in+Smart+Devices+apps)

The [Rows property](https://wiki.genexus.com/commwiki/wiki?2452) for Grids allows configuring infinite scrolling.

### [Infinite scrolling in Web applications](#Infinite+scrolling+in+Web+applications)

For Web applications, scrolling is available in two modes:

1. Grid infinite scrolling  
   The grid has a certain height and it displays a vertical scroll inside the grid's area, for the user to scroll and see all the rows.  
     
   `[imagen omitida: wiki id 31365]`
2. Page infinite scrolling  
   The grid doesn't have a fixed height and expands vertically as the user scrolls using the web page vertical scroll. In this case, there shouldn't be another control at the bottom of the grid because it will be unreachable.

**Warning**: It's available only for the [Abstract Layout](https://wiki.genexus.com/commwiki/wiki?25209) with Web User Experience = Smooth.

  
  
See [HowTo: Configure Infinite Scrolling in web applications](https://wiki.genexus.com/commwiki/wiki?31232)

### [See Also](#See+Also)

[Pull To Refresh property](https://wiki.genexus.com/commwiki/wiki?29993,,)

[Automatic paging in Grid control](https://wiki.genexus.com/commwiki/wiki?6086)


|  |
| --- |
| **Backlinks** |
| [Automatic paging in Grid control](https://wiki.genexus.com/commwiki/wiki?6086) | [HowTo: Configure Infinite Scrolling in web applications](https://wiki.genexus.com/commwiki/wiki?31232) |
| [Paging in apps](https://wiki.genexus.com/commwiki/wiki?31280) | [Rows property](https://wiki.genexus.com/commwiki/wiki?2452) |

---
