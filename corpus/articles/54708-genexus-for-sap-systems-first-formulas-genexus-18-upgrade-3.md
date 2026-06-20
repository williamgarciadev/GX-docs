---
title: "GeneXus for SAP Systems First Formulas (GeneXus 18 Upgrade 3 or prior)"
source_id: 54708
source_url: https://wiki.genexus.com/commwiki/wiki?54708
genexus_version: "18"
---

# GeneXus for SAP Systems First Formulas (GeneXus 18 Upgrade 3 or prior)

### [What are formulas?](#What+are+formulas%3F)

Applications are often required to make calculations that involve the values of specific attributes, constants and/or functions. For all these cases, GeneXus offers Formulas.

There are different possible ways to define formulas.

`[imagen omitida: wiki id 34252]`

`[imagen omitida: wiki id 34253]`

GLOBALLY: the calculation will be available throughout the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836).

LOCALLY or INLINE: in this case, the calculation will be available only for the object in which it has been defined.

Start by learning what a Global Formula is. A global formula is a calculation that you define in association with an attribute. Note that the [Transaction](https://wiki.genexus.com/commwiki/wiki?1908) structures contain a column labeled Formula:

`[imagen omitida: wiki id 34254]`

When a calculation is defined in this column for an attribute, this means that the attribute is virtual. In other words, it will not be created physically as a field in a table because the value of the attribute will be obtained every time it is needed by doing the calculation.

See this with an example:

Suppose the Travel Agency needs to know how many registered attractions there are of each category at all times.  So, define a new attribute in the Category Transaction with the purpose of defining it as a global formula:

`[imagen omitida: wiki id 34255]`

Now define the calculation associated to the CategoryAttractions attribute.   
GeneXus offers a formula called Count to calculate what the Travel Agency needs (there are many others, like Sum, Average, etc.).

`[imagen omitida: wiki id 34256]`

The attribute referenced inside the parenthesis of the formula provides GeneXus with the information of the table to be navigated to do the calculation (in the definition above, GeneXus knows that it has to count in the Attraction table).

Then, if GeneXus detects a relation between the table it will navigate (Attraction) and the context where the formula attribute is defined (Category), it will only consider the related records for the calculation. In this example, CateogryId is present in both contexts: where the formula is defined and in the table to be navigated for doing the calculation of the formula. So, only attractions of each category are counted and not all attractions recorded in the navigated table will be considered. If no relation is found, then GeneXus will do the calculation considering all records in the navigated table.

Press Build All. You can see that no physical changes will be made to the database. GeneXus will only generate some programs.

Execute the Category Transaction in order to see for each category how the attraction's quantity is always calculated at the time:

`[imagen omitida: wiki id 53121]`

Every attribute defined as a global formula will be read-only, and it will not be possible to enter a value for it. This happens because the attribute obtains its value from the associated calculation, which is run every time the attribute is used.

For this reason, there isn't a field in the physical table to store this attribute value, hence there's no need for it to be editable.

You can add more attractions in order to verify how the attraction's quantity is always calculated for each category at the time.
