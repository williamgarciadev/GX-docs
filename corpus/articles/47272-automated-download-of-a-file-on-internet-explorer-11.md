---
title: "Automated download of a file on Internet Explorer 11"
source_id: 47272
source_url: https://wiki.genexus.com/commwiki/wiki?47272
genexus_version: "18"
---

# Automated download of a file on Internet Explorer 11

When you want to download a file on Internet Explorer, it opens a download bar and we should manage it to download that. In this article, a workaround to download automatically a file on Internet Explorer 11 is provided.

## [Precondition](#Precondition)

When you click on the download button, the file must be  manually downloadable with the following keys sequence:  
      {F6}  
      {TAB}  
      {enter}

## [Solution](#Solution)

The workaround consists of the execution of this [auxiliary script](https://wiki.genexus.com/commwiki/wiki?47276,,) during the UI test execution. That script will be executed after clicking the download button with the [Shell function](https://wiki.genexus.com/commwiki/wiki?8502) and emulates the keys sequence shown in Precondition 2.

## [Example](#Example+)

For example, you can automate the download of the [auxiliary script](https://wiki.genexus.com/commwiki/wiki?47276,,) following the next steps:

1) [Download the auxiliary script](https://wiki.genexus.com/commwiki/wiki?47276,,) and save it in some directory, for the sake of this example it will be stored in C:// disk.

2) Create a UI test object in your KB with the following code:

```
//Start webdriver
&driver.Start()
&driver.Maximize()
// Initial navigation
&driver.Go("https://wiki.genexus.com/commwiki/wiki?47276,File%3Aexe+to+download+file+with+Internet+Explorer+11")
&driver.ClickByID("W0046W0015FILEDOWNLOADER")
&ret = shell('C:\\DownloadIE.exe',1)
&driver.End()
```

3) Run the UI test in Internet Explorer 11.

Note that depending on the file size, you should include a PauseFor command after the called [Shell function](https://wiki.genexus.com/commwiki/wiki?8502) to wait for the download to complete.


|  |
| --- |
| **Backlinks** |
| [GXtest Troubleshooting](https://wiki.genexus.com/commwiki/wiki?46828) |

---
