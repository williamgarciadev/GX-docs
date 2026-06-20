---
title: "Offline Database Object Table selection"
source_id: 23561
source_url: https://wiki.genexus.com/commwiki/wiki?23561
genexus_version: "18"
---

# Offline Database Object Table selection

GeneXus can **automatically** select the tables that are going to be in the Offline Database of an Offline Application. This selection is made by analyzing the objects call tree from the Main object that defines the application. Tables which are referenced by offline objects ( objects with [Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?20911) offline or inherited from offline objects ) are selected, as also all the tables which has [Referential Integrity](https://wiki.genexus.com/commwiki/wiki?1984,,) control from these tables.

### [Considerations](#Considerations)

It is important then to avoid the use of [Dynamic Calls](https://wiki.genexus.com/commwiki/wiki?17411). If Dynamic Calls are used in the applications, it is recommended to create and add to the call tree an object that references all the possible objects called via dynamic calls, so then GeneXus will automatically take the references that are needed to select the tables.

### [See here](#See+here)

An example of how to choose the tables that are going to be in the Offline Database [using the Connectivity Support Property](https://wiki.genexus.com/commwiki/wiki?23558)

### [See also](#See+also)

* [Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509)
* [Offline Database Object conditions](https://wiki.genexus.com/commwiki/wiki?23570)
* [Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?20911)
* [Dynamic Calls in Smart Devices](https://wiki.genexus.com/commwiki/wiki?17411)


|  |
| --- |
| **Backlinks** |
| [Create Offline Database](https://wiki.genexus.com/commwiki/wiki?27123) | [HowTo: Convert online applications into offline applications](https://wiki.genexus.com/commwiki/wiki?24591) | [HowTo: Use the Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?23558) |
| [Category:Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509) | [Offline Database reorganization](https://wiki.genexus.com/commwiki/wiki?27121) | [Toc:Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22228) |

---
