---
title: "Printer external object"
source_id: 48131
source_url: https://wiki.genexus.com/commwiki/wiki?48131
genexus_version: "18"
---

# Printer external object

The Printer external object enables you to print files (with PDF, PNG, JPG, and TXT extensions) from an Android application directly to a Bluetooth printer connected to the device.

`[imagen omitida: wiki id 53922]`

You can find the Printer object in the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210) within the SD module, which is in turn located within the GeneXus module. That is to say, it is part of the [Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288).

## [Properties](#Properties)

### [PrinterName](#PrinterName)

Sets the name of the printer to be used for printing. The name must match the Bluetooth name of the device.

### [Dpi](#Dpi)

Sets the resolution of the printer. Check the manufacturer's manual. The default value is 203 dpi.

### [Width](#Width)

Sets the printable width. The default value is 48 mm. For the Leopardo A7 printer, the value is 208 mm.

## [Methods](#Methods)

### [GetDevices method](#GetDevices+method)

Returns a list with the names of the devices previously connected. It doesn't distinguish printers.

|  |  |
| --- | --- |
| **Return value** | [VarChar](https://wiki.genexus.com/commwiki/wiki?6778) |
| **Parameters** | None. |

### [Print method](#Print+method)

Uses the current printer to print the specified file.

Supported file extensions are PDF, PNG, JPG, and TXT.

PDFs and images are scaled down if they are too wide based on the settings, but they aren't scaled up.

It automatically connects if necessary and it disconnects if 15 minutes of inactivity have passed.

|  |  |
| --- | --- |
| **Return value** | None. |
| **Parameters** | Path:VarChar, [Rotation:Rotation]. |

Rotation is a numeric value that indicates the rotation of the report. The possible values are as follows:

* 0: Prints normally. Default value.
* 1: Rotates left before printing.
* 2: Rotates right before printing.

### [CutPaper method](#CutPaper+method)

For printers that support this method, it cuts the paper.

|  |  |
| --- | --- |
| **Return value** | None. |
| **Parameters** | None. |

## [Events](#Events)

It doesn't have any.

## [Considerations](#Considerations)

* Only [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293)s that have PDF output are supported. That is to say, they must contain the Output\_File(!'<FileName>', !'PDF') rule. In addition, their [Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?20911) value must be "Offline".
* The code that uses the external object must be included inside a client-side event (even if the [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) has its Connectivity Support property = "Online"). The Panel object must have its [Use PDF Reports property](https://wiki.genexus.com/commwiki/wiki?42887) set to True.

## [Troubleshooting](#Troubleshooting)

* In some printers, if an incorrect value is entered in the Width property, the printout may contain unreadable characters.
* When printing PDF reports, the pages of the report are printed. Therefore, if the last page has a lot of extra white space, this will be reflected in the printout. The page size is determined by the Paper Height property of the Layout.

## [Scope](#Scope)

**Generators:**[Android](https://wiki.genexus.com/commwiki/wiki?14453)


|  |
| --- |
| **Backlinks** |
| [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) | [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) |

---
