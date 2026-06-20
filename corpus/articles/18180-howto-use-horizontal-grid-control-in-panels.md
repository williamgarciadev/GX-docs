---
title: "HowTo: Use Horizontal Grid control in Panels"
source_id: 18180
source_url: https://wiki.genexus.com/commwiki/wiki?18180
genexus_version: "18"
---

# HowTo: Use Horizontal Grid control in Panels

It is possible to show the elements of a [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) horizontally, instead of vertically as usual, by setting the Grid [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) to "Horizontal Grid".

You can also control how the elements are displayed by choosing the number of columns and rows you want to show by page.

For example, suppose you want to show 2 columns and 3 rows per page:

|  |  |
| --- | --- |
| **Android** | **Apple** |
|  |  |

To achieve this, follow these steps:

### [Step 1](#Step+1)

Create the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908):

```
Property
{
   PropertyId*
   PropertyName
   PropertyAddress
   PropertyFrontImage
}
```

### [Step 2](#Step+2)

Apply the [Work With Pattern](https://wiki.genexus.com/commwiki/wiki?15975) to it.

### [Step 3](#Step+3)

Press F5 and add some records.

### [Step 4](#Step+4)

Go to the [Work With List Node](https://wiki.genexus.com/commwiki/wiki?15984) and select the Grid. Set its [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) to **"**Horizontal Grid" and set the following properties as shown:

`[imagen omitida: wiki id 38952]`

#### [**Properties that let you customize the behavior and look of the Horizontal Grid**](#Properties+that+let+you+customize+the+behavior+and+look+of+the+Horizontal+Grid)

|  |
| --- |
| [Paged property](https://wiki.genexus.com/commwiki/wiki?38794) |
| [Show Page Controller property](https://wiki.genexus.com/commwiki/wiki?38864) |
| [PageController theme-class](https://wiki.genexus.com/commwiki/wiki?38876) |
| [Columns Per Page Portrait property](https://wiki.genexus.com/commwiki/wiki?56189) |
| [Rows Per Page Portrait property](https://wiki.genexus.com/commwiki/wiki?56190) |
| [Columns Per Page Landscape property](https://wiki.genexus.com/commwiki/wiki?56186) |
| [Rows Per Page Landscape property](https://wiki.genexus.com/commwiki/wiki?56185) |

You can see the runtime result in the two images below, depending on the orientation of your device and on the property settings for the number of rows and columns that will be shown by page.

#### [**Portrait:**](#Portrait%3A)

|  |  |
| --- | --- |
| **Android** | **Apple** |
|  |  |

#### [**Landscape**:](#Landscape%3A)

|  |  |
| --- | --- |
| **Android** | **Apple** |
|  |  |

**Note**: the last image shows a photo taken when the device in portrait mode. You will note the changes in the number of rows and columns shown.


|  |
| --- |
| **Backlinks** |
| [Columns Per Page Landscape property](https://wiki.genexus.com/commwiki/wiki?56186) | [Columns Per Page Portrait property](https://wiki.genexus.com/commwiki/wiki?56189) | [Category:Control Types](https://wiki.genexus.com/commwiki/wiki?20402) |
| [Grids with Selection By Code for Panels](https://wiki.genexus.com/commwiki/wiki?35987) | [Horizontal Grid Control](https://wiki.genexus.com/commwiki/wiki?30592) |
| [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [PageChanged event](https://wiki.genexus.com/commwiki/wiki?22735) | [Paged property](https://wiki.genexus.com/commwiki/wiki?38794) |
| [Rows Per Page Landscape property](https://wiki.genexus.com/commwiki/wiki?56185) | [Rows Per Page Portrait property](https://wiki.genexus.com/commwiki/wiki?56190) | [Show Page Controller property](https://wiki.genexus.com/commwiki/wiki?38864) |

---
