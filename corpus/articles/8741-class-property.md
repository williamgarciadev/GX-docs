---
title: "Class property"
source_id: 8741
source_url: https://wiki.genexus.com/commwiki/wiki?8741
genexus_version: "18"
---

# Class property

Assigns a Design System Class (or a Theme Class) to a control.

### [Syntax](#Syntax)

**control.** class = { styleClass:StyleClassName | Value }...   

**Where:**

*control*Name of the control to which you want to assign one or more classes.

*StyleClassName*Name of the class that you want to associate with the control, among those of the Style (Design System Object or Theme) associated with the object that contains the control.

*Value*  
    Represents a string that can be assigned to this property at runtime. It can be either a constant string or a variable.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies both at runtime and at design time.

### [Samples](#Samples)

In the following example, a Theme Class is assigned to the **class property** of a “Grid1” grid control.

”GreenGrid” and ”BlueGrid” are two classes derived from the “Grid” predefined class. These classes are defined in the Theme associated with the object that contains the control.

```
//A ThemeClass is asssigned
If &import > 0
   Grid1.class = StyleClass:GreenGrid
Else
   Grid1.class = StyleClass:BlueGrid
Endif

//A Value is assigned
If &import > 0
   Grid1.class = !”GreenGrid”
Else
   Grid1.class = !”BlueGrid”
EndIf
```

To associate two or more classes with a control's class property, just use the '+' operator to concatenate the strings, as the following code shows:

```
If &import > 0
   Grid1.class = StyleClass:GreenGrid + !" " + StyleClass:GreenLightGrid
Else
   Grid1.class = StyleClass:BlueGrid + !" " + StyleClass:BlueLightGrid
Endif
```

**Important:** It is highly recommended that you use the *StyleClass:ClassName* syntax because it creates a reference to the Theme class or Design System class. When a string value is used, there is no way to know which classes are referenced by an object.

### [See Also](#See+Also)

* [Style and Default Style properties](https://wiki.genexus.com/commwiki/wiki?8145)
* [Web Theme object](https://wiki.genexus.com/commwiki/wiki?6420)
* [Theme object](https://wiki.genexus.com/commwiki/wiki?16595)
* [Theme class cross reference](https://wiki.genexus.com/commwiki/wiki?24024,,)
* [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375)


|  |
| --- |
| **Backlinks** |
| [Application Bars Class property](https://wiki.genexus.com/commwiki/wiki?37518) | [Attribute/Variable control properties in Web Forms](https://wiki.genexus.com/commwiki/wiki?8133) | [Button properties](https://wiki.genexus.com/commwiki/wiki?9916) |
| [Column Class property in Grid and Tabular Grid](https://wiki.genexus.com/commwiki/wiki?24908) | [Design System Styles](https://wiki.genexus.com/commwiki/wiki?47379) | [DesignOps - Guide for designers](https://wiki.genexus.com/commwiki/wiki?46871) | [DesignOps - Guide for developers](https://wiki.genexus.com/commwiki/wiki?46877) |
| [Enable Header Row Pattern property](https://wiki.genexus.com/commwiki/wiki?29843) | [File Upload control](https://wiki.genexus.com/commwiki/wiki?30574) | [Flex control](https://wiki.genexus.com/commwiki/wiki?40521) | [Font All Caps property (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?56518) |
| [Form Control](https://wiki.genexus.com/commwiki/wiki?14619) | [Free Style Grid Properties](https://wiki.genexus.com/commwiki/wiki?9760) | [Header Row Application Bars Class property](https://wiki.genexus.com/commwiki/wiki?37186) | [How to configure Popup windows in Web apps](https://wiki.genexus.com/commwiki/wiki?31550) |
| [HowTo: Set the style of a read-only Attribute/Variable control using DSO](https://wiki.genexus.com/commwiki/wiki?49906) | [Live Editing in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?27806) | [Management considerations on Theme classes](https://wiki.genexus.com/commwiki/wiki?25083) | [Options - Themes](https://wiki.genexus.com/commwiki/wiki?43699) |
| [QueryViewer control properties](https://wiki.genexus.com/commwiki/wiki?32920) | [Text Block properties](https://wiki.genexus.com/commwiki/wiki?9908) | [text-transform property](https://wiki.genexus.com/commwiki/wiki?40682) | [Theme Class](https://wiki.genexus.com/commwiki/wiki?6246) |
|

---
