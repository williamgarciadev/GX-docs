---
title: "Default Log Level property"
source_id: 33333
source_url: https://wiki.genexus.com/commwiki/wiki?33333
genexus_version: "18"
---

# Default Log Level property

Determines the default log level.

### [Values](#Values)

|  |  |
| --- | --- |
| **Debug** | Shows debug log messages that are useful during development only, as well as the other message levels in this list. |
| **Error** | Shows issues that have caused errors. |
| **Info** | Errors, warnings, and any other relevant information is saved. |
| **Off** | Default value. Logging is disabled. |
| **Warning** | Errors and warnings are saved. |

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

Set the log level desired related to the following properties:

* [Offline Synchronization Log Level property](https://wiki.genexus.com/commwiki/wiki?33331)
* [Http Connections Log Level property](https://wiki.genexus.com/commwiki/wiki?33332)
* [Offline Data Base Access Log Level property](https://wiki.genexus.com/commwiki/wiki?33330)

The order in terms of verbosity, from the least to the most verbose, is:

Off, Error, Warning, Info, Debug.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at run-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770). |


|  |
| --- |
| **Backlinks** |
| [Android UITest Log](https://wiki.genexus.com/commwiki/wiki?55471) | [Enable Logging property](https://wiki.genexus.com/commwiki/wiki?37876) | [HowTo: Enable logging for Native Mobile](https://wiki.genexus.com/commwiki/wiki?37846) |
| [Log external object](https://wiki.genexus.com/commwiki/wiki?37872) | [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817) | [Notification Provider API](https://wiki.genexus.com/commwiki/wiki?33687) |

---
