---
title: "Base CSS property in User Control object"
source_id: 40587
source_url: https://wiki.genexus.com/commwiki/wiki?40587
genexus_version: "18"
---

# Base CSS property in User Control object

Sets the Base Style for a User Control object. All libraries (ZIP files) with UI design definitions previously added to the KB as File objects are offered to select one of them.

### [Values](#Values)

|  |  |
| --- | --- |
| **Default** | The User Control object doesn't have an assigned Base Style. |

### [Scope](#Scope)

**Objects:** User Control  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

The material available online about Web Design to integrate into the applications developed with GeneXus is astonishing! There is a boom of the so-called "CSS Frameworks," which complement JavaScript development Frameworks (for example, JQuery). Applications can be made more attractive thanks to CSS Frameworks.

These CSS Frameworks provide hundreds of widgets, compositions, sources, etc.  
Some of the most popular ones are as follows:

* Bulma.io
* Bootstrap
* SemanticUI
* Pure.css
* Kube
* Materialize

### [What is a Base Library](#What+is+a+Base+Library)

A Base Library is an external resource that uses a CSS Framework. For example, Semantic UI, Bootstrap, etc.

Base Libraries are external CSS & JS & Assets files that are globally installed with GeneXus.

### [How to create a new Base Library inside a KB](#How+to+create+a+new+Base+Library+inside+a+KB)

First, to create a Base Library, compress all the required files (CSS, JS, etc.) into a ZIP file and save it with .gxlibrary extension.

Next, you can include that Base Library in your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) by creating a new [File object](https://wiki.genexus.com/commwiki/wiki?5852) and specifying the path to upload your Base Library.

Finally, the Library will be offered for this property so that you can select it.

While several libraries can be included in the KB, using the same Base CSS for different objects is recommended to maintain consistency.

### [Notes:](#Notes%3A)

**1)** To just add external references to resources, create a references file inside the library; each line of this file will be considered a reference.

For example, you could add a glue.references with the following content:

ace.js  
ace.css

This means GeneXus will add references to those files when some Theme or User Control uses your Base Library.

**2)** If you create a [User Control object](https://wiki.genexus.com/commwiki/wiki?39356) and set its **Base CSS property** = None, it won't look appealing.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [See Also](#See+Also)

[Base CSS property in Design System Object](https://wiki.genexus.com/commwiki/wiki?49256)  
[Base CSS property in Web Theme Object](https://wiki.genexus.com/commwiki/wiki?38230)


|  |
| --- |
| **Backlinks** |
| [Base CSS property in Design System Object](https://wiki.genexus.com/commwiki/wiki?49256) | [Base CSS property in Web Theme Object](https://wiki.genexus.com/commwiki/wiki?38230) | [Creating SAPUI5 controls in GeneXus](https://wiki.genexus.com/commwiki/wiki?45691) |
| [GeneXus and SAP UI5 web component](https://wiki.genexus.com/commwiki/wiki?45707) | [Category:User Control object](https://wiki.genexus.com/commwiki/wiki?39356) |

---
