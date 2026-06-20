---
title: "Generate Maven pom file property"
source_id: 42987
source_url: https://wiki.genexus.com/commwiki/wiki?42987
genexus_version: "18"
---

# Generate Maven pom file property

**Deprecated**: Since GeneXus 18 upgrade 4.

Generates Maven compilation pom.xml file.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Level:** Deploy Target Options

### [Description](#Description)

For Java models, within the [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092), the Generate Maven pom file property is available when "Target = Local (sources)" is selected.

To generate the [Maven](https://maven.apache.org/) pom.xml, GeneXus uses a template named Maven.pom.stg that is copied to the Knowledge Base directory. You can change that file by adding the plugins you need, as well as profiles, reference parent files, etc.

That template is a template group of [StringTemplate](https://www.stringtemplate.org/) which has the skeleton of an XML and references subtemplates that can be changed as needed.

`[imagen omitida: wiki id 45576]`

### [Availability](#Availability)

This property is available since [GeneXus 16 upgrade 4](https://wiki.genexus.com/commwiki/wiki?42755,,).

### [See Also](#See+Also)

[How to deploy sources to Git or for compilation with Maven](https://wiki.genexus.com/commwiki/wiki?42656,,)


|  |
| --- |
| **Backlinks** |
| [Maven path for local libs property](https://wiki.genexus.com/commwiki/wiki?42988) |

---
