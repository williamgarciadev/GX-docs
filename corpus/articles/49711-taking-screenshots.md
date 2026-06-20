---
title: "Taking screenshots"
source_id: 49711
source_url: https://wiki.genexus.com/commwiki/wiki?49711
genexus_version: "18"
---

# Taking screenshots

These commands allow saving as files specific elements within a webpage and the page itself. Page screenshots can be full or of the viewport only.

## [TakeScreenshot](#TakeScreenshot)

`[imagen omitida: wiki id 47312]`

Captures a screenshot of the page and saves it to an image file. If the file already exists, it is overwritten. This function will use the value of the  [*Full Page Screenshot* property](https://wiki.genexus.com/commwiki/wiki?45420) in order to determine whether to take a screenshot of the viewport or the whole page.

Parameters:

* filePath: an absolute or relative path to the file to be saved.
* imageFormat: It is recommended to use PNG format always (imageFormat = 0)
  + 0 - png (java and .net)
  + 1 - jpg (only for .net)
  + 2 - gif (only for .net)
  + 3 - tiff (only for .net)
  + 4 - bmp (only for .net)

`[imagen omitida: wiki id 48373]`

Captures a screenshot of the page and saves it to an image file. If the file already exists, it is overwritten. With the third parameter, the user has the possibility to define whether or not a full-page screenshot will be taken, overriding the property-defined behavior.

Parameters:

* filePath: an absolute or relative path to the file to be saved.
* imageFormat: It is recommended to use PNG format always (imageFormat = 0)
  + 0 - png (java and .net)
  + 1 - jpg (only for .net)
  + 2 - gif (only for .net)
  + 3 - tiff (only for .net)
  + 4 - bmp (only for .net)
* fullPage: wether to take the screenshot as full page or not

Examples of use:

```
&driver.TakeScreenshot("../photos_wp.png", 0)

&driver.TakeScreenshot("../photos_wp.png", 0, true)
```

If you need, take a look at the implementation [example to not overwrite the screenshots](https://wiki.genexus.com/commwiki/wiki?47209) for the different executions of the same test.

DISCLAIMER

**The following functions depend upon the machine where the test is executed having 100% scaling set on its operating system's configuration. Taking screenshots with other scaling values IS NOT SUPPORTED.**

## [TakeScreenshotByControlName](#TakeScreenshotByControlName)

Captures a screenshot of the control with the given name and saves it to an image file. If the file already exists, it is overwritten.

Parameters:

* controlName: name of the control as defined in the KB.
* imagePath: an absolute or relative path to the file to be saved.

Examples of use:

```
&driver.TakeScreenshotByControlName("submitButton", "../photos_wp.png")
```

## [TakeScreenshotByControlName](#TakeScreenshotByControlName)

Captures a screenshot of the control with the given name in a given row and saves it to an image file. If the file already exists, it is overwritten.

Parameters:

* controlName: name of the control as defined in the KB.
* row: the row number where the control is located
* imagePath: an absolute or relative path to the file to be saved.

Examples of use:

```
&driver.TakeScreenshotByControlName("submitButton", 2, "../photos_wp.png")
```

## [TakeScreenshotByCSS](#TakeScreenshotByCSS)

Captures a screenshot of the element with given CSS selector and saves it to an image file. If the file already exists, it is overwritten.

Parameters:

* css: the CSS selector.
* imagePath: an absolute or relative path to the file to be saved.

Examples of use:

```
&driver.TakeScreenshotByCSS("#something .somethingElse", "../photos_wp.png")
```

## [TakeScreenshotById](#TakeScreenshotById)

Captures a screenshot of the element with the given id and saves it to an image file. If the file already exists, it is overwritten.

Parameters:

* id: the value of the id attribute.
* imagePath: an absolute or relative path to the file to be saved.

Examples of use:

```
&driver.TakeScreenshotById("elementId", "../photos_wp.png")
```

## [TakeScreenshotByLinkText](#TakeScreenshotByLinkText)

Captures a screenshot of the element with the given link text and saves it to an image file. If the file already exists, it is overwritten.

Parameters:

* linkText: the text of the link.
* imagePath: an absolute or relative path to the file to be saved.

Examples of use:

```
&driver.TakeScreenshotByLinkText("Home", "../photos_wp.png")
```

## [TakeScreenshotByName](#TakeScreenshotByName)

Captures a screenshot of the element with the given name attribute and saves it to an image file. If the file already exists, it is overwritten.

Parameters:

* name: the name of the element.
* imagePath: an absolute or relative path to the file to be saved.

Examples of use:

```
&driver.TakeScreenshotByName("HomeButton", "../photos_wp.png")
```

## [TakeScreenshotByXPath](#TakeScreenshotByXPath)

Captures a screenshot of the element with given XPath and saves it to an image file. If the file already exists, it is overwritten.

Parameters:

* xpath: the XPath to the element.
* imagePath: an absolute or relative path to the file to be saved.

Examples of use:

```
&driver.TakeScreenshotByXPath("//*[@id="MPW0050TABLE1"]/div[1]", "../photos_wp.png")
```


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) |

---
