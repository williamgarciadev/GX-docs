---
title: "PopUp command"
source_id: 6226
source_url: https://wiki.genexus.com/commwiki/wiki?6226
genexus_version: "18"
---

# PopUp command

Makes a call to a modal pop-up window.

### [Syntax](#Syntax)

* *GeneXusWebObject***.Popup(**params**)**
* **PopUp(***GeneXusWebObject*, params**)**

### [Description](#Description+)

This command has a similar behavior than the [Window Data Type](https://wiki.genexus.com/commwiki/wiki?7112). Itallows you to make a call to a modal pop-up window, which means that it blocks the parent application until the user closes it in any way. It can only be used in
[Transaction](https://wiki.genexus.com/commwiki/wiki?1908)s and
[Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) events.

Pop-up windows can be manually resized from their lower right corner.

When opening many PopUps in the same screen, only one (the last one called) is shown at once.

### [Samples](#Samples)

The following image shows two windows, the main one is at the back and the one on the right is the pop-up.

`[imagen omitida: wiki id 6227]`

The fourth button in the main window is a transaction that displays all the airlines to which the on-duty crew member has been associated with. This button is associated with a user event and is programmed as follows (method style):

```
Event 'ViewList'
    RptAirlinesAuto.Popup(&MessageTxt)
EndEvent
```

This is the equivalent of the following code (command style):

```
Event 'ViewList'
    PopUp(RptAirlinesAuto,&MessageTxt)
EndEvent
```

**Note**: When you call a Popup with the GET method, you don´t have control about the maximum URL length. Each browser solves it differently (https://stackoverflow.com/questions/4618013/414-request-uri-too-large-is-this-browser-dependant, https://support.microsoft.com/en-us/help/208427/maximum-url-length-is-2-083-characters-in-internet-explorer)


|  |
| --- |
| **Backlinks** |
| [Load balancing considerations](https://wiki.genexus.com/commwiki/wiki?45291) |

---
