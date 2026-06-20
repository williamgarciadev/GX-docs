---
title: "HowTo: Manage training examples using the Chatbot Generator API"
source_id: 41314
source_url: https://wiki.genexus.com/commwiki/wiki?41314
genexus_version: "18"
---

# HowTo: Manage training examples using the Chatbot Generator API

The [Chatbot generator](https://wiki.genexus.com/commwiki/wiki?37102) API allows you to [Initialize entity values in the AI provider](https://wiki.genexus.com/commwiki/wiki?39302), and also adds the possibility to keep the training phrases (examples) for the [intents](https://wiki.genexus.com/commwiki/wiki?38949) recognition updated in the Provider.

The training examples are called Trigger Messages at the [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113), and they can be configured from the [Trigger Messages property](https://wiki.genexus.com/commwiki/wiki?39067) of each [Flow](https://wiki.genexus.com/commwiki/wiki?38531).  
Besides configuring the training examples there, they can be obtained, added and deleted, using the Chatbot Generator API (to avoid editing the Conversational Flows instance to make any change at production time).

This document details the methods to be used:

### [SendFlowTriggers](#SendFlowTriggers)

It allows you to send to the NLP Provider some triggers for a specific [Flow](https://wiki.genexus.com/commwiki/wiki?38531).

```
Chatbot.Flows.SendFlowTriggers(&Instance, &Triggers, &Flow, &Messages)
```

**Where:**

*&Instance*  
      Is of Character type

*&Triggers*  
      Is a Varchar collection

*&Flow*  
      Is of Character type

*&Messages*  
      Is of Messages data type. See [Chatbot Generator common errors and solutions](https://wiki.genexus.com/commwiki/wiki?42695) to have details about the values which can take the &Messages parameter.

#### [Sample](#Sample)

```
&Triggers.Add(!"rides at no cost")
&Triggers.Add(!"Free journey") 
        
&Flow = !"FreeTrips" //Name of the Flow
&Instance = !"Citizen" //Name of the instance
Chatbot.Flows.SendFlowTriggers( &Instance, &Triggers, &Flow, &Messages)
```

### [GetFlowTriggers](#GetFlowTriggers)

Returns a collection of Triggers of a particular [Flow](https://wiki.genexus.com/commwiki/wiki?38531).

```
Chatbot.Flows.GetFlowTriggers(&Instance, &Flow, &Messages, &Triggers)
```

#### [Sample](#Sample)

```
&Flow = !"FreeTrips" //Name of the Flow
&Instance = !"Citizen" //Name of the instance
&Triggers = Chatbot.Flows.GetFlowTriggers(&Instance, &Flow, &Messages)
```

### [DeleteFlowTriggers](#DeleteFlowTriggers)

Deletes a collection of Triggers of a [Flow](https://wiki.genexus.com/commwiki/wiki?38531).

```
Chatbot.Flows.DeleteFlowTriggers(&Instance, &Triggers, &Flow, &Messages)
```

#### [Sample](#Sample)

```
&Provider = Chatbot.Conversational.Watson
&Flow = !"FreeTrips" //Name of the Flow
&Instance = !"Citizen" //Name of the instance
&Triggers.Add(!"rides at no cost")
Chatbot.Flows.DeleteFlowTriggers(&Instance, &Triggers, &Flow, &Messages)
```


|  |
| --- |
| **Backlinks** |
| [Chatbot Generator common errors and solutions](https://wiki.genexus.com/commwiki/wiki?42695) | [Chatbot Intent](https://wiki.genexus.com/commwiki/wiki?38949) | [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) |

---
