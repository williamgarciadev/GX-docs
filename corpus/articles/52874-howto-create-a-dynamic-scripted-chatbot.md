---
title: "HowTo: Create a Dynamic Scripted Chatbot"
source_id: 52874
source_url: https://wiki.genexus.com/commwiki/wiki?52874
genexus_version: "18"
---

# HowTo: Create a Dynamic Scripted Chatbot

This article describes how to create a [Dynamic Scripted Chatbot](https://wiki.genexus.com/commwiki/wiki?52873), which can be defined since GeneXus 18.

First, create a [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113).

To configure the chatbot as Scripted, set the [NLP Provider property](https://wiki.genexus.com/commwiki/wiki?38931) to “None”. To enable the generation of a dynamic scripted Chatbot, set the [Generate Dynamic Provider property](https://wiki.genexus.com/commwiki/wiki?51753) to True.

**Note**: The “Properties” button inside the Conversational [Flow](https://wiki.genexus.com/commwiki/wiki?38531) instance helps you view the Properties window.

`[imagen omitida: wiki id 52888]`

After saving the Conversational object, the necessary resources to develop the Dynamic Scripted chatbot will be imported and generated.

Note that within these resources, the necessary [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)s to access data related to chatbot instances are included.

Select “Run” (F5 on your keyboard) to start testing the edition of the wizard at runtime. The[Launchpad Tool Window](https://wiki.genexus.com/commwiki/wiki?52315)[Launchpad Tool Window](https://wiki.genexus.com/commwiki/wiki?52315) will be shown, including the links to execute the associated Panels:

`[imagen omitida: wiki id 52890]`

By clicking on the Main object, the following Panel *(PanelChatbotFlows)* will be executed:

`[imagen omitida: wiki id 52885]`

The purpose of this screen is to show all those Flows related to at least one instance. In addition, this Panel allows you to create a new Flow, choose an existing one, edit one, and even delete it.

As you can see in the picture below, there is an “Assigned to instance” combo box, which allows you to filter by a particular instance, or display all Flows (None).

`[imagen omitida: wiki id 52887]`

When selecting a specific instance, the “SET AS ACTIVE” option will be also enabled, which allows you to define that you want to work with that particular instance. The new Flows to be inserted and the chat available are associated with that selected instance.

`[imagen omitida: wiki id 52889]`

It is also possible to Export/Import Flows. To export, select the desired Flow or Flows and click on the “Export” button. This will generate a .json file with the necessary data.

When clicking on the “Import” button, a *.json* type file will be requested with the necessary information to add the desired Flows. By default, you will see two Flows already created in the PanelChatbotFlows Panel: “Hello World” and “Greetings.” You can associate them with an instance by using the “Assigned to instance” combo box.

### [How to create a Flow at runtime](#How+to+create+a+Flow+at+runtime)

Click on the “INSERT” button in the “PanelChatbotFlows” Panel to create a new Flow.

**Note:** It is possible to create a Flow associated with a previously selected instance or create a Flow without the need to have an instance activated. In the last case, the following warning will be shown:

`[imagen omitida: wiki id 52886]`

Note that a Flow can be associated with several instances because they can be reused.

After clicking on the “INSERT” button to create a new Flow, the following screen will be displayed for you to configure the data associated with a Flow.

`[imagen omitida: wiki id 52881]`

This dialog contains three tabs where you can configure Trigger Messages, User Inputs, and Responses for that particular Flow.

`[imagen omitida: wiki id 52880]`

#### [Trigger Messages Tab](#Trigger+Messages+Tab)

These are the messages you expect users might type in the chatbot. A Scripted chatbot checks that the Trigger Message matches the messages entered by the user.

When clicking on the Trigger Messages Tab in the Dynamic Scripted Chatbot, the following will be displayed:

`[imagen omitida: wiki id 52884]`

To add a new Trigger Message, click on the “NEW MESSAGE” button and this other dialog will be shown:

`[imagen omitida: wiki id 52883]`

In this screen, you can configure the newly added message for the Trigger messages of that Flow.

#### [User Input Tab](#User+Input+Tab)

When clicking on the User Input tab and then on New User Input, the following screen will be visible to configure the corresponding data:

`[imagen omitida: wiki id 52877]`

In the “Input Name” field, the name is configured without the &; for example: var1.

#### [Responses Tab](#Responses+Tab)

When clicking on the “Responses” Tab and then on “New Response”, the following screen is displayed:

`[imagen omitida: wiki id 52882]`

In the Parameters tab, the Output parameter and output message are configured. The output parameter is configured in the same way as the User input without the &; for example: var1. To reference an output variable in the Messages—if necessary—add the &; for example: &var1.

### [How to add a Conversational Object in a Chatbot Flow of a Dynamic Scripted Chatbot](#How+to+add+a+Conversational+Object+in+a+Chatbot+Flow+of+a+Dynamic+Scripted+Chatbot)

Inside the New Chatbot Flow, complete the Conversational Object field with the “Qualified Name” of the desired[Procedure object](https://wiki.genexus.com/commwiki/wiki?6293)[Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) (search the Procedure [Qualified Name property](https://wiki.genexus.com/commwiki/wiki?22477) and copy its value).

Next, indicate the input and output parameters of the Conversational Object.

### [Sample](#Sample)

Consider a Procedure called “TestCO” that contains the following [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862): Parm(in:&var1, out:&var2);

Click on the “UPDATE” link next to your Chatbot Flow. Go to the User Input section, and click on “NEW INPUT.” Add the variable var1 and its corresponding Ask Message.

`[imagen omitida: wiki id 52876]`

In the Position field, define the position of the parameter in the Parm rule of the Conversational Object.

Enter the output Parm “var2” in the Responses Tab as a parameter.

`[imagen omitida: wiki id 52875]`

Important: The Procedure to be used as a Conversational Object must be previously generated in your KB.

**Note**: For Dynamic Scripted type Chatbots, it is only possible to configure a Conversational Object that uses String type variables in its Parm rule.

### [Video](#Video)

`[imagen omitida: wiki id 20668]` [Chatbots with GeneXus 18](https://www.genexus.com/en/products/genexus/live-2022/software-development/chatbots-with-genexus-18)


|  |
| --- |
| **Backlinks** |
| [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) | [Dynamic Scripted Chatbot](https://wiki.genexus.com/commwiki/wiki?52873) | [Total Experience with GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51570) |

---
