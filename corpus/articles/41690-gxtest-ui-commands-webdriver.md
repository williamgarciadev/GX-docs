---
title: "GXtest UI Commands - WebDriver"
source_id: 41690
source_url: https://wiki.genexus.com/commwiki/wiki?41690
genexus_version: "18"
---

# GXtest UI Commands - WebDriver

WebDriver is a [w3c standard](https://www.w3.org/TR/webdriver1/) to handle test automation on the most popular browsers. GXtest takes advantage of this standard while providing an abstraction layer in GeneXus to create UI tests.

There are 3 main functions to start a new UI test. By default, all tests will run in a local browser using a driver unless you specify the opposite:

* [SetBrowser](https://wiki.genexus.com/commwiki/wiki?41690)
* [Start](https://wiki.genexus.com/commwiki/wiki?41690)
* [End](https://wiki.genexus.com/commwiki/wiki?41690)

If you don't specify a browser type inside your test (using the SetBrowser function) the test will run using the Knowledge Base property that is set under the Test section:

`[imagen omitida: wiki id 47929]`

As a good practice if you want to run tests on another browser, change this property instead of setting the browser type inside the test.

## [SetBrowser](#SetBrowser)

`[imagen omitida: wiki id 46666]`

Sets the browser type to be used in the test.

Parameters:

* browser: A string with browser type (you can use Browsers domain for this purpose like the example)

Examples of use:

```
&driver.SetBrowser(Browsers.Firefox)
```

```
&driver.SetBrowser("Chrome")
```

Note: As mentioned, it is recommended to avoid using this function and change the default browser property in the KB properties instead.

## [GetBrowser](#GetBrowser)

`[imagen omitida: wiki id 46667]`

Gets the current browser set.

Returns:

* the browser where the test is running on

Examples of use:

```
if &driver.GetBrowser() = Browsers.Firefox
    // do something only when the browser is Firefox
endif
```

## [Start](#Start)

`[imagen omitida: wiki id 41693]`

Starts a test session using WebDriver

Example of use:

```
&driver.Start()
```

## [End](#End)

`[imagen omitida: wiki id 41694]`

Ends a test session using WebDriver

Example of use:

```
&driver.End()
```

To run tests on any remote web driver node (Selenium node or Cloud), you can use these 2 functions:

## [AddCapability](#AddCapability)

`[imagen omitida: wiki id 46790]`

Adds a desired [capability](https://github.com/SeleniumHQ/selenium/wiki/DesiredCapabilities) for a WebDriver node. It allows to set browser preferences by prefixing the pref:: in the capabilityName parameter too.

Parameters:

* capabilityName: A capability key name.
* capabilityValue: The capability desired value.

Returns: n/a

Example of use:

```
&driver.AddCapability("AddExtension","thePathToExtension\fileName.crx") // to add an extension
&driver.AddCapability("UnhandledPromptBehavior", "Dismiss") // to choose the behavior when an alert is shown
```

For downloading PDF files without prompting in Chrome:

```
&driver.AddCapability("pref::download.prompt_for_download", "false")
&driver.AddCapability("pref::list::plugins.plugins_disabled", "Chrome PDF Viewer")
&driver.AddCapability("pref::plugins.always_open_pdf_externally", "true")
```

Remote:

```
&driver.AddCapability("browserName", "MicrosoftEdge")
&driver.AddCapability("platform", "Windows 10")
&driver.AddCapability("version", "16.16299")
```

## [SetArguments](#SetArguments)

`[imagen omitida: wiki id 47928]`

Sets browser's start arguments, e..g. --headless to run without the graphic interface. It must be used before the start command. For more information about available options check [Arguments property](https://wiki.genexus.com/commwiki/wiki?45420)

Parameters:

* Arguments: browser arguments separated by spaces.

Example of use:

```
&driver.SetArguments("--headless --incognito")
```

## [SetRemoteWebDriver](#SetRemoteWebDriver)

`[imagen omitida: wiki id 46791]`

Sets a remote WebDriver node URL to spin remote browsers.

Parameters:

* url: The remote WebDriver node URL.

Example of use:

```
&driver.SetRemoteWebDriver("http://[USER]:[KEY]@testmachine.mydomain.com:4444/wd/hub")
```


|  |
| --- |
| **Backlinks** |
| [Table of contents:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Table of contents:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) |
| [GXtest UI Commands - Property Setters](https://wiki.genexus.com/commwiki/wiki?48468) | [GXtest UI Commands - WebDriver](https://wiki.genexus.com/commwiki/wiki?41690) | [GXtest UI Commands - WebDriver (GeneXus 18 Upgrade 8 or prior)](https://wiki.genexus.com/commwiki/wiki?57767) | [GXtest UI Commands - WebDriver (GeneXus 18 Upgrade 8 or prior)](https://wiki.genexus.com/commwiki/wiki?57767) |
| [GXtest UI Test for Web - Supported Commands](https://wiki.genexus.com/commwiki/wiki?40281) | [Running tests on different browsers](https://wiki.genexus.com/commwiki/wiki?41128) |

---
