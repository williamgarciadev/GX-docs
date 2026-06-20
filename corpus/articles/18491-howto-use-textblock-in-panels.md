---
title: "HowTo: Use Textblock in Panels"
source_id: 18491
source_url: https://wiki.genexus.com/commwiki/wiki?18491
genexus_version: "18"
---

# HowTo: Use Textblock in Panels

This article shows you the steps to use a TextBlock in a Panel.

The Textblock control is used to show text in the layouts of [Panel](https://wiki.genexus.com/commwiki/wiki?24829). The main aim of this control is to show any kind of information that can be displayed as text, to the user. In this tutorial, it is explained how to use a [Text Block](https://wiki.genexus.com/commwiki/wiki?5948) in Panels.

Firstly, create a new Panel object. The next step is to drag and drop from the toolbox, a text block to the layout. Should look like this if successfully dropped:

`[imagen omitida: wiki id 53758]`

Then you can change its [Caption property](https://wiki.genexus.com/commwiki/wiki?4633) to display any information you need to:

`[imagen omitida: wiki id 53760]`

Done!

At runtime you can do this:

```
Event Start
    Textblock1.Caption = 'Hello world'
EndEvent
```

`[imagen omitida: wiki id 53761]`
