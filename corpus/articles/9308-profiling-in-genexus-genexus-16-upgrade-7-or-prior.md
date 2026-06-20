---
title: "Profiling in GeneXus (GeneXus 16 Upgrade 7 or prior)"
source_id: 9308
source_url: https://wiki.genexus.com/commwiki/wiki?9308
genexus_version: "18"
---

# Profiling in GeneXus (GeneXus 16 Upgrade 7 or prior)

Profiling is used to help fix performance problems by means of running the application and keeping track of what was executed, how many times and for how long.

**Deprecated**: Since [GeneXus 16 upgrade 8](https://wiki.genexus.com/commwiki/wiki?44913,,). Replaced by [Code Coverage and Profiling](https://wiki.genexus.com/commwiki/wiki?44369).

Follow these basic steps to profile your application:

1. Change to Performance Test mode

`[imagen omitida: wiki id 9329]`

2. Add objects to the Performance Test Objects tool window. These are the objects that will be monitored

`[imagen omitida: wiki id 9330]`

3. Select Menu / Performance Test / Start Capture to start capturing performance information

`[imagen omitida: wiki id 9331]`

4. The profiler is capturing information:

`[imagen omitida: wiki id 9332]`

5. Execute the application and select Stop when done. The performance analysis tool window is displayed for you to analyze

`[imagen omitida: wiki id 9333]`

**Important:**

* This feature only applies to objects without an interface, as Procedures or Data Providers. Otherwise, the results could be distorted by time interface.
* The profiler uses a port number to establish a connection with GeneXus. In case of connection problems see [GeneXus Debugger and Profiling common issues](https://wiki.genexus.com/commwiki/wiki?11013)

### [See also](#See+also)

[Debugging in GeneXus](https://wiki.genexus.com/commwiki/wiki?9307)

[GeneXus Debugger and Profiling common issues](https://wiki.genexus.com/commwiki/wiki?11013)


|  |
| --- |
| **Backlinks** |
| [Configuration options](https://wiki.genexus.com/commwiki/wiki?11087) | [Debugging in GeneXus](https://wiki.genexus.com/commwiki/wiki?9307) | [GeneXus Debugger and Profiling common issues](https://wiki.genexus.com/commwiki/wiki?11013) |
|

---
