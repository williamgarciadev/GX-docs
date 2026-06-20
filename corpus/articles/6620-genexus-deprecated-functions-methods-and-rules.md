---
title: "GeneXus deprecated functions, methods, and rules"
source_id: 6620
source_url: https://wiki.genexus.com/commwiki/wiki?6620
genexus_version: "18"
---

# GeneXus deprecated functions, methods, and rules

The term "deprecated" is used to refer to features that still work in the current version of GeneXus but won't be supported in the future. Therefore, it is advisable to replace them with the new ones.

In this article, you can find a list of deprecated functions, methods, and rules.

First, take into account that deprecated functions, methods, rules, etc. are shown in the IDE with a different color than non-deprecated ones, as shown below.

`[imagen omitida: wiki id 54404]`

Note that the [AddMth function](https://wiki.genexus.com/commwiki/wiki?8314) is not deprecated while the [DeleteFile function](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?8388,,) is deprecated.

Besides, when trying to save, if deprecated functions/methods/rules are detected, an [src0222 message](https://wiki.genexus.com/commwiki/wiki?38589) will appear in the output when saving.

 In addition, when selecting:

* Insert > Function
* Insert > Method
* Insert > Rule

...the deprecated ones are not offered.

### Deprecated functions

|  |  |
| --- | --- |
| **[DeleteFile()](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?8388,,)** | Deprecated since GeneXus X. Use the [Delete method](https://wiki.genexus.com/commwiki/wiki?6014) as follows:  ``` &File.Source = "file name" &File.Delete() ``` |
| **Udf()** | Deprecated since [GeneXus 9.0](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?3750,,). Use the [Udp method](https://wiki.genexus.com/commwiki/wiki?3964) instead. |
| **[GxCalculate()](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?14096,,)** | Deprecated since [GeneXus 15](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?27605,,). |
| **[GxCopyFile()](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?14099,,)** | Deprecated since [GeneXus 15](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?27605,,). |
| **[GxNewFile()](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?14101,,)** | Deprecated since [GeneXus 15](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?27605,,). |
| **[GxSelColor()](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?14103,,)** | Deprecated since [GeneXus 15](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?27605,,). |
| **[GxSelDir()](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?14105,,)** | Deprecated since [GeneXus 15](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?27605,,). |
| **[GxSelFile()](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?14087,,)** | Deprecated since [GeneXus 15](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?27605,,). |
| **[GxSelFont()](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?14100,,)** | Deprecated since [GeneXus 15](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?27605,,). |
| **[GxSelPict()](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?14102,,)** | Deprecated since [GeneXus 15](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?27605,,). |
| **[GxSelPrn()](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?14104,,)** | Deprecated since [GeneXus 15](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?27605,,). |
| **LoadBitmap()** | Use the [FromURL method](https://wiki.genexus.com/commwiki/wiki?9644) instead. |
| **After(Attribute)** | Deprecated since GeneXus 8.0. Use the [Dependencies clause](https://wiki.genexus.com/commwiki/wiki?6868) instead. |
| **Old()** | Use the [GetOldValue method](https://wiki.genexus.com/commwiki/wiki?12734) instead. |

### [Deprecated rules](#Deprecated+rules)

|  |  |
| --- | --- |
| **Allownulls()** | This rule is deprecated. It can still be used when the [Nullable property](https://wiki.genexus.com/commwiki/wiki?7642) is set as "Compatible".  It is advisable to change the Nullable property to "Yes" or "No" and delete the rule. Probably, in this case, the expected value is "Yes". |
| **Hidden()** | This rule is no longer generated.  You can achieve the same behavior by adding the attributes to the Grid and setting their [Visible property](https://wiki.genexus.com/commwiki/wiki?8849) = False.  When working with a [Free Style Grid control](https://wiki.genexus.com/commwiki/wiki?6058), the Visible property must be set by code (Attribute.Visible = 0). |
| **Nocheck() / Noread()** | In [knowledge bases](https://wiki.genexus.com/commwiki/wiki?1836) coming from old versions of GeneXus, you can usually see the use of Nocheck() / Noread() rules in objects.  In many cases, they were defined as a result of not having suitable subtype groups available. This situation should be reviewed and corrected. |
| **SEARCH(<condition>)** | Sets the positioning condition in the grid. Notice that this is different from a condition that filters data. The search is used to set the position in the grid.  Valid in [Work Panel object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7387,,), deprecated since [GeneXus 15](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?27605,,). |

### [Deprecated methods](#Deprecated+methods)

|  |  |
| --- | --- |
| **[Return method from SDActions external object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?15836,,)** | Deprecated since [GeneXus 15](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?27605,,). Use the [Return command](https://wiki.genexus.com/commwiki/wiki?31353) instead. |
| **[GetResponse()](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7097,,)** | Deprecated since [GeneXus 15](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?27605,,). |
| **ScanBarcode()** | Deprecated since [GeneXus X Evolution 2 Upgrade 3](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?22061,,). Use the [Scanner external object](https://wiki.genexus.com/commwiki/wiki?31316) instead. |
| **[DrawGeoLine()](https://wiki.genexus.com/commwiki/wiki?47026)** | Use the [DrawGeography method](https://wiki.genexus.com/commwiki/wiki?47024) instead. |
| **Xmlstart()** |  |
| **Xmlend()** |  |
| **Xmlraw()** |  |
