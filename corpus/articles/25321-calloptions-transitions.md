---
title: "CallOptions Transitions"
source_id: 25321
source_url: https://wiki.genexus.com/commwiki/wiki?25321
genexus_version: "18"
---

# CallOptions Transitions

[CallOptions](https://wiki.genexus.com/commwiki/wiki?23666) are used to specify at runtime the transitions, behavior, and position in a call to a particular [Panel object](https://wiki.genexus.com/commwiki/wiki?24829).  
With the transitions, you can change the way a Panel enters and the way it leaves the screen.

Transition effects between Panels are pre-defined and can be any of these:

* Default (default effect for the platform)
* CurlUp
* CurlDown
* FlipFromLeft
* FlipFromRight
* SlideDown
* SlideUp
* SlideLeft
* SlideRight
* PushUp
* PushDown
* PushLeft
* PushFromRight
* Fade
* None (no effect)

All these options are listed in an **enumerated domain** called **Effect**and are assigned to the Panels in the Form class as explained in the document: [HowTo: Use Transitions in Mobile applications](https://wiki.genexus.com/commwiki/wiki?20961).

**NOTE:**Curl and Flip only work on iOS.

### [**Definition**](#Definition)

If for some reason you don't want to use the transition defined in the class "Form" theme for the Panel, you can change that behavior at runtime.

Syntax:

```
<ObjectName>.CallOptions.EnterEffect = Effect.<Name of the effect>  
<ObjectName>.CallOptions.ExitEffect = Effect.<Name of the effect>
```

Example:

```
Panel.CallOptions.EnterEffect = Effect.FlipFromLeft
Panel.CallOptions.ExitEffect = Effect.FlipFromRight
Panel.Call()
```


|  |
| --- |
| **Backlinks** |
| [CallOptions](https://wiki.genexus.com/commwiki/wiki?23666) |

---
