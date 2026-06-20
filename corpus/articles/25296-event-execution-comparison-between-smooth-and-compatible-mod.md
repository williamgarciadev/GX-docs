---
title: "Event Execution comparison between Smooth and compatible models"
source_id: 25296
source_url: https://wiki.genexus.com/commwiki/wiki?25296
genexus_version: "18"
---

# Event Execution comparison between Smooth and compatible models

This document explains the difference between the execution of events in models that have the [Web User Experience property](https://wiki.genexus.com/commwiki/wiki?22449) set to Smooth, compared to those that have the same property set to "Previous versions compatible".

## [GET HTTP Method](#GET+HTTP+Method)

For the GET HTTP method (when the web page is loaded for the first time), there are no differences in event triggering between both models.

In a very simple web panel, event triggering when the GET HTTP method is executed can be summarized as follows:

|  |  |
| --- | --- |
| **Smooth Model** | **Compatible Model** |
| Start | Start |
| Refresh | Refresh |
| Load | Load |

Note: The Load event should be considered as the load event of all the grids which are inside the web panel.

### [Web panels with web components](#Web+panels+with+web+components)

For a web panel that has web components, event execution in the GET HTTP method is as follows:

|  |  |
| --- | --- |
| **Smooth Model** | **Compatible Model** |
| Start Event of the web panel | Start Event of the web panel |
| Refresh Event of the web panel | Refresh Event of the web panel |
| Start event of all the web components | Start event of all the web components |
| Load event of the web panel | Load event of the web panel |
| Refresh and Load events of all the web components in the order they appear on the screen (from left to right) | Refresh and Load events of all the web components in the order they appear on the screen (from left to right) |

### Example

Let's use the following example, where WEB PANEL X contains WEB COMPONENT A, and WEB COMPONENT B:

##### Figure #1

In this example, the execution of the GET HTTP method in both models is as follows:

* Start event of MasterPage
* Start event of web panel X
* Refresh event of MasterPage
* Load event of MasterPage
* Refresh event of web panel X
* Start of web component A
* Start of web component B
* Grid.load in web panel X
* Refresh of web component A
* Grid.load of web component A
* Refresh of web component B
* Grid.load of web component B

## [POST HTTP method](#POST+HTTP+method)

Consider a web panel where a [User defined event](https://wiki.genexus.com/commwiki/wiki?8044) - or the Enter Event - is executed.  
In this case there are differences in how the event is run in the Smooth and the compatible model. Basically, in the Smooth model the Refresh event is not triggered automatically after a user event.  
The Start event is not triggered either.

As a consequence, in a very simplified model, the execution of events would be as follows:

|  |  |
| --- | --- |
| **Smooth Model** | **Compatible Model** |
| X | Start |
| Variables of the form are read | Variables of the form are read |
| User Event | User Event |
| X | Refresh |
| X | Load |

### [Web panels with web components](#Web+panels+with+web+components)

In a web panel that has web components, the event triggering behavior when the POST HTTP method is executed depends on whether the event is executed from the web panel, or from a web component inside the web panel.

Let's see both cases here.

#### [POST HTTP method executed in the web panel](#POST+HTTP+method+executed+in+the+web+panel)

In a general model, event triggering is as follows:

|  |  |
| --- | --- |
| **Smooth Model** | **Compatible Model** |
| X | Start Event of the web panel |
| Variables in the form are read | Variables in the form are read |
| User Event of the web panel | User Event of the web panel |
| X | Refresh of the web panel |
| X | Start of all the components in the order they appear on the screen |
| X | Refresh and Load of all the components in the order they appear on the screen |

#### [POST HTTP method executed in the web component](#POST+HTTP+method+executed+in+the+web+component)

In a general model, event triggering is as follows:

|  |  |
| --- | --- |
| **Smooth Model** | **Compatible Model** |
| X | Start event of the web panel |
| X | Start event of the web component where the event was triggered |
| Variables of the web component form are read | Variables of the web component form are read |
| User event of the web component | User event of the web component |
| X | Refresh event of the web panel |
| X | Start event of the other web components |
| X | Refresh and Load of the other web components |

### Example

More specifically, in the example above - figure #1- suppose that a user event has been executed on WEB COMPONENT A.

In this case, the event execution would be as follows:

|  |  |
| --- | --- |
| **Smooth Model** | **Compatible model** |
| X | Start of the web panel X |
| X | Start event of web component A |
| Variables of the form of web component A are read | Variables of the form of web component A are read |
| User event of web component A | User event of web component A |
| X | Refresh of web panel X |
| X | Start of web component B |
| X | Load of web panel X |
| X | Refresh of web component A |
| X | Grid.Load of web component A |
| X | Refresh of web component B |
| X | Grid.load of web component B |

### [Note:](#Note%3A)

In a Smooth model, the different parts of the form can be refreshed explicitly, using the commands for that purpose:

* [Refresh method for Grid controls](https://wiki.genexus.com/commwiki/wiki?22578)
* [Refresh Web Component command](https://wiki.genexus.com/commwiki/wiki?22579)
* [Refresh Form command](https://wiki.genexus.com/commwiki/wiki?25287)
* [Refresh command](https://wiki.genexus.com/commwiki/wiki?25286)

## [See Also](#See+Also)

[Event Execution Scheme](https://wiki.genexus.com/commwiki/wiki?22472)


|  |
| --- |
| **Backlinks** |
| [Event Execution Scheme](https://wiki.genexus.com/commwiki/wiki?22472) |

---
