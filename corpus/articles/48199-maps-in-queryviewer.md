---
title: "Maps in QueryViewer"
source_id: 48199
source_url: https://wiki.genexus.com/commwiki/wiki?48199
genexus_version: "18"
---

# Maps in QueryViewer

In some situations, it is necessary to represent geographic locations such as countries, cities, etc.

As from [GeneXus 17 upgrade 4](https://wiki.genexus.com/commwiki/wiki?47936,,), this data can be represented on maps in the [QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075).

For example, look at the image below. It represents the total number of SARS-CoV-2 (Covid-19) cases per million people in each country.

`[imagen omitida: wiki id 48202]`

In this case, a Choropleth type map is used.

Now, look at this other map below. It represents the total number of deaths per million in each country.

`[imagen omitida: wiki id 48203]`

In this case, the data is represented in a Bubble type map.

**How is it done with GeneXus?**

For a query to be displayed on a map, in the [Query object](https://wiki.genexus.com/commwiki/wiki?9026) you need to define an attribute containing the ISO 3166-1 or ISO 3166-2 codes, depending on the geographic entities to be represented (if you want to use geographic coordinates instead, see below). For this attribute, its [Type property](https://wiki.genexus.com/commwiki/wiki?47137) must be set to Axis.

`[imagen omitida: wiki id 48205]`

In addition, it is necessary to add another attribute with the numerical data related to the geographic entity. In this case, it is CountryCasesPerMillion. The Type property of the Query element must be set to Datum.

`[imagen omitida: wiki id 48207]`

Additionally, you can choose the color of the data represented on the map. You can do this by setting the [ForeColor property](https://wiki.genexus.com/commwiki/wiki?8693) of the attribute whose type is Datum. Note that if no color is selected, a default color will be assigned.

Take a look at the following example. To represent specific colors for the different data values on the map, you can configure them in the [Conditional styles property](https://wiki.genexus.com/commwiki/wiki?48222).

`[imagen omitida: wiki id 48224]`

In this case, the Conditional styles property is configured as follows:

`[imagen omitida: wiki id 48225]`

`[imagen omitida: wiki id 48226]`

You can define this type of output using the [QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075). To this end, the QueryViewer control (inserted in a web form) must have the [Type property](https://wiki.genexus.com/commwiki/wiki?19612) set to Map.

`[imagen omitida: wiki id 48204]`

In the [Map Type property](https://wiki.genexus.com/commwiki/wiki?48161), select the map you want to use (Choropleth or Bubble).

`[imagen omitida: wiki id 52508]`

In the [Region property](https://wiki.genexus.com/commwiki/wiki?48162), set the type of map in which you want to represent the data (World, Continent, or Country).

`[imagen omitida: wiki id 52509]`

Note that if you select the [Country property](https://wiki.genexus.com/commwiki/wiki?48137) or [Continent property](https://wiki.genexus.com/commwiki/wiki?48138), the maps available for each option will be displayed.

The map type can also be configured programmatically through the enumerated domains QueryViewerMapType, QueryViewerCountry, QueryViewerRegion, and QueryViewerContinent.

Take a look at the following example. To represent the total vaccinated population per department per country, with a combo box to select the country and the type of map, you need to set it as follows:

`[imagen omitida: wiki id 48233]`

In this case, the enumerated domains used were QueryViewerRegion (to set the Region property to Country), QueryViewerCountry (to set the Country property to an initial value), and QueryViewerMapType (to change the MapType setting in Choropleth and Bubble).

`[imagen omitida: wiki id 48235]`  
Look at the following image. Changing the combo box options to another country and another type of map:

`[imagen omitida: wiki id 48237]`

**Using geographic coordinates**

Since [GeneXus 17 upgrade 7](https://wiki.genexus.com/commwiki/wiki?49301,,), it is possible to use GeoPoint attributes to place bubbles in a Bubble map at an exact coordinate (cities are a good example of this). The map below represents the total population of each capital city in Uruguay.

`[imagen omitida: wiki id 49541]`

Since [GeneXus 17 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?49616,,), it is possible to use GeoPoint attributes in a Choropleth map, adding the value of the points belonging to each region and reflecting the total value of the points that belong to each region of the map. The bubble map below represents the population by city in the United States of America.

`[imagen omitida: wiki id 49810]`

Now, look at this choropleth map below. The query and data are the same as in the previous case.

`[imagen omitida: wiki id 49811]`

The advantage of using attributes of the GeoPoint type with Bubble and Choropleth maps is that with Bubble maps you can view detailed information; in this case, the population of each city in the United States of America. On the other hand, in Choropleth maps with GeoPoint data type, you can see the information at the highest level by region.

In both cases, within the query, you can also define parameters based on a GeoPoint attribute or filter expressions containing "=" or "<>" comparisons or any of the following methods supported by the data type: IsEmpty(), IsNull(), FromWKT(), ToWKT() and Distance().

This feature is supported only in the following DMBS: SQLServer, MySQL, Oracle, and PostgreSQL.

**Considerations**

1. The library used is ECharts.

2. GeneXus provides the following country maps:

* Argentina
* Brazil
* Chile
* China
* Japan
* Mexico
* Paraguay
* Spain
* United States of America
* Uruguay

Only these country maps are supported and ready to use in QueryViewer (with all the ISO 3166-2 codes set for their main territorial divisions). This means that if you want to use a map that is not listed above, you must download and add the ISO 3166-2 codes in the relevant subdivisions of the map you want to use.

GeneXus provides a GitHub repository with the rest of the maps. If you want to use one of them it take a look in [How to use maps that are not provided by QueryViewer](https://wiki.genexus.com/commwiki/wiki?49859)

3. The following continent maps are available:

* Africa
* Antarctica
* Asia
* Europe
* North America
* Oceania
* South America.

In addition, the World map is offered.

### [Availability](#Availability)

This feature is available since [GeneXus 17 upgrade 4](https://wiki.genexus.com/commwiki/wiki?47936,,).

### [Videos](#Videos)


|  |
| --- |
| **Backlinks** |
|
| [Toc:GeoSuite](https://wiki.genexus.com/commwiki/wiki?52770) | [How to use maps that are not provided by QueryViewer](https://wiki.genexus.com/commwiki/wiki?49859) | [ItemClick Event](https://wiki.genexus.com/commwiki/wiki?19570) | [Query Object Compatibility](https://wiki.genexus.com/commwiki/wiki?11032) |
| [Category:QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075) | [Toc:Reporting in GeneXus](https://wiki.genexus.com/commwiki/wiki?25314) |

---
