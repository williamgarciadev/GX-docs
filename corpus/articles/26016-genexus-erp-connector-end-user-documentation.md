---
title: "GeneXus ERP Connector - End User Documentation"
source_id: 26016
source_url: https://wiki.genexus.com/commwiki/wiki?26016
genexus_version: "18"
---

# GeneXus ERP Connector - End User Documentation

This is the documentation for GeneXus developers; that is, the End Users of the GeneXus ERP Connector.

If GeneXus ERP Connector is installed, it can be accessed from the GeneXus IDE through the option Tools/Application Integration/SAP BAPI Import.

`[imagen omitida: wiki id 27741]`

Upon opening it, the login screen will be displayed for you to enter the credentials of the SAP system to which you will be connected.

`[imagen omitida: wiki id 27799]`

|  |  |
| --- | --- |
| Connection Name | Name that the connection will receive |
| Application Server | Name of SAP application server to which you will be connecting |
| Instance Number | Number of instance within the server |
| System ID | Identifier of the SAP system to be connected |
| Client Number | Number of SAP client |
| Router String | IP of SAP server |
| Use SAPGUI | When this option is selected, once the connection is established an SAP GUI is also loaded to enable the execution of any BAPI method later on. The result is shown on the SAP GUI. |
| Language | Language to be used in the connection. [Posible values list](http://goo.gl/QpmFZc). |
| User Name | SAP user to be used in the connection |
| Password | User's password |

The Test Connection option checks if a successful connection is achieved with the data entered.

If you get “Connection Test OK,” you may continue by pressing the OK button. This will take you to the GX ERP C Main screen, where all the BAPIs are shown in a tree structure organized by the SAP module. Upon selecting the primary key of any BAPI, all its events and methods will be displayed.

Upon selecting a method, you will see three tabs on the right side of your screen:

Info (Method): showing the method’s basic information

Detail: showing all the BAPI method parameters, indicating the type and whether they are input or output parameters. The possible return codes are also shown.

Documentation: this tab shows all documents in the BAPI’s method.

`[imagen omitida: wiki id 27800]`

Pressing the Test Runtime button allows testing the execution of the BAPI/Method selected directly from the tool. The call is made as an [RFC](http://wiki.genexus.com/commwiki/servlet/hwiki?SAP+Remote+Function+Call,) call form.

When you press the button, a screen will be displayed with the input/output parameters of the BAPI’s method. The input parameters may be completed at this point, before making the invocation.

`[imagen omitida: wiki id 27801]`

As shown in the image above, upon selecting the BAPI Material.GetList, the screen with parameters is displayed. You may, for example, by clicking on the Value column of the PlantSelection input parameter, complete the structure with values to restrict the result of the list of materials.

Then, when you press the Execute button, the structures corresponding to the output parameters are returned. In this case, the list of materials (MatnrList) and structure with a list of possible errors that might occur in the call (Return).

`[imagen omitida: wiki id 27802]`

Upon clicking on the Value (Table) column of the corresponding output parameter, you will view the values returned. In this example, the structure with a list of materials MatnrList.

`[imagen omitida: wiki id 27803]`

At this point, the BAPIs to be used to make the KB under development interact with SAP are analyzed and selected. To do so, you have two options: invoke them in a native manner through RFC calls, or invoke them as WebServices.

|  |
| --- |
|  |

[GeneXus ERP Connector - Invoking a BAPI through RFC](https://wiki.genexus.com/commwiki/wiki?27311)

[Invoking a BAPI as a Web Service](https://wiki.genexus.com/commwiki/wiki?27310)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus ERP Connector](https://wiki.genexus.com/commwiki/wiki?26013) |

---
