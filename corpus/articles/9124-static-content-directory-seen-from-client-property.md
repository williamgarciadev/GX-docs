---
title: "Static content directory seen from client property"
source_id: 9124
source_url: https://wiki.genexus.com/commwiki/wiki?9124
genexus_version: "18"
---

# Static content directory seen from client property

Sets the directory to which the JavaScript files (\*.js files) generated for the web objects’ menu bars and the Web Panels generated as static panels will be transferred. At compilation time, the generator will copy them to the specified directory. This property is read-only and is generated based on the Tomcat path property.

### [Scope](#Scope)

**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

This property is read-only and it is generated based on the [Tomcat path property](https://wiki.genexus.com/commwiki/wiki?48354).  
It allows specifying the directory to which to transfer the JavaScript files (\*.js files) generated for the web objects’ menu bars and the [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)s generated as static panels. At compilation time, the generator will copy them to the specified directory.

#### [Notes:](#Notes%3A)

* This directory will also contain files with the images used in the Web Objects. These files must be **manually copied** to this directory and a reference to them will be made in the generated programs using the value of the “Static Content Base URL” property, concatenated with the name of each image.
* The path specified must be related to the client; that is, it must be seen from the PC where they are working with GeneXus.

### [Samples](#Samples)

* X:\images – If the web server is installed in a PC that is mapped with the X “drive” and the directory used to leave the static content is the “images” directory.
* C:\resin\doc\images – If the servlets engine is RESIN and it has been installed locally in the C:\resin directory. Besides, the folder “images” has been created and the images have been copied there.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691).


|  |
| --- |
| **Backlinks** |
| [HowTo: My first GeneXus Java Application](https://wiki.genexus.com/commwiki/wiki?45875) | [HowTo: My first GeneXus Java Application (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55769) |
| [Category:Java Generator Properties set per User](https://wiki.genexus.com/commwiki/wiki?13930) | [Manually configuring Tomcat](https://wiki.genexus.com/commwiki/wiki?21382) | [Tomcat path property](https://wiki.genexus.com/commwiki/wiki?48354) | [User Properties](https://wiki.genexus.com/commwiki/wiki?25111) |

---
