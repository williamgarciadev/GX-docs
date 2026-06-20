---
title: "Example to not overwrite the screenshots"
source_id: 47209
source_url: https://wiki.genexus.com/commwiki/wiki?47209
genexus_version: "18"
---

# Example to not overwrite the screenshots

If you need to save all the screenshots of the [takeScreenshot command](https://wiki.genexus.com/commwiki/wiki?41616) in the different executions of the same test, this article provides a possible solution.

As a possible solution, we propose that the UI test creates a folder with the name of the test execution date and saves the screenshots in that folder with a unique name of "date\_hour". This way the captures will not be replaced.

The following code is the UI test code which it will code two auxiliary procedures written below:

```
// UI test with takeScreenShot command implementation 
//Start webdriver
&driver.Start()
&driver.Maximize()
//Folder creation to save screenshots
&absFolderName = folderCreation()
//First screenshot
&driver.Go("https://www.genexus.com/en/products/gxtest")
&ScreenshotFile.Source = &absFolderName + "\" + screenShotName()
&driver.takeScreenshot(&ScreenshotFile.GetAbsoluteName(), 0) 
//Second screenshot
&driver.Go("https://abstracta.us/") 
&ScreenshotFile.Source = &absFolderName + "\" + screenShotName() 
&driver.takeScreenshot(&ScreenshotFile.GetAbsoluteName(), 0) 
//End webdriver
&driver.End()
```

The following code is the folderCreation() procedure implementation:

```
// folderCreation auxiliar procedure implementation
&now = now()
//convert now variable to string
&nowVar = &now.ToFormattedString()
/*to convert nowVar in folder Name 
i.e. &nowVar=11/02/2020 10:46:13 AM -->  &folderName="11-02-2020"
*/
&pattern = "\b(\d{1,2})/(\d{1,2})/(\d{2,4})\s(\d{1,2}):(\d{1,2}):(\d{1,2})\s(AM|PM)\b"
&folderName = &nowVar.ReplaceRegEx(&pattern, "$1$2$3")
//folder creation in c:\
&ScreenshotDirectory.Source = "c:\GXtestScreenshots"
&ScreenshotDirectory.Create()
//&folderName folder creation
&ScreenshotDirectory.Source = &ScreenshotDirectory.GetAbsoluteName() + "\" + &folderName
&ScreenshotDirectory.Create()
//to save and to return the folder path in which the screenshots will be saved
&absFolderName = &ScreenshotDirectory.GetAbsoluteName()
```

The following code is the screenShotNow() procedure implementation:

```
// screenShotName auxiliar procedure implementation
&now = now()
//convert now variable to srting
&nowVar = &now.ToFormattedString()
/*to save and to return part of the screenshort name in the variable &screenShotName 
i.e. &nowVar=11/02/2020 10:46:13 AM -->  &screenShotName="11022020_104613"
*/
&pattern = "\b(\d{1,2})/(\d{1,2})/(\d{2,4})\s(\d{1,2}):(\d{1,2}):(\d{1,2})\s(AM|PM)\b"
&screenShotName = &nowVar.ReplaceRegEx(&pattern, "$1$2$3_$4$5$6") + ".png"
```


|  |
| --- |
| **Backlinks** |
| [Taking screenshots](https://wiki.genexus.com/commwiki/wiki?49711) |

---
