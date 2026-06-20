---
title: "Printing text reports on the client machine without changing the printer settings"
source_id: 28296
source_url: https://wiki.genexus.com/commwiki/wiki?28296
genexus_version: "18"
---

# Printing text reports on the client machine without changing the printer settings

### [Scenario](#Scenario)

The scenario covered here is that of a web application where text reports are generated and will be printed on the client machine (where the browser runs).  
The printer used will be selected by the end user through the printer dialog. However, the default printer can be used after doing some configuration in the browser only once, and no printer dialog should be shown. The [Printer rule](https://wiki.genexus.com/commwiki/wiki?11734) isn't used in these reports, and neither is the [gxprn.ini file](https://wiki.genexus.com/commwiki/wiki?17091), so different print settings can't be combined in this scenario.

The solution is independent of the platform, the server or client machines.

### [Configuration](#Configuration)

This configuration is necessary for GeneXus X Evolution 2, GeneXus 15, and GeneXus 16. Edit (or create the file if it does not exist) the config.gx file in the root of the KB, and add the following:

```
AvoidPrintingApplet=Y
```

### [Example](#Example)

Consider the following text report, whose properties are shown below:

* [Report output property](https://wiki.genexus.com/commwiki/wiki?7943) = Only to printer
* [Output device location property](https://wiki.genexus.com/commwiki/wiki?14110) = Client

Besides, it hasn't got the Printer rule.

`[imagen omitida: wiki id 28297]`

Once the report is created, it can be called from any web panel.   
The printer dialog will be shown before sending the print command to the printer.

### [Silent Printing](#Silent+Printing)

The [Show printer dialog on reports property](https://wiki.genexus.com/commwiki/wiki?9004) is ignored for this implementation.

If you want to avoid the printer dialog, you can do some configuration in the browser.

When using Chrome, you need to add the following parameters to execute it:  --kiosk-printing

`[imagen omitida: wiki id 28298]`

When using FireFox,

1. Type about:config in Firefox’s location bar and hit Enter.
2. Right-click anywhere on the page and select New > Boolean
3. Enter the preference name as print.always\_print\_silent and click OK.

`[imagen omitida: wiki id 28299]`

In IE there are similar settings.

Note that the reports that have a printer rule in the KB will be run as usual, using the print applet.

See [Printing text reports using the client’s printer and changing the printer settings](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?13722,,).

###


|  |
| --- |
| **Backlinks** |
| [Web printing on client printer (without an applet)](https://wiki.genexus.com/commwiki/wiki?33912) |

---
