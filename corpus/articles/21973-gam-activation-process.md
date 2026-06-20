---
title: "GAM - Activation Process"
source_id: 21973
source_url: https://wiki.genexus.com/commwiki/wiki?21973
genexus_version: "18"
---

# GAM - Activation Process

When you [activate GAM](https://wiki.genexus.com/commwiki/wiki?19946) in a [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836), the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535) is always imported into it (or updated when a new build or upgrade of GeneXus is installed).

However, importing the [Web Frontend examples](https://wiki.genexus.com/commwiki/wiki?21993) and/or [Mobile examples](https://wiki.genexus.com/commwiki/wiki?21993)​​​​​​​ is optional.

A dialog box is displayed to choose whether to import the optional objects.

##### Figure 1.

Look at the two check boxes that offer the following options:

1. Web Panels

It refers specifically to the objects that are part of the GAM examples. It includes the [Login Object for Web](https://wiki.genexus.com/commwiki/wiki?15590) example and the [Not Authorized Object for Web](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?17551,,) example. These are necessary to start using GAM in web applications. It is checked by default because importing these objects is **highly recommended**.

2. Panels

Examples of [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)s. They are imported to handle login and authorization with Panels. Some of these examples are [GAMSDLogin object](https://wiki.genexus.com/commwiki/wiki?15370), and [GAMSDRegister object](https://wiki.genexus.com/commwiki/wiki?15371). These are necessary to start using GAM in Native Mobile applications or Angular Front End apps. If this option is checked, [Login Object for SD property](https://wiki.genexus.com/commwiki/wiki?16589), [Change Password Object for SD property](https://wiki.genexus.com/commwiki/wiki?20013), and [Not Authorized Object for SD property](https://wiki.genexus.com/commwiki/wiki?20018) are initialized.

You can also configure if you want these examples to be automatically updated when a new build or upgrade of GeneXus is installed, or if you want to be prompted for it. The combo box allows you to indicate how to handle the updates to those examples. The options are as follows:

* Prompt me to update: A dialog box will be displayed when a new version of the examples is found.
* Install updates automatically: The examples will be imported every time a new version is found.
* Never update: No examples will be imported.

### [Changing the settings](#Changing+the+settings)

The options selected in the dialog of figure 1. can be changed from the menu **Tools > GeneXus Access Manager > Installation Settings**.

##### Figure 2.

The update button imports the newly selected option(s) and saves the changes. This is for changing the settings and applying those changes.  
The repair button forces a full import of the GAM API, and all the selected options, not only the new selections.

By using the GAM Settings dialog in a new KB that will be started from [GeneXus Server](https://wiki.genexus.com/commwiki/wiki?9911) from a KB in which GAM is already activated, you have the option to not import the GAM examples.

In a KB where GAM is used only for the web, and you want to start using it for Native Mobile apps, you have the option to apply GAM to the Native Mobile part of the KB using this dialog (import the GAM Native Mobile examples and initialize [Login Object for SD property](https://wiki.genexus.com/commwiki/wiki?16589), [Change Password Object for SD property](https://wiki.genexus.com/commwiki/wiki?20013), and [Not Authorized Object for SD property](https://wiki.genexus.com/commwiki/wiki?20018)).

**Important Note:**

If you get this message in the build process

```
warning: The "Integrated Security Level" version property is set to "Authentication" and there isn't an object configured for "Login Object for Web" property.
```

It means that you didn't select to import the Web frontend objects which includes the Login object and others or you didn't set a Login object in the mentioned property. To solve this, you can follow the same steps explained before in this section.

### [Updating GAM examples](#Updating+GAM+examples)

New GeneXus versions may include updates to [GAM - Examples](https://wiki.genexus.com/commwiki/wiki?21993). If you selected to automatically update GAM examples (see “Prompt me to update”), the following dialog may appear when updates are available.

##### Figure 3. Do you want to continue with update of 'GAM' frontend object?

The dialog box lets you confirm if you want to install the updates or not. Select Yes to install them or No if you do not want to at this time.  
Updates to GAM examples may be manually installed at a later time by importing GAM\_Panels-for-SD.xpz and/or GAM\_Frontend.xpz located in folder \Library\GAM under the GeneXus installation directory.

As stated above, the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535) is not affected by these properties; they are automatically imported every time that a new version is found while the GAM is activated.

### [See Also](#See+Also)

* [GAM Backoffice](https://wiki.genexus.com/commwiki/wiki?15935)
* [GAM repository creation for the first time from GeneXus](https://wiki.genexus.com/commwiki/wiki?29701)


|  |
| --- |
| **Backlinks** |
| [Administrator User Name property](https://wiki.genexus.com/commwiki/wiki?15215) | [Connection User Name property](https://wiki.genexus.com/commwiki/wiki?15217) | [Enable Integrated Security property](https://wiki.genexus.com/commwiki/wiki?14706) |
| [GAM - API for Menus](https://wiki.genexus.com/commwiki/wiki?29742) | [GAM - Getting Started](https://wiki.genexus.com/commwiki/wiki?19946) | [Category:GAM API](https://wiki.genexus.com/commwiki/wiki?16535) | [GAM options in GeneXus toolbar](https://wiki.genexus.com/commwiki/wiki?19947) |
| [GAM repository creation for the first time from GeneXus](https://wiki.genexus.com/commwiki/wiki?29701) | [HowTo: Manage a multi-language application using GAM.](https://wiki.genexus.com/commwiki/wiki?55986) | [Steps to build with GeneXus 18 a KB of GeneXus 17 or prior](https://wiki.genexus.com/commwiki/wiki?52345) |

---
