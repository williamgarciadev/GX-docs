---
title: "IsValid Event for Web Applications"
source_id: 6564
source_url: https://wiki.genexus.com/commwiki/wiki?6564
genexus_version: "18"
---

# IsValid Event for Web Applications

IsValid events are useful for validating a field in the web form, or just triggering actions after exiting a field in the form.

* In Edit controls, the IsValid event is triggered upon exiting the field. In check boxes, list boxes, combos and radio buttons, this event is triggered when a value is selected in the control.
* Only changes in fields are detected in web form validations, that is, if the field values don't change, the isvalid event won't be triggered (except the first time). It's the same behavior as in client side validation in web transactions.
* The messages inside the IsValid event are displayed in the ErrorViewer control.

IsValid validation is only executed when the focus is moved "forward". If you use Shift-Tab or manually click on another control which is located before the current selection, the IsValid Event will not be triggered.

### [IsValid behavior in web](#IsValid+behavior+in+web)

1. If the Isvalid event is associated to an attribute in a web transaction, the event will be triggered when the field entered is valid. In this case GeneXus rules, referential integrity, etc. are triggered before the IsValid event.

For example, TeacherId is a foreign key in "Course" Transaction. When the TeacherId is entered, if it's referential integrity checks are right, the IsValid event will be triggered afterwards.

```
Event teacherId.IsValid
    &window.Height = 100
    &window.Width = 200
    &window.Object = TeacherView.Create(TeacherId)
    &window.Open()
EndEvent
```

2. If you have &a, &b, &c in the form, what happens when the cursor is in &a and the user goes to the &c field with the mouse?

In this case, in the first time &a.isvalid and &b.isvalid events will be triggered. Then, the following times only &a.isvalid will be triggered if the associated value is explicitly changed.

3. If you have &a, &b, &c in the form, what happens when the cursor is in &c and the user goes to the &a field with the mouse?

In this case the events won't be triggered (they are not triggered when you go backwards).

### [One case of use](#One+case+of+use)

1. Suppose you have a &CollegeId variable in the form. After entering a value for that field, you want to create a web component showing the college information.

```
Event &CollegeId.IsValid
    webComp1.Object = CollegeInfo.Create(&CollegeId)
EndEvent
```

### [Event triggering](#Event+triggering)

The IsValid event is triggered like any other event, taking into account that :

* If the code inside the event can be evaluated entirely in the client, it's executed in the client. Start, Refresh, Load events are not triggered.
* If the code inside the event needs to be evaluated in the database server, it's executed in the web server. Start, Refresh, Load events are triggered in the same order as usual.

In both cases event triggering is solved using AJAX.

See [here](https://wiki.genexus.com/commwiki/wiki?6563,,) for more information.

#### [Important note](#Important+note)

In most cases IsValid events are used for validating fields, so they are used in combination with the setfocus method, as in the following example:

```
Event &StudentId.IsValid
    If &StudentId.IsEmpty()
       Msg('StudentId mandatory field')
      &StudentId.SetFocus()
    EndIf
EndEvent
```

The behavior in web applications will be different than in win applications. In win applications, the focus will not leave the field until a &StudentId other than 0 is entered.

In web applications, the following will happen:

1. The user enters 0 in the &StudentId field, so the condition (if &StudentId.IsEmpty()) will evaluate to TRUE, then, the message will be displayed. The focus will be set on the &StuentId field also.

2. Again, if the user tries to get out of the field (this time without changing it's value, just leaving the field empty), the focus will leave the field. That's because only changes in fields are detected in web form validations.

As a consequence, in general, the setfocus command should not be used for IsValid web events.


|  |
| --- |
| **Backlinks** |
| [Category:Context Sensitive User Interfaces](https://wiki.genexus.com/commwiki/wiki?5285) |
| [Events in Transactions](https://wiki.genexus.com/commwiki/wiki?8042) | [IsValid event](https://wiki.genexus.com/commwiki/wiki?8049) | [SetFocus method](https://wiki.genexus.com/commwiki/wiki?8836) |

---
