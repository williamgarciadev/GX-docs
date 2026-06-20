---
title: "Color rule"
source_id: 8348
source_url: https://wiki.genexus.com/commwiki/wiki?8348
genexus_version: "18"
---

# Color rule

**Deprecated**. Use [Design System Styles](https://wiki.genexus.com/commwiki/wiki?47379) instead.

### [Syntax](#Syntax)

**Color(***GXColor* [, *att* | *&var*]**)** [**If** *condition*];

**Where:**

*GxColor*  
      Is a set that defines the display and the accepted colors. See possible values below.

*att* or *&var*  
      Is the attribute or variable to be colored if the condition is true.

*condition*  
      Is the condition that is evaluated to determine whether the color is applied (if true) or not (if false) to the att or &var. If the condition is omitted, the color rule will always be triggered.

### [Scope](#Scope)

**Objects:**[Transaction](https://wiki.genexus.com/commwiki/wiki?1908)

### [Description](#Description)

There are times when one prefers to use colors in forms. Whether it be used for simple screen cosmetics or for improved screen usability, this option greatly enhances the actual application. A number of elements that are represented on the screen can be colored. The following is a list of all the elements that can be colored:

* **Background/Foreground.** These elements can have an associated default color screen. For example, the screen's background default color could be 'GRN' (green) or the default color literal could be 'RED'.

* Colors can also be used by attributes or variables that are either displayed or accepted. For example, the customer name can be displayed in 'BLU' (blue). Certain conditions can be applied to best represent a situation. For example, a Customer's balance may appear in 'BLU' if it is positive, or in 'RED' in any other case.

* **Certain screen literals.** For example, one may want to display a title in 'BLU' (blue). To do this, it is necessary to define a variable and assign it with a literal and later assign the desired color to the variable:

```
&Title = 'Credit Invoice'
```

And the corresponding color rule:

```
Color('BLU', &Title);
```

There are two concepts that should be noted with respect to colors: the color itself ('RED', 'BLU'), and the way in which the color is displayed (blinking, highlighted). Generally this is referred to as a 'screen attribute', but we avoid using this terminology since it could easily be confused with GeneXus attributes.

The following rule allows you to define default colors:

Color(*GxColor*);

To color attributes or variables the following rule is used:

color(*GxColor* [, *att* | *&var*] ) [ IF <cond> ];

Where *GxColor* is a set that defines the display and the accepted colors.

The display and accepted colors together form a color set that specifies the color and the display attribute:

<GxColor> := '''<DisplayColor>[ ',' <AcceptColor>]'''  
<DisplayColor> := <ColorPair>  
<AcceptColor> := <ColorPair>  
<ColorPair> := <ColorSet> [ '/' <ColorSet> ]  
<ColorSet> := <Color> [ <DspAttri> ]  
<Color> := 'WHT'| 'BLK'| 'RED'| 'GRN'| 'BRW'|'MGN'| 'BLU'| 'CYN'| 'YLW'| 'RI'| 'X'  
<DspAttri> := '+'|'\*'

Each <ColorPair> defines the foreground color and the background color.

An asterisk (\*) placed immediately after a color code can be used to make the background color bright.  
A plus sign (+) placed immediately after a color code can be used to give high intensity to the foreground color.

**Foreground/Background colors**

Each color is defined as a pair: the color of the letters (the foreground color) and the background color separated by a /, for example, 'RED/BLK', indicate red letters over a black background.

**Display/Accepted color**

Attributes can not only be assigned a display color, but also an entry color. To do this, use the <DisplayColor> and <AcceptColor> options respectively.

#### [**iSeries**](#iSeries)

The iSeries only considers the first <ColorSet> belonging to <DisplayColor>. That is, the foreground color is the only color that is taken into account and it will not be modified when the data is displayed or accepted. For example, the only color that is taken into account for the color expression 'GRN+/YLW,WHT/BLU' is 'GRN+'.

**Notes:**

* The option ‘RI’ is only available for Cobol and RPG generators.
* For each rule or set of rules, you may indicate that they be triggered \_only\_ for certain environment(s). See more details in the document "Form-specific Events and Rules".

### [Samples](#Samples)

* **Default Screen Colors.** To make the default color for all the letters on a screen red, use the following rule:

```
color('RED');
```

* **Coloring Attributes or Variables.** The attribute name is always displayed in white over a blue background:

```
color( 'WHT/BLU', Name);
```

* **Conditional Color Definition.**

```
color( 'RED+', Balance) if Balance < 0;
color( 'WHT', Balance) if Balance >= 0;
```

**Note**: When several Color rules are used for the same attribute/variable (a conditional color definition), the first color rule that is satisfied determines the color that will be used. If no rule is satisfied, the default color is used.

* **Colors Used for Password Entry**

```
color('X,X', Password);
```

X means no-display. The first X means no-display at display time, and the second means no-display at accept time. This allows passwords to be entered without being displayed.

* **Colors and arrays.** The color rule is applied to the whole array and not just to a particular element. Therefore, it is not possible to color a particular array element with this rule.

### [See Also](#See+Also)

[ForeColor property](https://wiki.genexus.com/commwiki/wiki?8693)  
[BackColor property](https://wiki.genexus.com/commwiki/wiki?8688)


|  |
| --- |
| **Backlinks** |
| [Color function](https://wiki.genexus.com/commwiki/wiki?8345) | [Rules in Transactions](https://wiki.genexus.com/commwiki/wiki?8213) | [Transaction rules when executed as Business Component](https://wiki.genexus.com/commwiki/wiki?2280) |

---
