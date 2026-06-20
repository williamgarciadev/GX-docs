---
title: "HowTo: Use the ScanInLoop method from Scanner external object in Native Mobile applications"
source_id: 21663
source_url: https://wiki.genexus.com/commwiki/wiki?21663
genexus_version: "18"
---

# HowTo: Use the ScanInLoop method from Scanner external object in Native Mobile applications

The purpose of this article is to explain the necessary steps to configure and use the ScanInLoop method offered by the [Scanner external object](https://wiki.genexus.com/commwiki/wiki?31316).

This method returns a [Structured Data Type](https://wiki.genexus.com/commwiki/wiki?10021) of ScannedBarcodes, and receives a [Boolean data type](https://wiki.genexus.com/commwiki/wiki?4374) indicating if a beep will be played on each read.

`[imagen omitida: wiki id 54622]`

### [Sample](#Sample)

In this example, the ScanInLoop method is used to load a Grid with all the scanned codes (this is one way to use the information obtained, there are many ways to use it).

### [Step 1](#Step+1)

Define a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) with a variable defined as follows:

`[imagen omitida: wiki id 54623]`

### [Step 2](#Step+2)

Add the variable to the layout and add a button to start the scanning:

`[imagen omitida: wiki id 54624]`

### [Step 3](#Step+3)

Create a new Event for the "Start Scan" button to use this method.

```
Event 'Start Scan'
    Composite
       &ProductsRead = Scanner.ScanInLoop(True)
       refresh
    EndComposite
EndEvent
```

Note that the ScanInLoop = True has been defined, so a beep sound will be played each time a code is scanned.

When scanning the codes, it will automatically open the scan application and save each code it reads. When the scan is stopped, the application will return to the [Panel](https://wiki.genexus.com/commwiki/wiki?24829) created and all the scanned codes will be displayed.

**Notes:**

* In
  [Apple](https://wiki.genexus.com/commwiki/wiki?14917) this Scanner is available for iPhone, iPad2 and iPod with iOS 4.X.
* The beep sound is always played in [Android](https://wiki.genexus.com/commwiki/wiki?14453).


|  |
| --- |
| **Backlinks** |
| [Scanner external object](https://wiki.genexus.com/commwiki/wiki?31316) |

---
