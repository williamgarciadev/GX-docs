---
title: "HowTo: Using the ShowError method from Interop in Native Mobile applications"
source_id: 51446
source_url: https://wiki.genexus.com/commwiki/wiki?51446
genexus_version: "18"
---

# HowTo: Using the ShowError method from Interop in Native Mobile applications

This method performs the equivalent of what is automatically done to display errors when a [Composite command](https://wiki.genexus.com/commwiki/wiki?17389) fails in a Native Mobile application.  
  
**Return value:**[Numeric](https://wiki.genexus.com/commwiki/wiki?6793)(3).

|  |  |
| --- | --- |
| **Value** | **Description** |
| 0 | No error |
| 1 | Unknown error |
| 2 | User canceled the action |
| 3 | Incorrect parameters |

When the action to be executed invokes a GeneXus object located on the server side—for example, an online [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) or [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270)—the returned value corresponds to the HTTP code returned by this call (for example, 404 or 500). If there is no response from the server, the [&Err variable](https://wiki.genexus.com/commwiki/wiki?51028) will have the value 1.

**Parameters:**none.

### [**Samples**](#Samples)

**1)**Sometimes it is necessary to use the Composite command to handle errors, butit is also necessary to implement something else. For example, suppose you have to solve a favorites toggle button in an online application.

The event can be defined as shown below:

```
Event “ToggleFavorites”
  Composite
     &IsFav = not &IsFav
     ProcSetFav(&IsFav) // The Procedure changes the style with dynamic properties to show the current state (if it is favorite or not). 
  EndComposite
EndEvent
```

The problem with this solution is that the appearance is changed but it is done after a round trip to the server, so the UX is not good. Besides, if the Procedure fails, the &IsFav value will have a wrong state.

Another solution could be:

```
Event “ToggleFav”
  Composite
     &IsFav = not &IsFav
     Control.Class = iif(&IsFav, !"FavClass”, !“FavClass”)
     ProcSetFav(&IsFav) // In this case the Procedure only saves the new favorite state
  EndComposite
EndEvent
```

This solution gives good UX feedback, but it has the same issues as the previous solution in the sense that if the Procedure fails, the &IsFav value will have a wrong state.

So, consider the following solution that uses the **Interop.ShowError** method:

```
Event “ToggleFav”
  Do ’ToogleIsFav’
  ProcSetFav(&IsFav) // // In this case the Procedure only saves the new favorite state
  if Interop.ShowError() <> 0
    Do ’ToogleIsFav’ // Restores the state before the Procedure failed
endif 
EndEvent 

Sub ’ToogleIsFav’ 
   &IsFav = not &IsFav 
   Control.Class = iif(&IsFav, !oFavClass”, !“FavClass”) 
EndSub
```

The **Interop.ShowError()** method is provided by GeneXus and does the same as is done automatically to display errors when [Composite command](https://wiki.genexus.com/commwiki/wiki?17389)s fail.

It solves the same as the following GeneXus code:

```
Sub “ShowError”

  if &err <> 0 and &err <> 2 // Error no Cancel
    if &errMsg.IsEmpty()
      msg(“GXM_ThereWasAnErrorExecutingAction”)
    else
      msg(&errMsg)
    endif
  endif
EndSub
```

In addition, to facilitate evaluations in [If command](https://wiki.genexus.com/commwiki/wiki?8608)s, the returned &Err variable is loaded.  
  
**2)** The following code doesn't have a [Composite command](https://wiki.genexus.com/commwiki/wiki?17389) and shows the errors using the Interop.ShowError method:

```
Event 'InsertNewUser'
    &ErrorResult.SetEmpty()
    ProcNewUser(&UserInformation)
    &ErrorResult = Interop.ShowError()
    if &ErrorResult <> 0
        //Some code...
    Else
        msg("A new user was added successfully", nowait)
    EndIf
Endevent
```

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Availability](#Availability)

Since [GeneXus 17 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?49972,,).

### [See Also](#See+Also)

[Interop external object](https://wiki.genexus.com/commwiki/wiki?23734)


|  |
| --- |
| **Backlinks** |
| [Interop external object](https://wiki.genexus.com/commwiki/wiki?23734) | [Interop external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55183) |

---
