---
title: "My first Android application"
source_id: 14555
source_url: https://wiki.genexus.com/commwiki/wiki?14555
genexus_version: "18"
---

# My first Android application

This document is a step-by-step explanation of how to create a simple **Android** application with GeneXus using [.NET](https://wiki.genexus.com/commwiki/wiki?2892) and SQLServer. If you are using another generator (Java) or DBMS, the steps are the same even though the prerequisites change.

Before starting the following steps, please check that the [Android Requirements](https://wiki.genexus.com/commwiki/wiki?14449) are correctly installed. See [Android platform](https://wiki.genexus.com/commwiki/wiki?14453) for more information.


**Step 1**

Create a [New Knowledge Base](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?9596,,) and select .NET as Prototyping Environment (you can also select Java).

`[imagen omitida: wiki id 51695]`

#### [**Step 2**](#Step+2)

Create the Customer and Company [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,)s with the following structures:

`[imagen omitida: wiki id 37362]`

Note the [Domains with Special Semantics](https://wiki.genexus.com/commwiki/wiki?14610) in Phone, Email, Address attributes.

Next, auto-number the identifier attributes. While positioned in the CustomerId field, go to the Properties window and change the [Autonumber property](https://wiki.genexus.com/commwiki/wiki?6798) to True. Do the same for the CompanyId attribute.

#### [**Step 3**](#Step+3)

[Apply the Work With pattern](https://wiki.genexus.com/commwiki/wiki?15975) to both Transactions. To do so, open each Transaction, click on the **Patterns** selector, choose the **Work With** tab, and select the "Apply this pattern on save" checkbox as shown below. Next, click on Save:

`[imagen omitida: wiki id 59843]`

From the Toolbox, drag the control **Attribute/variable** to insert the attributes you want to see on the Customer list screen (i.e., CustomerEmail):

`[imagen omitida: wiki id 59844]`

To remove the attribute label, change the **Label position** property value to "None":

`[imagen omitida: wiki id 59845]`

`[imagen omitida: wiki id 59846]`

**Step 4**

Create a [Menu object](https://wiki.genexus.com/commwiki/wiki?16321) called, for example, Menu.

`[imagen omitida: wiki id 14560]`

This object is like a menu that you can use to add items/actions in order to call the Work With objects created in the previous step. To do so, right-click on the **Items** option and add two consecutive actions to the Menu. Each **action** must be associated with each Work With. You will be able to select the WorkWithCustomer in the [Select Objects dialog](https://wiki.genexus.com/commwiki/wiki?9889) for the first action and the WorkWithCompany for the second action:

`[imagen omitida: wiki id 59847]`

When you select a WorkWith *<TransactionName>* object, the Event associated with this action will be generated automatically:

```
Event 'WorkWithCustomer'
     WorkWithCustomer.Customer.List()
EndEvent

Event 'WorkWithCompany'
     WorkWithCompany.Company.List()
EndEvent
```

#### [**Step 5**](#Step+5)

Edit the Native Mobile Generator Preferences. Make sure you have set the following properties:

* [Generate Android](https://wiki.genexus.com/commwiki/wiki?18654): True
* [Main Platform](https://wiki.genexus.com/commwiki/wiki?18657): Android (default)
* [Android SDK directory](https://wiki.genexus.com/commwiki/wiki?36361): Select your Android SDK directory (that is, the directory where you have installed the program)
* [JDK Directory](https://wiki.genexus.com/commwiki/wiki?36362): Select your JDK directory.

`[imagen omitida: wiki id 59850]`

With these settings, the Android and iOS code will be generated. In addition, the Android platform application will be executed at runtime.

#### [**Step 6**](#Step+6)

Before pressing **F5** to build and run the application, you have to set a [Main](https://wiki.genexus.com/commwiki/wiki?5770) object as [Startup Object](https://wiki.genexus.com/commwiki/wiki?5394). Menus by default are Main (their Main Object property is set to True by default), so set the Menu as Startup Object:

`[imagen omitida: wiki id 59851]`

Next, press **F5.**The first time you do it, GeneXus needs to know the database connection information.

`[imagen omitida: wiki id 37361]`

The other option is to [deploy to cloud](https://wiki.genexus.com/commwiki/wiki?18250).

The following output is shown, as well as the Impact Analysis report, indicating the tables that must be created in the database. Click on the **Create** button to create them.

`[imagen omitida: wiki id 37360]`

Then, GeneXus automatically runs the Android Emulator:

`[imagen omitida: wiki id 35478]`

You are now ready to test it!

To do so, tap on the Work With Customer option. The following screen will be displayed:

`[imagen omitida: wiki id 35515]`

Continue testing the application by inserting data and updating, deleting, searching, filtering, adding companies, etc.

#### [**Some Pics**](#Some+Pics)

`[imagen omitida: wiki id 14576]`

Enjoy it!

## [Note](#Note+)

To display the desired image for each menu action, go to the Menu object created in step 4. Then, while positioned on each action, associate the image (inserting it simultaneously in the [KB](https://wiki.genexus.com/commwiki/wiki?2428)) through the properties dialog:

`[imagen omitida: wiki id 22813]`

## [Tips](#Tips)

* To simplify the prototyping process, we recommend not closing the emulator between runs.

## [Download the XPZ](#Download+the+XPZ)

To import GeneXus objects used in this demo, right on your KB, download [this file](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?37477,,).

## [Videos](#Videos)

[First steps with a native mobile app](https://training.genexus.com/en/learning/courses/genexus-for-mobile/v18/course-genexus-for-mobile-genexus-18/26080/first-steps-with-a-native-mobile-app)

## [See also](#See+also)

* [My first iOS application](https://wiki.genexus.com/commwiki/wiki?14738)
* A more attractive sample: [LightCRM](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?22592,,)

For more information, check [Apple - FAQ and Common Issues](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?14925,,)

---

|  |
| --- |
| **Backlinks** |
| [Category:Android platform](https://wiki.genexus.com/commwiki/wiki?14453) | [Header property (Menu object)](https://wiki.genexus.com/commwiki/wiki?38239) |
| [My first BPM Native Mobile application](https://wiki.genexus.com/commwiki/wiki?50516) | [My first iOS application](https://wiki.genexus.com/commwiki/wiki?14738) | [My first Native Mobile application with GAM](https://wiki.genexus.com/commwiki/wiki?15275) | [My first Theme object](https://wiki.genexus.com/commwiki/wiki?16237) |
| [Table of contents:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Welcome to Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?18321) |

---
