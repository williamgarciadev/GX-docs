---
title: "Customize Unanimo"
source_id: 52178
source_url: https://wiki.genexus.com/commwiki/wiki?52178
genexus_version: "18"
---

# Customize Unanimo

You can use Unanimo as a base for your own [Design System](https://wiki.genexus.com/commwiki/wiki?40108). To do so, you can override the values of the [Tokens](https://wiki.genexus.com/commwiki/wiki?47378) defined in [Unanimo](https://wiki.genexus.com/commwiki/wiki?48382) Design System and the styles properties, as well as extend it by creating your own Tokens and [Styles](https://wiki.genexus.com/commwiki/wiki?47379).

As described in [How to use Unanimo](https://wiki.genexus.com/commwiki/wiki?52176), a [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375) is created in your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) and configured as the [Default Style](https://wiki.genexus.com/commwiki/wiki?8145) with the following content in the Style section:

```
styles NewKBName {

@import GeneXusUnanimo.UnanimoWeb;

}
```

Then if you run your web application, by default looks as shown below:

`[imagen omitida: wiki id 52189]`  

### [Token customization](#Token+customization)

To change the primary and secondary colors as shown below (based on the same Tokens as Unanimo Design System), go to the Token section in the Design System configured as the default style and type the following:

```
tokens NewKB (color-scheme:[light]|dark)
{
    //COLORS
    @color-scheme = light {
        #colors
        {
            #region Unanimo_Colors
                primary: #6AC796;
                secondary: #639FBA;
            #endregion
        }
    }
}
```

Note: In this example, only the light color-scheme is customized.

In this way, you are overriding the definition of the Token value.

After saving the changes in the Design System, you can force the reload of the browser and the Work With will look as shown below:

`[imagen omitida: wiki id 52190]`

The same applies to any Token that is defined in Unanimo.

### [Style customization](#Style+customization)

See how to change some styles defined in Unanimo with your own customizations.

For example, to change the style for the title, you can add the definition for the class heading-01 in the Design System used for the KB as the default style and customize any property.  

```
​​styles NewKBName {
@import GeneXusUnanimo.UnanimoWeb;

.heading-01 {
            font-family: $fonts.primary-semibold;
            font-size: $fontSizes.l;
            color: $colors.primary;
    }
}
```

After saving these changes and forcing the reload of the browser, you can see that the title “Products” looks smaller and with a different color.

`[imagen omitida: wiki id 52191]`

You can customize any of the classes defined in Unanimo Design Systems in this way.

See [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375) to learn more about how to work with Tokens and Styles; in particular, the [Include style rule](https://wiki.genexus.com/commwiki/wiki?49353) is very useful to customize classes.

### [How to apply the customization in GAM and GXflow UI](#How+to+apply+the+customization+in+GAM+and+GXflow+UI)

Since GeneXus 18, you can customize the built-in UI that is distributed for GAM and GXflow. The same Design System that is customized for your application can be used to customize the built-in UIs.

See these documents to learn how to do it:

* [GAM Backend Style Override property](https://wiki.genexus.com/commwiki/wiki?51754)
* [GXflow Backend Style Override property](https://wiki.genexus.com/commwiki/wiki?51755)

### [See Also](#See+Also)

* [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375)
* [Style and Default Style properties](https://wiki.genexus.com/commwiki/wiki?8145)

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [UX Design. Introduction](https://training.genexus.com/en/learning/courses/genexus/v18/core/content/ux-design-introduction)


|  |
| --- |
| **Backlinks** |
| [Toc:Unanimo](https://wiki.genexus.com/commwiki/wiki?48382) | [Unanimo module components](https://wiki.genexus.com/commwiki/wiki?52175) |

---
