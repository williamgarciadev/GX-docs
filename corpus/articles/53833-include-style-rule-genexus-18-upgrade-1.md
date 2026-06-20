---
title: "Include style rule (GeneXus 18 Upgrade 1)"
source_id: 53833
source_url: https://wiki.genexus.com/commwiki/wiki?53833
genexus_version: "18"
---

# Include style rule (GeneXus 18 Upgrade 1)

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

### [Availability](#Availability)

Since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?48684,,).

### [See Also](#See+Also)

See the general topic [Design System Style Rules](https://wiki.genexus.com/commwiki/wiki?47472).
