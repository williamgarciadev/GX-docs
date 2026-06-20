---
title: "Recorder-IDE integration"
source_id: 48448
source_url: https://wiki.genexus.com/commwiki/wiki?48448
genexus_version: "18"
---

# Recorder-IDE integration

## [Prerequisites](#Prerequisites)

* GeneXus IDE (Version 17 upgrade 5 and onwards)
* Google Chrome
* [GXtest Recorder](https://chrome.google.com/webstore/detail/gxtest-recorder/edbiefalppkhegcephbbcojpibobbdbd) chrome extension

## [Usage](#Usage)

In order to use this feature, the user must click the Record Web UI Test option in the Test menu, within the IDE.

`[imagen omitida: wiki id 48449]`

Once that happens, they will be prompted to create a new Web UI Test object. After creation, Google Chrome will be launched, as well as the recorder extension, already recording. This means that the recording will be ready and listening as soon as you start browsing within that Google Chrome window.

`[imagen omitida: wiki id 53809]`

Once you are satisfied with the state of your script, you should click the "Export to IDE" button. After that, you should check your IDE window, since it will be showing a popup message stating that the test has been modified outside the IDE, and ask the user whether they want to reload the test. When the user accepts, the test object will be updated and the script captured with the recorder extension will already be there, ready to be run or modified.

`[imagen omitida: wiki id 48451]`

## [Disclaimer](#Disclaimer)

Once the user has exported the recording to the IDE, the option will disappear and only a copy to clipboard option will be available. If the user wishes to work further within the recorder after exporting, they can, and once they are done they can just click the copy to clipboard button and paste the contents within their test object in the IDE.


|  |
| --- |
| **Backlinks** |
| [GXtest config file](https://wiki.genexus.com/commwiki/wiki?45137) | [GXtest Menu Commands](https://wiki.genexus.com/commwiki/wiki?48103) | [GXtest Menu Commands (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54365) |
| [GXtest Menu Commands (GeneXus 18)](https://wiki.genexus.com/commwiki/wiki?52983) |

---
