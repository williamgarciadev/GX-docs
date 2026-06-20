---
title: "Panel object"
source_id: 24829
source_url: https://wiki.genexus.com/commwiki/wiki?24829
genexus_version: "18"
---

# Panel object

Defines a UI screen, no matter whether it is for Native Mobile, Web, TV, or a Watch. It shows and/or requests data through flexible abstract Layouts. User and system actions are defined through Events.

## [Description](#Description)

This object provides all the freedom to design the layout without pre-established structuring. The layout is empty, ready to be completed. You have to implement everything from scratch.

Through this object, you can show data to the user, ask the user for data, and make appealing and flexible layouts. It is very useful for creating more-complex user information interaction screens, creating wizards, showing messages, creating another kind of menus (different from the [Menu object](https://wiki.genexus.com/commwiki/wiki?16321) and more flexible), showing data obtained from other sources (e.g. [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270)s).

It is analogous to a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) (and to any section in a [Work With pattern and Work With object](https://wiki.genexus.com/commwiki/wiki?15974) empty initialized). That is to say, it implements a single screen that starts empty, with no definition, so you have the absolute freedom to put and remove what you want, and load the data from the database or anywhere else.

## [Sample](#Sample)

Suppose you need to define a Panel to ask the user for a date and invoke another Panel that shows all the appointments for that day. To do so, you have to define a variable &AppointmentDate based on the [Date data type](https://wiki.genexus.com/commwiki/wiki?7373), incorporate it in the layout, and insert a button in the Layout with an associated event defined in the Events section.

`[imagen omitida: wiki id 37454]`

This Panel does not have a [Base Table](https://wiki.genexus.com/commwiki/wiki?6347), but you could design Panels with Base Table.

## [Grids](#Grids)

There is no maximum of grids to be added to a Panel (neither without a base table nor with a base table).

`[imagen omitida: wiki id 46138]`

Here you can see a Panel that shows tweets which has been implemented from scratch by adding a grid to that panel's layout, with variables. These variables belong to an SDT that will be loaded by accessing an API, an external service from Twitter that will return the tweets.

Although there are some differences between Panels and Web Panels regarding the use of events, they are very similar.

## [Scope](#Scope)

**Generators:**[Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

## [See also](#See+also)

* [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)
* [Work With pattern and Work With object](https://wiki.genexus.com/commwiki/wiki?15974)
* [HowTo: Loading Data Using SDT on Panels Layouts](https://wiki.genexus.com/commwiki/wiki?17172)


|  |
| --- |
| **Pages** |
| [Check For New Data After Minutes Elapsed property](https://wiki.genexus.com/commwiki/wiki?18329) | [Check For New Data property](https://wiki.genexus.com/commwiki/wiki?18322) | [Checked Value property](https://wiki.genexus.com/commwiki/wiki?8734) |
| [Control Title property](https://wiki.genexus.com/commwiki/wiki?8736) | [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) | [Deep Link Name property](https://wiki.genexus.com/commwiki/wiki?36162) |
| [Enable Data Caching property](https://wiki.genexus.com/commwiki/wiki?18302) | [Enable Show Password property](https://wiki.genexus.com/commwiki/wiki?35577) | [InputType property](https://wiki.genexus.com/commwiki/wiki?8799) |
| [Is Password property](https://wiki.genexus.com/commwiki/wiki?8803) | [Lapse property](https://wiki.genexus.com/commwiki/wiki?17303) | [PageChanged event](https://wiki.genexus.com/commwiki/wiki?22735) |
| [Radio Direction property](https://wiki.genexus.com/commwiki/wiki?8818) | [Registration Handler property](https://wiki.genexus.com/commwiki/wiki?22981) | [Row Span property](https://wiki.genexus.com/commwiki/wiki?8828) |
| [Unchecked Value property](https://wiki.genexus.com/commwiki/wiki?8737) |

---
