---
title: "Dynamic Combo Box"
source_id: 7598
source_url: https://wiki.genexus.com/commwiki/wiki?7598
genexus_version: "18"
---

# Dynamic Combo Box

It is a type of control similar to a combo box, and the difference is that the set of possible values are read from a database table. Two attributes are used to define a dynamic combo box: an attribute for descriptions and an attribute holding all possible values.

Dynamic combo boxes are loaded each time a transaction, work panel, or web panel storing the necessary values is loaded. All values are loaded only once (pagination on request is not available), so it is recommended that the controls be used with tables with not more than 100 records (prompts should be used for larger tables as they provide pagination on request). Although these Control Types do assist in making the application more user-friendly, their use is not recommended in intensive 'data-entry' transactions.

### [Item Descriptions](#Item+Descriptions)

Specifies the attribute from which the descriptions will be loaded. The selected attribute must be of the string type.

### [Sort Descriptions](#Sort+Descriptions)

Sorts the attribute by description.

*Note:  When Sort Description is disabled, GX will navigate the Table without any ORDER clause specified. The SQL specification doesn't state the specific order that records are to be returned, so it's going to be implementation dependent.*

### [Item Values](#Item+Values)

Specifies the selected attribute holding all possible values. Selected attribute holding all possible values.

### [Example](#Example)

The variable &CountryId may be defined as a dynamic combo box where the description will be CountryName and the value will be CountryId. GeneXus will define, during specification time, the table that must be used to load the dynamic combo box values (both attributes must be stored in the same table). If you desire, you may order the box by the description (Sort descriptions). Note that &CountryId and CountryId must have identical definitions.

`[imagen omitida: wiki id 20745]`

### [See Also](#See+Also)

[HowTo: Use the Dynamic Combo Box Control for Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?16778)  
[Control Information](https://wiki.genexus.com/commwiki/wiki?7241)


|  |
| --- |
| **Backlinks** |
| [A01:2021 - Broken access control](https://wiki.genexus.com/commwiki/wiki?50181) | [AddItem method](https://wiki.genexus.com/commwiki/wiki?8668) |
| [Call method](https://wiki.genexus.com/commwiki/wiki?16224) | [Control Information](https://wiki.genexus.com/commwiki/wiki?7241) | [Data Source From property](https://wiki.genexus.com/commwiki/wiki?22945) | [Data Source From property (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55489) |
| [Dynamic List Box](https://wiki.genexus.com/commwiki/wiki?7599) | [Edit with Suggest](https://wiki.genexus.com/commwiki/wiki?55531) | [FontUnderline property](https://wiki.genexus.com/commwiki/wiki?8780) | [GetDescriptionByKey Procedure Parameters property](https://wiki.genexus.com/commwiki/wiki?55468) |
| [GetDescriptionByKey Procedure property](https://wiki.genexus.com/commwiki/wiki?55413) | [HowTo: Use the Data Source From property](https://wiki.genexus.com/commwiki/wiki?22948) | [HowTo: Use the Dynamic Combo Box Control for Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?16778) | [HowTo: Using the Data Source From property (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55521) |
| [Item Descriptions property](https://wiki.genexus.com/commwiki/wiki?8807) | [Item Descriptions property (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?56079) | [Item Values property](https://wiki.genexus.com/commwiki/wiki?8808) | [Item Values property (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?56077) |
| [Notify Context Change property](https://wiki.genexus.com/commwiki/wiki?8856) | [Reload method](https://wiki.genexus.com/commwiki/wiki?8813) | [SetFocus method](https://wiki.genexus.com/commwiki/wiki?8836) | [Sort Descriptions Property](https://wiki.genexus.com/commwiki/wiki?8839) |
| [Specification Codes from spc0150 onwards](https://wiki.genexus.com/commwiki/wiki?6774) | [Text method](https://wiki.genexus.com/commwiki/wiki?8841) |

---
