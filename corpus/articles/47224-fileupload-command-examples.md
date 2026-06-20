---
title: "FileUpload command examples"
source_id: 47224
source_url: https://wiki.genexus.com/commwiki/wiki?47224
genexus_version: "18"
---

# FileUpload command examples

In this article, you will find examples of [FileUpload command](https://wiki.genexus.com/commwiki/wiki?45868) implementation in two different controls.

## [Automated file upload in File Upload User control](#Automated+file+upload+in+File+Upload+User+control)

Web Panel with a [FileUploadData](https://wiki.genexus.com/commwiki/wiki?30574) variable called “FileUploadData”:

`[imagen omitida: wiki id 47226]`

The variable view is the following:

`[imagen omitida: wiki id 47227]`

To automated upload a file you have to use the commands [FileUploadByName](https://wiki.genexus.com/commwiki/wiki?45868) and  [ClickBy](https://wiki.genexus.com/commwiki/wiki?41647), in example:

```
//Start webdriver
&driver.Start()
&driver.Maximize()
// Initial navigation
&driver.Go(webpanelName.Link())
//automated files upload
&driver.FileUploadByName("files[]","path\PDFexample.pdf")
&driver.FileUploadByName("files[]","path\PDFexample2.pdf")
//...more files.. 
&driver.ClickByCSS("#FILEUPLOAD1Container > div > div.row.fileupload-buttonbar > div.col-lg-7 > button.btn.btn-primary.start > span")
&driver.End()
```

Notes:  
\* “files[]” is the name of “+Add files...” button  
\* The click command over is over the “Start upload” button to load the files

## [Automated file upload in Blob data type](#Automated+file+upload+in+Blob+data+type)

Web Panel with a [Blob variable](https://wiki.genexus.com/commwiki/wiki?6704) called “AttacheBlob”:

`[imagen omitida: wiki id 47228]`

The variable view is:

`[imagen omitida: wiki id 47229]`

To automated upload a file you have to use the command [FileUploadByName](https://wiki.genexus.com/commwiki/wiki?45868). Optionally, you can verify the name upload file with the command [Verify](https://wiki.genexus.com/commwiki/wiki?45806):

```
//Start webdriver
&driver.Start()
&driver.Maximize()
// Initial navigation
&driver.Go(webpanelName.Link())
//automated file upload
&driver.FileUploadByName("vATTACHEBLOB","PDFUploadfile.pdf")
//verify the name of the upload file 
&driver.Verify((&driver.GetValueByName("vATTACHEBLOB").Contains("PDFUploadfile.pdf")))
&driver.End()
```


|  |
| --- |
| **Backlinks** |
| [GXtest UI Commands - File Upload](https://wiki.genexus.com/commwiki/wiki?45868) |

---
