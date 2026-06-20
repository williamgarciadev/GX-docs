---
title: "Modules - Grammar"
source_id: 25609
source_url: https://wiki.genexus.com/commwiki/wiki?25609
genexus_version: "18"
---

# Modules - Grammar

An important feature of [Module object](https://wiki.genexus.com/commwiki/wiki?22411)s is that they allow the developer to define objects using the same [Name property](https://wiki.genexus.com/commwiki/wiki?6985). This introduces the disadvantage of ambiguity — how to call a specific object when its name is repeated. To overcome this disadvantage, the use of the [Qualified Name property](https://wiki.genexus.com/commwiki/wiki?22477) is required.

Take for example the following module organization:

`[imagen omitida: wiki id 22436]`

If "ObjectC" from "ModuleD" is to be called from an object belonging to the [Root module](https://wiki.genexus.com/commwiki/wiki?22439), the code below would be used:

```
ObjectC.Call()
```

but since there is ambiguity the following error will be displayed:

error: 'ObjectC' is ambiguous. There is a program name with the same name.

In order to make the call we must eliminate the ambiguity through the use of the Qualified Name property, as shown below:

```
ModuleA.ModuleD.ObjectC.Call()
```

Or it could be shorter, since in this example adding "ModuleD" is enough to identify the object to be called:

```
ModuleD.ObjectC.Call()
```

This will cause the ambiguity to disappear and the call will be made as desired.

See [How are partially qualified object names resolved](https://wiki.genexus.com/commwiki/wiki?22438) for further details on the automatic qualification rules applied when non qualified names are used.

It is important to clarify that the latter only happens when the name of the object is repeated.

See Also

* [Qualified Name property](https://wiki.genexus.com/commwiki/wiki?22477)
* [How are partially qualified object names resolved](https://wiki.genexus.com/commwiki/wiki?22438)


|  |
| --- |
| **Backlinks** |
| [Toc:Modules](https://wiki.genexus.com/commwiki/wiki?22414) | [Working with Modules](https://wiki.genexus.com/commwiki/wiki?25607) |

---
