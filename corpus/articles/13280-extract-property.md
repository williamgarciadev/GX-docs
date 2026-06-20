---
title: "Extract property"
source_id: 13280
source_url: https://wiki.genexus.com/commwiki/wiki?13280
genexus_version: "18"
---

# Extract property

It allows you to automatically copy the file to a certain directory during the building process.

It's very useful for files that need to be copied to the application directory, such as some classes or *\*.**dll* files used with external objects.

**Warning**: This property and its subordinates (*Generator* and *Extract to* *path* properties) have been deprecated as of [GeneXus 15 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?38845,,). Refer to [File object](https://wiki.genexus.com/commwiki/wiki?5852) article for details.

### [Values](#Values)

|  |  |
| --- | --- |
| **No** | The file is not going to be copied. This is the default value. |
| **Always** | The file is always copied after the generation process. |
| **Newer** | The file is copied only when it's newer. |

When 'Always' or 'Newer' is selected, the "Generator" and "Extract to path" properties appear.

#### [**Generator property**](#Generator+property)

|  |  |
| --- | --- |
| **Any** | The file will be copied regardless of the generator used. This is the default value. |
| **CSharp** | The file is copied only when generating with CSharp. |
| **Java** | The file is copied only when generating with Java. |
| **Ruby** | The file is copied only when generating with Ruby (not available in [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?28265,,)). |

#### [**Extract to path property**](#Extract+to+path+property)

It's the path where the file is going to be copied, and it may be an absolute or relative path. When left empty, the default behavior is as follows:

|  |  |
| --- | --- |
| **Win User Interface** | [Target Path property](https://wiki.genexus.com/commwiki/wiki?9612,,) directory (for CSharp it's TargetPath\bin). |
| **Web User Inteface** | [Target Path property](https://wiki.genexus.com/commwiki/wiki?9612,,) \web directory. |

### [Notes](#Notes)

* If the “Extract to path” property is empty during the specification process, the extraction will be made in the 'bin' folder of the KB.
* If the extraction is to be made in another folder, or if the absolute address is used or if it is indicated with a “.”, the extraction will be made in the Web folder of the KB.

Both cases are independent of the environment (win/web).

### [Scope](#Scope)

**Objects** [File object](https://wiki.genexus.com/commwiki/wiki?5852)


|  |
| --- |
| **Backlinks** |
| [.NET Framework Generator Extraction Directory property](https://wiki.genexus.com/commwiki/wiki?39502) | [Adding additional files to an application package](https://wiki.genexus.com/commwiki/wiki?35361) | [Toc:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) |
| [Toc:Application Deployment tool (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54334) | [Extract for .NET Framework Generator property](https://wiki.genexus.com/commwiki/wiki?39501) | [Extract for Java Generator property](https://wiki.genexus.com/commwiki/wiki?39499) | [HowTo: Use an external CSS file on a Web Panel](https://wiki.genexus.com/commwiki/wiki?24387) |
| [Java Generator Extraction Directory property](https://wiki.genexus.com/commwiki/wiki?39500) |

---
