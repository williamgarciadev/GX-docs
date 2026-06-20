---
title: "Image object"
source_id: 23387
source_url: https://wiki.genexus.com/commwiki/wiki?23387
genexus_version: "18"
---

# Image object

Stores an image inside the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836).

### [Description](#Description)

Images are embedded objects in a [GeneXus](https://wiki.genexus.com/commwiki/wiki?1756) [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836). They hold the definition and the actual image(s) of an image that you can use anywhere you need in your Knowledge Base. Having images as objects in the Knowledge Base provides several benefits, including:

* Cross reference. You know where images are used.
* Images can depend on [Themes](https://wiki.genexus.com/commwiki/wiki?4375), Languages or [Density](https://wiki.genexus.com/commwiki/wiki?24062). Apps know which actually to use depending on the context.
* [Import/Export](https://wiki.genexus.com/commwiki/wiki?5679) objects with the images they use. There's no more need for additional zip files with images.

### [Creating an Image](#Creating+an+Image)

An Image can be created by selecting in the main GeneXus Menu: File > New > Object (or its shortcut keys Ctrl-N), but most of the time you will create a new image when you need to select one to fill the value of a property or anywhere you need an image.  
Say, for example, you want to show an image in a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916). You can drag an Image control from the Toolbox into the form. At this time you are prompted to select one of the available images (those already existing in your Knowledge Base). The dialog will look like the one shown below. It has a filter field at the top, a list of image names on the left and a preview pane on the right. There are also two buttons at the bottom of the list of images.  
  
`[imagen omitida: wiki id 4826]`  
  
The "*Import from file"* button lets you create a new [GeneXus](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?3146,,) Image from a file stored in your file system. It opens a file selector and, once you have selected an image file, a new dialog like the one below is opened, prompting you to provide basic information on the image you are creating.  
  
`[imagen omitida: wiki id 4828]`  
  
At this time, just give the name you want to assign to the Image object, and ignore other dialog options. If the default name suits you, just hit the OK button and you're done.

### [External Images](#External+Images)

There may be images you do not "control". For example, you need to reference an image belonging to another company on the Internet, or you just want to share images between applications in your company. These are external images. They are basically the same as internal ones in terms of functionality, but the actual image is not stored in your Knowledge Base. Only its address (URL) is stored there.  
  
Creating an external image is almost the same as creating an internal one. [Drag](https://wiki.genexus.com/commwiki/wiki?5060) an image control into a Web Panel form and the Select Image dialog appears. Select the "*Reference External*" Image button and a new dialog (like the one below) will be displayed. You must type in a name for it and provide a Source (i.e. where the image is located). The Source is usually a URL, such as "http://www.gxtechnical.com/main/images/evgx\_xiv.gif".  
  
`[imagen omitida: wiki id 4829]`

### [External and Internal Images](#External+and+Internal+Images)

Internal and external images are functionally the same. They can be used, referenced, etc. in the same way as preferences, Themes, source code, properties, etc. The difference is that, while the actual images of an Internal Image are stored in the Knowledge Base, the only thing that is stored for External Images is a reference to where the actual image should be. Internal Images are managed automatically, which means that you no longer need to worry about where the image should be in order for it to be available to your application either at design or runtime. Changes in the location of External Images must be handled manually.  
  
`[imagen omitida: wiki id 4830]`  
  
On the other hand, Internal Images require more storage space and generate larger Export files than External Images.

### [Managing Images](#Managing+Images)

The Images node which is under the Customization node in the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210) opens the Images tool window, which should look like the following image if the Detail view is the active one. It has several different views: List, Thumbnails, Tile, and Detail, which resemble Windows Explorer.  
  
`[imagen omitida: wiki id 4831]`  
  
On the right, there is a Preview pane that shows the actual image, if available. Note that if an External Image is selected and it cannot be found (i.e. the image is not where it is expected to be, or it is on the Internet and there is no Internet connection) it will not be displayed. GeneXus does not cache external images.  
  
When an image is opened (double-click, context menu Open, etc.), a new window appears (like the one below). At this time, you may need more detailed information on how Images are implemented.

A GeneXus Image is actually a container. It holds actual images used for each Language, Theme, Density, or combinations of all. See [HowTo: Use different images depending on the theme, language and density of the screen](https://wiki.genexus.com/commwiki/wiki?23754)  
The images contained in an Image Object have the following properties:

`[imagen omitida: wiki id 24061]`

|  |  |
| --- | --- |
| **Name** | Name of the image |
| **Description** | Description of the image |
| **Is External** | Indicates if the image is external or not |
| **Theme** | Indicates the theme for which the image is designed. |
| **Language** | Indicates the language for which the image has to be used ([if it is language dependant](https://wiki.genexus.com/commwiki/wiki?23754)). This is helpful when images have text drawn in them |
| **Density** | Indicates for which screen density the image is designed. [See more](https://wiki.genexus.com/commwiki/wiki?24062) |
| **Rendering Mode** | [See more](https://wiki.genexus.com/commwiki/wiki?23135) |
| **Scalable Image** | Indicates if the image is [scalable](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?23862,,). [See more](https://wiki.genexus.com/commwiki/wiki?23865). |

This is great, as changing the current Language and/or the current [Theme](https://wiki.genexus.com/commwiki/wiki?4375) and/or [Screen Density](https://wiki.genexus.com/commwiki/wiki?24062) will change the actual images accordingly without any coding.

This approach is commonly used in [smart devices images](https://wiki.genexus.com/commwiki/wiki?31379) (e.g. icons, launch and application images, platform depending). When a developer wants to add multiple images in the same Image object, there are two different ways to do it:

* Adding one by one clicking "New image" button and setting its properties properly (density and theme at least).
* Compress all the images in a *\*.zip* file and simply import it as an image file.  
  If the developer follows a simple file system guideline, GeneXus automatically imports the images in its respective densities.  
  `[imagen omitida: wiki id 31463]`  
  Some examples can be found on [this](https://design.google.com/icons/) site.

### [Changing images at runtime](#Changing+images+at+runtime)

The actual image shown by a control may be changed at runtime using one of the following methods.

#### [FromImage(<ImageName>)](#FromImage%28%26lt%3BImageName%26gt%3B%29)

Applies to Bitmap data type Variables and to Image controls. <ImageName> is the name of an Image object stored in the Knowledge Base. If &Bitmap is a bitmap data type variable the following code will change the image displayed by it to MyNewImage.

```
&Image.FromImage(MyNewImage)
```

#### [FromImage(<StringExpression>)](#FromImage%28%26lt%3BStringExpression%26gt%3B%29)

Applies to Bitmap data type Variables and to Image controls. <StringExpression> is an expression that **must** evaluate at runtime to the name of an Image object stored in the Knowledge Base. If &Bitmap is a bitmap data type variable and &Image is a character variable whose value is "MyNewImage", the following code will change the image displayed by it to MyNewImage.

```
&Image.FromImage( &Image)
```

#### [FromLink(<StringExpression>)](#FromLink%28%26lt%3BStringExpression%26gt%3B%29)

Applies to Bitmap data type Variables and to Image controls. <StringExpression> is a string expression that must evaluate to a valid image URL. This format is equivalent to the LoadBitmap function.

#### [Link()](#Link%28%29)

Applies to Image objects. It returns a string containing a link to the actual image for the current Language and [Theme](https://wiki.genexus.com/commwiki/wiki?4375) (if aplicable). For example:

```
TableControl.Background = BackgroundImage.Link()
```

### [Importing and Exporting Images](#Importing+and+Exporting+Images)

Images are "standard objects". They can be exported and imported without any special consideration unless importing from previous versions as discussed [here](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?6435,,).

As you can see, having images inside the KB improves GeneXus [usability](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7263,,) and [Knowledge integration](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7265,,).

### [Images used automatically by GeneXus and managed as image object in KB](#Images+used+automatically+by+GeneXus+and+managed+as+image+object+in+KB)

GeneXus applications use a set of image objects that are included in the Knowledge Base creation. All images in the GeneXus generated application can be modified using the associated Image object within the Knowledge Base.

All images references can be found in the file images.txt file located in the model target path.

### [Supported Image formats](#Supported+Image+formats)

You can add images of any kind or format. Be careful to add to your KB only those that are supported by the target platforms (Browsers, Native apps, etc)

Note: When you add an image using the IDE, the selector lets you choose an image file, filtering by the following file extensions:

`[imagen omitida: wiki id 46718]`

Anyway, you can select an image of any file extension by using the common '\*.\*' filter in the 'File name'.

Furthermore, the IDE shows previews and information like the size, of images with a format that is supported by the .NET Framework ([ref](https://docs.microsoft.com/en-us/dotnet/api/system.drawing.bitmap?view=netframework-4.7.1#remarks)), but this does not limit you to these formats. The image format is only limited by the target platform.

For example, if you choose an SVG, the IDE won't preview it, but the browser will support it. (The SVG format is still not supported by the Native Mobile Generator.)

### [See also](#See+also)

* [HowTo: Use different images depending on the theme, language and density of the screen](https://wiki.genexus.com/commwiki/wiki?23754)
* [gx-content-mode property](https://wiki.genexus.com/commwiki/wiki?23857)
