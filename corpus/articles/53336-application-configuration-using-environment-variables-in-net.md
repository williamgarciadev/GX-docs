---
title: "Application Configuration using Environment Variables in .NET and Java"
source_id: 53336
source_url: https://wiki.genexus.com/commwiki/wiki?53336
genexus_version: "18"
---

# Application Configuration using Environment Variables in .NET and Java

In various scenarios, it is common practice to read configuration information from environment variables, rather than configuration files.  This document details how to achieve this in the [.NET](https://wiki.genexus.com/commwiki/wiki?38604) and [Java](https://wiki.genexus.com/commwiki/wiki?12258) Generators.

Each configuration entry of an application can be read from an environment variable. This environment variable must be prefixed with 'GX\_' and it must be all in capital letters.

**Sample:**

|  |  |  |
| --- | --- | --- |
| **Name** | **Environment Variable (.NET)** | **Environment Variable (JAVA)** |
| Database Name | GX\_CONNECTION-DEFAULT-DB | Does not apply. Use GX\_DEFAULT\_DB\_URL instead |
| Connection endpoint | GX\_CONNECTION-DEFAULT-DATASOURCE | GX\_DEFAULT\_DB\_URL  Sample:   * jdbc:mysql://hostname:3306/mybdname?useSSL=false |
| Connection username | GX\_CONNECTION-DEFAULT-USER | GX\_DEFAULT\_USER\_ID |
| Connection password | GX\_CONNECTION-DEFAULT-PASSWORD | GX\_DEFAULT\_USER\_PASSWORD |
| Connection port | GX\_CONNECTION-DEFAULT-PORT | Does not apply. Use GX\_DEFAULT\_DB\_URL instead |
| Additional connection string attributes | GX\_CONNECTION-DEFAULT-OPTS | Does not apply. Use GX\_DEFAULT\_DB\_URL instead |

### [**Environment Variables Database configuration Example (.NET)**](#Environment+Variables+Database+configuration+Example+%28.NET%29)

```
GX_CONNECTION-DEFAULT-DB=test
GX_CONNECTION-DEFAULT-DATASOURCE=mysql8
GX_CONNECTION-DEFAULT-USER=root
GX_CONNECTION-DEFAULT-PASSWORD=admin
GX_CONNECTION-DEFAULT-PORT=3307
GX_CONNECTION-DEFAULT-OPTS=Timeout=30
```

**GAM**

```
GX_CONNECTION-GAM-DB=test
GX_CONNECTION-GAM-DATASOURCE=mysql8
GX_CONNECTION-GAM-USER=root
GX_CONNECTION-GAM-PASSWORD=admin
GX_CONNECTION-GAM-PORT=3307
GX_CONNECTION-GAM-OPTS=Timeout=30
```

### [**Environment Variables Database configuration Example (JAVA)**](#Environment+Variables+Database+configuration+Example+%28JAVA%29)

```
GX_DEFAULT_DB_USER_ID=root
GX_DEFAULT_DB_PASSWORD=admin
GX_DEFAULT_DB_URL=jdbc:mysql://hostname:3306/mybdname?useSSL=false
```

### [.NET](#.NET)

In the case of .NET, the variable must be called the same as it is defined in the appsettings.json.

Suppose you have a Docker Image (named "environmenttest.netenvironment") with a web app that points to a production DB. Now you want to raise an instance of that image pointing to the Test DB (named "EnvTest"). For that, you execute the following command:

```
docker run --rm -e GX_CONNECTION-DEFAULT-DB=EnvTest environmenttest.netenvironment
```

where the flag -e sets the environment variable GX\_Connection-Default-DB (same name as it has in the appsettings.json) to "EnvTest". When the application starts and wants to read the value of that property, it first checks if there is an environment variable with that name. As it exists, it takes that value.

If, on the contrary, you want to raise the same image (environmenttest.netenvironment) against the production DB (EnvProd), execute the following command:

```
docker run --rm -e GX_CONNECTION-DEFAULT-DB=EnvProd environmenttest.netenvironment
```

The same works for any configuration property of the appsettings.json. Whenever you are going to look for a configuration property, the application first searches for an environment variable with that name.

### [.NET Framework](#.NET+Framework)

[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892) works just like .NET, but the settings are stored in a file called web.config.

### [Java](#Java)

The case of Java is a bit different, because Java has the client.cfg that works differently, it has sections.

For example, suppose you have a section called com.environmenttest|DEFAULT (which is the default DBMS of your environment) where there is a DB\_URL entry that has the following url to the DBMS

jdbc:jtds:sqlserver://172.16.3.21:1435/EnvProd

If you want to change that value, you have to create an environment variable concatenating the section and the property, all in upper case, replacing dots (".") and pipes ("|") with an underscore ("\_"). For example, if you create the variable GX\_COM\_ENVIRONMENTTEST\_DEFAULT\_DB\_URL you overwrite the value of the client.cfg. The value of that variable becomes the one that the app handles.

You can also create the variable without specifying the namespace, like this: GX\_DEFAULT\_DB\_URL.

In this case, to launch the container with this variable, you have to execute the following command to connect to the test DB:

```
docker run --rm -p 8890: 8080 -e GX_DEFAULT_DB_URL=jdbc:jtds:sqlserver://172.16.3.21:1435/EnvTest environmenttestjavaenvironment
```

and the following one for the production DB:

```
docker run --rm -p 8890: 8080 -e GX_DEFAULT_DB_URL=jdbc:jtds:sqlserver://172.16.3.21:1435/EnvProd environmenttestjavaenvironment
```

When searching for the DB\_URL environment variable in the default data store, the following environment variable will be searched for:

GX\_COM\_ENVIRONMENTTEST\_DEFAULT\_DB\_URL

If no value is found for that entry, then GX\_DEFAULT\_DB\_URL will be searched for.

**AWS MYSQL Sample**

```
docker run --rm -p 8890: 8080 -e GX_DEFAULT_DB_URL=jdbc:mysql://myrdsname.us-east-1.rds.amazonaws.com/mybdname?useSSL=false
```

### [See Also](#See+Also)

[Application Configuration using Environment Variables](https://wiki.genexus.com/commwiki/wiki?39459)  
[Application Configuration using Environment Variables in Cloud Services](https://wiki.genexus.com/commwiki/wiki?53339)  
[HowTo: Deploy an Application to Docker](https://wiki.genexus.com/commwiki/wiki?36951)


|  |
| --- |
| **Backlinks** |
| [Application Configuration using Environment Variables](https://wiki.genexus.com/commwiki/wiki?39459) | [Application Configuration using Environment Variables in Cloud Services](https://wiki.genexus.com/commwiki/wiki?53339) | [Table of contents:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) |
| [Table of contents:Application Deployment tool (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54334) | [Log settings with environment variables](https://wiki.genexus.com/commwiki/wiki?53361) | [Log settings with environment variables (GeneXus 18 upgrade 1)](https://wiki.genexus.com/commwiki/wiki?53615) | [Log settings with environment variables (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?56152) |
| [Log settings with environment variables (GeneXus 18 Upgrade 7)](https://wiki.genexus.com/commwiki/wiki?57632) |

---
