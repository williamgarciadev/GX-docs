---
title: "GeneXus For SAP Filters"
source_id: 38588
source_url: https://wiki.genexus.com/commwiki/wiki?38588
genexus_version: "18"
---

# GeneXus For SAP Filters

Filters allow you to insert controls in order to filter grid records that meet the filter criteria. To view their properties, you have to be positioned on the filter.

`[imagen omitida: wiki id 39062]`

Filters have the following properties:

* Name: Defines the name of the variable that will represent the filter control of the form.
* Description: Specifies the text that will appear if the Show description property is True.
* Right Text: If not empty, the text will be included next to the filter.
* Domain/attribute: Is the domain or attribute on which the variable is based.
* Value default: Specifies the default value that will be displayed in the filter when the page loads for the first time.
* Value all: It can only be applied if the control type is a combo box; specifies if there is an option to add all values or not.
* Condition: Specifies the statement that will be executed within the filter variable value and the attribute value of every transaction record to determine whether the record meets the condition or not and, therefore, if the record will be included in a grid or not. In other words, it represents the condition statement associated with the filter.

In the example above, the filter will be applied to CountryName only if you add a string to the filters; otherwise, it will show all records.

```
CustomerName.ToLower() like '%' +  &CustomerName.ToLower() when not &CustomerName.IsEmpty()
```

It is possible to add filters without conditions, associating with filters with a condition concatenated by OR.

There are different kinds of filters, as follows:

* FilterAttribute: Only filters with one condition.
* FilterAttributeRange: Will add two search fields for each Range filter (from-to). It is useful for date, datetime, numbers or characters.
* DynamicFilters: Contain operators to select. For example, search for a value at the beginning of the word or the content (in the case of a character filter).
* FilterAttributeMultiple: Allows end users to select more than one item from a list or a prompt.

### 

### [FilterAttribute](#FilterAttribute)

The FilterAttribute filters with only one condition.

### [FilterAttributeRange](#FilterAttributeRange)

The FilterAttributeRange allows filtering items within a range. Its Middle Text property allows you to customize the text to be shown between the range fields; by default, it is "to."

### [Dynamic Filters](#Dynamic+Filters)

They group filters of all kinds so the user can select which filters to apply at runtime.

To add filters, right-click on the dynamic filter, click on Add, and select the kind of filter you want to add: FixedFilter (always stays in the header), FilterAttribute, FilterFilterAttributeRange, FilterAttributeMultiple.

`[imagen omitida: wiki id 38673]`

### [FilterAttributeMultiple](#FilterAttributeMultiple)

The Type property defines whether the filter will be Prompt or DropDownSelector.

`[imagen omitida: wiki id 38675]`

The Type definition properties are as follows:

* Values Attribute: Defines the attribute that will be used to filter.
* Descriptions Attribute: Defines the description of the values to be shown on the list.

The condition property is set by default as follows:

```
<SelectedValuesAttribute> in &<SelectedValuesAttribute>Values when &<SelectedValuesAttribute>Values.Count > 0.
```

Also, you can set whatever condition you need.

By setting the Filter Attribute Multiple type to DropDown selector, the Filter Definition property will appear.

`[imagen omitida: wiki id 38674]`

This property determines if the filter is set by default or if it will be customized for this attribute in particular.

When "custom" is selected, these properties will appear:

* Include Search Box: Determines if the filter will have a search box; this is useful if you have many filters.
* Search Box Condition: Defines the condition to use in the search.
* Data List: Defines whether the list will be dynamic or fixed. That is to say, if it loads attribute values or fixed descriptions and keys previously entered.
* Data List Include Total Records: Defines whether to include the number of elements of each value, next to them (For example: Countries(3), Cities(15), Tours(25)). This is only applicable when the list is dynamic.
* Data List Max Values: Defines the maximum number of items to display on the dynamic data list.

When the Filter Attribute Multiple type is set to Prompt, you must use a Prompt multiple object that will be opened to select items.


|  |
| --- |
| **Backlinks** |
| [GeneXus For SAP Systems - KPI Worklist Floorplan](https://wiki.genexus.com/commwiki/wiki?38645) | [GeneXus For SAP Systems - List Report Floorplan](https://wiki.genexus.com/commwiki/wiki?38572) | [GeneXus For SAP Systems - Simple Worklist Floorplan](https://wiki.genexus.com/commwiki/wiki?38636) |
| [GeneXus For SAP Systems - Simple Worklist with global action Floorplan](https://wiki.genexus.com/commwiki/wiki?38796) | [GeneXus For SAP Systems - Split Screen Master List Floorplan](https://wiki.genexus.com/commwiki/wiki?38873) | [GeneXus For SAP Systems - Split Screen Master List with amount Floorplan](https://wiki.genexus.com/commwiki/wiki?38912) | [GeneXus For SAP Systems - Split Screen Master List with amount Floorplan (GeneXus 18 Upgrade 3)](https://wiki.genexus.com/commwiki/wiki?55230) |
| [GeneXus For SAP Systems KPI Worklist Floorplan (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54915) | [GeneXus For SAP Systems List Report Floorplan (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54853) | [GeneXus For SAP Systems Simple Worklist Floorplan (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54970) | [GeneXus For SAP Systems Simple Worklist with global action Floorplan (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55017) |
| [GeneXus For SAP Systems Split Screen Master List Floorplan (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54939) |

---
