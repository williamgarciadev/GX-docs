---
title: "GetAgentServiceHeader method of GAM object"
source_id: 43221
source_url: https://wiki.genexus.com/commwiki/wiki?43221
genexus_version: "18"
---

# GetAgentServiceHeader method of GAM object

Gets the correct header to execute an HTTP call to a service using GAM.

### [Syntax](#Syntax)

GAM.**GetAgentServiceHeader(**in: *GAMServiceTypesHeader*, out: *&HeaderName*, out: *&HeaderValue***)**

**Where:**

*GAMServiceTypesHeader*  
     Is a domain which has the values {SmartDevice, STSOAuth}

*&HeaderName* and *&HeaderValue*Are out parameters, which have to be used to call the service afterwards.

### [Description](#Description)

Depending on the security of the service, the header should be different. The purpose of this method is to get the correct one.

### [Samples](#Samples)

Consider the example of calling a service under the [Security Token Service Client Authorization](https://wiki.genexus.com/commwiki/wiki?43202) mechanism.  
A client application (AppA) requests access to another application (AppB) - for example, to execute a service of this application.

After having asked for the access token, using the [GetSTSAuthorizationAccessToken method of GAMRepository Object](https://wiki.genexus.com/commwiki/wiki?43218), you can ask for the correct headers before executing the service in AppB.

Note that in this example, the **STSOauth** value of GAMServiceTypesHeader domain is used.

```
    GAM.GetAgentServiceHeader(GAMServiceTypesHeader.STSOauth, &HeaderName, &HeaderValue)
    &StrCall = "http://localhost/ClientSTS2.NetEnvironment/rest/ProcRest_testSTS"
    &httpClient.AddHeader(&HeaderName, &HeaderValue)
    &httpClient.AddHeader(!"Content-Type",!"application/x-www-form-urlencoded")
    &httpClient.AddHeader(!"Authorization", &access_token)
    &httpClient.AddVariable(!"client_id", &client_id)
    &httpClient.Execute(!"POST", &StrCall)
    &ResultHttpC = &httpClient.ToString()
```

### Availability

Since [GeneXus 16 upgrade 4](https://wiki.genexus.com/commwiki/wiki?42755,,)


|  |
| --- |
| **Backlinks** |
| [HowTo: Access secure REST services defined via API Objects](https://wiki.genexus.com/commwiki/wiki?52864) | [HowTo: Configure GAM to use Security Token Service](https://wiki.genexus.com/commwiki/wiki?43206) | [HowTo: Upload an image, video, or audio file via an API object](https://wiki.genexus.com/commwiki/wiki?51411) |

---
