---
title: "Send Knowledge Base to GeneXus Server"
source_id: 10215
source_url: https://wiki.genexus.com/commwiki/wiki?10215
genexus_version: "18"
---

# Send Knowledge Base to GeneXus Server

The *Send Knowledge Base to Server* operation is used when you have a local Knowledge Base and want to publish it in a [GeneXus Server](https://wiki.genexus.com/commwiki/wiki?9911) instance so it can be served as a [teamworking GeneXus Server](https://wiki.genexus.com/commwiki/wiki?9297) Knowledge Base.

### [Step by step](#Step+by+step)

After creating the local Knowledge Base, the following steps must be executed:

1) Select the ***Send Knowledge Base to Server*** option located under the ***File*** option.

2) A dialog will show up where you must enter the [GeneXus Server url](https://wiki.genexus.com/commwiki/wiki?10657,,) and the Knowledge Base [alias](https://wiki.genexus.com/commwiki/wiki?10659,,). Note: the Knowledge Base alias must be unique in the [GeneXus Server](https://wiki.genexus.com/commwiki/wiki?9911) instance.

`[imagen omitida: wiki id 31883]`

**Notes:**

* You can choose to export all versions by clicking the CheckbBox ***All versions in Knowledge Base***. Otherwise, only the active version of the Knowledge Base will be sent.
* The *[Work with Lock](https://wiki.genexus.com/commwiki/wiki?17482,,)* or *[Merge](https://wiki.genexus.com/commwiki/wiki?17481,,)* model option it's also available. By default the [Merge](https://wiki.genexus.com/commwiki/wiki?17481,,) model is selected, to select the [Work with Lock](https://wiki.genexus.com/commwiki/wiki?17482,,) model the ***Work With Lock Model*** option must be chosen. Please refer to [HowTo: Change between Merge and Lock Models](https://wiki.genexus.com/commwiki/wiki?21745,,) to know how to change the [Team Collaboration Mode Property](https://wiki.genexus.com/commwiki/wiki?17492,,) after the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) has been sent to the [GeneXus Server](https://wiki.genexus.com/commwiki/wiki?9911).

3) After clicking ***Send*** GeneXus will gather all the necessary information from the local Knowledge Base to send it to the GeneXus Server instance. This process may take a few minutes, depending on the size of the Knowledge Base.

`[imagen omitida: wiki id 31884]`

Check the ***Team Development output section*** for further information.  
  
`[imagen omitida: wiki id 31885]`

*A **success*** message must be displayed; if not, see [GeneXus Server Common Issues](https://wiki.genexus.com/commwiki/wiki?9562,,).

`[imagen omitida: wiki id 31886]`

4) The Knowledge Base is now served by the selected [GeneXus Server](https://wiki.genexus.com/commwiki/wiki?9911) instance, so other users can perform a [Create Knowledge Base from GeneXus Server](https://wiki.genexus.com/commwiki/wiki?22416) operation (from the IDE or using [Team Development MSBuild Tasks](https://wiki.genexus.com/commwiki/wiki?24612,,)) and selecting the recently uploaded Knowledge Base.

The local Knowledge Base is now linked to the one on the [GeneXus Server](https://wiki.genexus.com/commwiki/wiki?9911). This means that from now on, you will be able to work in a [team working environment](https://wiki.genexus.com/commwiki/wiki?9297) by [updating](https://wiki.genexus.com/commwiki/wiki?10627) and [committing](https://wiki.genexus.com/commwiki/wiki?10626) changes. 

**Note:** once a Knowledge Base has been sent to a GeneXus Server instance, the option ***Send Knowledge Base to Server*** will be unavailable from the ***File*** menu.

### [See also](#See+also)

* [Create Knowledge Base from GeneXus Server](https://wiki.genexus.com/commwiki/wiki?22416)


|  |
| --- |
| **Backlinks** |
| [Create Knowledge Base from GeneXus Server](https://wiki.genexus.com/commwiki/wiki?22416) | [Defining versions for each application release](https://wiki.genexus.com/commwiki/wiki?20945) |
| [Disconnect From Server](https://wiki.genexus.com/commwiki/wiki?10654) | [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) |
|
|
| [KB alias](https://wiki.genexus.com/commwiki/wiki?21220) |
| [Server Connection Type property](https://wiki.genexus.com/commwiki/wiki?21107) | [Server Linked Knowledge Base property](https://wiki.genexus.com/commwiki/wiki?21105) | [Server Linked Version property](https://wiki.genexus.com/commwiki/wiki?21106) |
| [Server Password property](https://wiki.genexus.com/commwiki/wiki?21109) | [Server URL property](https://wiki.genexus.com/commwiki/wiki?21104) | [Server Username property](https://wiki.genexus.com/commwiki/wiki?21108) |
|

---
