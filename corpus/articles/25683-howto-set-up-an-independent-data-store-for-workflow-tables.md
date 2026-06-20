---
title: "HowTo: Set up an independent Data Store for Workflow tables"
source_id: 25683
source_url: https://wiki.genexus.com/commwiki/wiki?25683
genexus_version: "18"
---

# HowTo: Set up an independent Data Store for Workflow tables

The purpose of this article is to explain the necessary steps to create and use an independent Data Store for Workflow tables

### [Step 1 - Create a secondary Data Store](#Step+1+-+Create+a+secondary+Data+Store)

The first step is to create a secondary [Data Store](https://wiki.genexus.com/commwiki/wiki?7117); to do so:

**1.** Open the [Preferences](https://wiki.genexus.com/commwiki/wiki?7109) tab.  
**2.** Right-click on the "DataStore" node.  
**3.** Select the "New Data Store" option and the [DBMS](https://wiki.genexus.com/commwiki/wiki?9518,,) you want to configure.

`[imagen omitida: wiki id 25686]`

### [Step 2 - Name the Secondary Data Store](#Step+2+-+Name+the+Secondary+Data+Store)

Name the newly created secondary Data Store as: "GXFLOW"

`[imagen omitida: wiki id 25685]`

The result should be as follows:

`[imagen omitida: wiki id 25684]`

It is important to rename the newly created Data Store to 'GXFLOW'; otherwise, GeneXus will not use it for hosting workflow tables and the default Data Store will be used as usual. In other words, this feature does not have any effect when the 'GXFLOW' DataStore is not defined.

### [Step 3 - Configure GXFLOW](#Step+3+-+Configure+GXFLOW)

Once the 'GXFLOW' Data Store is created, the [Database name property](https://wiki.genexus.com/commwiki/wiki?9080) and [Server Name Property](https://wiki.genexus.com/commwiki/wiki?9117) can be changed. It is possible to change the [User ID Property](https://wiki.genexus.com/commwiki/wiki?9039,,) and [User Password Property](https://wiki.genexus.com/commwiki/wiki?9040,,) also.

### [Step 4 - Done](#Step+4+-+Done)

Press F5 to run your application.

### [Changing the Schema Name Property (Optional)](#Changing+the+Schema+Name+Property+%28Optional%29)

If the secondary Data Store "GXFLOW" is defined, it is also possible to change the value of the [Schema Name Property](https://wiki.genexus.com/commwiki/wiki?9471,,) of the Workflow tables—for those DBMSs supporting Schemas.

It is important to distinguish two different scenarios:

#### [Scenario 1 - Using same database but assigning a schema for Workflow tables](#Scenario+1+-+Using+same+database+but+assigning+a+schema+for+Workflow+tables)

It is possible to use the same database as the application tables but using a schema only for Workflow tables—or different from the schema used for the application tables.  
To do so:

* Create the "GXFLOW" secondary Data Store as explained above.
* Do not change any of "GXFLOW" secondary Data Store properties from the default values.
* Set the [Schema Name Property](https://wiki.genexus.com/commwiki/wiki?9471,,) for the "GXFLOW" Data Store to the desired value.

**Note**: The [Schema Name Property](https://wiki.genexus.com/commwiki/wiki?9471,,) of the default DataStore will only impact the application tables and not the Workflow Tables.

#### Scenario 2 - Using a different database and assigning a schema

It is possible to use a different database and also use a schema for the Workflow tables; to do so:

* Create "GXFLOW" secondary Data Store as explained above.
* Change the [Database name property](https://wiki.genexus.com/commwiki/wiki?9080) and [Server Name Property](https://wiki.genexus.com/commwiki/wiki?9117) to the desired values.
* Set the [Schema Name Property](https://wiki.genexus.com/commwiki/wiki?9471,,) for the "GXFLOW" Data Store to the desired value.

### Availability

Since [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?20247,,).

### [See Also](#See+Also)

[GXflow Support for Independent Data Store](https://wiki.genexus.com/commwiki/wiki?25207,,)  
[My first BPM Application](https://wiki.genexus.com/commwiki/wiki?11218)
