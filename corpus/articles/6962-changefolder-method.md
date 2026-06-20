---
title: "ChangeFolder method"
source_id: 6962
source_url: https://wiki.genexus.com/commwiki/wiki?6962
genexus_version: "18"
---

# ChangeFolder method

Changes the folder from which the messages will be received.

### [Syntax](#Syntax)

**&***DataType***.ChangeFolder(** [ *FolderName* ] **)**

**Type Returned:**   
Numeric

**Where:**  
*FolderName*  
   Is the name of the folder from which the emails will be read. This is an optional parameter; if it is bypassed or left blank, a reference to the Inbox folder will be made.

### [Scope](#Scope)

**Extended Data Types:** [MAPISession](https://wiki.genexus.com/commwiki/wiki?6935), [OutlookSession](https://wiki.genexus.com/commwiki/wiki?6936)  
**Generators:** 

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

Rules for the Correct Definition of the Folder Names:

The notation is similar to the one used in DOS and UNIX to navigate directories, with some exceptions. The rules are usually the following:

* The “.” character can be used to indicate the current folder.
* The  “..” string can be used to indicate a higher level folder.
* The “\” character can be used to indicate a sub-folder.
* The  “\” character can be used at the beginning of the name to indicate the root.

If a simple name is specified, without “\” or “..”, it will refer to an Inbox sister folder. “\*Inbox”, “\*Outbox”, “\*Sent Items”, “\*Deleted Items” and “\*Drafts” values will be used to indicate the folders that are usually called such names, even if their names are not exactly those. This is useful when a client is used in another language. For instance, in the Spanish version of Outlook, “\*Inbox” will refer to the “Inbox” folder regardless of the name it has in Spanish.

If you have the following structure:

Mailbox  
                Drafts  
                Inbox  
                           Urgent    
                Outbox  
                Pending  
                           On Hold  
                Sent Items  
Public Folders  
                Favorites  
                All Public Folders  
                           General  
  
The following FolderName values are valid:

* “Pending”
* “Pending\On Hold”
* “\Mailbox\Pending”
* “\Public Folders\All Public Folders\General”
* “\*Inbox\Urgent”

If the folder currently chosen is Inbox\Urgent:

* “..” (Selects Inbox)
* “..\..\Pending\On Hold”

If the folder currently chosen is Inbox:

* “.\Urgent”

**Note**: This method returns an error code, so it is possible to call it as a (**&**Err **= &**DataType**.ChangeFolder(.....)**) function.

### [See Also](#See+Also)

[Receive Method](https://wiki.genexus.com/commwiki/wiki?6964)  
[Send Method](https://wiki.genexus.com/commwiki/wiki?6965)  
[MAPISession Data Type](https://wiki.genexus.com/commwiki/wiki?6935)  
[OutlookSession Data Type](https://wiki.genexus.com/commwiki/wiki?6936)


|  |
| --- |
| **Backlinks** |
| [MAPISession Data Type](https://wiki.genexus.com/commwiki/wiki?6935) | [NewMessages Property](https://wiki.genexus.com/commwiki/wiki?6961) | [OutlookSession Data Type](https://wiki.genexus.com/commwiki/wiki?6936) |

---
