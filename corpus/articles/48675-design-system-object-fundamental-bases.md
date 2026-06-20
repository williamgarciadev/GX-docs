---
title: "Design System Object - Fundamental bases"
source_id: 48675
source_url: https://wiki.genexus.com/commwiki/wiki?48675
genexus_version: "18"
---

# Design System Object - Fundamental bases

The [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375) is introduced as part of an evolution of GeneXus aimed at a more organic integration of the overall [concept of Design System](https://wiki.genexus.com/commwiki/wiki?40108), which is already well established in the field of digital application design and development. The objective is to simplify its implementation by strengthening two essential properties: productivity and economy; that is, to achieve great expressiveness with a few well-articulated elements.

This object is meant to replace the [Theme](https://wiki.genexus.com/commwiki/wiki?4375), including its [classes](https://wiki.genexus.com/commwiki/wiki?49309) and [Color Palette](https://wiki.genexus.com/commwiki/wiki?31262). In its next evolution, it will also allow defining the default rendering of the controls inserted in your application screens. You will even be able to specify that whenever a control is inserted in a layout, it should always adopt certain style properties.

In short, this object will centralize all the design aspects of your screens in a more articulable, granular and flexible way than the Theme.

Unlike the Theme, the Design System object can be composed of other Design System objects, and even with CSS for the web, thus creating true cascading designs in your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836)s.

In this way, you can define the design of one part of the application in a Design System Object (DSO) and, for more specific parts, create DSOs that extend the first one and/or specialize it.

A single DSO may provide a multi-experience design that can be applied to web, web Angular or native mobile screens. Everything is in the same object, unlike what happened with Themes.

There is more power, allowing for more varied scenarios without increasing complexity.

What follows is an introduction to its concept and use through a very simple example.

All of this is aligned, of course, with a [DesignOps](https://wiki.genexus.com/commwiki/wiki?47020) methodology: the software development cycle is named in a way that integrates designers in the implementation of the end solution.

The Design System Object seeks to bring the roles of designer and developer closer together, reducing the need to translate from one language (the designer's) to another (the developer's). In addition, the end product is viewed as an articulation of design and behavior elements that must be integrated and assembled, making economical use of resources: not repeating duplicates, granularizing so as to assemble larger structures from smaller pieces, not adding what is not going to be used, etc. To this end, as we have always done in GeneXus, we prioritize the capacity for abstraction.

### [Availability](#Availability)

Since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?48684,,).


|  |
| --- |
| **Backlinks** |
| [Toc:Design Systems](https://wiki.genexus.com/commwiki/wiki?40108) |

---
