---
title: "Drag and Drop in Applications Sample 2"
source_id: 6585
source_url: https://wiki.genexus.com/commwiki/wiki?6585
genexus_version: "18"
---

# Drag and Drop in Applications Sample 2

Consider a university web site where students may enroll in different courses. There's a grid in the form which loads all the available courses, and another one where the student may drop the courses he/she wants to enroll in.

`[imagen omitida: wiki id 6592]`

1. We have two grids in the form:

* "Courses" grid: variables &CourseId, &CourseDescription
* "Enroll" grid: variables &CourseIdEnroll, &CourseDescriptionEnroll

2. The "Courses" grid has the "Allow Drag" property set to TRUE:

`[imagen omitida: wiki id 6593]`

3. The "Drop" event for the "Enroll" grid is the following.

Note that the "in" parameters of this event are &CourseId and &CourseDescription, the same variables loaded by the "Courses" grid.

```
Event Enroll.Drop(&CourseId, &CourseDescription)
    for each line in Enroll
        Enroll.Load() //reload the preexisting lines
    endfor

  
    &CourseIdEnroll = &CourseId  
    &CourseDescriptionEnroll = &CourseDescription  
    Enroll.Load() //loads the new line added by the Drop  
EndEvent
```

Related links: [Developing Drag and Drop in Web Panels](https://wiki.genexus.com/commwiki/wiki?5579)


|  |
| --- |
| **Backlinks** |
| [Developing Drag and Drop in Web Panels](https://wiki.genexus.com/commwiki/wiki?5579) | [Drag and Drop in Applications Sample 4](https://wiki.genexus.com/commwiki/wiki?6587) | [Drop event in Web](https://wiki.genexus.com/commwiki/wiki?9643) |

---
