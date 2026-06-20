---
title: "HowTo: Responsive vertical centering"
source_id: 30650
source_url: https://wiki.genexus.com/commwiki/wiki?30650
genexus_version: "18"
---

# HowTo: Responsive vertical centering

This document explains how to center an element vertically and responsively by showing you an example.

Consider a [Responsive Web Applications](https://wiki.genexus.com/commwiki/wiki?25159) where the login window has to be centered on the web page. By setting an element’s width, height and margins in [viewport units](https://wiki.genexus.com/commwiki/wiki?30636), you can center it easily.

In this example, the login Web Panel's Main [Responsive Table](https://wiki.genexus.com/commwiki/wiki?24961) has the Class property set to "TableCenter", which is a class defined in the Theme.

`[imagen omitida: wiki id 30652]`

The "TableCenter" class has the following properties:

```
    width: 60vw;
    height: 60vh;
    margin: 20vh auto;
```

`[imagen omitida: wiki id 30653]`

At runtime it looks as follows:

`[imagen omitida: wiki id 30651]`

Running on a phone, it looks like this:

`[imagen omitida: wiki id 30654]`


|  |
| --- |
| **Backlinks** |
| [Using relative length units on the web](https://wiki.genexus.com/commwiki/wiki?30636) |

---
