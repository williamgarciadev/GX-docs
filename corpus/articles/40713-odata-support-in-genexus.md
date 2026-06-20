---
title: "OData Support in GeneXus"
source_id: 40713
source_url: https://wiki.genexus.com/commwiki/wiki?40713
genexus_version: "18"
---

# OData Support in GeneXus

OData Service is one of the possible data sources described in [External data sources](https://wiki.genexus.com/commwiki/wiki?53659,,).

Open Data Protocol (a.k.a OData) is a data access protocol designed to provide standard CRUD access to a data source via a website.

"Open Data Protocol (OData) is a standardized protocol for creating and consuming data APIs. OData builds on core protocols like HTTP and commonly accepted methodologies like REST. The result is a uniform way to expose full-featured data APIs."

Source: [Odata Home page.](https://www.odata.org/)

## [Technology used](#Technology+used)

The GeneXus implementation is based on version 4 of the protocol (OData Version Documentation), and even though services implemented in previous versions are supported, there is no guarantee that there won't be any problems.

### [How to Consume OData Services](#How+to+Consume+OData+Services)

See this feature with an example.

Suppose you want to integrate the OData TripPin model into your Knowledge Base.

**OData model of the example (TripPin)**

`[imagen omitida: wiki id 36123]`

It consists of 4 main entities:

1. Person
2. Airline
3. Airport
4. Photo

The other entities cannot be the "base entity" of a query; that is to say, for example, I cannot access a Trip directly, and I should do it through a Person instead.

The model is quite complete in that it uses a lot of OData v4 features, some of which are not directly mapped to the GeneXus model:

* There are fields of entities that are collections.
* There are entities of complex data types (a Person has a collection of AddressInfo where each AddressInfo is a complex type that has a City, for example).
* There are fields based on [Enumerated Domanins](https://wiki.genexus.com/commwiki/wiki?2207) (Gender), as well as [Subtypes](https://wiki.genexus.com/commwiki/wiki?20206) (Friends),[Geography data type](https://wiki.genexus.com/commwiki/wiki?32408) (Loc), Multimedia (Photo), [Formulas](https://wiki.genexus.com/commwiki/wiki?25327) (Concurrency).

## [Importing the model from GeneXus](#Importing+the+model+from+GeneXus)

To import the model, select **Tools > Application Integration > External Data Store Service Import**.

Since the import will create attributes with long names, increasing the value of Significant Attribute Name Length in the version's properties is convenient.

A screen like the following will be displayed:

`[imagen omitida: wiki id 36124]`

There, select "OData" as a Service Provider and a Data Store of Service type.

If one of them doesn't exist, you can create it right there using the New button.

Next, add:

* The service URL, in this case: https://services.odata.org/V4/(S(40gwjcqlhjmuyfayfnplov0o))/TripPinServiceRW/
* User and Password to access the service (in this case, it has no authentication).
* Extra connection information; in this case, filter\_strings=n to indicate that the service doesn't support conditions through >, <, >=, <= with the String data type.

When inspecting the service, a new dialog appears to choose which entities to import:

`[imagen omitida: wiki id 36126]`

By default, this dialog only shows transactions associated with main entities. In this case, the Import process will import all the additional transactions required to work with the selected main entities. If you want to specifically import part of the model, you can deselect "Show only top level" and manually select the transactions you want to import (not recommended).

## [SAP's OData Services](#SAP%27s+OData+Services)

SAP has widely adopted this protocol for exchanging data. Although it provides many pre-built services that can be consumed by GeneXus using this mechanism, you can also invoke Abap functions (or BAPIs) of SAP ERP, published as OData services in SAP NetWeaver Gateway.

To publish a BAPI as OData service, follow this [wizard](https://blogs.sap.com/2012/10/26/step-by-step-guide-to-build-an-odata-service-based-on-rfcs-part-1/).

SAP NetWeaver Gateway uses "cross-site request forgery" as [security method](https://laravel.com/docs/5.4/csrf). You need to send your username and password to SAP and it sends a token similar to 'X-CSRF-Token: qyFwSG-\_meLAJt-Ei7gOBA==' that you need to use in future POST/PUT/PATCH/DELETE operations. To have GeneXus do it automatically when importing the service, in the **Connection info** field (and/or in the property Additional connection string attributes of the Data store associated with the OData services), enter **SAP=true**.

In case you want to consume from SAP Business One instead of ERP you have to add **SapLogin=<sapLogin>**,rather than SAP=true, where <**sapLogin>** is the CompanyDB name (Temporary only available on for C#)

## [Restrictions](#Restrictions)

* OData allows exposing functions; for example, the TripPin model has a function that returns the nearest airport. This could be modeled as a method of an external object, but at the moment it is not implemented.
* Some things have to be worked on; for example, not all orders are valid in OData, or some orders are partial. The queries currently generated generally work, but sometimes the order is not taken into account.
* In [.NET](https://wiki.genexus.com/commwiki/wiki?38604), updates over the multimedia type do not work well.
* In [Java](https://wiki.genexus.com/commwiki/wiki?12258), it is only supported OData v4.
* The query object does not support OData (it only generates SQL queries at the moment, no OData queries). For this reason, the solution is to create a Data Provider that returns the data (since the Data Provider does support the generation of OData queries) and associate this DP to the Query Viewer (Property Data bindings / Object).

## [Availability](#Availability)

This feature is available since [GeneXus 16](https://wiki.genexus.com/commwiki/wiki?35351,,).


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus for SAP Systems](https://wiki.genexus.com/commwiki/wiki?33616) |
|

---
