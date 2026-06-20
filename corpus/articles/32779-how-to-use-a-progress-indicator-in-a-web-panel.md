---
title: "How To: Use a Progress Indicator in a Web Panel"
source_id: 32779
source_url: https://wiki.genexus.com/commwiki/wiki?32779
genexus_version: "18"
---

# How To: Use a Progress Indicator in a Web Panel

First, the [Progress Indicator User Control](https://wiki.genexus.com/commwiki/wiki?31275) can be dragged from the toolbox to the web form.

See control [Requirements](https://wiki.genexus.com/commwiki/wiki?27740).

`[imagen omitida: wiki id 32778]`

In this example, we execute a "long running task" and we want to notify the user about its progress using a progress bar.

In the web panel we program the following:

```
Event Test1
    LongRunningTask.Submit('')
Endevent
```

Note that the code has to be [submitted](https://wiki.genexus.com/commwiki/wiki?15386) (executed asynchronously).

The LongRunningTask code is as follows:

```
//do something that takes some time
//ProgressIndicator is defined as: Progress (GeneXus.Common.UI)
&ProgressIndicator.Type = ProgressIndicatorType.Determinate
&ProgressIndicator.ShowWithTitle("Executing action")
&ProgressIndicator.Value = 10
//do something that takes some time
&ProgressIndicator.Value = 30
//do something that takes some time
&ProgressIndicator.Value = 70
//do something that takes some time
&ProgressIndicator.Value = 100
//do something that takes some time
&ProgressIndicator.Hide()
```

### [Style of the Progress Indicator](#Style+of+the+Progress+Indicator)

By default, the progress indicator for the web is assigned to the GXProgressBar class under the custom nodes of the Theme.

`[imagen omitida: wiki id 32784]`  
The classes progress-bar-title and progress-bar are descendants of GXProgressBar and may be customized if necessary by using the Theme editor.

You can make changes to it or create a child node of GXProgressBar and set the class to the control at runtime as follows:

```
&ProgressIndicator.Class = "progress-bar-success"
```

Download the sample [here](https://wiki.genexus.com/commwiki/wiki?32785,,).

### [See Also](#See+Also)

[HowTo: Use a Progress Indicator in a Panel](https://wiki.genexus.com/commwiki/wiki?19338)


|  |
| --- |
| **Backlinks** |
| [Progress external object](https://wiki.genexus.com/commwiki/wiki?39341) | [Progress Indicator User Control](https://wiki.genexus.com/commwiki/wiki?31275) |

---
