---
title: "GAM Backend Style Override property"
source_id: 51754
source_url: https://wiki.genexus.com/commwiki/wiki?51754
genexus_version: "18"
---

# GAM Backend Style Override property

Defines the Design System object used to customize the GAM Backend style.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** [Version](https://wiki.genexus.com/commwiki/wiki?7860)

### [Description](#Description)

This property allows you to select your custom [Design System](https://wiki.genexus.com/commwiki/wiki?40108) based on [Unanimo](https://wiki.genexus.com/commwiki/wiki?48382) to be used in the [GAM Backend](https://wiki.genexus.com/commwiki/wiki?29699).

The default value is none, which means that it takes the Design System that comes by default with the GAM Backend.

**Note:**

When the "Run GAM Backend" option is executed from the Build menu or you do a Build, the file \Web\GAMResources\English\GAMDesignSystem.css is edited to add the import to the Design System selected in the GAM Backend Style Override property for each different language.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

Consider the following Design System:

```
styles NewKBGAM1 { 
@import GeneXusUnanimo.UnanimoWeb; 
}
```

Change the primary and secondary colors as shown below (based on the same tokens as Unanimo Design System):

```
tokens NewKBGAM1 (color-scheme:[light]|dark)
{
    //COLORS
    @color-scheme = light {
        #colors
        {
            #region Unanimo_Colors
                primary: #ECF269;
                secondary: #388645;
            #endregion
        }
    }
}
```

Select the Design System called "NewKBGAM1" in the GAM Backend Style Override property at the version level.

The file GAMDesignSystem.css is left with the following content (the changes made to the original file, which is distributed with the GAM compiled backend, are highlighted in bold):

```
@import "GeneXusUnanimo.UnanimoWeb.css";
@import "GeneXusReporting.QueryViewer.css";
@import "GeneXusReporting.DashboardViewer.css";
@import "GAMDesignSystem_Tokens.css";
/* gx-style-customization - start */
@import "../../Resources/English/NewKBGAM1.css";
/* gx-style-customization - end */

@layer GAMDesignSystem {
/* gx-css-import ignore - start */
 
/* gx-css-import ignore - end */
/* gx-css-user-controls - start */
/* gx-css-user-controls - end */
}
```

The GAM backend takes the style of the NewKBGAM1 Design System. It will look as follows:

`[imagen omitida: wiki id 51820]`

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

No action is required to apply the corresponding changes when the property value is configured.


|  |
| --- |
| **Backlinks** |
| [Customize Unanimo](https://wiki.genexus.com/commwiki/wiki?52178) | [Total Experience with GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51570) | [Toc:Unanimo](https://wiki.genexus.com/commwiki/wiki?48382) |

---
