---
title: "Chatbot Generator - Troubleshooting"
source_id: 41260
source_url: https://wiki.genexus.com/commwiki/wiki?41260
genexus_version: "18"
---

# Chatbot Generator - Troubleshooting

This page summarizes some of the errors related to the [Chatbot generator](https://wiki.genexus.com/commwiki/wiki?37102) that may be encountered through the various stages (during generation or at runtime) and explains the causes of such errors and how to solve them.

### [Synchronization](#Synchronization)

#### [**1. Using DialogFlow, the instance synchronization fails.**](#1.+Using+DialogFlow%2C+the+instance+synchronization+fails.)

**Problem:**The following error is thrown in the General output:

|  |
| --- |
| ``` ========== Chatbot synchronization for <instance> started ==========  error: One or more errors occurred.  error: invalid_client  error: Unauthorized ``` |

**Cause / Solution:**  The credentials are used to connect to the provider, and they will be stored in your development machine. This error means that any of them are not valid.

Check the credentials [Client Id property](https://wiki.genexus.com/commwiki/wiki?39761) and/or [Client Secret property](https://wiki.genexus.com/commwiki/wiki?39762), the [Dialogflow Agent property](https://wiki.genexus.com/commwiki/wiki?39758) and the [Google Cloud Project property](https://wiki.genexus.com/commwiki/wiki?39759).

For more details, see [Configure Google Dialogflow for the Chatbot generator](https://wiki.genexus.com/commwiki/wiki?39749).

### [Generation](#Generation)

#### [**1. The resources are not being updated.**](#1.+The+resources+are+not+being+updated.)

**Problem**: The [resources](https://wiki.genexus.com/commwiki/wiki?37102) (CommonChatbots module or the Chatbot generator's Theme Classes) are not being updated. In some cases, when you update to a new upgrade, the resources have fixes which you may need to update in your KB.

**Cause / Solution:** The resources are automatically updated in the Build process. However, if for some reason they are not updated (and there are changes to be updated), you can force the updating of resources by executing the [Force Chatbot Generation menu option](https://wiki.genexus.com/commwiki/wiki?40241).

#### [**2. The Chatbot module isn't updated automatically. This is the expected behavior.**](#2.+The+Chatbot+module+isn%27t+updated+automatically.+This+is+the+expected+behavior.)

If you see the following warning:

========== Copying Module 'GeneXus' started ==========  
Copying Module 'GeneXus' Success  
warning: Built-in 'Chatbot' module must be updated to version 2.1.10.129299.  
========== Copying Module 'Chatbot' started ==========

You have to update it through the Knowledge Manager > Manage Module References option:

`[imagen omitida: wiki id 41567]`

#### [**3. Programs that should be generated automatically aren't being generated.**](#3.+Programs+that+should+be+generated+automatically+aren%27t+being+generated.)

**Problem:** Some objects should be [automatically generated](https://wiki.genexus.com/commwiki/wiki?37102). However, this depends on the [Generate Web UI property](https://wiki.genexus.com/commwiki/wiki?40211) and the [Generate UI property](https://wiki.genexus.com/commwiki/wiki?40680).

**Cause/ Solution:** If Enable Web UI Generation property and the Enable SD UI Generation property are set to FALSE, you may encounter the following warning, which means that none of the UI objects are automatically generated (e.g., <InstanceName>WEBUI and <InstanceName>SDUI objects).

**warning: <Flow Name> component can't be generated because the web and sd UI generation are disabled at the conversational** **flows instance '<Instance Name>'**

As a result, the chatbot may not work as expected.

### [Runtime](#Runtime)

#### [**1. The chatbot replies with an empty string.**](#1.+The+chatbot+replies+with+an+empty+string.)

**Problem**: The response message of the chatbot is empty.

**Cause / Solution I:** Check that the GXCF\_Chatbots.config (it was called GXCF\_<InstanceName>Chatbot.config prior to GeneXus 16 upgrade 7) file is under the virtual directory in .NET, and the WEB-INF directory of the servlet server in JAVA. You should also check the contents of this file, as it may have invalid information, such as the reference to the workspaceId, the APIkey, or any other information which may not be valid.

If you generate the log file **(\*)**, you may see an entry similar to the following:

```
System.Net.WebException: The remote server returned an error: (401) Unauthorized.
   at System.Net.HttpWebRequest.GetResponse()
   at GeneXus.Http.Client.GxHttpClient.Execute(String method, String name)
10:55:24,466 [15] DEBUG GeneXus.Http.Client.GxHttpClient - Reading response...
10:55:24,490 [15] DEBUG GeneXus.Http.Client.GxHttpClient - BytesRead 37
10:55:24,495 [15] DEBUG GeneXus.Http.Client.GxHttpClient - BytesRead 0
10:55:24,501 [15] DEBUG GeneXus.Http.Client.GxHttpClient - _responseString {"code":401, "error": "Unauthorized"}
10:55:24,505 [15] DEBUG GeneXusUserLog - Chatbot Generator - Response body: {"code":401, "error": "Unauthorized"}
```

See [Connecting to the Chatbot Provider](https://wiki.genexus.com/commwiki/wiki?37102) for more information.

Specifically, check if you have a warning in the output, as follows:

* *The user and password for the Watson conversation service are empty. The workspace is not going to be uploaded to Watson conversation.*
* *Client Id for <InstanceName> Conversational Flows Instance is Empty.*
* *Client Secret for <InstanceName> Conversational Flows Instance is Empty.*

In such case, the GXCF\_Chatbots.config cannot be created.  
Enter the required values for the [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113) properties as explained in [Configuring GeneXus for using the Chatbot Generator](https://wiki.genexus.com/commwiki/wiki?37096). After saving the instance, the .config file will be created / updated.

**Cause / Solution II:** Check the [Web Notifications and Progress UC requirements](https://wiki.genexus.com/commwiki/wiki?27740) as the Chatbot Generator uses Web notifications as a basis.

**(\*)**

**Note**: For troubleshooting, you can set the [Log level property](https://wiki.genexus.com/commwiki/wiki?36304) and [Log output property](https://wiki.genexus.com/commwiki/wiki?39568) to get a detailed trace about the dialog between the client and the Provider.

**Important Note: Since [GeneXus 16 upgrade 3](https://wiki.genexus.com/commwiki/wiki?42129,,), error messages can be configured to be displayed on the prototyping screen (see [SAC 42519](https://www.genexus.com/developers/websac?en,,,45219)).**

`[imagen omitida: wiki id 42694]`

See [Chatbot Generator common errors and solutions](https://wiki.genexus.com/commwiki/wiki?42695).

#### [**2. Using DialogFlow provider, the following web page appears after setting the Instance Credentials.**](#2.+Using+DialogFlow+provider%2C+the+following+web+page+appears+after+setting+the+Instance+Credentials.)

**Problem:** Error 401 is thrown when you try to configure the instance to use DialogFlow.

`[imagen omitida: wiki id 41931]`

Or the following:

`[imagen omitida: wiki id 41939]`

If you check the General output, you may see the following error:

```
Refreshing instance <instance>
error: An error occurred while applying pattern instance x: 'System.AggregateException'
error: One or more errors occurred.
error: One or more errors occurred.
error: Error:"invalid_client", Description:"Unauthorized", Uri:""
Pattern generation (Conversational Flows) Failed
```

**Cause / Solution:** Some information related to the connection to DialogFlow is not valid. Check the credentials [Client Id property](https://wiki.genexus.com/commwiki/wiki?39761) and/or [Client Secret property](https://wiki.genexus.com/commwiki/wiki?39762), the [Dialogflow Agent property](https://wiki.genexus.com/commwiki/wiki?39758) and the [Google Cloud Project property](https://wiki.genexus.com/commwiki/wiki?39759).

See [Configure Google Dialogflow for the Chatbot generator](https://wiki.genexus.com/commwiki/wiki?39749).


|  |
| --- |
| **Backlinks** |
| [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) |

---
