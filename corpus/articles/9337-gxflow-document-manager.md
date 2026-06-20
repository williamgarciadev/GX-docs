---
title: "GXflow Document Manager"
source_id: 9337
source_url: https://wiki.genexus.com/commwiki/wiki?9337
genexus_version: "18"
---

# GXflow Document Manager

Through this application, a process administrator user can view all the documents that were created in the system. This application is only visible if the Enable option is set to Yes in [Document Management](https://wiki.genexus.com/commwiki/wiki?10118). The Documents Manager interface is shown in the image below:

`[imagen omitida: wiki id 52388]`

The following sections describe the different components that make up this application.

### [Actions](#Actions)

* **Read**: This option allows reading the document.
* **Rename**: This option allows renaming the document.
* **Check In**: This option allows you to upload new document versions to the document repository of the workflow system.

  For this action to be available, two conditions have to be met:

  The document type must have the Change action enabled in the task where the Work with Documents was executed.  
  The user who wants to upload the new document version must have previously executed the *Change Document* action.  
  Once a user uploads a new version of a document to the repository, it is unlocked and it can be changed by other users.
* **Check Out**: This action downloads a copy of the last version of the document in the user's PC, which will be used to perform the modification.  
  When a user executes this action on a document, it is locked for the exclusive use of the user that executed the Modify Document action. This implies that other users will not be enabled to modify the document until the modification is completed through the check in action.  
  A document will have this action enabled only if the type of document it belongs to has the modification action enabled in the task where Work with Documents was executed.
* **Undo Check Out**: It allows undoing the check out action.
* **Remove**: This option allows deleting documents from the documents repository of the workflow system. This means that every existing version of the documents will be physically deleted from the repository.  
  A document will have this action enabled only if the type of document it belongs to has the Delete action enabled in the task where Work with Documents is being executed.
* **Versions**: It shows the different versions of a document.
* **Extended Attributes**: It allows adding extended attributes to a document.

### [Documents Grid](#Documents+Grid)

This grid has the following options:

`[imagen omitida: wiki id 52012]` It allows selecting the columns that should be visible.  
`[imagen omitida: wiki id 52013]` It allows refreshing the grid.  
It is possible to sort some columns by clicking on their title.

This grid has the following columns:

**`[imagen omitida: wiki id 52389]` Comments**: This column will display the icon, which will allow the user to view the comments associated with the document.**`[imagen omitida: wiki id 52390]`Signed**: When a document has been digitally signed, this column gives access to a dialog with details of the digital signature and the certificate used to sign the document.  
**`[imagen omitida: wiki id 52391]`Locked**: This column shows whether the document is locked by a user to modify it. Bear in mind that when a user executes the Modify action on a document, it will remain locked until the user completes the modification.  
**Type**: This column shows the format of each document through the icon identifying it.  
**Id**: Document Id  
**Name**: Document name  
**Versions**: Document version.  
**Type**: It shows the document type. Be careful not to confuse the type with the format. Formats may be Word, Excel, or PDF, among others, while document types are exclusive for each workflow application.  
**Created**: Creation date.  
**Updated**: Update date.  
**Author**: User that was the author of a document. This column will always show the desktop user.  
**Check Out By**: User that checked out the document.  
**Check Out Time**: Time when the document was last checked out.

For an overview of GXflow client, refer to the [GXflow Client General Structure](https://wiki.genexus.com/commwiki/wiki?7896,,) section.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [HowTo: Use GXflow Entry Point User Control](https://wiki.genexus.com/commwiki/wiki?10721) |

---
