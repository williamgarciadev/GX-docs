---
title: "HowTo: Deploy an application to SAP Cloud Platform"
source_id: 32059
source_url: https://wiki.genexus.com/commwiki/wiki?32059
genexus_version: "18"
---

# HowTo: Deploy an application to SAP Cloud Platform

It is possible to run
[Java](https://wiki.genexus.com/commwiki/wiki?12258)-generated applications in SAP Cloud Platform.

Before deployment, using a new [environment](https://wiki.genexus.com/commwiki/wiki?7115) in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) is recommended to generate a new deployment version that runs locally in the Tomcat of the computer used to work with GeneXus connected to the SAP HANA database, as described in [How to use SAP HANA Database on SAP Business Technology Platform](https://wiki.genexus.com/commwiki/wiki?47848). In this way, you can make the configurations that will be used in the production database.

To make a deployment to SAP Cloud Platform, you need to have an account in SAP Cloud Platform because the information of the account will be used not only to connect to the SAP HANA database, but also to upload the application to SAP Cloud Platform during the deployment process. For more information, visit [hcp.sap.com](https://hcp.sap.com/index.html)

The SAP HCP SDK that is required can be downloaded from here: <https://tools.hana.ondemand.com/#cloud>. It corresponds to Java Web Tomcat 8.

### [Steps to deploy to SAP Cloud Platform](#Steps+to+deploy+to+SAP+Cloud+Platform)

**1.** Before making a deployment, the property “Use data source for web based applications” of the SAP HANA data store has to be set to True. Then, the property “JDBC data source” is enabled and has to be set to java:comp/env/jdbc/DefaultDB

**2.** Run a Build All.

**3.** Go to the Build menu and select the Deploy Application option.

**4.** In the Deployment screen:

**1.** Select the Main objects to be included in the deployment.

**2.** In Target, select the option SAP Cloud Platform.

**3.** Set the following properties as indicated below:

**1.** **Host:** Enter the hired server in SAP Cloud Platform. If you're using a trial version, type hanatrial.ondemand.com.

**2.** **HCP SDK Directory:** Configure the path where the SAP Cloud Platform SDK is configured. For example, C:\neo-java-web-sdk-3.14.3.

**3.** **Account name:** It's the account name obtained from the account information in SAP Cloud Platform Cockpit.

**4.** **User and Password:** Username and password used to register at hcp.sap.com.

**5.** **Application Name:** It's the name used to display the application in SAP Cloud Platform. It can be seen in the Java Applications option in the SAP Cloud Platform Cockpit.

**6.** After selecting the main objects and configuring the necessary properties for the automatic deployment, press the Deploy button. It will build the WAR package, as well as upload and deploy it in SAP Cloud Platform.

**7. Using the ERP Connector considerations:** Copy the sapjco3.jar and the libsapjco3.so files in the "Driver" directory under the model's target directory. Those files can be downloaded from the [SAP download center](https://support.sap.com/swdc).

To learn more about how to use SAP Cloud Platform Cockpit, read this [documentation](https://help.hana.ondemand.com/help/frameset.htm?e47748b5bb571014afedc70595804f3e.html).


|  |
| --- |
| **Backlinks** |
| [Toc:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Toc:Application Deployment tool (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54334) | [Deploy Application Targets](https://wiki.genexus.com/commwiki/wiki?42079) |
| [Toc:GeneXus for SAP Systems](https://wiki.genexus.com/commwiki/wiki?33616) |

---
