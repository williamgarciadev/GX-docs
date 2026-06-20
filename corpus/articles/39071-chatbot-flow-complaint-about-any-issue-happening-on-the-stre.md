---
title: "Chatbot Flow: Complaint about any issue happening on the street"
source_id: 39071
source_url: https://wiki.genexus.com/commwiki/wiki?39071
genexus_version: "18"
---

# Chatbot Flow: Complaint about any issue happening on the street

Learn how to define a [Flow](https://wiki.genexus.com/commwiki/wiki?38531) in order to model making a request or complaint about any issue happening on the street.

There are three types of requests:

* Lighting
* Green Places
* Traffic Signals

In this solution, the user enters any utterance that the [AI](https://en.wikipedia.org/wiki/Artificial_intelligence) engine detects as any of the possibilities above, so each of them is considered to be a different [intent](https://wiki.genexus.com/commwiki/wiki?38949).  
In all three cases, the user needs to enter the address where the problem has taken place. If the request is about Traffic Signs, the user has to specify the traffic sign involved.

### [Making a complaint about a lighting issue](#Making+a+complaint+about+a+lighting+issue)

Here you will see some of the intents, starting with "*Making a complaint about a Lighting issue.*" In this case the [Conversational Object property](https://wiki.genexus.com/commwiki/wiki?38189) is a procedure that inserts the complaint in the database.  
The parameters of this procedure are the Identity of the user making the complaint and the details of the issue. The chatbot asks this information from the user and then runs the procedure.

See the detailed explanation of this case [here](https://wiki.genexus.com/commwiki/wiki?37115,,).

### [Making a complaint about Traffic Signs](#Making+a+complaint+about+Traffic+Signs)

In this example, the [Conversational Object property](https://wiki.genexus.com/commwiki/wiki?38189) is set to a web panel that shows the traffic signs so the user can choose between any of them and make the complaint.

The flow would be as follows:

`[imagen omitida: wiki id 43964]`

Note that you define a Response Message (text) that says: "Please select the traffic signal". This message is displayed at the same time of the web panel load, so the user can understand the purpose of the web panel displayed on the screen.

`[imagen omitida: wiki id 43965]`

At runtime, it looks like this:

`[imagen omitida: wiki id 40093]`

`[imagen omitida: wiki id 40917]`


|  |
| --- |
| **Backlinks** |
| [Chatbot Flow: Set up an appointment for any administrative formality](https://wiki.genexus.com/commwiki/wiki?39073) | [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) |

---
