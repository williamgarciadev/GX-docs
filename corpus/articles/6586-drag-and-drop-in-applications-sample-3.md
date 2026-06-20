---
title: "Drag and Drop in Applications Sample 3"
source_id: 6586
source_url: https://wiki.genexus.com/commwiki/wiki?6586
genexus_version: "18"
---

# Drag and Drop in Applications Sample 3

Consider a web page of the university site application where a grid displays all the colleges of the university. To view additional information of each college, the user can drag a row of the grid to a "web container" which loads that information automatically. 

In GeneXus terms, that "web container" is a [Web Component control](https://wiki.genexus.com/commwiki/wiki?6056,,) which is dynamically created according to the college dragged to it.

1. Create a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) named "ViewCollege" with the following controls in its form:

* "Colleges" grid: loads CollegeId, CollegeDescription
* CollegeInfoControl is a [Web Component control](https://wiki.genexus.com/commwiki/wiki?6056,,).

`[imagen omitida: wiki id 6594]`

2.  Create also a "CollegeInfo" Web Component which displays the college information, and has the following rule:

parm(CollegeId);

3. In the "ViewCollege" web panel configure the "Allow Drag" property of the "Colleges" grid to True: 

`[imagen omitida: wiki id 6595]`

4.  In the "ViewCollege" web panel code the following "Drop Event". Note that the Web Component is created each time a row of the grid is dragged to the area where the Web Component is drawn in the form. The "in" parameters of the "Drop Event" are CollegeId, and CollegeDescription (the attributes loaded by the grid):

```
Event collegeInfoControl.Drop(&CollegeId,&CollegeDescription)
    collegeInfoControl.Object = CollegeInfo.Create(&CollegeId)
EndEvent
```

### See Also

[Developing Drag and Drop in Web Panels](https://wiki.genexus.com/commwiki/wiki?5579)


|  |
| --- |
| **Backlinks** |
| [Developing Drag and Drop in Web Panels](https://wiki.genexus.com/commwiki/wiki?5579) | [Drop event in Web](https://wiki.genexus.com/commwiki/wiki?9643) |

---
