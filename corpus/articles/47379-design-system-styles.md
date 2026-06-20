---
title: "Design System Styles"
source_id: 47379
source_url: https://wiki.genexus.com/commwiki/wiki?47379
genexus_version: "18"
---

# Design System Styles

Styles are a way of representing the design decisions made for a system. Together with [Tokens](https://wiki.genexus.com/commwiki/wiki?47378), they make up an essential part of [Design Systems](https://wiki.genexus.com/commwiki/wiki?40108).

As you may know, each control in a layout can be associated with one [Design System Class](https://wiki.genexus.com/commwiki/wiki?49309) (or several). The class is precisely what determines the style that this control will have at runtime (color, background color, font, size, etc.).

Within the [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375) (DSO), styles are defined in the corresponding 'Styles' section. Basically, this section will declaratively define the style for each class in the system.

In the following example, style settings were applied to four classes used by some Text Blocks (in addition to the Form class, to specify the background color of the screens):

`[imagen omitida: wiki id 49296]`

### [Language](#Language)

A style sheet within the Design System object has a structure and format very similar to [CSS](https://www.w3schools.com/css/), even when it is to be used for native applications. In fact, writing any CSS [pseudo-element or pseudo-class](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors/Pseudo-classes_and_pseudo-elements) is supported.

Simply put:

```
 styles <StyleSetName>
'{'
    ListOfRulesAndClassDeclarations
'}'
```

 View [Design System Syntax conventions](https://wiki.genexus.com/commwiki/wiki?49363)

**Where:**

*StyleSetName*  
         Name given by the developer to the set of declarations it contains. Currently, only one set of style declarations can be defined in a DSO, but more may be available in the future.

*ListOfRulesAndClassDeclarations*  
         List with the style declaration of each class. It may also include rules to do other things, such as import another DSO, incorporate a non-standard font family, vary the definition of a class by screen size, and/or include the definitions of one class in another.

         The syntax of this list is as follows:

#### [**Syntax**](#Syntax)

```
styles <StyleSetName>
   '{'
    [import_declaration]
    [font_declaration]
    [media_condition
   '{'
       [class_declaration1 …]  
   '}']
    [class_declaration2 …]
   '}'
```

View [Syntax conventions](https://wiki.genexus.com/commwiki/wiki?6626)

**Where:**

*[import\_declaration](https://wiki.genexus.com/commwiki/wiki?49346)* It is a declaration that imports and uses definitions made in Design System Object, Design System Tokens, Design System Styles and External CSS.

*[font\_declaration](https://wiki.genexus.com/commwiki/wiki?49338)* It is a declaration that defines a font family other than the default ones for Tokens and Styles of the Design System Object.

*[media\_condition](https://wiki.genexus.com/commwiki/wiki?49344)*  
          It is a condition that creates media in your Design System Object.

*[class\_declaration](https://wiki.genexus.com/commwiki/wiki?49309)***1*, ...**[class\_declaration](https://wiki.genexus.com/commwiki/wiki?49309)**N*Set of design characteristics that you want one or more controls to adopt.

**Note**: Only the [Import rule](https://wiki.genexus.com/commwiki/wiki?49346) must go at the beginning. The order of the other declarations and conditions is not relevant.

#### [**Declaration of classes**](#Declaration+of+classes)

The most simple way to define the style characteristics of each class is to select the class with a period, followed by the class name without spaces, and then, between curly brackets, specify all the desired characteristics through properties.

```
.<class_name>
'{'
     {
      <property_name1> : <value1>;
      <property_name2> : <value2>;
      ...
     }
'}'
```

Some properties are valid for rendering both [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) and [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) controls, but others are specific to each one.   
In addition, unlike CSS, in the DSO styles language, the values assigned to properties can be replaced with references to tokens defined in the Tokens section (or imported from other DSOs).   
In the following example, references to color, font size, and font family tokens are used for the first 3 properties, while for the last 2 the values are used directly:

```
    .H2
    {
        color: $colors.OnSurface;
        font-size: $fontSizes.H2;
        font-family: $fonts.Title1;
        font-weight: bold;
        letter-spacing: -2px;
    }
```

Here you can see an overview of [Design System Classes writing styles](https://wiki.genexus.com/commwiki/wiki?49363) according to tokenization.

The units of measurement px and dip are converted (1 to 1 equivalence) to allow using the same Design System Object or an extension of it in both types of applications (those using Web Panels and those using Panels).

Read more at [Design System Class](https://wiki.genexus.com/commwiki/wiki?49309).

#### [**Declaration of rules**](#Declaration+of+rules)

There’s a set of rules (beginning with the at sign) that you can use for structuring styles. Among other things, they let you compose classes, import tokens or styles (or both) from other Design System objects, vary the style of a class according to screen size, etc.

Read more at [Design System Style Rules](https://wiki.genexus.com/commwiki/wiki?47472).

#### [**Usage**](#Usage)

All the classes declared in this part can be added as classes in the object controls (just as [Classes](https://wiki.genexus.com/commwiki/wiki?6246) of a [Theme](https://wiki.genexus.com/commwiki/wiki?4375)) and also be used in other Design System objects where this section (Styles) or the entire object are imported.

It is also possible to modify the class or classes associated with a control dynamically, through the control's [Class property](https://wiki.genexus.com/commwiki/wiki?8741):

*control\_name***.class = styleClass**:*class\_name*

To see more specifically how classes are applied to a control to be rendered at runtime in the output, read [Rendering precedences for controls with Design System Object](https://wiki.genexus.com/commwiki/wiki?49302).

### [Availability](#Availability)

Since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?48684,,).


|  |
| --- |
| **Backlinks** |
| [Attribute-checkbox class for Design System objects](https://wiki.genexus.com/commwiki/wiki?52932) | [Attribute-date class for Design System objects](https://wiki.genexus.com/commwiki/wiki?52976) | [Attribute-radiobutton class for Design System objects](https://wiki.genexus.com/commwiki/wiki?52968) |
| [Customize Unanimo](https://wiki.genexus.com/commwiki/wiki?52178) | [Design System Class](https://wiki.genexus.com/commwiki/wiki?49309) | [Design System Classes writing styles](https://wiki.genexus.com/commwiki/wiki?49363) | [Category:Design System Object](https://wiki.genexus.com/commwiki/wiki?47375) |
| [Design System Style Rules](https://wiki.genexus.com/commwiki/wiki?47472) | [Design System Tokens](https://wiki.genexus.com/commwiki/wiki?47378) | [Toc:Design Systems](https://wiki.genexus.com/commwiki/wiki?40108) | [DesignOps - Guide for designers](https://wiki.genexus.com/commwiki/wiki?46871) |
| [DesignOps - Guide for developers](https://wiki.genexus.com/commwiki/wiki?46877) | [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239) | [gx-grid-column-class property](https://wiki.genexus.com/commwiki/wiki?54459) |
| [gx-grid-column-header-class property](https://wiki.genexus.com/commwiki/wiki?35383) | [gx-grid-even-row-class property](https://wiki.genexus.com/commwiki/wiki?54460) | [gx-grid-hover-row-class property](https://wiki.genexus.com/commwiki/wiki?54463) | [gx-grid-odd-row-class property](https://wiki.genexus.com/commwiki/wiki?54461) |
| [gx-grid-row-class property](https://wiki.genexus.com/commwiki/wiki?32772) | [gx-grid-row-class property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54492) | [gx-grid-selected-row-class property](https://wiki.genexus.com/commwiki/wiki?54462) | [gx-overflow-style property](https://wiki.genexus.com/commwiki/wiki?51796) |
| [Migration of KB with Carmine Theme to Unanimo Design System](https://wiki.genexus.com/commwiki/wiki?51821) | [KB:Unanimo KB](https://wiki.genexus.com/commwiki/wiki?52172) | [Uses of Cascade Layers in CSS](https://wiki.genexus.com/commwiki/wiki?53234) |

---
