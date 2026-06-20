---
title: "Call command"
source_id: 8260
source_url: https://wiki.genexus.com/commwiki/wiki?8260
genexus_version: "18"
---

# Call command

Executes a GeneXus object or an external program synchronously.

**Note**: Use the [Call method](https://wiki.genexus.com/commwiki/wiki?16224) instead of this command, except for the case where you need to indicate the name of the called object in a variable.

### [Syntax](#Syntax)

**Call(***GeneXusObjectName*| '*pgm*' | *&var* | ATT:*Att*  [, *parm1*, …, parmN] **)**

#### [**Where:**](#Where%3A)

*GeneXusObjectName*Is the name of the [GeneXus object](https://wiki.genexus.com/commwiki/wiki?1866) to be called.

'*pgm*'  
   Is the name of the external program to be called. Use apostrophes or quotes.

*&var*  
   Is a variable based on the character data type that contains the name of the GeneXus object to be called.

*Att*  
   Is an attribute based on the character data type that contains the name of the GeneXus object be called, ATT: is a [prefix](https://wiki.genexus.com/commwiki/wiki?19922) that must be used.

*parm1, …, parmN*  
   Are optional parameters that can be sent to the called object with some purpose (and they must be received in the called object by declaring them with the [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862).

### [Scope](#Scope)

**Objects:**[Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Work Panel](https://wiki.genexus.com/commwiki/wiki?7387,,)

### [Samples](#Samples)

**1)** Calling a GeneXus object (without sending parameters to it)

```
Call(CustomInfo)
```

**2)** Calling an external program (without sending parameters to it)

```
Call('ExtPrg')
```

Check the considerations section for further detail.

**3)** Calling a GeneXus object, but the object name is loaded in an attribute (Att is the name of the attribute defined in the KB). Two parameters are sent to the called object.

```
Call(ATT:Att, parm1, parm2, …)
```

Check the considerations section for further detail.

**4)** Calling a GeneXus object, but the object name is loaded in a variable. Two parameters are sent to the called object.

```
Call(&var, parm1, parm2, …)
```

### [Dynamic Call considerations](#Dynamic+Call+considerations)

* The object name must exactly match the target object name; otherwise, you will get a runtime error. For example: in Java, all classes are generated as lowercase so you will need to set the Dynamic call as lowercase.
* Do not use an expression for the first parameter in the Dynamic call, it only supports a variable or attribute name containing the object name.
* Dynamic Calls to web objects are not supported in Procedures and Data Providers. Use for that the [Link command](https://wiki.genexus.com/commwiki/wiki?8446). (More information at [SAC 47097](https://www.genexus.com/en/developers/websac?data=47097;;))

### See Also

[Call method](https://wiki.genexus.com/commwiki/wiki?16224)  
[Call rule](https://wiki.genexus.com/commwiki/wiki?6849,,)  
[Submit command](https://wiki.genexus.com/commwiki/wiki?15386)  
[Submit rule](https://wiki.genexus.com/commwiki/wiki?15405,,)  
[Link command](https://wiki.genexus.com/commwiki/wiki?8446)  
[Parm rule](https://wiki.genexus.com/commwiki/wiki?6862)  
[Significant object name length property](https://wiki.genexus.com/commwiki/wiki?7250)  
[Expand dynamic calls property](https://wiki.genexus.com/commwiki/wiki?8569)  
[Prefixes to use when calling and having to indicate explicitly certain definitions](https://wiki.genexus.com/commwiki/wiki?19922)


|  |
| --- |
| **Backlinks** |
| [Call Variable](https://wiki.genexus.com/commwiki/wiki?17489) | [Code Snippets](https://wiki.genexus.com/commwiki/wiki?10662) | [Commands in Procedures](https://wiki.genexus.com/commwiki/wiki?7924) |
| [Commands in Transactions](https://wiki.genexus.com/commwiki/wiki?8649) | [Dynamic Calls in Smart Devices](https://wiki.genexus.com/commwiki/wiki?17411) | [Expand dynamic calls property](https://wiki.genexus.com/commwiki/wiki?8569) | [GeneXus Cognitive API - Train procedure](https://wiki.genexus.com/commwiki/wiki?44246) |
| [HowTo: Create a Code Snippet](https://wiki.genexus.com/commwiki/wiki?10725) | [Link command](https://wiki.genexus.com/commwiki/wiki?8446) | [Modules - Dynamic calls](https://wiki.genexus.com/commwiki/wiki?22585) | [Parameters Style property for Environments](https://wiki.genexus.com/commwiki/wiki?46404) |
| [Procedures as REST: Sending blob data as input to the procedure](https://wiki.genexus.com/commwiki/wiki?15316) | [Single Page Applications](https://wiki.genexus.com/commwiki/wiki?22455) | [SRC Error Codes and messages](https://wiki.genexus.com/commwiki/wiki?38589) | [Submit command](https://wiki.genexus.com/commwiki/wiki?15386) |
| [Transitions for Web](https://wiki.genexus.com/commwiki/wiki?22460) | [Type Property](https://wiki.genexus.com/commwiki/wiki?43861) |

---
