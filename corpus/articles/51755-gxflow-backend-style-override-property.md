---
title: "GXflow Backend Style Override property"
source_id: 51755
source_url: https://wiki.genexus.com/commwiki/wiki?51755
genexus_version: "18"
---

# GXflow Backend Style Override property

Defines the Design System object used to customize the GXflow Backend style.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** [Version](https://wiki.genexus.com/commwiki/wiki?7860)

### [Description](#Description)

This property allows you to select your custom [Design System](https://wiki.genexus.com/commwiki/wiki?40108) based on [Unanimo](https://wiki.genexus.com/commwiki/wiki?48382) to be used in the [GXflow](https://wiki.genexus.com/commwiki/wiki?4179,,) backend.

Once you select your Design System in the GXflow Backend Style Override property, the classes and definitions of that Design System are applied to the GXflow Backend.

The default value is none, which means that it takes the Design System that comes by default with the GXflow Backend.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

Consider the following Design System:

```
styles NewKB { 
@import GeneXusUnanimo.UnanimoWeb; 
}
```

Change the primary and secondary colors as shown below (based on the same tokens as Unanimo Design System):

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

Select the Design System called "NewKB" in the GXflow Backend Style Override property at the version level.

The file GXflowDS.css is left in the following path: Web\GXflowResources\English. It is highlighted in bold in the following example:

```
@import"GeneXusUnanimo.UnanimoWeb.css";

@import"GeneXusReporting.QueryViewer.css";

@import"GeneXusReporting.DashboardViewer.css";

@import"GXflowDS_Tokens.css";
/* [gx-style-customization - start] */
@import "../../Resources/English/NewKB.css";
/* [gx-style-customization - end] */
```

The GXflow backend takes the style of the NewKB Design System. It will look as follows:

`[imagen omitida: wiki id 51826]`

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build All](https://wiki.genexus.com/commwiki/wiki?5691).


|  |
| --- |
| **Backlinks** |
| [Customize Unanimo](https://wiki.genexus.com/commwiki/wiki?52178) | [GeneXus 18 BPM Suite Release Notes](https://wiki.genexus.com/commwiki/wiki?51076) | [Total Experience with GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51570) |
| [Toc:Unanimo](https://wiki.genexus.com/commwiki/wiki?48382) |

---
