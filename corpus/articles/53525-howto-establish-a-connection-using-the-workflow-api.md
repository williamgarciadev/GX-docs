---
title: "HowTo: Establish a connection using the Workflow API"
source_id: 53525
source_url: https://wiki.genexus.com/commwiki/wiki?53525
genexus_version: "18"
---

# HowTo: Establish a connection using the Workflow API

This article explains how to establish a connection using the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350), since an established connection is essential to be able to use most of the API.

To do so, you can execute the following code:

```
&WorkflowServer.Connect(&UserName,&Password)
commit
```

Also, you can keep the connection with the WorkflowWebSession domain; otherwise, you will need to use the Connect() method each time you need to use the API. It is necessary to import this domain from the [Custom Client KB](https://wiki.genexus.com/commwiki/wiki?48897).

```
&WebSession.Set(WorkflowWebSession.SessionHandle, &WorkflowServer.Session)
&WebSession.Set(WorkflowWebSession.UserCode, &UserName)
```

Finally, if you want to create an external login for the [Standard Client](https://wiki.genexus.com/commwiki/wiki?17835) you need to use the following code:

```
&WorkflowServer.Connect(&Name, &Password)
commit
&Websession.Set(!'WorkflowUser', &Name)
&Websession.Set(!'WorkflowPassword', &Password)
Link(!"wfautosignin.aspx")
```

Where the data type variables are as follows:

```
&WorkflowServer – WorkflowServer
&WebSession – WebSession
&UserName – WorkflowName
&Password – WorkflowPassword
```


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |

---
