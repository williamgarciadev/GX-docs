---
title: "Considerations when changing the HTML Document type property"
source_id: 17945
source_url: https://wiki.genexus.com/commwiki/wiki?17945
genexus_version: "18"
---

# Considerations when changing the HTML Document type property

This article details the considerations to take into account when changing the [HTML Document type](https://wiki.genexus.com/commwiki/wiki?13517) property.

Up to [GeneXus X Evolution 1](https://wiki.genexus.com/commwiki/wiki?9256,,) the default value is "*Do not specify*".

Pages generated with the "*Do not specify*" value don’t have a doctype specified on the page header. Therefore ’*no doctype*’ means the browser will act in [quirks mode](http://www.quirksmode.org/css/quirksmode.html).

Contrarily, when changing the [HTML Document Type](https://wiki.genexus.com/commwiki/wiki?13517) property value to other value (take into account the [Xev2](https://wiki.genexus.com/commwiki/wiki?15152,,) default value in new KBs is *HTML5*); a doctype header is added; therefore the browser will act in *strict mode* (according to pure standards - *Standards Compliance Mode*).

Specifically, this means you're using the [W3C Box model](http://www.quirksmode.org/css/box.html) now which computes width/height for block elements differently than [quirks mode](http://www.quirksmode.org/css/quirksmode.html).

The issue can cause visualization differences when comparing a GeneXus generated application with HTML5 or other standard value vs the *do not specify* value.

### [Box models](#Box+models)

In the [W3C box model](http://www.quirksmode.org/css/box.html), the width of an element gives the width of the content of the box, excluding padding and border.

In the *traditional box model*, the width of an element gives the width between the borders of the box, including padding and border.

`[imagen omitida: wiki id 17946]`

### [Known Issues](#Known+Issues)

The following section details known issues when modifying the [HTML Document type](https://wiki.genexus.com/commwiki/wiki?13517) property to a value other than "*do not specify*".

#### [Image within a Div tag](#Image+within+a+Div+tag)

In some cases, when rendering an image a visual difference could be detected. For example check this image:

`[imagen omitida: wiki id 17954]`

The same application generated using *HTML5* or other standard, will render using *Strict Mode* and the following difference will appear:

`[imagen omitida: wiki id 17955]`

To solve the issue, edit the Image class associated to the Theme Object and set the *vertical-align* property to *middle*.

#### [Width and Height Control properties](#Width+and+Height+Control+properties)

When using fixed Height and Width values for a control in a Webpanel, take into account that the box-model changed; change the margin, padding, width or height accordingly.

For Example, supose the following WebPanel generated in Xev1 using *Height:21px* (fixed value)

`[imagen omitida: wiki id 17956]`

When using the *Strict Mode*, and as the *padding* and *border* are no longer contained within the *height* property, the control will be rendered "*higher*":

`[imagen omitida: wiki id 17957]`

Notice the difference in size because of the Box model change (4 pixels added to the control height):

`[imagen omitida: wiki id 17958]`

To solve this particular issue, you can change the control height property from *21px* to *17px*.

`[imagen omitida: wiki id 17959]`

See Also

<http://en.wikipedia.org/wiki/Internet_Explorer_box_model_bug>
