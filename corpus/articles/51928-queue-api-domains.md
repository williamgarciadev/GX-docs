---
title: "Queue API domains"
source_id: 51928
source_url: https://wiki.genexus.com/commwiki/wiki?51928
genexus_version: "18"
---

# Queue API domains

The following are the domains under the *GeneXusMessagingQueue.SimpleQueue module*, defined to be used by the [Queue API](https://wiki.genexus.com/commwiki/wiki?51771) methods.

## [MessageStatus](#MessageStatus)

Enumerated domain with the Status of the message after being sent.

* Unknown
* Sent
* Deleted
* Failed

## [MessageQueueProviderProperty](#MessageQueueProviderProperty)

Enumerated domain with the name of the Environment Variables to be used, to connect to the Queue without hard coding the connection credentials.

By defining the Environment variables, the method [AWSQueue.MessageQueueProvider external object](https://wiki.genexus.com/commwiki/wiki?51778) and [AzureQueue.MessageQueueProvider external object](https://wiki.genexus.com/commwiki/wiki?51737) can receive empty values for the credential parameters.

`[imagen omitida: wiki id 51929]`

###


|  |
| --- |
| **Backlinks** |
| [Toc:Asynchronous messaging APIs](https://wiki.genexus.com/commwiki/wiki?51735) | [AWSQueue.MessageQueueProvider external object](https://wiki.genexus.com/commwiki/wiki?51778) | [AzureQueue.MessageQueueProvider external object (GeneXus 18 Upgrade 5)](https://wiki.genexus.com/commwiki/wiki?55673) |
| [HowTo: Connect to a Queue](https://wiki.genexus.com/commwiki/wiki?51761) |

---
