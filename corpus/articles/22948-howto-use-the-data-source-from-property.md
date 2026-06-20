---
title: "HowTo: Use the Data Source From property"
source_id: 22948
source_url: https://wiki.genexus.com/commwiki/wiki?22948
genexus_version: "18"
---

# HowTo: Use the Data Source From property

It is common to find dynamic controls such as Combo Boxes or Wheels in web applications and native mobile applications. These controls restrict user data input dynamically and allow defining the data source in an easy and reusable way.

GeneXus simplifies this by making it possible to configure the data source (either Attributes or [Data Providers](https://wiki.genexus.com/commwiki/wiki?5270)) at the design stage for controls such as [Dynamic Combo Box](https://wiki.genexus.com/commwiki/wiki?7598), [Dynamic List Box](https://wiki.genexus.com/commwiki/wiki?7599), [Wheel Control for Native Mobile apps](https://wiki.genexus.com/commwiki/wiki?20180) or Edit.

This article explains how to apply dynamic controls using the [Data Source From property](https://wiki.genexus.com/commwiki/wiki?22945). To learn how to use it when it is configured as "Data Provider" and the [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) is "Edit", see [Edit with Suggest](https://wiki.genexus.com/commwiki/wiki?55531).

Consider an application called [LightCRM](https://wiki.genexus.com/commwiki/wiki?22592,,), which enables end end users to schedule Meetings with a certain Contact of a Company. To schedule a new meeting, among other things, the Company name must be indicated as well as the Contact with whom the meeting will be held. Suppose you want to display, on the web or native mobile application, a [Dynamic Combo Box](https://wiki.genexus.com/commwiki/wiki?7598) with the Company’s Contacts which should be ordered by birth date.

To solve this requirement, you need to use the [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) as the data source for the controls to be used. Then, follow the steps below:

### [1. Create an SDT](#1.+Create+an+SDT)

First, create a [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021) and name it “ContactsSDT”.

Indicate the SDT is a collection by selecting the Is Collection checkbox, and define the ContactId and ContactName members as follows:

`[imagen omitida: wiki id 55522]`

### [2. Create a Data Provider](#2.+Create+a+Data+Provider)

Create a Data Provider object and name it "GetContactsByBirthday". Drag the ContactsSDT object from the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210) to the Source tab of this Data Provider and edit the Source as shown below:

`[imagen omitida: wiki id 55523]`

Add the following rule to the Rules section of the Data Provider:

```
Parm(CompanyID);
```

**Note**: The ContactBirthday attribute is based on the [Date data type](https://wiki.genexus.com/commwiki/wiki?7373) in the Contact [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908).

### [3. Set the properties](#3.+Set+the+properties)

This feature can be used both for web applications and native mobile applications.

#### [**Web applications**](#Web+applications)

Go to the Web Layout of the Meeting [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908).

* Set the following for the CompanyId attribute:
  + [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) = Dynamic Combo Box
  + [Data Source From property](https://wiki.genexus.com/commwiki/wiki?22945) = **Attributes**
  + [Item Values property](https://wiki.genexus.com/commwiki/wiki?8808) = CompanyId
  + [Item Descriptions property](https://wiki.genexus.com/commwiki/wiki?8807) = CompanyName
* Set the following for the ContactID attribute:
  + [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) = Dynamic Combo Box
  + [Data Source From property](https://wiki.genexus.com/commwiki/wiki?22945) = **Data Provider**
  + [Data Provider property](https://wiki.genexus.com/commwiki/wiki?56081) = GetContactsByBirthday
  + [Parameters property](https://wiki.genexus.com/commwiki/wiki?8815) = CompanyID
  + [Item Values property](https://wiki.genexus.com/commwiki/wiki?8808) = ContactId
  + [Item Descriptions property](https://wiki.genexus.com/commwiki/wiki?8807) = ContactName
  + [Sort Descriptions Property](https://wiki.genexus.com/commwiki/wiki?8839) = False

The following image shows the detailed configuration of the properties:

`[imagen omitida: wiki id 55524]`

Next, run the [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) called "Home", select the Work With Meetings object, and click on the Insert button to create a new Meeting.

The image below shows the result of the configurations.

`[imagen omitida: wiki id 55525]`

#### [**Native mobile applications**](#Native+mobile+applications)

Open the "WorkWithMeeting" object and go to Section(General). In the Layout, click on the ContactID attribute and set the same properties that were previously set for the web version, as shown in the following image:

`[imagen omitida: wiki id 55527]`

**Note**: If "WorkWithMeeting" is configured with another Layout of Edit type, the same changes have to be made if you want to show the same features in all platforms.

Finally, run the "LightCRM" [Menu object](https://wiki.genexus.com/commwiki/wiki?16321) and add a new Meeting record.

`[imagen omitida: wiki id 55529]`

### [Considerations](#Considerations)

* When the [Data Source From property](https://wiki.genexus.com/commwiki/wiki?22945) is set to **Data Provider**:
  + Parameters can be sent to it by setting the [Parameters property](https://wiki.genexus.com/commwiki/wiki?8815) that is displayed after selecting this option.
  + The first numeric member and the first descriptor member of the SDT returned by the Data Provider are automatically assigned to the [Item Values property](https://wiki.genexus.com/commwiki/wiki?8808) and the [Item Descriptions property](https://wiki.genexus.com/commwiki/wiki?8807) respectively.
* For native mobile applications, the Wheel control can be used with the same settings as for the Dynamic Combo Box control.

### [See Also](#See+Also)

[Data Source From property](https://wiki.genexus.com/commwiki/wiki?22945)  
[Dynamic Combo Box and Dynamic List Box Properties in Web Forms](https://wiki.genexus.com/commwiki/wiki?8740)  
[HowTo: Use the Dynamic Combo Box Control for Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?16778)  
[Wheel Control for Native Mobile apps](https://wiki.genexus.com/commwiki/wiki?20180)  
[Edit with Suggest](https://wiki.genexus.com/commwiki/wiki?55531)


|  |
| --- |
| **Backlinks** |
| [Data Provider property in Attributes/Variables](https://wiki.genexus.com/commwiki/wiki?56081) | [Data Source From property](https://wiki.genexus.com/commwiki/wiki?22945) | [Data Source From property (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55489) |
| [HowTo: Using the Data Source From property (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55521) |

---
