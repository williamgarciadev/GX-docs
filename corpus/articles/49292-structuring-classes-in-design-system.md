---
title: "Structuring classes in Design System"
source_id: 49292
source_url: https://wiki.genexus.com/commwiki/wiki?49292
genexus_version: "18"
---

# Structuring classes in Design System

Can the properties of a class be defined according to the screen size? What happens if the same class is declared more than once? What properties prevail when [rendering a control](https://wiki.genexus.com/commwiki/wiki?49302)?

### [Conditioning](#Conditioning)

A class can be conditioned so that its declaration is only valid when the condition is met. For the moment, the condition only refers to the output media (for example, screen size and orientation) and is set through the [@media rule](https://wiki.genexus.com/commwiki/wiki?49344), which is equivalent to that of CSS. For the moment, it is only taken into account if the [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375) is used for the Web.

Example: In the example, the H1 class will take the pink color declaration when a control is being rendered with that class on a screen up to 767px wide.

```
@media screen and (max-width:767px)
{
    .H1
    {
        color: pink;
    }
}
```

[View Syntax conventions](https://wiki.genexus.com/commwiki/wiki?49363).

See more about this condition in [Design System Style Rules](https://wiki.genexus.com/commwiki/wiki?47472).

### [Duplication of classes](#Duplication+of+classes)

In a DSO you can declare a class that already exists among the Styles of an imported DSO (or in the "extended" one). The properties coming from the imported DSO will be taken and the properties of your DSO will be added. If there are matching properties, those of your DSO are applied.

Example: a Text Block with class H1 in a [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) that has TravelAgencyExtended Style will be shown with pink color and font size 95px.

```
styles TravelAgency
{
    .H1
    {
        color: green;
        font-size: 95px;
    }
}

styles TravelAgencyExtended
{
    @import TravelAgency;
    
    .H2
    {
        color: blue;
    }

    .H1
    {
          color: pink;
    }
}
```

Likewise, if a class is duplicated but in one case it is declared without conditions and in the other it is declared with conditions (through the @media rule), the same will be done as in the previous case. The properties are added when the rule condition is met.

Example: If the screen size of the Web Panel is smaller than 768px, the Text Block of class H1 will be displayed with pink color and size 95px. If the screen size is larger or equal, then it will look green and with size 95px.

```
styles TravelAgency
{  
    .H1
    {
        color: green;
        font-size: 95px;
    }
    .H2
    {
        color: blue;
    }

    @media screen and (max-width:767px)
    {
        .H1
        {
            color: pink;
        }
    }
}
```

This also applies if in one case it comes from an imported DSO.

Example: The Text Block has 95px size and pink color when the screen size is smaller than 768px. Otherwise, it is shown in green.

```
styles TravelAgency
{
    .H1
    {
        color: green;
        font-size: 95px;
    }
}

styles TravelAgencyExtended
{
    @import TravelAgency;

    .H2
    {
        color: blue;
    }

    @media screen and (max-width:767px)
    {
        .H1
        {
            color: pink;
        }
    }
}
```

If the same class is declared more than once in the same DSO (not recommended), or for the same condition (@media), for the moment the first one will be taken. This behavior may change in future upgrades to match CSS behavior, which takes the last one.

Example: Here the TextBlock with H1 class will be rendered with green color and default size (not 95px).

```
styles TravelAgency
{  
    .H1
    {
        color: green;
    }
    .H2
    {
        color: blue;
    }
    .H1
    {
        color: pink;
        font-size: 95px;
    }
}
```

### [Availability](#Availability)

Since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?48684,,).

### [See also](#See+also)

All considerations related to [How a control is rendered at runtime](https://wiki.genexus.com/commwiki/wiki?49302).


|  |
| --- |
| **Backlinks** |
| [Design System Class](https://wiki.genexus.com/commwiki/wiki?49309) | [Toc:Design Systems](https://wiki.genexus.com/commwiki/wiki?40108) | [Media style rule](https://wiki.genexus.com/commwiki/wiki?49344) |
| [Rendering precedences for controls with Design System Object](https://wiki.genexus.com/commwiki/wiki?49302) |

---
