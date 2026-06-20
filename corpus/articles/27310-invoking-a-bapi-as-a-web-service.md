---
title: "Invoking a BAPI as a Web Service"
source_id: 27310
source_url: https://wiki.genexus.com/commwiki/wiki?27310
genexus_version: "18"
---

# Invoking a BAPI as a Web Service

To invoke a BAPI as a [Web Service](https://wiki.genexus.com/commwiki/wiki?1919,,) using the SOAP protocol, once the BAPI is available as a WS in SAP you need to locate the associated WSDL interface. Next, import the BAPI into a GeneXus KB as an [External Object](https://wiki.genexus.com/commwiki/wiki?5669) using the [WSDL Import](https://wiki.genexus.com/commwiki/wiki?6181) utility.

Also, this external object may be used from any GeneXus object. To do so, we define a variable with the EO data type, and invoke any method of the BAPI with a <EODataTypeVariable>.<method>([parms]).

Upon generating this object, GeneXus will create a SOAP call to invoke the BAPI.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus ERP Connector](https://wiki.genexus.com/commwiki/wiki?26013) | [GeneXus ERP Connector - End User Documentation](https://wiki.genexus.com/commwiki/wiki?26016) |

---
