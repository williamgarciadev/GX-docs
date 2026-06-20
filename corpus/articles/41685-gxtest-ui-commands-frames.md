---
title: "GXtest UI Commands - Frames"
source_id: 41685
source_url: https://wiki.genexus.com/commwiki/wiki?41685
genexus_version: "18"
---

# GXtest UI Commands - Frames

Frames add some challenges in UI automation since locating an element to interact is always relative to each HTML frame. This means that every time you need to interact with elements on different frames, you will need to set the context in your UI test using the SwitchFrame command.

For example, when using Selection Lists or some Prompt Rules in web panels, a typical frame is drawn on top of the original window like here:

`[imagen omitida: wiki id 41689]`

To interact on top of that frame, you need to use the SwitchFrame function.

The function receives a FrameId that needs to be using the following format:

* index=N // where N is the index starting at zero (0)  
  or
* relative=parent // to navigate to "parent" frame  
  or
* relative=top // to navigate to "top" frame

Remember that you can always record the commands using GXtest Recorder, who will automatically add the SwitchFrame commands needed to interact.

## SwitchFrame

`[imagen omitida: wiki id 47335]`

Sets a frame to work with

Parameters:

* FrameId: a special string with frame index ("relative=parent", "relative=top", "index=0", "index=1", ...)

Example of use:

```
&driver.SwitchFrame("index=0")
```

```
&driver.SwitchFrame("relative=top")
```

Note: frame handling can differ in the different browsers. In those cases the WA is to have different commands depending on the browser as follows:

```
if (&driver.GetBrowser() = "Firefox")
    &driver.SwitchFrame("relative=parent")
else
   &driver.SwitchFrame("index=0")
endif
```


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) | [GXtest UI Test for Web - Supported Commands](https://wiki.genexus.com/commwiki/wiki?40281) |

---
