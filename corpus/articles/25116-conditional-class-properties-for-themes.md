---
title: "Conditional Class Properties for Themes"
source_id: 25116
source_url: https://wiki.genexus.com/commwiki/wiki?25116
genexus_version: "18"
---

# Conditional Class Properties for Themes

In a world of multiple devices with different screen sizes, resolutions and operating systems, it is common for designers to use different style sheets, depending on the screen size of devices. As the style sheet used for large displays may vary from the one used for mobile devices, it should be correctly adapted in each case by using a method called [Responsive web design](http://en.wikipedia.org/wiki/Responsive_web_design).

There are cases where designers will want to change fonts, borders, visibility, or other aspects, but without changing the page content.

In GeneXus, [Themes](https://wiki.genexus.com/commwiki/wiki?6420) help in configuring the look & feel of web objects. To support a responsive web design, Conditional Class Properties allow us to specify the circumstances in which the properties of a class should be applied.

## [Example](#Example)

Consider the case where a designer must set a different Font size in accordance with the device’s screen.

Instead of the "Attribute" class with Font Size = 22pt, the designer wants to set the Font Size to 18pt for cases where the device is a phone.

The steps to take are as follows:

1. Open the GeneXus Theme.  
   Then, define a new Rule. The Rule may be defined either using the contextual menu Add Rule, or from the GeneXus menu: Edit -> Add Rule.  
     
   `[imagen omitida: wiki id 25124]`
2. Name the Rule as desired, for example: "Iphone like devices", and then set the conditions for this rule to apply.  
   The conditions are expressed using Max Width and Min Width properties.  
   Note: You can add more complex conditions using the Custom property.  
     
   `[imagen omitida: wiki id 25125]`
3. For each class in the Theme, you may re-define any of the class’ properties  in the context of this rule. This means that when the rule’s conditions are true, the settings for the class will apply.  
     
   `[imagen omitida: wiki id 25126]`

## [How to use the Editor to configure conditional classes](#How+to+use+the+Editor+to+configure+conditional+classes)

The Rules are shown as a list at the top of Theme Editor. Every time that we configure properties of a class in the context of that rule, we click on that Rule’s column.

Note: in the figure below, the Border property of Button class that is unconditional, is shown by clicking on Button class.

`[imagen omitida: wiki id 25128]`

The Border property of Button class which is conditional to the Rule, is shown by clicking on the column corresponding to that Rule:

`[imagen omitida: wiki id 25129]`

In sum, we can say that, at runtime, the values configured for classes regarding  conditional rules are taken into account only for devices matching the rules’ given conditions.

The classes and properties considered at runtime are the unconditional classes, plus the non-default properties of conditional classes.

## [Class properties inheritance](#Class+properties+inheritance)

The class properties defined in the context of a Rule inherit their values from unconditional classes.

In the example above, the Font Size property of the "Attribute" class inherits from the unconditional value of the property. So, if the designer sets "Use Default" for that property, it inherits the value configured for the Font Size property of the unconditional "Attribute" class.

Note: The implementation of this solution uses <http://en.wikipedia.org/wiki/Media_queries> in the [CSS](http://en.wikipedia.org/wiki/Cascading_Style_Sheets). The media query generated may be viewed in the CSS view in the Theme Editor.

`[imagen omitida: wiki id 25131]`


|  |
| --- |
| **Backlinks** |
| [CallOptions Target for Web](https://wiki.genexus.com/commwiki/wiki?32382) | [Container Theme Class for RWA](https://wiki.genexus.com/commwiki/wiki?25962) |
| [How to design a Responsive Web Application: Hiding a column in a grid](https://wiki.genexus.com/commwiki/wiki?25495) | [How to design a responsive web application: Hiding an element of the form](https://wiki.genexus.com/commwiki/wiki?25490) | [KB:OnlineShop (Shopping cart sample)](https://wiki.genexus.com/commwiki/wiki?27158) | [Responsive Table](https://wiki.genexus.com/commwiki/wiki?24961) |
| [Toc:Responsive Web Design in GeneXus](https://wiki.genexus.com/commwiki/wiki?29134) | [Theme Editor class menu options](https://wiki.genexus.com/commwiki/wiki?46483) |

---
