---
title: "HowTo: Create a Super App on the Mini App Center"
source_id: 53316
source_url: https://wiki.genexus.com/commwiki/wiki?53316
genexus_version: "18"
---

# HowTo: Create a Super App on the Mini App Center

To define a new [Super App](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?50900,,), you need to be a **Provisioning Administrator**user and a member with the **Organization Administrator** or **Super App Administrator** role.

To create a new Super App, go to the main menu of the Mini App Center and select **Super Apps** > **NEW SUPPER APP** button**.**

`[imagen omitida: wiki id 56180]`

If the application was developed with GeneXus, the data to be provided is obtained from the Super App KB. On the other hand, if the application was developed with another tool, this data is obtained from the solution used to develop it.

For GeneXus-developed applications, the data to be entered is obtained as follows:

* Super App Id: In the [Super App object](https://wiki.genexus.com/commwiki/wiki?53457), it is the value of the [Super App Identifier property](https://wiki.genexus.com/commwiki/wiki?50308).
* Name: Name or description of the Super App object.
* Enabled: If selected, indicates that the Super App is available.

If you have a **Provisioning Administrator** role, you must also specify:

* Organization: Organization name. The Organization must have permission to create Super Apps.

### [Attribute Configuration in Super Apps](#Attribute+Configuration+in+Super+Apps)

When configuring attributes for Super Apps, it's important to understand that this process is optional. Its primary purpose is to facilitate the use of the GetByFilters feature in the Mini App Center, enabling users to search for Mini Apps based on specific filter criteria.

This added attributes will be utilized for filtering purposes and should be [instantiated with values in the Mini App Version](https://wiki.genexus.com/commwiki/wiki?53318). This ensures that the attributes are meaningful and effectively contribute to the filtering process.

Follow the steps below to configure custom attributes for your Super App:

Log in as a Provisioning Administrator user with an Organization Administrator or Super App Administrator role.

Go to the Super Apps section in the Mini App Center and select the Super App to which you want to add attributes.

`[imagen omitida: wiki id 57949]`

Click on the + ADD ATTRIBUTES button.

`[imagen omitida: wiki id 57950]`

Specify the name, type (Number, Character, or Values), and whether it's required for each attribute.

`[imagen omitida: wiki id 57951]`

Review the list of attributes and make any necessary adjustments.

Next, save your changes. After saving, make sure that all attributes are listed correctly. The result of the addition looks as follows:

`[imagen omitida: wiki id 57952]`

### [Security Configuration in a Super App](#Security+Configuration+in+a+Super+App)

In this guide, you can explore how to add security to your Super App during its creation or modification process.

#### [**Adding security when creating a Super App**](#Adding+security+when+creating+a+Super+App)

When creating a new Super App, ensuring its security is important.  
Follow these steps to add security during the creation process:

First, go to the Super App section in the Mini App Center.  
Click on the NEW SUPER APP button and enter the New Super App information.

`[imagen omitida: wiki id 58020]`

Locate the Security field and set it to True. This step enables the security features for your Super App.

`[imagen omitida: wiki id 58021]`

After configuring the security settings, click on the CONFIRM button to complete the creation process for your Super App. Ensure all other necessary information is provided accurately before finalizing.

#### [**Adding security when modifying a Super App**](#Adding+security+when+modifying+a+Super+App)

Follow these steps to add security when modifying an existing Super App:

First, go to the Super App section in the Mini App Center.  
Click on the name of the Super App you want to modify its security.

`[imagen omitida: wiki id 58022]`

In the Super App information window, locate the Security field and set it to True. This step enables the security features for your Super App.

`[imagen omitida: wiki id 58023]`

**Note:** Currently, the Security field is visible but does not have active functionality. This feature is planned for future upgrades.


|  |
| --- |
| **Backlinks** |
| [HowTo: Create a Super App](https://wiki.genexus.com/commwiki/wiki?50906) | [HowTo: Create a Super App on the Mini App Center (GeneXus 18 Upgrade 9)](https://wiki.genexus.com/commwiki/wiki?57953) | [HowTo: Upload a Mini App version to the Mini App Center](https://wiki.genexus.com/commwiki/wiki?53318) |
| [Table of contents:Mini App Center](https://wiki.genexus.com/commwiki/wiki?51290) | [Provisioning.GetByFilters method](https://wiki.genexus.com/commwiki/wiki?57960) |

---
