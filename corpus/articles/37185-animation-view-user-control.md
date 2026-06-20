---
title: "Animation View User Control"
source_id: 37185
source_url: https://wiki.genexus.com/commwiki/wiki?37185
genexus_version: "18"
---

# Animation View User Control

Animation View is a User Control whose purpose is to allow you to [integrate animations](https://wiki.genexus.com/commwiki/wiki?37189) in applications screens and manage their behavior.

This control is distributed with GeneXus. The control can be found in the Miscellaneous section of the Toolbox and should be dragged to the layout of a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916), [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) or [Work With object](https://wiki.genexus.com/commwiki/wiki?15974).

`[imagen omitida: wiki id 53522]`

## [Methods](#Methods)

### [SetAnimation](#SetAnimation)

With this method, a [Lottie](https://airbnb.design/lottie/) animation is loaded in the control using the Animation classes of the [Theme object](https://wiki.genexus.com/commwiki/wiki?16595).

#### Syntax SetAnimation(*AnimationClass*, *Loop*)

**Where:**

|  |  |  |
| --- | --- | --- |
| **Parameter** | **Type** | **Description** |
| AnimationClass | Character | Class of the Theme or DSO with the animation to be loaded. |
| Loop | Boolean | Indicates if the animation will be played in a loop or not. |

#### Sample

```
Event Start
   AnimationView1.SetAnimation(StyleClass:Birthday, true)
Endevent
```

### [SetProgress](#SetProgress)

#### [This method allows setting the progress of the animation (already set with the SetAnimation method) to any point.](#This+method+allows+setting+the+progress+of+the+animation+%28already+set+with+the+SetAnimation+method%29+to+any+point.)

#### [Syntax](#Syntax)

SetProgress(*Progress*)

**Where:**

|  |  |  |
| --- | --- | --- |
| **Parameter** | **Type** | **Description** |
| Progress | Numeric | Value from 0 to 1 indicates the percentage of progress from where the animation will start. |

#### Sample

```
Event 'SetProgress'
   &Progress = 0.5
   AnimationView1.SetProgress(&Progress)
Endevent
```

### [Play](#Play)

Used to start the animation.

#### [Syntax](#Syntax)

Play(*FromPosition -optional-*, *ToPosition* -*optional*-)

**Where:**

|  |  |  |
| --- | --- | --- |
| **Parameter** | **Type** | **Description** |
| FromPosition | Numeric | Value from 0 to 1 indicates the position (progress) from where the animation execution will start. |
| ToPosition | Numeric | Value from 0 to 1 indicates the position (progress) to where the animation execution will finish. |

#### Samples

```
Event 'PlayAnimation'
   // Animation will be execution completly
   AnimationView1.Play()
Endevent

Event 'PlayAnimation2' 
   // Animation will be executed until the middle point
   // If only one parameter is indicated, it is used as ToPosition
   AnimationView1.Play(0.5) 
Endevent

Event 'PlayAnimation3' 
   // Animation will be executed from the middle point to 3/4 progress
   AnimationView1.Play(0.5, 0.75) 
Endevent
```

### [Pause](#Pause)

Used to pause the animation.

#### [Syntax](#Syntax)

Pause()

#### [Sample](#Sample)

```
Event 'PauseAnimation'
   AnimationView1.Pause()
Endevent
```

## [Scope](#Scope)

**Generators**: [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Objects**: [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)


|  |
| --- |
| **Backlinks** |
| [Category:Common Controls](https://wiki.genexus.com/commwiki/wiki?5928) | [HowTo: Include animations in Native Mobile and Angular apps](https://wiki.genexus.com/commwiki/wiki?37189) |

---
