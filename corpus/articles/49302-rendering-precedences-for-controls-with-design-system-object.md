---
title: "Rendering precedences for controls with Design System Object"
source_id: 49302
source_url: https://wiki.genexus.com/commwiki/wiki?49302
genexus_version: "18"
---

# Rendering precedences for controls with Design System Object

When executing a [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) or [Panel object](https://wiki.genexus.com/commwiki/wiki?24829), to render each control of the object at runtime:

1.    The corresponding style object must be determined. To do so:

●    **Web Panel:** The value of the object's Style property is taken. There you will find the name of a [Design Systems](https://wiki.genexus.com/commwiki/wiki?40108) or a [Web Theme](https://wiki.genexus.com/commwiki/wiki?6420).   
●    **Panel:** The value of the [Style property in Map User Control](https://wiki.genexus.com/commwiki/wiki?42433) corresponding to the Platform where the application is running is taken. For example, if you are running on an Android phone, it will be the value of the Style property of the Android Phone platform. Again, there you will find the name of a Design System or Theme.   
●    **Both:** If the style object for the Web Panel or Panel has been changed at runtime ([SetTheme function for Web](https://wiki.genexus.com/commwiki/wiki?21777) or [SetTheme function](https://wiki.genexus.com/commwiki/wiki?41978)), the dynamic and not the static one is chosen.

2.    It is necessary to determine how to render each control. Only the case in which a [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375) (DSO) was identified in step 1 will be analyzed.

●    The associated class or classes are identified (if they are associated statically and dynamically, the latter ones prevail).  
●    These classes are searched for in the style object found in step 1.  
●    For a DSO importing another one or more: it’s as if the styles and/or tokens sections (or CSS if one of these files was imported directly) were copied in the order in which they were imported into the Tokens and Styles sections of the current DSO (which is always before the specific token and style definitions of the current DSO). Therefore, there may be repeated classes.    
●    If in the classes identified for the control to be rendered:  
               ○    There are repeated ones in the DSO (extended), the definitions of all of them are taken (union), except for the repeated properties, where the last one defined is valid.  
               ○    The same class, in addition to being defined without conditions, is also defined with conditions (for example, with an @media rule for screen size and/or orientation), it’s as if the unconditional one had been written first, followed by the conditional one; therefore, if some properties overlap, the last ones, those of the conditional one, are taken. Of course, the conditional class only applies if the application is running in the context that meets the condition (for example, on that screen size).   
●    If the control has properties defined (such as Height or Width), they will always take precedence over their class counterparts, so they will be the ones applied.

3.    Other more subtle aspects, such as whether the control has a link property, or is read-only, etc., will also matter in determining its stylistic behavior. For example, if the control is a Text Block and has the Link property configured, in a Web platform it will be rendered with the typical blue color for browser links even if the color property of the associated class says otherwise. This is unless the associated class specifies the class that governs the style for a link, and the desired color is configured there.

### [Availability](#Availability)

Since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?48684,,).

### [See also](#See+also)

[Structuring classes in Design System](https://wiki.genexus.com/commwiki/wiki?49292)

###


|  |
| --- |
| **Backlinks** |
| [Design System Class](https://wiki.genexus.com/commwiki/wiki?49309) | [Design System Styles](https://wiki.genexus.com/commwiki/wiki?47379) | [Toc:Design Systems](https://wiki.genexus.com/commwiki/wiki?40108) |
| [Structuring classes in Design System](https://wiki.genexus.com/commwiki/wiki?49292) |

---
