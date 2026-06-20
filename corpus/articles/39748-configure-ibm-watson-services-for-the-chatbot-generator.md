---
title: "Configure IBM Watson services for the Chatbot generator"
source_id: 39748
source_url: https://wiki.genexus.com/commwiki/wiki?39748
genexus_version: "18"
---

# Configure IBM Watson services for the Chatbot generator

To use IBM Watson services, you need to configure the **Watson Assistant** API services:

First, log in to [IBM](https://cloud.ibm.com/) and create a new Watson Assistant Service by clicking on "Create resource."

`[imagen omitida: wiki id 45724]`  
  
Select Services from the left menu, and filter by "Watson Assistant":

`[imagen omitida: wiki id 45725]`

After creating the Service, you can see it in the Services list:

`[imagen omitida: wiki id 45723]`

There you can get the Service credentials to set the [credentials](https://wiki.genexus.com/commwiki/wiki?37096) in GeneXus.

`[imagen omitida: wiki id 45726]`

To learn more, read [Service credentials for Watson services](https://console.bluemix.net/docs/services/watson/getting-started-credentials.html#creating-credentials) (Updating service credentials section).

### [Skills](#Skills)

Each [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113) generates a different skill (formerly workspace).  
In Watson, you can open the web console and access the skills created by GeneXus.

To do so, click on "Launch Watson Assistant":

`[imagen omitida: wiki id 45727]`

Then select Skills from the left menu.

`[imagen omitida: wiki id 45728]`

The skill structure (entities and entity values, training triggers, and the dialogue) is created and mantained by the Chatbot Generator.


|  |
| --- |
| **Backlinks** |
| [API Key property](https://wiki.genexus.com/commwiki/wiki?41263) | [Authentication Type property](https://wiki.genexus.com/commwiki/wiki?41262) | [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) |
| [Configuring GeneXus for using the Chatbot Generator](https://wiki.genexus.com/commwiki/wiki?37096) | [Region property in Conversational Flows Instance](https://wiki.genexus.com/commwiki/wiki?41264) | [Workspace Id property](https://wiki.genexus.com/commwiki/wiki?39768) |

---
