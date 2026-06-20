---
title: "HowTo: Use maps that are not provided by QueryViewer"
source_id: 49859
source_url: https://wiki.genexus.com/commwiki/wiki?49859
genexus_version: "18"
---

# HowTo: Use maps that are not provided by QueryViewer

The [QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075) provides and supports the following maps:

* World
* All the continents
* The following countries:
  + Argentina
  + Brazil
  + Chile
  + China
  + Japan
  + Mexico
  + Paraguay
  + Spain
  + United States of America
  + Uruguay

These are the countries that are most used by the GeneXus community. With every map included in the QueryViewer the size of the deploy package increases. In order to keep it as small as possible no further maps will be, by default, included in QueryViewer.

But you can still use any country you need. You simply have to follow the steps below:

1) Access the following GitHub repository: <https://github.com/genexuslabs/echarts-countries-js/tree/releases/1.0>

2) Choose the country map that you need and download it.

3) If you want to use ISO 3166-2 codes as the geographical dimension you will need to make some editions to the map as explained below.

4) Copy the downloaded map in the following GeneXus directories:

* UserControls\QueryViewer\Echarts\countries
* Packages\Reporting\QueryViewer\Echarts\countries

5) Restart GeneXus

### [How to add the ISO code to a map?](#How+to+add+the+ISO+code+to+a+map%3F)

To use a map from the GitHub repository above and use ISO 3166-2 codes as the geographical dimension you must edit and add the ISO 3166-2 codes for all the first level subdivisions of that country.

To do so, open the JS file of the required map (i.e. if you want to add the ISO 3166-2 codes of France, the map name will be fr-all.js).

In the fr-all.js file, inside the properties of each subdivision, add the "iso-code" property as shown in the following example:

`[imagen omitida: wiki id 49923]`

You can find the ISO code of each country and subdivision in [ISO - International Organization for Standardization.](https://www.iso.org/obp/ui/#search/code/)

### [Considerations](#Considerations)

* In the GitHub repository, you can find the map of a country named according to the ISO Code 3166. The structure of the name of any map is the following: **(iso code 3166)-all.js**. For example, if you need the map of France you have to look for the file with the name **fr-all.js**.
* Please, don't change the name of the map that you downloaded from the GitHub repository.
* In the same way you can define the property "center" to the different regions as shown in the following example:

`[imagen omitida: wiki id 49925]`

This is useful when you use bubble maps (with ISO 3166 codes) and want the bubble to be centered in specific coordinates.  
By default the position of the bubbles is calculated as the center of the region's polygon but for some areas that doesn't represent very well the main geographic area, or it's located outside the polygon for very irregular areas.

* For download a map from GitHub, there are some tips:

1. If you need all the country map collection you can download this in a zip folder:

`[imagen omitida: wiki id 50002]`

2. If you need only some maps and you want to download individually, you can follow the next steps:

-Select the map of the country that you want   
-Select "Raw"  
-Press "Ctrl+S" and you can save it with the original name.

`[imagen omitida: wiki id 50003]`

### [See Also](#See+Also)

[Maps in QueryViewer](https://wiki.genexus.com/commwiki/wiki?48199)


|  |
| --- |
| **Backlinks** |
| [Maps in QueryViewer](https://wiki.genexus.com/commwiki/wiki?48199) | [Query Object Compatibility](https://wiki.genexus.com/commwiki/wiki?11032) |
| [Table of contents:Reporting in GeneXus](https://wiki.genexus.com/commwiki/wiki?25314) |

---
