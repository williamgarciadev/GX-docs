---
title: "Transitions for Web"
source_id: 22460
source_url: https://wiki.genexus.com/commwiki/wiki?22460
genexus_version: "18"
---

# Transitions for Web

In the Form class (or descendants) of the GeneXus [Web Theme object](https://wiki.genexus.com/commwiki/wiki?6420), some properties allow the designer to configure the effect in the navigation of web pages.

The designer may configure the enter effect of a web page that is loaded, and the exit effect of the web page that exits the screen.

This helps in the case of using [Single Page Applications](https://wiki.genexus.com/commwiki/wiki?22455), to give the user the perception of navigability of separate logical pages in the application.

The referred properties are as follows:

## [Enter Effect](#Enter+Effect)

Effect that takes place when the new page loads.

* Enter Effect Name. Possible values are:
  + Fade
  + Push (Up, Down, Left, Right)
  + None
* Enter Effect Length: The length of the enter effect in pixels or percentage, when it moves along horizontal or vertical axes.
* Enter Effect Duration: The duration of the enter effect in seconds or milliseconds.
* Enter Effect Opacity: The opacity used to start the enter effect, until it reaches opacity = 1 at the end of the transition.

## [Exit Effect](#Exit+Effect)

Effect that takes place when the page exits.

* Exit Effect Name. Possible values are:
  + Fade
  + Push (Up, Down, Left, Right)
  + None
* Exit Effect Length: The length of the exit effect in pixels or percentage, when it moves along horizontal or vertical axes.
* Exit Effect Duration: The duration of the exit effect in seconds or milliseconds.
* Exit Effect Opacity: The opacity used to end the exit effect. It starts with opacity = 1 at the beginning of the transition.

#### [Note:](#Note%3A)

When the effect is "Fade", its length is not considered.

In order to configure these effects, we must edit the GeneXus Theme, and change the settings of the Form class associated with the web page:

`[imagen omitida: wiki id 25305]`

Transitions take place in two cases (the browser needs to support [animations](http://caniuse.com/#feat=css-animation), CSS [transitions](http://caniuse.com/#feat=css-transitions) and the [History API](http://caniuse.com/#feat=history)):

1. When navigating from page A to page B (the navigation can be done with [Call command](https://wiki.genexus.com/commwiki/wiki?8260), [Link command](https://wiki.genexus.com/commwiki/wiki?8446), or in any way available in GeneXus to go from one page to another).

2. When a web component B is created in a control where another web component A has been previously created:

```
Event Start
    WebCom1.Object = A.Create()
EndEvent

Event Enter
    WebCom1.Object = B.Create()
EndEvent
```

The effects apply as follows:

* The Exit effect property settings of the Form class associated with page A applies when page A exits.
* The Enter effect property settings of the Form class associated with page B applies when page B is loaded.

### [Note](#Note)

If the browser does not support animations or transitions or History API, effects are not considered.


|  |
| --- |
| **Backlinks** |
| [Single Page Applications](https://wiki.genexus.com/commwiki/wiki?22455) |

---
