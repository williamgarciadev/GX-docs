---
title: "GeneXus Generators (GeneXus 18 Upgrade 5 or prior)"
source_id: 55944
source_url: https://wiki.genexus.com/commwiki/wiki?55944
genexus_version: "18"
---

# GeneXus Generators (GeneXus 18 Upgrade 5 or prior)

A GeneXus Generator generates code in a programming language.

For each [Environment](https://wiki.genexus.com/commwiki/wiki?7115) you create in your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836), you have to select:

1. One GeneXus Generator to generate the code corresponding to the application's **Back end** (it is automatically named "Default").
2. One or more GeneXus Generators to generate the code corresponding to the application's **Front end**.

`[imagen omitida: wiki id 55861]`

Later, in addition to having a "Default" Generator to generate the application's back-end code, eventually, you can add more Generators (usually known as "Secondary" Generators) to generate, for example, certain objects with Java and others, like some batch processes, in RPG).

The "Default" Generator is also used to generate the programs to create/modify the database structure (that is to say, the [Reorganization](https://wiki.genexus.com/commwiki/wiki?5288) programs).

The [Preferences window](https://wiki.genexus.com/commwiki/wiki?7109) shows, for each environment, a **Back end** node and a **Front end** node with, among other things, their Generators. The symbol pointed out indicates the Reorganization Generator:

`[imagen omitida: wiki id 55864]`

The Reorganization Generator can be changed (if needed). There are two ways to do it:

1. By updating the Environment [Reorganization Generator property](https://wiki.genexus.com/commwiki/wiki?13605) value.
2. By right-clicking on one of the Environment Generators and selecting the "Set As Reog Generator" option:

`[imagen omitida: wiki id 55866]`

To add a Secondary Generator, right-click on the **Back end** node and select the "New Generator" option:

`[imagen omitida: wiki id 46825]`

A Secondary Generator can be set as the Reorganization Generator of the Environment.

Moreover, as mentioned above, it is possible to generate certain objects with a Generator and other objects with different Generators. To do so, each [Main Object](https://wiki.genexus.com/commwiki/wiki?5770) can be associated with a Generator (Default, Secondary, or Reorganization) that defines the target language to generate. The [Generator property](https://wiki.genexus.com/commwiki/wiki?7957) of each main object indicates the Generator with which GeneXus will build it and any object of its main call tree. Note that an object can be called by more than one main object, so it can be generated with different Generators.
