---
title: "Update Android SDK tool"
source_id: 35473
source_url: https://wiki.genexus.com/commwiki/wiki?35473
genexus_version: "18"
---

# Update Android SDK tool

GeneXus provides a tool option for updating the Android-SDK component. In order to execute this option, an Android-SDK installation must exist on your machine and the [Android SDK Directory property](https://wiki.genexus.com/commwiki/wiki?31449) must indicate where it is located. The complete process consists of three simple steps.

**Warning**: If you are using multiple GeneXus upgrades and you need to upgrade Android-SDK, it is highly recommended you back-up the previous Android-SDK directory for previous GeneXus upgrade. Android-SDK may include not backward-compatible changes.

### [Step 1 - Execute the update from GeneXus](#Step+1+-+Execute+the+update+from+GeneXus)

Go to *Tools > Update Android SDK*. This option is visible only when the Knowledge Base has enabled the Smart Device Generator.

`[imagen omitida: wiki id 35455]`

### [Step 2 - Read the recommendations and conditions](#Step+2+-+Read+the+recommendations+and+conditions)

A warning dialog will be displayed alerting the user that the process is non-backward-compatible and the Android SDK Directory will be overwritten (property closely associated with the Knowledge Base and the Environment). We strongly recommend backing up this directory before starting the process. In case that we accept the conditions, an informational dialog will be displayed advising that the process won't provide visual feedback and may take a long time.

`[imagen omitida: wiki id 35456]`

### [Step 3 - Accept the Licence Agreements by Google](#Step+3+-+Accept+the+Licence+Agreements+by+Google)

A terminal will be opened, and Google forces us to accept two Licence Agreements (one for *android-sdk-license* and another for *intel-android-extra-licence*). When the command-line tool displays "Accept? (y/N): ", the user must write a "y" and press "Enter" in order to continue with the update process. This process may take a long time, but once it has finished, a dialog will be displayed advising the success of the operation.

`[imagen omitida: wiki id 35454]`

**Warning**: You must select an appropriate virtualization accelerator. See [Android Requirements](https://wiki.genexus.com/commwiki/wiki?14449), step 3.

### [Availability](#Availability)

This tool option is available as of [GeneXus 15 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?34646,,).


|  |
| --- |
| **Backlinks** |
| [Android - FAQ and Common Issues](https://wiki.genexus.com/commwiki/wiki?14575) | [Android Requirements](https://wiki.genexus.com/commwiki/wiki?14449) | [Android Requirements (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55100) |
| [Android Requirements (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?56500) | [Update Android SDK tool (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55101) |

---
