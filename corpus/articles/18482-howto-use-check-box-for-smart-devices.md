---
title: "HowTo: Use Check Box for Smart Devices"
source_id: 18482
source_url: https://wiki.genexus.com/commwiki/wiki?18482
genexus_version: "18"
---

# HowTo: Use Check Box for Smart Devices

Check Box is a control applied for Win, Web and SD applications. It is used to show two possible values for a variable or attribute, in a checked-unchecked way.

This tutorial explains how to use a Check Box in Smart Devices, with a simple example.

### [**Properties**](#Properties)

|  |  |
| --- | --- |
| [Auto Grow](https://wiki.genexus.com/commwiki/wiki?20204) | If this property is true, then the field will adjust the length of the attribute. |
| [ControlTitle](https://wiki.genexus.com/commwiki/wiki?8736) | Used to define a title to the control. |
| [CheckedValue](https://wiki.genexus.com/commwiki/wiki?8734) | This property defines the value that will be used when the Check Box is checked. |
| **UncheckedValue** | This property defines the value that will be used when the Check Box is unchecked. |

### [Samples](#Samples)

**Example 1**

For this example, a [domain](https://wiki.genexus.com/commwiki/wiki?7221) called "EnumBool" will be defined as follows:

`[imagen omitida: wiki id 32742]`

The definiton of the values in the domain is made in the [Enum Values property](https://wiki.genexus.com/commwiki/wiki?7379), as shown in the next image:

`[imagen omitida: wiki id 32743]`

In the images above you can see that the properties Checked and Unchecked have been set to coincide with the default, but it could be set as you want.

The transaction to be used for this example is the next one, with the Work With for Smart Devices pattern applied (see [Applying Work With Pattern](https://wiki.genexus.com/commwiki/wiki?15975)).

`[imagen omitida: wiki id 32744]`

Take a look at the properties of the CheckBoxTRNCheckBoolean:

`[imagen omitida: wiki id 32745]`

All done! All you have to do now is hit F5 and see the results.

**Snapshot -**

[**Android**](https://wiki.genexus.com/commwiki/wiki?14453)

`[imagen omitida: wiki id 32746]`
