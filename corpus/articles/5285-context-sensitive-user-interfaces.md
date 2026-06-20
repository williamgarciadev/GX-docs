---
title: "Context Sensitive User Interfaces"
source_id: 5285
source_url: https://wiki.genexus.com/commwiki/wiki?5285
genexus_version: "18"
---

# Context Sensitive User Interfaces

The current trend is to implement Intent-oriented interfaces, which can be approached by keeping track of the application context and taking actions accordingly.

The best way to introduce this feature is to give an example: Suppose that you have a web page which loads two web components. One of them has a list of all the colleges (or faculties) in a university. Another component displays the college details (photo and description).

The first component saves the collegeid in the context when a college is selected by the user. The other component tracks the context changes and therefore loads the corresponding information as soon as the collegeid is selected.

`[imagen omitida: wiki id 8165]`

### [What Do We Call Context?](#What+Do+We+Call+Context%3F)

When we say Context, we mean the context of our application in a form. When we access the CustomerId Textbox, our context is CustomerId; when we access the invoice lines grid, our context is the invoice line; and so on. When we move inside a screen, we're changing the context of attributes and variables. This information about context changes is essential when creating an intent-oriented interface.

Our approach enables us to trigger events and take actions depending on the context information of the application (the place where the cursor is positioned).

Suppose that the application consists of several web components which make up the web form. You can easily trigger an event in one of the web components as soon as the end user changes his/her context information in another component (changes the focus to a control, or selects a grid line).

Basically, the web controls that you want to track changes in "subscribe" to an event which listens to the context changes of any other control.

By programming a *TrackContext* event, the programmer retrieves the context information and takes the desired actions. That's all!

### [Implementation Details](#Implementation+Details)

**NotifyContextChange Property**  
  
Applies to the following controls: grids, freestylegrids, grid columns, attributes/variables.  
  
If the Notify Context Change property is set for a control, the context is saved by default with the corresponding information.

For attributes and variables, it only applies to fields that are not read-only (it can be any control: edits, checkboxes, comboboxes, radio buttons). When the variable/attribute is focused, the context is saved with that information. Value changes in the variable/attribute are not detected, only the cursor's focus on it. The same happens for attributes/variables in freestyle grids.

In the case of standard grids:

* by selecting a row, the entire row is saved in the context.

In the case of standard/freestyle grids:

* for grids bound to SDT collections, select the grid title and all the grid information is tracked in the context (1).

You can change the information that is tracked by programming the SetContext event (explained below).

For example, Notify Context Change Property in grid control:

`[imagen omitida: wiki id 6370]`

**SetContext Event**

It applies to the same controls as the NotifyContextChange property: grids, freestylegrids, grid columns, attributes/variables.

Syntax: Event <control>.SetContext(parameter)

It can only be one SDT-type variable parameter. It means the context will be loaded in that parameter.  
It's a way of changing the information tracked in the context for a control.

**TrackContext Event**  
  
Syntax: Event TrackContext(parameters)

The parameters can only be variables.  
The event is qualified by the parameters it receives; that is to say, you may have any number of *TrackContext Events* in your source code, and they are distinguished by the parameters they receive.

Notes:

1. Any parameter which is not a Structured Data Type (SDT) is qualified by name.  
   If you have the following in an object "A":  
       
      Event TrackContext(&X)  
      EndEvent  
     
   Any object "B" which has a variable &X with the NotifyContextChange property set to TRUE (in the form or in a grid) will subscribe to that TrackContext event. The same happens with an attribute named "X".
2. Any parameter which is a Structured Data Type is qualified by type. That is to say,  
   If you have the following in an object "A", where &sdtvar1 is based on SDT:  
       
      Event TrackContext(&sdtvar1)  
      EndEvent  
     
   Any object "B", which has a grid with "Notify Context" that loads a &sdtvar2 variable also based on an SDT, will subscribe to that TrackContext event.
3. The following applies to all subgroups:  
   Suppose you have the following events in the same object:

             Event TrackContext(param1, param2,..., paramN)  
             EndEvent

             Event TrackContext(param1, param2)  
             EndEvent

**Both** events will be triggered as param1, param2, paramN notify their context.

### [Examples and Use Cases](#Examples+and+Use+Cases)

1. When selecting an element from a grid (for example, "Colleges"), show the detailed information about the College next to it (this information may or may not be in the same web component of the "Colleges grid").  
  
`[imagen omitida: wiki id 6371]`  
  
`[imagen omitida: wiki id 6372]`

2. When selecting a foreign key field, show a contextual prompt.

3. When selecting a field, show a textblock with Help information next to it. It's very easy! Suppose that you have three fields in the form: &courseid, &coursedescription, &courseprerequisites. You want to show a contextual help each time the focus is on one of these fields. Thus, you may code as follows:

```
Event TrackContext(&courseId)
  textBlock1.Caption = 'Course Identification. Required field'
EndEvent
Event TrackContext(&coursedescription)
  textBlock2.Caption = 'Course Description. Required field'
EndEvent
Event TrackContext(&courseprerequisites)
  textBlock3.Caption = 'Course Prerequisites.'
EndEvent
```

`[imagen omitida: wiki id 6374]`

4. Load information without posts! Suppose you have two web components in your web form. One of them displays a grid with college degrees. The other web component displays a grid which loads all the courses of that degree program. You can load the second grid depending on the line selected in the first one, just by reading the context and without posting the entire web form!

`[imagen omitida: wiki id 6375]`

The "Careers" grid has the Notify Context Change property set to true.

The code in the web component where the "Courses" grid displays is the following:

```
Event TrackContext(&CareerId,&careerDescription)
   for each 
       where CareerId = &CareerId
            &CourseId = CourseId
            &CourseDescription = CourseDescription
            &CoursePrerequisites = CoursePrerequisites
            coursegrid.Load()
   endfor
EndEvent
```

Notes:

(1) In the future it will be possible to track all of the grid's information regardless of whether it is bound to an SDT Collection or not.

**FAQ**  
Q: Can I use the "Context functionalities" to make form validations, for instance, to validate data entered by the user?  
A: Changes in field values are not detected, so this functionality cannot be used to validate the form. For information on validating forms, click [here](https://wiki.genexus.com/commwiki/wiki?6564).  
  
Q: What user actions are detected as Context changes?  
A:

1. The cursor's position in a form field (the change of position is detected when the user moves with either the mouse or the tab key). The form field can be an edit control, dynamic/combobox, checkbox, or listbox, all of them NON read-only. Changes in field values are not detected; only the position or selection of the cursor in that field is detected.
2. The click on a grid column, row, or the grid itself. In this case, the grid rows can be ReadOnly.

`[imagen omitida: wiki id 6373]`


|  |
| --- |
| **Pages** |
| [Notify Context Change property](https://wiki.genexus.com/commwiki/wiki?8856) |

---
