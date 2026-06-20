---
title: "Designing the tables related to WWSD Layouts"
source_id: 19487
source_url: https://wiki.genexus.com/commwiki/wiki?19487
genexus_version: "18"
---

# Designing the tables related to WWSD Layouts

When designing the User Interface of a [Native Mobile](https://wiki.genexus.com/commwiki/wiki?14451) application, sometimes different Layouts must be used to encompass the various platforms, modes and orientations.

Layouts designed for applications are made up basically by the data to be displayed and the actions the user can perform. Layouts are designed using tables. Tables have rows, columns and cells, all of them have properties that allow configuring how data is displayed.

For example, when the [WWSD is applied to a Transaction](https://wiki.genexus.com/commwiki/wiki?15975), the Layouts of the [List](https://wiki.genexus.com/commwiki/wiki?15984) and [Detail](https://wiki.genexus.com/commwiki/wiki?15985) nodes are created using tables:

`[imagen omitida: wiki id 19488]`

Tables have, among others, the following properties:

* Column Style
* Row Style
* Width
* Height

These properties allow setting row and column size in order to design the application layouts.

The values for these properties can be expressed in various units:

|  |  |
| --- | --- |
| **Percentage (%)** | Using this unit is similar to designing tables for Web applications. A percentage can be indicated for each one of the columns or rows, and the total sum of all values has to be 100%. |
| **Device Independent Pixel (dip)** | This unit allows working with fixed sizes that in turn depend on the device. For example, 1 dip in Android doesn’t involve the same number of pixels as it does in iOS. |
| **Platform Default (pd)** | This unit means: “Using the best value depending on the platform”. |

`[imagen omitida: wiki id 19489]`

### [Default property values](#Default+property+values)

Thus, some of the above properties will use values in the units we have seen (%, dip, pd), and they can even be combined. For example, the default value of the Column Style property is “64dip; 100%”, which means that the first column will take 64 dips, and the following column will take all the remaining space.

The default property values will vary for each table. For example, the List has two tables: one containing the Grid and another inside the Grid. Their default values are different:

#### [Table containing the Grid](#Table+containing+the+Grid)

`[imagen omitida: wiki id 19490]`

#### [Table inside the Grid](#Table+inside+the+Grid)

`[imagen omitida: wiki id 19491]`

And the same goes for the other tables of the [Detail](https://wiki.genexus.com/commwiki/wiki?15985) and each [WWSD](https://wiki.genexus.com/commwiki/wiki?15974) section.

### [Properties’ “Platform Default” (pd) value](#Properties%E2%80%99+%E2%80%9CPlatform+Default%E2%80%9D+%28pd%29+value)

As mentioned before, applying this value to a property means: “Using the best value depending on the platform”.

In addition to depending on the platform used, this value also depends on what you want to display in a cell.

That is to say, the platform default value varies depending on whether a field has a label or doesn’t have one, or if the field label will be displayed on top or to the left. The same happens when an Edit or View layout is involved.

Below is a list of platform default values for the [Row Style](https://wiki.genexus.com/commwiki/wiki?15984) property of the tables used in [WWSD](https://wiki.genexus.com/commwiki/wiki?15974) Layouts:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Label Position=Top** | | **Label Position=Left** | |
|  | **Mode=View** | **Mode=Edit** | **Mode=View** | **Mode=Edit** |
| **Android** | 64 | 64 | 44 | 50 |
| **iOS** | 53 | 53 | 44 | 53 |
| **iOS 7** | 53 | 53 | 44 | 44 |

The **platform default** value for the [Height](https://wiki.genexus.com/commwiki/wiki?15984) property of the table is calculated according to the value of the Rows Style property.

### [Examples](#Examples)

When running a Smart Device application with default configurations, in this case in the Android emulator, Lists are displayed as shown below:

`[imagen omitida: wiki id 19492]`

Below is the Detail associated with one of the elements:

`[imagen omitida: wiki id 19493]`

For iOS, lists are displayed as shown below:

`[imagen omitida: wiki id 19494]`

Below is the associated Detail:

`[imagen omitida: wiki id 19495]`
