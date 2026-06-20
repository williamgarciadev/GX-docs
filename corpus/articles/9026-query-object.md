---
title: "Query object"
source_id: 9026
source_url: https://wiki.genexus.com/commwiki/wiki?9026
genexus_version: "18"
---

# Query object

Defines a reusable query to the application database.

### [Description](#Description)

Many times you may need to make queries to the database to analyze data and be able to make decisions.

In this sense, you may need to group data according to one or several criteria, make calculations, and finally view the result in a certain way, such as:

* A static table, with fixed rows and columns
* A dynamic table, which allows, for instance, shifting columns and grouping data
* Or a chart.

The Query object allows you to create these queries in a simple and intuitive way, thus enhancing the value of the information retrieved from the database.

**Note**: To execute a Query object at runtime, you must use a [QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075).

### Query object creation and description

You can create a Query object through the [New Object dialog](https://wiki.genexus.com/commwiki/wiki?9931) (it is inside the Reporting group).

Query objects are composed of four sections:

1) Structure  
2) SQL Statement  
3) Preview  
4) Documentation.

These sections are displayed below the query's name.

`[imagen omitida: wiki id 52589]`

### [1) Structure](#1%29+Structure)

The most important task executed using the Query object is the definition of the query. Each Query object defines one query over the database, and a very intuitive GeneXus-assisted definition interface is provided to make this task easier.

`[imagen omitida: wiki id 52598]`

A query is defined in the Structure section of the object, which has four main subsections:

* **Attributes:**Attributes that will be returned in the query result.
* **Parameters:** If the query receives parameters to filter the result, it must be declared in this section.
* **Filters:**Filters applied to the query's result.
* **OrderBy:**Declares the desired default query order. This option is not taken into account when using a pivot table output.

After filling the query structure with the proper data, the object will look, for example, as shown in the following image:

`[imagen omitida: wiki id 52591]`

### [Subsections](#Subsections)

#### [1.1) Attributes](#1.1%29+Attributes)

The attributes involved in the query are selected here in a simple flat list. They can be added to the list by dragging them from the *Work With Attributes* toolbox or just writing the attribute name inline in the query structure. The suggest mechanism is provided while writing to make attribute selection easier and faster.

`[imagen omitida: wiki id 52592]`

The description column will be the label for the attribute in the query output, and it is recommended to check these values when defining the Query. The attribute list can be reorganized by moving the items up and down; check the contextual menu for more options.

Also, it is possible to define the following for the attributes:

* **Aggregation function:** The functions available are *Count*, *Sum,* *Average, Min, and Max* (\*). The definition of nested aggregation functions is allowed –that is, Sum(Count(ProductName)). The function to be applied can be set by typing it inline or by right-clicking on an attribute with aggregation and using the contextual menu.

You can group by an attribute before applying the aggregation function. This functionality allows the user to consult the data in different ways without creating all the DataBase tables.

For example, suppose you have a Year table with the attributes YearId, MonthId, and DayId (the table will have 365 records), but you want to make a Query by Month. To do this, you can use the aggregation Sum(YearId) by (MonthId) that will show only 12 records instead of 365. The syntax for this aggregation is as follows:

```
<Aggregation function>(<AttributeName>) by <AttributeName1>, <AttributeName2>, ..,<AttributeNamen>
```

\* Not all aggregation functions apply to all attribute types. ***Sum,******Average, Max,*and *Min* are only available for Numeric attributes**. Also, when dragging an attribute that is Numeric with decimals to the query structure, the *Sum* function is automatically applied.

* **Percentage:** Sets the attribute information to be displayed in percentage terms. Only for attributes with aggregation functions previously applied. You can set it to be displayed as a percentage with the *Show as percentage* contextual menu option.
* [**Filters**](https://wiki.genexus.com/commwiki/wiki?12250): Particular filters (when using an aggregated attribute) can define different kinds of filters for the attribute. The options are the same when defining a global one; refer to the filter section below.
* [**Expressions**](https://wiki.genexus.com/commwiki/wiki?11782)

Properties (displayed in the Properties section) vary depending on the type of the selected attribute:

For example, the [**ShowAllValues**](https://wiki.genexus.com/commwiki/wiki?12555) propertyis only available for attributes with no aggregation functions applied, and the properties **Percentage** and [**Calculation Group**](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?30963,,) are only available for attributes with aggregation applied.

|  |  |
| --- | --- |
| **Attributes with aggregation functions applied** | **Attributes with no aggregation functions applied** |
|  |  |

#### [1.2) Parameters](#1.2%29+Parameters)

In this section, it is possible to define the query parameters and configure the following properties:

`[imagen omitida: wiki id 32629]`

* **Name:** Parameter name. This property value will be used when the query parameter values are set at runtime for the [QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075).
* **Description:** Parameter description.
* **Based On:** Defines the parameter type based on an attribute or domain.
* **Data type:** Parameter type (depending on the type set here other properties can be available, such as *Length, Decimals, Signed. Date format,*or *Hour format*).
* **Is Collection:** Defines whether the parameter is of type Collection. If the value is true, another property is displayed (Collection value) to determine the values of the Collection. More information: [Query Object: Parameters](https://wiki.genexus.com/commwiki/wiki?15294).
* **Value:** Default value for the parameter. You will set it at runtime; otherwise, the default value will be applied.

#### [1.3) Filters](#1.3%29+Filters)

This section describes the query filters in detail (with formal syntax diagrams): [Query object: Filters](https://wiki.genexus.com/commwiki/wiki?12250)

`[imagen omitida: wiki id 52421]`

Each filter definition consists of a group of filter elements linked with a logic operator (AND, OR). These elements can be as follows:

* **List Filter:** Indicates a list of values for the attribute to be filtered. The syntax is as follows:

```
<AttributeName> in (<Value>, <Value>, ..., <Value>)
```

* **Range Filter:** Indicates a filter using a list of value ranges linked with a logic operator (AND, OR). In each range, you can use relational operators (<, >, >=, <=, =), constants, and parameters. This type of filter also accepts many types of syntax, for example:

```
<AttributeName> in (<Value> to <Value>) or <AttributeName>+"-"+<AttributeName> in (<Value> to <Value>)
```

* **Filter by Other Attribute:** Indicates a filter using the values of another attribute.
* **Other filter groups**: Using filter groups, any multilevel filter definition can be inserted in the query.

### [2) SQL Statement](#2%29+SQL+Statement)

The SQL statement that will be used to retrieve the data from the database can be seen in the SQL Statement section.

`[imagen omitida: wiki id 52593]`

### [3) Preview](#3%29+Preview)

This option allows you to easily modify all the properties related to the Output of the Query object and see all its effects immediately. The [QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075) takes all the property values from the associated Query object as default values.

To preview the query being defined there are five different options:

* Table
* PivotTable
* Chart
* Card
* Map

#### [**Table Option**](#Table+Option)

`[imagen omitida: wiki id 52599]`

#### [**PivotTable Option**](#PivotTable+Option)

`[imagen omitida: wiki id 52600]`

#### [**Chart Option**](#Chart+Option)

`[imagen omitida: wiki id 52601]`

#### [**Card Option**](#Card+Option)

`[imagen omitida: wiki id 52602]`

#### [**Map Option**](#Map+Option)

`[imagen omitida: wiki id 52609]`

This Preview tab is the same as the query you will get in a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) using the [QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075).

A complete example using the Query object and Query Viewer control can be found here: [Query Object Usage Example](https://wiki.genexus.com/commwiki/wiki?33991).

### [See Also](#See+Also)

[Query Element](https://wiki.genexus.com/commwiki/wiki?19788)  
[QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075)  
[Query Card Type](https://wiki.genexus.com/commwiki/wiki?31810)


|  |
| --- |
| **Pages** |
| [Allow Change Axes Order property](https://wiki.genexus.com/commwiki/wiki?19603) | [Average type property](https://wiki.genexus.com/commwiki/wiki?50386) | [Axis and Visible property refactoring](https://wiki.genexus.com/commwiki/wiki?47094) |
| [Axis property in Query Element](https://wiki.genexus.com/commwiki/wiki?47159) | [Continent property in Query](https://wiki.genexus.com/commwiki/wiki?48168) | [Country property in Query](https://wiki.genexus.com/commwiki/wiki?48170) |
| [Defining a common language for GeneXus Queries and GXquery 4.0](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?26173,Defining+a+common+language+for+GeneXus+Queries+and+GXquery+4.0,) | [Difference from property](https://wiki.genexus.com/commwiki/wiki?50340) | [Elements Property](https://wiki.genexus.com/commwiki/wiki?19577) |
| [Grouping time values in the Query object](https://wiki.genexus.com/commwiki/wiki?23426) | [Include Max and Min Property](https://wiki.genexus.com/commwiki/wiki?33158) | [Include Sparkline Property](https://wiki.genexus.com/commwiki/wiki?33131) |
| [Include Trend Property](https://wiki.genexus.com/commwiki/wiki?33127) | [Map type property in Query](https://wiki.genexus.com/commwiki/wiki?48163) | [Max Rows property](https://wiki.genexus.com/commwiki/wiki?18477) |
| [Number of terms property](https://wiki.genexus.com/commwiki/wiki?50339) | [Orientation Property](https://wiki.genexus.com/commwiki/wiki?33178) | [Query Card Type](https://wiki.genexus.com/commwiki/wiki?31810) |
| [Query Object - Troubleshooting](https://wiki.genexus.com/commwiki/wiki?9105) | [Query Object Considerations](https://wiki.genexus.com/commwiki/wiki?12038) | [Query Object Considerations (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54655) |
| [Query object expressions](https://wiki.genexus.com/commwiki/wiki?11782) | [Query Object Usage Example](https://wiki.genexus.com/commwiki/wiki?33991) | [Query object: Filters](https://wiki.genexus.com/commwiki/wiki?12250) |
| [Query Object: Parameters](https://wiki.genexus.com/commwiki/wiki?15294) | [Raise ItemClick event property](https://wiki.genexus.com/commwiki/wiki?42812) | [Region property in Query](https://wiki.genexus.com/commwiki/wiki?48166) |
| [RemoveDuplicates property](https://wiki.genexus.com/commwiki/wiki?18476) | [Show as percentage property](https://wiki.genexus.com/commwiki/wiki?50341) | [Show values as property](https://wiki.genexus.com/commwiki/wiki?50338) |
| [Timeline chart](https://wiki.genexus.com/commwiki/wiki?30172) | [Type property in Query Element](https://wiki.genexus.com/commwiki/wiki?47137) | [Use Domain Descriptions property](https://wiki.genexus.com/commwiki/wiki?47098) |
| [Visible property in Query Element](https://wiki.genexus.com/commwiki/wiki?47140) | [YAxis Title property](https://wiki.genexus.com/commwiki/wiki?42240) |

---
