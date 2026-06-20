---
title: "Intersection Observer control"
source_id: 55147
source_url: https://wiki.genexus.com/commwiki/wiki?55147
genexus_version: "18"
---

# Intersection Observer control

The Intersection Observer control allows detecting the visibility of a control (Target) in relation to the browser window (Root).

### [Scope](#Scope)

**Generators:** [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

You can find this control in the [Toolbox](https://wiki.genexus.com/commwiki/wiki?10000) and drag it, for example, to the Layout of a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829). At runtime, when the user scrolls the page (the Panel) in the browser, it is possible to know the visibility percentage of each control inside it.

`[imagen omitida: wiki id 55150]`

Once the control is included, it looks as follows:

`[imagen omitida: wiki id 55151]`

### [Slot](#Slot)

The Intersection Observer control contains a Slot (also known as Target control). Inside it, you can define the layout on which you want to detect visibility changes.

Optionally, the Intersection Observer control can be used without specifying the Target layout (leaving it empty). In this case, it can be used as a marker to indicate when a certain intersection occurs.

**Note**: To use this control, the [GeneXusUIControls module](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?60714,,) must be installed.

For more information, read [https://developer.mozilla.org/enUS/docs/Web/API/Intersection\_Observer\_API](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API).

### [Properties](#Properties)

|  |  |  |  |
| --- | --- | --- | --- |
| **Property** | **Type** | **Scope** | **Description** |
| Top Root Margin | string | DesignTime | Top Margin around the Root element.  Accepts values such as 50dip or 10%. |
| Right Root Margin | string | DesignTime | Right Margin around the Root element.  Accepts values such as 50dip or 10%. |
| Bottom Root Margin | string | DesignTime | Bottom Margin around the Root element.  Accepts values such as 50dip or 10%. |
| Left Root Margin | string | DesignTime | Left Margin around the Root element.  Accepts values such as 50dip or 10%. |
| Threshold | string | DesignTime | It is an array of numbers (with values from 0 to 100) containing the points at which the IntersectionUpdate event is executed (see description of the IntersectionUpdate event below), depending on the visibility of the Target control.    For example:  25, 50, 75  In this case, the IntersectionUpdate event will be executed when the Target control is 25%, 50%, or 75% visible in relation to the Root container. |
| Intersection Ratio | numeric | RunTime | It is a number that indicates the visibility percentage of the Target control. This value is updated every time the IntersectionUpdate event is executed. |

**Notes**:

* The Root Margin properties are used to increase or reduce each side of the container box of the Root control before calculating the intersections.
* Since this control is not a "visual control", it cannot be styled.

### [Events](#Events)

#### [IntersectionUpdate](#IntersectionUpdate)

* **Description:** This event is executed every time the target control crosses some visibility threshold specified in the Threshold property.
* **Parameters:** None.

**Note**: The IntersectionUpdate event is also executed when the IntersectionObserver control is loaded in the application.

### [Samples](#Samples)

The following code shows an example of general use:

```
Event IntersectionObserver.IntersectionUpdate
    If IntersectionObserver.IntersectionRatio > 25
        // Do something
    EndIf
EndEvent
```

Following are two samples whose complete implementation is provided in an .xpz file below.

#### [**Sample 1) How to use the control to implement a custom Header.**](#Sample+1%29+How+to+use+the+control+to+implement+a+custom+Header.)

When scrolling down at runtime, a certain header is displayed.

1.1) In the [Panel](https://wiki.genexus.com/commwiki/wiki?24829) containing the control called IntersectionObserverHRP, the following event is defined:

```
Event IntersectionObserverHRP.IntersectionUpdate
    GlobalEvents.ChangeAppBarVisibility(IntersectionObserverHRP.IntersectionRatio = 0)
EndEvent
```

2.2) In the [Master Panel](https://wiki.genexus.com/commwiki/wiki?46247), the following is defined:

```
Event GlobalEvents.ChangeAppBarVisibility(&Visible)
    TblAppBar.Visible = &Visible
EndEvent
```

#### 

#### [**Sample 2) How to use the control to animate the application UI when scrolling the page.**](#Sample+2%29+How+to+use+the+control+to+animate+the+application+UI+when+scrolling+the+page.)

In the Panel containing the controls IntersectionObserver1, IntersectionObserver2, IntersectionObserver3, the following is defined:

```
Event IntersectionObserver1.IntersectionUpdate
    If NOT &ComingSoon1_Visible AND IntersectionObserver1.IntersectionRatio > 1
        ComingSoon1_Img.Class         += !" visible--left"
        ComingSoon1_Subtitle.Class    += !" visible--left"
        ComingSoon1_Title.Class       += !" visible--left"
        ComingSoon1_Description.Class += !" visible--left"
        ComingSoon1_MainImg.Class     += !" visible--left"
        
        &ComingSoon1_Visible = True
    EndIf
EndEvent

Event IntersectionObserver2.IntersectionUpdate
    If NOT &ComingSoon2_Visible AND IntersectionObserver2.IntersectionRatio > 1
        ComingSoon2_Img.Class         += !" visible--right"
        ComingSoon2_Subtitle.Class    += !" visible--right"
        ComingSoon2_Title.Class       += !" visible--right"
        ComingSoon2_Description.Class += !" visible--right"
        ComingSoon2_MainImg.Class     += !" visible--right"
        
        &ComingSoon2_Visible = True
    EndIf
EndEvent

Event IntersectionObserver3.IntersectionUpdate
    If NOT &ComingSoon3_Visible AND IntersectionObserver3.IntersectionRatio > 1
        ComingSoon3_Img.Class         += !" visible--left"
        ComingSoon3_Subtitle.Class    += !" visible--left"
        ComingSoon3_Title.Class       += !" visible--left"
        ComingSoon3_Description.Class += !" visible--left"
        ComingSoon3_MainImg.Class     += !" visible--left"
        
        &ComingSoon3_Visible = True
    EndIf
EndEvent
```

Runtime result:

`[imagen omitida: wiki id 55166]`

[xpz File](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?55148,,) (see the "Tests" Panel containing several Intersection Observer controls)

### [Restrictions](#Restrictions)

* Only the browser window is supported as Root element.
* Root Margin properties do not accept negative values.

### [Availability](#Availability)

Since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238).


|  |
| --- |
| **Backlinks** |
| [GeneXusUI module (GeneXus 18 Upgrade 13 or prior)](https://wiki.genexus.com/commwiki/wiki?60716) | [GeneXusUIControls module (GeneXus 18 latest upgrade or prior)](https://wiki.genexus.com/commwiki/wiki?60717) |

---
