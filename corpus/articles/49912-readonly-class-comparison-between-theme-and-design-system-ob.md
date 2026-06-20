---
title: "Readonly Class Comparison between Theme and Design System Object"
source_id: 49912
source_url: https://wiki.genexus.com/commwiki/wiki?49912
genexus_version: "18"
---

# Readonly Class Comparison between Theme and Design System Object

In [HowTo: Set the style of a read-only Attribute/Variable control using DSO](https://wiki.genexus.com/commwiki/wiki?49906) it was shown how to define specific design features when an Attribute/Variable control is readonly and a Design System is being used as an object that gives a style to the classes of the object in which the control is located.

This solution addresses the problems that were caused when trying to implement the same requirement in a [Web Theme](https://wiki.genexus.com/commwiki/wiki?6420).

For the same case of the example: if you wanted to implement a MinorText class, you had to create a child of the Attribute class, name it as desired, and set the necessary properties. But when the subclass was created, four children were automatically created as well. One of them had the Readonly prefix in its name, and its Background color was changed to yellow.
