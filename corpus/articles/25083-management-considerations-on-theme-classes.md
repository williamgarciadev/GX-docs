---
title: "Management considerations on Theme classes"
source_id: 25083
source_url: https://wiki.genexus.com/commwiki/wiki?25083
genexus_version: "18"
---

# Management considerations on Theme classes

As of [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?20247,,), Theme classes create [cross references](https://wiki.genexus.com/commwiki/wiki?24024,,), allowing the user and GeneXus to know which objects reference a given class. This new feature includes certain considerations to be taken into account when we work with Themes classes.

### [Creating a new Theme Class](#Creating+a+new+Theme+Class)

When we create a new class on a Theme, this new class will be added to all Themes, inheriting the corresponding parent class properties for each Theme. By default, this class is only visible on the same kind of Themes. For instance, if you create a new class on a Web Theme, it is only visible on the remaining Web Themes.

### [Updating a Theme Class](#Updating+a+Theme+Class)

When we update a Theme class:

* The name of the updated Theme class must be unique within the whole Knowledge Base. Otherwise, we would not be able to update it.
* The other properties only affect the current Theme.

### [Deleting a Theme Class](#Deleting+a+Theme+Class)

 When we want to delete a Theme class:

* The class must not be referenced by any control in our Knowledge Base.
* The properties of that class on every Theme must have the default value.

**Note:** When we try to delete a class that is not referenced by any control but has properties defined in other Themes, we will get the following message:

`[imagen omitida: wiki id 25309]`

The *Yes* option sets as default all the properties of the class in the current Theme. To delete the class from the Knowledge Base, we must go through every Theme and clean all properties for that class.

### [See Also](#See+Also)

* [Theme class cross reference](https://wiki.genexus.com/commwiki/wiki?24024,,)
* [References](https://wiki.genexus.com/commwiki/wiki?24910)
* [Class property](https://wiki.genexus.com/commwiki/wiki?8741)


|  |
| --- |
| **Backlinks** |
| [References](https://wiki.genexus.com/commwiki/wiki?24910) |

---
