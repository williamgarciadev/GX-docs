---
title: "Mapping relevant data"
source_id: 25149
source_url: https://wiki.genexus.com/commwiki/wiki?25149
genexus_version: "18"
---

# Mapping relevant data

GeneXus performs an automatic mapping of attributes or variables, upon the GeneXus object associated with a business process diagram symbol.

For example, by associating a Transaction with an interactive task, GeneXus automatically creates relevant data with the same name as the Transaction’s identifier attribute.

`[imagen omitida: wiki id 25145]`

This relevant data will have the same name and type as the Transaction’s primary key. 

If the primary key includes more than one attribute, then relevant data will be created for each attribute that is part of the primary key.

In the Relevant Data tab of the [Business Process Diagram object](https://wiki.genexus.com/commwiki/wiki?16486), you can see the relevant data defined.

`[imagen omitida: wiki id 11747]`

This data appears under the ampersand symbol to indicate that it consists of variables.

When you refer to the relevant data ReservationId you always have to do it by using the ampersand symbol as a prefix in order to set it apart from the ReservationId attribute, as well as in the case of variables in GeneXus objects.

### [Automatic management of relevant Data in Transactions](#Automatic+management+of+relevant+Data+in+Transactions)

When Transactions receive the primary key in the Transaction by parameter, directly in the attribute or in variables based on the primary key, there is also an automatic mapping with the relevant data. It is required that the variables must have the same name as the primary key attributes.  

For example, if you drag a Transaction object to the diagram, one thing you have to bear in mind is whether it has a [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862) defined where the value of the primary key is received in a variable.

The dragging of the Transaction to the diagram creates the relevant data, but if the names of variables in the Parm rule match those of the attributes in the primary key, there will be a mapping between the relevant data and the variables, so that **when the Transaction is executed, the variables take the values stored in the relevant data at the time.**

The mapping is at the input, and at the ouput of the object execution. This means:

* When the task associated with the Transaction object is executed, the value stored in the relevant data will be copied to the variable in the Parm rule of the Transaction. When the Transaction is executed, the primary key will be instantiated with that value.
* When the Transaction finishes its execution and the flow returns to the diagram, if the value was modified during the Transaction execution, the value will be updated into its corresponding relevant data.

`[imagen omitida: wiki id 25144]`

### [Automatic management of relevant Data in Web Panels](#Automatic+management+of+relevant+Data+in+Web+Panels)

In the case of association of a task with [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916), if the Web Panel has a Parm rule and the variables or attributes in Parm rule have the same name as the diagram relevant data, there will be an automatic mapping of relevant data.

In the case of variables, the values of variables are assigned automatically.

This mapping is just for values at the entry point of the Web Panel. Values are not updated at the end of Web Panel's execution when the flow is turning back to the diagram.

If the variable values changed, the relevant data update should be done manually using the [Workflow API](https://wiki.genexus.com/commwiki/wiki?17240) methods, like in the following example:

`[imagen omitida: wiki id 25225]`

### [Automatic management of relevant Data in Procedures](#Automatic+management+of+relevant+Data+in+Procedures)

In the case of association of a task with [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293), If variables or attributes in Parm rule match the mapping of relevant data, the values of variables are automatically assigned.

The mapping is both at the entry point of the Procedure and at the end of Procedure execution. This implies that when a Procedure is called, the value stored in the relevant data will be copied to the variable in the Parm rule. And when the flow returns to the diagram, if the value was modified in the Procedure execution, the value will be updated into the corresponding relevant data.

`[imagen omitida: wiki id 25234]`


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |

---
