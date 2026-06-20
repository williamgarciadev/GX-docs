---
title: "HowTo: Using web fonts in Web Themes"
source_id: 22701
source_url: https://wiki.genexus.com/commwiki/wiki?22701
genexus_version: "18"
---

# HowTo: Using web fonts in Web Themes

This article describes how to use [Google Fonts](http://www.google.com/fonts/) and web fonts in [Web Theme object](https://wiki.genexus.com/commwiki/wiki?6420)s.

**Note**: If you are using Design Systems, refer to [Font-face style rule](https://wiki.genexus.com/commwiki/wiki?49338).

### [Using web fonts](#Using+web+fonts)

The main purpose of this feature is to make it possible to use any font, even those that are not installed on the client machine (where the browser is running).

The use of remote fonts is explained in the CSS3 specification, using the @font-face rule.

### [Using web fonts in Web Themes](#Using+web+fonts+in+Web+Themes)

1. Edit the [Web Theme object](https://wiki.genexus.com/commwiki/wiki?6420) where the font will be referenced.  
Click on the "Fonts" node and select "Add Font". A dialog will appear with the following options:

* Select a file object in the KB where the font file will be referenced, or
* Click "Import from file" and look for the font file on the PC. In this case, a file object will be automatically created with the name of the font file. See figure 1.

##### Figure 1.

As a result of the above step, a node will be created under the Fonts node, referencing the font in its "File property". To be used in GeneXus, the font is identified by the File name. It may be changed as needed. See figure 2.

##### Figure 2.

When the CSS of the Theme is generated, it includes a @font-face rule like the one in the following example:

```
@font-face{
       font-family:'OpenSans-Regular';
       src:url(OpenSans-Regular.ttf)
}
```

Note that, in this case, the OpenSans-Regular.ttf file has to be copied to the same folder where the CSS is located.

2. Next, you need to reference this font class in the controls. The recommended way to do it is by referencing the font in the classes of the Theme that will be associated with attributes or Text Blocks that will use this font.

So, edit the class of the Theme that will use the font, select the "Font Family" property and enter the custom class (Custom Theme Fonts) created in the first step.

##### Figure 3.

Note that you can select an order for the alternative fonts of this class.

After going through the steps described above, the "TextBlock1" class will have the font "OpenSans-Regular" in the font family group. As a result, any Text Block associated with this class will use this font as a first alternative.

```
.TextBlock1 {
      font-family: OpenSans-Regular,"Trebuchet MS",Arial,Helvetica,sans-serif;
}
```

Note: by default, not all font types are supported by IIS. If you get a 404 error trying to get to the font file, run the following command:

```
C:\Windows\System32\inetsrv\appcmd set config /section:staticContent /+[fileExtension='.woff',mimeType='text/css']
```

(replace .woff with the extension you are adding) and restart your IIS

### [Using Google Fonts](#Using+Google+Fonts)

If you need to use a Google Font such as "Joti One", just like in the above example, you will have to reference this font in the Font Family property of the Theme Class.

For example, for "TextBlock1" class, open the Font Family dialog and include the reference to the font as shown in figure 4:

##### Figure 4.

In this case, the Custom Theme Font referenced there is the name of the Google font, and you don't need to add a Font tag as in the example above because the font is included in a Google CSS.

To reference this CSS, you can use the [HeaderRawHTML Property](https://wiki.genexus.com/commwiki/wiki?14620) as in the example below:

```
Event Start
     form.HeaderRawHTML = "<link href='http://fonts.googleapis.com/css?family=Joti+One' rel='stylesheet' type='text/css'>"
Endevent
```

For example, see [here](https://fonts.google.com/?query=source&selection.family=Source+Sans+Pro).

`[imagen omitida: wiki id 31922]`

This reference will be included in the page header.

The "TextBlock1" class will include the "Joti One" font in the group of fonts of its Font Family property:

```
.TextBlock1 {
      font-family: "Joti One",OpenSans-Regular,"Trebuchet MS",Arial,Helvetica,sans-serif;
}
```

### [Note](#Note)

Do not assign the web font directly in the control property; do it only in the CSS class.

### [See Web Fonts in Action](#See+Web+Fonts+in+Action)

* [Product Catalog Sample](https://wiki.genexus.com/commwiki/wiki?21791,,)

### [Note](#Note)

Consider the browser support for the fonts used (find more information [here](https://developers.google.com/fonts/faq?hl=es-UY#Browsers_Supported)).

### [See Also](#See+Also)

[Using Custom Fonts](https://wiki.genexus.com/commwiki/wiki?22781)  
[How to define fonts in a Design System object](https://wiki.genexus.com/commwiki/wiki?49338)


|  |
| --- |
| **Backlinks** |
|
| [Using Custom Fonts](https://wiki.genexus.com/commwiki/wiki?22781) |

---
