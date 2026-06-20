---
title: "Chatbot Generator common errors and solutions"
source_id: 42695
source_url: https://wiki.genexus.com/commwiki/wiki?42695
genexus_version: "18"
---

# Chatbot Generator common errors and solutions

### [Error Codes](#Error+Codes)

1 - Common Runtime Errors

2 - Message API Errors

3 - Flows API(1) Errors ([HowTo: Manage training examples using the Chatbot Generator API](https://wiki.genexus.com/commwiki/wiki?41314))

4 - Entities API(2) Errors ([HowTo: Initialize entity values in the AI provider](https://wiki.genexus.com/commwiki/wiki?39302))

5 - Watson Assistant Errors

6 - Dialogflow Errors

7 - Context API(3) Errors ([HowTo: Manage the Context of the conversation through the Chatbot API](https://wiki.genexus.com/commwiki/wiki?41364))

| **Error Code** | **Description** | **Help** |
| --- | --- | --- |
| GXCF1001 | Configuration file {file} not found. | Check if the GXCF\_<InstanceName>Chatbot.config file exists under the virtual directory (or WEB-INF in case of java applications).  See [Synchronize Chatbot menu option](https://wiki.genexus.com/commwiki/wiki?40243) to know how to update the config file. If necessary, copy it to production. |
| GXCF1002 | Authentication error ({Provider}). | It's an Authorization Error.  Check at the [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113) if the credentials are correctly configured. See [Configuring GeneXus for using the Chatbot Generator](https://wiki.genexus.com/commwiki/wiki?37096).  Check that the GXCF\_<InstanceName>Chatbot.config file has the credentials correctly set according to the workspace (Watson) / Agent (Dialog Flow) you are trying to connect to. |
| GXCF1003 | Provider not found in the configuration file. | The GXCF\_<Instance>Chatbot.config file does not include the Provider. This happened for old versions (GX 16 upgrade 3 or prior). Since GX 16 upgrade 4 the configuration file has a new structure.  Solution: Synchronize the instance again to generate the config file. |
| GXCF1004 | {Provider} is not a Provider. | The GXCF\_<Instance>Chatbot.config file does not include a valid Provider.  Solution: Synchronize the instance again to generate the config file. |
| GXCF2001 | The Provider parameter is empty. | This error is thrown in an API call. In this case, the Provider parameter is missing. |
| GXCF2002 | The UserId parameter is empty. | This error is thrown in an API call (e.g: CleanUserContext). In this case, the UserId parameter is missing. |
| GXCF2003 | The Chatbot Instance parameter is empty. | This error is thrown in an API call (e.g: SetContextValue). In this case, the Chatbot Instance parameter is missing. |
| GXCF2004 | The message is empty. | This error is thrown in an API call.  An empty message is sent from the Provider. |
| GXCF3001 | The Instance parameter is empty. | This error is thrown in a **Flows API(1)** call (e.g: DeleteFlowTriggers). In this case, the Instance parameter is missing. |
| GXCF3002 | The Flow parameter is empty. | This error is thrown in a **Flows API(1)** call (e.g: GetFlowTriggers). In this case, the Flow parameter is missing. |
| GXCF3003 | The Triggers collection parameter is empty. | This error is thrown in **Flows API(1)** call (e.g: SendFlowTriggers). In this case, the Trigger Collection parameter is missing. |
| GXCF4001 | The ChatbotInstance parameter is empty. | This error is thrown in a **Entities API(2)** call (e.g: SendEntityValues). In this case, the ChatbotInstance parameter is missing. |
| GXCF4002 | The EntityValues parameter is empty. | This error is thrown in a **Entities API(2)** call (e.g: SendEntityValues). In this case, the EntityValues parameter is missing. |
| GXCF5001 | Watson workspace not found. | The Watson workspace defined at the GXCF\_<InstanceName>Chatbot.config does not exist at the Provider's. |
| GXCF5002 | Watson authentication type not found. | The Watson authentication type is not defined at the GXCF\_<InstanceName>Chatbot.config.  Edit the [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113), set the [Authentication Type property](https://wiki.genexus.com/commwiki/wiki?41262) correctly and save. This updates the .config file.  See also: [Synchronize Chatbot menu option](https://wiki.genexus.com/commwiki/wiki?40243) to know how to update the config file. |
| GXCF5003 | Watson user not found. | The Watson User is not defined at the GXCF\_<InstanceName>Chatbot.config.  Edit the [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113), set the [User Name property](https://wiki.genexus.com/commwiki/wiki?38932) correctly and save. This updates the .config file.  See also: [Synchronize Chatbot menu option](https://wiki.genexus.com/commwiki/wiki?40243) to know how to update the config file. |
| GXCF5004 | Watson password not found. | The Watson Password is not defined at the GXCF\_<InstanceName>Chatbot.config.  Edit the [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113), set the [Watson User Password property](https://wiki.genexus.com/commwiki/wiki?38933) correctly and save. This updates the .config file.  See also: [Synchronize Chatbot menu option](https://wiki.genexus.com/commwiki/wiki?40243) to know how to update the config file. |
| GXCF5005 | Watson api key not found. | The Watson api key is not defined at the GXCF\_<InstanceName>Chatbot.config.  Edit the [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113), set the [API Key property](https://wiki.genexus.com/commwiki/wiki?41263) correctly and save. This updates the .config file.  See also: [Synchronize Chatbot menu option](https://wiki.genexus.com/commwiki/wiki?40243) to know how to update the config file. |
| GXCF5006 | Watson region not found. | The Watson region is not defined at the GXCF\_<InstanceName>Chatbot.config.  Edit the [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113), set the [Region property in Conversational Flows Instance](https://wiki.genexus.com/commwiki/wiki?41264) correctly and save. This updates the .config file.  See also: [Synchronize Chatbot menu option](https://wiki.genexus.com/commwiki/wiki?40243) to know how to update the config file. |
| GXCF5007 | Watson ‘workspaceId’ not found. | This error is thrown when you execute an API call and the workspace Id is not present at the GXCF\_<InstanceName>Chatbot.config file.  Edit the [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113), set the [Workspace Id property](https://wiki.genexus.com/commwiki/wiki?39768) correctly and save. This updates the .config file.  See also: [Synchronize Chatbot menu option](https://wiki.genexus.com/commwiki/wiki?40243) to know how to update the config file. |
| GXCF5009 | ‘{value}’ is not a valid value for Watson authentication type. | The Watson Authentication type defined at the GXCF\_<InstanceName>Chatbot.config is not valid.  Edit the [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113), set the [Authentication Type property](https://wiki.genexus.com/commwiki/wiki?41262) correctly and save. This updates the .config file.  See also: [Synchronize Chatbot menu option](https://wiki.genexus.com/commwiki/wiki?40243) to know how to update the config file. |
| GXCF6001 | Dialogflow access token not found. | The access token is not defined at the GXCF\_<InstanceName>Chatbot.config.  Check the section "Configure the GeneXus Chabot instance for using Dialogflow" of [Configuring Google Dialogflow for the Chatbot Generator](https://wiki.genexus.com/commwiki/wiki?39749) to know how the access token is updated in the .config file. |
| GXCF6002 | Dialogflow client Id not found. | The client id is not defined at the GXCF\_<InstanceName>Chatbot.config.  Edit the [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113), set the [Client Id property](https://wiki.genexus.com/commwiki/wiki?39761) correctly and save. This updates the .config file.  See also: [Synchronize Chatbot menu option](https://wiki.genexus.com/commwiki/wiki?40243) to know how to update the config file. |
| GXCF6003 | Dialogflow client secret not found. | The client secret is not defined at the GXCF\_<InstanceName>Chatbot.config.  Edit the [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113), set the [Client Secret property](https://wiki.genexus.com/commwiki/wiki?39762) correctly and save. This updates the .config file.  See also: [Synchronize Chatbot menu option](https://wiki.genexus.com/commwiki/wiki?40243) to know how to update the config file. |
| GXCF6004 | Dialogflow project not found. | The project id is not defined at the GXCF\_<InstanceName>Chatbot.config.  Edit the [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113), set the [Google Cloud Project property](https://wiki.genexus.com/commwiki/wiki?39759) correctly and save. This updates the .config file.  See also: [Synchronize Chatbot menu option](https://wiki.genexus.com/commwiki/wiki?40243) to know how to update the config file. |
| GXCF6005 | Dialogflow refresh token not found. | The refresh token is not defined at the GXCF\_<InstanceName>Chatbot.config.  Check the section "Configure the GeneXus Chabot instance for using Dialogflow" of [Configuring Google Dialogflow for the Chatbot Generator](https://wiki.genexus.com/commwiki/wiki?39749) to know how the access token is updated in the .config file. |
| GXCF6006 | Dialogflow language code not found. | The language is not defined at the GXCF\_<InstanceName>Chatbot.config.  Edit the [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113), set the [Instance Language property](https://wiki.genexus.com/commwiki/wiki?41753) correctly and save. This updates the .config file.  See also: [Synchronize Chatbot menu option](https://wiki.genexus.com/commwiki/wiki?40243) to know how to update the config file. |
| GXCF7001 | User Context is empty. | Using the **Context API(3)**, the user context parameter is empty. |
| GXCF7002 | Parameter {Parameter} not found. | Using the **Context API(3)**, the parameter isn't found in the context when it is queried for it. |
| GXCF8001 | The chatbot cannot execute any of the responses defined for the current flow because its conditions did not evaluate to True in any case. To avoid this kind of error, defining a default response is recommended. | Define a [Chatbot Response](https://wiki.genexus.com/commwiki/wiki?39781) for the case that none of the [Conditions](https://wiki.genexus.com/commwiki/wiki?39491) evaluate to TRUE. |

### [See Also](#See+Also)

[Channels API - Troubleshooting](https://wiki.genexus.com/commwiki/wiki?44609)


|  |
| --- |
| **Backlinks** |
| [Chatbot Generator - Troubleshooting](https://wiki.genexus.com/commwiki/wiki?41260) | [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) | [HowTo: Initialize entity values in the AI provider](https://wiki.genexus.com/commwiki/wiki?39302) |
| [HowTo: Manage the Context of the conversation through the Chatbot API](https://wiki.genexus.com/commwiki/wiki?41364) | [HowTo: Manage training examples using the Chatbot Generator API](https://wiki.genexus.com/commwiki/wiki?41314) |

---
