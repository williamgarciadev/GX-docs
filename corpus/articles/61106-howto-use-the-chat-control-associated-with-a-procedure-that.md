---
title: "HowTo: Use the Chat Control associated with a Procedure that calls a Globant Enterprise AI API (GeneXus 18 latest upgrade or prior)"
source_id: 61106
source_url: https://wiki.genexus.com/commwiki/wiki?61106
genexus_version: "18"
---

# HowTo: Use the Chat Control associated with a Procedure that calls a Globant Enterprise AI API (GeneXus 18 latest upgrade or prior)

The following sample outlines the steps required to implement an interface that contains a [Chat Control](https://wiki.genexus.com/commwiki/wiki?59254) whose [SendMessageHandlerObject property](https://wiki.genexus.com/commwiki/wiki?60797) is set to the name of a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) that connects to a Globant Enterprise AI API to execute an Assistant defined in a Globant Enterprise AI project.

1. Create a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) and drag a Chat Control to its [Web Layout](https://wiki.genexus.com/commwiki/wiki?8132) (you can follow the same steps using a Panel object generated in Angular).

`[imagen omitida: wiki id 61101]`

2. Create a Procedure object.

This Procedure receives the messages sent by the Chat Control, calls the Globant Enterprise AI API, and returns the response.

Create a Procedure (for example, called TravelAgencyChatHandler) and define it as follows:

**Source:**

```
&chatMessagesUI.FromJson(&httpRequest.ToString())

// Globant Enterprise AI Connection
&httpClient.Host = !'api.corp.saia.ai' // Address of the GEAI API
&httpClient.Secure = 1
&httpClient.BaseUrl = !'/'
&httpClient.AddHeader(!'Content-Type', !'application/json')
&httpClient.AddHeader(!'Authorization', !'Bearer <Your_Authorization_Token>') // Your authorization token from GEAI.

// Globant Enterprise AI Data
&chatData.model = !'saia:assistant:<Your_Assistant_ID>' // GEAI Assistant Id
&chatData.stream = true
&chatData.messages = &chatMessagesUI

// Globant Enterprise AI Request
// Sends the request to the API (this is where the chat messages are sent)
&httpClient.AddString(&chatData.ToJson())
&httpClient.Execute(!'POST', !'chat')

// Response
Do While not &HttpClient.EOF
    &httpResponse.AddString(&HttpClient.ReadChunk() + Chr(10))
EndDo

//Error Handling
If &httpClient.ErrCode > 0
    &chatMessageUI.content = &httpClient.ErrDescription
    &chatMessageUI.role = GeneXusUIControls.Chat.MessageRole.ERROR
    &httpResponse.AddString(&chatMessageUI.ToJson())
EndIf
```

**Properties:**

You must set the following properties in the Procedure:

* [Main program property](https://wiki.genexus.com/commwiki/wiki?7407) = True
* [Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947) = HTTP
* [Buffer Response property](https://wiki.genexus.com/commwiki/wiki?55195) = Disabled (this ensures that the Procedure can send partial responses progressively to the Chat as they are generated).

**Variables:**

* **&chatMessagesUI:** Variable based on the [MessageUI SDT](https://wiki.genexus.com/commwiki/wiki?60714), which must be marked as a collection. It is loaded with a collection of messages received from the Chat Control.
* **&chatData:** Variable based on the predefined ChatData SDT that defines the data to be sent to the Globant Enterprise AI **chat** endpoint.  
    
  The ChatData SDT structure is as follows:

ChatData  
{  
    model: Character(20)  
    messages: Collection          // Collection of MessageUI  
        messagesItem: MessageUI   // GeneXusUIControls.Chat.Message  
    stream: Boolean  
}

**Note**: For more details about the /chat endpoint and the request structure, refer to the [Chat API documentation](https://docs.globant.ai/en/wiki?34,Chat+API).

* **&httpClient:** Variable based on the [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932).
* **&httpRequest:** Variable based on the [HttpRequest data type](https://wiki.genexus.com/commwiki/wiki?6933).
* **&httpResponse:** Variable based on the [HttpResponse data type](https://wiki.genexus.com/commwiki/wiki?6934).

3. Use a Chat Assistant defined in a Globant Enterprise AI Project.

You may have a [Chat Assistant](https://docs.globant.ai/en/wiki?708,Chat+Assistant) provided by someone else, or you can create one by yourself. In either case, you must obtain specific information from the Chat Assistant.

To get the required information:

3.1. Enter the Globant Enterprise console, go to the Assistants section, and search for the Assistant that will handle your chat. Click on the Update button associated with that Assistant and copy the Assistant ID value. In the Procedure source, replace **<Your\_Assistant\_ID>**  with this identifier.

3.2. In the Globant Enterprise console, go to the API Tokens section. Search for the corresponding API Token and copy its value. In the Procedure source, replace **<Your\_Authorization\_Token>** with this token.

4. Connect the Chat Control to the Procedure.

In the Web Panel (or Panel), set the [SendMessageHandlerObject property](https://wiki.genexus.com/commwiki/wiki?60797) of the Chat Control to the Procedure name (TravelAgencyChatHandler).

## [Availability](#Availability)

Since [GeneXus 18 Upgrade 14](https://wiki.genexus.com/commwiki/wiki?59631).


|  |
| --- |
| **Backlinks** |
| [GeneXus 18 Upgrade 14](https://wiki.genexus.com/commwiki/wiki?59631) |

---
