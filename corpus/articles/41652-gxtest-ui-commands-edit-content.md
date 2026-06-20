---
title: "GXtest UI commands - Edit Content"
source_id: 41652
source_url: https://wiki.genexus.com/commwiki/wiki?41652
genexus_version: "18"
---

# GXtest UI commands - Edit Content

This commands only apply when you want to set the content of HTML5 controls that are using a [ContentEditable attribute](https://www.w3schools.com/tags/att_global_contenteditable.asp). This particular case happens for example when using controls with type = FCK HTML Editor, the resulting HTML will use [contenteditable = true](https://www.w3schools.com/tags/att_global_contenteditable.asp). Actually, this article is being written on top of an FCK HTML Editor in GeneXus wiki.

For this kind of controls, instead of using traditional [type commands](https://wiki.genexus.com/commwiki/wiki?41649), you will need to use the following ones.

## [EditContentByID](#EditContentByID)

Sets the content of the specified element using its ID.

Parameters:

* ID: the control's ID of the content.
* Text: A string containing the HTML context to set.

Example of use:

```
&driver.EditContentById("content1", "<h2> this is the new sub-title </h2>")
```

## [EditContentByLinkText](#EditContentByLinkText)

Sets the content of an element, locating it by the text name:

Parameters:

* LinkText: the link text to set the content.
* Text: A string containing the HTML context to set.

Example of use:

```
&driver.EditContentByLinkText("edit this link here", "link edited")
```

## [EditContentByName](#EditContentByName)

Sets the content of the specified element using its 'name' attribute.

Parameters:

* Name: the NAME attribute of the control to set the content.
* Text: A string containing the HTML context to set.

Example of use:

```
&driver.EditContentByName("content1", "text and text over here (html accepted)")
```

## [EditContentByCSS](#EditContentByCSS)

Sets the content of the specified element using a CSS selector.

Parameters:

* CSS: the CSS selector of the element that you want to set the content.
* Text: A string containing the HTML context to set.

Example of use:

```
&driver.EditContentByCSS("body.cke_editable.cke_editable_themed.cke_contents_ltr.cke_show_borders","<pre>//Coding style here</pre>")
```

## [EditContentByXPath](#EditContentByXPath)

Sets the content of the specified element using an XPath selector.

Parameters:

* XPath: the XPath selector of the element to be edited.
* Text: A string containing the HTML context to set.

```
Example of use: 

&driver.EditContentByXPath("//body", ,"<pre>//Coding style here</pre>")
```


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) | [GXtest UI Test for Web - Supported Commands](https://wiki.genexus.com/commwiki/wiki?40281) |

---
