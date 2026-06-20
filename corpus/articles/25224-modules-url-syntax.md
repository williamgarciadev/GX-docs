---
title: "Modules - URL Syntax"
source_id: 25224
source_url: https://wiki.genexus.com/commwiki/wiki?25224
genexus_version: "18"
---

# Modules - URL Syntax

The purpose of this document is to explain how different URLs are modified, by default, when you move objects to a [Module object](https://wiki.genexus.com/commwiki/wiki?22411) other than the [Root module](https://wiki.genexus.com/commwiki/wiki?22439).

Consider "ObjectC" in module "ModuleC", in the following image:

`[imagen omitida: wiki id 22436]`

### [Web Objects URL](#Web+Objects+URL)

The URL will be as follows:

#### [Java](#Java)

.../packagename.modulea.modulec.objectc

When using modules and generating for Java the [Java package name property](https://wiki.genexus.com/commwiki/wiki?24941) must be set; in this example, it is supposed that its value is: "packagename".

#### [Net and .NET Core](#Net+and+.NET+Core)

.../modulea.modulec.objectc.aspx

### [SOAP services URL](#SOAP+services+URL)

SOAP services are published using the following syntax:

.../modulea.modulec.objectc?wsdl

### [Rest services URL](#Rest+services+URL)

Rest services are published using the following syntax:

.../rest/modulea/modulec/objectc

**Info**: The URL of a web object and its parameters can be customized using [URL Rewrite object](https://wiki.genexus.com/commwiki/wiki?46523), and the one of ReST Services can be customized using [API object](https://wiki.genexus.com/commwiki/wiki?46151).

### [See Also](#See+Also)

[Qualified Name property](https://wiki.genexus.com/commwiki/wiki?22477)

[Modules - Object names](https://wiki.genexus.com/commwiki/wiki?22483)


|  |
| --- |
| **Backlinks** |
| [Toc:Modules](https://wiki.genexus.com/commwiki/wiki?22414) | [Working with Modules](https://wiki.genexus.com/commwiki/wiki?25607) |

---
