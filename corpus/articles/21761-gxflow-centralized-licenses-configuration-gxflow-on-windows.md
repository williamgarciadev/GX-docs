---
title: "GXflow centralized licenses configuration (GXflow on Windows)"
source_id: 21761
source_url: https://wiki.genexus.com/commwiki/wiki?21761
genexus_version: "18"
---

# GXflow centralized licenses configuration (GXflow on Windows)

In order to configure a GXflow installation that runs on a Windows Server to use licenses from a [Protection Server](https://wiki.genexus.com/commwiki/wiki?37204) you must follow these steps:

## [License Server](#License+Server)

This is the Windows server where the licenses are installed. Do these steps on it:

1. Install [GeneXus Protection Server](https://wiki.genexus.com/commwiki/wiki?18887,,) (9.7.2.14 or higher)
2. Install GXflow Licenses
3. Add a local network user (that will be used for executing the application) to the windows group called "Artech Remote Protection Users" or "GeneXus Remote Protection Users".

## [Application Server](#Application+Server)

This is the Windows server where the application with GXflow is installed. Do these steps:

### [GeneXus 15 Upgrade 8 or higher](#GeneXus+15+Upgrade+8+or+higher)

Since the introduction of a new [GXflow license scheme](https://wiki.genexus.com/commwiki/wiki?37204), from GeneXus 15 Upgrade 8 there are no additional requirements to use centralized licenses.

Just set the License Protection Type to Protection Server in the [GXflow license manager](https://wiki.genexus.com/commwiki/wiki?37207).

### [GeneXus 15 Upgrade 7 or lower](#GeneXus+15+Upgrade+7+or+lower)

1. Install [GeneXus Protection Server](https://wiki.genexus.com/commwiki/wiki?18887,,) (9.1 or higher)
2. Setup up the remote server using "Select Computer" option
3. Setup up the user that will be used for executing the application (same as step 3). For this select the option "Select Computer" and then press the "Advanced" button.
4. Copy the protect.ini file from *C:\Program Files (x86)\Common Files\Artech\GXprot1* to *C:\Windows\System32.* If the application runs in 32 bits copy the protect.ini file to *C:\Windows\SysWow64*


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [GXflow license scheme](https://wiki.genexus.com/commwiki/wiki?37204) |

---
