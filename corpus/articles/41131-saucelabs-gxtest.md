---
title: "Saucelabs GXtest"
source_id: 41131
source_url: https://wiki.genexus.com/commwiki/wiki?41131
genexus_version: "18"
---

# Saucelabs GXtest

Since GXtest is Remote WebDriver compatible, running UI tests on the cloud using Saucelabs or any similar service is easy. You will just need a Saucelabs account (user and accessKey).

Once you have it, replace them properly on the following code example:

```
//Run on the cloud, on any browser / device / PC  (saucelabs)
&driver.SetRemoteWebDriver("http://[USER]:[KEY]@ondemand.saucelabs.com:80/wd/hub")
&driver.AddCapability("browserName", "MicrosoftEdge")
&driver.AddCapability("platform", "Windows 10")
&driver.AddCapability("version", "16.16299")
```

This example will launch your test using Windows 10 and Edge v16.

You can change the platform, browser, and version using [Saucelabs Platform Configurator](https://wiki.saucelabs.com/display/DOCS/Platform+Configurator#/).

Using Saucelabs you will be able to:

* Run tests over thousands of browser/platform combination sets
* Scale and run tests in parallel
* Forgetting about provisioning browser / OS
* Video recording and test dashboard.


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) |

---
