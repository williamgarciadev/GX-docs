---
title: "GXtest config file"
source_id: 45137
source_url: https://wiki.genexus.com/commwiki/wiki?45137
genexus_version: "18"
---

# GXtest config file

GXtest has some properties that can be used to customize how GXtest uses resources in GeneXus.  
The file is **Abstracta.GXtest.BL.dll.config** and can be found in <GeneXusProgramDir>/Packages/. In case you want to edit its values, you must restart the IDE so that the changes take effect.

These properties are:

* **version**: used to check if UITestSD external object must be updated
* **UITestSD**: the path to XPZ file that contains external object needed to execute UI tests for mobile applications
* **testResultFileName**: name for XML file that GXtest reads to show execution results.
* **executionDataFileName**: name for JSON file used by GXtest as execution parameter to runner object
* **exportTestResultsTemplate**: Path to HTML template report to be used when using the feature Export Results in the Test Results window
* **gxtestModuleVersion**: GXtest module version to use for this extension in this GeneXus installation (available since GXtest for GX16 U8). It uses the latest by default
* **gxtestModuleId**: GXtest module identifier
* **applicationsRegistryKey**: registry keys to search installed applications
* **browsersMainRegistryKey**: registry key to search for installed browsers
* **browsersSecondaryRegistryKey**: secondary registry key to search for installed browsers
* **recorderExtensionURL**: GXtest Recorder chrome extension URL to launch when using [Recorder-IDE integration](https://wiki.genexus.com/commwiki/wiki?48448) feature
* **recorderHomeURL**: home URL to navigate when launching the GXtest Recorder using Google Chrome
* **recorderToken**: token used to detect that the new script was sent from the GXtest Recorder to the GeneXus IDE


|  |
| --- |
| **Backlinks** |
| [Test Preferences](https://wiki.genexus.com/commwiki/wiki?45420) | [Test Preferences (GeneXus 18 Upgrade 6)](https://wiki.genexus.com/commwiki/wiki?56007) | [Test Preferences (GeneXus 18)](https://wiki.genexus.com/commwiki/wiki?52980) |

---
