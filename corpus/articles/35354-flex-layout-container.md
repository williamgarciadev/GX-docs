---
title: "Flex Layout Container"
source_id: 35354
source_url: https://wiki.genexus.com/commwiki/wiki?35354
genexus_version: "18"
---

# Flex Layout Container

Flex Layout container aims to offer more ways to lay out controls in a container even if the control size is unknown. Because of this, it offers more efficient ways to achieve responsive user interfaces than existing table containers.

## [Why being flex is important: The canonical sample](#Why+being+flex+is+important%3A+The+canonical+sample)

There are many simple cases where you don't know the control size because the size depends on the content of the control. The canonical sample is when you have for example several Textblocks to show in a row. The Width of the Textblocks depends on the captions of the controls, so depending on those captions all the text blocks can fit the screen width or not.  
  
This case is impossible to model using tables because you don't know if you will show 2,3,4 or more text blocks in a row, so you can not specify the number of columns of the table. This is the perfect sample to use a Flex Layout, then the text blocks will be shown in one, two, or more rows depending on the size of each text block.

For example when you have some data like an address but using several attributes and you want to render something like:

**Garcia Morales 1235 Zip 11300**

You can drag and drop the attributes CustomerAddress, CustomerNumber, CustomerZipNumber, without giving width to each attribute because actually, you don't know the length of each data.

Note that using the [Abstract Layout](https://wiki.genexus.com/commwiki/wiki?25209) each control in the table has a predefined width (given in percentage values), although it could be changed using your own Theme Classes. Through the Flex Table, it's the control size inside the cell which governs the column width.   
Additionally, using a Flex Table you are not forced to a maximum of n (e.g. 12) columns in a row.

Check the browsers [support for this feature](https://caniuse.com/#feat=flexbox).

## [How to use it?](#How+to+use+it%3F)

[Flex control](https://wiki.genexus.com/commwiki/wiki?40521) is available to be dragged and dropped from the [Toolbox](https://wiki.genexus.com/commwiki/wiki?10000) in the same way as Canvas and Tables containers.

`[imagen omitida: wiki id 36182]`

Also, Flex Grid is a value offered by the Grids [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) and the Free Style Grids  [Custom Render property](https://wiki.genexus.com/commwiki/wiki?11407) (for Web applications).

## [Notes](#Notes)

* It does not exist the "safe area" concept when designing apps using Flex containers. For such reason, it is recommendable to use [Expand Bounds property](https://wiki.genexus.com/commwiki/wiki?37136) with 'None' value.

## [Availability](#Availability)

Available since [GeneXus 15 upgrade 12](https://wiki.genexus.com/commwiki/wiki?39737,,).

## [Flex Layout Properties](#Flex+Layout+Properties)

The Flex Table container became a standard for web interfaces, and also for mobile layouts. In GeneXus, you have it on both platforms: Web and Mobile.


* Flex Table and Flex Grid properties
  + [Flex Direction property](https://wiki.genexus.com/commwiki/wiki?36107)
  + [Justify Content property](https://wiki.genexus.com/commwiki/wiki?36108)
  + [Flex Wrap property](https://wiki.genexus.com/commwiki/wiki?36109)
  + [Align Items property](https://wiki.genexus.com/commwiki/wiki?36111)
  + [Align Content property](https://wiki.genexus.com/commwiki/wiki?36110)
* Flex Layout embedded controls properties
  + [Flex Grow property](https://wiki.genexus.com/commwiki/wiki?39715)
  + [Flex Shrink property](https://wiki.genexus.com/commwiki/wiki?39716)
  + [Align Self property](https://wiki.genexus.com/commwiki/wiki?39717)
  + [Width property](https://wiki.genexus.com/commwiki/wiki?39731)
  + [Height property](https://wiki.genexus.com/commwiki/wiki?39732)
  + [Min Width property](https://wiki.genexus.com/commwiki/wiki?39729) & [Min Height property](https://wiki.genexus.com/commwiki/wiki?39720)
  + [Max Width property](https://wiki.genexus.com/commwiki/wiki?39718) & [Max Height property](https://wiki.genexus.com/commwiki/wiki?39719)
* Sample
  + [PhotosGallery](https://wiki.genexus.com/commwiki/wiki?40306,,)
* Media
  + [Flex Layout in the Media](https://wiki.genexus.com/commwiki/wiki?40431,,)

---
