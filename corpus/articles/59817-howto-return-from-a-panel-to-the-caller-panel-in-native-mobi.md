---
title: "HowTo: Return from a Panel to the caller Panel in Native Mobile Apps"
source_id: 59817
source_url: https://wiki.genexus.com/commwiki/wiki?59817
genexus_version: "18"
---

# HowTo: Return from a Panel to the caller Panel in Native Mobile Apps

There are three ways to return from a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) to the Panel object that called it (besides making an explicit call to the caller Panel):

1) Including code in the [Back event](https://wiki.genexus.com/commwiki/wiki?24950) (it will be executed when the end user presses the Back button).  
2) Using the [Cancel method of the Actions EO](https://wiki.genexus.com/commwiki/wiki?18363).  
3) Using the [Return command](https://wiki.genexus.com/commwiki/wiki?31353).

For example, suppose there are two Panels, A and B. Panel A calls Panel B as follows:

```
Event 'Call_B'
   Composite
     // ... do something before calling B
     B()  //B is called without parameters
     msg("After calling B")
     // ... do something else after calling B
   EndComposite
EndEvent
```

If you use the first two options, the code following the call to Panel B will not be executed when returning to Panel A.

However, if you use the Return command, the code following the call to Panel B will be executed.

In the case of including a Return command within the Back event, the device's back button will adopt the Return behavior, executing the code that follows the call to Panel B.

### [Scope](#Scope)

**Objects:** [Panel](https://wiki.genexus.com/commwiki/wiki?24829)  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [See Also](#See+Also)

[Actions external object](https://wiki.genexus.com/commwiki/wiki?31350)  
[Composite command](https://wiki.genexus.com/commwiki/wiki?17389)


|  |
| --- |
| **Backlinks** |
| [Return command](https://wiki.genexus.com/commwiki/wiki?31353) |

---
