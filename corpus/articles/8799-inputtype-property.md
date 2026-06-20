---
title: "InputType property"
source_id: 8799
source_url: https://wiki.genexus.com/commwiki/wiki?8799
genexus_version: "18"
---

# InputType property

Indicates whether the end user will type a value that corresponds to a code/identifier or the description associated with the value (and the code will be automatically obtained).

### [Values](#Values)

|  |  |
| --- | --- |
| **Values** | The end user will enter a value that corresponds to a code/identifier. This is the default value. |
| **Descriptions** | The end user will enter a description and the associated code/identifier will be automatically obtained. |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** [Attribute](https://wiki.genexus.com/commwiki/wiki?7240), [Variable](https://wiki.genexus.com/commwiki/wiki?7375)

### [Description](#Description)

Instead of forcing end users to handle codes, they can work with the descriptions that contain the semantic meaning. For example, they can type a CountryName and its CountryId can be automatically retrieved.

To achieve this for the attribute/variable for which you want to provide this functionality (for example, the CountryId attribute in a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) or a &CountryId variable in a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) among other possibilities), first, you have to set its **InputType property** to Descriptions.

After that, for the same attribute/variable (CountryId / &CountryId):

* The Item Values property must be set to CountryId (this will be assigned by default).
* The Item Descriptions property must be set to CountryName.

Thus, on the screen, the CountryId attribute will be “disguised” as CountryName. End users will see a field to type/select a CountryName, but the attribute is not CountryName. On the contrary, it is the CountryId attribute.

When an end user writes “Uruguay”, an internal search is performed to retrieve the code that corresponds to "Uruguay". That value (for example: 1) is stored in the CountryId attribute. This is totally transparent for the end user.

**Considerations**

There must be a bi-univocal relation between the code (or identifier) and the description. That is, for each description, there will be only one associated code. In the example, there can't be more than one country with the same name and a different identifier, because if there were, it would be impossible to perform the match. In other words, the attribute that stores the descriptions must be a [Candidate Key](https://wiki.genexus.com/commwiki/wiki?2199,,) of the table, that is, there must be a unique index for the CountryName attribute. When the candidate key doesn't exist, the following warning will be shown:

Spc0107 Candidate Key CountryName for CountryId may have duplicated values.

At runtime, if the end user selects a duplicated value (for which there is more than one CountryId) a “Country is ambiguous” error will be given, as it will not know which to choose.

**Note:** This property is not available for formula attributes.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [See Also](#See+Also)

[Suggest property](https://wiki.genexus.com/commwiki/wiki?8800)


|  |
| --- |
| **Backlinks** |
| [Attribute/Variable control properties in Web Forms](https://wiki.genexus.com/commwiki/wiki?8133) | [Data Source From property](https://wiki.genexus.com/commwiki/wiki?22945) | [Edit with Suggest](https://wiki.genexus.com/commwiki/wiki?55531) |
| [Item Descriptions property](https://wiki.genexus.com/commwiki/wiki?8807) | [Item Descriptions property (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?56079) | [Item Values property](https://wiki.genexus.com/commwiki/wiki?8808) | [Item Values property (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?56077) |
| [Specification Codes from spc0150 onwards](https://wiki.genexus.com/commwiki/wiki?6774) | [Suggest property](https://wiki.genexus.com/commwiki/wiki?8800) |

---
