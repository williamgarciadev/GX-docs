---
title: "Event Triggering Order in Panels"
source_id: 17614
source_url: https://wiki.genexus.com/commwiki/wiki?17614
genexus_version: "18"
---

# Event Triggering Order in Panels

This document explains the order in which events are executed in a Panel for Android and iOS applications, including components, Global Events, and application lifecycle events such as ApplicationPause, ApplicationResume, and Back.

Understanding this sequence helps developers design predictable data flows, avoid redundant server calls, and coordinate communication between nested components.

### [Execution Flow in Panels](#Execution+Flow+in+Panels)

When a Panel is executed, a specific sequence of client and server events takes place. These events determine how and when UI initialization, data loading, and updates occur.

|  |  |  |  |
| --- | --- | --- | --- |
| **Order** | **Event** | **Context** | **Description** |
| 1 | [ClientStart](https://wiki.genexus.com/commwiki/wiki?24044) | Client | Runs once on the device when the Panel is first opened. Used to initialize variables, UI controls, and access device capabilities. |
| 2 | [Navigation.Start](https://wiki.genexus.com/commwiki/wiki?25668) | Client | Runs after ClientStart when the navigation style requires it (Slide, Tab, Flip, etc.). |
| 3 | [Start](https://wiki.genexus.com/commwiki/wiki?8043) | Server | Executes once. Used for data initialization, service calls, or loading fixed information into variables. |
| 4 | [Refresh](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?8195,,) | Server | Runs after Start. Used for dynamic data updates or variable recalculation. |
| 5 | [Load](https://wiki.genexus.com/commwiki/wiki?8188) | Server | Runs last, once per record if the grid has a Base Table, once if it has no base table, and not at all if the grid is SDT-based. |

 

For example:  Panel opens → ClientStart → Navigation.Start → Start → Refresh → Load

### [Manual Refresh](#Manual+Refresh)

You can manually trigger a refresh using the [Refresh() command](https://wiki.genexus.com/commwiki/wiki?25060) from any client event. If the data context has changed, the Refresh and Load events are executed again. Otherwise, no server request occurs.

**Note:** Use [Parm() rules](https://wiki.genexus.com/commwiki/wiki?6862) with filters to force reloading.

### [Panels with Components](#Panels+with+Components)

When a Panel contains components, each component executes its own independent event sequence immediately after the main Panel’s events finish.

Sample:

```
MainPanel.ClientStart
MainPanel.Start
MainPanel.Refresh
MainPanel.Load
├── ComponentA.ClientStart
│   ├── ComponentA.Start
│   ├── ComponentA.Refresh
│   └── ComponentA.Load
└── ComponentB.ClientStart
    ├── ComponentB.Start
    ├── ComponentB.Refresh
    └── ComponentB.Load
```

### [Global Events (Component Communication)](#Global+Events+%28Component+Communication%29)

Global Events allow components to communicate inside a Panel without having direct references to each other. They use the predefined external object GlobalEvents, which works as an event bus within the same screen.

Usage Example:

```
Event ItemUpdated(&ProductId)
EndEvent

Event &Update.Click
   GlobalEvents.ItemUpdated(&ProductId)
EndEvent

Event GlobalEvents.ItemUpdated
   Refresh()
EndEvent
```

### [Lifecycle Events (Background and Foreground Transitions)](#Lifecycle+Events+%28Background+and+Foreground+Transitions%29)

When a mobile application transitions between background and foreground, GeneXus executes application lifecycle events that allow you to manage state restoration or data updates.

|  |  |  |  |
| --- | --- | --- | --- |
| **Event** | **Trigger** | **Platform** | **Behavior** |
| ApplicationPause | Applications goes to background. | Android & iOS | Executes once in the visible Panel. Used to save state, stop timers, or pause animations. |
| ApplicationResume | Application returns to foreground. | Android & iOS | Executes before interaction resumes. Used to refresh or synchronize data. |
| Back | User navigates back. | Android & iOS | Captures hardware button or gesture. If not handled, it performs default navigation. |

### [Sample](#Sample)

```
Event ApplicationResume
    Refresh()
EndEvent
```

### [Full sample: Complex Flow](#Full+sample%3A+Complex+Flow)

This sample shows a complete execution flow for a Panel with Components and Global Events:

1. The user opens ProductPanel → ClientStart → Navigation.Start → Start → Refresh → Load  
2. Two components (ProductInfo and ProductList) execute their full cycles.  
3. The user marks a product as favorite in ProductList, triggering GlobalEvents.FavoriteUpdated().  
4. ProductInfo listens and executes Refresh → Load.  
5. The user switches to another application → ApplicationPause executes.  
6. The user returns → ApplicationResume executes → Refresh() updates data.  
7. The user presses Back → Event 'Back' executes, controlling navigation.

### [Event execution order in Panels](#Event+execution+order+in+Panels)

|  |  |  |  |
| --- | --- | --- | --- |
| **Event** | **Context** | **Frequency** | **Purpose** |
| ClientStart | Client | Once | Initialize UI and device state. |
| Navigation.Start | Client | Once | Navigation-specific setup. |
| Start | Server | Once | Initialize data and variables. |
| Refresh | Server | Multiple | Reload data dynamically. |
| Load | Server | Per record | Populate Grids. |
| GlobalEvents | Client | On demand | Communicate between Components. |
| ApplicationPause | Client | On demand | Save UI state. |
| ApplicationResume | Client | On demand | Restore or sync data. |
| Back | Client | On demand | Handle navigation or exit. |

### [Event handling best practices for Panels](#Event+handling+best+practices+for+Panels)

* Use ClientStart event for visual setup and device logic.
* Use Start and Refresh events for data loading and filtering.
* Use Parm() rule to force refresh when filter variables change.
* Handle ApplicationPause and ApplicationResume events for continuity.
* Use GlobalEvents to synchronize components.
* Use Components designed to be idempotent (safe to reload).

### [See Also](#See+Also)

[Native Mobile Applications Events](https://wiki.genexus.com/commwiki/wiki?17042)  
[Server-side Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?24234)  
[Refresh event](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?8195,,)  
[Load event](https://wiki.genexus.com/commwiki/wiki?8188)


|  |
| --- |
| **Backlinks** |
| [Back event](https://wiki.genexus.com/commwiki/wiki?24950) | [Client-side Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?24332) |
| [ClientStart event](https://wiki.genexus.com/commwiki/wiki?24044) | [Component control](https://wiki.genexus.com/commwiki/wiki?29811) | [ControlValueChanging event](https://wiki.genexus.com/commwiki/wiki?35768) | [Determining the Base Table for the Form and Grid in Panels](https://wiki.genexus.com/commwiki/wiki?24807) |
| [Load event](https://wiki.genexus.com/commwiki/wiki?8188) | [Category:Native Mobile Applications Events](https://wiki.genexus.com/commwiki/wiki?17042) | [Refresh command in Panels](https://wiki.genexus.com/commwiki/wiki?25060) |

---
