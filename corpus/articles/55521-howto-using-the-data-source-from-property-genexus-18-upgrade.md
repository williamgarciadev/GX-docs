---
title: "HowTo: Using the Data Source From property (GeneXus 18 Upgrade 4 or prior)"
source_id: 55521
source_url: https://wiki.genexus.com/commwiki/wiki?55521
genexus_version: "18"
---

# HowTo: Using the Data Source From property (GeneXus 18 Upgrade 4 or prior)

It is common to find dynamic controls such as Combo Boxes or Wheels in web applications and Native Mobile applications. These controls restrict user data input dynamically, allowing to define the data source in an easy and reusable way.

Genexus simplifies this by allowing to configure at the design stage the data source (either Attributes or [Data Providers](https://wiki.genexus.com/commwiki/wiki?5270)) for controls such as [Dynamic Combo Box](https://wiki.genexus.com/commwiki/wiki?7598), [Dynamic List Box](https://wiki.genexus.com/commwiki/wiki?7599) or [Wheel Control for Native Mobile apps](https://wiki.genexus.com/commwiki/wiki?20180).

This article explains how to apply dynamic controls using the [Data Source From property](https://wiki.genexus.com/commwiki/wiki?55489).

Consider an application called [LightCRM](https://wiki.genexus.com/commwiki/wiki?22592,,), which enables users to schedule Meetings with a certain Contact of a Company. To schedule a new meeting, among other things, you have to indicate the Company name as well as that of the Contact with whom the meeting will be held. Suppose you want, on the Web and in a Native Mobile application, to display a [Dynamic Combo Box](https://wiki.genexus.com/commwiki/wiki?7598) with a Company’s Contacts which should be ordered by birth date.

To do so, you need to use [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) as data source for the controls to be used. Then, follow the steps below.

### [1. Create a SDT](#1.+Create+a+SDT)

First, create a [Structured Data Type](https://wiki.genexus.com/commwiki/wiki?10021) object and name it “ContactsSDT”.

`[imagen omitida: wiki id 22984]`

### [2. Create a Data Provider](#2.+Create+a+Data+Provider)

Next, create a Data Provider and name it "GetContactsByBirthday". Drag the ContactsSDT object to the Source Panel of this DataProvider.

`[imagen omitida: wiki id 22985]`

Change the Source of the "GetContactsByBirthday" object as shown below:

```
ContactsSDT
{
    ContactsSDTItem
    order ContactBirthday
    {
        ContactId  = ContactId
        ContactName = ContactName
    }
}
```

Add the following rule to the Rules section:

```
Parm(CompanyID);
```

### [3. Set the properties](#3.+Set+the+properties)

At this point you can choose to configure for web applications or Native Mobile applications.

#### [Web applications](#Web+applications)

Change the [Web Panel Web Layout](https://wiki.genexus.com/commwiki/wiki?8132) of the Meeting [Transaction](https://wiki.genexus.com/commwiki/wiki?1908) and set the properties of the ContactID attribute as shown in the image below:

`[imagen omitida: wiki id 22986]`

To test it, select Run on the [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) object called "Home", go to Meetings and create a new record by clicking on the Insert button.

`[imagen omitida: wiki id 22987]`

#### [Native Mobile applications](#Native+Mobile+applications)

Just like on the web, to test it, open the "WorkWithDevicesMeeting" object and change the Edit layout on the "Section(General)" level and the properties of the ContactID attribute as shown in the image below:

`[imagen omitida: wiki id 22994]`

**Note:** If "WorkWithDevicesMeeting" is configured with another Layout of Edit type, the same changes have to be made if you want to show the same features in all platforms.

Lastly, run the "LightCRM" [Menu object](https://wiki.genexus.com/commwiki/wiki?54116,,) on a device and test it by adding a new Meeting record.

`[imagen omitida: wiki id 22995]`

### [Considerations](#Considerations)

* When using the Data Providers option, parameters can be used for Data Providers by setting the “Parameters” property that is displayed after selecting this option.
* On selecting a Data Provider, the first numeric attribute and the first descriptor attribute of the SDT returned by the Data Provider are automatically selected.
* For Native Mobile applications, the Wheel control can be used with the same settings as for the Dynamic Combo Box control.

### [See Also](#See+Also)

[Data Source From property](https://wiki.genexus.com/commwiki/wiki?22945)  
[Dynamic Combo Box and Dynamic List Box Properties in Web Forms](https://wiki.genexus.com/commwiki/wiki?8740)  
[HowTo: Use the Dynamic Combo Box Control for Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?16778)  
[Wheel Control for Native Mobile apps](https://wiki.genexus.com/commwiki/wiki?20180)
