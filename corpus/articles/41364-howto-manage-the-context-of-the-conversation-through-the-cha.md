---
title: "HowTo: Manage the Context of the conversation through the Chatbot API"
source_id: 41364
source_url: https://wiki.genexus.com/commwiki/wiki?41364
genexus_version: "18"
---

# HowTo: Manage the Context of the conversation through the Chatbot API

The following API allows managing the [Context](https://wiki.genexus.com/commwiki/wiki?39351) values of a chatbot conversation. It consists of API methods to get, add, and update the Context values of a specific conversation as well as all the conversations that are active.

This is very useful to avoid having to call a service every time you need some values that should be persisted in the conversation. For instance, some information is specific to a conversation, such as a User's account data (name, ID, and other information needed), and should be maintained during the conversation without the need to call any service or prompt the user to enter it.

Another example is the information which is global to all conversations. Consider the following example where modifying the context parameters may affect all the chatbots behavior: the human fallback. In this example, the possibility to speak with a person is offered only if there is a connected official to be able to assist them. To avoid calling a service that returns the number of connected officials to find out if it is possible to speak to a person, you can set that amount globally for the context of all conversations. So, when there are changes in the status of those officials, there would be no need to go and query that service.

### [User Context Management](#User+Context+Management)

#### [Get](#Get)

Gets the context value for a specific conversation.

```
&ParameterValue = Chatbot.Context.GetUserContextValue(&Instance, &UserGuid, &Parameter, &Messages)
```

**Where:**

*&Instance*  
      Is a character parameter that denotes the [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113)´s name

*&UserGuid*  
      Is a GUID variable, which identifies the user of the chatbot. See the GetUserId Procedure included in the Data folder (under the [Chatbot Generator resources](https://wiki.genexus.com/commwiki/wiki?39998) CommonChatbots module) which includes an example assigning a hard-coded sample user.

*&Parameter*  
      Is a character value.

*&ParameterValue*  
      Is a character value.

*&Messages*  
      Is Messages Data type. See [Chatbot Generator common errors and solutions](https://wiki.genexus.com/commwiki/wiki?42695) to have details about the values which can take the &Messages parameter.

#### [Set](#Set)

Sets the context value for a specific conversation.

```
Chatbot.Context.SetUserContextValue(&Instance, &UserGuid, &Parameter, &ParameterValue)
```

**Note**: SetUserContextValue cannot be used inside a Conversational object.

#### [Clean](#Clean)

Cleans all the context content, for a specific conversation.

```
Chatbot.Context.CleanUserContext(&Instance, &UserGuid)
```

#### [Samples](#Samples)

**Sample 1**

The information of the user's profile (i.e: name, address, phone) can be obtained at login. Then, you can set there all the information in the user's context.

That information can be retrieved afterwards, when it's needed, for example, in any [Conversational Object](https://wiki.genexus.com/commwiki/wiki?38189).

**Sample 2**

You can pass information from one Flow to another, by the user's context parameters retrieval. Suppose, for example, that you have a [User Input](https://wiki.genexus.com/commwiki/wiki?38959) to ask for the User Identification in a Flow. In a [Conversational Object](https://wiki.genexus.com/commwiki/wiki?38189) of another Flow, you can get that information if it's necessary.

```
&ParameterValue = Chatbot.Context.GetUserContextValue(&Instance, &UserGuid, !"UserIdentification",&Messages)
```

### [Global Context Management](#Global+Context+Management)

#### [Get](#Get)

Gets the context value set for all the conversations.

```
&ParameterValue = Chatbot.Context.GetContextValue(&Instance, &Parameter, &Messages)
```

#### [Set](#Set)

Sets a context value, valid for all the conversations.

```
Chatbot.Context.SetContextValue(&Instance, &Parameter, &ParameterValue)
```

#### [Clean](#Clean)

Cleans all the context content valid for all conversations.

```
Chatbot.Context.CleanContext(&Instance)
```

#### [Sample](#Sample)

Consider a [Flow](https://wiki.genexus.com/commwiki/wiki?38531) where the user asks for the availability of free tickets for an activity or a trip.

The response to the user is the available quota.

`[imagen omitida: wiki id 41368]`

That information is updated through a web service which is called from a Backend, where the following code is executed:

```
&Instance = !"Citizen"
Chatbot.Context.SetContextValue(&Instance, !"quota", &value)
```

In the [Conversational Object](https://wiki.genexus.com/commwiki/wiki?38189) of the Flow, the value of &quota is obtained and returned as an out parameter:

```
&Instance = !"Citizen"   
&Parameter = !"quota"         
&quota = Chatbot.Context.GetContextValue(&Instance, &Parameter, &Messages)
<Rules>
parm(out:&quota);
```

### [Implementation Details](#Implementation+Details)

The context information is stored in the GXChatMessage table that is provided by default with the Chatbot Generator (as part of its [resources](https://wiki.genexus.com/commwiki/wiki?39998)). In turn, the user has two Procedures in the CommonChatbots module (GetContext and SetContext), which are the ones that update / get the context from this table. Those Procedures can be edited: if you do not want to store the data in the way provided, it is possible to change it.

Global context information is handled in the cache, as well as the user information when a conversation does not yet exist for that user. For example, when the user logs in, and you get the user's profile data, that information can be stored in the context even though the user hasn't started to chat yet.


|  |
| --- |
| **Backlinks** |
| [Chatbot Context](https://wiki.genexus.com/commwiki/wiki?39351) | [Chatbot Generator common errors and solutions](https://wiki.genexus.com/commwiki/wiki?42695) | [Chatbot Generator resources update](https://wiki.genexus.com/commwiki/wiki?39998) |
| [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) | [KB:HowTo : Create a chatbot with human fallback](https://wiki.genexus.com/commwiki/wiki?46255) | [Validation Procedure property](https://wiki.genexus.com/commwiki/wiki?42594) |

---
