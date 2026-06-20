---
title: "HowTo: Configure Infinite Scrolling in web applications"
source_id: 31232
source_url: https://wiki.genexus.com/commwiki/wiki?31232
genexus_version: "18"
---

# HowTo: Configure Infinite Scrolling in web applications

The purpose of this article is to explain the necessary steps to configure [Infinite scrolling](https://wiki.genexus.com/commwiki/wiki?31231) for grids in web applications.

### [Step 1](#Step+1)

First, the [Rows property](https://wiki.genexus.com/commwiki/wiki?2452) has to be set to a value different than 0, as this property indicates the number or rows that have to be brought from the server in each request.

When the Rows property is set to a value different than zero, the [Paging property](https://wiki.genexus.com/commwiki/wiki?55903) becomes available.

`[imagen omitida: wiki id 31235]`

### [Step 2](#Step+2)

The Paging property has to be set to Infinite Scrolling value to have infinite scrolling behavior. If it's set to "One Page at a Time" it will do a traditional paging.

Then, the [Scroll Bar property](https://wiki.genexus.com/commwiki/wiki?31236) becomes available. The scroll can be on the grid itself (Scroll bar= Grid), or in the form (Scroll Bar = Form).

**Notes:**

* The [PreviousPage method](https://wiki.genexus.com/commwiki/wiki?8770) and [NextPage method](https://wiki.genexus.com/commwiki/wiki?8769) are ignored when Paging = Infinite Scrolling.
* There is a Loading Text which displays while the data is being loaded. The style of the loading text is configured using the Loading Text Class of the Grid in the Theme.
* The width of the columns is static and does not adapt to the size of the screen ([SAC 45356](https://www.genexus.com/developers/websac?es,,,45356)).


|  |
| --- |
| **Backlinks** |
| [Infinite scrolling](https://wiki.genexus.com/commwiki/wiki?31231) | [Paging property in Grids and Free Style Grids](https://wiki.genexus.com/commwiki/wiki?55903) | [Rows property](https://wiki.genexus.com/commwiki/wiki?2452) |

---
