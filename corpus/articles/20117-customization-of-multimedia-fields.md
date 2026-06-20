---
title: "Customization of Multimedia Fields"
source_id: 20117
source_url: https://wiki.genexus.com/commwiki/wiki?20117
genexus_version: "18"
---

# Customization of Multimedia Fields

GeneXus makes it possible to store multimedia contents, such as: images, audio or video files. It’s as easy as configuring a variable or attribute based on any of these data types: [Image data type](https://wiki.genexus.com/commwiki/wiki?15204), [Audio data type](https://wiki.genexus.com/commwiki/wiki?16529) and [Video data type](https://wiki.genexus.com/commwiki/wiki?16608).

These variables or attributes are known as multimedia fields.

In web applications, these fields provide two options labeled “Change” and “Clear”; both options are displayed in the UI, by moving the mouse over them:

`[imagen omitida: wiki id 20061]`

The “Change” action has an associated pencil icon and can be used to edit the field contents. Upon selecting this option, a dialog box is displayed to indicate a file or URL.

The “Clear” action is displayed to the right of the “Change” action with a garbage bin icon, and allows you to clear the value associated with the field. Upon selecting this option, the field is cleared and shows the placeholder image (PlaceHolderImage, PlaceHolderAudio or PlaceHolderVideo, as applicable).

### [Example](#Example)

`[imagen omitida: wiki id 20062]`

The appearance of multimedia files can be fully customized, taking into account that:

* The icons associated with both actions are images saved in the KB, and they can be customized by replacing the file associated with their corresponding image object (MultimediaEdit/MultimediaClear) with another icon with these dimensions: 10 x10.
* If you want to replace the standard image of these icons, you can select other images depending on the topic and language.
* Both actions can be used as images, deleting the text of the Change label, but they can't both be used as text because it's not possible to configure text for the "Clear" action.
* The images displayed when a field doesn’t have an assigned value are as follows: PlaceHolderImage, PlaceHolderAudio and PlaceHolderVideo, and their dimensions are 64x64.
* For Video and Audio, when the field has an assigned value, the VideoDownload and AudioDownload images are used, respectively (also of 64x64). For Image, the image itself is associated.
