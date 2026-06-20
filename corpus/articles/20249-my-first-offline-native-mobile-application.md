---
title: "My first Offline Native Mobile application"
source_id: 20249
source_url: https://wiki.genexus.com/commwiki/wiki?20249
genexus_version: "18"
---

# My first Offline Native Mobile application

This document is a step by step explanation of how to create a simple native offline application with GeneXus.

**Before** starting with the tutorial, please check that the [prerequisites](https://wiki.genexus.com/commwiki/wiki?22259) are correctly installed, as also it is recommended you to briefly look at the [Offline Applications overview](https://wiki.genexus.com/commwiki/wiki?22228) and the [Offline Native Mobile applications architecture](https://wiki.genexus.com/commwiki/wiki?22221) documents for better understanding of how the Offline applications works.

In this sample, the application uses a local SQLite database on the device and communicates via REST services with a [NET Generator](https://wiki.genexus.com/commwiki/wiki?2892) web server, which persists data on an MSSQLServer database, to perform synchronization processes. If you are using another web generator, like the Java Generator, or another [DBMS](https://wiki.genexus.com/commwiki/wiki?9518,,), the steps are the same but the prerequisites may change.

### [Step 1: Create a new Knowledge Base](#Step+1%3A+Create+a+new+Knowledge+Base)

Open GeneXus and create a [new Knowledge Base](https://wiki.genexus.com/commwiki/wiki?9596). Select your preferred Prototyping Environment.

`[imagen omitida: wiki id 37362]`

### [Step 2: Model the application](#Step+2%3A+Model+the+application)

Create the Customer and Company [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)s with the following structure:

`[imagen omitida: wiki id 32436]`

Please **note** that [predefined domains](https://wiki.genexus.com/commwiki/wiki?14610) were used for certain attributes and, in both Transactions. **Note** that each identifier attribute is based on the GUID data type with the [Autogenerate Guid property](https://wiki.genexus.com/commwiki/wiki?40892) set to True.

### [Step 3: Apply the Work With pattern](#Step+3%3A+Apply+the+Work+With+pattern)

[Apply the Work With pattern](https://wiki.genexus.com/commwiki/wiki?15975) on both transactions. To do so, for each Transaction, click on the **Patterns** tab, then choose **Work With** tab, and check the checkbox as shown below and save:

`[imagen omitida: wiki id 32437]`

### [Step 4: Customize some layouts (Optional)](#Step+4%3A+Customize+some+layouts+%28Optional%29)

Once the Work With pattern is applied to both transactions, you are free to modify their Layouts, Events, and many other components.  
In this step, some little changes are made on the List layout of the Work With applied to the Customer Transaction in order to show more information when displaying the customers.

From the Toolbox, drag & drop the control **Attribute/variable** in order to insert attributes you want to see on the Customer list screen. For example, CustomerEmail:

`[imagen omitida: wiki id 32438]`

You can remove the label of the attribute by setting the **Label position** property value to "None":

`[imagen omitida: wiki id 32439]`

### [Step 5: Create the main Menu of the application](#Step+5%3A+Create+the+main+Menu+of+the+application)

Create a [Menu object](https://wiki.genexus.com/commwiki/wiki?16321) called Menu.

`[imagen omitida: wiki id 32440]`

This object is like a menu; you can use it to call the Work With objects created in the previous Steps. To do this: right-click in the **Items** option to add actions to the Menu. You must select the WorkWith<*TransactionName>* objects from the [Select Object dialog](https://wiki.genexus.com/commwiki/wiki?9889):

`[imagen omitida: wiki id 32441]`

When you select a WorkWith<*TransactionName*> object, the associated Event to this action is generated automatically:

```
Event 'WorkWithCustomer'
     WorkWithCustomer.Customer.List()
EndEvent

Event 'WorkWithCompany'
     WorkWithCompany.Company.List()
EndEvent
```

### [Step 6: Shift your application to the offline architecture](#Step+6%3A+Shift+your+application+to+the+offline+architecture)

Change the [Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?20911) of the Menu object to "Offline". This step is crucial, it means a huge change in the application architecture. If you want to learn more about this, read the [Offline Native Mobile applications architecture](https://wiki.genexus.com/commwiki/wiki?22221) document.

`[imagen omitida: wiki id 32443]`

### [Step 7: Edit the Native Mobile Generator Preferences](#Step+7%3A+Edit+the+Native+Mobile+Generator+Preferences)

Change the [Native Mobile Generator](https://wiki.genexus.com/commwiki/wiki?14451) Preferences to choose how is your application built.

You can build and run your application in any of the platforms mentioned in the [Offline Applications Requirements](https://wiki.genexus.com/commwiki/wiki?22259) document.  
However, in this example, it is shown how to build your offline application for an [Android](https://wiki.genexus.com/commwiki/wiki?14453) device. In order to follow this sample, edit the Native Mobile Generator Preferences like in the image below:

* Generate Android: True (default)
* Generate iOS: False
* Main Platform: Android
* Android SDK directory: Select your Android SDK directory (which is: the directory where you have installed the program)
* JDK Directory: Select your JDK directory.

`[imagen omitida: wiki id 32444]`

**Important note**: Because the [Offline Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?22237) are fully generated in native code, the applications must be compiled and installed on Devices or Simulators of the corresponding platforms. This means that the [KBN](https://wiki.genexus.com/commwiki/wiki?18653) application does not work with [Offline applications](https://wiki.genexus.com/commwiki/wiki?22237).

### [Step 8: Deploy your application to the cloud (Optional)](#Step+8%3A+Deploy+your+application+to+the+cloud+%28Optional%29)

If your computer and the Device are not on the same network, and/or you prefer a simpler solution for wireless prototyping, you can **[deploy your app to the cloud](https://wiki.genexus.com/commwiki/wiki?18250)** (this option is recommended for your first deploy). To do this, go to the Generator properties, and set the value "Yes" to the "Deploy to cloud" property, as shown below:

`[imagen omitida: wiki id 32445]`

### [Step 9: Build your application](#Step+9%3A+Build+your+application)

Press **F8** to call the "build all" command and build the entire application. This step is **necessary**, at least for the first time you build your application.

**Note**: If you have skipped the Step 8, as it is the first time you build the application, GeneXus needs to know the database connection information.

The following output is shown, as well as the [Impact Analysis](https://wiki.genexus.com/commwiki/wiki?31023), indicating which tables must be created on the database. Click on the "Create" button in order to create them.

`[imagen omitida: wiki id 32446]`

Once the Menu object called "Menu" is built, a new object appears right below the Menu: it is the [Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509). This object is in charge of selecting which tables are being created in the local database of the device once the application is installed, as also this object properties can manage how is the [Data Synchronization](https://wiki.genexus.com/commwiki/wiki?22269) done, among other features.

In the build process, after the [Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509) appears, the [Offline Database Object Navigation Report](https://wiki.genexus.com/commwiki/wiki?23568) is shown, giving to you all the related information about the tables which are going to be synchronized in the device with respect to the server.

`[imagen omitida: wiki id 32447]`

### [Step 10: Run your application!](#Step+10%3A+Run+your+application%21)

Once the "build all" process finishes, to run your application in your Android Device or Android Emulator, first right-click the "Menu" [Menu object](https://wiki.genexus.com/commwiki/wiki?16321) and set it as the [Startup Object](https://wiki.genexus.com/commwiki/wiki?5393).

Finally, press **F5** and the application is going to be installed in the Android Device or Android Emulator. This depends on whether the Android Device is plugged into the computer or not.

### [How does this application work?](#How+does+this+application+work%3F)

As mentioned at the beginning of this document, this application uses a local database in order to work. This means that all data the application uses is from the local database. In addition, all insertions, deletions, and updates are made in the local database.

The first time the application is installed, the local database is created inside the Device. After that, a reception synchronization process is executed in order to receive all data from the server and store that data into the device. Once both, the device and the server, are synchronized, you are free to use the application either the device has connected to the internet or not.

#### [But what happens if data is modified while the device is connected to the internet?](#But+what+happens+if+data+is+modified+while+the+device+is+connected+to+the+internet%3F)

The device always applies changes in the local database, but at the same time, it inserts events that represent those modifications into an auxiliary table in the local database. After that, and because the [Send Changes property](https://wiki.genexus.com/commwiki/wiki?23392,,) of the [Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509) is set to "When connected" by default, the device sends those events to the server via REST services in order to apply the same changes in the server-side.

#### [And what happens if data is modified while the device is disconnected from the internet?](#And+what+happens+if+data+is+modified+while+the+device+is+disconnected+from+the+internet%3F)

Like when the device is indeed connected, every modification is inserted as an event in the auxiliary table in the local database. But because the device has no connection to the internet, it keeps stacking all events into that auxiliary table. All these events are sent to the server once the device is again connected, and another modification is made, or next time the application starts again.

#### [When does the device receive modifications made in the server?](#When+does+the+device+receive+modifications+made+in+the+server%3F)

By default, the device receives data from the server every time it starts up. However, this behavior can be customized by changing the [Data Receive Criteria property](https://wiki.genexus.com/commwiki/wiki?22223) from the [Offline Database Object properties](https://wiki.genexus.com/commwiki/wiki?25196).

#### [Keep learning](#Keep+learning)

You can learn more about how synchronization works by reading the [Automatic Offline Data Synchronization](https://wiki.genexus.com/commwiki/wiki?22267) document and the [Data Synchronization](https://wiki.genexus.com/commwiki/wiki?22269) document for more advanced concepts.

### [What is next](#What+is+next)

The first recommendation is to read the whole Table of Contents of the [Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22228), paying special attention to the [Offline Native Mobile applications architecture](https://wiki.genexus.com/commwiki/wiki?22221) and the [Offline Native Mobile Applications Generation](https://wiki.genexus.com/commwiki/wiki?22262) documents.

After that, you can try to create a new Knowledge Base from some of the Offline applications samples:

* [Sales](https://wiki.genexus.com/commwiki/wiki?23672) (Available in GeneXus Start Page)
* [Survey](https://wiki.genexus.com/commwiki/wiki?24355,,)
* [EventDay](https://wiki.genexus.com/commwiki/wiki?22550,,) using the Offline branch
* [Sales with manual synch example](https://wiki.genexus.com/commwiki/wiki?20698,,) for manual synchronization

Or if you already have an online application and you want to convert it into Offline, please read the [HowTo: Convert online applications into offline applications](https://wiki.genexus.com/commwiki/wiki?24591) document to get started.

### [Considerations](#Considerations)

* The offline local database, which is inside the device or emulator, is not reorganized. Therefore, if you make any change to the data model which affects the offline application database, the application re-creates the database, loosing all stored data ( with exception of Pending Events: see the [Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509)).
* Most of the times, starting by developing a simple Online application might be easier and faster to prototype. Once it is ready, you are free to [convert your application from Online to Offline](https://wiki.genexus.com/commwiki/wiki?24591).
* This sample application uses autonumbered primary keys, but not by setting its [Autonumber property](https://wiki.genexus.com/commwiki/wiki?6798)=Yes. On the other hand, primary keys are defined based on the [GUID data type](https://wiki.genexus.com/commwiki/wiki?31772) (with Autogenerate) in order to avoid possible conflicts on the server-side when sending changes. To learn more about this, please read the [Automatically generated identifiers synching conflicts](https://wiki.genexus.com/commwiki/wiki?23543) article.

### [Troubleshooting](#Troubleshooting)

See the [Offline Native Mobile Applications Common Issues](https://wiki.genexus.com/commwiki/wiki?20287)

### [Download the XPZ](#Download+the+XPZ)

[My First Offline Model](https://wiki.genexus.com/commwiki/wiki?25372,,)

### [See Also](#See+Also)

* [Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22228)
* [Offline Native Mobile Applications Scenarios](https://wiki.genexus.com/commwiki/wiki?22507)
* [Data Synchronization](https://wiki.genexus.com/commwiki/wiki?22269)
* [HowTo: Use the Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?23558)
* [HowTo: Convert online applications into offline applications](https://wiki.genexus.com/commwiki/wiki?24591)


|  |
| --- |
| **Backlinks** |
| [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Toc:Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22228) |

---
