---
title: "Submit command"
source_id: 15386
source_url: https://wiki.genexus.com/commwiki/wiki?15386
genexus_version: "18"
---

# Submit command

Executes a program asynchronously. The main program flow will continue processing immediately.

### [Syntax](#Syntax)

**Submit(***pgm*, *submit-parms*[, *parm1*, … , *parmN*]**)**  
   
**Where:**  
  
*pgm*  
    Is the name of the GeneXus object or an external program to be called. If a GeneXus object is used, the only valid objects are Procedures that do not require screen (i.e. Asks and Confirms). If an external program is used, the name is a string and must be written between quotes or apostrophe. It cannot be a variable.  
   
*submit-parms*  
    This parameter is only used in [iSeries applications](https://wiki.genexus.com/commwiki/wiki?24383), all other generators will ignore the parameter.

*parm1, … , parmN*  
    Are optional parameters that can be sent to the called object with some purpose (and they must be received in the called object by declaring them with the [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862). These parameters can be attributes or variables. Expressions or constants are not supported.

### [Scope](#Scope)

**Objects:**[Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Work Panel](https://wiki.genexus.com/commwiki/wiki?7387,,)

**Notes:**

* In Java, a pool of threads is used, and it should be managed editing the client.cfg file and changing the SUBMIT\_POOL\_SIZE entry.
* For GeneXus 9.0 or higher versions, we recommend using the [Submit method](https://wiki.genexus.com/commwiki/wiki?24382).
* The Client WebSession is not available in the submit procedure.

### [See Also](#See+Also)

[Call command](https://wiki.genexus.com/commwiki/wiki?8260)  
[Call rule](https://wiki.genexus.com/commwiki/wiki?6849,,)  
[Submit rule](https://wiki.genexus.com/commwiki/wiki?15405,,)  
[iSeries Submit considerations](https://wiki.genexus.com/commwiki/wiki?24383)  
[VB Submit considerations](https://wiki.genexus.com/commwiki/wiki?24384,,)  
[Smart Devices Submit considerations](https://wiki.genexus.com/commwiki/wiki?28719,,)


|  |
| --- |
| **Backlinks** |
| [Call command](https://wiki.genexus.com/commwiki/wiki?8260) | [Commands in Procedures](https://wiki.genexus.com/commwiki/wiki?7924) | [Commands in Transactions](https://wiki.genexus.com/commwiki/wiki?8649) |
| [How To: Use a Progress Indicator in a Web Panel](https://wiki.genexus.com/commwiki/wiki?32779) | [iSeries Submit considerations](https://wiki.genexus.com/commwiki/wiki?24383) | [Kafka Producer and Consumer External Objects](https://wiki.genexus.com/commwiki/wiki?40593) |
|

---
