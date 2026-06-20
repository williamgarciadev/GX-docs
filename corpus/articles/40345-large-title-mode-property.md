---
title: "Large Title Mode property"
source_id: 40345
source_url: https://wiki.genexus.com/commwiki/wiki?40345
genexus_version: "18"
---

# Large Title Mode property

Sets the mode to be used when displaying the application bar title.

### [Values](#Values)

|  |  |
| --- | --- |
| **Always** | Always use large titles. |
| **Automatic** | (Default): Enables large titles when the Panel (or Menu) is in a position where large titles are considered the most common use case. |
| **Inherit** | Inherits the mode of the previous object in the stack, and behaves like Automatic when it is the first object. This value is useful for objects (like Menu) that could be called in different places, and its large title mode adjusts to the context. |
| **Never** | Never use large titles. |

### [Scope](#Scope)

**Objects:** [Theme](https://wiki.genexus.com/commwiki/wiki?17876,,)  
**Generators:** [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

iOS 11 adds the concept of large titles:

`[imagen omitida: wiki id 40614]`

The purpose of large titles is to provide extra emphasis on context when needed. In some apps, the big, bold text of a large title can help orient people as they browse and search. In a tabbed layout, for example, large titles can help clarify the active tab and inform the user when they've scrolled to the top. Apple's Phone app uses this approach, while Music uses large titles to differentiate content areas like albums, artists, playlists, and radio. A large title transitions to a standard title as the user begins scrolling content. Large titles don't make sense in all apps and should never compete with content. Although the Clock app has a tabbed layout, large titles are unnecessary because each tab has a distinct, recognizable layout.

### [Use Cases](#Use+Cases)

#### [1. Use large titles in the root of navigation stacks](#1.+Use+large+titles+in+the+root+of+navigation+stacks)

The most common use case for large titles applies to the first panel of a navigation stack. That is, in a Tab-based navigation style, it would be the first panel of each tab. In the Flip-based and Split-based (iPad) navigation style, it will also be the first panel. The general rule is that each navigation style defines which targets are expected to use large titles on its first Panel. Also, if the first object is a Menu instead of a Panel, the large title can also be applied to the second object in the stack (like Mail app does).

#### [2. Use large titles (or not) based on your knowledge of the app](#2.+Use+large+titles+%28or+not%29+based+on+your+knowledge+of+the+app)

Use case 1 covered the most common use case; however, in some cases, this common pattern should be avoided (like the Clock app does).

Note: This property should be used in conjunction with the Scroll Bouncing property defined in [Scroll properties group](https://wiki.genexus.com/commwiki/wiki?40618), as the large title collapses when scrolling:

`[imagen omitida: wiki id 40615]`

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build a main object.

### [Availability](#Availability)

This property is available since [GeneXus 15 upgrade 12](https://wiki.genexus.com/commwiki/wiki?39737,,).

### [See Also](#See+Also)

* <https://developer.apple.com/documentation/uikit/uinavigationitem/2909056-largetitledisplaymode>
* <https://developer.apple.com/documentation/uikit/uinavigationbar/2908999-preferslargetitles>
* <https://developer.apple.com/design/human-interface-guidelines/ios/bars/navigation-bars/>


|  |
| --- |
| **Backlinks** |
| [Scroll properties group](https://wiki.genexus.com/commwiki/wiki?40618) |

---
