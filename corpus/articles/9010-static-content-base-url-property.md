---
title: "Static content base URL property"
source_id: 9010
source_url: https://wiki.genexus.com/commwiki/wiki?9010
genexus_version: "18"
---

# Static content base URL property

Indicates a path to the folder where the application's static content  (javascript, images, cascade stylesheets and other) is located. It can be a relative path (eg.: /static) or a URL (eg.: https://example.com/static).

### [Scope](#Scope)

**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258), .NET, [.NET Core](https://wiki.genexus.com/commwiki/wiki?38604)

### [Description](#Description)

#### [Notes:](#Notes%3A)

* If the value is not indicated in this property, the web server root is assumed (directory “/”).
* If the image path does not begin with a slash  (“/”), the servlet concatenates the following to build the reference in the html generated: the url to the web server root  + what was specified in this property + what was specified in the properties of the image inserted in the web object; whether they are fixed (i.e.: they have been included with insert/picture) or variable (i.e.: they are loaded with the loadbitmap function). Thus, the path must not be repeated in design and in the property so that the latter is correctly loaded.
* If the image path begins with a slash (“/”) it is assumed that it is indicating an absolute path and the property does not apply.
* If you want the reference to be absolute instead of relative, for example, you can indicate http://server/static.

#### [Values](#Values+)

The default value in Java is '/static', and in .NET the default is empty

If a directory called “static” is created under the web application's folder, and all the required images and other static content are copied to this directory, and only the image name is specified in design-time of the web objects, then we should include ‘/static’ in this property.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build with this Only](https://wiki.genexus.com/commwiki/wiki?5693) of the object.


|  |
| --- |
| **Backlinks** |
| [GetInternalURI method](https://wiki.genexus.com/commwiki/wiki?52480) |
| [Toc:Progressive Web Applications in GeneXus](https://wiki.genexus.com/commwiki/wiki?42600) |

---
