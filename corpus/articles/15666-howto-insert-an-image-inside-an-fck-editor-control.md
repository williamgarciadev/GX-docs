---
title: "HowTo: Insert an image inside an FCK Editor Control"
source_id: 15666
source_url: https://wiki.genexus.com/commwiki/wiki?15666
genexus_version: "18"
---

# HowTo: Insert an image inside an FCK Editor Control

The purpose of this article is to explain the necessary steps to insert an image inside an [FCK Editor control](https://wiki.genexus.com/commwiki/wiki?4858).

There are two ways to upload an insert images inside an FCK Editor Control:

**1.**  By using the control’s File Manager, which allows you to upload and insert images, browse previously uploaded files, etc. This solution implies that a script needs to be configured to call a **PHP** program to handle the file upload. For further information check [here](http://docs.cksource.com/CKEditor_3.x/Developers_Guide/File_Browser_%28Uploader%29). This [SAC](http://www2.gxtechnical.com/portal/hgxppredirect.aspx?15,26,0,,,30291) details how to integrate it with GeneXus.

**2.** By adding a button to the FCK Editor and using a GeneXus object to upload and insert the image. This is an easy way to upload images by just using GeneXus objects:  
  
Requirements:

* [GeneXus X Evolution 1](https://wiki.genexus.com/commwiki/wiki?9256,,) Upgrade 3 or higher
* [Uploadify User Control](http://marketplace.genexus.com/viewproduct.aspx?128) (Version 1.4)

### [Steps](#Steps)

**1.** Add an *Insert image* button in the FCKeditor toolbar.

**2.** Create the “uploader” object, which allows you to select an image from your local disc and automatically sends it to the server.

**3.** Insert the new file reference on the FCKeditor body.

### [Step 1 - Insert a button on the FCKEditor Toolbar](#Step+1+-+Insert+a+button+on+the+FCKEditor+Toolbar)

To insert a button in the FCKEditor toolbar, add this code in the object’s Start Event:

```
Event Start
    &FCKEditorMenuItem.Id = "upload"
    &FCKEditorMenuItem.Description = "Upload"
    &FCKEditorMenuItem.Icon = ActionUpdate.Link()
    &FCKEditorMenuItem.ObjectInterface = FckEditorObjectInterface.Dialog
    &FCKEditorMenuItem.Link = FileUploader.Link("")  // Object URL that will be opened as a popup inside the dialog.
    &FCKEditorMenu.Add(&FCKEditorMenuItem)
    &HTML.SetMenu(&FCKEditorMenu)
EndEvent
```

Where *&HTML* is the control of type FCK html editor. It can be a Attribute or variable.

Check the property **&FCKEditorMenuItem.Link**; this is needed to be configured with the GeneXus Object that will upload the image.

### [Step 2 - Uploader Object](#Step+2+-+Uploader+Object)

Create a
[Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) called “*FileUploader*” (the name that you set in &FCKEditorMenuItem.Link). Then insert on it the Uploadify User Control.

This control is just a button that will automatically upload the file (image) on the server once it has been clicked.

### [Step 3 - Insert the imagen inside the dialog](#Step+3+-+Insert+the+imagen+inside+the+dialog)

In order to insert the uploaded imagen on the FCKEditor body, add this event in the “FileUploader” object:

```
Event Uploadify1.OnComplete
    &blob.FromString(Uploadify1.UploadedTemporalFileName)
    &url = pathtourl(&blob)
    &ImgHtml = Format(!'<img src=%1>', &url)
    return
EndEvent
```

And this rule:

```
parm(out: &ImgHtml);
```

The event gets the uploaded file from the server (**Uploadify1.UploadedTemporalFileName**) and returns its URL.

The object first output parameter will be automatically inserted in the FCKEditor Body.

That’s all.  You can get this example (xpz) from [here](https://wiki.genexus.com/commwiki/wiki?15667,,).


|  |
| --- |
| **Backlinks** |
| [FCK HTML Editor Control](https://wiki.genexus.com/commwiki/wiki?4858) |

---
