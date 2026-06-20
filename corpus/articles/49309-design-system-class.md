---
title: "Design System Class"
source_id: 49309
source_url: https://wiki.genexus.com/commwiki/wiki?49309
genexus_version: "18"
---

# Design System Class

A class determines a set of design characteristics that you want one or more controls to adopt in the UI at runtime (rendering).

It is declared in the section [Design System Styles](https://wiki.genexus.com/commwiki/wiki?47379).

### [Syntax](#Syntax)

```
.<class_name1>[, {.<class_nameN>, ...}]
‘{’
       [@include <class_namej>... ;]      
       {<property_name>: {value[unit]|$token_group.token_name | gx-function}...}; 
       ...
‘}’
```

View [Design System Syntax conventions](https://wiki.genexus.com/commwiki/wiki?49363)

**Where:**

*class\_name1,..., class\_nameN*  
    Name given to the class by the developer. This name will be used in the class properties of the controls. You can specify more than one class name if you want them to share the same block of property definitions (currently only for Web). Read about the [Temporary restriction on casing of Web class names](https://wiki.genexus.com/commwiki/wiki?49309).

*class\_namej*  
Name of a class declared in the same Style whose properties are to be included in this one. If there is no class with that name, it is ignored.

*property\_name*Valid style property name. Valid properties are both the existing ones for Web platform objects (for example, [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)) as well as Native or Angular (for example, [Panel](https://wiki.genexus.com/commwiki/wiki?24829)). See [Design System Class Properties](https://wiki.genexus.com/commwiki/wiki?49323).

*value*Valid value for the *property\_name*.

*unit*  
    Valid unit of measurement according to *property\_name*. Some of them are **px**, **dip**, **em**, **%**.

***$**token\_group*  
    Valid Token category. In the Token editor, you can see a combo box with all the possible values (colors, radius, spacing, etc.).

*token\_name*Name of the Token defined under the *token\_group*category in the Tokens section of the [DSO](https://wiki.genexus.com/commwiki/wiki?47375) or of a DSO (or Tokens section of a DSO) imported by it (in a sort of "extended DSO" if viewed as an analogy to the concept of an extended table).

*gx-function*Function used to return a reference to a [KB](https://wiki.genexus.com/commwiki/wiki?2428) object as a value. For example, the **gx-image** function returns a reference to a KB image and is used for properties specifying images. The **gx-file** function returns a reference to a KB file.

**Note**: Among other things, CSS also allows you to select HTML tags or identifiers —not only classes— and combine selectors, etc. The Styles section of the DSO allows you to directly import or copy a CSS, and for this reason that syntax should be included here as well. However, it is not explained here because it has a lower level and is not supported for native objects (Panels type). This [tutorial](https://www.w3schools.com/css/css_syntax.asp) can be very helpful to access it.

If there is an [Include rule](https://wiki.genexus.com/commwiki/wiki?49353), the property declarations of each of the included classes are taken as if they were written within the class being declared, in that same order. Therefore, they are added to those of the class. If there is overlap, the last one applies.

### [Sample:](#Sample%3A)

For the H1 class, the entire H1\_Negative declaration block is valid except for the color declaration; in this case, the declaration explicitly specified in H1 is valid.

```
.H1_Negative
{
    color: #FFFFFF;
    font-family: $fonts.Title1;
    font-size: $fontSizes.H1;
    font-weight: bold;
    text-align: center;
    letter-spacing: -1.72px;
    line-height: 75px;
} 
.H1
{
    @include H1_Negative;
    color: $colors.Black;
}
```

Note that values were used for some properties, while other properties have values with units of measurement or references to Tokens. If this DSO were to be applied to a Panel, then the px unit would be converted to dip (1 to 1 equivalence).

### [Characteristics of classes](#Characteristics+of+classes)

Classes are not specific, meaning that they have no restrictions as to the type of control to which they can be applied. When any of the style declarations of the associated class doesn't make sense for a control type, that declaration (and only that one) will not be taken into account.

Thus, if a class defines text features such as font size, they will have an effect on Text Block or Attribute/Variable type controls but not on an Image type control.

There may be classes not associated with any UI control, just as there may be controls that have classes associated with them that are not specified in the DSO (nor in any of the DSOs or Styles of DSOs imported by it). In the latter case, it’s as if they had no associated class.

### [About properties](#About+properties)

Some properties are valid for rendering both Web Panel and Panel controls, but others are specific.

See more in [Design System Class Properties](https://wiki.genexus.com/commwiki/wiki?49323)

### [Class structuring in the Styles section](#Class+structuring+in+the+Styles+section)

A class can be conditioned so that its declaration is only valid when the condition is met. For now, the condition is only related to the medium, such as screen size, and applies only to the Web.

In addition, the same class can be selected in the same DSO with no condition (or with another condition), or in the Styles of an imported DSO. See [Structuring classes in Design System](https://wiki.genexus.com/commwiki/wiki?49292) to know what happens in those cases.

See also [Rendering precedences for controls with Design System Object](https://wiki.genexus.com/commwiki/wiki?49302).

### [Temporary restriction on casing of Web class names](#Temporary+restriction+on+casing+of+Web+class+names)

A DSO used in a Web application will generate a CSS file with the classes having the same casing as that of the DSO.

While the DSO is not case-sensitive, nor is CSS, HTML considers selectors to be case-sensitive. So, for a control that has a MyClass class associated with it to take its values from that class in the CSS at runtime, it has to be called MyClass, and not, for example, myclass.

At the moment ([GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?48684,,)), the first time a class name is typed in a DSO and saved, that will be the casing used from then on in the KB; even if the developer modifies it in the DSO, internally the first one will continue to be taken, so it will be the one used by the controls.

#### [This has some drawbacks:](#This+has+some+drawbacks%3A)

1.    Suppose you have a DSO where you first declared:

```
styles MyStyles
{
    .MyClass
    {
        color: brown;
    }
}
```

When you try to associate this class with a control, you will be offered the MyClass class. When the CSS is generated, it will be generated with the casing of the DSO object, so it will be MyClass. At runtime, the brown color will be displayed correctly.

However, if you change the casing in the DSO (or delete the class and write it again with another casing) and call the class "myclass," when trying to associate that class with a control, even if you type "myclass" in the Class field value, you will see that the IDE will show "MyClass" after losing focus.

The problem is that in the generated CSS the change will be applied —you will see "myclass"— but the HTML tag for the control will read MyClass. So, when you look for that class in the CSS it will not be found and you will not see the brown color at runtime.

2.    The same will happen if you use the same class name in two different DSOs. The internal casing will be the one used the first time it was saved, regardless if it comes from two different DSOs.

Therefore, once you have saved a class with a certain casing, you should always use that exact casing in all DSOs, even if they are independent of each other. No matter what casing you type, the controls will always map to the first one regardless of which DSO they come from.   
The other option is to change something in the name to make it understood that it is another entity.

**Note**: All that has been said is also valid for Angular applications.

### [Availabilty](#Availabilty)

Since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?48684,,).


|  |
| --- |
| **Backlinks** |
| [Application Bars Class property](https://wiki.genexus.com/commwiki/wiki?37518) | [Attribute-checkbox class for Design System objects](https://wiki.genexus.com/commwiki/wiki?52932) | [Attribute-date class for Design System objects](https://wiki.genexus.com/commwiki/wiki?52976) |
| [Attribute-radiobutton class for Design System objects](https://wiki.genexus.com/commwiki/wiki?52968) | [Design Import option](https://wiki.genexus.com/commwiki/wiki?46882) | [Design Import option (GeneXus 18 Upgrade 4)](https://wiki.genexus.com/commwiki/wiki?55439) | [Design System Class](https://wiki.genexus.com/commwiki/wiki?49309) |
| [Design System Object - Automatic import of the designers’ design](https://wiki.genexus.com/commwiki/wiki?48931) | [Design System Object - Classes that can be combined](https://wiki.genexus.com/commwiki/wiki?48690) | [Design System Object - Classes to separate what is particular from what is shared](https://wiki.genexus.com/commwiki/wiki?48686) | [Design System Object - Declaring the classes of the application's Design System](https://wiki.genexus.com/commwiki/wiki?48687) |
| [Design System Object - Fundamental bases](https://wiki.genexus.com/commwiki/wiki?48675) | [Design System Object - How to associate a Design System Object to your screens](https://wiki.genexus.com/commwiki/wiki?48696) | [Design System Object - Tokens, design constants (semantized)](https://wiki.genexus.com/commwiki/wiki?48691) | [Design System Object - Untyped classes](https://wiki.genexus.com/commwiki/wiki?48689) |
| [Design System Style Rules](https://wiki.genexus.com/commwiki/wiki?47472) | [Design System Styles](https://wiki.genexus.com/commwiki/wiki?47379) | [Table of contents:Design Systems](https://wiki.genexus.com/commwiki/wiki?40108) | [Extend Unanimo](https://wiki.genexus.com/commwiki/wiki?52179) |
| [Font size property (QueryViewer) and gx-qv-map-series-labels-font-size property (DSO Style Class)](https://wiki.genexus.com/commwiki/wiki?48293) | [font-style property](https://wiki.genexus.com/commwiki/wiki?56524) | [font-weight property](https://wiki.genexus.com/commwiki/wiki?43671) | [font-weight property (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?57941) |
| [gx-button-disabled-class property](https://wiki.genexus.com/commwiki/wiki?30896) | [gx-content-mode property](https://wiki.genexus.com/commwiki/wiki?23857) | [gx-content-size-change property](https://wiki.genexus.com/commwiki/wiki?33517) | [gx-datepicker-image-class property](https://wiki.genexus.com/commwiki/wiki?50630) |
| [gx-elevation property](https://wiki.genexus.com/commwiki/wiki?28180) | [gx-focused-class property](https://wiki.genexus.com/commwiki/wiki?51849) | [gx-grid-column-class property](https://wiki.genexus.com/commwiki/wiki?54459) | [gx-grid-column-header-class property](https://wiki.genexus.com/commwiki/wiki?35383) |
| [gx-grid-column-hidden property](https://wiki.genexus.com/commwiki/wiki?56456) | [gx-grid-column-size property](https://wiki.genexus.com/commwiki/wiki?56550) | [gx-grid-even-row-class property](https://wiki.genexus.com/commwiki/wiki?54460) | [gx-grid-focused-row-class property](https://wiki.genexus.com/commwiki/wiki?57657) |
| [gx-grid-header-row-class property](https://wiki.genexus.com/commwiki/wiki?35382) | [gx-grid-header-row-class property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54491) | [gx-grid-hover-row-class property](https://wiki.genexus.com/commwiki/wiki?54463) | [gx-grid-odd-row-class property](https://wiki.genexus.com/commwiki/wiki?54461) |
| [gx-grid-row-class property](https://wiki.genexus.com/commwiki/wiki?32772) | [gx-grid-row-class property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54492) | [gx-grid-selected-row-class property](https://wiki.genexus.com/commwiki/wiki?54462) | [gx-hide-date-time-picker property](https://wiki.genexus.com/commwiki/wiki?56050) |
| [gx-loading-animation-behavior property](https://wiki.genexus.com/commwiki/wiki?53933) | [gx-multimedia-upload-change-class property](https://wiki.genexus.com/commwiki/wiki?50634) | [gx-multimedia-upload-class property](https://wiki.genexus.com/commwiki/wiki?50632) | [gx-multimedia-upload-clear-class property](https://wiki.genexus.com/commwiki/wiki?50633) |
| [gx-multimedia-upload-empty-class property](https://wiki.genexus.com/commwiki/wiki?50635) | [gx-overflow-style property](https://wiki.genexus.com/commwiki/wiki?51796) | [gx-popup-resize-handle-class property](https://wiki.genexus.com/commwiki/wiki?51284) | [gx-prompt-image-class property](https://wiki.genexus.com/commwiki/wiki?50631) |
| [gx-qv-map-background-opacity property](https://wiki.genexus.com/commwiki/wiki?48278) | [gx-qv-map-title-font property](https://wiki.genexus.com/commwiki/wiki?48279) | [gx-qv-map-title-font-family property](https://wiki.genexus.com/commwiki/wiki?48280) | [gx-qv-map-title-font-size property](https://wiki.genexus.com/commwiki/wiki?48281) |
| [gx-qv-map-title-font-style property](https://wiki.genexus.com/commwiki/wiki?48282) | [gx-qv-map-title-font-weight property](https://wiki.genexus.com/commwiki/wiki?48283) | [gx-readonly-class property](https://wiki.genexus.com/commwiki/wiki?48092) | [gx-table-row-cell-class property](https://wiki.genexus.com/commwiki/wiki?25796) |
| [HowTo: Display a menu in a responsive application](https://wiki.genexus.com/commwiki/wiki?25778) | [Import style rule](https://wiki.genexus.com/commwiki/wiki?49346) | [Media style rule](https://wiki.genexus.com/commwiki/wiki?49344) | [PivotTable Main color](https://wiki.genexus.com/commwiki/wiki?41081) |
| [text-transform property](https://wiki.genexus.com/commwiki/wiki?40682) | [Category:Web Master Panel object](https://wiki.genexus.com/commwiki/wiki?10348) |

---
