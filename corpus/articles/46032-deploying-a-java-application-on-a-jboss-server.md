---
title: "Deploying a Java application on a JBoss server"
source_id: 46032
source_url: https://wiki.genexus.com/commwiki/wiki?46032
genexus_version: "18"
---

# Deploying a Java application on a JBoss server

This example focuses on a particular case, deploying a Java application to a test environment using a JBoss application server, accessing the Oracle Database via JNDI and using the [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746).

## [Step 1: Creating the Data Source](#Step+1%3A+Creating+the+Data+Source)

`[imagen omitida: wiki id 46117]`

For this step, you need to use the Database Driver, which can be found at <GeneXus\_Installation>\gxjava\drivers\ojdbc\*.jar

The driver is deployed in the application server, and you can check that it is listed in the configuration. The creation of a new data source must use the driver, as well as contain the connection data to the Oracle instance; the process is completed with a successful connection test.

The name assigned to the Data Source is configured in the KB, in the Data Store properties.

```
java:/OracleDS
```

[Use Data Source for Web Based Applications](https://wiki.genexus.com/commwiki/wiki?9384,,)

[JDBC Data Source](https://wiki.genexus.com/commwiki/wiki?2112)

Both the default data store and the GAM data store use the same data source in the example.

## [Step 2: Packaging Generation](#Step+2%3A+Packaging+Generation)

The WAR packaging is generated using the [Application Deployment Tool](https://wiki.genexus.com/commwiki/wiki?32092).

`[imagen omitida: wiki id 46118]`

To do so, set the property [Use Application Server Data Source](https://wiki.genexus.com/commwiki/wiki?44032) to True.

Reorganization of the GAM database can be done from within GeneXus or using the GAM Deploy Tool in standalone or command line mode. See [GAM Deploy Tool](https://wiki.genexus.com/commwiki/wiki?18608)

## [Step 3: Deployment and Packaging Configuration (WAR)](#Step+3%3A+Deployment+and+Packaging+Configuration+%28WAR%29)

The application is deployed in the test environment.

`[imagen omitida: wiki id 46119]`

In this step, errors may occur due to the specific configuration of the environment, which should be solved by modifying mainly web.xml or jboss-deployment-structure.xml configuration files.

```
GenexusWebApp.war could not be deployed.Details {"WFLYDC0074: Operation failed or undone on all servers. Server failures: " => {"server-group" => {"main-server-group" => {"host" => {"master" => { "server-one" => {"WFLYCTL0080: Servicios fallidos" => {"jboss.deployment.unit.\"GenexusWebApp.war\".undertow-deployment.UndertowDeploymentInfoService" => "java.lang.ClassNotFoundException: genexus.security.api.aGAMSSORestRequestTokenAndUserInfo_v20 from [Module \"deployment.GenexusWebApp.war\" from Service Module Loader] Caused by: java.lang.ClassNotFoundException: genexus.security.api.aGAMSSORestRequestTokenAndUserInfo_v20 from [Module \"deployment.GenexusWebApp.war\" from Service Module Loader]"}}, "server-two" => {"WFLYCTL0080: Service failures" => {"jboss.deployment.unit.\"GenexusWebApp.war\".undertow-deployment.UndertowDeploymentInfoService" => "java.lang.ClassNotFoundException: genexus.security.api.aGAMSSORestRequestTokenAndUserInfo_v20 from [Module \"deployment.GenexusWebApp.war\" from Service Module Loader] Caused by: java.lang.ClassNotFoundException: genexus.security.api.aGAMSSORestRequestTokenAndUserInfo_v20 from [Module \"deployment.GenexusWebApp.war\" from Service Module Loader]"}} }}}}}}
```

The [Solution](https://access.redhat.com/solutions/3682621) to this error is a dependency defined in the web.xml file that is not necessary, so it is enough to delete or rename it using lowercase.

Also added to the web.xml file are the tags needed to disable JBoss' RESTeasy service module, as described in the article [Deployment of Java Applications](https://wiki.genexus.com/commwiki/wiki?20110)

## [Step 4: Connection property may be needed](#Step+4%3A+Connection+property+may+be+needed)

In the particular case of some DBMS such as Oracle or SQL Server, the Data Source property must be configured.

```
fixed string = True
```

`[imagen omitida: wiki id 46120]`

This can also be done by editing the file domain.xml/standalone.xml, as indicated in [SAC #21246](https://www.genexus.com/es/developers/websac?data=21246;;)  
“NOTE: This is because a Data Source is used; GeneXus adds this property through code, but when using a Data Source you have to add it manually.” For this reason, see how the error Repository not found is solved.

## [Step 5: Application testing](#Step+5%3A+Application+testing)

`[imagen omitida: wiki id 46121]`

In this step, a test is performed by querying the application data and successfully changing it.

**Software versions used:**

* [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/wiki?45624,,)
* JBoss EAP 7.3.0.GA
* Java 1.8
* Oracle 19C

**Note:** To deploy the application in a distributed environment (cluster), take into account the information of [SAC #47815](https://www.genexus.com/es/developers/websac?data=47815;;)
