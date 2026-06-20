---
title: "How does GeneXus decide which generator to use when generating an object"
source_id: 7853
source_url: https://wiki.genexus.com/commwiki/wiki?7853
genexus_version: "18"
---

# How does GeneXus decide which generator to use when generating an object

Each main object can indicate the generator to use for generation (if this information is not provided, the primary generator is always used). This is done indirectly, instead of exactly indicating the generator, an order is defined for the model. For example, the second generator for the model is indicated instead of "C/SQL".

Although this solution can be a little more complex to understand, it has some advantages: you can change a generator for a model and there is no need to modify each object information, and you can have different generators for the same object in different models. For example, if you have a knowledge base with a Client/Server model on an RS/6000 and another model for the iSeries, in the first model, the secondary generator is C# and Java in the second model. You can define all batch programs so that they use the model's secondary generator. This way, the first model will use C# and the second model will use Java.

If the generator number indicated in the object does not exist, the primary generator is used. This is very useful for prototyping. For example, if there is a Main object called X and its generator is C#, when generating in a model where C# is not available, the model’s primary generator is used instead (i.e.: we are prototyping in Visual FoxPro).

For all objects that are not main, the generators of the main objects that call them (directly or indirectly) are used. Because an object can be called by many Main objects and each of them can have a different generator, the same object can be generated with more than one generator in the same model. For example, if X is a main object with C# generator and Y is another main object with VFP generator, and both of them call object Z, then Z will be generated with C# (for the case when it is called by object X) and with VFP (for the case when it is called by object Z).
