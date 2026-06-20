---
title: "GXtest UI Commands - Property Setters"
source_id: 48468
source_url: https://wiki.genexus.com/commwiki/wiki?48468
genexus_version: "18"
---

# GXtest UI Commands - Property Setters

All the [test preferences](https://wiki.genexus.com/commwiki/wiki?45420) that can be set on your [KB](https://wiki.genexus.com/commwiki/wiki?2428) and environments have an associated setter method in the GXtest webdriver that is used before each test execution. This means you can override the value set in the KB properties in any test by just adding one of the following commands in it.

## [SetArguments](#SetArguments)

Official documentation page: [SetArguments command](https://wiki.genexus.com/commwiki/wiki?41690)

## [SetBaseURL](#SetBaseURL)

Official documentation page: [SetBaseURL command](https://wiki.genexus.com/commwiki/wiki?41616)

## [SetBrowser](#SetBrowser)

Official documentation page: [SetBrowser command](https://wiki.genexus.com/commwiki/wiki?41690)

## [SetLogLevel](#SetLogLevel)

`[imagen omitida: wiki id 48759]`

Sets the web UI tests' verbosity level at execution time.

Parameters:

* LogLevel: the chosen log level to set. Check [*Log Level* property article](https://wiki.genexus.com/commwiki/wiki?45420) for information about the values available.

Example of use:

```
&driver.SetLogLevel("Debug")
&driver.SetLogLevel("Warn")
```

## [SetFileUploadBasePath](#SetFileUploadBasePath)

Official documentation page: [SetFileUploadBasePath command](https://wiki.genexus.com/commwiki/wiki?45868)

## [SetFullPageScreenshot](#SetFullPageScreenshot)

`[imagen omitida: wiki id 48472]`

Sets the default type of screenshot GXtest takes. Visit [FullPageScreenshot property](https://wiki.genexus.com/commwiki/wiki?45420) for more details.

Parameters:

* Value: the value indicating if the page screenshots are full (true) or not (false).

Example of use:

```
&driver.SetFullPageScreenshot(true)
```

## [SetHtmlMode](#SetHtmlMode)

`[imagen omitida: wiki id 48493]`

Sets the situations in which the page HTML must be saved.

Parameters:

* Mode: the value to set. See all the available values in the [HTML Mode property page](https://wiki.genexus.com/commwiki/wiki?45420)

Example of use:

```
&driver.SetHTMLMode("OnVerifyAndError")
&driver.SetHTMLMode("Never")
```

## [SetScreenshotMode](#SetScreenshotMode)

`[imagen omitida: wiki id 48494]`

Sets the situations in which a page screenshot must be saved.

Parameters:

* Mode: the value to set. See all the available values in the [Screenshot Mode property page](https://wiki.genexus.com/commwiki/wiki?45420)

Example of use:

```
&driver.SetScreenshotMode("OnError")
&driver.SetScreenshotMode("Always")
```

## [SetVerifyStopsExecution](#SetVerifyStopsExecution)

Official documentation page: [SetVerifyStopsExecution](https://wiki.genexus.com/commwiki/wiki?45806)


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) |

---
