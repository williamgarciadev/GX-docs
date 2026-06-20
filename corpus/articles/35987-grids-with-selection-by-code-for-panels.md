---
title: "Grids with Selection By Code for Panels"
source_id: 35987
source_url: https://wiki.genexus.com/commwiki/wiki?35987
genexus_version: "18"
---

# Grids with Selection By Code for Panels

Grid selection is an important feature to achieve the best user experience.

In GeneXus, there are several alternatives for managing Grid selection.

The first alternative is provided automatically by setting [multiple layouts for the Grid control](https://wiki.genexus.com/commwiki/wiki?22556). Another option consists in manipulating the selected items by using programming strategies adapted to the business logic of the application. This document focuses on the principles of this last alternative, for the automatic case please refer to [Default Selected Item Layout property](https://wiki.genexus.com/commwiki/wiki?22556) article.

## [Selection by code](#Selection+by+code)

There are four features that help you to manipulate Grid item selection by code.

* [SelectedItem property](https://wiki.genexus.com/commwiki/wiki?36232)
* [Select method](https://wiki.genexus.com/commwiki/wiki?36234)
* [Deselect method](https://wiki.genexus.com/commwiki/wiki?36235)
* [SelectionChanged Event](https://wiki.genexus.com/commwiki/wiki?36236)

## [Usage example](#Usage+example)

Suppose you need to design a simple music playlist application.

The requirements are:

* The user can tap on any item to play it; this action changes the selected item on the Grid.
* When a song finishes, the next one should be played automatically and the selected item on the Grid must change accordingly.

In other words, the aim will be to keep in sync both the Grid and the media queue (facilities provided by the [Audio external object](https://wiki.genexus.com/commwiki/wiki?30041)).

First, you have to design how the music list will look on a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829). Basically, it will be a Grid control where each item is a song (you display its title, subtitle and cover image). This Grid will have two layouts: one for displaying the song currently playing, and another one for the rest of the songs in the playlist. This first layout will be set as the [Default Selected Item Layout property](https://wiki.genexus.com/commwiki/wiki?22556).

|  |  |
| --- | --- |
|  |  |

The <default> value in [Default Action property](https://wiki.genexus.com/commwiki/wiki?20424) won't have any effect because the Grid control is embedded in a Panel object (different from the WorkWith object which will display the Detail node). Then, you can write the code of the SelectionChange event without worrying about whether the Default Action will be triggered or not. In this scenario, you can get the selected index from the grid and use it with SetQueueCurrentIndex method of the [Audio external object](https://wiki.genexus.com/commwiki/wiki?30041) before start playing it or while it is playing another song.

```
Event Grid1.SelectionChanged
    Composite
        &Index = Grid1.SelectedIndex
        Audio.SetQueueCurrentIndex(&Index)
    EndComposite
EndEvent
```

With these settings, any song will start playing when the end user taps on it from the playlist. But, there is another scenario that you must satisfy: when a song has finished playing, the application should select on the Grid the next one from the playlist. In order to do that, before starting the next song, you may use the QueueItemFinished event from [Audio external object](https://wiki.genexus.com/commwiki/wiki?30041) facilities and select the appropriate index. For example, you can write the event in a very simple way as follows:

```
Event Audio.QueueItemFinished(&MediaItemFinishedInfo)
    Composite
        If &MediaItemFinishedInfo.Reason = MediaFinishReason.PlaybackCompleted
            &Index = &MediaItemFinishedInfo.QueuePosition
            Grid1.Select(&Index)
        EndIf
    EndComposite
EndEvent
```

Finally, you get the following result.

`[imagen omitida: wiki id 36217]`

## [Note](#Note)

* For those grids which [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) is out of scope (such as Image Gallery, Leaves, etc.) the behavior of the described elements in this document are:
  + The Select/Deselect methods do not have any effect.
  + The SelectedIndex will return empty (value 0).
  + The SelectionChanged event will never be triggered.

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Controls:** | [Grid control](https://wiki.genexus.com/commwiki/wiki?24817), [Horizontal Grid control](https://wiki.genexus.com/commwiki/wiki?18180) (Apple). |
| **Generators:** | [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550) |

##


|  |
| --- |
| **Backlinks** |
| [Deselect method](https://wiki.genexus.com/commwiki/wiki?36235) | [Deselect method (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54487) |
| [Select method](https://wiki.genexus.com/commwiki/wiki?36234) | [Select method (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54486) | [SelectedItem property](https://wiki.genexus.com/commwiki/wiki?36232) | [SelectionChanged Event](https://wiki.genexus.com/commwiki/wiki?36236) |
| [SelectionChanged Event (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54483) |

---
