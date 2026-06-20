---
title: "ERP Connector - Generating the application with GeneXus Java generator"
source_id: 28182
source_url: https://wiki.genexus.com/commwiki/wiki?28182
genexus_version: "18"
---

# ERP Connector - Generating the application with GeneXus Java generator

To generate and run your application using GeneXus Java generator, you need the [SAP Java connector](https://support.sap.com/en/product/connectors/jco.html) (free of charge for SAP Customers and SAP Partners).  
Once you have installed the SAP Java connector (for example, in C:\Program Files (x86)\SAP\SAPJCo) you must copy the sapjco3.jar from the instalation directory to the webapp lib directory (C:\Program Files (x86)\SAP\SAPJCo\sapjco3.jar).

If you are using Tomcat over Windows:

The generated application will also use the C:\Program Files (x86)\SAP\SAPJCo\sapjco3.dll, so you must add this path to the path system variable.

To do that, choose Control pannel\System\Advanced system settings\Environment variables\System variables and add C:\Program Files (x86)\SAP\SAPJCo to the Path variable.

If you are using Tomcat over Linux:

The generated application will also use the libsapjco3.so file (from SAPJCo), so you must copy to the webapp lib directory.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus ERP Connector](https://wiki.genexus.com/commwiki/wiki?26013) | [GeneXus ERP Connector - Installation Documentation](https://wiki.genexus.com/commwiki/wiki?26015) | [GeneXus ERP Connector - Invoking a BAPI through RFC](https://wiki.genexus.com/commwiki/wiki?27311) |

---
