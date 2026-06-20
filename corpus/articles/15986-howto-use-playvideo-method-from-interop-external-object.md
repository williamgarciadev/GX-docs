---
title: "HowTo: Use PlayVideo method from Interop external object"
source_id: 15986
source_url: https://wiki.genexus.com/commwiki/wiki?15986
genexus_version: "18"
---

# HowTo: Use PlayVideo method from Interop external object

This tutorial is a guide for using the PlayVideo method offered by the [Interop external object](https://wiki.genexus.com/commwiki/wiki?23734).

`[imagen omitida: wiki id 54715]`

### [Step 1](#Step+1)

Create a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) with the following attributes:

```
Multimedia
{
   MultimediaId*
   MultimediaVideo //Based on the URL domain. It is NOT based on the standard Video data type.
}
```

### [Step 2](#Step+2)

Apply the [Work With pattern](https://wiki.genexus.com/commwiki/wiki?15975) to it.

### Step 3

Go to the Section (General) node located under the Detail node.

Click on the Events tab:

`[imagen omitida: wiki id 54667]`

Add the following event:

```
Event 'Play'
      Interop.PlayVideo(MultimediaVideo)
EndEvent
```

Finally, go to the Layout tab and insert in the Application Bar a button associated with the 'Play' event:

`[imagen omitida: wiki id 54716]`


|  |
| --- |
| **Backlinks** |
| [Background Modes property](https://wiki.genexus.com/commwiki/wiki?35408) | [Interop external object](https://wiki.genexus.com/commwiki/wiki?23734) | [Interop external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55183) |

---
