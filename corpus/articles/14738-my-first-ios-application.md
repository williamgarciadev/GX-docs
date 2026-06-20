---
title: "My first iOS application"
source_id: 14738
source_url: https://wiki.genexus.com/commwiki/wiki?14738
genexus_version: "18"
---

# My first iOS application

This document is a step by step explanation of how to create a simple native iOS application with GeneXus.

In this sample, the application connects to REST services in Java that persists data on MySQL. If you are using another generator (e.g. .NET) or DBMS the steps are the same but the prerequisites change.

**Before** starting with the tutorial please check that the [prerequisites](https://wiki.genexus.com/commwiki/wiki?14974) are correctly installed. See [Apple platform article](https://wiki.genexus.com/commwiki/wiki?14917) for more information.

### [**Step 1**](#Step+1)

Open GeneXus and create a [New Knowledge Base](https://wiki.genexus.com/commwiki/wiki?9596). Select Ruby as the Prototyping Environment.

`[imagen omitida: wiki id 37363]`

### [**Step 2**](#Step+2)

Create a Customer and Company Transaction with the following structure:

`[imagen omitida: wiki id 37362]`

Please **note** that [predefined domains](https://wiki.genexus.com/commwiki/wiki?14610) were used for certain attributes and, in both cases, be sure to set as True the [Autonumber property](https://wiki.genexus.com/commwiki/wiki?6798) of each identifier attribute (i.e.: positioned on the CustomerId field, press F4 to see its properties, and change the Autonumber property. Do the same for the CountryId attribute).

### [**Step 3**](#Step+3)

[Apply Work With for Smart Devices pattern](https://wiki.genexus.com/commwiki/wiki?15975) to both transactions (e.g.: open each transaction, click on **Patterns** selector, choose **Work With for Smart Devices** tab, and check the checkbox as shown below. Then, save):

`[imagen omitida: wiki id 35470]`

From the Toolbox, drag & drop the control **Attribute/variable** in order to insert attributes you want to see on the Customer list screen (e.g.: CustomerEmail):

`[imagen omitida: wiki id 35471]`

To remove the attribute label, change the **Label position** property, to "None" value:

`[imagen omitida: wiki id 35472]`

### [**Step 4**](#Step+4)

Create a [Menu for Smart Devices object](https://wiki.genexus.com/commwiki/wiki?46149,,) called Menu.

`[imagen omitida: wiki id 14560]`

This object is like a menu; you can use it to call the Work With objects created in the previous Steps. To do it: right click in the **Items** option to add actions to the Dashboard. You must select the WorkWithDevices<*TransactionName>* objects in the [Select Object dialog](https://wiki.genexus.com/commwiki/wiki?9889):

`[imagen omitida: wiki id 35475]`

When you select a WorkWithDevices<*TransactionName*> object, the Event associated with this action will be generated automatically:

```
Event 'WorkWithDevicesCustomer'
     WorkWithDevicesCustomer.Customer.List()
EndEvent

Event 'WorkWithDevicesCompany'
     WorkWithDevicesCompany.Company.List()
EndEvent
```

### [**Step 5**](#Step+5)

Edit the SmartDevices Generator Preferences. Set the following properties:

|  |  |
| --- | --- |
| **[Generate Android property](https://wiki.genexus.com/commwiki/wiki?18654)** | False |
| **[Generate Apple property](https://wiki.genexus.com/commwiki/wiki?18656)** | **True** |
| **[Main Platform property](https://wiki.genexus.com/commwiki/wiki?18657)** | iOS |
| **[Execution Type property](https://wiki.genexus.com/commwiki/wiki?18658)** | **Knowledge Base Navigator (Device)**  Now, download and install GeneXus [KBN](https://wiki.genexus.com/commwiki/wiki?18653) into your iOS device, which is a kind of browser that lets you execute your GeneXus application. |
| **Execution Device property** | You have to choose in which of your registered devices the prototyping is going to be done. If you have not logged in yet, you will be asked to do it. After that, the following window opens, so you can choose the device: |

### 

### [**Step 6**](#Step+6)

Press **F5** to build the application. At the first time, you do this GeneXus needs to know the database connection information.

`[imagen omitida: wiki id 37365]`

If your computer and the Device are not in the same network (viewing each other), and/or you prefer a simpler solution for wireless prototyping, you could  **[deploy to cloud](https://wiki.genexus.com/commwiki/wiki?18250)** (we recommend that option for your first develop). For that, press Cancel on the window, and go to Preferences, setting Yes for the "Deploy to cloud" property, as shown below:

`[imagen omitida: wiki id 37366]`

The following output is shown, as well as the Impact Analysis report, indicating the tables that must be created on the database. Click on Create button in order to actually create them.

`[imagen omitida: wiki id 37360]`

After executing the web application on your computer, a Notification will appear on your device (in this case iPad), that will automatically take you to the KBN. On this screen, you can see the URL (or you can introduce a URL shortcut(\*1)) where it is deployed and underneath you have to select which application you want to execute. Then, enter to your application.

`[imagen omitida: wiki id 37367]`

Enjoy!

## [Notes](#Notes)

(\*1)  Available since GeneXus Evolution 3 Upgrade 7

## [Download the XPZ](#Download+the+XPZ)

To import GeneXus objects used in this demo, right on your [KB](https://wiki.genexus.com/commwiki/wiki?2428), download the following file: [My First Smart Device Application](https://wiki.genexus.com/commwiki/wiki?37477,,).

## [See also](#See+also)

* [My first Android application](https://wiki.genexus.com/commwiki/wiki?14555)

For more information check [Apple - FAQ and Common Issues](https://wiki.genexus.com/commwiki/wiki?14925,,)


|  |
| --- |
| **Backlinks** |
| [Category:Apple platform](https://wiki.genexus.com/commwiki/wiki?14917) | [Input View Appearance property](https://wiki.genexus.com/commwiki/wiki?37783) | [My first Android application](https://wiki.genexus.com/commwiki/wiki?14555) |
| [My first BPM Native Mobile application](https://wiki.genexus.com/commwiki/wiki?50516) | [My first Theme object](https://wiki.genexus.com/commwiki/wiki?16237) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |
| [Welcome to Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?18321) |

---
