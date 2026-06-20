---
title: "HowTo: Get data from the Document Repository using the Workflow API"
source_id: 53542
source_url: https://wiki.genexus.com/commwiki/wiki?53542
genexus_version: "18"
---

# HowTo: Get data from the Document Repository using the Workflow API

The DocumentRepository object is the way to access your application's document information with the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350). Document instances and definitions can be a collection or a specific document.

For example, you can get a list of the document instances and display it in a [Grid](https://wiki.genexus.com/commwiki/wiki?24817) of a [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) by defining and executing the following code:

`[imagen omitida: wiki id 53543]`

```
Event Start
     &WorkflowServer.connect('<UserName>','<Password>')
Endevent

Event Grid.Refresh
    &WorkflowDocumentRepository = &WorkflowServer.GetDocumentRepository()
    &WorkflowDocumentInstances = &WorkflowDocumentRepository.ListDocumentInstances(&WorkflowFilter)
EndEvent

Event Grid.Load()
    For &WorkflowDocumentInstance in &WorkflowDocumentInstances
        &Name = &WorkflowDocumentInstance.Name
        &Version = &WorkflowDocumentInstance.Version
        &Created = &WorkflowDocumentInstance.Created
        &Author = &WorkflowDocumentInstance.Author.Name
        &Updated = &WorkflowDocumentInstance.Updated
        Grid.Load()
    endfor
Endevent
```

Where the data types variables are as follows:

```
&WorkflowServer – WorkflowServer
&WorkflowDocumentRepository – WorkflowDocumentRepository
&WorkflowDocumentInstance – WorkflowDocumentInstance
&WorkflowDocumentInstances – WorkflowDocumentInstance (collection)
&WorkflowFilter– WorkflowFilter
&Name – WorkflowName
&Version – WorkflowVersion
&Created – DateTime
&Author – WorkflowName
&Updated – DateTime
```

A list of document definitions can be obtained in a similar way with the method *&WorkflowDocumentRepository.ListDocumentDefinitions()*

You can also get a specific object with the following code:

```
&WorkflowServer.Connect(<UserName>,<Password>)
&WorkflowDocumentInstance = &WorkflowDocumentRepository.GetDocumentInstanceById(&Id)
```

Where the data types variables are as follows:

```
&WorkflowServer – WorkflowServer
&WorkflowDocumentRepository – WorkflowDocumentRepository
&WorkflowDocumentInstance – WorkflowDocumentInstance
```

A document definition can be obtained with the method *&WorkflowDocumentRepository.GetDocumentDefinitionById()*


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |

---
