---
title: "Offline Native Mobile Applications Common Issues"
source_id: 20287
source_url: https://wiki.genexus.com/commwiki/wiki?20287
genexus_version: "18"
---

# Offline Native Mobile Applications Common Issues

## [Limitations](#Limitations)

### [Server-side External Object methods](#Server-side+External+Object+methods)

Some External Object methods, those that are executed from server-side like GeoLocalizationAPI.GetDistance(), are not implemented for offline Generators, yet. This kind of methods are generally invoked from [System Events](https://wiki.genexus.com/commwiki/wiki?17042), Procedures, and Data Providers.  However, methods that run on the device's side, those directly mentioned on [User Events](https://wiki.genexus.com/commwiki/wiki?17042) are supported (for instance GeoLocalizationAPI.GetMyLocation).

### [Data types](#Data+types)

There are some DataTypes that are not implemented for offline applications yet. Check the [Offline non-implemented DataTypes](https://wiki.genexus.com/commwiki/wiki?25398) document for offline applications.

### [Business component for two-level transactions](#Business+component+for+two-level+transactions)

Transaction objects with two-levels (header plus a set of lines) won't be automatically synchronized with the server from the device (i.e. send) by using [Business Component](https://wiki.genexus.com/commwiki/wiki?5846). Since only one-level transaction business component is allowed, as a workaround, you can flat the transaction by splitting it into two independent components: the header and its lines.

## [Troubleshooting](#Troubleshooting)


### ['Known Error' when inserting/updating tables from offline app](#%27Known+Error%27+when+inserting%2Fupdating+tables+from+offline+app)

This is a temporally restriction. Referential integrity messages errors, such as "Not matching Customer", "Customer already exists", etc are not included.  This also applies to Error rule messages.

---

### [Unable to Chain SQLException no such column](#Unable+to+Chain+SQLException+no+such+column)

This error appears when invoking a WWSD that requires a join on SQLite between two tables (Order and Customer):

09-04 02:19:19.915: E/AndroidRuntime(884): Caused by: com.genexus.GXRuntimeException: java.sql.SQLException: Unable to Chain SQLException no such column: T1.CustomerId: , while compiling: SELECT T1.`CustomerId`, T1.`PurchaseOrderDate`, T1.`PurchaseOrderId`, T2.`CustomerName` FROM (`PurchaseOrder` T1 INNER JOIN `Customer` T2 ON T2.`CustomerId` = T1.`CustomerId`) ORDER BY T2.`CustomerName`

This was a restriction on SQlite 3.5.9 (more info).  Android 2.2 is required. Check [GeneXus X Evolution 3 Hardware and Software Requirements](https://wiki.genexus.com/commwiki/wiki?22453,,)

---

### [Failure [INSTALL\_FAILED\_OLDER\_SDK]](#Failure+NoWiki+1)

Android Execution Failed  
Run <main> Failed

Solution:

Android 2.1 is no longer supported since GeneXus Tilo. Version 2.2 or higher is required.Check [GeneXus X Evolution 3 Hardware and Software Requirements](https://wiki.genexus.com/commwiki/wiki?22453,,)

After installed, delete the myGxAvd emulator instance and run the app again in order to create a new instance in GX.

Recommended: install Google Inc.:Google APIs:8 (2.2) in order to prototype faster than with Android 4.x emulator instances

---

### [java.lang.OutOfMemoryError when loading the app in Emulator](#java.lang.OutOfMemoryError+when+loading+the+app+in+Emulator)

If logcat shows this error,  increase Max VM Heap size of the Android Virtual Device (AVD)

```
E/GeneXusApplication(  299): java.lang.OutOfMemoryError

E/GeneXusApplication(  299):  at java.lang.AbstractStringBuilder.enlargeBuffer(AbstractStringBuilder.java:97)

E/GeneXusApplication(  299):  at java.lang.AbstractStringBuilder.append0(AbstractStringBuilder.java:157)

E/GeneXusApplication(  299):  at java.lang.StringBuilder.append(StringBuilder.java:217)

E/GeneXusApplication(  299):  at com.artech.common.StringUtil.convertStreamToString(StringUtil.java:56)

E/GeneXusApplication(  299):  at com.artech.base.metadata.loader.MetadataLoader.getDefinition(MetadataLoader.java:161)

E/GeneXusApplication(  299):  at com.artech.base.metadata.loader.WorkWithMetadataLoader.load(WorkWithMetadataLoader.java:20)

E/GeneXusApplication(  299):  at com.artech.base.metadata.loader.ApplicationLoader.loadPatternInstances(ApplicationLoader.java:340)

E/GeneXusApplication(  299):  at com.artech.base.metadata.loader.ApplicationLoader.loadMetadata(ApplicationLoader.java:209)

E/GeneXusApplication(  299):  at com.artech.base.metadata.loader.ApplicationLoader.loadApplication(ApplicationLoader.java:93)

E/GeneXusApplication(  299):  at com.artech.application.MyApplication.initialize(MyApplication.java:254)

E/GeneXusApplication(  299):  at com.artech.activities.dashboard.DashboardActivity.LoadApplication(DashboardActivity.java:314)

E/GeneXusApplication(  299):  at com.artech.activities.dashboard.DashboardActivity.access$000(DashboardActivity.java:53)

E/GeneXusApplication(  299):  at com.artech.activities.dashboard.DashboardActivity$1.run(DashboardActivity.java:301)

E/GeneXusApplication(  299):  at java.lang.Thread.run(Thread.java:1096)
```

---

---

|  |
| --- |
| **Backlinks** |
| [HowTo: Convert online applications into offline applications](https://wiki.genexus.com/commwiki/wiki?24591) | [My first Offline Native Mobile application](https://wiki.genexus.com/commwiki/wiki?20249) | [Toc:Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22228) |

---
