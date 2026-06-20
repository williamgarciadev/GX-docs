---
title: "Media style rule"
source_id: 49344
source_url: https://wiki.genexus.com/commwiki/wiki?49344
genexus_version: "18"
---

# Media style rule

Creates media in your Design System Object to achieve responsive displays.

### [Syntax](#Syntax)

```
@media  [not | only] <media_type> and <media_feature> [and | or| not <media_feature>]...
|
@media $mediaQueries.<token_name>
‘{‘
    class_declaration...
‘}’
```

View [Design System Syntax conventions](https://wiki.genexus.com/commwiki/wiki?49363).

**Where:**

*media\_type*  
Specifies the media/device type:  
*all:*used for all media type devices. It is the default value.  
        *print:*used for printers  
       *screen:*used for computer screens, tablets, smartphones, etc.  
       *speech:*used for screen readers that ‘read’ the page out loud.

*media\_feature*Is the feature used to apply a condition. The most common ones are min-width, max-width, width, orientation, but there are more. See [CSS @media Rule](https://www.w3schools.com/cssref/css3_pr_mediaquery.asp).

*token\_name*Name of a token defined in the [Tokens](https://wiki.genexus.com/commwiki/wiki?47378) section of the same DSO or of an imported one inside the **#mediaqueries** category. There, the token definition follows the syntax:   
*token\_name:***[** **not | only** **]** *media\_type* and *media\_feature* [ **and | or| not** *media\_feature* ]...;

*class\_declaration*[Class declaration](https://wiki.genexus.com/commwiki/wiki?49309). The ellipses indicate that a number of class declarations can be specified.

### Description

A Media rule encapsulates a set of classes that take that value if the conditions specified in the media header are met. It is equivalent to [CSS Media Queries](https://www.w3schools.com/css/css3_mediaqueries.asp).

It is only taken into account if the Design System object is used for Web.

Media queries can be used to check many things, such as:

●    width and height of the viewport  
●    width and height of the device  
●    orientation (is the tablet/phone in landscape or portrait mode?)  
●    resolution

### [Restrictions](#Restrictions)

●    The headers cannot be combined; that is, you have one made up of a single token, or one made up of the rule as in CSS.

### [Samples](#Samples+)

**Example 1**

The H1\_Negative class is defined both without any condition and with two disjoint conditions (one with tokens and the other without them).

```
styles TravelAgencyFrontendExtended
{
   .H1_Negative
   {
        color: white;
        font-family: AbhayaLibre-Bold;
   } 
    @media $mediaQueries.XS
    {
        .H1_Negative {
            font-size: $fontSizes.H1_XS;
        }
        .H2 {
            font-size: $fontSizes.H2_XS;
        }
    }
    @media screen and (min-width: 768px) and (max-width: 991px)
    {
        .H1_Negative {
            font-size: $fontSizes.H1_S;
        }
        .H2 {
            font-size: $fontSizes.H2_S;
        }
    }
}

tokens TravelAgencyFrontendExtended
{
    #fontSizes
    {
       H1: 95px; 
       H1_XS: 50px;
       H1_S: 80px;
       H2: 60px;
       H2_XS: 24px;
       H2_S: 60px;

   }    
    #mediaQueries
    {
        XS: screen and (max-width: 767px);
    }
}
```

 A Text Block control that has the H1\_Negative class associated with it will be rendered in the output as follows. If the screen width is:

●    Larger than 991px, it will take the properties "color: white" and "font-family: AbhayaLibre-Bold."  
●    Between 768 and 991px, it will take, in addition to the properties "color: white" and "font-family: AbhayaLibre-Bold," the property "font-size:$fontSizes.H1\_S" (80px).  
●    Smaller than 768, it will take, in addition to the properties "color: white" and "font-family: AbhayaLibre-Bold," the property "font-size:$fontSizes.H1\_XS" (50px).

See more at [Structuring classes in Design System](https://wiki.genexus.com/commwiki/wiki?49292).

**Example 2**

styles myStyles  
{  
          //Classes…

         @media print and (min-width: 30em) and (orientation: landscape)  
                  {  
                       .class1  
                       {  
                          //Properties...  
                       }  
                       .class3  
                      {  
                         //Properties...  
                      }  
                        //More classes....  
                 }  
        //Classes…  
}

### [Availability](#Availability)

Since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?48684,,).

### [See Also](#See+Also)

See the general topic [Design System Style Rules](https://wiki.genexus.com/commwiki/wiki?47472).


|  |
| --- |
| **Backlinks** |
| [Design System Style Rules](https://wiki.genexus.com/commwiki/wiki?47472) | [Design System Styles](https://wiki.genexus.com/commwiki/wiki?47379) | [Design System Tokens](https://wiki.genexus.com/commwiki/wiki?47378) |
| [Toc:Design Systems](https://wiki.genexus.com/commwiki/wiki?40108) | [gx-grid-column-hidden property](https://wiki.genexus.com/commwiki/wiki?56456) | [gx-grid-column-size property](https://wiki.genexus.com/commwiki/wiki?56550) | [Structuring classes in Design System](https://wiki.genexus.com/commwiki/wiki?49292) |

---
