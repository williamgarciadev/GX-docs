---
title: "Use PDF Reports property"
source_id: 42887
source_url: https://wiki.genexus.com/commwiki/wiki?42887
genexus_version: "18"
---

# Use PDF Reports property

Indicates whether PDF reports are used in your offline mobile application (to include the necessary library).

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974)  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

This property has to be set for the Main object that invokes PDF reports in your offline native mobile application.

Note: By default, the [Menu object](https://wiki.genexus.com/commwiki/wiki?16321) has its [Main program property](https://wiki.genexus.com/commwiki/wiki?7407) set to True. As a result, the Use PDF Reports property will be shown, in order to set it to True. On the other hand, for a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) or a [Work With pattern and Work With object](https://wiki.genexus.com/commwiki/wiki?15974), you must first set their [Main program property](https://wiki.genexus.com/commwiki/wiki?7407) to True to have the Use PDF Reports property displayed.

Legal Notice for Android: iText 5.x is used, which requires an AGPL or Commercial License. More information at [External utilities used by GeneXus generated Android applications](https://wiki.genexus.com/commwiki/wiki?25098).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

Consider a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) that defines an offline PDF report.

It must have the following properties configured:

* [Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?20911) = Offline
* [Report output property](https://wiki.genexus.com/commwiki/wiki?7943) = Only to file

And the following rule:

* Output\_file("ReportName.pdf", "PDF")

The PDF file is generated in the device and saved in the TemporaryFilesPath directory.

To open the report, you have to define the following:

```
&filePath = Directory.TemporaryFilesPath + & file.Separator + 'ReportName.pdf'
&fileUrl =! 'file: //' + & filePath
if Interop.CanOpen(&fileUrl)
     Interop.Open(&fileUrl)
endif
```

Lastly, the Main offline object that includes the PDF report call must have the Use PDF Reports property set to True.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770).

### [Availability](#Availability)

This property is available since [GeneXus 16 upgrade 4](https://wiki.genexus.com/commwiki/wiki?42755,,).


|  |
| --- |
| **Backlinks** |
| [Printer external object](https://wiki.genexus.com/commwiki/wiki?48131) |

---
