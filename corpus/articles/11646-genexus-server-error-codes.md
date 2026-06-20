---
title: "GeneXus Server Error Codes"
source_id: 11646
source_url: https://wiki.genexus.com/commwiki/wiki?11646
genexus_version: "18"
---

# GeneXus Server Error Codes

The following list details [GeneXus Server](https://wiki.genexus.com/commwiki/wiki?9911) error codes.

|  |  |
| --- | --- |
| **Code** | **Message** |
| **srv001** | CheckoutFailed: Occurs when the server can not generate the data to be sent to the client. |
| **srv002** | ConnectionOK: Connection with the server went OK. |
| **srv003** | FeedError: There was an error creating the feed. |
| **srv004** | FrozenVersion: Version is frozen, you will not be able to commit here. |
| **srv005** | InvalidKB: Your local Knowledge Base is not linked to the one in the server you're trying to commit to. |
| **srv006** | KBHosted: Knowledge Base already hosted in this server. |
| **srv007** | NoHostedKB: Knowledge Base is not hosted on this server. |
| **srv008** | NoPermissionsOnDB: User not allowed to acces the data base. |
| **srv009** | NoPrototypeFound: The sent KB must have an environment. |
| **srv010** | OutOfTime: Client and Server are out of time. |
| **srv011** | NotAvailable: Server Not available. |
| **srv012** | NotValidRequest: Invalid request. |
| **srv013** | NoPermissionOnCatalog: User does not have writing permission on catalog file. |
| **srv014** | LockingMessage: Cannot perform operation on KB. |
| **srv015** | InvalidGX: Incompatible versions. |
| **srv016** | NotAuthorized: You are not authorized to perform this action. |
| **srv017** | CouldNotReadCatalogFile: Error while reading catalog file. |
| **srv018** | CouldNotGetLocation: Could not get Knowledge Base. |
| **srv019** | NoVersionFound: Invalid version sent from client. |
| **srv020** | ServerLockingMessage: Canno perform this action right now, there's another one in progress. |
| **srv021** | ServerExclusiveLock: Server busy. |
| **srv022** | WrongVersion: Incompatibility between GX and GXServer. |
| **srv023** | InvalidVersionRequested: Invalid Version Requested. VersionId:{0}, VersionName:{1}. |
| **srv024** | InvalidFolderName: Invalid folder name:'{0}'. Please send the Knowledge Base with a different alias. |
| **srv025** | RevisionNotFound: No revision found at '{0}' in version '{1}' of Knowledge Base '{2}'. |
| **srv026** | NoActionsFound: No objects found on revision '{0}' of version '{1}' in Knowledge Base '{2}'. |
| **srv027** | InvalidObjectType: Invalid object type found:{0}. |
| **srv028** | InvalidPackageObjectType: Object type {0} ({1}) by '{2}' not found. |
