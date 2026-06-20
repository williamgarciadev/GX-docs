---
title: "GeneXus Debugger and Profiling common issues"
source_id: 11013
source_url: https://wiki.genexus.com/commwiki/wiki?11013
genexus_version: "18"
---

# GeneXus Debugger and Profiling common issues

The following issues may occur when [Debugging](https://wiki.genexus.com/commwiki/wiki?9307) or [Profiling](https://wiki.genexus.com/commwiki/wiki?9308,,) an application.

### [Message error](#Message+error)

Warning: <Object Name> debuggable program. No debugger found at: <Computer Name>

or

Warning: <Object Name> under code coverage testing and no host found at: <Computer Name>  
Description: Unable to connect to the remote server

Where Computer Name is where GeneXus is being executed.

### [Cause and Solutions](#Cause+and+Solutions)

* **Cause:** UAC (User Access Control) is enabled (Windows Vista or higher)
* **Solution:** Run GeneXus as administrator (right-button, 'Run as Administrator')

* **Cause:** The firewall is blocking the debugger.
* **Solution:** add GeneXus.exe as an exception in the Firewall. Follow the steps shown in the image below:

`[imagen omitida: wiki id 11016]`

### [Check connectivity between the Debugger and the application](#Check+connectivity+between+the+Debugger+and+the+application)

Follow the steps to test the connectivity between the debugger and the application.

1. Open GeneXus.

2. Open a command prompt console and run: *telnet machinename 6776.*

`[imagen omitida: wiki id 11017]`

**Note**: *6776* is the default port number used by the debug tool window (DebuGx), but sometimes could be different. To know the real port number being used, open the source code of some debuggable program and search for Gxdebug.setPort (for Java) or Gxdebug.Port (for .NET).

2. Press <Enter>.

`[imagen omitida: wiki id 11018]`

3. Press Y (or y).

`[imagen omitida: wiki id 11019]`

If you run the application in Debug mode, the console will show traffic between the application and GeneXus Debugger.


|  |
| --- |
| **Backlinks** |
| [Debugging in GeneXus](https://wiki.genexus.com/commwiki/wiki?9307) |

---
