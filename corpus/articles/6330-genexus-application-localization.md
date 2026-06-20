---
title: "GeneXus Application Localization"
source_id: 6330
source_url: https://wiki.genexus.com/commwiki/wiki?6330
genexus_version: "18"
---

# GeneXus Application Localization

GeneXus allows generating the same application in multiple languages.

### [What is translated?](#What+is+translated%3F)

All fixed texts and messages (those predefined by GeneXus and those defined by you in single or double quotes) that appear in your [GeneXus](https://wiki.genexus.com/commwiki/wiki?1756) code (Sources, Controls, Rules, Events, etc.).

#### [**Exceptions**](#Exceptions)

* Texts prefixed with an exclamation mark (!) as in: !"Customer name" or !'Customer name'. This indicates not to translate a text.
* Texts in formula definitions.
* Texts that follow the commands Do, Sub, Event (i.e. Subroutine and Event names).
* Texts in HTML forms (those that are **not** the [Text Block control](https://wiki.genexus.com/commwiki/wiki?5948)).
* The first parameter of the [SetLanguage function](https://wiki.genexus.com/commwiki/wiki?18757) and [GetMessageText function](https://wiki.genexus.com/commwiki/wiki?21782).
* Help.

### [How is automatic translation enabled?](#How+is+automatic+translation+enabled%3F)

When creating a [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836), a language is selected (English, by default) for GeneXus to generate button labels, messages, etc. This language is set in the [Kb Language property](https://wiki.genexus.com/commwiki/wiki?7671).

After that, you can create different [Environments](https://wiki.genexus.com/commwiki/wiki?7115) in your KB, and for each of them you can decide whether to enable automatic translation or not. To do so, set the [Translation type property](https://wiki.genexus.com/commwiki/wiki?9126) (at Environment level) to a value other than "No translation".

Read about the possible [Translation types](https://wiki.genexus.com/commwiki/wiki?54437) offered by GeneXus to decide which of them to select in the [Translation type property](https://wiki.genexus.com/commwiki/wiki?9126).

### [See also](#See+also)

[Kb Language property](https://wiki.genexus.com/commwiki/wiki?7671)  
[Translation type property](https://wiki.genexus.com/commwiki/wiki?9126)  
[Translate to language property](https://wiki.genexus.com/commwiki/wiki?13242)  
[Autoresize form controls property](https://wiki.genexus.com/commwiki/wiki?9057)  
[Language object](https://wiki.genexus.com/commwiki/wiki?7258)


* [Translation types](https://wiki.genexus.com/commwiki/wiki?54437)
* [Language object](https://wiki.genexus.com/commwiki/wiki?7258)
* [Programming considerations](https://wiki.genexus.com/commwiki/wiki?54440)
  + Useful functions
    - [GetLanguage function](https://wiki.genexus.com/commwiki/wiki?18751)
    - [SetLanguage function](https://wiki.genexus.com/commwiki/wiki?18757)
    - [GetMessageText function](https://wiki.genexus.com/commwiki/wiki?21782)
    - [Format function](https://wiki.genexus.com/commwiki/wiki?8406)

---
