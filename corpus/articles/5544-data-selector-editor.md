---
title: "Data Selector Editor"
source_id: 5544
source_url: https://wiki.genexus.com/commwiki/wiki?5544
genexus_version: "18"
---

# Data Selector Editor

When editing a [Data Selector object](https://wiki.genexus.com/commwiki/wiki?5271), two tabs are displayed:

* [Data Selector Structure](https://wiki.genexus.com/commwiki/wiki?5544)
* [Documentation](https://wiki.genexus.com/commwiki/wiki?6685)

### [**Data Selector Structure**](#Data+Selector+Structure)

The Data Selector Structure contains 4 sections:

**1) Parameters**

Here, enter the list of parameters received from the Data Selector invocation to use them in Conditions.  
Parameters may be variables or attributes (if a parameter is declared as an attribute, it will automatically act as a filter by equality).

**2) Conditions**

Here, define the filter conditions to retrieve the desired data.  
You can use logical operators: 'and', 'or', and 'not'.  If you define conditions in multiple lines, all lines will be connected with the 'and' operator.  
Conditional constraints are supported using the 'When' clause, which can only refer to variables included in the Parameters section.

**3) Orders**

In this section, you can define conditional orders.  
To define a compound order, specify all the attributes that compose it in the same line, separated by commas.  
Use the 'when' clause, which can only refer to variables included in the Parameters section.

**4) Defined By**

Here, include an attribute or list of attributes that determine the final base table.


|  |
| --- |
| **Backlinks** |
| [Data Selector Editor](https://wiki.genexus.com/commwiki/wiki?5544) | [Category:Data Selector object](https://wiki.genexus.com/commwiki/wiki?5271) | [Table of contents:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) |

---
