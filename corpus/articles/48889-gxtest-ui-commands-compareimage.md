---
title: "GXtest UI Commands - CompareImage"
source_id: 48889
source_url: https://wiki.genexus.com/commwiki/wiki?48889
genexus_version: "18"
---

# GXtest UI Commands - CompareImage

Compares the second image against the first one. Returns the percentage similarity as a decimal number, returning 100 if the images are completely equal. Images must have similar aspect ratios in order for the comparison to be performed.

**Parameters**

* OriginalImagePath (Character): the path of the image you want to compare the new image against. It also supports references to external images, such as those in a shared drive or the web.
* NewImagePath (Character): the path of the image you want to compare against the original. It also supports references to external images, such as those in a shared drive or the web.
* Tolerance (Numeric): [optional] a decimal value in a 0 to 100 range to choose the difference color tolerance when comparing each image pixel. The default value is 7.5 when no set.

**Returns**

* A decimal value between 0 and 100 representing the similarity percentage between the images compared. Fully equal images return 100.

**Examples**

```
&driver.Verify(&driver.CompareImage("C:\screenshot1.png","C:\screenshot2.png") >= 95, true, "Comparing screenshots") // Local images

&driver.Verify(&driver.CompareImage("C:\screenshot1.png","https://somewhere/screenshot2.png") > 99.5, true, "Comparing screenshots") // Local image vs web image

&driver.Verify(&driver.CompareImage(ExpectedPageAfterInsert.Link(),"currentScreenshot.png", 10) > 95, true, "Comparing screenshots") // KB image vs local relative path image, using a custom tolerance value
```

To view the differences between the images compared, click on the image icon associated with the CompareImage command. The differences will be highlighted with a pink fluor color.

**Disclaimers**

* The best results can be achieved by comparing images with the same resolution.
* Image diff visibility(in the TestResults' window) is only offered when the user compares two images with the same resolution.
* Two images with different resolutions will be compared as long as their aspect ratios (e.g. 16:9 when talking about FHD resolution) are similar. A square image and a rectangular image will give result 0 due to an aspect ratio incompatibility.
* Two images that appear similar can be really different in reality, for example, if one image is offset by 1px, every pixel in that image can potentially be different than the one in the original.
* Two images of the same website taken on two monitors with the same resolution but different scaling (OS setting) will not be comparable.
* Comparing two full-page screenshots of a webpage with dynamic content loading is not a good idea since the result might differ between executions due to loading times.

### [Availability](#Availability)

This command is available since GeneXus 17 upgrade 6.


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Changelog GXtest](https://wiki.genexus.com/commwiki/wiki?43807) |
| [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) | [GXtest UI Commands - CompareImage (GeneXus 18 Upgrade 3)](https://wiki.genexus.com/commwiki/wiki?54847) |

---
