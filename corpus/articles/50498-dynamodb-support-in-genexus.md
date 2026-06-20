---
title: "DynamoDB Support in GeneXus"
source_id: 50498
source_url: https://wiki.genexus.com/commwiki/wiki?50498
genexus_version: "18"
---

# DynamoDB Support in GeneXus

GeneXus makes it possible to consume [DynamoDB](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?50601,,)  Databases mainly because of their advantages in terms of scalability. They allow you to scale data reading and writing almost infinitely, without worrying about maintenance of the associated hardware. In addition, you pay for exactly what you use.

This is particularly true in scenarios where the ACID (atomicity, consistency, isolation, durability) properties of relational DBMSs are not required and data consistency is not the most important factor at the time of data insertion.

To use GeneXus with a [NoSQL](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?50507,,) DynamoDB external Database, follow the steps below.

**Note**: As of GeneXus 18, multimedia (Image/Audio/Video) fields are no supported. Blobs are supported, but are not recommended due to DynamoDB binary fields limitation (400KB).

Given a DynamoDB Database:

**1.** In the GeneXus main menu, select **Tools > Application Integration > External Data Store Service Import**.

The dialog shown in the image will be displayed:

`[imagen omitida: wiki id 50501]`

In the Service Provider combo box, select DynamoDB. The Name and Description fields will be automatically filled in.

In the Data Store combo box, select one of those defined in your KB of the service type. If it doesn't exist, you can create it right there using the New button.

Leave the Service URI field empty.

In User and Password, add the **Access Key ID** and **Secret Access Key** provided by Amazon.

Lastly, in Connection Info you can add the following depending on the case:

**A.** If you are working locally, you need to indicate the URL for the local DynamoDB test service. For example :

localurl=http://localhost:8000

**Note**: If you are working locally with NoSQL Workbench and the [.NET Generator](https://wiki.genexus.com/commwiki/wiki?38604), in addition to the service URL, you must add the region (localhost) to which you are going to connect, as shown below:

localurl=http://localhost:8000;region=localhost

**B.** If you are working in the cloud, you can indicate the [region](https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints) to which you are going to connect. For example:

region=us-east-1

Also, you can control how many records to read from each Table to get the schema (the default is 15). For example:

importitems=5

The next step is to click on Inspect. GeneXus will connect to the DynamoDB Database and get the metadata and items from the existing **Tables**.

**2.** The following dialog box will be displayed, showing the Tables that can be imported. Select the Tables you need:

The Import process, in addition to importing the selected Tables, will import all the secondary indexes, because they are the ones that allow you to perform ordered queries.

For each selected Table, GeneXus will create a Transaction. In addition, it will generate the associated Data Views:

`[imagen omitida: wiki id 50502]`

The import process also performs a query on the Table to read the first 15 items. Since DynamoDB is a NoSQL Database, there can be items with different attributes; therefore, GeneXus gets all the attributes included in other items of the Table.

When an attribute doesn't have stored data, it is not imported and you have to add it manually in the Transaction and Data View.

At the moment, only scalar data types are supported, and from these the most appropriate GeneXus data type will be tried to be inferred. For example, the String type can be mapped to Character, VarChar or DateTime depending on the context.

When importing non-scalar data, GeneXus generates a [warning](https://wiki.genexus.com/commwiki/wiki?47288) and they are set as [VarChar](https://wiki.genexus.com/commwiki/wiki?6778). Then, at runtime, the reads return the associated Json as a String.

This import process allows you to work with [Transactions](https://wiki.genexus.com/commwiki/wiki?1908), [Business Component](https://wiki.genexus.com/commwiki/wiki?5846), [For Each commands](https://wiki.genexus.com/commwiki/wiki?24744), and [Data Selectors](https://wiki.genexus.com/commwiki/wiki?5271) accessing the DynamoDB Database.

### [Considerations](#Considerations+)

The data store can be created manually using the Service Provider from Preferences. To do this, right-click on DataStore and then select Service from the drop-down menu that appears:

`[imagen omitida: wiki id 53450]`

This will generate a pop-up window where you can enter the name. Also be sure to select Services as the Data Sote. Once this is set, click "OK".

Finally, you must fill in the connection information:

Server name: leave empty  
User id: Access Key  
User password: Secret Access Key  
Datastore Provider: DynamoDB  
Additional conecction string attributes: Connection information, similar to that explained above. That is, you may also enter the region here. If you do not set the region, it defaults to us-east-1.

For example, in the image below you can see that the connection is made locally with NoSQL Workbench and the .NET Generator:

`[imagen omitida: wiki id 53452]`

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [See Also](#See+Also)

[Navigation restrictions](https://wiki.genexus.com/commwiki/wiki?50640)  
[Simple example with DynamoDB](https://wiki.genexus.com/commwiki/wiki?50607)  
[With AWS, Uruguay implements vaccination scheduling system in record time (in Spanish)](https://aws.amazon.com/es/solutions/case-studies/agesic-msp/)  
[FestivalTickets - High Scalability Sample](https://wiki.genexus.com/commwiki/wiki?51266)

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Amazon Web Services and GeneXus: The Key to Building Mission-Critical Systems](https://www.youtube.com/watch?v=tzxNo3FEay4)  
`[imagen omitida: wiki id 20668]` [Next-Gen Trends: NOSQL and Serverless Apps in the Cloud](https://www.youtube.com/watch?v=oQPamb78bG8)  
`[imagen omitida: wiki id 20668]` [Creating Mission-Critical Applications](https://www.youtube.com/watch?v=i_bbyFG9hI4&t=30s)  
`[imagen omitida: wiki id 20668]` [Modern and Scalable Applications in the Cloud with GeneXus 18](https://www.genexus.com/en/products/genexus/live-2022/mission-critical-highly-scalable-systems/modern-and-scalable-applications-in-the-cloud-with-genexus-18)


|  |
| --- |
| **Backlinks** |
| [Table of contents:DynamoDB](https://wiki.genexus.com/commwiki/wiki?50659) |
| [Simple example with DynamoDB](https://wiki.genexus.com/commwiki/wiki?50607) |

---
