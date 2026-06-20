---
title: "HowTo: Initialize entity values in the AI provider"
source_id: 39302
source_url: https://wiki.genexus.com/commwiki/wiki?39302
genexus_version: "18"
---

# HowTo: Initialize entity values in the AI provider

In order to create and initialize [Chatbot Entity](https://wiki.genexus.com/commwiki/wiki?39083) values (and their synonyms) in the [AI](https://en.wikipedia.org/wiki/Artificial_intelligence) provider, using the [Chatbot generator](https://wiki.genexus.com/commwiki/wiki?37102), you just need to execute the following steps.

**1.** Create a [Data Provider](https://wiki.genexus.com/commwiki/wiki?4417) or procedure which loads into a [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021) the list of values for the entity you want to load in the AI provider.

**2.** Call the "*SendEntitiyValues*" procedure (this procedure is an entry point which belongs to the Chatbot external module). In the Kb, you can see it under References - Chatbot/Entities module.  
  
`[imagen omitida: wiki id 42957]`

Its signature is as follows:

```
parm(in:&ChatbotInstance, in:&EntityValues, in:&Entity, out:&Messages);
```

**Where:**

*&ChatbotInstance*  
      Is varchar(256). The name of the [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113).

*&EntityValues*  
      Is of EntityValues data type. Load all the entity values and its synonyms here.

`[imagen omitida: wiki id 40209]`

*&Entity*  
      Is varchar(40). The name of the [Entity](https://wiki.genexus.com/commwiki/wiki?39083) in the NLP provider.

*&Messages*  
      Is an output parameter of Messages data type. See [Chatbot Generator common errors and solutions](https://wiki.genexus.com/commwiki/wiki?42695) to have details about the values which can take the *&Messages* parameter.

### [Sample](#Sample)

Take a look at the example shown in [HowTo: Build a chatbot using GeneXus](https://wiki.genexus.com/commwiki/wiki?37076), and open the "*InitializeEntityValuesPrc*" procedure.

In this example, you are sending values to the AI provider to load the "*Social\_Event\_Type*" entity and some synonyms for each of the values (the synonyms are not mandatory).

```
&SDTEntityValues.values.Clear()
&SDTEntitiesValuesValue.value = !"Art"
&SDTEntitiesValuesValue.synonyms.Add(!"Artistic")
&SDTEntityValues.values.Add(&SDTEntitiesValuesValue)

&SDTEntitiesValuesValue = new()
&SDTEntitiesValuesValue.value = !"Culture"
&SDTEntitiesValuesValue.synonyms.Add(!"Cultural")
&SDTEntityValues.values.Add(&SDTEntitiesValuesValue)

&SDTEntitiesValuesValue = new()
&SDTEntitiesValuesValue.value = !"Nature"
&SDTEntitiesValuesValue.synonyms.Add(!"Fresh air")
&SDTEntityValues.values.Add(&SDTEntitiesValuesValue)

&InstanceName = !"CitizenServiceSD"
Chatbot.Watson.SendEntitiyValues(&InstanceName,&SDTEntityValues,!"Social_Event_Type",&messages)
do "ProcessErrors"
```

After executing this procedure, consider that the AI takes a time to train the information.

**Note**: The entities are created in the Provider if they do not exist.

### [See Also](#See+Also)

[Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520)


|  |
| --- |
| **Backlinks** |
| [Chatbot Entity](https://wiki.genexus.com/commwiki/wiki?39083) | [Chatbot generator](https://wiki.genexus.com/commwiki/wiki?37102) | [Chatbot Generator common errors and solutions](https://wiki.genexus.com/commwiki/wiki?42695) |
| [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) | [KB:Chatbots workshop](https://wiki.genexus.com/commwiki/wiki?44641) | [KB:Citizen Service Chatbot sample](https://wiki.genexus.com/commwiki/wiki?40937) | [HowTo: Integrate queries in a chatbot](https://wiki.genexus.com/commwiki/wiki?46415) |
| [HowTo: Manage training examples using the Chatbot Generator API](https://wiki.genexus.com/commwiki/wiki?41314) |

---
