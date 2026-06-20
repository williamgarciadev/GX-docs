---
title: "HowTo: Display a menu in a responsive application"
source_id: 25778
source_url: https://wiki.genexus.com/commwiki/wiki?25778
genexus_version: "18"
---

# HowTo: Display a menu in a responsive application

This document is focused to guide you on how to display a menu in a responsive application.

In a [RWD](https://wiki.genexus.com/commwiki/wiki?25157,,), wide screens have plenty of space to display a menu, and that's why it is shown on the left or right side of the web page. However, in small screens (like phone screens) the contents of the web page and the menu may not be appropriate to be displayed together.

So, in the case of extra small screens (<768px), by using a button or an image the user can make the menu appear smoothly on one side of the screen, overlapping with what is shown in the page. After selecting a menu option, the menu disappears, and the page shows the information according to the user's selection.

The button to make the menu appear is the same button used to make it disappear from the screen.

In the [GeneXus Web Laboratory example](https://wiki.genexus.com/commwiki/wiki?25937,,), the menu is shown on the left side of the screen; in the case of wide screens:

`[imagen omitida: wiki id 25779]`

When the web page is displayed in cell phone screens, there is a button in the top right corner of the screen for the user to call the menu.

`[imagen omitida: wiki id 25780]`

When the user clicks on the button, the menu appears on the left, overlapping with the contents of the page:

`[imagen omitida: wiki id 25781]`

The [Work With for Web pattern](https://wiki.genexus.com/commwiki/wiki?25475) generates this solution for the case of work with objects that have many filter options.  
The same happens with default prompts that have filters and ordering conditions.

`[imagen omitida: wiki id 25782]`

##### [Light CRM WW Meetings in Wide Screens.](#Light+CRM+WW+Meetings+in+Wide+Screens.)

`[imagen omitida: wiki id 25783]`

##### [Light CRM WW Meetings in phone screens.](#Light+CRM+WW+Meetings+in+phone+screens.)

### [Implementation of the solution](#Implementation+of+the+solution)

The following example is an automatically generated prompt for the Meeting Transaction of the [LightCRM](https://wiki.genexus.com/commwiki/wiki?22592,,) [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836).

The [Abstract Layout](https://wiki.genexus.com/commwiki/wiki?25209) of the prompt is shown in the picture below.

`[imagen omitida: wiki id 53618]`

Note that:

1. The [Responsive Table](https://wiki.genexus.com/commwiki/wiki?24961) is called "FiltersContainer" on the right side contains the different filters for the selection list.  
The FiltersContainer table is going to be shown by default only for small screen devices and bigger (>=768px), not for extra small screen devices (like phones).

In the case of phones, the user will have the "Toggle" button to press and make the FltersContainer table appear.

`[imagen omitida: wiki id 53619]`

##### [Abstract Layout prompt: properties of the Toggle button](#Abstract+Layout+prompt%3A+properties+of+the+Toggle+button)

So, the toggle button is visible only for extra small screens.  
The following pictures show how the [Responsive Sizes property](https://wiki.genexus.com/commwiki/wiki?25478,,) is configured to achieve the desired behavior.

`[imagen omitida: wiki id 53620]`

##### [Abstract Layout prompt: Responsive table for phone screens](#Abstract+Layout+prompt%3A+Responsive+table+for+phone+screens)

`[imagen omitida: wiki id 53622]`

##### [Abstract Layout prompt: Responsive table for small and bigger screens](#Abstract+Layout+prompt%3A+Responsive+table+for+small+and+bigger+screens)

2. The following code is associated with "Toggle" on click event:

```
Event 'Toggle'
    if FiltersContainer.Class = StyleClass:filters-container
        FiltersContainer.Class = StyleClass:filters-container + !" " + StyleClass:filters-container--visible
        GridCell.Class = StyleClass:ww__grid-cell + " col-xs-12 col-sm-9 col-md-10"
        BtnToggle.Class = StyleClass:ww__button-filters--hide
        BtnToggle.Caption = "Hide Filters"
        BtnToggle.TooltipText = "Hide Filters"
    else
        FiltersContainer.Class = StyleClass:filters-container
        GridCell.Class = StyleClass:ww__grid-cell--expanded + " col-xs-12 col-sm-3 col-md-2"
        BtnToggle.Class = StyleClass:ww__button-filters--show
        BtnToggle.Caption = "Show Filters"
        BtnToggle.TooltipText = "Show Filters"
    endif
EndEvent
```

When the Toggle button class is FiltersContainer, the FiltersContainerVisible [Class](https://wiki.genexus.com/commwiki/wiki?49309) is added to the list of classes of the FiltersContainer table.

On the contrary, when the class is FiltersContainerVisible, the FiltersContainer class is associated with it.

The effect is that the table appears and disappears when the button is clicked.

The FiltersContainerVisible and FiltersContainer classes are predefined classes, descendants of the Table class.

Basically, the FiltersContainerVisible and FiltersContainer class properties are as follows:

```
.FiltersContainerVisible {
      display: inherit;
}
```

```
.filters-container, .filters-container--visible {
         visibility: hidden;
         opacity: 0;
         padding-left: 20px;
         padding-right: 20px;
         position: absolute;
         right: -15px;
         background-color: $colors.surface;
         width: 100%;
}

.FiltersContainer {
    display: none;
    background: $colors.surface;
    padding: $spacing.inset-m;
    border: solid $borders.extra-small;
    box-shadow: $shadows.m;
}
```

Additionally, the FiltersContainer responsive table has the Cell Class property set to ".PromptAdvancedBarCell", which is a class with the following settings:

```
.PromptAdvancedBarCell {
      border-right-width: 1px;
      border-right-style: solid;
      border-right-color: $colors.gray01;
}
```

Note:

* For a customized example, it may be necessary to adjust the settings of the left property, and the z-Index [CSS](http://en.wikipedia.org/wiki/Cascading_Style_Sheets) property of the FiltersContainerVisible class.
* The CSS transition is defined as a [Custom property](https://wiki.genexus.com/commwiki/wiki?25303).

### [Download sample](#Download+sample)

The [LightCRM](https://wiki.genexus.com/commwiki/wiki?22592,,) is a sample KB where you can find the WW pattern applied to all the web transactions, and the prompts that have filters and ordering conditions are examples where the menu displays differently depending on the screen size.

### [See Also](#See+Also)

[Look and feel of responsive web applications](https://wiki.genexus.com/commwiki/wiki?25649,,)  
[Action Group Control for the Web](https://wiki.genexus.com/commwiki/wiki?25631)  
[Responsive Web Applications](https://wiki.genexus.com/commwiki/wiki?25159)


|  |
| --- |
| **Backlinks** |
| [Arranging the layout in a RWA](https://wiki.genexus.com/commwiki/wiki?25514) |

---
