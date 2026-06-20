---
title: "DSO properties that begin with gx- and end with class"
source_id: 55707
source_url: https://wiki.genexus.com/commwiki/wiki?55707
genexus_version: "18"
---

# DSO properties that begin with gx- and end with class

Properties with names such as "gx-xxxx-class" must be assigned a certain class that gives them a style.

Some examples for Web applications are as follows:

* [gx-multimedia-upload-clear-class property](https://wiki.genexus.com/commwiki/wiki?50633)
* [gx-multimedia-upload-empty-class property](https://wiki.genexus.com/commwiki/wiki?50635)
* [gx-multimedia-upload-change-class property](https://wiki.genexus.com/commwiki/wiki?50634)

This is an example for Web, Angular, and Native Mobile applications:

* [gx-focused-class property](https://wiki.genexus.com/commwiki/wiki?51849)

Below is an example for a Native Mobile application.

Consider a [Menu object](https://wiki.genexus.com/commwiki/wiki?16321) whose [Control property](https://wiki.genexus.com/commwiki/wiki?55318) = Tabs and its Class property = Tab.

A [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375) called "MyStyle" is defined, containing in its Styles section the following definitions:

```
Styles MyStyle{
    .Tab
      {
        gx-tab-strip-background-color: $colors.Primary;
        gx-tab-strip-indicator-color: $colors.ActionTint;
        gx-selected-tab-page-class: TabPageSelected;
        gx-unselected-tab-page-class: TabPageUnselected;
      }
    .TabPage
      {
        text-transform: uppercase;
      }
    .TabPageSelected
      {
        @include TabPage;
        color: $colors.Background;
      }
    .TabPageUnselected
      {
        @include TabPage;
        color: $colors.Background55;
        font-weight: normal;
      }
}
```

Note the **gx-selected-tab-page-class** and the **gx-unselected-tab-page-class** properties to which the TabPageSelected and the TabPageUnselected classes have been assigned, respectively.

The [Design System Tokens](https://wiki.genexus.com/commwiki/wiki?47378) section is defined as shown below:

```
tokens Name {
    #colors
      {
        Primary: #656A76;
        ActionTint: #602C80;
        Background: #AACCAD;
        Background55: #D0B9CD;
      }
}
```

Finally, in the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210), under the Customization node > Platforms > Any Platform, the [Style property](https://wiki.genexus.com/commwiki/wiki?43966) was set to "MyStyle".

At runtime, you will see the following:

`[imagen omitida: wiki id 55740]`


|  |
| --- |
| **Backlinks** |
| [Toc:Design Systems](https://wiki.genexus.com/commwiki/wiki?40108) | [gx-button-disabled-class property](https://wiki.genexus.com/commwiki/wiki?30896) | [gx-datepicker-image-class property](https://wiki.genexus.com/commwiki/wiki?50630) |
| [gx-focused-class property](https://wiki.genexus.com/commwiki/wiki?51849) | [gx-grid-column-class property](https://wiki.genexus.com/commwiki/wiki?54459) | [gx-grid-column-header-class property](https://wiki.genexus.com/commwiki/wiki?35383) | [gx-grid-even-row-class property](https://wiki.genexus.com/commwiki/wiki?54460) |
| [gx-grid-header-row-class property](https://wiki.genexus.com/commwiki/wiki?35382) | [gx-grid-hover-row-class property](https://wiki.genexus.com/commwiki/wiki?54463) | [gx-grid-odd-row-class property](https://wiki.genexus.com/commwiki/wiki?54461) | [gx-grid-row-class property](https://wiki.genexus.com/commwiki/wiki?32772) |
| [gx-grid-selected-row-class property](https://wiki.genexus.com/commwiki/wiki?54462) | [gx-multimedia-upload-change-class property](https://wiki.genexus.com/commwiki/wiki?50634) | [gx-multimedia-upload-class property](https://wiki.genexus.com/commwiki/wiki?50632) | [gx-multimedia-upload-clear-class property](https://wiki.genexus.com/commwiki/wiki?50633) |
| [gx-multimedia-upload-empty-class property](https://wiki.genexus.com/commwiki/wiki?50635) | [gx-popup-resize-handle-class property](https://wiki.genexus.com/commwiki/wiki?51284) | [gx-prompt-image-class property](https://wiki.genexus.com/commwiki/wiki?50631) | [gx-readonly-class property](https://wiki.genexus.com/commwiki/wiki?48092) |
| [gx-table-row-cell-class property](https://wiki.genexus.com/commwiki/wiki?25796) | [HowTo: Set the style of a read-only Attribute/Variable control using DSO](https://wiki.genexus.com/commwiki/wiki?49906) |

---
