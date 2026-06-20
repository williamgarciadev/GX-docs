---
title: "Language dialogs"
source_id: 13247
source_url: https://wiki.genexus.com/commwiki/wiki?13247
genexus_version: "18"
---

# Language dialogs

To prepare translation of titles and labels, double click on language selected in Folder View. This will make available the dialog necessary to perform the translation task.

### [Translations selector](#Translations+selector)

This selector is where translations are done. For the example in the image below, Spanish was the language selected.

`[imagen omitida: wiki id 13248]`

There are two columns: "Code" and "Localized text". By default, the first column includes everything translatable existing in the KB. The other column includes text already translated, and text still to be translated.

Besides the messages listed by GeneXus, it is also possible to enter text directly. For instance, focus on any line and press <Enter>. The first line will be made available to enter the message.

#### [Filters](#Filters)

There are filters to enable a quicker location of the desired messages.

* **Messages that match pattern.** Allows entering a message search pattern to be shown on the list.
* **Messages used in object.** Allows searching for the object whose messages are to be shown.
* **Show only messages without translation.** Allows obtaining the list of messages still to be translated ("Localized text" column empty).
* **Show only user messages.** Allows obtaining list of messages that are only user messages, that is: messages of the KB's internal system are excluded.

Note: from GeneXus 16 Upgrade 5 "User messages" are included in the language object when objects are specified and the environment have translation (ie. [Translation type property](https://wiki.genexus.com/commwiki/wiki?9126) is set to "static" or "run-time").

#### [Reference Language Combo Box](#Reference+Language+Combo+Box)

Allows indication of the language to be taken as reference in case of need to translate into another language. For example, for translating into Portuguese, it could prove more useful to use Spanish as the reference language rather than English. So, to start from Spanish when in the Portuguese Language Object, select Spanish from the list of languages of the combo box and GeneXus will immediately add a new column (read-only) that the user will be able to use as a guide in the translation process.

`[imagen omitida: wiki id 13250]`

### [Images selector](#Images+selector)

This selector shows which images depend on the language (the setting of images with languages and themes is done in the image object itself). In the image, it is clear that thre is an image for English and another image for SimplifiedChinese.

`[imagen omitida: wiki id 13252]`

### [Documentation selector](#Documentation+selector)

See [Documenting](https://wiki.genexus.com/commwiki/wiki?10344).

### [See also](#See+also)

[Folder View](https://wiki.genexus.com/commwiki/wiki?3210)  
[Managing Images](https://wiki.genexus.com/commwiki/wiki?23387)  
[Document Object](https://wiki.genexus.com/commwiki/wiki?10344)
