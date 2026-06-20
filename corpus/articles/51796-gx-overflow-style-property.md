---
title: "gx-overflow-style property"
source_id: 51796
source_url: https://wiki.genexus.com/commwiki/wiki?51796
genexus_version: "18"
---

# gx-overflow-style property

Shows or hides the content that exceeds the size of the container in Angular apps.

### [Values](#Values)

|  |  |
| --- | --- |
| **hide** | Hides the content that exceeds the control size. |
| **show** | Shows the content that exceeds the control size. |

### [Scope](#Scope)

**Generators:** [Angular](https://wiki.genexus.com/commwiki/wiki?42550)  
**Level:** [Design System Style Class](https://wiki.genexus.com/commwiki/wiki?49309)

### [Description](#Description)

With this property, you can configure the behavior of the content that exceeds the size of its container.

The "show" value is useful when you don’t want to clip popovers, dropdowns, absolute content, shadows, etc., to the control size.

The "hide" value is useful when you want to clip animations that are inside the control and at some point overflow the control. Also, this value is useful when you want to apply border-radius to a container that has an image that exceeds the container size.

Controls like Grids, Tables, and Canvas may have associated classes that support this property.

### [Samples](#Samples)

Add the following classes in the Design System object [Styles section](https://wiki.genexus.com/commwiki/wiki?47379).

```
.MainTable {
    gx-overflow-style: show;
}

 .TableOverflowStyleHide {
    margin-right: 16dip;
    border-width: 2dip;
    border-style: solid;
    border-color: #13142c;

    gx-overflow-style: hide;
}

 .TableOverflowStyleShow {
    margin-left: 16dip;
    border-width: 2dip;
    border-style: solid;
    border-color: #13142c;

    gx-overflow-style: show;
}

.AttributeElevation {
    border-width: 2dip;
    border-style: solid;
    border-color: #2a2c5f;
    border-radius: 16dip;
    margin: 1dip;

    gx-elevation: 6;
}
```

Create a Layout like the following, where the Class associated with each control is the one indicated by the labeled arrow:

`[imagen omitida: wiki id 51867]`

Runtime result:

`[imagen omitida: wiki id 51868]`

**Notes:**

* In some cases, when you have multiple nested containers and you want to show or hide the content overflow, it may be necessary to set the gx-overflow-style property on the nested containers.
* This property in Grids only applies to cells.
* This property has no effect when used on a Table with [Auto Grow property](https://wiki.genexus.com/commwiki/wiki?20204) = False and [Overflow Behavior property](https://wiki.genexus.com/commwiki/wiki?46288) = Add Scroll.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Run the main object.
