---
title: "Configuring Google Dialogflow for the Chatbot Generator"
source_id: 39749
source_url: https://wiki.genexus.com/commwiki/wiki?39749
genexus_version: "18"
---

# Configuring Google Dialogflow for the Chatbot Generator

This article introduces the steps to use the [Chatbot Generator](https://wiki.genexus.com/commwiki/wiki?37102) with Dialogflow.  
After the setup in Google Clouds, you need to create an [Agent](https://dialogflow.com/docs/agents) in Dialogflow, where GeneXus will create your chatbot for this provider (create and update the [intents](https://wiki.genexus.com/commwiki/wiki?38949), [entities](https://wiki.genexus.com/commwiki/wiki?39083), and the dialog itself).

Below is a summary of the steps that should be followed:

* [Create a project in Google Cloud](#Create+a+project+in+Google+Cloud)
* [Enable the "Dialogflow API" service in your project](#Enable+the+%22Dialogflow+API%22+service+in+your+project)
* [Get the credentials for accessing the API](#Get+the+credentials+for+accessing+the+API)
* [Create an Agent in Dialogflow that is related to the Google Cloud project](#Create+an+Agent+in+Dialogflow+that+is+related+to+the+Google+Cloud+project)
* [Configure the GeneXus Chabot instance for using Dialogflow](#Configure+the+GeneXus+Chabot+instance+for+using+Dialogflow)
* [Compatibility](#Compatibility)

### [Create a project in Google Cloud](#Create+a+project+in+Google+Cloud)

Go to [this](https://console.cloud.google.com/) link. Select the list of projects, and create a New Project.  
Then, you'll have something similar to the following:

`[imagen omitida: wiki id 39750]`

### [Enable the "Dialogflow API" service in your project](#Enable+the+%22Dialogflow+API%22+service+in+your+project)

In the project's Dashboard, go to APIs & Services -> Library

`[imagen omitida: wiki id 39751]`

In the search bar, look for Dialogflow. Select it and click the Enable button.

`[imagen omitida: wiki id 39752]`

### [Get the credentials for accessing the API](#Get+the+credentials+for+accessing+the+API)

The following images show step by step how to create a Service Account to work with the Dialogflow APIs:

**![](https://lh4.googleusercontent.com/WrNrF1OI8Kq4ul3hCWR2YazwDgyHl6Ytu12NEdJqmxjzuUSdbAE_lcjs-A0zdy_8fD_3vSuwOMu-oXVplslrZCfcidYxSgj6wPSBVyhrd9Py2NTp1BYJFHj4uBBl3puo3JGHbi6h)**

Next, click on the option to create a service account:

**![](https://lh4.googleusercontent.com/u0wki7Ljc1MzlqO4mSUBsk_o4z-jErRqxlsQ5O35lFbp0D_DaJuCj-vwpLHmpv9ycI-Ris8LAMqNFygEHrOUD-d0iUQbfTBusHxQpLeXulj_gmtPcG878vU6zWvmyOWXiNhyETOS)**

Find the new account in the list of service accounts and click on edit (in the Actions menu). In the edit screen, create a new key:

**![](https://lh6.googleusercontent.com/aP4BxjbybE0VQDpUREscTJ72t9UrEJ2dFfltUOFwLDqtv2HB7CaKcI-JUrf1vdJzN0olLsRsU734TTMvgJZgf2kqxMs8fS5ollri6wzAtLmPn9D4C3_S3Uxt8rJYDKJVyXovHMoP)**

Select the JSON type:

**![](https://lh3.googleusercontent.com/dayQ_hU5-3rcjBrOYR91QzbiYplELWob0q-Al8M-VW1vlzmUl1qzc7SLmOss82Ibhy9gfpznGcLWFNDoPwdRvzMIoRPn3FsVa3L4glYSwqNQnInyIVqJw9nxXZQr9Yb41RTNuvG0)**

The generated JSON is downloaded as shown below:

**![](https://lh3.googleusercontent.com/jLaGYF7D1D9nFWE1A8B_M2OpOGDfBrv-Hga1HFPP8sLN9XkiW9YGpT6rX4OPvScMQAlvdpiu4zJWFx2q-zOQJy8inACUIfuKzt5cQNiNO9TXYfpR8KG_tSuzp_kZvSeEVZjU3W0r)**

The content of this JSON must be entered in the [Google Cloud JSON Credentials property](https://wiki.genexus.com/commwiki/wiki?47826).

### [Create an Agent in Dialogflow that is related to the Google Cloud project](#Create+an+Agent+in+Dialogflow+that+is+related+to+the+Google+Cloud+project)

Go to the [Dialogflow](https://console.dialogflow.com) website to create a new Agent. Make sure you select the right Project (defined in the previous step) before pressing the create Agent button. Note that you can create only one Agent per project.

`[imagen omitida: wiki id 39757]`

### [Configure the GeneXus Chabot instance for using Dialogflow](#Configure+the+GeneXus+Chabot+instance+for+using+Dialogflow)

Edit the [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113) and configure the [NLP Provider property](https://wiki.genexus.com/commwiki/wiki?38931), [Google Cloud Project property](https://wiki.genexus.com/commwiki/wiki?39759) and [Google Cloud JSON Credentials property](https://wiki.genexus.com/commwiki/wiki?47826).

To continue, save or execute "Generate Chatbot." At this moment, GeneXus will try to synchronize your instance with the agent created in Dialogflow.

It will no longer be necessary to authenticate to use Dialogflow because a service account is now used.

### [Compatibility](#Compatibility)

Since [GeneXus 17 upgrade 3](https://wiki.genexus.com/commwiki/wiki?47659,,), it is necessary to use the Service Account authentication mechanism because the previous mechanism is no longer supported.


|  |
| --- |
| **Backlinks** |
| [Chatbot Generator - Troubleshooting](https://wiki.genexus.com/commwiki/wiki?41260) | [Chatbot Generator common errors and solutions](https://wiki.genexus.com/commwiki/wiki?42695) | [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) |
| [Client Id property](https://wiki.genexus.com/commwiki/wiki?39761) | [Client Secret property](https://wiki.genexus.com/commwiki/wiki?39762) | [Configuring GeneXus for using the Chatbot Generator](https://wiki.genexus.com/commwiki/wiki?37096) | [Dialogflow Agent property](https://wiki.genexus.com/commwiki/wiki?39758) |
| [Google Cloud JSON Credentials property](https://wiki.genexus.com/commwiki/wiki?47826) | [Google Cloud Project property](https://wiki.genexus.com/commwiki/wiki?39759) |

---
