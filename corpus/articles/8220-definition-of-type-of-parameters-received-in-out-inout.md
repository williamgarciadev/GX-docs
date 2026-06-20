---
title: "Definition of type of parameters received (in, out, inout)"
source_id: 8220
source_url: https://wiki.genexus.com/commwiki/wiki?8220
genexus_version: "18"
---

# Definition of type of parameters received (in, out, inout)

Each parameter declared in the [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862) can be defined to operate as:

* input parameter (specifying the **in** operator)
* output parameter (specifying the **out** operator)
* input and output parameter (specifying the **inout** operator)

When no operator is specified, it will depend on the following:

* If the object was called with [Call](https://wiki.genexus.com/commwiki/wiki?16224), the parameter behavior will be: **inout**.
* If the object was called with [Udp](https://wiki.genexus.com/commwiki/wiki?3964), and it's the last parameter, it will be an **out** parameter.

### [Syntax](#Syntax)

**parm(**[**out:**&var1**, in:**&var2**,** &var3, **inout:**&var4]**);**

Where:

*&var1, &var2, &var3, &var4:*  
Are -local and temporary- variables defined in the called object.

### Example

The following rule is declared in a procedure:

```
parm(out:&var1, in:&var2, &var3, inout:&var4);
```

So, note that:

&var1: Is an out parameter  
&var2: Is an in parameter  
&var3: Is an in-out parameter  
&var4: Is an in-out parameter

### [Advantages of defining operators](#Advantages+of+defining+operators)

Declaring explicitly each parameter behavior, you obtain the following advantages:

1. A better specification of the semantics of the interface. This means that the following will be understood:

* **inout**: the parameter comes with a value and after executing the called object, the resulting value is returned to the caller object.
* **in:** the parameter comes with a value and after executing the called object, the resulting value is not returned to the caller object. (\*)
* **out:** the parameter doesn't come with a value and after executing the called object, the resulting value is returned to the caller object.

2. Independence from generation languages. That is if you specify operators explicitly, whenever applications are generated using different generation languages, the behavior of the parameters will not change based on the default behavior of the corresponding generation language.

3. Input variables are also considered read-only. They will be read-only in the Layout, and if you try to change them in some way in the code, you get an SPC0022 warning in specification time.

### [Considerations](#Considerations)

The specifier will not allow specifying a program assigning values (in rules/source/events) to parameters defined as **in**.

(\*) When the variable is a complex type (such as a Business Component, Structured Data type, External Object) the parameter is passed by reference.

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Invocations between objects](https://training.genexus.com/en/learning/courses/genexus/v18/core/content/invocations-between-objects-6104721)  
`[imagen omitida: wiki id 20668]` [Invocations between objects (Cont.)](https://training.genexus.com/en/learning/courses/genexus/v18/core/content/invocations-between-objects-cont--6104739)


|  |
| --- |
| **Backlinks** |
| [API object Syntax](https://wiki.genexus.com/commwiki/wiki?50879) | [Calling a GeneXus generated program from other Environments](https://wiki.genexus.com/commwiki/wiki?21387) | [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) |
| [HowTo: Upload an image, video, or audio file via an API object](https://wiki.genexus.com/commwiki/wiki?51411) | [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862) | [RestPath annotation](https://wiki.genexus.com/commwiki/wiki?50360) |

---
