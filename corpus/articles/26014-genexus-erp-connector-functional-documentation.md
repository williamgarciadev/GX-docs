---
title: "GeneXus ERP Connector - Functional Documentation"
source_id: 26014
source_url: https://wiki.genexus.com/commwiki/wiki?26014
genexus_version: "18"
---

# GeneXus ERP Connector - Functional Documentation

The SAP BAPI Import feature (technically known as GeneXus™ ERP Connector) is executed from within GeneXus™ IDE.

`[imagen omitida: wiki id 53584]`

Applications developed with GeneXus integrate with SAP, interacting with its Business Objects through the BAPIs defined and maintained in the SAP Business Objects Repository (BOR).

Through SAP BAPI Import, GeneXus,  among other things, reads the Meta Data of the BAPIs using its [RFC (Remote Function Call)](https://wiki.genexus.com/commwiki/wiki?26017,,) interface, known as BOR-API.

`[imagen omitida: wiki id 26018]`

RFC calls are made using the SAP Connector ([SAP Connector for Microsoft .NET](https://support.sap.com/en/product/connectors/msnet.html)).

After you enter the corresponding credentials, SAP BAPI Import connects to a SAP server an inspection of all its BAPIs.

This BAPI “inspector” is a “browser” of objects, which, by accessing the BAPIs catalog (the BOR of the SAP installation to which it is connected), is capable of showing the hierarchy of SAP components and the types of Business Objects in a “tree” structure.

Not only does SAP BAPI Import show us that structure, but it also shows, for each BAPI corresponding to a BO, its methods, parameters and all related information. It allows to select  any methods of a BAPI to test its execution directly within the tool and also "import" them into the GeneXus™ KB, creating External Objects of the BAPI with all its methods (when executed from within GeneXus™), or generating an xpz with that External Object when the tool is executed in stand-alone manner).

When this EO is used in a GeneXus™ object, and the application is generated and executed, an RFC call to the corresponding BAPI is made.

The interface of SAP BAPI Import is similar to that of the SAP BAPIs Browser, accessed in an installation of SAP R/3 through "SAP Menu/Tools/Business Framework/BAPI Explorer", with this appearance:

`[imagen omitida: wiki id 26019]`

Upon selecting a BO, it shows the BAPI’s different methods:

`[imagen omitida: wiki id 26020]`

And for each element in the "i" button, in blue, it shows its Help:

`[imagen omitida: wiki id 26021]`

* To access the BOR Program Interface and show the information in tree or list format, GeneXus™ ERP Connector uses the following function modules:
  + SWO\_QUERY\_OBJTYPES
  + SWO\_QUERY\_API\_OBJTYPES
  + RPY\_BOR\_TREE\_INIT
  + RPY\_BOR\_TREE\_EXPAND
  + SWO\_QUERY\_OBJTYPE\_INFO
  + SWO\_QUERY\_OBJTYPE\_
  + SWO\_QUERY\_OBJTYPE\_DOCU
  + SWO\_QUERY\_BASEDATA
  + SWO\_QUERY\_KEYFIELDS
  + SWO\_QUERY\_ATTRIBUTES
  + SWO\_QUERY\_METHODS
  + SWO\_QUERY\_EVENTS
  + SWO\_QUERY\_PARAMETERS
  + SWO\_QUERY\_RETURNCODES
  + DDIF\_FIELDINFO\_GET
* For processing the SAP Business Objects it uses the following function modules of the BOR Runtime Environment:
  + SWO\_TYPE\_INFO\_GET
  + SWO\_CREATE
  + SWO\_INVOKE
  + SWO\_FREE
  + SWO\_OBJECT\_ID\_GET
  + SWO\_OBJECT\_ID\_SET
  + SWO\_SET\_ENVIRONMENT
* And lastly, in addition to the BOR-API mentioned above, it uses the RFMs (Remote Function Modules) present in the RFC1 Group of Functions:
  + RFC\_FUNCTION\_DOCU\_GET
  + RFC\_FUNCTION\_SEARCH
  + RFC\_GROUP\_DOCU\_GET
  + RFC\_GROUP\_SEARCH


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus ERP Connector](https://wiki.genexus.com/commwiki/wiki?26013) |

---
