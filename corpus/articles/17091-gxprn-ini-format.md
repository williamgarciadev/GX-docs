---
title: "GXPRN.INI Format"
source_id: 17091
source_url: https://wiki.genexus.com/commwiki/wiki?17091
genexus_version: "18"
---

# GXPRN.INI Format

This document details the *gxprn.ini* file format. In this file, you can define many "forms" with different printing settings to be used by a GeneXus report or procedure [Printer Rule](https://wiki.genexus.com/commwiki/wiki?11734).

The file format is the following:

```
[FORMNAME_1]
<Key_1> = <Value_1>
<Key_2> = <Value_2>
...
<Key_N> = <Value_N>

[FORMNAME_2]
...

[FORMNAME_N]
...
```

For each Form (Printer rule settings) there is a NAME within brackets and all the printing parameters; the form name must be uppercase.

If you define a blank bracket ([]); it will be used as default settings when the Genexus object does not have the [printer rule](https://wiki.genexus.com/commwiki/wiki?11734) defined.

The parameters are:

|  |  |  |
| --- | --- | --- |
| **Key** | **Value** | **Description** |
| UseDefaultSettings | 0 | Apply gxprn.ini's form settings. |
| 1 | Use printer's default settings: it will print with the printer's default settings ignoring the form's settings. |
| Printer |  | Set the printer name as it was installed. |
| XOffset  YOffset |  | Paper upper left corner point coordinate to start printing. |
| Mode | 0 | Show Printer Dialog: Never |
| 2 | Show Printer Dialog: If sent directly to a printer |
| 3 | Show Printer Dialog: Always |
| Orientation | 1 | Portrait (Vertical) |
| 2 | Landscape (Horizontal) |
| PaperSize | 1 | Letter |
| 9 | A4 |
| 11 | A5 |
| 13 | B5 |
|  | Other paper sizes are printer dependant. |
| PaperLength  PaperWidth |  | Paper size in millimeters x 10.  Example: If the paper size is 297mm x 210 mm ,then PaperLength = 2970 and PaperWidth = 2100. |
| Copies |  | The number of copies to print. |
| DefaultSource |  | Paper source (Tray 1, Tray 2, Labels, etc). The values are printer dependant. |
| PrintQuality |  | Quality printing. The values are printer dependant.  Examples: 600x600 points PrintQuality = 600, 300x300 points PrintQuality = 300 for the HP LaserJet 6MP. |
| Color | 1 | Black and white. |
| 2 | Color. |
| TextEject  (only text mode) | FF | [Eject](https://wiki.genexus.com/commwiki/wiki?8592) Command: Form Feed |
| Skip | [Eject](https://wiki.genexus.com/commwiki/wiki?8592) Command: Skip PL Lines (default value) |
| Duplex | 1 | Simplex, print only on one side of the sheet. |
| 2 | Duplex, print on both sides of the sheet. |

The following sample details two sections: a general one [] and [MyPrinter] .

```
[MYPRINTER]
Scale= 0
Color= 1
Copies= 1
PrintQuality= 0
Duplex= 1
PaperWidth= 16834
PaperSize= 256
PaperLength= 11909
Orientation= 0
Mode= 3
DefaultSource= 1

[]
Scale= 0
Color= 1
Copies= 2
PrintQuality= 0
Duplex= 2
PaperWidth= 11909
PaperSize= 256
PaperLength= 16834
Orientation= 2
Mode= 3
DefaultSource= 1
```

Notice that this file is read-only once when the first report is executed, any change made to the file after that will force you to restart the application. It is recommended to modify the file while the application is offline.


|  |
| --- |
| **Backlinks** |
| [Printer rule](https://wiki.genexus.com/commwiki/wiki?11734) | [Printing text reports on the client machine without changing the printer settings](https://wiki.genexus.com/commwiki/wiki?28296) |
|

---
