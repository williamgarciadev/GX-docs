---
title: "Include style rule"
source_id: 49353
source_url: https://wiki.genexus.com/commwiki/wiki?49353
genexus_version: "18"
---

# Include style rule

Includes another defined class from a Class selector or CSS selector.

### [Syntax](#Syntax)

```
@include <class_name1>[ <class_nameN> ...];
```

 View [Design System Syntax conventions](https://wiki.genexus.com/commwiki/wiki?49363).

**Where:**

*class\_name1, ..., class\_nameN*Name of a class declared in the same Style. If there is no class with that name, it is ignored.

### [Restrictions](#Restrictions)

●    This rule can’t be used within an @Media rule.  
●    This rule doesn’t support using classes defined in another DSO or CSS and imported with the @import rule.

When an Include rule is declared in a class, the property declarations of the classes to include are taken in the same order as if they had been written within that class. Therefore, they are added to those of the class. If there is overlap, those of the parent class are not included. The only ones included are those of the child class (the class being declared).

### [Samples](#Samples)

For the H1 class, the entire H1\_Negative declaration block is valid except for the color declaration; in this case, the declaration explicitly specified in H1 is valid.

```
.H1_Negative
{
     font-family: $fonts.Title1;
     font-size: $fontSizes.H1;
     font-weight: bold;
     letter-spacing: -1.72px;
     color: #FFFFFF;
}
.H1
{
     @include H1_Negative;
     color: $colors.Black;
}
```

If it is to be used for a Web application, the generated CSS will look as follows (note that the tokens are replaced by their values):

```
.H1_Negative
{
    font-family: AbhayaLibre-Bold;
    font-size: 95px;
    font-weight: bold;
    letter-spacing: -1.72px;
    color: #FFFFFF;
} 
.H1
{
    font-family: AbhayaLibre-Bold;
    font-size: 95px;
    font-weight: bold;
    letter-spacing: -1.72px;
    color: #181918;
}
```

Note that a class could be defined by including several classes:

```
.MenuMainItem
    {
        @include Margin-Sides MenuItem;
        color: #FFFFFF;
    }
```

It could even have only one Include rule, without a specific block of properties:

```
.MenuMainItem
    {
        @include Margin-Sides MenuItem;
    }
```

### [F12 - Go to Class](#F12+-+Go+to+Class)

When there is a class referenced in an Include rule, you can easily go to its class definition. To do this, you have two options:

1. You can select the class and press the keyboard shortcut F12.
2. You can right-click on the class and then select the "Go to class" option in the context menu.

In both cases, you will go to the class definition regardless of whether it is within the same Style in a DSO or in a different DSO.   
  
If the class is not in the same DSO, the inheritance is checked over. Then, the parent DSO (or any in the imports tree, it can be the parent of the parent) is opened and the definition of the corresponding class is highlighted.

### [See Also](#See+Also)

See the general topic [Design System Style Rules](https://wiki.genexus.com/commwiki/wiki?47472).


|  |
| --- |
| **Backlinks** |
| [Customize Unanimo](https://wiki.genexus.com/commwiki/wiki?52178) | [Design System Class](https://wiki.genexus.com/commwiki/wiki?49309) | [Design System Class Properties](https://wiki.genexus.com/commwiki/wiki?49323) |
| [Design System Style Rules](https://wiki.genexus.com/commwiki/wiki?47472) | [Toc:Design Systems](https://wiki.genexus.com/commwiki/wiki?40108) | [GeneXus 18 Upgrade 2](https://wiki.genexus.com/commwiki/wiki?53396) | [HowTo: Configure Design System Class Properties](https://wiki.genexus.com/commwiki/wiki?49494) |
| [Include style rule (GeneXus 18 Upgrade 1)](https://wiki.genexus.com/commwiki/wiki?53833) |

---
