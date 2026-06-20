---
title: "Translation types (GeneXus 18 Upgrade 2 or prior)"
source_id: 54444
source_url: https://wiki.genexus.com/commwiki/wiki?54444
genexus_version: "18"
---

# Translation types (GeneXus 18 Upgrade 2 or prior)

There are two types of translation available in GeneXus: static translation and runtime translation.

### [Static Translation](#Static+Translation)

Static translation is achieved at specification time. The resulting application cannot change the language at runtime. Static translation is the best performing translation option, as no runtime code is added. To activate Static translation set the [Translation type property](https://wiki.genexus.com/commwiki/wiki?9126) (at [Environment](https://wiki.genexus.com/commwiki/wiki?7115) level) to Static, and select the language you want to translate into in the [Translate to language property](https://wiki.genexus.com/commwiki/wiki?13242).

#### [When to use static translation](#When+to+use+static+translation)

Static translation is available for all generators (many generators only have this value for the Translate environment property). Static translation provides the best performing code as no runtime overhead is added: translation is performed at specification time. Having your application in different languages requires different executables (one for each language). If you plan to have your application translated into different languages using Static translation, you should set up a new Environment for every new language you want to translate into.

Notice that if your languages references different ISO code pages, you will need to change the windows regional settings configuration for each language generation process.

For instance, if you have languages such as Japanese, Chinese, Thai and so on; the static translation process needs to correctly configure the associated [Language for non-Unicode programs](https://wiki.genexus.com/commwiki/wiki?42339) (Windows configuration). If this is problem for your environment switch to Run-time translation.

### [Run-time Translation](#Run-time+Translation)

Run-time translation is available for [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258) and [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892) generators. Run-time translation is the most versatile solution with a little performance overhead (compared to Static translation). When using Run-time translation you can:

* Manage a single set of executables running in different languages;
* Allow the end-user to select the desired application language among the list of available languages;
* Add new languages to your application without changing the executable code.

Remember to set the [SetLanguage](https://wiki.genexus.com/commwiki/wiki?18757) and [SetTheme](https://wiki.genexus.com/commwiki/wiki?21777) functions to change the language and orientation.

### [See Also](#See+Also)

[Real-time translation of RTL languages](https://wiki.genexus.com/commwiki/wiki?54495)
