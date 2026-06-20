---
title: "Disambiguations"
source_id: 47955
source_url: https://wiki.genexus.com/commwiki/wiki?47955
genexus_version: "18"
---

# Disambiguations

Disambiguations are particularly useful when given a message from a user the chatbot understands that the same message may correspond to several flows. In this case, it becomes necessary to be able to ask the user to clarify how to continue the conversation.  
As from [GeneXus 17 upgrade 3](https://wiki.genexus.com/commwiki/wiki?47659,,), the [Chatbot generator](https://wiki.genexus.com/commwiki/wiki?37102) supports the use of disambiguations for Watson Assistant.

### [How to use Disambiguations in GeneXus](#How+to+use+Disambiguations+in+GeneXus)

In the properties of a [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113) instance, enable the [Disambiguation property](https://wiki.genexus.com/commwiki/wiki?47823), which is only available when the value of the [NLP Provider property](https://wiki.genexus.com/commwiki/wiki?38931) is Watson.

`[imagen omitida: wiki id 47957]`

After enabling the [Disambiguation property](https://wiki.genexus.com/commwiki/wiki?47823), it will be possible to enter the message with which the different disambiguation options are going to be presented, through the [Disambiguation Message property](https://wiki.genexus.com/commwiki/wiki?47824). Also, it will be possible to define the message that will be shown if the user considers that none of the options displayed is correct using the [Disambiguation Cancellation Message property](https://wiki.genexus.com/commwiki/wiki?47825).

Example

In the following example, there is a [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113) and two Wifi and Service Location Bathroom Floor flows.

`[imagen omitida: wiki id 47961]`

In this case, the chatbot is asked the question "where is the bathroom, and what is the Wifi password?"

In this sentence entered by the user, it is possible to recognize that reference is made to two flows, so the chatbot will show the corresponding options for the user to choose the most suitable one.

`[imagen omitida: wiki id 47962]`

Next, the Wifi option is chosen, so the bot will follow the conversation through the Wifi flow.

`[imagen omitida: wiki id 47963]`

If the user considers that none of the options provided is related to his/her intention, he/she can choose the option "None of the above."

`[imagen omitida: wiki id 47964]`

### [Availability](#Availability)

This feature is available since [GeneXus 17 upgrade 3](https://wiki.genexus.com/commwiki/wiki?47659,,)

### [See also](#See+also)

* [Disambiguation Message property](https://wiki.genexus.com/commwiki/wiki?47824)
* [Disambiguation Cancellation Message property](https://wiki.genexus.com/commwiki/wiki?47825)


|  |
| --- |
| **Backlinks** |
| [Disambiguation Cancellation Message property](https://wiki.genexus.com/commwiki/wiki?47825) | [Disambiguation Message property](https://wiki.genexus.com/commwiki/wiki?47824) | [Disambiguation property](https://wiki.genexus.com/commwiki/wiki?47823) |

---
