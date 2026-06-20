---
title: "Fixed Grid header with vertical scroll"
source_id: 36036
source_url: https://wiki.genexus.com/commwiki/wiki?36036
genexus_version: "18"
---

# Fixed Grid header with vertical scroll

It is possible for a grid in Web environments to set a fixed header. Its purpose is to enable scrolling of the whole grid keeping the column headers visible at any time.

To use it you need to:

* Set the grid [Auto Resize property](https://wiki.genexus.com/commwiki/wiki?8687) to false.
* Set the grid [Height property](https://wiki.genexus.com/commwiki/wiki?8792) to some value different from 0; for example you could set a fixed size such as 500px or relative values such as 80vh or 80% (or any other value).
* Set the grid [Rows property](https://wiki.genexus.com/commwiki/wiki?2452) to 0 so [paging](https://wiki.genexus.com/commwiki/wiki?6086) is disabled).

The grid header will be fixed and you will be able to scroll through your data as details the following image:

`[imagen omitida: wiki id 36037]`

### [Availability](#Availability)

This options is available since [GeneXus 15 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?35908,,).
