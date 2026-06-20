---
title: "Query Card Type"
source_id: 31810
source_url: https://wiki.genexus.com/commwiki/wiki?31810
genexus_version: "18"
---

# Query Card Type

A Card is an output type which can be configured at the [Type property](https://wiki.genexus.com/commwiki/wiki?19612) of the [QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075) or [Query object](https://wiki.genexus.com/commwiki/wiki?9026) preview to show the result of a query.

`[imagen omitida: wiki id 31811]`

This type of output it's usually used to show KPI (Key Performance Indicator) as a percentage of a target value or both.

For a query to be shown in a Card, it has to contain an aggregated attribute in the Data section (property Axis = Data) at least.

#### [One indicator properties](#One+indicator+properties)

`[imagen omitida: wiki id 33182]`

If the [Query object](https://wiki.genexus.com/commwiki/wiki?9026) includes a Date or DateTime attribute, trending can be shown by setting the [Include Trend Property](https://wiki.genexus.com/commwiki/wiki?33127) in True. The trending it's shown with an arrow at the left of the value:

`[imagen omitida: wiki id 33135]`

Also, a Sparkline can be displayed by setting the [Include Sparkline Property](https://wiki.genexus.com/commwiki/wiki?33131) in True:

`[imagen omitida: wiki id 33134]`

When using a Card output for a Query sometimes can be useful to know the Minimum and Maximum value taken by the indicator. This can be accomplished by setting the [Include Max and Min Property](https://wiki.genexus.com/commwiki/wiki?33158) in True:

`[imagen omitida: wiki id 33160]`

#### [Two indicator properties](#Two+indicator+properties)

`[imagen omitida: wiki id 33183]`

If the query has more than one indicator defined, as shown in the preceding query, orientation can be set by choosing the corresponding value for the [Orientation Property](https://wiki.genexus.com/commwiki/wiki?33178):

**Horizontal:** `[imagen omitida: wiki id 33180]`

**Vertical:**`[imagen omitida: wiki id 33181]`

**Note:** all the properties defined for one indicator's queries can also be applied to two indicator's queries.

### [Customization](#Customization+)

The Card output type can be configurated using the QueryViewer theme class

`[imagen omitida: wiki id 31814]`

Where:

**Container class** allows selecting a Table class to set the container's aesthetics.

**Value class** allows selecting a TextBlock class to set the value's aesthetics.

**Title class** allows choosing a TextBlock class to set the title's aesthetics.

**Trend image class** allows selecting a Section class to set the image's aesthetics (not the image itself).

**Upward trend image**, **Downward trend image**, and **Sideward trend image** allows selecting the image to be shown when the trending is growing, decreasing or equal.

For example, after setting the above properties, a KPI can look as the following image:

`[imagen omitida: wiki id 31816]`


|  |
| --- |
| **Backlinks** |
| [Dashboard Card Include sparkline property](https://wiki.genexus.com/commwiki/wiki?40463) | [Dashboard Card Include trend property](https://wiki.genexus.com/commwiki/wiki?40464) | [Dashboard widgets](https://wiki.genexus.com/commwiki/wiki?36779) |
| [Include Max and Min Property](https://wiki.genexus.com/commwiki/wiki?33158) | [Include Sparkline Property](https://wiki.genexus.com/commwiki/wiki?33131) | [Include Trend Property](https://wiki.genexus.com/commwiki/wiki?33127) |
| [Orientation Property](https://wiki.genexus.com/commwiki/wiki?33178) | [Category:Query object](https://wiki.genexus.com/commwiki/wiki?9026) | [Category:QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075) |
|

---
