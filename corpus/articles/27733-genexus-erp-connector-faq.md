---
title: "GeneXus ERP Connector - FAQ"
source_id: 27733
source_url: https://wiki.genexus.com/commwiki/wiki?27733
genexus_version: "18"
---

# GeneXus ERP Connector - FAQ

Below you can find frequently asked questions (FAQ) about [ERP Connector](https://wiki.genexus.com/commwiki/wiki?26013).

#### [**1. What is** **an RFM?**](#1.+What+is+an+RFM%3F)

An RFM (RFC-enabled Function Module) is an ABAP function module that can be remotely invoked. An RFM takes some parameters as input, and after execution, returns some output parameters. You can view an RFM in the SAP system via Transaction SE37.

#### [**2. Can I integrate** **an RFM** **with GeneXus ERP Connector (for example, ZBAPI or ZRFM)?**](#2.+Can+I+integrate+an+RFM+with+GeneXus+ERP+Connector+%28for+example%2C+ZBAPI+or+ZRFM%29%3F)

Yes, you can.

To be seen by GeneXus [ERP Connector](https://wiki.genexus.com/commwiki/wiki?26013), these functions must be published in the BOR (Business Object Repository). This is done in SAP ERP using the [following steps](https://wiki.scn.sap.com/wiki/display/ABAP/A+step+by+step+guide+for+beginners+on+user+defined+BAPI+creation) (in particular from Stage 3)

#### [**3. Where can I download SAP .Net Connector or SAP Java Connector from?**](#3.+Where+can+I+download+SAP+.Net+Connector+or+SAP+Java+Connector+from%3F)

You can download them from <http://service.sap.com/connectors>.

#### [**4. Which role should I grant to a SAP user to make RFC calls in a SAP System?**](#4.+Which+role+should+I+grant+to+a+SAP+user+to+make+RFC+calls+in+a+SAP+System%3F)

The SAP user needs the role sap\_s\_rfcacl in order to make RFC calls.

**5. When I select Tools > Application Integration > SAP BAPI Import, I get the following error message: "*Could not load file or assembly ‘sapnco, version=3.0.0.42, Culture=neutral, PublicKeyToken=50436dca5c7f7d23’ or one of its dependencies. The system cannot find the file specified (EnterpriseInspector)."***

You must copy the sapnco.dll and sapnco\_utils.dll (part of SAP .Net Connector 3.0.13.0 or higher, 32 bits compiled with .NET Framework 2.0, or compiled with Framework 4.0 if you are using GeneXus 15 Upgrade 1 or higher) to the root of GeneXus installation directory. You can download it from <http://service.sap.com/connectors>. 

#### [**6. When I select Tools > Application Integration > SAP BAPI Import, I get the following error message: "*The type initializer for ‘SAP.Middleware.Connector.RfcDestinationManager’ threw an exception. (sapnco)"***](#6.+When+I+select+Tools+%26gt%3B+Application+Integration+%26gt%3B+SAP+BAPI+Import%2C+I+get+the+following+error+message%3A+%22The+type+initializer+for+%E2%80%98SAP.Middleware.Connector.RfcDestinationManager%E2%80%99+threw+an+exception.+%28sapnco%29%22)

Additional Information:

*Could not load file or assembly ‘sapnco\_utils, version=3.0.0.42, Culture=neutral, PublicKeyToken=50436dca5c7f7d23’ or one of its dependencies. The system cannot find the file specified (EnterpriseInspector).*

You must copy the sapnco\_utils.dll (part of SAP .Net Connector 3.0.13.0 or higher, 32 bits compiled with .NET Framework 2.0, or compiled with Framework 4.0 if you are using GeneXus 15 Upgrade 1 or higher) to the root of GeneXus installation directory. You can download it from <http://service.sap.com/connectors>.

#### [**7. When I select Tools > Application Integration > SAP BAPI Import from GeneXus 15 Upgrade 1 or higher, I get the following error message: "*The type initializer for 'SAP.Middleware.Connector.RfcDestinationManager' threw an exception. (sapnco)"***](#7.+When+I+select+Tools+%26gt%3B+Application+Integration+%26gt%3B+SAP+BAPI+Import+from+GeneXus+15+Upgrade+1+or+higher%2C+I+get+the+following+error+message%3A+%22The+type+initializer+for+%27SAP.Middleware.Connector.RfcDestinationManager%27+threw+an+exception.+%28sapnco%29%22)

From GeneXus 15 Upgrade 1 or higher, you need the SAP .Net Connector compiled with Framework 4.0  
You must copy the sapnco.dll and sapnco\_utils.dll (part of SAP .Net Connector compiled with .NET Framework 4.0) to the root of GeneXus installation directory. You can download it from http://service.sap.com/connectors.

```
Detailed Error Message:
The type initializer for 'SAP.Middleware.Connector.RfcDestinationManager' threw an exception. (sapnco)
------------------------------
Product = GeneXus 15
Version = 15.0.107450 U1
------------------------------
Program Location:
   at SAP.Middleware.Connector.RfcDestinationManager.IsDestinationConfigurationRegistered()
........
===================================
The type initializer for 'SAP.Middleware.Connector.RfcConfigParameters' threw an exception. (sapnco)
------------------------------
Program Location:
   at SAP.Middleware.Connector.RfcConfigParameters.Initialize()
   at SAP.Middleware.Connector.RfcDestinationManager..cctor()
===================================
Mixed mode assembly is built against version 'v2.0.50727' of the runtime and cannot be loaded in the 4.0 runtime without additional configuration information. (sapnco)
------------------------------
Program Location:
   at SAP.Middleware.Connector.RfcConfigParameters.loadConfiguration()
   at SAP.Middleware.Connector.RfcConfigParameters..cctor()
```

#### **8. When I select Tools > Application Integration > SAP BAPI Import, I get the following error message: "Enterprise Inspector License Not Found."**

You must request a GeneXus ERP Connector for SAP license through the [GeneXus License Manager](https://wiki.genexus.com/commwiki/wiki?19789,,).

You will find the product to authorize with the product name "ERP Connector".

 

#### [**9. When I select Tools > Application Integration > SAP BAPI Import, I get the following error message: "*Method not found: 'Void SAP.Middleware.Connector.RfcTrace.WriteText(System.String)'. (sapnco)"***](#9.+When+I+select+Tools+%26gt%3B+Application+Integration+%26gt%3B+SAP+BAPI+Import%2C+I+get+the+following+error+message%3A+%22Method+not+found%3A+%27Void+SAP.Middleware.Connector.RfcTrace.WriteText%28System.String%29%27.+%28sapnco%29%22)

#### This problem could be related to the fact that an unexpected version of the sapnco.dll in the GAC (Global Assembly Cache) directory exists.

#### [**10. While compiling a GeneXus project which uses a SAP Connector Interface type External Object, I get errors similar to the following: "*sap\type\_SdtSAPGeneralLedgerAccount.cs(66,10): error CS0103: The name  'BUS3006' does not exist in the current context"***](#10.+While+compiling+a+GeneXus+project+which+uses+a+SAP+Connector+Interface+type+External+Object%2C+I+get+errors+similar+to+the+following%3A+%22sap%5Ctype_SdtSAPGeneralLedgerAccount.cs%2866%2C10%29%3A+error+CS0103%3A+The+name+%27BUS3006%27+does+not+exist+in+the+current+context%22)

The reason is that you don't have a GeneXus ERP Connector license. Please request it to [keys@genexus.com](mailto:keys@genexus.com)

In the compilation output, you can find the next error message following the previous one:

```
error CS0006: The metadata file 'bin\GeneXus.Programs.Common.dll' cannot be found
```

If you take a look at the generated program with the error (in that case type\_SdtSAPGeneralLedgerAccount.cs) you will find the following line:

```
// ****  Enterprise Connector Licence Not Found  *****
```

#### **11. When executing a GeneXus .Net application which uses SAP BAPIs as External Objects, I get the following error message:*****"Server Error in '/MyGXSAPAppI.NetEnvironment' Application**."*

Could not load file or assembly 'sapnco, Version=3.0.0.42, Culture=neutral, PublicKeyToken=50436dca5c7f7d23' or one of its dependencies. The system cannot find the file specified.

You must copy the sapnco.dll and sapnco\_utils.dll (part of SAP .Net Connector 3.0.13.0 or higher, 32/64 bits compiled with .NET Framework 2.0) to the web\bin directory of your application. You can download it from <http://service.sap.com/connectors>.

#### [**12.** **When e****xecuting a GeneXus .Net application which uses SAP BAPIs as External Object, I get the following error message: *"Could not load file or assembly 'sapnco' or one of its dependencies. An attempt was made to load a program with an incorrect format."***](#12.+When+executing+a+GeneXus+.Net+application+which+uses+SAP+BAPIs+as+External+Object%2C+I+get+the+following+error+message%3A+%22Could+not+load+file+or+assembly+%27sapnco%27+or+one+of+its+dependencies.+An+attempt+was+made+to+load+a+program+with+an+incorrect+format.%22)

You must check the AppPool used in your web application and set the property Enable 32-Bit Application to true or use the 64bits version of the sapnco\_utils.dll. 

#### [**13. When executing a GeneXus Java application using SAP BAPIs as External Object, I get the following error message: *"NullPointerException Caused by: java.lang.ExceptionInInitializerError: JCo initialization failed with java.lang.UnsatisfiedLinkError: no sapjco3 in java.library.path"***](#13.+When+executing+a+GeneXus+Java+application+using+SAP+BAPIs+as+External+Object%2C+I+get+the+following+error+message%3A+%22NullPointerException+Caused+by%3A+java.lang.ExceptionInInitializerError%3A+JCo+initialization+failed+with+java.lang.UnsatisfiedLinkError%3A+no+sapjco3+in+java.library.path%22)

Review the SAP Java Connector 3.\* documentation; your sapjco3 installation folder must be included in the Path system variable.

#### [**14. When executing a GeneXus Java application using SAP BAPIs as External Object, I get the following error message: *"NullPointerException. Caused by: java.lang.NoClassDefFoundError: Could not initialize class com.sap.conn.jco.rt.JCoRuntimeFactory"***](#14.+When+executing+a+GeneXus+Java+application+using+SAP+BAPIs+as+External+Object%2C+I+get+the+following+error+message%3A+%22NullPointerException.+Caused+by%3A+java.lang.NoClassDefFoundError%3A+Could+not+initialize+class+com.sap.conn.jco.rt.JCoRuntimeFactory%22)

There are different distribution packages for various JRE versions and hardware processors available (AMD, INTELL x86-bit or x64-bit architectures) for SAP Java Connector 3.\*; make sure you install the correct one.

#### [**15.** **When u****sing a BAPI from a GeneXus Application, I get the following error message: *"Cannot convert null or empty string into a BCD."***](#15.+When+using+a+BAPI+from+a+GeneXus+Application%2C+I+get+the+following+error+message%3A+%22Cannot+convert+null+or+empty+string+into+a+BCD.%22)

#### Please, see the SAC# 41866 - Conversion error using a SAP BAPI imported by GX ERP Connector

#### [**16.** **When u****sing a BAPI from a GeneXus Application In Windows Server x64, I get the following error message: *"Could not load file or assembly 'sapnco\_utils.DLL' or one of its dependencies. The specified module could not be found."***](#16.+When+using+a+BAPI+from+a+GeneXus+Application+In+Windows+Server+x64%2C+I+get+the+following+error+message%3A+%22Could+not+load+file+or+assembly+%27sapnco_utils.DLL%27+or+one+of+its+dependencies.+The+specified+module+could+not+be+found.%22)

Make sure you have Microsoft Visual C++ 2010 Redistributable Pack (x86) (mscvp100.dll) installed.

#### [**17. Can I manage documents through the SAP DMS (using BAPIs to manage Objects with attached documents)?**](#17.+Can+I+manage+documents+through+the+SAP+DMS+%28using+BAPIs+to+manage+Objects+with+attached+documents%29%3F)

For more information, read this paper: [GeneXus for SAP: Manage DMS attachments](https://wiki.genexus.com/commwiki/wiki?43745,,)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus ERP Connector](https://wiki.genexus.com/commwiki/wiki?26013) |

---
