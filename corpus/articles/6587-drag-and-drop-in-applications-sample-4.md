---
title: "Drag and Drop in Applications Sample 4"
source_id: 6587
source_url: https://wiki.genexus.com/commwiki/wiki?6587
genexus_version: "18"
---

# Drag and Drop in Applications Sample 4

Consider a case very similar to [Drag and Drop in Applications Sample 2](https://wiki.genexus.com/commwiki/wiki?6585), but now the "Available Courses" grid is in a web component and the "Courses to Enroll" grid is in another.

1. The first web component looks as shown below. The "Available Courses" grid has the "Allow Drag" property set to TRUE:

`[imagen omitida: wiki id 6601]`

2. The web component where the "Courses to Enroll" grid is located has the following code. Note that the "in" parameters of the "Drop Event" are &CourseId and &CourseDescription, which are the same variables loaded by the grid from where the information is dragged.

```
Event CoursestoEnroll.Drop(&CourseId,&CourseDescription)  
    &CoursetoEnrollId = &CourseId  
    &CoursetoEnrollDescription = &CourseDescription  
    CoursestoEnroll.Load()  
EndEvent
```

Related links: [Developing Drag and Drop in Web Panels](https://wiki.genexus.com/commwiki/wiki?5579)


|  |
| --- |
| **Backlinks** |
| [Developing Drag and Drop in Web Panels](https://wiki.genexus.com/commwiki/wiki?5579) | [Drop event in Web](https://wiki.genexus.com/commwiki/wiki?9643) |

---
