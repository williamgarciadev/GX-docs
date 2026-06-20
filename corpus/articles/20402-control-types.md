---
title: "Control Types"
source_id: 20402
source_url: https://wiki.genexus.com/commwiki/wiki?20402
genexus_version: "18"
---

# Control Types

Want to show an ImageGallery and browse through it in a very intuitive way? Want to have a natural view of locations using a Map? Want to rate a product using a StarRating control instead of typing a value?

GeneXus provides these kinds of controls and more so you can build flexible and intuitive applications. Besides, you will be able to create your own custom controls! User controls will make it easy to create flexible and intuitive applications by taking advantage of most features currently available in smart devices.

User Controls like these can be included in GeneXus applications:

|  |  |  |
| --- | --- | --- |
| [Maps Control Type](https://wiki.genexus.com/commwiki/wiki?15309) | [Rating Control](https://wiki.genexus.com/commwiki/wiki?18350) | [Scanner Control](https://wiki.genexus.com/commwiki/wiki?15310) |
|  |  |  |

Probably, you've already imagined more such as various controls that differ in functionality and complexity. For this reason, we are developing an extensible control platform to let you integrate a broad set of controls.

There are two types of user controls for smart devices: **Item** and **List**.

The **items** user controls apply to single-valued items, such as:

* [Scanner Control](https://wiki.genexus.com/commwiki/wiki?15310)
* [Rating Control](https://wiki.genexus.com/commwiki/wiki?18350)
* [HowTo: Use the Wheel Control](https://wiki.genexus.com/commwiki/wiki?16239)
* [HowTo: Use MultiWheel Control](https://wiki.genexus.com/commwiki/wiki?20171)
* [Linear Gauge Control](https://wiki.genexus.com/commwiki/wiki?16269)
* [HowTo: Use the Native Mobile PhysicalMeasures Control](https://wiki.genexus.com/commwiki/wiki?17951)
* [Slider Control](https://wiki.genexus.com/commwiki/wiki?20334)
* [Advanced Image Control](https://wiki.genexus.com/commwiki/wiki?20497)
* [HowTo: Use SD Geolocation Control in Smart Devices](https://wiki.genexus.com/commwiki/wiki?16756)

The **list** user controls apply to complex data types such as a collection ([Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021) or [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270)). Below are samples of this kind:

|  |  |  |
| --- | --- | --- |
| **Control Type** | **Description** | **Example** |
| **Paged Grid** | Shows one record of a list per page. This enables you to show more information and navigate through the list more easily. Also, by double-tapping, you can access the detailed view of the Item. [See more...](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?17302,,) |  |
| **Leaves** | Offers a similar experience to turn the page of a book. Each grid item is shown on a single page. [See more...](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?17124,,) |  |
| **Horizontal Grid** | Lets you show elements horizontally, instead of the usual vertical way for a Grid. Also, it lets you control the way the elements are shown, letting you choose the number of columns and rows we want to display by page. [See more...](https://wiki.genexus.com/commwiki/wiki?18180) |  |
| **Magazine Viewer** | Provides an experience similar to reading a newspaper, magazine, or catalog. Each page shows many articles (parts of them), that can be zoomed in with a touch (the equivalent of “continued on page X” of a printed newspaper version). The number of items shown could vary among columns. [See more...](https://wiki.genexus.com/commwiki/wiki?17567) |  |
| **Maps** | Provides a way for displaying locations using a map and interacting with them. For that, the grid needs to have a geolocation value for each item. [See more...](https://wiki.genexus.com/commwiki/wiki?15309) |  |
| **Image Map** | Lets you display a background image with regions identified by its coordinates {x, y} and a size. Each defined region can have an image to display on the coordinates defined to it with the defined size. Each region corresponds to one item on the list. [See more...](https://wiki.genexus.com/commwiki/wiki?17823) |  |
| **Charts** | Lets you display numeric information of a grid as a chart (pie or timeline). [See more...](https://wiki.genexus.com/commwiki/wiki?16106) |  |
| **Spark Line** | Often used to show high-density series of numbers. [See more...](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?17110,,) |  |
| **Matrix Grid** | To display data in two-dimensional grids (as of GeneXus X Evolution 3). [See more...](https://wiki.genexus.com/commwiki/wiki?25139) |  |

### Scope

**Generators:** Android, Apple, Angular


|  |
| --- |
| **Pages** |
| [Advanced Image Control](https://wiki.genexus.com/commwiki/wiki?20497) | [GeoLocation Picker](https://wiki.genexus.com/commwiki/wiki?15969) | [HowTo: Use Charts Control](https://wiki.genexus.com/commwiki/wiki?16106) |
| [HowTo: Use Horizontal Grid control in Panels](https://wiki.genexus.com/commwiki/wiki?18180) | [HowTo: Use SD Geolocation Control in Smart Devices](https://wiki.genexus.com/commwiki/wiki?16756) | [HowTo: Using SD Paged Grid Control](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?17302,HowTo%3A+Using+SD+Paged+Grid+Control,) |
| [HowTo: Using SD SparkLine Control for Smart Devices](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?17110,HowTo%3A+Using+SD+SparkLine+Control+for+Smart+Devices,) | [Magazine Viewer Control](https://wiki.genexus.com/commwiki/wiki?17567) | [PageControllerBackColor property for Smart Devices](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?39038,PageControllerBackColor+property+for+Smart+Devices,) |

---
