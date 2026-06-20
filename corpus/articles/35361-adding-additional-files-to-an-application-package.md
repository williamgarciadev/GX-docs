---
title: "Adding additional files to an application package"
source_id: 35361
source_url: https://wiki.genexus.com/commwiki/wiki?35361
genexus_version: "18"
---

# Adding additional files to an application package

### [Introduction](#Introduction)

The [Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) is very smart on what files need to be packaged depending on the objects you want to deploy and the properties where objects are used. For instance if you're using [Web Notifications](https://wiki.genexus.com/commwiki/wiki?32302,,) in your application and have set some of the properties involved in the process, like [Received Handler](https://wiki.genexus.com/commwiki/wiki?33633), the generated files for the objects set in those properties are also included in the package.

But there are times when you need to add files that are not referenced by any object in your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836), in that case, you need to add additional files to the final package, and this document will show you how to do it.

### [Create files](#+Create+files)

GeneXus has the [File object](https://wiki.genexus.com/commwiki/wiki?5852) which is used for that exact reason. Let's say you're using a custom JDBC driver that you had to download yourself, or there's an external JAR you need for your application to work.

The File object allows you to keep that file in your knowledge base and using the [Extract property](https://wiki.genexus.com/commwiki/wiki?13280) so you don't have to worry about copying that file in new environments or share it with new users of your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836).

### [Add them to your deployment](#Add+them+to+your+deployment)

[File object](https://wiki.genexus.com/commwiki/wiki?5852) can now be added as a regular object in the Deployment tool dialog. That actual file associated with this GeneXus's [File](https://wiki.genexus.com/commwiki/wiki?5852) will be found in your application web folder, it should be already there if you already built something, and will be added to the exact same location in your package.

### [Sample](#Sample)

Let's say you need your app to work with a zip file called myFile.zip that need to be under a folder called 'MyStuff'.

1) First, you need to add this file to the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836)

2) Set the newly created [File](https://wiki.genexus.com/commwiki/wiki?5852)'s [Extract property](https://wiki.genexus.com/commwiki/wiki?13280) to MyStuff. This step will make GeneXus create the MyStuff folder under your web folder and copy the zip file there. You can also set if you want GeneXus to extract it always or only when there is a newer version of it.

3) Add the desired main object to deploy to the Deployment Tool Dialog (Build -> Deploy Application) and add also the required file (by default it will be called myFile\_zip)

4) Hit Deploy, and that's it. GeneXus will create your package creating the MyStuff folder and the myFile.zip inside of it.

### [See also](#See+also)

[Customize GeneXus Deployment capabilities](https://wiki.genexus.com/commwiki/wiki?45672)


|  |
| --- |
| **Backlinks** |
| [Toc:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Toc:Application Deployment tool (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54334) |

---
