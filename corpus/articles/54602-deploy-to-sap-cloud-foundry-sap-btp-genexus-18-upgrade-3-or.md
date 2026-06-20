---
title: "Deploy to SAP Cloud Foundry - SAP BTP (GeneXus 18 Upgrade 3 or prior)"
source_id: 54602
source_url: https://wiki.genexus.com/commwiki/wiki?54602
genexus_version: "18"
---

# Deploy to SAP Cloud Foundry - SAP BTP (GeneXus 18 Upgrade 3 or prior)

**Prerequisites:**

* Having installed the [Cloud Foundry Client](https://github.com/cloudfoundry/cli#installers-and-compressed-binaries)

To deploy a GeneXus Application to SAP Cloud Foundry, follow the steps described below:

1. [Cloud Foundry Configuration](https://wiki.genexus.com/commwiki/wiki?49572)
2. [Data Store Configuration](https://wiki.genexus.com/commwiki/wiki?49572)
3. [Application Deployment](https://wiki.genexus.com/commwiki/wiki?49572)

### [Cloud Foundry Configuration](#Cloud+Foundry+Configuration)

Log into SAP Cloud Foundry Trial (if you do not have an account, you have to create one). Once there, select trial:

`[imagen omitida: wiki id 49573]`

Then, select the dev Space as shown below:

`[imagen omitida: wiki id 49574]`

In the left menu, select Services > Service Marketplace. Then, search for Hana using the search box, and select SAP HANA Cloud:

`[imagen omitida: wiki id 49575]`

The next step is to create a new instance of the service. So, select Instances and press the New Instance button:

`[imagen omitida: wiki id 49576]`

This will open a Popup Wizard that will inform you to follow a link if you want to manage SAP HANA Cloud Instances, click on that link.

`[imagen omitida: wiki id 49577]`

This will redirect you to a new page and ask to select an account to login with

`[imagen omitida: wiki id 49578]`

Log in or select an account and continue.  
  
SAP HANA Cloud Central will load, on this page select Create

`[imagen omitida: wiki id 49579]`

This will launch a new Wizard, to set up the new HANA database to be created.  
  
`[imagen omitida: wiki id 49580]`  
  
On the first step, select SAP HANA Cloud, SAP HANA Database and proceed to the next step.  
  
`[imagen omitida: wiki id 49581]`

On this next step lets setup the HANA instance name and the password of the DBADMIN (**Save this password somewhere you will use it later**)  
  
After setting these properties up, continue to the next step.  
  
`[imagen omitida: wiki id 49582]`

This step it lets you configure the space that will be assigned to the database (by default it is 120Gb).

After setting this up (if you decided to change the default) continue to the next step.

On the 4th step, the Wizard lets you set up replicas, but this functionality is unavailable for trial instances.

Proceed to the 5th and last step.  
  
`[imagen omitida: wiki id 49583]`

This step allows you to set up the accessibility to this database. For you to be able to reach this database from GeneXus, you will have to select **Allow all IP addresses.**  
  
After this last step, select Create Now. While the database is being created, go to Service Instances of the SAP BTP Cockpit.  
  
Here, you will see the new database as an instance. Select the 3 dots and Create Service Key:  
  
`[imagen omitida: wiki id 49584]`  
  
This will open a Popup to create de Service Key. Select the name you want for the Service Key and then click on Create:  
  
`[imagen omitida: wiki id 49585]`  
  
After creating the Service Key save its JSON, because you will need it to configure the database on GeneXus.

### [Data Store Configuration](#Data+Store+Configuration)

To be able to use the HANA Cloud, you need to configure the [Data Store](https://wiki.genexus.com/commwiki/wiki?7117). To achieve this, go to the [Knowledge Base Preferences](https://wiki.genexus.com/commwiki/wiki?7109) and select the [Environment](https://wiki.genexus.com/commwiki/wiki?7115) you want to deploy. Then, select the desired [Data Store](https://wiki.genexus.com/commwiki/wiki?7117), and set the following properties with the values you have on the JSON you retrieved from the Service Key:

[Use Custom JDBC URL](https://wiki.genexus.com/commwiki/wiki?9381) = True  
[Use Custom JDBC URL](https://wiki.genexus.com/commwiki/wiki?9381) = JSON URL field (you must set to false the validateCertificate parameter, for example, jdbc:sap://ad72c-43e5-b2ea-39c60bbcc1be.hana.trial-us10.hanacloud.ondemand.com:443?encrypt=true&validateCertificate=false )  
User Id = DBADMIN  
Password = DBADMIN password that you created.  
Database Schema = The schema name you want to use.

You should have something like this:

`[imagen omitida: wiki id 53395]`

To connect with SAP HANA database you must use the latest SAP HANA JDBC driver, you can download it from [here](https://mvnrepository.com/artifact/com.sap.cloud.db.jdbc/ngdbc) and then copy the ngdbc.jar, for example the ngdbc-2.14.10.jar, inside the folder \Web\lib in your target environment.

This allows you to work on your application using the SAP HANA Cloud directly, even if you are still developing on your PC and have not deployed yet to SAP BTP.

After executing all the queries, you are ready to deploy the application to SAP BTP.

### [Application Deployment](#Application+Deployment)

**Important:**

1. You must verify that the [Java platform support property](https://wiki.genexus.com/commwiki/wiki?48353) is set with "Java EE" and the [JDK Directory (JAVA HOME) property](https://wiki.genexus.com/commwiki/wiki?52135) is configured with the path to a JDK 8 directory and then rebuild all if necessary. The default version in SAP BTP when using the sap\_java\_buildpack is Java 8 as documented [here](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/a3f90069d6cd41da82f34a6123d82ce6.html?q=java%20buildpack#supported-versions).
2. You must include the reference to include the JDBC driver file as explained in [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) in the section Deployment of additional files and directories.  For example, in the file gxdproj you must add
   1. <ItemGroup>  
              <AdditionalFile Include="lib\ngdbc-2.14.10.jar">  
                  <RelativeTargetDir>WEB-INF\lib</RelativeTargetDir>  
              </AdditionalFile>  
          </ItemGroup>

To deploy the application, go to Build > Deploy Application and select the objects you want to deploy. Select SAP Cloud Platform (Cloud Foundry) as Target.

Then, you need to set up the following Deploy Properties:

[Cloud Foundry CLI Directory](https://wiki.genexus.com/commwiki/wiki?45791) = the directory where you have installed the Cloud Foundry client (e.g.: C:\Program Files\Cloud Foundry)  
[API Endpoint](https://wiki.genexus.com/commwiki/wiki?45792) = endpoint where your Cloud Foundry account is located.  
[Organization name](https://wiki.genexus.com/commwiki/wiki?45793) = organization name of your Cloud Foundry account (e.g.: p123456789trial).  
[Space name](https://wiki.genexus.com/commwiki/wiki?45794) = space name of the Cloud Foundry (e.g.: dev).  
User = user account used to log into the SAP Cloud Foundry.  
Password = user's password.  
[HANA Instance Name](https://wiki.genexus.com/commwiki/wiki?45795) = name of the service created (e.g.: myHANAdb).  
[Application Name](https://wiki.genexus.com/commwiki/wiki?45796) = name you want to give to the application.

In the routes field, it will show you where the app has been deployed, and you can access it by adding /servlet/com.<Knowledge Base name>.<object you want to access>

(e.g.: https://deploycf-wacky-klipspringer.cfapps.eu10.hana.ondemand.com/servlet/com.deploycf.fioribaseobjects.fiorilaunchpad).
