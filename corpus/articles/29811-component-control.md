---
title: "Component control"
source_id: 29811
source_url: https://wiki.genexus.com/commwiki/wiki?29811
genexus_version: "18"
---

# Component control

Components are available in the [GeneXus Toolbox](https://wiki.genexus.com/commwiki/wiki?10000) for [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)s or [Work With object](https://wiki.genexus.com/commwiki/wiki?15974)s.

Like [Web Components](https://wiki.genexus.com/commwiki/wiki?31172), Components are controls that can contain [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)s or [Work With object](https://wiki.genexus.com/commwiki/wiki?15974)s without losing any of their characteristics and they can also run independently. This feature provides GeneXus application designers with a high degree of reusability.

The main difference with [Web Components](https://wiki.genexus.com/commwiki/wiki?31172) is that Components don't need any additional property like [Type property (in Web Panels and Transactions)](https://wiki.genexus.com/commwiki/wiki?10444).

|  |
| --- |
|  |
| *Final result on [EventDay](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?22550,,) sample* |

## [Simple usage example](#Simple+usage+example)

In *[EventDay](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?22550,,)*, suppose you want to view tweets while you are reading session content.

To do this, you create a Panel called "SessionsWithTweets" and drag two Component controls from the toolbox.

`[imagen omitida: wiki id 29995]`

Then, you must set both Component controls with WorkWith object for Sessions and the Panel of Tweets as shown below:

`[imagen omitida: wiki id 29996]`

Finally, the layout results as shown below.

`[imagen omitida: wiki id 30370]`

## [Methods](#Methods)

#### [Refresh](#Refresh)

  Causes an object embedded into a Component to execute the Refresh event.

**Return value**: None

**Parameters**: None

**Note**: Differences between Refresh methods/commands and how to use them:

* To refresh an object and all its components (including forms, grids, etc), use the [Refresh command](https://wiki.genexus.com/commwiki/wiki?25069).
* To refresh the full screen, use the [Refresh Form command](https://wiki.genexus.com/commwiki/wiki?25287).
* To refresh a Grid in an object, use the [Refresh method for Grid controls](https://wiki.genexus.com/commwiki/wiki?22578).
* To refresh an object embedded in a Component (and all its descendants) use the method described here.

## [Event trigger sequence with multiple Components](#Event+trigger+sequence+with+multiple+Components)

Read about [Event Triggering Order in Panels](https://wiki.genexus.com/commwiki/wiki?17614). If you have C1...CN  Components in a Panel P, schematically, the execution order will be:

```
Client Start (P)
Start (P)
Refresh (P)
Load (P)

     ClientStart (C1)
     Start (C1)
     Refresh (C1)
     Load (C1)

     <...>

     ClientStart (CN)
     Start (CN)
     Refresh (CN)
     Load (CN)
```

### 

## [Action Bar behavior](#Action+Bar+behavior)

When using multiple Components, the Action Bar behavior will be the combination of actions for each Component.

## [Advance usage example](#Advance+usage+example)

Continuing with the previous example, suppose you want to read the tweets every minute. To do this, you must write an event associated with a Timer variable (invisible in Panel and with [Chronometer control](https://wiki.genexus.com/commwiki/wiki?25058) set) and refresh the screen when the elapsed time exceeds 60 seconds.

`[imagen omitida: wiki id 29812]`

```
Event ClientStart
    // Init timer
    &Timer = 0
Endevent

Event &Timer.Tick
    // If one minute elapsed, refresh component
    If Mod(&Timer,60) = 0
        Component2.Refresh()
    EndIf
EndEvent
```

Finally, substitute the invocation to Sessions on the dashboard, delete the Tweets node and run the application.  
Notes

* Components controls cannot be drawn into a Grid Control.
* To synchronize the components at run-time programmatically, you can use [Global Events](https://wiki.genexus.com/commwiki/wiki?30201).
* The [Object property](https://wiki.genexus.com/commwiki/wiki?7011) is available at design-time, and also available at run-time programmatically for [Dynamic Component Creation](https://wiki.genexus.com/commwiki/wiki?5404).

## [Scope](#Scope)

**Objects**[Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974)  
**Generators:** [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453)


|  |
| --- |
| **Backlinks** |
| [Dynamic Component Creation](https://wiki.genexus.com/commwiki/wiki?5404) | [GeneXus Markup Language (GXML)](https://wiki.genexus.com/commwiki/wiki?46876) |
| [HowTo: Using Global Events in Smart Device applications](https://wiki.genexus.com/commwiki/wiki?30201) | [Object property](https://wiki.genexus.com/commwiki/wiki?7011) | [KB:PlantCare - ECommerce Sample](https://wiki.genexus.com/commwiki/wiki?50476) | [KB:PlantCare and SweetWorld - ECommerce Sample (GeneXus 18 Upgrade 3)](https://wiki.genexus.com/commwiki/wiki?56139) |

---
