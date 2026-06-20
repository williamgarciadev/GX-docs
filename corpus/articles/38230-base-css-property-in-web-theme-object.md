---
title: "Base CSS property in Web Theme Object"
source_id: 38230
source_url: https://wiki.genexus.com/commwiki/wiki?38230
genexus_version: "18"
---

# Base CSS property in Web Theme Object

Sets the Base Style for a Web Theme. All libraries (ZIP files) with UI design definitions previously added to the KB as File objects are offered to select one of them. The selected library will be included when generating panels based on the Theme.

### [Values](#Values)

|  |  |
| --- | --- |
| **Bootstrap v3** | Selects the Bootstrap v3 library, which is a popular HTML, CSS, and JS library. |
| **Bootstrap v3 RTL** | Selects the Bootstrap v3 Right-to-Left library. |
| **None** | The Web Theme object doesn't have an assigned library. |

### [Scope](#Scope)

**Objects:** [Web Theme](https://wiki.genexus.com/commwiki/wiki?6420)  
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

Next, you can include that Base Library in your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) by creating a new [File object](https://wiki.genexus.com/commwiki/wiki?5852) and specifying the path to upload your Base Library (make sure that when adding the file, the name ends with \_gxlibrary; otherwise, the IDE will not consider it as a library).

Finally, the Library will be offered for this property so that you can select it.

While several libraries can be included in the KB, using the same Base CSS for different objects is recommended in order to maintain consistency.

### [Notes:](#Notes%3A)

**1)** To just add external references to resources, you need to create a references file inside the library; each line of this file will be considered a reference.

For example, you can add a glue.references with the following content:

ace.js  
ace.css

This means GeneXus will add references to those files when some Theme or User Control uses your Base Library.

**2)** If you create a [Web Theme object](https://wiki.genexus.com/commwiki/wiki?6420) and set its **Base CSS property** = None, the Action Groups and Tab controls will have a basic appearance. To give them a style, set the ActionGroup and ActionGroupItem Theme classes for the Action Group control, and the Tab and TabPage classes for the Tab control.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [See Also](#See+Also)

[Base CSS property in User Control object](https://wiki.genexus.com/commwiki/wiki?40587)  
[Base CSS property in Design System Object](https://wiki.genexus.com/commwiki/wiki?49256)  
[RTL](https://wiki.genexus.com/commwiki/wiki?42318)


|  |
| --- |
| **Backlinks** |
| [Base CSS property in Design System Object](https://wiki.genexus.com/commwiki/wiki?49256) | [Base CSS property in User Control object](https://wiki.genexus.com/commwiki/wiki?40587) | [Toc:Design Systems](https://wiki.genexus.com/commwiki/wiki?40108) |
| [HowTo: Add RTL styles](https://wiki.genexus.com/commwiki/wiki?42319) | [HowTo: Add RTL styles (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54443) |

---
