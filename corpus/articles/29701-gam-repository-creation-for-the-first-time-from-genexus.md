---
title: "GAM repository creation for the first time from GeneXus"
source_id: 29701
source_url: https://wiki.genexus.com/commwiki/wiki?29701
genexus_version: "18"
---

# GAM repository creation for the first time from GeneXus

When you [activate GAM](https://wiki.genexus.com/commwiki/wiki?19946) for the first time in a [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836), the following happens:

### [1. GAM objects are imported into the Knowledge Base.](#1.+GAM+objects+are+imported+into+the+Knowledge+Base.)

External objects are imported and used to access the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535).

[Examples](https://wiki.genexus.com/commwiki/wiki?21993) are imported in the "GAM\_Examples" folder depending on the options selected during the [Activation Process](https://wiki.genexus.com/commwiki/wiki?21973).

### [2. A secondary Data Store is created for storing GAM information.](#2.+A+secondary+Data+Store+is+created+for+storing+GAM+information.)

This Data Store is called "GAM" and is created following these criteria:

#### [**For SQL Server**](#For+SQL+Server)

If the Reorganization Data Store is *SQL Server*, the default values for "GAM" Data Store are as follows:

* Database Name is the same as the Database Name of the Reorganization Data Store.
* Database Schema: This property is set to "gam" by default.

#### [**For MySQL**](#For+MySQL)

The GAM repository will be located by default in the same database as the default database; however, the schema will be another one named "gam".  
If the Reorganization Data Store is *MySQL*, the default value for "GAM" Data Store is as follows:

* Database Name: by default, it is set to \_gam.

The GAM repository will be under a different database by default.

#### [**For Oracle**](#For+Oracle)

In an *Oracle database*, GeneXus does not set any default value for the Database Name; this value must be set by the user.

### [3. After pressing F5, a connection to the database is established](#3.+After+pressing+F5%2C+a+connection+to+the+database+is+established)

After pressing F5, a connection is established to the database specified in GAM Data Store (using the connection properties of this Data Store: database name, user ID, user password), checking for the existence of some tables and GAM version.

Given that these tables don't exist, the GAM database tables are created. So, the following happens:

* Some properties related to the connection to GAM repository are assigned, with their default values: [Repository ID property](https://wiki.genexus.com/commwiki/wiki?15802), [Administrator User Name Property](https://wiki.genexus.com/commwiki/wiki?15215), [Administrator User Password Property](https://wiki.genexus.com/commwiki/wiki?15216), [Connection User Name property](https://wiki.genexus.com/commwiki/wiki?15217), [Connection User Password Property](https://wiki.genexus.com/commwiki/wiki?15218).
* The GAM database and all its tables are created. Before the tables are created, the user is asked if he/she wants to create the GAM database structure.

`[imagen omitida: wiki id 15771]`

### [4. Metadata is initialized](#4.+Metadata+is+initialized)

* Tables are populated with metadata.
* The [GAM Manager Repository](https://wiki.genexus.com/commwiki/wiki?18617) and the working Repository are created.
* Also, the administrator user and the [connection user](https://wiki.genexus.com/commwiki/wiki?16150) are created.
* The default [Security Policy](https://wiki.genexus.com/commwiki/wiki?18521) is created, as well as the default AuthenticationType: [Local Authentication Type](https://wiki.genexus.com/commwiki/wiki?20703). The default [Roles](https://wiki.genexus.com/commwiki/wiki?17569) are created.

### [5. Registration of [GAM Applications](https://wiki.genexus.com/commwiki/wiki?15910) is executed](#5.+Registration+of+com.gxwiki.wiki%3F15910%2CGAM%2B-%2BApplications+GAM+Applications+is+executed)

* The [GAM Backend Application](https://wiki.genexus.com/commwiki/wiki?29699) is created. It's populated with some permissions to allow building the Menu of the [GAM Backoffice](https://wiki.genexus.com/commwiki/wiki?15935).
* An [Application](https://wiki.genexus.com/commwiki/wiki?15910) is created for the Web model, and one Application is generated for each Main SD object.
* Also, [Permissions](https://wiki.genexus.com/commwiki/wiki?15912) are generated (if [Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214) = Authorization).

### [Notes](#Notes)

* Any of the default values of these properties can be changed: [Repository ID property](https://wiki.genexus.com/commwiki/wiki?15802), [Administrator User Name Property](https://wiki.genexus.com/commwiki/wiki?15215), [Administrator User Password Property](https://wiki.genexus.com/commwiki/wiki?15216), [Connection User Name property](https://wiki.genexus.com/commwiki/wiki?15217), [Connection User Password Property](https://wiki.genexus.com/commwiki/wiki?15218). When creating the GAM database for the first time, the administrator user and connection user are created according to the settings of the corresponding properties.
* If [Reorganize server tables property](https://wiki.genexus.com/commwiki/wiki?8955) is set to 'No', the GAM database won't be reorganized.


|  |
| --- |
| **Backlinks** |
| [GAM - Activation Process](https://wiki.genexus.com/commwiki/wiki?21973) | [GAM - Getting Started](https://wiki.genexus.com/commwiki/wiki?19946) | [GAM - Native Mobile Authentication](https://wiki.genexus.com/commwiki/wiki?15222) |
| [GAM Backend Application](https://wiki.genexus.com/commwiki/wiki?29699) | [GAM repository management in GeneXus](https://wiki.genexus.com/commwiki/wiki?15769) | [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [HowTo: Define a Menu using GAM](https://wiki.genexus.com/commwiki/wiki?29681) |

---
