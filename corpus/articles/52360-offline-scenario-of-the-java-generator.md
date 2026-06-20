---
title: "Offline scenario of the Java Generator"
source_id: 52360
source_url: https://wiki.genexus.com/commwiki/wiki?52360
genexus_version: "18"
---

# Offline scenario of the Java Generator

Before starting to set the offline environment for the generator, check [SAC #60943](https://www.genexus.com/en/developers/websac?data=60943;;).

The [GeneXus Java Generator](https://wiki.genexus.com/commwiki/wiki?12258) Standard Classes and their dependencies are downloaded from the Internet. So, to install the necessary drivers the computer must be connected to the Internet at least once.

In order to use Gradle on a computer without internet access, you must follow these steps:

1. Make sure you have a computer with Internet access.
2. Go to **Tools >CMD Environment Directory**,and open the Windows command console (CMD).
3. Navigate to the Web folder of a model that uses the Java Generator.
4. Run the Gradle's [getDeps](https://wiki.genexus.com/commwiki/wiki?52359) command to download the necessary packages to a local directory (by default it will be C:\Users\<user>\.gradle\caches\modules-2\files-2.1). In addition, the DBMS to be used must be specified. The available DBMS are as follows:
   * SQLSERVER
   * ORACLE
   * POSTGRESQL
   * MYSQL
   * DB2ISERIES
   * DAMENG

**Note**: If you need a DBMS that is not in the list above you must download the driver from the provider's site and copy it into the lib folder.

After downloading the packages required by the Java Generator to the local directory, the KBs can be generated and compiled even without an internet connection.

In addition, it is possible to copy the downloaded folders to an offline computer to be able to compile the same KB. For that, you need to copy the folders .gradle and .m2 from C:\Users\<user>\ of the online computer to the same path on the computer without an internet connection.

Notice that this operation must be done every time a GeneXus upgrade is installed, as internal dependencies are updated.

### [Samples](#Samples+)

To use the Oracle or SQL Server DBMS, execute the following command:

```
gradlew getDeps -PJAVA_PLATFORM="both" -PSQLSERVER -PORACLE
```

### [Considerations](#Considerations)

To work with [SAP HANA Database](https://wiki.genexus.com/commwiki/wiki?31713) follow the steps below:

1. Download and install the SAP HANA client from [SAP's website](https://tools.hana.ondemand.com/#hanatools).
2. Download the SAP HANA JDBC driver from a Maven repository such as <https://mvnrepository.com/artifact/com.sap.cloud.db.jdbc/ngdbc>.
3. Configure the JDBC connection in Genexus and add the downloaded JDBC driver to the Genexus classpath. As shown in [Error in the first table creation when you use SAP HANA database](https://wiki.genexus.com/commwiki/wiki?34179)
4. Create a connection to the SAP HANA database using the JDBC connection information. As shown in [Data Store Configuration](https://wiki.genexus.com/commwiki/wiki?49572).

Note that this must be done with an Internet connection and once you have downloaded the necessary packages for the Java generator to the local directory, the KBs can be generated and compiled even without an Internet connection.

### [Troubleshooting](#Troubleshooting)

1. If there are dependency problems, build your KB on the computer with an internet connection to download the missing dependencies.
2. Remember that in order to download the necessary dependencies, it is essential to have access to the following domains:

   * pkgs.dev.azure.com
   * repo.maven.apache.org
   * repository.openmindonline.it
   * mavenCentral()

### [Availability](#Availability)

This feature is available since [GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066).


|  |
| --- |
| **Backlinks** |
| [Compilation process with the Java Generator](https://wiki.genexus.com/commwiki/wiki?52362) | [Compilation process with the Java Generator (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?53881) | [Table of contents:Java Applications Development](https://wiki.genexus.com/commwiki/wiki?52358) |

---
