---
title: "Web UI test browsers compatibility"
source_id: 46393
source_url: https://wiki.genexus.com/commwiki/wiki?46393
genexus_version: "18"
---

# Web UI test browsers compatibility

The following table shows the supported browsers by generator type:

| Browser | [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892) | [.NET](https://wiki.genexus.com/commwiki/wiki?38604) | [Java](https://wiki.genexus.com/commwiki/wiki?12258) |
| --- | --- | --- | --- |
| Google Chrome | Yes | Yes | Yes |
| Mozilla Firefox | Yes | Yes | Yes |
| Internet Explorer | Yes | Yes | Yes |
| Edge Legacy | Yes | Yes | Yes |
| Edge (Chromium) | Yes | Yes | Yes |

### [Compatibility issues](#Compatibility+issues)

GXtest releases its versions being compatible with the latest browsers at the time that the release was made. So, it is possible that if you are not using the latest GXtest version, you get a compatibility error.

Typically this happens with Google Chrome and Edge Chromium browsers.

In this case, what you have to do is:

**1.** Download the proper Chromedriver for your Chrome version from <https://chromedriver.chromium.org/downloads>. For Chromedriver versions 115 and up, visit <https://github.com/GoogleChromeLabs/chrome-for-testing#json-api-endpoints> to get endpoint URLs to download the appropriate Chromedriver.

**2.** Extract the content of the downloaded file and copy the chromedriver.exe file

**3.** Paste the file in <GX\_PROGRAM\_DIR>/Packages/GXtestFiles/UIObjects/

That's it! The next time you run the test, it will be working again.

### [Other browsers](#Other+browsers)

In case you are having compatibility trouble with another browser, you can follow the same procedure.

Edge and Edge Legacy drivers' site: <https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/>

Firefox driver site: <https://github.com/mozilla/geckodriver/releases>


|  |
| --- |
| **Backlinks** |
| [GXtest Troubleshooting](https://wiki.genexus.com/commwiki/wiki?46828) |

---
