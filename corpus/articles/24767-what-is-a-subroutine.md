---
title: "What is a subroutine?"
source_id: 24767
source_url: https://wiki.genexus.com/commwiki/wiki?24767
genexus_version: "18"
---

# What is a subroutine?

It's a routine that is local to the object in which it is defined. That is to say, it's a block of code identified with a name. From there, it can be run within the object (and only there) using the [Do command](https://wiki.genexus.com/commwiki/wiki?8581).

In this way, if you need to run the same block of code from several places of the object, it can be written once and invoked from various locations.

Subroutines are defined using the [Sub command](https://wiki.genexus.com/commwiki/wiki?8586).

Where are they created? In the objects that accept procedural programming in any of their sections:

* [Transactions](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panels](https://wiki.genexus.com/commwiki/wiki?6916), [Panels](https://wiki.genexus.com/commwiki/wiki?24829), [Work With object](https://wiki.genexus.com/commwiki/wiki?15974): In the events section.
* [Procedures](https://wiki.genexus.com/commwiki/wiki?6293): In the source.

### [Features](#Features)

1. They don't support passing parameters; therefore, to exchange data you use variables that are global to the objects.
2. They are not context-sensitive (beyond variables and object parameters). This has some consequences:

* In the programming defined in a subroutine, using "loose" attributes and expecting them to have the same value they had when making the call is not recommended (the subroutine can be invoked from several places within the object). Therefore, before calling the subroutine it is recommended that you assign these attributes to variables and use these variables in the subroutine.
* If a subroutine contains [For Each](https://wiki.genexus.com/commwiki/wiki?24744) or [New](https://wiki.genexus.com/commwiki/wiki?6714) commands:
  + They won't be nested in For Each or New commands from where the subroutine was called, which means that there won't be any inferences or filters.
  + They won't be nested in implicit For Each commands corresponding to grids or the fixed part of [Web Panels](https://wiki.genexus.com/commwiki/wiki?6916), [Panels](https://wiki.genexus.com/commwiki/wiki?24829), Work Panels.

### [Example](#Example)

If in the Source of a Procedure or in the Events section of any of the above objects you have a For Each command that calls a subroutine:

```
 Do 'Something'
```

and you have the 'Something' subroutine defined as follows:

```
Sub 'Something'
   For each
      …
   Endfor
Endsub
```

The For Each command present in the subroutine will not be nested with the For Each command from where the subroutine was called. They will not be related, meaning that there won't be any automatic filters or inferences of any kind.

**Note**: The attributes used in an object will be global variables in the corresponding generated program. Therefore, if a certain attribute takes value in a certain section of an object, and later a subroutine that also assigns a value to the same attribute is called, when returning from the invoked subroutine and querying the attribute's value it will have the value assigned in the subroutine.


|  |
| --- |
| **Backlinks** |
| [Client-side Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?24332) | [Data Provider Subgroup statement](https://wiki.genexus.com/commwiki/wiki?25412) | [Do command](https://wiki.genexus.com/commwiki/wiki?8581) |
| [For Each command](https://wiki.genexus.com/commwiki/wiki?24744) | [GAM - One Time Password for mobile](https://wiki.genexus.com/commwiki/wiki?50664) | [GAM - Time Based One Time Password for mobile](https://wiki.genexus.com/commwiki/wiki?50708) | [Inline Formulas](https://wiki.genexus.com/commwiki/wiki?6441) |
| [Inline Formulas outside a contextual table](https://wiki.genexus.com/commwiki/wiki?6442) | [Marker Clustering property for Maps in Web Panels](https://wiki.genexus.com/commwiki/wiki?54841) | [Sub command](https://wiki.genexus.com/commwiki/wiki?8586) |

---
