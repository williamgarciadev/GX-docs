---
title: "GeneXusUIControls module"
source_id: 60714
source_url: https://wiki.genexus.com/commwiki/wiki?60714
genexus_version: "18"
---

# GeneXusUIControls module

The GeneXusUIControls module provides controls to simplify the creation of user interfaces.

It can be installed by selecting [Knowledge Manager Menu](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?5679,,) > [Manage Module References](https://wiki.genexus.com/commwiki/wiki?40172) in the GeneXus main menu.

It contains two submodules:

### [1. Chat submodule](#1.+Chat+submodule)

This submodule includes the Chat Control and objects for building conversational user interfaces.

* [Chat Control](https://wiki.genexus.com/commwiki/wiki?59254)**:** Allows you to integrate chat experiences into Web and Angular applications. It can be used, for example, to interact with an [Agent object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?59249,,). It can also be used for a standard chat between a user and the application, without the need for an agent.
* **MessageUI:** A [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021) that defines the structure and layout of a chat message:

  ```
      MessageUI
      {
          id: Character(20)
          role: 'MessageRole, GeneXusUIControls.Chat' //Enum Values: System, User, Agent, Error
          content: Character(20)
          status: 'MessageStatus, GeneXusUIControls.Chat'  //Enum Values: Complete, Waiting, Streaming
          sources (Collection = 'True')
          {        
              source
              {
                 url:'Url, GeneXus'
                 caption: Character(20)
                 accessibleName: Character(20)            
              }
      }
  ```
* **Domains:** [GeneXus Domains](https://wiki.genexus.com/commwiki/wiki?7221) that define roles and statuses for messages. They are:  
  + 'MessageRole' Domain
    - Data Type: Varchar(20)
    - Enum Values: System, User, Agent, Error
  + 'MessageStatus' Domain
    - Data Type: Varchar(20)
    - Enum Values: Complete, Waiting, Streaming
* **Translations:** A Structured Data Type that stores localized texts for chat interactions.
* **TranslationsProvider:** A[Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) to dynamically handle translations.

### [2. IntersectionObserver submodule](#2.+IntersectionObserver+submodule)

This submodule includes the [Intersection Observer control](https://wiki.genexus.com/commwiki/wiki?55147).


|  |
| --- |
| **Backlinks** |
| [Chat Control](https://wiki.genexus.com/commwiki/wiki?59254) | [GeneXus 18 Upgrade 14](https://wiki.genexus.com/commwiki/wiki?59631) |
| [GeneXusUI module (GeneXus 18 Upgrade 13 or prior)](https://wiki.genexus.com/commwiki/wiki?60716) | [HowTo: Use the Chat Control associated with a Procedure that calls a Globant Enterprise AI API (GeneXus 18 latest upgrade or prior)](https://wiki.genexus.com/commwiki/wiki?61106) |
| [Intersection Observer control](https://wiki.genexus.com/commwiki/wiki?55147) |

---
