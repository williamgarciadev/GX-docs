---
title: "User control structure overview"
source_id: 26973
source_url: https://wiki.genexus.com/commwiki/wiki?26973
genexus_version: "18"
---

# User control structure overview

**Warning**: Since GeneXus 16, it is strongly recommended to create a [User Control object](https://wiki.genexus.com/commwiki/wiki?39356) instead of creating a [Web User Control](https://wiki.genexus.com/commwiki/wiki?27212).

Every GeneXus User Control must be placed under the UserControls folder inside the GeneXus installation directory. In addition, every UC is composed by at least 4 files:

* Control Definition file (\*.control): defines general aspects of the control such as name, icon, resources.
* Properties file (xml): defines the control's properties.
* Runtime render file (js): specifies how the control must be displayed at runtime.
* Design render file (xsl): specifies how the control must be displayed at design time (in the GeneXus IDE).

Consequently, the [User Control Editor](https://wiki.genexus.com/commwiki/wiki?26976) is divided into different tabs where each tab helps you create one of the files specified above, that is to say:

* the Control Definition tab belongs to the \*.control file. See [User Control definition file](https://wiki.genexus.com/commwiki/wiki?13309,,).
* the Events tab also belongs to a specific "section" of the \*.control file. See [User control events](https://wiki.genexus.com/commwiki/wiki?27205).
* the "Properties" tab belongs to the properties file (xml). See [User control properties](https://wiki.genexus.com/commwiki/wiki?27179,,).
* the "JScript Runtime Render" tab belongs to the runtime render file (js). See [JScript Runtime Render](https://wiki.genexus.com/commwiki/wiki?27194,,).
* the "Xsl Designer Render" tab belongs to the design render file (xsl). See [XSL Designer Render](https://wiki.genexus.com/commwiki/wiki?27181,,).

### [Example](#Example)

In order to give a specific sample, the [Hello World User Control](https://wiki.genexus.com/commwiki/wiki?4880) is composed by:

* HelloWorld.control
* HelloWorldProperties.xml
* HelloWorldRender.js
* HelloWorldRender.xsl

In the User control Editor, the relationship between "tabs and files" would be as follows:

`[imagen omitida: wiki id 4941]`


|  |
| --- |
| **Backlinks** |
| [User Control Editor](https://wiki.genexus.com/commwiki/wiki?26976) | [Toc:Web User Controls](https://wiki.genexus.com/commwiki/wiki?27212) |

---
