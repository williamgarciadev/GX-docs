---
title: "GeneXus ERP Connector - Invoking a BAPI through RFC"
source_id: 27311
source_url: https://wiki.genexus.com/commwiki/wiki?27311
genexus_version: "18"
---

# GeneXus ERP Connector - Invoking a BAPI through RFC

To invoke a BAPI through [RFC (Remote Function Call)](https://wiki.genexus.com/commwiki/wiki?26017,,), first import it into the GeneXus KB from [GeneXus ERP Connector](https://wiki.genexus.com/commwiki/wiki?26013).

Next, select the BAPI(s) you want to import and press the Import button.

This will generate an [External Object](https://wiki.genexus.com/commwiki/wiki?5669) in the KB with the BAPI’s name and all its methods.

`[imagen omitida: wiki id 26088]`

Then, from any GeneXus object, you may invoke with <EO>.<method>(<parms>) or <EODataTypeVariable>.<method>(<parms>)

`[imagen omitida: wiki id 26089]`

Upon generating this object, GeneXus will create an RFC call to invoke the BAPI. At runtime, the RFC call uses [SAP Connector](https://service.sap.com/connectors) ([SAP .Net Connector](https://websmp101.sap-ag.de/form/handler?_APP=00200682500000002672&_EVENT=DISPLAY&_SCENARIO=01100035870000000122&_HIER_KEY=501100035870000018527&_HIER_KEY=601100035870000225415&) or [SAP Java Connector](https://websmp101.sap-ag.de/form/handler?_APP=00200682500000002672&_EVENT=DISPLAY&_SCENARIO=&_HIER_KEY=501100035870000018527&_HIER_KEY=601100035870000225414&) depending on the GeneXus generator used), so it is a prerequisite to have it installed and distribute the corresponding DLL with the application.

SAP .Net connector and SAP Java connector are free of charge for SAP Customers and SAP Partners.

[ERP Connector - Generating the application with GeneXus .NET generator](https://wiki.genexus.com/commwiki/wiki?28181)

[ERP Connector - Generating the application with GeneXus Java generator](https://wiki.genexus.com/commwiki/wiki?28182)

**Note**: RFC calls to the BAPI are only supported in .NET and Java generators. Android and iOS Devices cannot invoke the BAPI directly; they need to call server-side components (generated in .NET or Java) that interact with the BAPI.

Before invoking a BAPI via RFC from a GeneXus object, the application must be connected to the SAP server where the BAPI will be invoked.

To do so, see:

[Using the External Object GXEnterpriseSessionManager](https://wiki.genexus.com/commwiki/wiki?27423)

## [Types of methods](#Types+of+methods)

Each BAPI has two types of methods: an instance method, and a class method. You will notice the class method in the GX ERP connector marked with a red circle in its icon.

`[imagen omitida: wiki id 27567]`  
Instance Method

`[imagen omitida: wiki id 27566]`  
Class Method

When you use a class method in a GeneXus Object, you use the External Object directly in the code by writing <EOName>.<ClassMethodName>(<parms>).

```
Material.GETLIST(&BAPIMATRAW, &BAPIMATRADC, &BAPIMATRASO, &BAPIMATRAL, &BAPIMATRAM, &BAPIMATRAS, &BAPIMATMFRPN, &BAPIF4A, 
&BAPIMATLST, &BAPIRET2)
```

But when you use an instance method, you must define a variable of the External Object data type. In the GeneXus Object, you must select a value for the SAP Object Key (this means to instantiate the object) and invoke the method from the variable <EODataTypeVariable>.<InstanceMethod>(<parms>).

```
&Material.Material = '000000000000000001' // Material number instantiation for GetDetail
&Material.GETDETAIL(&Plant, &ValuationArea, &ValuationType, &BAPIMGVMATNR, &BAPIMATDOBEW, &BAPIMATDOC, &BAPIMATDOA, 
&BAPIRETURN)
```

## [Using Zfunctions](#Using+Zfunctions)

In addition to standard BAPI, there are other standard or user-developed RFC functions (the latter are known as Zfunctions).

All those functions can be used with GeneXus ERP Connector, but to be seen by GeneXus ERP Connector, they must be published in the BOR (Business Object Repository). This is done in SAP ERP using  [these steps](http://wiki.scn.sap.com/wiki/display/ABAP/A+step+by+step+guide+for+beginners+on+user+defined+BAPI+creation) (in particular, from Stage 3).


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus ERP Connector](https://wiki.genexus.com/commwiki/wiki?26013) | [GeneXus ERP Connector - End User Documentation](https://wiki.genexus.com/commwiki/wiki?26016) | [Is Factory property](https://wiki.genexus.com/commwiki/wiki?41717) |

---
