---
title: "GeneXus Generators"
source_id: 7116
source_url: https://wiki.genexus.com/commwiki/wiki?7116
genexus_version: "18"
---

# GeneXus Generators

A GeneXus Generator generates code in a programming language.

For each [Environment](https://wiki.genexus.com/commwiki/wiki?7115) you create in your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836), you have to select:

1. One GeneXus Generator to generate the code corresponding to the application's **Back end** (it is automatically named "Default").
2. One or more GeneXus Generators to generate the code corresponding to the application's **Front end**.

`[imagen omitida: wiki id 55861]`

Later, in addition to having a "Default" Generator to generate the application's back-end code, eventually, you can add more Generators (usually known as "Secondary" Generators) to generate, for example, certain objects with Java and others, like some batch processes, in RPG).

The "Default" Generator is also used to generate the programs to create/modify the database structure (that is to say, the [Reorganization](https://wiki.genexus.com/commwiki/wiki?5288) programs).

The [Preferences window](https://wiki.genexus.com/commwiki/wiki?7109) shows, for each Environment, a **Back end** node and a **Front end** node with, among other things, their Generators. The symbol pointed out indicates the Reorganization Generator:

`[imagen omitida: wiki id 55864]`

The Reorganization Generator can be changed (if needed). There are two ways to do it:

1. By updating the Environment [Reorganization Generator property](https://wiki.genexus.com/commwiki/wiki?13605) value.
2. By right-clicking on one of the Environment Generators and selecting the "Set As Reog Generator" option:

`[imagen omitida: wiki id 55945]`

To add a Secondary Generator, right-click on the **Back end** node and select the "New Generator" option:

`[imagen omitida: wiki id 46825]`

A Secondary Generator can be set as the Reorganization Generator of the Environment.

Moreover, for a Secondary Generator, you can change its language by clicking on it and selecting the "Change Generator" option:

`[imagen omitida: wiki id 55946]`

The "Change Generator" option is not valid for the "Default" Generator. To change the "Default" Generator values you have to edit the Environment properties.

Finally, as mentioned above, it is possible to generate certain objects with a Generator and other objects with different Generators. To do so, each [Main Object](https://wiki.genexus.com/commwiki/wiki?5770) can be associated with a Generator (Default, Secondary, or Reorganization) that defines the target language to generate. The [Generator property](https://wiki.genexus.com/commwiki/wiki?7957) of each main object indicates the Generator with which GeneXus will build it and any object of its main call tree. Note that an object can be called by more than one main object, so it can be generated with different Generators.


|  |
| --- |
| **Sub Categories** |
| [Category:GeneXus .NET Framework Generator](https://wiki.genexus.com/commwiki/wiki?2892) | [Category:GeneXus .NET Generator](https://wiki.genexus.com/commwiki/wiki?38604) | [Category:GeneXus .NET Generator (GeneXus 18 Upgrade 6)](https://wiki.genexus.com/commwiki/wiki?57219) |
| [Category:GeneXus Angular Generator](https://wiki.genexus.com/commwiki/wiki?42550) | [Category:GeneXus iSeries Applications](https://wiki.genexus.com/commwiki/wiki?9296) | [Category:GeneXus Java Generator](https://wiki.genexus.com/commwiki/wiki?12258) |
| [Category:GeneXus Ruby Generator](https://wiki.genexus.com/commwiki/wiki?5353,Category%3AGeneXus+Ruby+Generator,) | [Category:GeneXus Visual FoxPro Generator](https://wiki.genexus.com/commwiki/wiki?10302,Category%3AGeneXus+Visual+FoxPro+Generator,) | [Category:Native Mobile Generator](https://wiki.genexus.com/commwiki/wiki?14451) |

---

|  |
| --- |
| **Pages** |
| [Chatbot generator](https://wiki.genexus.com/commwiki/wiki?37102) | [GeneXus 15 Web Generators](https://wiki.genexus.com/commwiki/wiki?31726,GeneXus+15+Web+Generators,) |

---
