---
title: "ERP Connector - Generating the application with GeneXus .NET generator"
source_id: 28181
source_url: https://wiki.genexus.com/commwiki/wiki?28181
genexus_version: "18"
---

# ERP Connector - Generating the application with GeneXus .NET generator

To generate and run your application using GeneXus .Net Framework generator, you need the [SAP Connector for Microsoft .NET](https://support.sap.com/en/product/connectors/msnet.html) DLL (free of charge for SAP Customers and SAP Partners).  
Even though to use the GeneXus ERP connector in the GeneXus IDE you must use the 32-bit version of the DLL, in the generated application you can use the 32-bit DLL or the 64-bit DLL.

From SAP Connector for Microsoft .NET (3.0.13.0 or higher, 32/64 bits), you must copy the sapnco.dll and sapnco\_utils.dll to the bin directory of your application.

When using the 32-bit SAP Connector for Microsoft .NET DLL, you must set the "Enable 32 bits applications" property to true for the Application pool used by your Web Application in the IIS.

[Temporal limitation](https://wiki.genexus.com/commwiki/wiki?39853): not supported at the moment in .Net generator (ex .Net core)


|  |
| --- |
| **Backlinks** |
| [Deploy to GeneXus Prototyping Cloud - FAQ](https://wiki.genexus.com/commwiki/wiki?18292) | [Toc:GeneXus ERP Connector](https://wiki.genexus.com/commwiki/wiki?26013) | [GeneXus ERP Connector - Invoking a BAPI through RFC](https://wiki.genexus.com/commwiki/wiki?27311) |

---
