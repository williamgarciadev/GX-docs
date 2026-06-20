---
title: "Chatbot Generator resources update"
source_id: 39998
source_url: https://wiki.genexus.com/commwiki/wiki?39998
genexus_version: "18"
---

# Chatbot Generator resources update

A [Module](https://wiki.genexus.com/commwiki/wiki?22414) called CommonChatbots is created in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836), containing all the [Chatbot generator](https://wiki.genexus.com/commwiki/wiki?37102) pattern resources.

In the **Build**process, and in the **Generate bot** action, it is checked whether those resources have any change in comparison with the version of the resources that you have in the KB, and depending on the [Keep Resources Updated property](https://wiki.genexus.com/commwiki/wiki?40218), they are updated or not.

When the resources need to be updated in the KB, if the property [Keep Resources Updated property](https://wiki.genexus.com/commwiki/wiki?40218) = prompt, the following dialog is shown:

`[imagen omitida: wiki id 40071]`

The Chatbot generator resources to be updated are all the objects under the **CommonChatbots** module.

### [Data](#Data)

**GXChatMessage**: Table used to store messages and their metadata.

* GXChatMessageId -> Message Identifier (GUID)
* GXChatUserId -> FK of the GXChatUser table (GUID)
* GXChatMessageMessage -> The message (The text you see in the chat)
* GXChatMessageType -> Message type (if it is a response or is from the user including its format)
* GXChatMessageImage -> If you send an Image, it is saved there.
* GXChatMessageDate -> DateTime of the message
* GXChatMessageMeta -> Stores the metadata of the message (The JSON sent by the provider)
* GXChatMessageRepeat -> Auxiliary for SD (see again)
* GXChatUserDevice -> FK of the GXChatUser table
* GXChatMessageInstance -> Instance of the conversational flow to which the message belongs

**GXChatUser**: Table in which users and their devices are stored.

* GXChatUserId -> User identification (GUID)
* GXChatUserDevice -> User device identification

**GetUserId** procedure: The procedure called GetUserId, which is consulted in runtime to obtain the user's ID, by default returns the same ID (as an example). However, you can modify it to customize the way the ID is obtained (modify the procedure or save it as another and change the call, whichever is better for you). In this way, you can manage the users and their IDs as you wish, only modifying that entry point.

### [Themes](#Themes)

The Carmine and CarmineSD Themes include the classes used to style the UI of the chatbot. These are default classes prefixed by "CF" which give a predefined style to the chatbot.

### [UI objects](#UI+objects)

* PanelChatWeb -> called by the <InstanceName>WebUI generated object.
* PanelChat -> called by the <InstanceName>UI generated object. The PanelChat panel has the [Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?20911) set to Online.

**Note**: Up to Genexus 17 upgrade 0:

* PanelChatSD -> called by the <InstanceName>SDUI generated object. The PanelChatSD panel has the [Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?20911) set to Offline.

### [Context](#Context)

GetContext and SetContext procedures have the logic to get and update the Chatbot Context from the GXChatMessage table. See [HowTo: Manage the Context of the conversation through the Chatbot API](https://wiki.genexus.com/commwiki/wiki?41364) for more information.

**Note**: These objects can be modified as desired because they aren't updated mandatorily every time the pattern is generated (as opposed to the generated objects of the Chatbot generator pattern). They are updated considering the Keep Resources Updated property.  
The selection to update the resources is done in the Build process, and in the Generate bot action.

  
  
  


|  |
| --- |
| **Backlinks** |
| [Chatbot generator](https://wiki.genexus.com/commwiki/wiki?37102) | [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) |
| [HowTo: Manage the Context of the conversation through the Chatbot API](https://wiki.genexus.com/commwiki/wiki?41364) | [Keep Resources Updated property](https://wiki.genexus.com/commwiki/wiki?40218) |

---
