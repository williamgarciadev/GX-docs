---
title: "AppLifecycle external object"
source_id: 42056
source_url: https://wiki.genexus.com/commwiki/wiki?42056
genexus_version: "18"
---

# AppLifecycle external object

Sometimes the application needs to perform some actions when its execution state changes. For example, when the application starts, when it goes to background or when it comes back to foreground again. This external object allows asking for the application's execution state, and to code an event to manage state changes.

`[imagen omitida: wiki id 42060]`

## [Domains](#Domains)

### [ApplicationState domain](#ApplicationState+domain)

This domain is defined in order to identify the application execution state.  
It is based on Numeric(1) with the following enumerated values:

|  |  |
| --- | --- |
| **Active** | The application is running in foreground. |
| **Inactive** | The application is running in foreground but does not respond to events, i.e., when a phone call arrives in the device. Available only in iOS. |
| **Background** | The application is running in background. |
| **NotRunning** | The application is not running at all. Used only in the AppStateChanged event. |

## [Properties](#Properties)

### [ApplicationState](#ApplicationState)

It is a read-only property automatically set to the application current execution state.  
The property only returns the values Active, Inactive (iOS only) or Background. NotRunning value is never returned by the property.  
This property replaces the use of [Interop external object](https://wiki.genexus.com/commwiki/wiki?23734) ApplicationState property.

## [Events](#Events)

### [AppStateChanged event](#AppStateChanged+event)

Notifies when the application's execution state changes.  
This event must be used only in the [Smart Devices Main object](https://wiki.genexus.com/commwiki/wiki?17817)

|  |  |
| --- | --- |
| **Input** | oldState: ApplicationState  newState: ApplicationState |
| **Output** | None |

## [Example](#Example)

If you need to execute something when the application is starting

```
Event AppLifecycle.AppStateChanged(&old, &new)
    Composite
        if &old = ApplicationState.NotRunning
            // your code
        endif
    EndComposite
EndEvent
```

If you need to execute something when the application is going to background

```
Event AppLifecycle.AppStateChanged(&old, &new)
    Composite
         if &new = ApplicationState.Background
             // your code
         endif
    EndComposite
EndEvent
```

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators:** | [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453) |

## [Availability](#Availability)

This external object is available as of [GeneXus 16 upgrade 2](https://wiki.genexus.com/commwiki/wiki?41525,,).


|  |
| --- |
| **Backlinks** |
| [Interop external object](https://wiki.genexus.com/commwiki/wiki?23734) | [Interop external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55183) | [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) |
| [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) |

---
