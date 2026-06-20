---
title: "Application Help"
source_id: 12152
source_url: https://wiki.genexus.com/commwiki/wiki?12152
genexus_version: "18"
---

# Application Help

This is a help-generating program provided within applications. It is used to generate help files.

The generated help files contain the help text defined for every attribute, domain or object.

The help is generated in HTML format. Also incorporated is the possibility of packing all the generated help in a single [CHM](http://en.wikipedia.org/wiki/Microsoft_Compiled_HTML_Help) format file, including all the characteristics provided by this feature, such as the possibility of searching in the generated help, defining indexes, etc.

* If a help item has a link to an image when the help file is generated the image is created in the help directory. The page reference is relative to this directory. If the image depends on the language, it is associated with the language in which the help file is being generated.

* If the reference to an object is added in the help editor, a reference to the help page corresponding to this object will be generated (if the object doesn’t have a help item defined).

## [How to use it](#How+to+use+it)

* Define the help for all the objects needed in the KB.
* Use the [Help Generator Options](https://wiki.genexus.com/commwiki/wiki?12154) to actually generate the files, go to Tools and Application Help on the IDE.
* Make sure to add a button connected to the Help event.
* The application at runtime will call the help associated with the object in a new tab when clicking on the Help button.

### [See also](#See+also)

[Type of Help](https://wiki.genexus.com/commwiki/wiki?12153,,)  
[Help Generator Options](https://wiki.genexus.com/commwiki/wiki?12154)


|  |
| --- |
| **Backlinks** |
| [Help Event](https://wiki.genexus.com/commwiki/wiki?12604) | [HelpGenerator MSBuild Task](https://wiki.genexus.com/commwiki/wiki?12560) |

---
