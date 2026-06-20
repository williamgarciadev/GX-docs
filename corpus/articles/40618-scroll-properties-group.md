---
title: "Scroll properties group"
source_id: 40618
source_url: https://wiki.genexus.com/commwiki/wiki?40618
genexus_version: "18"
---

# Scroll properties group

In smart devices, in some cases, you need to customize how the scroll behaves and how the scroll indicators look in controls like [Table control](https://wiki.genexus.com/commwiki/wiki?6001) (with [Auto Grow property](https://wiki.genexus.com/commwiki/wiki?20204) = false), grid, form. Even when in most cases the best values could be inferred, in some cases it's not possible and it's up to you to customize what's best.

## [Use Cases](#Use+Cases)

### [1.Customize scroll indicators appearance to match look the background color.](#1.Customize+scroll+indicators+appearance+to+match+look+the+background+color.)

There are different styles of scroll indicators, which looks better depending on the background.

In the image below (left to right), are the available iOS styles:

* Default (dark with light border): looks fine in any background.
* Dark (narrower than Default): looks best with a light background.
* Light (narrower than Default): looks best with a dark background.

`[imagen omitida: wiki id 40619]`

Use [Scroll Indicators Style property](https://wiki.genexus.com/commwiki/wiki?40236) to customize it.

### [2. Hide scroll indicators.](#2.+Hide+scroll+indicators.)

In some cases, like in horizontal/paged grids, or grids with low cardinality, it's better to hide the scroll indicators.

For this, use [Scroll Indicators Visibility property](https://wiki.genexus.com/commwiki/wiki?40235)

### [3. Bounce (or not) when it encounters a boundary of the content.](#3.+Bounce+%28or+not%29+when+it+encounters+a+boundary+of+the+content.)

On iOS, scroll views bouncing visually indicates that scrolling has reached an edge of the content by default.

Depending on the case, bouncing could be desired:

* Only when the content size is bigger than the container's size (Default in most cases).
* Always bounce in one direction (horizontal or vertical), or both. This case is useful when the content amount varies, and it's better to always bounce even when the content fits it's container to hint in other cases (with bigger content) there may be a scroll. I.e. grids in which the number of items may be small, or big, or in forms with a description text which could be short, or very long. This behavior is useful also for force effects like zooming on scroll/parallax, even when the content is small and fits in its container bounds.
* Disable bounce.

Use [Scroll Bouncing property](https://wiki.genexus.com/commwiki/wiki?40237) and [Large Title Mode property](https://wiki.genexus.com/commwiki/wiki?40345), maybe together with the ones of [Scroll behavior properties group](https://wiki.genexus.com/commwiki/wiki?31174) to customize this.


|  |
| --- |
| **Backlinks** |
| [Large Title Mode property](https://wiki.genexus.com/commwiki/wiki?40345) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Scroll behavior properties group](https://wiki.genexus.com/commwiki/wiki?31174) |
| [Scroll Bouncing property](https://wiki.genexus.com/commwiki/wiki?40237) | [Scroll Indicators Style property](https://wiki.genexus.com/commwiki/wiki?40236) | [Scroll Indicators Visibility property](https://wiki.genexus.com/commwiki/wiki?40235) |

---
