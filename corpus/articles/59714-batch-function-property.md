---
title: "Batch Function property"
source_id: 59714
source_url: https://wiki.genexus.com/commwiki/wiki?59714
genexus_version: "18"
---

# Batch Function property

Determines whether messages received from the Service Bus are processed individually or in batches.

### [Values](#Values)

|  |  |
| --- | --- |
| **False** | Messages are processed one by one as they arrive. |
| **True** | Messages are collected and processed in batches. This can improve efficiency but may increase resource consumption. |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

The "Batch Function" property, available in the [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) dialog when you set [Service Bus](https://wiki.genexus.com/commwiki/wiki?49355) as the [Trigger Type](https://wiki.genexus.com/commwiki/wiki?51466), determines how your application handles incoming messages.

`[imagen omitida: wiki id 59728]`

Enabling batch processing (setting the property to "true") can reduce the overhead of processing each message individually. This is particularly beneficial when dealing with related messages that can be processed together. However, large batches can demand more memory and resources.

#### [Considerations for choosing batch processing:](#Considerations+for+choosing+batch+processing%3A)

* **Message interdependency:** Batch processing is efficient for related messages that need to be processed as a group.
* **Resource availability:** Ensure your system has sufficient memory and resources to handle potentially large batches.

#### [Cases where individual message processing (non-batch) is useful:](#Cases+where+individual+message+processing+%28non-batch%29+is+useful%3A)

* **Real-time or time-sensitive processing:** For immediate responses or actions, such as transaction confirmations or critical event processing, individual processing is more suitable.
* **Independent messages:** When messages are unrelated and don't have dependencies, processing them individually simplifies logic.
* **Variable or large message sizes:** If messages vary significantly in size or are potentially large and exceed batch size limits, individual processing is recommended.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [See Also](#See+Also)

* [Trigger Type property](https://wiki.genexus.com/commwiki/wiki?51466)
* [HowTo: Deploy as Azure Functions](https://wiki.genexus.com/commwiki/wiki?49351)

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 12](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?59446,,).
