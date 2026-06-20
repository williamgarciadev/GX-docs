---
title: "GeneXus ERP Connector - Installation Documentation"
source_id: 26015
source_url: https://wiki.genexus.com/commwiki/wiki?26015
genexus_version: "18"
---

# GeneXus ERP Connector - Installation Documentation

The GeneXus™ ERP Connector tool comes preinstalled with GeneXus™ from X Evolution 3 Upgrade 4 or higher and must be installed as an Extension for previous versions (GeneXus™ X Evolution 3 Upgrade 3).

**Prerequisite**

To execute GeneXus™ ERP Connector, you need [GeneXus™ X Evolution 3 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?27678,,)  (or higher) and [SAP Connector for Microsoft .NET](https://support.sap.com/en/product/connectors/msnet.html) installed. Even when it is not distributed with GeneXus™ or with GeneXus™ ERP Connector, everyone with an SAP license will have this connector.

Below are the necessary DLL files (3.0.13.0 or higher, 32 bits compiled with .NET Framework 2.0, from GX 15 U1 or up you need the dlls compiled with .NET Framework 4.0):  
sapnco.dll  
sapnco\_utils.dll

These two DLL files must be copied to the installation directory of GeneXus™ ERP Connector when the tool is used in standalone mode, or to the root installation directory of GeneXus™ when it is used as an extension.

To be able to call a BAPI using the RFC protocol, the SAP user should have at least the SAP\_S\_RFCACL role.

Pay attention also to the TCP/IP ports used by SAP applications, specifically to ports 36<NN>, 32<NN>, and 33<NN> where <NN> represents the SAP Instance Number.

**Installation process**

To install GeneXus™ ERP Connector, all you need is to download the extension GeneXus™ ERP Connector from [GeneXus™ Marketplace](https://marketplace.genexus.com/product.aspx?gxerpconnectorforsap,en) and execute it.

Step 1. Welcome to the wizard:

`[imagen omitida: wiki id 27878]`

Step 2. Select the GeneXus installation directory:

`[imagen omitida: wiki id 27879]`

Step 3. Click on Next to start the installation process:

`[imagen omitida: wiki id 27880]`

Step 4. The installation process begins:

`[imagen omitida: wiki id 27881]`

Step 5. GeneXus ERP Connector is installed, and you can choose to run GeneXus or finish the process.

`[imagen omitida: wiki id 27882]`

Once GeneXus ERP Connector for SAP is installed, you must request a license through [GeneXus License Manager](https://wiki.genexus.com/commwiki/wiki?19789,,).

You will find the product to authorize with the name "GX ERP Connector."

If you try to run, from inside GeneXus™, the option "Tools/Application Integration/SAP BAPI Import" without having a GeneXus ERP Connector license, the message "Enterprise Inspector License Not Found" will be displayed.

**Prototyping Cycle**

If you are using the C# generator, you will need to copy sapnco.dll and sapnco\_utils.dll files to the TargetEnvironment\web\bin\ folder.  
For the Java environment, make sure to add sapjco3.jar to the classpath; next, follow the [Connector instructions](https://wiki.genexus.com/commwiki/wiki?28182) for further detail.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus ERP Connector](https://wiki.genexus.com/commwiki/wiki?26013) | [GeneXus for SAP Systems - Hardware and Software Requirements](https://wiki.genexus.com/commwiki/wiki?33981) |

---
