---
title: "Create Knowledge Base from GeneXus Server"
source_id: 22416
source_url: https://wiki.genexus.com/commwiki/wiki?22416
genexus_version: "18"
---

# Create Knowledge Base from GeneXus Server

The ***Knowledge Base from GeneXus Server*** option is the first operation you have to complete in order to subscribe to a [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) hosted in a [GeneXus Server](https://wiki.genexus.com/commwiki/wiki?9911) instance.

It's located under the *File > New* menu in the GeneXus IDE.

`[imagen omitida: wiki id 31888]`

### [Step by step](#Step+by+step)

1) Select the ***Knowledge Base from GeneXus Server*** optionfrom the *File>New*menu. The following prompt will be shown:  
`[imagen omitida: wiki id 31889]`  
  
2) If you know the Knowledge Base URL then you just have to write it in ***Server KB URL*** and continue with the following step. Otherwise, click ***Select Server KB*** to select the Server's Knowledge Basefrom a list of available GeneXus Servers

After clicking the ***Select Server KB*** option, a new window will be prompted to select the GeneXus Server Instance from the *Servers* list. Open and Sandbox instances are listed by default:  
`[imagen omitida: wiki id 31890]`  
  
The wanted Server must be chosen. If the GeneXus Server instance isn’t listed, to add it to the list the ***Add New Server*** option must be selected:  
`[imagen omitida: wiki id 31891]`

Write all the required information:

* **URL**: The [GeneXus Server URL](https://wiki.genexus.com/commwiki/wiki?21104) to connect.
* **Friendly Name**: Name that will be used in the Server's list for the instance.
* **Authentication Type:** Corresponding [Authentication Type](https://wiki.genexus.com/commwiki/wiki?21107).
* **Username:** GeneXus Account or Local username.
* **Password**: GeneXus Account or Local password.

Click ***Check Connection***to test the Server's connection (using the selected username and password) and click OK to add the GeneXus Server instance to the Servers list.  
  
**Note**: The username and password can be remembered using the ***Save Password*** CheckBox. If the ***Save Password*** checkbox isn't enabled, the next time you want to connect to the GeneXus Server an authentication dialog will be displayed:  
`[imagen omitida: wiki id 31892]`

3) Once you are connected to a GeneXus Server Instance, a list of Knowledge Bases served by this GeneXus Server is displayed in***Knowledge Bases***:  
`[imagen omitida: wiki id 31893]`  
  
Select one Knowledge Base from the list, by double-clicking on it or by clicking and then pressing ***Ok**.*

**Note**: Filter Knowledge Bases using the search box located above the list, for easy and fast Knowledge Base searching. This is especially useful to create a Knowledge Base from a GeneXus Server Instance populated with several Knowledge Bases.

4) After a Knowledge Base has been selected, the Version(s) must be chosen. You can choose to import only the ***Trunk version**,* to import ***All versions***, or to import a custom set of ***Selected versions***.  
`[imagen omitida: wiki id 31894]`  
  
Select all the [Development Versions](https://wiki.genexus.com/commwiki/wiki?5684) and/or [Frozen Versions](https://wiki.genexus.com/commwiki/wiki?5681) from that Knowledge Base.  
  
**Note**: To choose a custom set of Versions select ***Selected Versions*** on the radio button and then click the "..." button. A dialog will be displayed:  
`[imagen omitida: wiki id 31895]`

Check all the versions to import (if more than one Version is selected a Minimum Spanning Tree will be automatically selected). Notice that filters can be applied by using the search box located above the list.

5) Once the Versions are selected set ***Name*** and ***Path*** of the Knowledge Base and click the ***Create*** button.  
  
**Note**: Use ***Advanced Setting*** to configure Knowledge Base storage properties.

Next, a progress bar will be displayed showing the three steps involved in the creation of a KB:

Once all steps have been completed, the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) created will be an exact copy of the Knowledge Base hosted in the [GeneXus Server](https://wiki.genexus.com/commwiki/wiki?9911). After this process, the connection to [GeneXus Server](https://wiki.genexus.com/commwiki/wiki?9911) is dropped and you are ready to work off-line.  
  
Note that the [Team Development node](https://wiki.genexus.com/commwiki/wiki?20902) located under the [Preferences](https://wiki.genexus.com/commwiki/wiki?7109) has been updated.

#### [See also](#See+also)

[Send Knowledge Base to GeneXus Server](https://wiki.genexus.com/commwiki/wiki?10215)


|  |
| --- |
| **Backlinks** |
| [Commit to GeneXus Server](https://wiki.genexus.com/commwiki/wiki?10626) | [Defining versions for each application release](https://wiki.genexus.com/commwiki/wiki?20945) |
| [KB:FestivalTickets - High Scalability Sample](https://wiki.genexus.com/commwiki/wiki?51266) | [KB:FestivalTickets - High Scalability Sample (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54299) | [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) |
|
| [KB:PlantCare - ECommerce Sample](https://wiki.genexus.com/commwiki/wiki?50476) |
| [KB:PlantCare and SweetWorld - ECommerce Sample (GeneXus 18 Upgrade 3)](https://wiki.genexus.com/commwiki/wiki?56139) | [Send Knowledge Base to GeneXus Server](https://wiki.genexus.com/commwiki/wiki?10215) | [Category:Team Development with GeneXus Server](https://wiki.genexus.com/commwiki/wiki?9297) | [KB:WanderNest - Online Booking Sample](https://wiki.genexus.com/commwiki/wiki?55028) |

---
